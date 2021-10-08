<template>
  <div>
    <h2>סינונים אפשריים:</h2>
    <h6>&#9888;שים לב כי במידה ואינך יודע אשאר את הנתונים כפי שהם</h6>
    <b-container>
      <b-row>
        <b-col sm="3">
          <p>בחר מסלולים:</p>
        </b-col>
        <b-col sm="8" style="padding-bottom:5px">
          <multiselect :style="cssVars" v-model="filtersData.selected_investment_track" placeholder="הוסף או הסר מסלול" selectedLabel="" deselectLabel="הסר" selectLabel="בחר"
                       :options="investment_track_options" :multiple="true" @change="update('selected_investment_track', $event.target.value)"></multiselect>
        </b-col>
      </b-row>
    </b-container>
    <b-container v-if="!filtersData.isValidSelectedInvestmentTrack ">
      <b-row style="align-items: center;">
        <b-col sm="3"></b-col>
        <b-col>
          <h4>יש לבחור לפחות מסלול אחד</h4>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
        <b-row>
          <b-col sm="3">
            <p>דמי ניהול עד:</p>
          </b-col>
          <b-col sm="5">
            <b-input-group prepend="%">
              <b-form-input id="management_fee"
                            placeholder= "יש לשים מספר"
                            :state="filtersData.isValidManagementFee"
                            aria-describedby="input-live-feedback"
                            v-model="filtersData.management_fee" type="number" min="0.000001"></b-form-input>
              <b-form-invalid-feedback id="input-live-feedback">דמי ניהול חייב להיות גדול מ-0</b-form-invalid-feedback>
            </b-input-group>
          </b-col>
        </b-row>
      </b-container>
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
  h4{
    width: 100%;
    margin-top: 0.25rem;
    font-size: 80%;
    color: #dc3545;
    font-weight:normal;
  }

</style>
