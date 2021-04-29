<template>
  <div class="home">
    <img class="logo-img" src="../assets/logo.png" alt="Logo">
    <div class="css-typing">
      <p> Welcome to Smart Save </p>
      <p> This site was created to allow a comparison between a variety of provident funds for investment in Israel. </p>
      <p> I saw a need to build this site to allow people to compare provident funds using a simple calculator and </p>
      <p> system recommendations based on data. </p>
      <p> About Me: </p>
      <p> I have always thought about how to save my money wisely and efficiently. My fear was that because of the</p>
      <p> lack of knowledge I would lose the money I wanted to invest. After a long search I found information about</p>
      <p> investment provident funds, but even when I found the information and wanted to examine and compare</p>
      <p> different offers it was difficult to do so.</p>
      <p> I will note, I am an information systems engineer, once I realized I have the power and ability to bring</p>
      <p> about change I decided to build this site.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>
<style scoped>
  .home{
    font-family: 'Courier New', monospace;
    background: linear-gradient(45deg, rgb(31, 64, 102) 0%, rgb(101, 171, 127) 48%, rgb(113, 249, 131) 100%);
    height: 100%;
  }
  .logo-img{
    border-radius: 300px;
    width: 250px;
    height: 250px;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  .css-typing p {
    border-right: .15em solid #6d9af5;
    font-size: 20px;
    white-space: nowrap;
    overflow: hidden;
    color: #060645;
    font-weight: bold;
  }
  .css-typing p:nth-child(1) {
    width: 14em;
    -webkit-animation: type 3s steps(40, end);
    animation: type 3s steps(40, end);
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
    font-weight: bold;
    font-size: 30px;
    color: black;
  }
  .css-typing p:nth-child(2) {
    width: 65em;
    opacity: 0;
    -webkit-animation: type2 8s steps(140, end);
    animation: type2 8s steps(140, end);
    -webkit-animation-delay: 3s;
    animation-delay: 3s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  .css-typing p:nth-child(3) {
    width: 65em;
    opacity: 0;
    -webkit-animation: type3 8s steps(140, end);
    animation: type3 8s steps(140, end);
    -webkit-animation-delay: 11s;
    animation-delay: 11s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  .css-typing p:nth-child(4) {
    width: 24em;
    opacity: 0;
    -webkit-animation: type4 3s steps(40, end);
    animation: type4 3s steps(40, end);
    -webkit-animation-delay: 19s;
    animation-delay: 19s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  .css-typing p:nth-child(5) {
    width: 5.3em;
    opacity: 0;
    -webkit-animation: type4 1s steps(40, end);
    animation: type4 1s steps(40, end);
    -webkit-animation-delay: 22s;
    animation-delay: 22s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
    color: black;
  }
 .css-typing p:nth-child(6) {
    width: 63em;
    opacity: 0;
    -webkit-animation: type3 8s steps(140, end);
    animation: type6 8s steps(140, end);
    -webkit-animation-delay: 23s;
    animation-delay: 23s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  .css-typing p:nth-child(7) {
    width: 64em;
    opacity: 0;
    -webkit-animation: type7 8s steps(140, end);
    animation: type6 8s steps(140, end);
    -webkit-animation-delay: 31s;
    animation-delay: 31s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  .css-typing p:nth-child(8) {
    width: 62em;
    opacity: 0;
    -webkit-animation: type8 8s steps(140, end);
    animation: type6 8s steps(140, end);
    -webkit-animation-delay: 39s;
    animation-delay: 39s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  .css-typing p:nth-child(9) {
    width: 26em;
    opacity: 0;
    -webkit-animation: type4 3s steps(40, end);
    animation: type4 3s steps(40, end);
    -webkit-animation-delay: 47s;
    animation-delay: 47s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  .css-typing p:nth-child(10) {
    width: 63em;
    opacity: 0;
    -webkit-animation: type10 8s steps(140, end);
    animation: type6 8s steps(140, end);
    -webkit-animation-delay: 50s;
    animation-delay: 50s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  .css-typing p:nth-child(11) {
    width: 26em;
    opacity: 0;
    -webkit-animation: type4 3s steps(40, end);
    animation: type4 3s steps(40, end);
    -webkit-animation-delay: 58s;
    animation-delay: 58s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
  }
  @keyframes type{
    0% {
      width: 0;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      border: none;
    }
  }
  @-webkit-keyframes type {
    0% {
      width: 0;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      border: none;
    }
  }
  @keyframes type2 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type2 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @keyframes type3 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type3 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
    @keyframes type4 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type4 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @keyframes type5 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type5 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
    @keyframes type6 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type6 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
    @keyframes type7 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type7 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
    @keyframes type8 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type8 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @keyframes type9 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type9 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
    @keyframes type10 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type10 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
    @keyframes type11 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
  @-webkit-keyframes type11 {
    0% {
      width: 0;
    }
    1% {
      opacity: 1;
    }
    99.9% {
      border-right: .15em solid #6d9af5;
    }
    100% {
      opacity: 1;
      border: none;
    }
  }
</style>
