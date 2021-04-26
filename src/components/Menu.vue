<template>
<div>
  <b-navbar type="dark" variant="dark">
  <!-- Image and text -->
    <b-navbar-brand>
      <img class="logo" src="../assets/logo.png" alt="Logo">
      Smart Save
    </b-navbar-brand>
    <b-navbar-nav>
      <b-nav-item to="/" v-on:click="setActive('home')" :class="{ active: isActive('home') }">Home</b-nav-item>
      <b-nav-item to="/about" v-on:click="setActive('about')" :class="{ active: isActive('about') }">PPF Calculator</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</div>
</template>
<script>
export default {
  name: 'Menu',
  data () {
    return { activeItem: 'home' }
  },
  methods: {
    isActive: function (menuItem) {
      return this.activeItem === menuItem
    },
    setActive: function (menuItem) {
      this.activeItem = menuItem
    }
  }
}
</script>
<style scoped>
  .logo{
    display: inline;
    color: #fff;
    font-weight: bold;
    font-size: 40px;
    border-radius: 100px;
    width: 40px;
    height: 40px;
    vertical-align: middle;
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  ::v-deep .nav-link {
    color: white !important;
    font-weight: bold;
  }
  ::v-deep .active .nav-link {
    color: #6d9af5 !important;
    font-weight: bold;
  }
</style>
