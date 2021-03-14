<template>
  <div class="home">
    <Navigation />
    <div class="main-content">
      <b-container class="bv-container-row">
        <b-row class="bv-row">
          <b-col
            sm="12"
            md="6"
            class="left"
          >
            <div class="left-header">
              <h1>Online Test & Exams Software</h1>
              <h2>The best software for recruiters</h2>
            </div>
            <div class="left-content">
              <p>
                Administer online secure exams to candidates, students or
                employees.
                Create your own tests.
              </p>
            </div>
            <div class="left-footer">
              <router-link
                size="lg"
                variant="primary"
                class="btn try-free-button btn-primary btn-lg"
                to="/try-demo"
                tag="button"
              >
                Try For Free
              </router-link>
              <b-button
                variant="link"
                class="link-button"
              >
                Create exam
                <font-awesome-icon
                  :icon="['fas', 'angle-right']"
                  size="sm"
                />
              </b-button>
            </div>
          </b-col>
          <b-col
            sm="6"
            class="right"
          >
            <b-img
              :src="rightLogo"
              fluid
              alt=""
            />
          </b-col>
        </b-row>
        <h3
          style="text-align: center; margin-bottom: 2rem; margin-top: 2rem; font-size: 1.5rem"
        >
          We create it using
        </h3>
        <b-row class="bv-row-icons">
          <b-col
            cols="4"
            sm="4"
            md="2"
          >
            <font-awesome-icon
              :icon="['fab', 'github']"
              size="lg"
            />
          </b-col>
          <b-col
            cols="4"
            sm="4"
            md="2"
          >
            <font-awesome-icon
              :icon="['fab', 'docker']"
              size="lg"
            />
          </b-col>
          <b-col
            cols="4"
            sm="4"
            md="2"
          >
            <font-awesome-icon
              :icon="['fab', 'python']"
              size="lg"
            />
          </b-col>
          <b-col
            cols="4"
            sm="4"
            md="2"
          >
            <font-awesome-icon
              :icon="['fab', 'vuejs']"
              size="lg"
            />
          </b-col>
          <b-col
            cols="4"
            sm="4"
            md="2"
          >
            <font-awesome-icon
              :icon="['fab', 'node-js']"
              size="lg"
            />
          </b-col>
          <b-col
            cols="4"
            sm="4"
            md="2"
          >
            <font-awesome-icon
              :icon="['fab', 'font-awesome-flag']"
              size="lg"
            />
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
          <b-col
            sm="12"
            md="4"
            data-aos="fade-up"
            data-aos-offset="100"
            data-aos-delay="100"
            data-aos-duration="1000"
            data-aos-easing="ease-in"
            data-aos-mirror="true"
            data-aos-once="true"
            data-aos-anchor-placement="top-center"
          >
            <span class="line">1</span>
            <div class="after-line-content">
              <h1>Create an exam</h1>
              <p>Create your own exam in easy way by using our platform</p>
            </div>
          </b-col>
          <b-col
            sm="12"
            md="4"
            data-aos="fade-up"
            data-aos-offset="100"
            data-aos-delay="600"
            data-aos-duration="1000"
            data-aos-easing="ease-in"
            data-aos-mirror="true"
            data-aos-once="true"
            data-aos-anchor-placement="top-center"
          >
            <span class="line">2</span>
            <div class="after-line-content">
              <h1>Share it</h1>
              <p>
                Share your exam with a group of people that you're
                recruiting
              </p>
            </div>
          </b-col>
          <b-col
            sm="12"
            md="4"
            data-aos="fade-up"
            data-aos-offset="10"
            data-aos-delay="1100"
            data-aos-duration="1000"
            data-aos-easing="ease-in"
            data-aos-mirror="true"
            data-aos-once="true"
            data-aos-anchor-placement="top-center"
          >
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
          <b-col
            cols="12"
            lg="4"
          >
            <h4>
              <font-awesome-icon
                :icon="['far', 'check-circle']"
                size="lg"
              />
              <b>HR</b>Software
            </h4>
            <ul>
              <li>Warsaw, Poland</li>
              <li>+48 575 234 015</li>
              <li>step.kozbvb@gmail.com</li>
            </ul>
          </b-col>
          <b-col
            cols="6"
            md="3"
            lg="2"
          >
            <h5>Company</h5>
            <ul>
              <li><a href="#">About us</a></li>
            </ul>
          </b-col>
          <b-col
            cols="6"
            md="3"
            lg="2"
          >
            <h5>Solutions</h5>
            <ul>
              <li><a href="#">Create a test</a></li>
              <li><a href="#">Question types</a></li>
              <li><a href="#">Reporting</a></li>
              <li><a href="#">Question bank</a></li>
            </ul>
          </b-col>
          <b-col
            cols="6"
            md="3"
            lg="2"
          >
            <h5>Info</h5>
            <ul>
              <li>Languages</li>
              <li>Pricing</li>
              <li>Features List</li>
            </ul>
          </b-col>
          <b-col
            cols="6"
            md="3"
            lg="2"
          >
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
          <b-col
            cols="12"
            style="flex-direction: row; display: flex;"
          >
            <ul class="middle-footer-list">
              <li>English</li>
              <li class="opacity">
                |
              </li>
              <li>Русский</li>
              <li class="opacity">
                |
              </li>
              <li>Polski</li>
              <li class="opacity">
                |
              </li>
              <li>Українська</li>
            </ul>
          </b-col>
        </b-row>
        <hr>
      </b-container>
      <!--  Footer bottom  -->
      <b-container class="footer-bottom">
        <b-row>
          <b-col
            cols="6"
            style="flex-direction: row; display: flex;"
          >
            <ul class="bottom-footer-list">
              <li>Privacy Policy</li>
              <li class="opacity">
                /
              </li>
              <li>Sitemap</li>
            </ul>
          </b-col>
          <b-col
            cols="6"
            style="display: flex; justify-content: flex-end;"
          >
            <ul class="bottom-footer-list">
              <li>
                <a href="#">
                  <font-awesome-icon
                    :icon="['fab', 'facebook-square']"
                    size="lg"
                  />
                </a>
              </li>
              <li class="opacity">
                /
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon
                    :icon="['fab', 'twitter-square']"
                    size="lg"
                  />
                </a>
              </li>
              <li class="opacity">
                /
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon
                    :icon="['fab', 'youtube']"
                    size="lg"
                  />
                </a>
              </li>
            </ul>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="12">
            <p style="text-align: center;color: #677788;">
              © HRSoftware, since
              2020. All rights reserved.
            </p>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import Navigation from '../components/Navigation.vue';
import rightLogo from '../assets/images/right-logo.png';
import '../assets/styles/home.scss';

export default {
  name: 'Home',
  components: {
    Navigation,
  },
  data() {
    return {
      rightLogo,
    };
  },
};
</script>
