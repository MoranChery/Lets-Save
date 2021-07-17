<template>
  <div class="filters">
    <h2>סינונים אפשריים:</h2>
    <h4>שים לב כי במידה ואינך יודע אשאר את הנתונים כפי שהם</h4>
    <div class="wrapper">
      <p>בחר חברות:</p>
      <multiselect v-model="selected_company" placeholder="הוסף או הסר חברה" selectedLabel="" deselectLabel="הסר" selectLabel="בחר" :options="companies_options" :multiple="true"></multiselect>
      <p>בחר מסלולים:</p>
      <multiselect v-model="selected_investment_track" placeholder="הוסף או הסר מסלול" selectedLabel="" deselectLabel="הסר" selectLabel="בחר" :options="investment_track_options" :multiple="true"></multiselect>
      <p>דמי ניהול עד:</p>
      <div class="wrapper">
        <input type="text"
               Placeholder= "יש לשים מספר"
               @input="change" @change="change" :value="inpNum"/>
        <p>%</p>
      </div>
    </div>
  </div>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  name: 'Filters',
  components: { Multiselect },
  data: function () {
    return {
      selected_company: ['opt1', 'opt2', 'opt3', 'opt4cdwcdfvdswsdcdwa', 'opt5', 'opt6', 'opt7', 'opt8'],
      companies_options: ['opt1', 'opt2', 'opt3', 'opt4cdwcdfvdswsdcdwa', 'opt5', 'opt6', 'opt7', 'opt8'],
      selected_investment_track: ['opt1בהגכדקכבגרקככרק', 'opt2', 'opt3'],
      investment_track_options: ['opt1בהגכדקכבגרקככרק', 'opt2', 'opt3'],
      management_fee: 2
    }
  },
  computed: {
    inpNum: function () {
      return this.management_fee
    }
  },
  methods: {
    change (event) {
      const val = event.target.value.trim()
      if (/^[0-9]*\.?[0-9]*\d*$|^$/.test(val)) {
        this.management_fee = val
      } else {
        event.target.value = this.management_fee
      }
    }
  }
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped>
  .filters{
    padding: 10px;
    background: rgb(101, 171, 171);
    height: 100%;
    text-align: justify;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    margin-bottom: 15px;
  }
  h2 {
    direction: rtl;
    font-size: 25px;
    color: black;
    font-weight: bold;
  }
  p {
    direction: rtl;
    font-size: 18px;
    color: #090952;
    font-weight: bold;
  }
  .wrapper {
    display: grid;
    grid-template-columns: 200px 400px;
    column-gap: 10px;
    row-gap: 1em;
  }
  .multiselect {
    width: 800px;
    height: 80px;
  }

</style>
