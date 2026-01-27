<!--
  Game Card Component

  This component displays information about a single game.
  -->

<script lang="ts">
  import Fa from 'svelte-fa';
  import { faPaperPlane, faUser } from '@fortawesome/free-regular-svg-icons';
  import { faPlus, faCircleInfo, faChartSimple } from '@fortawesome/free-solid-svg-icons';
  import { faSteam } from '@fortawesome/free-brands-svg-icons';

  import type { Game } from '$lib/types/game';
  
  let { game }: { game: Game } = $props();

  </script>

<div class="card">
  <!--
    Game cover image.
    Alt text describes the image for accessibility and SEO.
  -->
  <img src={game.cover_url} alt="Cover art for {game.title}" />

  <div class="content">
    <header>
      <h2>
        {game.title}      
      </h2>

      <!--
        Action icons (share, add to wishlist, more info).
        These are placeholders - they would need click handlers to be functional.
      -->
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
      {game.description}
    </div>

    <!--
      Platform availability icons.
      Shows which platforms the game is available on (Steam, PlayStation, etc.).
    -->
    <div class="platforms">
      <ul>
        <li>
          <!-- Steam icon - should conditionally show based on game.platforms.steam -->
          <Fa icon={faSteam} />
        </li>
      </ul>
    </div>
  </div>
</div>

<style lang="scss">
  @use '$lib/styles/variables';

  .card {
    background-color: variables.$secondary;
    height: 30%;
    width: 90%;
    display: flex; /* Arrange image and content side by side */
    justify-content: left;
    border: none;
    margin: 20px 30px; /* Space between cards */
  }

  /**
   * Game cover image styling.
   * Takes up 30% of the card width.
   */
  .card > img {
    width: 30%;
    left: 0;
    border: none;
  }

  /**
   * Content area (everything except the image).
   * Uses flexbox column layout to stack sections vertically.
   */
  .content {
    width: auto;
    display: flex;
    flex-direction: column; /* Stack sections vertically */
    justify-content: space-between; /* Distribute space evenly */
    background-color: variables.$secondary;
    border: none;
  }

  /**
   * Header section styling.
   * Displays title on left and action icons on right.
   */
  .content > header {
    display: flex;
    justify-content: space-between; /* Push title left and icons right */
    width: 100%;
    display: flex;
    flex-direction: row;
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    min-height: 250px;
  }

  /**
   * Platform icons section at the bottom of the card.
   * Aligned to the right side.
   */
  .platforms {
    background-color: variables.$secondary;
    border: none;
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
    justify-content: start; /* Align to left */
    background-color: variables.$secondary;
    border: none;
    font-size: 1rem;
    padding-left: 1rem;
  }

  /**
   * Player count display.
   * Shows icon and text horizontally.
   */
  .number-players {
    display: flex;
    align-items: center; /* Vertically center icon and text */
    border: none;
    background-color: variables.$secondary;
    gap: 0.5rem; /* Space between icon and text */
    padding-right: 2.5rem; /* Space before review score */
    justify-content: start;
  }

  /**
   * Review score display.
   * Shows icon and text horizontally.
   */
  .review-score {
    display: flex;
    align-items: center; /* Vertically center icon and text */
    height: 30px;
    background-color: variables.$secondary;
    border: none;
    gap: 0.5rem; /* Space between icon and text */
    width: 300px;
    justify-content: start;
  }

  /**
   * Game description text.
   * Limited width to prevent overly long lines.
   */
  .description {
    background-color: variables.$secondary;
    border: none;
    font-size: 1rem;
    padding-left: 1rem;
    width: 88%;
    align-self: start;
  }
</style>
