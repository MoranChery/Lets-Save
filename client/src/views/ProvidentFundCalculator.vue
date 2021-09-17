<template>
  <div class="provident_fund_calculator">
    <div class="sticky">
      <h1>מחשבון קופת גמל</h1>
      <h6>מעוניין להפקיד מידי חודש סכום מסויים ו/או הפקדה חד פעמית  כדי להבטיח לך בסיס כלכלי ואינך יודע מהו הסכום, באמצעות מחשבון הגמל תוכל לקבל הערכה לגבי סכום הצבירה הצפוי לך בהפקדה חד פעמית ו/או שוטפת</h6>
    </div>
    <Calculator :provident-fund-calculator-data="providentFundCalculatorData" class="filters"/>
    <Filters :filters-data="filtersData" class="filters"/>
    <button @click="getProvidentFundCalculatorData">חשב</button>
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
        isValidMDepositAndOneDeposit: true,
        isValidSelectedTime: true
      },
      filtersData: {
        management_fee: 2,
        selected_investment_track: [],
        isValidSelectedInvestmentTrack: true,
        isValidManagementFee: true,
        height: 100
      }
    }
  },
  methods: {
    getProvidentFundCalculatorData () {
      console.log(this.filtersData)
      let isValidOneDeposit = true
      let isValidMDeposit = true
      let isValidSelectedTime = true
      let isValidManagementFee = true
      if (typeof (this.providentFundCalculatorData.oneTimeDeposit) === 'number') {
        isValidOneDeposit = false
      } else if (typeof (this.providentFundCalculatorData.oneTimeDeposit) === 'object') {
        isValidOneDeposit = false
      } else if (typeof (this.providentFundCalculatorData.oneTimeDeposit) === 'string') {
        if (this.providentFundCalculatorData.oneTimeDeposit === '') {
          console.log('oneTimeDeposit type string and it empty')
          isValidOneDeposit = false
        } else {
          try {
            const oneTimeDepositNum = Number(this.providentFundCalculatorData.oneTimeDeposit)
            if (oneTimeDepositNum === 0) {
              isValidOneDeposit = false
            }
          } catch (e) {
            isValidOneDeposit = false
          }
        }
      }
      if (typeof (this.providentFundCalculatorData.mDeposit) === 'number') {
        isValidMDeposit = false
      } else if (typeof (this.providentFundCalculatorData.mDeposit) === 'object') {
        isValidMDeposit = false
      } else if (typeof (this.providentFundCalculatorData.mDeposit) === 'string') {
        if (this.providentFundCalculatorData.mDeposit === '') {
          isValidMDeposit = false
        } else {
          try {
            const mDepositNum = Number(this.providentFundCalculatorData.mDeposit)
            if (mDepositNum === 0) {
              isValidMDeposit = false
            }
          } catch (e) {
            isValidMDeposit = false
          }
        }
      }
      if (typeof (this.providentFundCalculatorData.numTime) === 'object') {
        isValidSelectedTime = false
      } else if (typeof (this.providentFundCalculatorData.numTime) === 'string') {
        if (this.providentFundCalculatorData.numTime === '') {
          isValidSelectedTime = false
        } else {
          try {
            const numTimeNum = Number(this.providentFundCalculatorData.numTime)
            if (numTimeNum === 0) {
              isValidSelectedTime = false
            }
          } catch (e) {
            isValidSelectedTime = false
          }
        }
      }
      if (!isValidOneDeposit && !isValidMDeposit) {
        this.$set(this.providentFundCalculatorData, 'isValidMDepositAndOneDeposit', false)
      } else {
        this.$set(this.providentFundCalculatorData, 'isValidMDepositAndOneDeposit', true)
      }
      if (!isValidSelectedTime) {
        this.$set(this.providentFundCalculatorData, 'isValidSelectedTime', false)
      } else {
        this.$set(this.providentFundCalculatorData, 'isValidSelectedTime', true)
      }
      if (this.filtersData.selected_investment_track.length === 0) {
        this.$set(this.filtersData, 'isValidSelectedInvestmentTrack', false)
        this.$set(this.filtersData, 'height', 40)
      } else {
        this.$set(this.filtersData, 'isValidSelectedInvestmentTrack', true)
        this.$set(this.filtersData, 'height', 80)
      }
      if (typeof (this.filtersData.management_fee) === 'string') {
        if (this.filtersData.management_fee === '') {
          isValidManagementFee = false
        } else {
          try {
            const managementFeeNum = Number(this.filtersData.management_fee)
            if (managementFeeNum === 0) {
              isValidManagementFee = false
            }
          } catch (e) {
            isValidManagementFee = false
          }
        }
      }
      if (!isValidManagementFee) {
        this.$set(this.filtersData, 'isValidManagementFee', false)
      } else {
        this.$set(this.filtersData, 'isValidManagementFee', true)
      }
      if (this.providentFundCalculatorData.isValidMDepositAndOneDeposit && isValidSelectedTime && isValidManagementFee) {
        console.log('send request to server')
      }
    }
  }
}
</script>
<style scoped>
  .provident_fund_calculator {
    padding-top: 50px;
    text-align: justify;
    margin-left: auto;
    margin-right: auto;
    margin-top: 1%;
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
    margin-left: 10%;
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
