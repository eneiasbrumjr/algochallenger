<template>
<div>
  <button v-if="loading" :class="'btn btn-'+btnType" type="button" disabled>
  <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
    Loading...
  </button>
  <button v-else :class="'btn btn-'+btnType">{{label}}</button>
</div>
</template>

<script>
  export default {
    name: 'BaseButton',
    props: {
      label: {
        type: String,
        default: 'Submit'
      },
      loading: {
        type: Boolean,
        default: false
      },
      btnType: {
        type: String,
        default: 'primary'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
