<template>
  <div class="try-free">
    <Navigation />
    <b-container>
      <b-row class="question-row">
        <b-form
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
              placeholder="Your answer here"
            />
          </b-form-group>

          <b-button
            type="submit"
            variant="primary"
          >
            Submit
          </b-button>
          <b-button
            type="reset"
            variant="danger"
          >
            Reset
          </b-button>
        </b-form>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';
import Navigation from '@/components/Navigation.vue';

const BASE_API_URL = 'http://localhost:8080/hr-api';

export default {
  name: 'TryForFree',
  components: {
    Navigation,
  },

  data() {
    return {
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
      grade: 0,
    };
  },
  mounted() {
    this.getAPI();
  },

  methods: {
    getAPI() {
      axios.get(`${BASE_API_URL}/demo_questions/`).then((response) => {
        this.questions = this.shuffle(response.data);
      });

      axios.get(`${BASE_API_URL}/demo_answers/`).then((response) => {
        this.answers = response.data;
      });
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

    checkAnswers() {
      /* eslint-disable no-unused-vars */
      Object.entries(this.form).forEach(([testKey, testValue]) => {
        for (let i = 0; i < this.questions.length; i++) {
          if (testValue === this.questions[i].demo_answer_id) {
            this.grade += 1;
          }
        }
      });
    },

    onSubmit(evt) {
      evt.preventDefault();
      this.checkAnswers();
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
};
</script>

<style scoped lang="scss">
.questions-block {
  height: calc(100vh - 72px);
}
.question-row {
  color: #377dff;

  min-width: calc(100% - 5rem);
  font-size: 1rem;
  font-weight: bold;
  display: flex;
  justify-content: flex-start;
  align-items: center;

  form {
    width: 100%;
    margin: 0.5rem 1rem;

    .form-group {
      background-color: rgba(55, 125, 255, 0.1);
      border-radius: 1rem;
      padding: 1rem;
      margin: 1rem 0 !important;
    }
  }

}
</style>
