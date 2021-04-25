<template>
  <div class="menu">
    <nav class="main-nav">
      <img class="logo" src="../assets/logo.png">
      <div class="logo"> LET'S IMPROVE </div>
      <ul class="nav-bar">
        <li class="item-nav" ><router-link to="/">דף הבית</router-link></li>
        <li class="item-nav"><router-link to="/about">קצת עלינו</router-link></li>
      </ul>
    </nav>
  </div>
</template>
<script>
export default {
  name: 'Menu'
}
</script>
<style>
  .menu{
    padding-left: 10px;
    padding-top: 10px;
    padding-bottom: 10px;
    background: black;
  }
  .logo, .nav-bar{
    text-align: center;
    display: inline;
    color: #fff;
    font-weight: bold;
    font-size: 30px;
    border-radius: 100px;
    width: 40px;
    height: 40px;
    vertical-align: middle;
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
  .item-nav{
    padding-right: 20px;
    float: right;
    display: block;
  }

  .item-nav a {
    color: white;
    text-align: center;
    padding: 16px;
    text-decoration: none;
  }

  .item-nav a:hover {
    background-color: #117eb8;
  }
</style>
