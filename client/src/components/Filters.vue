<template>
  <div class="filters">
    <h2>סינונים אפשריים:</h2>
    <p>בחר חברה:
    <select v-model="selected_company">
      <option v-for="company in companies_options"  :key=company>{{company}}</option>
    </select>
    </p>
  </div>
</template>
<script>
export default {
  name: 'Filters',
  data: function () {
    return {
      selected_company: 'All',
      companies_options: ['All', 'opt1', 'opt2', 'opt3']
    }
  }
}
</script>
<style scoped>
  .filters{
    padding: 10px;
    direction: rtl;
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
</style>
