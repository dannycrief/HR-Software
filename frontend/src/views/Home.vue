<template>
  <div class="home">
    <Navigation></Navigation>
    <div class="main-content">
      <b-container class="bv-container-row">
        <b-row class="bv-row">
          <b-col sm="12" md="6" class="left">
            <div class="left-header">
              <h1>Online Test & Exams Software</h1>
              <h2>The best software for recruiters</h2>
            </div>
            <div class="left-content">
              <p>Administer online secure exams to candidates, students or employees.
                Create your own tests.</p>
            </div>
            <div class="left-footer">
              <b-button size="lg" variant="primary" class="try-free-button">Try for free</b-button>
              <b-button variant="link" class="link-button">Schedule a demo
                <font-awesome-icon :icon="['fas', 'angle-right']" size="sm"/>
              </b-button>
            </div>
          </b-col>
          <b-col sm="6" class="right">
            <b-img :src="rightLogo" fluid alt=""></b-img>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <div class="instruction-content">
      <b-container class="bv-example-row">
        <b-row>
          <b-col sm="12" md="4">
            <span class="line">1</span>
            <h1>Create an exam</h1>
            <p>Create your own exam in easy way by using our platform</p>
          </b-col>
          <b-col sm="12" md="4">
            <span class="line">2</span>
            <h1>Share it</h1>
            <p>Share your exam with a group of people that you recruit</p>
          </b-col>
          <b-col sm="12" md="4">
            <span>3</span>
            <h1>See results</h1>
            <p>The results you will see here or we can send by email</p>
          </b-col>
        </b-row>
      </b-container>
    </div>

    <div class="footer-content">
      <b-container class="bv-example-row">
        <b-row>
          <h1>hello footer</h1>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import Navigation from '@/components/Navigation.vue';
import rightLogo from '../assets/right-logo.jpg';

export default {
  name: 'Home',
  data() {
    return {
      rightLogo,
    };
  },
  components: {
    Navigation,
  },
};
</script>

<style lang="scss">
@media (max-width: 767px) {
  .right {
    display: none;
  }
}

.bv-container-row {
  margin-top: 3.5rem;

  .bv-row {
    justify-content: center;
    align-items: center;
  }

  .left-header {
    h1 {
      color: #1e2022;
      font-size: 1.5rem;
      font-weight: bold;
      line-height: 1.4;
    }

    h2 {
      text-transform: uppercase;
      color: #8ca7b6;
      font-style: italic;
      font-size: 0.9rem;
      margin-bottom: 1.5rem;
      line-height: 1.4;
    }
  }

  .left-content {
    margin-top: 0;
    margin-bottom: 2rem;
    color: #677788;
    font-size: 1rem;
    line-height: 1.6;
  }

  .left-footer {
    .try-free-button {
      box-shadow: 0 4px 11px rgba(55, 125, 255, 0.35);
      transition: all 0.2s ease-in-out;
      min-width: 10rem;
      margin-right: 1rem;
      margin-bottom: 0.5rem;
    }

    .try-free-button:focus,
    .try-free-button:hover {
      webkit-transform: translateY(-3px);
      transform: translateY(-3px);
    }

    .link-button {
      text-decoration: none;
    }
  }
}

.instruction-content {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #F7FAFF;
  height: 300px;

  .bv-example-row {
    .row {
      .col-sm-12.col-md-4 {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1rem;
        flex-direction: column;

        span {
          color: #377dff;
          background-color: rgba(55, 125, 255, 0.1);
          height: 3.125rem;
          width: 3.125rem;
          border-radius: 50%;
          font-size: 1rem;
          font-weight: bold;
          display: flex;
          justify-content: center;
          align-items: center;
        }

        span.line::after {
          position: absolute;
          top: 3.59375rem;
          left: 50%;
          height: calc(100% - 2.65625rem);
          border-left: 0.125rem solid #e7eaf3;
          content: "";
        }

        @media (min-width: 768px) {
          span.line::after {
            top: 1.5625rem;
            width: calc(100% - 4.85rem);
            left: calc(50% + 2.5rem);
            height: 1.0625rem;
            border-top: 0.125rem solid #e7eaf3;
            border-left: none;
          }
        }

        h1 {
          font-size: 1.2rem;
          font-weight: bold;
        }

        p {
          text-align: center;
        }
      }
    }
  }
}

.footer-content {
  height: 300px;
  background-color: black;
}
</style>
