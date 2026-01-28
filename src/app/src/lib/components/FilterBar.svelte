<script lang="ts">
  // These variables will store the current filter selections
  let players = "Any";
  let price = "Any Price";
  let release = "All Time";
  let score = "Any Score";

  function applyFilters() {
    console.log("Filters applied:", { players, price, release, score });
  }
</script>

<div class="filter-bar">
  <div class="filter-group">
    <label for="players">Players:</label>
    <select id="players" bind:value={players}>
      <option>Any</option>
      <option>Singleplayer</option>
      <option>Multiplayer</option>
    </select>
  </div>

  <div class="filter-group">
    <label for="price">Price:</label>
    <select id="price" bind:value={price}>
      <option>Any Price</option>
      <option>Free</option>
      <option>Under $20</option>
      <option>$20 - $50</option>
      <option>$50+</option>
    </select>
  </div>

  <div class="filter-group">
    <label for="release">Release:</label>
    <select id="release" bind:value={release}>
      <option>All Time</option>
      <option>Last 30 Days</option>
      <option>This Year</option>
      <option>Coming Soon</option>
    </select>
  </div>

  <div class="filter-group">
    <label for="score">Score:</label>
    <select id="score" bind:value={score}>
      <option>Any Score</option>
      <option>90+ (Exceptional)</option>
      <option>80+ (Great)</option>
      <option>70+ (Good)</option>
    </select>
  </div>

  <button class="apply-btn" on:click={applyFilters}>
    Apply Filters
  </button>
</div>

<style lang="scss">
  @use '$lib/styles/variables';

  .filter-bar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 1.5rem;
    padding: 1rem 2rem;
    background: rgba(20, 10, 40, 0.4); /* Darker semi-transparent background */
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    margin-top: 60px; /* Pushes it below the fixed 60px Nav bar */
    width: 100%;
  }

  .filter-group {
    display: flex;
    align-items: center;
    gap: 0.5rem;

    label {
      color: white;
      font-size: 0.9rem;
      font-weight: 500;
    }

    select {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: white;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;

      option {
        background: #1a1a2e; /* Dark background for dropdown options */
        color: white;
      }

      &:focus {
        border-color: #6366f1; /* Purple focus glow */
      }
    }
  }

  .apply-btn {
    background: #6366f1; /* Matches the blue/purple button in your image */
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 0.85rem;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #4f46e5;
    }
  }
</style>
