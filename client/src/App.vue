<template>
  <div id="app">
    <Menu id='menu'></Menu>
    <router-view id="router"/>
  </div>
</template>
<script>

import Menu from './components/Menu.vue'
export default {
  name: 'app',
  components: {
    Menu
  }
}
</script>
<style>
  body, html {
    padding: 0;
    margin: 0;
    width: 100%;
    min-height: 100%;
  }
  #menu {
    position:fixed;
    left:0;           /* top left corner should start at leftmost spot */
    top:0;            /* top left corner should start at topmost spot */
    width:100vw;      /* take up the full browser width */
    z-index:200;  /* high z index so other content scrolls underneath */
    height:100px;
  }
  #router{
    padding-top: 75px;
  }

</style>
