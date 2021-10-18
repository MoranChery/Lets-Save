<template>
  <div>
    <div>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand class="logo">
      <img class="logo-img" src="../assets/logo.png" alt="Logo">
      Smart Save
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown text="מחשבונים" right>
          <b-dropdown-item to="/provident_fund_calculator">קופת גמל</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-navbar-nav>
          <b-nav-item to="/">דף הבית</b-nav-item>
        </b-navbar-nav>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
  </div>

</template>
<script>
export default {
  name: 'Menu'
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
  .logo{
    padding-right: 15px;
    font-size: 25px;
  }
</style>
