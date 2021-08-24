<template>
    <div>
      <h2>בחירת סכומים:</h2>
      <h6>&#9888;שים לב כי את הפרטים הבאים חובה עליך למלא</h6>
      <div class="wrapper">
        <p>הפקדה חד פעמית (ש"ח):</p>
        <input id="oneTimeDeposit" Placeholder= "הזן מספר (0 או יותר)" v-model="oneTimeDeposit" min="0" type="number"/>
        <p>הפקדה חודשית (ש"ח):</p>
        <input id="mDeposit" Placeholder= "הזן מספר (0 או יותר)" v-model="mDeposit"  type="number" min="0"/>
        <p>לפי:</p>
        <select v-model="selectedTime">
          <option>שנים</option>
          <option>חודשים</option>
        </select>
        <p>לכמה {{selectedTime}}:</p>
        <input id="numTime" Placeholder= "הזן מספר" v-model="numTime"  type="number" min="1"/>
        <p>חישוב תשואה:</p>
        <select v-model="selectedYearsComper">
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
      oneTimeDeposit: '',
      mDeposit: '',
      numTime: 1,
      selectedTime: 'שנים',
      selectedYearsComper: 'לפי השנה האחרונה'
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
    row-gap: 1em;
  }
</style>
