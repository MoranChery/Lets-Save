<template>
  <div>
    <h2>סינונים אפשריים:</h2>
    <h6>&#9888;שים לב כי במידה ואינך יודע אשאר את הנתונים כפי שהם</h6>
    <div class="wrapper">
      <p>בחר מסלולים:</p>
      <multiselect :style="cssVars" v-model="filtersData.selected_investment_track" placeholder="הוסף או הסר מסלול" selectedLabel="" deselectLabel="הסר" selectLabel="בחר" :options="investment_track_options" :multiple="true" @change="update('selected_investment_track', $event.target.value)"></multiselect>
    </div>
    <div v-if="!filtersData.isValidSelectedInvestmentTrack" class="wrapper-alert">
      <h6 style="font-size:24px; font-weight: bold;"> &#128712;</h6>
      <h6>יש לבחור לפחות מסלול אחד</h6>
    </div>
    <div class="wrapper">
      <p>דמי ניהול עד:</p>
      <div class="wrapper">
        <input id="management_fee" Placeholder= "יש לשים מספר" v-bind:value="filtersData.management_fee" @input="update('management_fee', $event.target.value)" min="0" type="number"/>
        <p>%</p>
      </div>
    </div>
    <div v-if="!filtersData.isValidManagementFee" class="wrapper-alert">
      <h6 style="font-size:24px; font-weight: bold;"> &#128712;</h6>
      <h6>יש לבחור לפחות מסלול אחד</h6>
    </div>
  </div>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  name: 'Filters',
  components: { Multiselect },
  props: {
    filtersData: {
      type: Object,
      default: function () {
        return {
          management_fee: {
            type: Number
          },
          selected_investment_track: {
            type: Array
          },
          isValidSelectedInvestmentTrack: {
            type: Boolean
          },
          isValidManagementFee: {
            type: Boolean
          }
        }
      }
    }
  },
  data: function () {
    return {
      investment_track_options: [],
      management_fee: 2
    }
  },
  created () {
    this.getInvestmentTrackOptions()
  },
  computed: {
    cssVars () {
      return {
        /* variables you want to pass to css */
        '--height': this.filtersData.height
      }
    }
  },
  methods: {
    async getInvestmentTrackOptions () {
      try {
        // get companies_options and selected_company
        this.filtersData.selected_investment_track = []
        const response = await this.$http.get('investmentTrackOptions/')
        // JSON responses are automatically parsed.
        for (const arr in response.data.json_list) {
          for (const investmentTrack in arr) {
            const investmentTrackStr = response.data.json_list[arr][investmentTrack]
            if (investmentTrackStr) {
              this.filtersData.selected_investment_track.push(investmentTrackStr)
              this.investment_track_options.push(investmentTrackStr)
            }
          }
        }
      } catch (error) {
        console.log(error)
      }
    },
    update (key, value) {
      this.filtersData[key] = value
      this.$emit('input', { ...this.filtersData })
    }
  }
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped>
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
    grid-template-columns: 15% 70%;
    column-gap: 10px;
    padding-bottom: 1em;
  }
  .multiselect {
    width: 60%;
    height: var(--height)+ px;
  }
  .wrapper-alert {
    display: grid;
    grid-template-columns: 30px 500px;
    color:red;
    align-items: center;
  }

</style>
