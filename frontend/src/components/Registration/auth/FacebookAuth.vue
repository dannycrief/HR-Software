<template>
  <div class="facebook-auth">
    <router-link
      to="/"
      class="auth-button facebook-button"
    >
      <font-awesome-icon
        :icon="['fab', 'facebook']"
        size="lg"
      />
      Continue with Facebook
    </router-link>
  </div>
</template>

<script>

export default {
  name: "FacebookAuth",
};
</script>

