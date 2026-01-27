<script lang="ts">
  import Fa from "svelte-fa";
  import { faHouse, faGamepad, faPen, faMagnifyingGlass, faXmark } from "@fortawesome/free-solid-svg-icons";
  import Avatar from "./Avatar.svelte";
  import logo from "$lib/assets/img/logo.jpg";

  let searchQuery = ""; 

  /**
   * Navigation menu items.
   * Each item has a label, an icon, and a route path.
   * This makes it easy to add or modify menu items in the future.
   */
  const navItems = [
    { label: "Home", icon: faHouse, path: "/" },
    { label: "My Games", icon: faGamepad, path: "/my-games" },
    { label: "Wishlist", icon: faPen, path: "/wishlist" }
  ];

  function clearSearch() {
    searchQuery = "";
  }
</script>

<nav>
  <!--
    App logo at the top of the nav.
    Alt text is important for accessibility - screen readers will read this
    description to users who can't see the image.
  -->
  <img src="/img/logo.jpg" alt="Game Recommender logo" />

  <div class="search-wrapper">
    <div class="search-container">
      <Fa icon={faMagnifyingGlass} class="search-icon" />
      <input 
        type="text" 
        placeholder="Search games..." 
        bind:value={searchQuery} 
      />
      {#if searchQuery.length > 0}
        <button class="clear-btn" on:click={clearSearch} aria-label="Clear search">
          <Fa icon={faXmark} />
        </button>
      {/if}
    </div>
  </div>

  <div class="side-section right">
    <Avatar />
  </div>
</nav>

<style lang="scss">
  @use '$lib/styles/variables';

  /**
   * Style the FontAwesome icons to be white.
   * This is a global class that applies to all icons in this component.
   */
  :global(.font-awesome-icon) {
    color: variables.$white;
  }

  /**
   * Main navigation container.
   *
   * This is fixed to the left side of the screen and takes up 15% of the width.
   * It uses flexbox to arrange its children (logo, menu, avatar) vertically.
   */
  nav {
    background-color: variables.$primary-accent;
    padding-top: 4rem; /* Space at the top for breathing room */
    display: flex;
    flex-direction: column; /* Stack children vertically */
    align-items: center; /* Center children horizontally */
    border-right: 1px solid variables.$secondary-accent; /* Separates nav from main content */
    position: fixed; /* Stays in place when scrolling */
    height: 100vh; /* Full viewport height */
    width: 15%; /* Takes up 15% of screen width */
  }

  .side-section {
    display: flex;
    align-items: center;
    flex: 1; /* Occupies equal space as the right side to keep center true */
    
    &.right {
      justify-content: flex-end;
    }
  }

  .nav-logo {
    height: 30px;
    width: auto;
  }

  .nav-links {
    display: flex;
    flex-direction: row;
    gap: 1.5rem;
    list-style: none;
    margin-left: 2rem;
    padding: 0;
  }

  .search-wrapper {
    display: flex;
    justify-content: center;
    flex: 2; /* Provides more space for the search bar in the center */
  }

  .search-container {
    display: flex;
    align-items: center;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 5px 15px;
    width: 100%;
    max-width: 400px; 
    border: 1px solid rgba(255, 255, 255, 0.2);
  }

  input {
    background: transparent;
    border: none;
    color: white;
    margin-left: 10px;
    outline: none;
    width: 100%;
    font-size: 0.85rem;
    
    &::placeholder { 
      color: rgba(255, 255, 255, 0.5); 
    }
  }

  .clear-btn {
    background: none;
    border: none;
    color: rgba(255, 255, 255, 0.5);
    cursor: pointer;
    display: flex;
    align-items: center;

    &:hover { 
      color: white; 
    }
  }

  li {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    color: white;
    font-size: 0.85rem;
    white-space: nowrap;
    cursor: pointer;

    &:hover { 
      opacity: 0.8; 
    }
  }

  :global(.search-icon) {
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.8rem;
  }
</style>
