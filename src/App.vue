<template>
  <div id="app">
    <Menu></Menu>
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
  body {
    border: 0;
    margin: 0;
  }
  #router{
    padding-left: 20px;
  }

</style>
