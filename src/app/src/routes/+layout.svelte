<!--
  Main Layout Component

  This layout wraps all pages in the application.
  Whatever we put here will appear on every page.
-->

<script lang="ts">
  import '../app.scss';
  import Nav from '$lib/components/Nav.svelte';
  import FilterBar from '$lib/components/FilterBar.svelte'; // Import the new filter bar

  let { children } = $props();
</script>

<svelte:head>
  <link rel="icon" href="/favicon.svg" />
</svelte:head>

<div>
  <Nav />
  
  <FilterBar />

  <main>
    {@render children()}
  </main>
</div>

<style>
  main {

    margin-top: 15px; 

    padding: 0 20px 20px 20px; 

    display: flex;
    flex-direction: column;
    align-items: center; 
    width: 100%;
    box-sizing: border-box; 
  }
</style>
