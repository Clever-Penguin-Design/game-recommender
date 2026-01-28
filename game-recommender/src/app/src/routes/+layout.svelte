<!--
  Main Layout Component

  This layout wraps all pages in the application.
  Whatever we put here will appear on every page.
-->

<script lang="ts">
  import '../app.scss';
  import Nav from '$lib/components/Nav.svelte';
  import favicon from '$lib/assets/favicon.svg';

  let { children } = $props();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<div class="app-container">
  <Nav />
  <main>
    {@render children()}
  </main>
</div>

<style>
  .app-container {
    display: flex;
    flex-direction: column; [cite_start]/* Stacks Nav on top of Main content [cite: 53] */
  }

  main {
    margin-top: 70px; [cite_start]/* Prevents top bar from covering content [cite: 53] */
    width: 100%;      [cite_start]/* Takes full width now that sidebar is gone [cite: 53] */
  }
</style>
