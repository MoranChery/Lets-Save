<template>
    <div>
      <h2>בחירת סכומים:</h2>
      <h6>&#9888;שים לב כי את הפרטים הבאים חובה עליך למלא</h6>
      <b-container>
        <b-row>
          <b-col sm="3">
            <p>הפקדה חד פעמית (ש"ח):</p>
          </b-col>
          <b-col sm="5">
            <b-input-group prepend="">
              <b-form-input id="oneTimeDeposit" :state="providentFundCalculatorData.isValidMDepositAndOneDeposit" placeholder= "הזן מספר (0 או יותר)" v-model="providentFundCalculatorData.oneTimeDeposit" min="0" type="number"></b-form-input>
            </b-input-group>
          </b-col>
        </b-row>
      </b-container>
      <b-container>
        <b-row>
          <b-col sm="3">
            <p>הפקדה חודשית (ש"ח):</p>
          </b-col>
          <b-col sm="5">
            <b-input-group prepend="">
              <b-form-input id="mDeposit" Placeholder= "הזן מספר (0 או יותר)"
                            :state="providentFundCalculatorData.isValidMDepositAndOneDeposit" v-model="providentFundCalculatorData.mDeposit" type="number" min="0"></b-form-input>
               <b-form-invalid-feedback id="input-live-feedback">הפקדה חד פעמית או הפקדה חודשית צריכים להיות גדולים מ-0</b-form-invalid-feedback>
            </b-input-group>
          </b-col>
        </b-row>
      </b-container>
      <b-container>
        <b-row>
          <b-col sm="3">
            <p>לפי:</p>
          </b-col>
          <b-col sm="5">
            <b-form-select v-model="selectedTime" chenge="update('selectedTime', $event.target.value)" class="mb-3">
              <b-form-select-option value="שנים">שנים</b-form-select-option>
              <b-form-select-option value="חודשים">חודשים</b-form-select-option>
            </b-form-select>
          </b-col>
        </b-row>
      </b-container>
      <b-container>
        <b-row>
          <b-col sm="3">
            <p>לכמה {{selectedTime}}:</p>
          </b-col>
          <b-col sm="5">
            <b-input-group prepend="">
              <b-form-input id="numTime"
                            placeholder= "הזן מספר"
                            :state="providentFundCalculatorData.isValidSelectedTime"
                            aria-describedby="input-live-feedback"
                            v-model="providentFundCalculatorData.numTime" type="number" min="1"></b-form-input>
              <b-form-invalid-feedback id="input-live-feedback">מספר ה{{selectedTime}} חייב להיות 1 או יותר</b-form-invalid-feedback>
            </b-input-group>

          </b-col>
        </b-row>
      </b-container>
      <b-container>
        <b-row>
          <b-col sm="3">
            <p>חישוב תשואה:</p>
          </b-col>
          <b-col sm="5">
            <b-form-select v-model="selectedYearsCompared" chenge="update('selectedYearsCompared', $event.target.value)" class="mb-3">
              <b-form-select-option value="לפי השנה האחרונה">לפי השנה האחרונה</b-form-select-option>
              <b-form-select-option value="לפי ה-3 שנים האחרונות">לפי ה-3 שנים האחרונות</b-form-select-option>
              <b-form-select-option value="לפי ה-5 שנים האחרונות">לפי ה-5 שנים האחרונות</b-form-select-option>
            </b-form-select>
          </b-col>
        </b-row>
      </b-container>
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
      console.log('key: ', key)
      console.log('value: ', value)
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
  .wrapper-alert {
    display: grid;
    grid-template-columns: 30px 500px;
    color:red;
    align-items: center;
  }

</style>
