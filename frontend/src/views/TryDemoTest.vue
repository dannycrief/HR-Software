<template>
  <div class="try-free">
    <div v-if="loading">
      <loader
        object="#ff9633"
        color1="#ffffff"
        color2="#17fd3d"
        size="5"
        speed="2"
        bg="#343a40"
        objectbg="#999793"
        opacity="80"
        name="circular"
      />
    </div>
    <Navigation />
    <b-container>
      <b-row class="question-row">
        <p v-if="errors!==''">
          {{ errors }}
        </p>
        <div>
          <b-modal
            ref="modal-center"
            hide-footer
            title="Let us know your email"
          >
            <b-form
              @submit="onSubmitEmail"
            >
              <b-form-group
                id="input-group-1"
                label="Email address:"
                label-for="input-1"
                description="We'll never share your email with anyone else."
              >
                <b-form-input
                  id="input-1"
                  v-model="demoUserEmail"
                  type="email"
                  required
                  placeholder="Enter email"
                />
              </b-form-group>
              <b-button
                class="mt-3"
                variant="outline-danger"
                type="submit"
                block
              >
                Submit
              </b-button>
            </b-form>
          </b-modal>
        </div>
        <b-form
          v-if="errors === '' "
          @submit="onSubmit"
          @reset="onReset"
        >
          <b-form-group
            id="input-group"
            label-for="input-1"
            :label="getQuestion(1)"
          >
            <b-form-input
              id="input-1"
              v-model="form.question_1"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label-for="input-2"
            :label="getQuestion(2)"
          >
            <b-form-input
              id="input-2"
              v-model="form.question_2"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-3"
            label-for="input-3"
            :label="getQuestion(3)"
          >
            <b-form-input
              id="input-3"
              v-model="form.question_3"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-4"
            label-for="input-4"
            :label="getQuestion(4)"
          >
            <b-form-input
              id="input-4"
              v-model="form.question_4"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-5"
            label-for="input-5"
            :label="getQuestion(5)"
          >
            <b-form-input
              id="input-5"
              v-model="form.question_5"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-6"
            label-for="input-6"
            :label="getQuestion(6)"
          >
            <b-form-input
              id="input-6"
              v-model="form.question_6"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-7"
            label-for="input-7"
            :label="getQuestion(7)"
          >
            <b-form-input
              id="input-7"
              v-model="form.question_7"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-8"
            label-for="input-8"
            :label="getQuestion(8)"
          >
            <b-form-input
              id="input-8"
              v-model="form.question_8"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-9"
            label-for="input-9"
            :label="getQuestion(9)"
          >
            <b-form-input
              id="input-9"
              v-model="form.question_9"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-form-group
            id="input-group-10"
            label-for="input-10"
            :label="getQuestion(10)"
          >
            <b-form-input
              id="input-10"
              v-model="form.question_10"
              type="search"
              placeholder="Your answer here"
            />
          </b-form-group>
          <div
            class="buttons"
          >
            <b-button
              v-if="!isHidden && isAPI"
              type="reset"
              variant="danger"
            >
              Reset All
            </b-button>
            <b-button
              v-if="!isHidden && isAPI"
              variant="primary"
              @click="checkAnswers()"
            >
              Submit Answer
            </b-button>
            <b-button
              v-if="isHidden"
              type="submit"
              variant="primary"
              tag="button"
              class="btn btn-primary"
            >
              Show Grade
            </b-button>
          </div>
        </b-form>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Navigation from '../components/Navigation.vue';
import '../assets/styles/trydemotest.scss';
import axios from 'axios';

const BASE_API_URL = 'http://localhost:8080/hr-api';
const MAIN_SERVER_API_URL = 'http://localhost:8080';

