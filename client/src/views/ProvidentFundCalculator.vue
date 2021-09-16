<template>
  <div class="provident_fund_calculator">
    <div class="sticky">
      <h1>מחשבון קופת גמל</h1>
      <h6>מעוניין להפקיד מידי חודש סכום מסויים ו/או הפקדה חד פעמית  כדי להבטיח לך בסיס כלכלי ואינך יודע מהו הסכום, באמצעות מחשבון הגמל תוכל לקבל הערכה לגבי סכום הצבירה הצפוי לך בהפקדה חד פעמית ו/או שוטפת</h6>
    </div>
    <Calculator :provident-fund-calculator-data="providentFundCalculatorData" class="filters"/>
    <Filters class="filters"/>
    <button @click="printProvidentFundCalculatorData">חשב</button>
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
  },
  data: function () {
    return {
      providentFundCalculatorData: {
        oneTimeDeposit: 0,
        mDeposit: 0,
        numTime: 1,
        selectedTime: 'שנים',
        selectedYearsCompared: 'לפי השנה האחרונה',
        isValidOneTimeDeposit: true,
        isValidMDeposit: true
      }
    }
  },
  methods: {
    printProvidentFundCalculatorData () {
      console.log('Click:', this.providentFundCalculatorData)
      if (typeof (this.providentFundCalculatorData.oneTimeDeposit) === 'number') {
        console.log('oneTimeDeposit type number')
        if (this.providentFundCalculatorData.oneTimeDeposit === 0) {
          console.log('oneTimeDeposit type number and is 0')
          this.$set(this.providentFundCalculatorData, 'isValidOneTimeDeposit', false)
          this.$set(this.providentFundCalculatorData, 'isValidMDeposit', false)
        }
      } else if (typeof (this.providentFundCalculatorData.oneTimeDeposit) === 'object') {
        console.log('oneTimeDeposit type object')
      } else if (typeof (this.providentFundCalculatorData.oneTimeDeposit) === 'string') {
        console.log('oneTimeDeposit type string')
      }
    }
  }
}
</script>
<style scoped>
  .provident_fund_calculator {
    padding-top: 50px;
    text-align: justify;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
  .sticky{
    position: sticky;
    background-color: white;
    padding-right: 10px;
    padding-bottom: 10px;
    top: 65px;
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
