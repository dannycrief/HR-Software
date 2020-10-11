<template>
  <mdb-alert
    color="danger"
    class="error-alert"
  >
    {{ message }}
  </mdb-alert>
</template>

<script>
import {mdbAlert} from 'mdbvue';

export default {
  name: "Error",
  components: {
    mdbAlert
  },
  props: {
    message: {type: String, default: ''},
  }
};
</script>
