<template>
  <div class="provident_fund_calculator">
    <h1>מחשבון קופת גמל</h1>
    <h6>מעוניין להפקיד מידי חודש סכום מסויים ו/או הפקדה חד פעמית  כדי להבטיח לך בסיס כלכלי ואינך יודע מהו הסכום, באמצעות מחשבון הגמל תוכל לקבל הערכה לגבי סכום הצבירה הצפוי לך בהפקדה חד פעמית ו/או שוטפת</h6>
    <Calculator class="filters"/>
    <Filters class="filters"/>
    <button>חשב</button>
  </div>
</template>
<script>
import Filters from '../components/Filters'
import Calculator from '../components/Calculator'
export default {
  name: 'ProvidentFundCalculator',
  components: {
    Filters,
    Calculator
  }
}
</script>
<style scoped>
  .provident_fund_calculator {
    margin: 15px;
    text-align: justify;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
  h1{
    direction: rtl;
  }
  h6 {
    direction: rtl;
    margin-left: 20%;
  }
  .filters{
    direction: rtl;
    padding: 10px;
    background: rgb(106, 179, 179);
    height: 100%;
    text-align: justify;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    margin-bottom: 15px;
  }
  button {
    padding: 10px;
    display: block;
    background-color:white;
    color: black;
    border: 2px solid #555555;
    border-radius: 8px;
    width: 200px;
    font-size: 20px;
    font-weight: bold;
    margin: auto;
  }
  button:hover {
    background-color:  rgb(106, 179, 179);
    color: white;
  }
</style>
