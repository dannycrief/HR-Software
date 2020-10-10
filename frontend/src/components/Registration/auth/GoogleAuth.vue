<template>
  <div class="google-auth">
    <router-link
      to="/"
      class="auth-button google-button"
    >
      <img
        :src="Google_Logo"
        alt="Google logo"
      >
      Continue with Google
    </router-link>
  </div>
</template>

<script>
import Google_Logo from '../../../assets/images/Google__G__Logo.svg';
export default {
  name: "GoogleAuth",
  data() {
    return {
      Google_Logo
    };
  }
};
</script>

