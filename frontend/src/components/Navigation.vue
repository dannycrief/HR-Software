<template>
  <div class="navigation-bar">
    <b-navbar
      toggleable="lg"
      type="light"
      variant="light"
    >
      <b-navbar-brand
        variant="primary"
        to="/"
      >
        <font-awesome-icon
          :icon="['far', 'check-circle']"
          size="lg"
        />
        <b>HR</b>Software
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse" />
      <b-collapse
        id="nav-collapse"
        is-nav
      >
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown
            id="dropdown-text"
            text="Solutions"
            class="m-2"
          >
            <b-dropdown-text style="width: 240px;">
              Create your exams and share in easy way.
            </b-dropdown-text>
            <b-dropdown-divider />
            <b-dropdown-item-button><b>Administer Your Own Exams</b></b-dropdown-item-button>
            <b-dropdown-item-button>Create Exam</b-dropdown-item-button>
            <b-dropdown-item-button>Second Item</b-dropdown-item-button>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown
            id="dropdown-text"
            text="Learn more"
            class="m-2"
          >
            <b-dropdown-text style="width: 240px;">
              Here you can see our price list and take a demo exam.
            </b-dropdown-text>
            <b-dropdown-divider />
            <b-dropdown-item-button><b>Information</b></b-dropdown-item-button>
            <b-dropdown-item-button>
              Pricing
              <b-badge
                variant="primary"
                pill
              >
                Packages
              </b-badge>
            </b-dropdown-item-button>
            <b-button
              class="dropdown-item"
              @click="redirectToTryDemo()"
            >
              Take Demo Exams
              <b-badge
                variant="danger"
                pill
              >
                Try
              </b-badge>
            </b-button>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown
            id="dropdown-text"
            text="Languages"
            class="m-2"
          >
            <b-dropdown-item-button><b>Choose your<br>Language</b></b-dropdown-item-button>
            <b-dropdown-item-button>EN</b-dropdown-item-button>
            <b-dropdown-item-button>
              RU
              <b-badge
                variant="danger"
                pill
              >
                Demo
              </b-badge>
            </b-dropdown-item-button>
            <b-dropdown-item-button>
              PL
              <b-badge
                variant="danger"
                pill
              >
                Demo
              </b-badge>
            </b-dropdown-item-button>
            <b-dropdown-item-button>
              UA
              <b-badge
                variant="danger"
                pill
              >
                Demo
              </b-badge>
            </b-dropdown-item-button>
          </b-nav-item-dropdown>
          <div class="buttons-auth">
            <router-link
              class="btn login-btn btn-outline-primary"
              variant="outline-primary"
              to="/login"
              tag="a"
            >
              Log In
            </router-link>
            <router-link
              class="btn login-btn btn-outline-primary"
              variant="outline-primary"
              to="/registration"
              tag="a"
            >
              Sign up
            </router-link>
          </div>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>

export default {
  name: 'Navigation',
  methods: {
    redirectToTryDemo() {
      this.$router.push({path: '/try-demo'});
    }
  },
};
</script>

<style scoped lang="scss">
.navbar-brand {
  font-size: 1.8rem;
  color: #377DFF !important;
}

.buttons-auth {
  display: flex;
  .login-btn {
    padding: 0.4rem;
    display: flex;
    justify-self: center;
    align-self: center;
  }

  .login-btn:first-child {
    margin-right: 1rem;
  }
}
</style>
