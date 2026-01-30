<script lang="ts">
  import Fa from "svelte-fa";
  import { faHouse, faGamepad, faPen, faMagnifyingGlass, faXmark } from "@fortawesome/free-solid-svg-icons";
  import Avatar from "./Avatar.svelte";

  let searchQuery = $state("");

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
  <div class="side-section left">
    <img src="/img/logo.jpg" alt="Game Recommender logo" class="nav-logo" />
    <ul class="nav-links">
      {#each navItems as item (item.path)}
        <li>
          <Fa icon={item.icon} class="font-awesome-icon" fw />
          {item.label}
        </li>
      {/each}
    </ul>
  </div>

  <div class="search-wrapper">
    <div class="search-container">
      <Fa icon={faMagnifyingGlass} class="search-icon" />
      <input
        type="text"
        placeholder="Search games..."
        bind:value={searchQuery}
      />
      {#if searchQuery.length > 0}
        <button class="clear-btn" onclick={clearSearch} aria-label="Clear search">
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

  :global(.font-awesome-icon) {
    color: variables.$white;
  }

  nav {
    background-color: variables.$primary-accent;
    padding: 0 2rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid variables.$secondary-accent;
    position: fixed;
    top: 0;
    left: 0;
    height: 60px;
    width: 100vw;
    z-index: 100;
    box-sizing: border-box;
  }

  .side-section {
    display: flex;
    align-items: center;
    flex: 1;

    &.left {
      justify-content: flex-start;
      gap: 1.5rem;
    }

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
    margin: 0;
    padding: 0;
  }

  .search-wrapper {
    display: flex;
    justify-content: center;
    flex: 2;
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
