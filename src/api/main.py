from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from datetime import date
from uuid import uuid4
from models import Game
from database import Database
from services.rawg_client import RawgClient

# Create the FastAPI application instance
# This is the main entry point for your API
app = FastAPI()
rawg_client = RawgClient()

# Configure CORS (Cross-Origin Resource Sharing)
# This allows your frontend (running on localhost:5173) to make requests
# to your backend API (running on localhost:8000)
#
# Without this, browsers block cross-origin requests for security reasons.
# This is safe for local development, but in production you should
# specify only the domains that should have access to your API.
app.add_middleware(
    CORSMiddleware,
    # allow_origins: List of origins that can access the API
    # ["*"] would allow ALL origins (not recommended for production)
    # For now, we only allow our local frontend
    allow_origins=["http://localhost:5173"],
    # allow_credentials: Allow cookies and authentication headers
    allow_credentials=True,
    # allow_methods: Which HTTP methods are allowed (GET, POST, PUT, DELETE, etc.)
    # ["*"] allows all methods
    allow_methods=["*"],
    # allow_headers: Which HTTP headers can be sent in requests
    # ["*"] allows all headers
    allow_headers=["*"],
)

# Create database instance
# This handles all database connections and sessions
db = Database()

# Constants
OBJECTS_PER_PAGE = 10

# GET /api/games
# Query Params
#  - page <int> required
@app.get("/api/games")
async def index(page_number: int = 10):
    # TODO: Uncomment once we are ready to serve live data from the DB.
    # with db.create_session() as session:
    #     statement = select(Game).limit(OBJECTS_PER_PAGE)
    #     results = session.exec(statement)
    #     games = results.all()

    try:
        raw_games = await rawg_client.get_games(page=page_number)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Map RAWG fields to your API format
    games = []
    for g in raw_games:
        games.append({
            "id": str(uuid4()),
            "title": g.get("name"),
            "description": g.get("slug") or "",
            "release_date": g.get("released"),
            "review_score": g.get("metacritic") or 0,
            "platforms": {p["platform"]["name"].lower().replace(" ", "_"): True for p in g.get("platforms", [])},
            "player_count": 1,
            "cover_url": g.get("background_image"),
        })

    return {"data": games}
