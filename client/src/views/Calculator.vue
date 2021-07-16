<template>
  <div class="calculator">
    <h1>מחשבון קופת גמל</h1>
    <Filters/>
  </div>
</template>
<script>
import Filters from '../components/Filters'
export default {
  name: 'Calculator',
  components: {
    Filters
  }
}
</script>
<style scoped>
  .calculator{
    margin: 15px;
    direction: rtl;
    text-align: justify;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
</style>
