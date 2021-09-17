<template>
    <div>
      <h2>בחירת סכומים:</h2>
      <h6>&#9888;שים לב כי את הפרטים הבאים חובה עליך למלא</h6>
      <div class="wrapper">
        <p>הפקדה חד פעמית (ש"ח):</p>
        <input id="oneTimeDeposit" Placeholder= "הזן מספר (0 או יותר)" v-bind:value="providentFundCalculatorData.oneTimeDeposit" @input="update('oneTimeDeposit', $event.target.value)" min="0" type="number"/>
      </div>
      <div class="wrapper">
        <p>הפקדה חודשית (ש"ח):</p>
        <input id="mDeposit" Placeholder= "הזן מספר (0 או יותר)" v-bind:value="providentFundCalculatorData.mDeposit" @input="update('mDeposit', $event.target.value)" type="number" min="0"/>
      </div>
      <div v-if="!providentFundCalculatorData.isValidMDepositAndOneDeposit" class="wrapper-alert">
          <h6 style="font-size:24px; font-weight: bold;"> &#128712;</h6>
          <h6>הפקדה חד פעמית או הפקדה חודשית צריכים להיות גדולים מ-0</h6>
      </div>
      <div class="wrapper">
        <p>לפי:</p>
        <select v-model="selectedTime" @select="update('selectedTime', $event.target.value)">
          <option >שנים</option>
          <option>חודשים</option>
        </select>
      </div>
      <div class="wrapper">
        <p>לכמה {{selectedTime}}:</p>
        <input id="numTime" Placeholder= "הזן מספר" v-bind:value="providentFundCalculatorData.numTime" @input="update('numTime', $event.target.value)" type="number" min="1"/>
      </div>
      <div v-if="!providentFundCalculatorData.isValidSelectedTime" class="wrapper-alert">
        <h6 style="font-size:24px; font-weight: bold;"> &#128712;</h6>
        <h6>מספר ה{{selectedTime}} חייב להיות 1 או יותר</h6>
      </div>
      <div class="wrapper">
        <p>חישוב תשואה:</p>
        <select v-model="selectedYearsCompared" @select="update('selectedYearsCompared', $event.target.value)">
          <option>לפי השנה האחרונה</option>
          <option>לפי ה-3 שנים האחרונות</option>
          <option>לפי ה-5 שנים האחרונות</option>
        </select>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Calculator',
  data: function () {
    return {
      selectedTime: 'שנים',
      selectedYearsCompared: 'לפי השנה האחרונה'
    }
  },
  props: {
    providentFundCalculatorData: {
      type: Object,
      default: function () {
        return {
          oneTimeDeposit: {
            type: Number
          },
          mDeposit: {
            type: Number
          },
          numTime: {
            type: Number
          },
          selectedTime: {
            type: String
          },
          selectedYearsCompared: {
            type: String
          },
          isValidMDepositAndOneDeposit: {
            type: Boolean
          },
          isValidSelectedTime: {
            type: Boolean
          }
        }
      }
    }
  },
  methods: {
    update (key, value) {
      this.providentFundCalculatorData[key] = value
      this.$emit('input', { ...this.providentFundCalculatorData })
    }
  }
}
</script>
<style scoped>
  h2 {
    direction: rtl;
    font-size: 25px;
    color: black;
    font-weight: bold;
  }
  p{
    direction: rtl;
    font-size: 18px;
    color: #090952;
    font-weight: bold;
  }
  .wrapper {
    display: grid;
    grid-template-columns: 300px 400px;
    column-gap: 10px;
    padding-bottom: 0.5em;
  }
  .wrapper-alert {
    display: grid;
    grid-template-columns: 30px 500px;
    color:red;
    align-items: center;
  }

</style>
