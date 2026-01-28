<!--
  Main Layout Component

  This layout wraps all pages in the application.
  Whatever we put here will appear on every page.
-->

<script lang="ts">
  import '../app.scss';
  import Nav from '$lib/components/Nav.svelte';
  import FilterBar from '$lib/components/FilterBar.svelte'; // Import the new filter bar
<<<<<<< HEAD
  import favicon from '$lib/assets/favicon.svg';
=======
>>>>>>> 14924a13a87b61b9c81dac8a1ae23676a18f5292

  let { children } = $props();
</script>

<svelte:head>
  <link rel="icon" href="/favicon.svg" />
</svelte:head>

<div class="app-container">
  <Nav />
  
  <FilterBar />

  <main>
    {@render children()}
  </main>
</div>

<style>
  .app-container {
    display: block; 
    width: 100%;
  }

  main {
    margin-top: 130px; /* Accounts for both Nav and FilterBar height */
    padding: 20px;
    
    /* Center the content horizontally */
    display: flex;
    flex-direction: column;
    align-items: center; 
    width: 100%;
    box-sizing: border-box;
  }
</style>
