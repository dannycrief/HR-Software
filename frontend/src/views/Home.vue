<template>
  <div class="home">
    <!--  Navigation starts  -->
    <Navigation></Navigation>
    <!--  Main content starts  -->
    <div class="main-content">
      <b-container class="bv-container-row">
        <b-row class="bv-row">
          <b-col sm="12" md="6" class="left">
            <div class="left-header">
              <h1>Online Test & Exams Software</h1>
              <h2>The best software for recruiters</h2>
            </div>
            <div class="left-content">
              <p>Administer online secure exams to candidates, students or
                employees.
                Create your own tests.</p>
            </div>
            <div class="left-footer">
              <b-button size="lg" variant="primary" class="try-free-button"
                        to="try-demo">
                Try for free
              </b-button>
              <b-button variant="link" class="link-button">Create exam
                <font-awesome-icon :icon="['fas', 'angle-right']" size="sm"/>
              </b-button>
            </div>
          </b-col>
          <b-col sm="6" class="right">
            <b-img :src="rightLogo" fluid alt=""></b-img>
          </b-col>
        </b-row>
        <h3
          style="text-align: center; margin-bottom: 2rem; margin-top: 2rem; font-size: 1.5rem">
          We create it using
        </h3>
        <b-row class="bv-row-icons">
          <b-col cols="4" sm="4" md="2">
            <font-awesome-icon :icon="['fab', 'github']" size="lg"/>
          </b-col>
          <b-col cols="4" sm="4" md="2">
            <font-awesome-icon :icon="['fab', 'docker']" size="lg"/>
          </b-col>
          <b-col cols="4" sm="4" md="2">
            <font-awesome-icon :icon="['fab', 'python']" size="lg"/>
          </b-col>
          <b-col cols="4" sm="4" md="2">
            <font-awesome-icon :icon="['fab', 'vuejs']" size="lg"/>
          </b-col>
          <b-col cols="4" sm="4" md="2">
            <font-awesome-icon :icon="['fab', 'node-js']" size="lg"/>
          </b-col>
          <b-col cols="4" sm="4" md="2">
            <font-awesome-icon :icon="['fab', 'font-awesome-flag']" size="lg"/>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <!--  Second menu starts  -->
    <div class="instruction-content">
      <!--  First container starts  -->
      <b-container class="bv-container-one-row">
        <b-row>
          <b-col>
            <span>Did you ever seen something like this before?</span>
          </b-col>
          <b-col>
            <h3>Learn how use our software in 3 easy steps</h3>
          </b-col>
        </b-row>
      </b-container>
      <!--  Second container starts  -->
      <b-container class="bv-container-two-row">
        <b-row>
          <b-col sm="12" md="4"
                 data-aos="fade-up"
                 data-aos-offset="100"
                 data-aos-delay="100"
                 data-aos-duration="1000"
                 data-aos-easing="ease-in"
                 data-aos-mirror="true"
                 data-aos-once="true"
                 data-aos-anchor-placement="top-center">
            <span class="line">1</span>
            <div class="after-line-content">
              <h1>Create an exam</h1>
              <p>Create your own exam in easy way by using our platform</p>
            </div>
          </b-col>
          <b-col sm="12" md="4"
                 data-aos="fade-up"
                 data-aos-offset="100"
                 data-aos-delay="600"
                 data-aos-duration="1000"
                 data-aos-easing="ease-in"
                 data-aos-mirror="true"
                 data-aos-once="true"
                 data-aos-anchor-placement="top-center">
            <span class="line">2</span>
            <div class="after-line-content">
              <h1>Share it</h1>
              <p>Share your exam with a group of people that you're
                recruiting</p>
            </div>
          </b-col>
          <b-col sm="12" md="4"
                 data-aos="fade-up"
                 data-aos-offset="10"
                 data-aos-delay="1100"
                 data-aos-duration="1000"
                 data-aos-easing="ease-in"
                 data-aos-mirror="true"
                 data-aos-once="true"
                 data-aos-anchor-placement="top-center">
            <span>3</span>
            <div class="after-line-content">
              <h1>See results</h1>
              <p>The results you can see here or we can also send by email</p>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <!--  Footer starts  -->
    <div class="footer-content">
      <!--  Footer top  -->
      <b-container class="footer-top">
        <b-row>
          <b-col cols="12" lg="4">
            <h4>
              <font-awesome-icon :icon="['far', 'check-circle']" size="lg"/>
              <b>HR</b>Software
            </h4>
            <ul>
              <li>Warsaw, Poland</li>
              <li>+48 575 234 015</li>
              <li>step.kozbvb@gmail.com</li>
            </ul>
          </b-col>
          <b-col cols="6" md="3" lg="2">
            <h5>Company</h5>
            <ul>
              <li><a href="#">About us</a></li>
            </ul>
          </b-col>
          <b-col cols="6" md="3" lg="2">
            <h5>Solutions</h5>
            <ul>
              <li><a href="#">Create a test</a></li>
              <li><a href="#">Question types</a></li>
              <li><a href="#">Reporting</a></li>
              <li><a href="#">Question bank</a></li>
            </ul>
          </b-col>
          <b-col cols="6" md="3" lg="2">
            <h5>Info</h5>
            <ul>
              <li>Languages</li>
              <li>Pricing</li>
              <li>Features List</li>
            </ul>
          </b-col>
          <b-col cols="6" md="3" lg="2">
            <h5>Links</h5>
            <ul>
              <li>Help Center</li>
              <li>Newsletters</li>
              <li>Your account</li>
            </ul>
          </b-col>
        </b-row>
      </b-container>
      <!--  Footer middle  -->
      <b-container class="footer-middle">
        <b-row>
          <b-col cols="12" style="flex-direction: row; display: flex;">
            <ul class="middle-footer-list">
              <li>English</li>
              <li class="opacity">|</li>
              <li>Русский</li>
              <li class="opacity">|</li>
              <li>Polski</li>
              <li class="opacity">|</li>
              <li>Українська</li>
            </ul>
          </b-col>
        </b-row>
        <hr>
      </b-container>
      <!--  Footer bottom  -->
      <b-container class="footer-bottom">
        <b-row>
          <b-col cols="6" style="flex-direction: row; display: flex;">
            <ul class="bottom-footer-list">
              <li>Privacy Policy</li>
              <li class="opacity">/</li>
              <li>Sitemap</li>
            </ul>
          </b-col>
          <b-col cols="6" style="display: flex; justify-content: flex-end;">
            <ul class="bottom-footer-list">
              <li><a href="#">
                <font-awesome-icon :icon="['fab', 'facebook-square']"
                                   size="lg"/>
              </a></li>
              <li class="opacity">/</li>
              <li><a href="#">
                <font-awesome-icon :icon="['fab', 'twitter-square']" size="lg"/>
              </a></li>
              <li class="opacity">/</li>
              <li><a href="#">
                <font-awesome-icon :icon="['fab', 'youtube']" size="lg"/>
              </a></li>
            </ul>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="12">
            <p style="text-align: center;color: #677788;">© HRSowftware, since
              2020. All rights reserved.</p>
          </b-col>
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

