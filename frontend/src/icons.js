import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faCheckCircle } from '@fortawesome/free-regular-svg-icons';
import { faAngleRight } from '@fortawesome/free-solid-svg-icons';
import {
  faGithub, faDocker,
  faPython, faVuejs,
  faNodeJs, faFontAwesomeFlag,
  faFacebookSquare, faTwitterSquare,
  faYoutube,
} from '@fortawesome/free-brands-svg-icons';

library.add(faCheckCircle, faAngleRight, faGithub,
  faDocker, faPython, faVuejs, faNodeJs, faFontAwesomeFlag,
  faFacebookSquare, faTwitterSquare, faYoutube);
Vue.component('font-awesome-icon', FontAwesomeIcon);