export default {
  name: 'TryForFree',
  components: {
    Navigation,
  },

  data() {
    return {
      demoUserEmail: '',
      questions: {
        0: {
          demo_question: '',
          demo_answer_id: '',
        },
        1: {
          demo_question: '',
          demo_answer_id: '',
        },
        2: {
          demo_question: '',
          demo_answer_id: '',
        },
        3: {
          demo_question: '',
          demo_answer_id: '',
        },
        4: {
          demo_question: '',
          demo_answer_id: '',
        },
        5: {
          demo_question: '',
          demo_answer_id: '',
        },
        6: {
          demo_question: '',
          demo_answer_id: '',
        },
        7: {
          demo_question: '',
          demo_answer_id: '',
        },
        8: {
          demo_question: '',
          demo_answer_id: '',
        },
        9: {
          demo_question: '',
          demo_answer_id: '',
        },
        10: {
          demo_question: '',
          demo_answer_id: '',
        },
      },
      form: {
        question_1: '',
        question_2: '',
        question_3: '',
        question_4: '',
        question_5: '',
        question_6: '',
        question_7: '',
        question_8: '',
        question_9: '',
        question_10: '',
      },
      isAPI: false,
      grade: 0,
      isHidden: false,
      errors: '',
      loading: false,
      previousRoute: null,
      isModalWasShowed: false,
      currentTestUUID: null,
    };
  },

  mounted() {
    if (!this.isModalWasShowed) this.showModal();
    if (localStorage.getItem('demo-grade')) {
      localStorage.removeItem('demo-grade');
    }
  },

  methods: {
    getAPI() {
      this.loading = true;
      axios.get(`${BASE_API_URL}/demo_questions/`).then((response) => {
        this.questions = this.shuffle(response.data);
      }).catch((error => {
        this.errors = error;
      })).finally(() => {
        this.isAPI = true;
        this.loading = false;
      });
    },

    showModal() {
      this.$refs['modal-center'].show();
    },

    getQuestion(number) {
      return `${number}) ${JSON.stringify(this.questions[number - 1].demo_question).replace(/['"]+/g, '')}`;
    },

    shuffle(sourceArray) {
      for (let i = 0; i < sourceArray.length - 1; i++) {
        const j = i + Math.floor(Math.random() * (sourceArray.length - i));

        const temp = sourceArray[j];
        sourceArray[j] = sourceArray[i];
        sourceArray[i] = temp;
      }
      return sourceArray;
    },

    async checkAnswers() {
      this.isHidden = true;
      /* eslint-disable no-unused-vars */
      await Object.entries(this.form).forEach(([testKey, testValue]) => {
        for (let i = 0; i < this.questions.length; i++) {
          const currentElement = document.getElementById('input-' + `${i + 1}`);
          if (testValue === this.questions[i].demo_answer_id && testValue !== '') {
            this.grade += 1;
            currentElement.classList.add('active');
          }
        }
      });
      localStorage.setItem('demo-grade', this.grade);
    },

    async onSubmit(evt) {
      evt.preventDefault();
      this.loading = true;

      const requestData = {
        id: this.currentTestUUID,
        demoUserEmail: this.demoUserEmail,
        demoGrade: this.grade,
      };
      const csrf = this.$cookies.get('csrftoken');

      const config = {
        headers: {
          'X-CSRFToken': csrf,
        },
      };

      await axios.post(`${MAIN_SERVER_API_URL}/demo-hr-api/demo-test/`, requestData, config).catch((error) => {
        this.errors = error + '. You see this error because there is a problem with server.' +
          ' Please contact with us to solve this problem.';
      }).finally(() => {
        this.loading = false;
      });

      await setTimeout(() => {
        this.loading = true;
        this.$router.push({path: '/try-demo/grade'});
      }, 0);
    },

    onSubmitEmail: async function (evt) {
      evt.preventDefault();
      this.isModalWasShowed = true;
      this.loading = true;

      const requestData = {
        demoUserEmail: this.demoUserEmail,
      };
      const csrf = this.$cookies.get('csrftoken');

      const config = {
        headers: {
          'X-CSRFToken': csrf,
        }
      };

      await axios.post(`${BASE_API_URL}/demo_user_test/`, requestData, config).then((response) => {
        this.currentTestUUID = response.data.id;
      }).catch((error => {
        this.errors = error + '. You see this error because there is a problem with server.' +
          ' Please contact with us to solve this problem.';
      })).finally(() => {
        this.loading = false;
      });

      await this.$refs['modal-center'].hide();
      await this.getAPI();
      await setTimeout(async () => {
        this.loading = true;
        await this.checkAnswers();
        await document.querySelector('.btn.btn-primary').click();
      }, 600000);
    },

    onReset(evt) {
      evt.preventDefault();
      this.form.question_1 = '';
      this.form.question_2 = '';
      this.form.question_3 = '';
      this.form.question_4 = '';
      this.form.question_5 = '';
      this.form.question_6 = '';
      this.form.question_7 = '';
      this.form.question_8 = '';
      this.form.question_9 = '';
      this.form.question_10 = '';
    },
  },

  beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.previousRoute = from;
    });
  },
};
</script>