<style scoped lang="scss">
@media (max-width: 767px) {
  .right {
    display: none;
  }
}

@media (min-width: 1200px) {
  .main-content {
    height: calc(100vh - 80px);
    margin-bottom: 0 !important;
  }
}

.main-content {
  margin-bottom: 4rem;
}

.bv-container-row {
  margin-top: 3.5rem;

  .bv-row {
    justify-content: center;
    align-items: center;
  }

  .bv-row-icons {
    .col-sm-4, .col-md-2 {
      display: flex;
      justify-content: center;
      align-items: center;

      svg {
        font-size: 3rem;
      }
    }
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

.bv-container-row.container > .row + .row {
}

.instruction-content {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  background-color: #F7FAFF;
  margin-bottom: 5rem;
  padding-top: 4rem;
  padding-bottom: 4rem;

  .bv-container-one-row {
    .row {
      display: flex;
      flex-direction: column;
      justify-content: center;
      margin-left: auto;
      margin-right: auto;
      text-align: center;

      .col {
        margin: 0.5rem 0;

        span {
          text-transform: uppercase;
          letter-spacing: 0.03125rem;
          font-weight: 600;
          color: #677788;
        }

        h3 {
          color: #1e2022;
          margin-bottom: 1.5rem;
          font-weight: 600;
          line-height: 1.4;
          font-size: calc(1.25625rem + 0.075vw)
        }
      }
    }
  }

  .bv-container-two-row {
    .row {
      @media (max-width: 767px) {
        .col-sm-12.col-md-4 {
          display: flex !important;
          flex-direction: row !important;
        }
      }

      .col-sm-12.col-md-4 {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        flex-direction: column;

        span {
          color: #377dff;
          background-color: rgba(55, 125, 255, 0.1);
          min-height: 3.125rem;
          min-width: 3.125rem;
          border-radius: 50%;
          font-size: 1rem;
          font-weight: bold;
          display: flex;
          justify-content: center;
          align-items: center;
          margin-right: 1rem;
        }

        span.line::after {
          position: absolute;
          top: 5rem;
          left: 2.4rem;
          height: calc(100% - 3rem);
          border-left: 0.125rem solid #e7eaf3;
          content: "";
          //position: absolute;
          //top: 3.59375rem;
          //left: 1.5625rem;
          //height: calc(100% - 2.65625rem);
          //border-left: 0.125rem solid #e7eaf3;
          //content: "";
        }

        @media (min-width: 768px) {
          span.line::after {
            top: 1.5625rem;
            width: calc(100% - 4.85rem);
            left: calc(50% + 2rem);
            height: 1.0625rem;
            border-top: 0.125rem solid #e7eaf3;
            border-left: none;
          }
        }

        .after-line-content {
          display: flex;
          flex-direction: column;
          @media (min-width: 768px) {
            h1 {
              text-align: center;
            }
            p {
              text-align: center;
            }
          }

          h1 {
            font-size: calc(1.25625rem + 0.075vw);
            font-weight: bold;
            color: #1e2022;
          }

          p {
            font-size: 1rem;
            color: #677788;
          }
        }
      }
    }
  }

}

.footer-content {
  background-color: #21325B;
  color: white;
  padding-top: 3rem;

  hr {
    border-top: 0.0625rem solid #e7eaf3;
    opacity: .2;
    margin: 3rem 0;
  }

  .footer-top {
    ul {
      margin-top: 1.5rem;
      padding: 0;
    }

    li {
      list-style: none;
      color: rgba(255, 255, 255, 0.7);
      padding: 0.5rem 0;

      a {
        color: rgba(255, 255, 255, 0.7);
        text-decoration: none;
      }

      a:hover {
        color: white;
      }
    }

    li:hover {
      color: white;
    }
  }

  .footer-middle {
    .middle-footer-list {
      display: flex;
      -ms-flex-wrap: wrap;
      flex-wrap: wrap;
      padding-left: 0;
      margin-bottom: 0;
      list-style: none;
      color: rgba(255, 255, 255, 0.7);

      li:hover {
        color: white;
      }

      .opacity {
        opacity: 0.6;
        margin-left: 1rem;
        margin-right: 1rem;
      }
    }
  }

  .footer-bottom {
    .bottom-footer-list {
      display: flex;
      -ms-flex-wrap: wrap;
      flex-wrap: wrap;
      padding-left: 0;
      margin-bottom: 0;
      list-style: none;
      color: rgba(255, 255, 255, 0.7);

      a {
        color: rgba(255, 255, 255, 0.7);
      }

      li:hover {
        color: white;
      }

      .opacity {
        opacity: 0.6;
        margin-left: 1rem;
        margin-right: 1rem;
      }
    }
  }
}
</style>
