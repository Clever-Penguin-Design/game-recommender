<!--
  Game Card Component

  This component displays information about a single game.
  It shows:
  - Game cover image
  - Title and ID
  - Action icons (share, add to list, more info)
  - Number of players
  - Review score
  - Short description
  - Platform availability icons

  Props:
  - game: The game object containing all the game's information
-->
<script lang="ts">
  import Fa from 'svelte-fa';
  import { faPaperPlane, faUser } from '@fortawesome/free-regular-svg-icons';
  import { faPlus, faCircleInfo, faChartSimple } from '@fortawesome/free-solid-svg-icons';
  import { faSteam } from '@fortawesome/free-brands-svg-icons';
  import type { Game } from '$lib/types/game';

  let { game }: { game: Game } = $props();

  const placeholderImage =
    'https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80';
</script>

<div class="card">
  <div class="image-container">
    <img src={placeholderImage} alt="Cover art for {game.title}" />
  </div>

  <div class="content">
    <header>
      <h2>{game.title} #{game.id}</h2>
      <ul class="card-header-icons">
        <li><Fa icon={faPaperPlane} style="color: #fafafa" /></li>
        <li><Fa icon={faPlus} /></li>
        <li><Fa icon={faCircleInfo} /></li>
      </ul>
    </header>

    <div class="info">
      <div class="number-players">
        <Fa icon={faUser} />
        <p>1-4 Players</p>
      </div>
      <div class="review-score">
        <Fa icon={faChartSimple} />
        <p>Review Score {game.review_score || 'N/A'}</p>
      </div>
    </div>

    <div class="description">
      {game.description || 'No description available for this game.'}
    </div>

    <div class="platforms">
      <Fa icon={faSteam} />
    </div>
  </div>
</div>

<style lang="scss">
  @use '$lib/styles/variables';

  .card {
    background-color: variables.$secondary-color;
    width: 100%;
    display: flex;
    flex-direction: row;
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    min-height: 250px;
  }

  .image-container {
    width: 25%;
    min-width: 200px;
    max-width: 300px;
    
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  .content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 2rem;
  }

  header {
    display: flex;
    align-items: center;
    width: 100%;

    h2 {
      font-size: 1.6rem;
      margin: 0;
      color: white;
    }

    .card-header-icons {
      display: flex;
      gap: 15px;
      list-style: none;
      margin: 0;
      padding: 0;
      /* Pushes icons to the far right */
      margin-left: auto; 
    }
  }

  .info {
    display: flex;
    align-items: center;
    width: 100%;
    color: white;

    .number-players {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .review-score {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      /* Pushes review score to the far right */
      margin-left: auto; 
    }
  }

  .description {
    width: 100%;
    color: rgba(255, 255, 255, 0.8);
    margin: 1rem 0;
  }

  .platforms {
    display: flex;
    justify-content: flex-end;
    width: 100%;
    font-size: 1.5rem;
  }
</style>
