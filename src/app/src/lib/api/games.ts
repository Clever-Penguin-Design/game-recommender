/**
 * API Client for Game Data
 *
 * This file contains functions that communicate with our backend API
 * to fetch game data. By centralizing API calls here, we can:
 * 1. Reuse the same code across different components
 * 2. Handle errors in a consistent way
 * 3. Easily update the API endpoint if it changes
 */

import { env } from "$env/dynamic/public";
import type { GamesApiResponse } from "$lib/types/game";
/**
 * The base URL for our backend API.
 *
 * This is read from the PUBLIC_API_URL environment variable, which allows
 * the app to work in different environments:
 * - Local development: http://127.0.0.1:8000 (or localhost:8000)
 * - Docker: http://backend:8000 (using Docker service name)
 * - Production: Your deployed backend URL
 *
 * The environment variable is set in:
 * - Local: .env file in src/app/
 * - Docker: compose.yaml file
 *
 * If the env var is not defined, we use the default FastAPI localhost port.
 */
const BASE_URL = `${env.PUBLIC_API_URL ?? "http://localhost:8000"}/api/games`;

export async function fetchGames(
  pageNumber: number,
): Promise<GamesApiResponse> {
  try {
    const response = await fetch(`${BASE_URL}?page_number=${pageNumber}`);

    // Check if the request was successful
    if (!response.ok) {
      throw new Error(`HTTP error: The status is ${response.status}`);
    }

    const data: GamesApiResponse = await response.json();

    return data;
  } catch (error) {
    // If anything goes wrong (network error, bad response, etc.),
    // we throw a new error with a helpful message
    console.error("Error fetching games:", error);
    throw new Error(
      `Failed to fetch games: ${error instanceof Error ? error.message : "Unknown error"}`,
    );
  }
}
