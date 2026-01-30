<!--
  Avatar Component

  This component displays a user avatar with an icon and username.
  It's shown at the bottom of the navigation sidebar.

  In the future, this could be enhanced to:
  - Show the actual user's profile picture
  - Display the real username from authentication
  - Allow clicking to open a user menu
-->

<script lang="ts">
  /**
   * FontAwesome icon for the user avatar.
   * We import just the specific icon we need to keep bundle size small.
   */
  import Fa from 'svelte-fa';
  import { faUser } from '@fortawesome/free-regular-svg-icons';

  /**
   * The username to display.
   * For now this is hardcoded, but could be passed as a prop
   * or fetched from a user authentication system.
   */
  const username = 'UserName';
</script>

<!--
  The avatar container holds both the icon and the username.
  It's styled to appear at the bottom of the navigation bar.
-->
<div class="avatar">
  <!--
    The avatar icon is a circular container with a white background
    that holds the user icon inside.
  -->
  <div class="avatar-icon">
    <!-- FontAwesome user icon, displayed in black -->
    <Fa icon={faUser} style="color: #000000" />
  </div>

  <!-- Display the username next to the icon -->
  <h3>{username}</h3>
</div>

<!--
  Component-specific styles using SCSS.

  In Svelte, styles in a <style> block are automatically scoped to this component.
  This means these styles won't affect other components, preventing style conflicts.

  The "lang='scss'" tells Svelte to process this as SCSS instead of plain CSS.
-->
<style lang="scss">
  @use '$lib/styles/variables';

  .avatar {
    display: flex; 
    gap: 10px;          /* Changed from 4% to a fixed gap [cite: 16] */
    align-items: center;
    justify-content: flex-end; /* Align content to the right of its container [cite: 18] */
    background-color: transparent; /* Remove the solid block background  */
    border-top: none;   /* REMOVES THE BLACK LINE  */
    width: auto;        /* Stop it from stretching across the whole bar [cite: 20] */
    height: 100%;       /* Match the nav bar height [cite: 20] */
  }

  .avatar-icon {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: white;
    height: 2.2em;      /* Slightly larger for the top bar [cite: 24] */
    width: 2.2em;
    border-radius: 50%;
  }
  
  h3 {
    font-size: 0.9rem;  /* Ensure the username matches the small nav text */
    margin: 0;
  }
</style>
