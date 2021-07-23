<template>
<div>
  <b-navbar type="dark" variant="dark">
    <b-navbar-brand class="logo">
      <img class="logo-img" src="../assets/logo.png" alt="Logo">
      Smart Save
    </b-navbar-brand>
    <b-navbar-nav>
      <b-nav-item to="/" v-on:click="setActive('home')" :class="{ active: isActive('home') }">Home</b-nav-item>
      <b-nav-item to="/provident_fund_calculator" v-on:click="setActive('provident_fund_calculator')" :class="{ active: isActive('provident_fund_calculator') }">PPF Calculator</b-nav-item>
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
  ::v-deep .logo-img{
    display: inline;
    border-radius: 100px;
    width: 40px;
    height: 40px;
    vertical-align: middle;
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  ::v-deep {
    color: white !important;
    font-weight: bold;
  }
  ::v-deep .active .nav-link {
    color: #6d9af5 !important;
    font-weight: bold;
  }
  .logo{
    padding-right: 15px;
    font-size: 25px;
  }
</style>
