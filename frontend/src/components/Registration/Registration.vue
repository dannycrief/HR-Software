<template>
  <div class="vue-template">
    <div class="main-content">
      <div class="left-side d-none d-lg-block">
        <div class="top-content">
          <b>Online Test & Exams Software</b>
        </div>
        <img
          :src="rightLogo"
          alt="HRSoftware Logo"
        >
        <div class="bottom-content">
          Administer online secure exams to candidates, students or employees.<br>
          Create your own tests.
        </div>
      </div>
      <div class="right-side">
        <div class="registration-app">
          <router-link
            to="/"
            class="home-button-logo"
          >
            <font-awesome-icon
              :icon="['far', 'check-circle']"
              size="lg"
            />
            <b>HR</b>Software
          </router-link>
          <div class="register-menu">
            <div class="login-link">
              <div class="signup">
                <b>Signup</b>
              </div>
              <div class="login">
                Already have an account?
                <router-link
                  to="/login"
                  class="login-button"
                >
                  Log in
                </router-link>
              </div>
            </div>
            <GoogleAuth />
            <FacebookAuth />
          </div>
          <div class="divider">
            <div class="divider__line" />
            <div class="divider__text">
              or
            </div>
            <div class="divider__line" />
          </div>
          <RegistrationForm />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RegistrationForm from "./RegistrationForm";
import GoogleAuth from "./auth/GoogleAuth";
import FacebookAuth from "./auth/FacebookAuth";
import rightLogo from '../../assets/images/right-logo.png';
import '../../assets/styles/registration.scss';


export default {
  name: 'RegistrationComponent',
  components: {
    RegistrationForm,
    GoogleAuth,
    FacebookAuth,
  },
  data() {
    return {
      rightLogo,
    };
  }
};
</script>
