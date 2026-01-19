<!--
  Main Layout Component

  This layout wraps all pages in the application.
  Whatever we put here will appear on every page.
-->

<script lang="ts">
  import '../app.scss';
  import Nav from '$lib/components/Nav.svelte';

  let { children } = $props();
</script>

<svelte:head>
  <link rel="icon" href="/favicon.svg" />
</svelte:head>

<div>
  <Nav />
  <main>
    {@render children()}
  </main>
</div>

<style>
  
</style>
