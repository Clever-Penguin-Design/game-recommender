<!--
  Cards Container Component with Infinite Scroll

  This is the main component that displays the list of game cards.
  It handles:
  - Fetching initial game data when the component loads
  - Implementing infinite scroll to load more games as you scroll down
  - Managing loading states and errors
  - Displaying the footer when all games are loaded

  How infinite scroll works:
  1. We listen to the window's scroll event
  2. When the user scrolls near the bottom (within 200px), we fetch more games
  3. New games are appended to the existing list
  4. The process repeats until all games are loaded
-->

<script lang="ts">
  import { onMount } from 'svelte';
  import { games, loading, error, currentPage, hasMoreGames } from '$lib/stores/games';
  import { fetchGames } from '$lib/api/games';
  import Card from './Card.svelte';
  import Footer from './Footer.svelte';

  let isFetching = false;

  async function loadInitialGames() {
    try {
      $loading = true;
      const response = await fetchGames(1);
      $games = response.data;
      $error = null;
    } catch (err) {
      $error = err instanceof Error ? err.message : 'An unknown error occurred';
    } finally {
      $loading = false;
    }
  }

  async function loadMoreGames() {
    if (isFetching || $loading || !$hasMoreGames) return;

    try {
      isFetching = true;
      $loading = true;
      $currentPage += 1;
      const response = await fetchGames($currentPage);
      if (response.data && response.data.length > 0) {
        $games = [...$games, ...response.data];
        if (response.data.length < 10) $hasMoreGames = false;
      } else {
        $hasMoreGames = false;
      }
      $error = null;
    } catch (err) {
      $error = err instanceof Error ? err.message : 'An unknown error occurred';
    } finally {
      $loading = false;
      isFetching = false;
    }
  }

  function handleScroll() {
    const scrollHeight = document.documentElement.scrollHeight;
    const scrollTop = window.scrollY;
    const clientHeight = window.innerHeight;
    const distanceFromBottom = scrollHeight - (scrollTop + clientHeight);

    if (distanceFromBottom < 200 && $hasMoreGames && !isFetching && !$loading) {
      loadMoreGames();
    }
  }

  onMount(() => {
    loadInitialGames();
  });
</script>

<svelte:window on:scroll={handleScroll} />

<section class="cards">
  {#each $games as game (game.id)}
    <Card {game} />
  {/each}

  {#if $loading}
    <p>Loading...</p>
  {/if}

  {#if !$hasMoreGames && !$loading}
    <Footer />
  {/if}

  {#if $error}
    <p class="error">Error: {$error}</p>
  {/if}
</section>

<style lang="scss">
  .cards {
    margin-left: auto; 
    width: 85%;
    display: flex;
    flex-direction: column;
    list-style: none; 
  }

  :global(.cards li) {
    list-style-type: none !important;
  }

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
