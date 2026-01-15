<!--
  Cards Container Component with Infinite Scroll

  This component displays the list of game cards and handles:
  - Fetching initial game data when the component loads
  - Implementing infinite scroll to load more games as you scroll down
  - Managing loading states and errors
  - Displaying the footer when all games are loaded
-->

<script lang="ts">
  import { onMount } from 'svelte';
  import { fetchGames } from '$lib/api/games';
  import type { Game } from '$lib/types/game';
  import Card from './Card.svelte';
  import Footer from './Footer.svelte';

  // Local state using Svelte 5 runes
  let games: Game[] = $state([]);
  let loading = $state(true);
  let error: string | null = $state(null);
  let currentPage = $state(1);
  let hasMoreGames = $state(true);
  let isFetching = $state(false);

  async function loadInitialGames() {
    try {
      loading = true;
      const response = await fetchGames(1);
      games = response.data;
      error = null;
    } catch (err) {
      error = err instanceof Error ? err.message : 'An unknown error occurred';
      console.error('Error loading initial games:', err);
    } finally {
      loading = false;
    }
  }

  async function loadMoreGames() {
    if (isFetching || loading || !hasMoreGames) {
      return;
    }

    try {
      isFetching = true;
      loading = true;
      currentPage += 1;

      const response = await fetchGames(currentPage);

      if (response.data && response.data.length > 0) {
        games = [...games, ...response.data];

        if (response.data.length < 10) {
          hasMoreGames = false;
        }
      } else {
        hasMoreGames = false;
      }

      error = null;
    } catch (err) {
      error = err instanceof Error ? err.message : 'An unknown error occurred';
      console.error('Error loading more games:', err);
    } finally {
      loading = false;
      isFetching = false;
    }
  }

  function handleScroll() {
    const scrollHeight = document.documentElement.scrollHeight;
    const scrollTop = window.scrollY;
    const clientHeight = window.innerHeight;
    const distanceFromBottom = scrollHeight - (scrollTop + clientHeight);

    if (distanceFromBottom < 200 && hasMoreGames && !isFetching && !loading) {
      loadMoreGames();
    }
  }

  onMount(() => {
    loadInitialGames();
  });
</script>

<svelte:window onscroll={handleScroll} />

<section class="cards">
  {#each games as game (game.id)}
    <Card {game} />
  {/each}

  {#if loading}
    <p>Loading...</p>
  {/if}

  {#if !hasMoreGames && !loading}
    <Footer />
  {/if}

  {#if error}
    <p class="error">Error: {error}</p>
  {/if}
</section>

<!--
  Component-specific styles.
-->
<style lang="scss">
  .cards {
    margin-left: auto; 
    width: 85%; 
    
    /* 1. Remove dots if Card.svelte uses <li> tags */
    display: flex;
    flex-direction: column;
    list-style: none; 
  }

  /* 2. This forces any list items inside the container to hide their dots */
  :global(.cards li) {
    list-style-type: none !important;
  }

  /* 3. This catches any default browser padding that pushes icons to the right */
  :global(.cards ul) {
    padding: 0;
    margin: 0;
    list-style: none;
  }

  .error {
    color: #ff6b6b;
    padding: 1rem;
    text-align: center;
    font-weight: bold;
  }
</style>
