<template>
  <div class="try-free">
    <!--  Navigation starts  -->
    <Navigation></Navigation>

    <b-container>
      <b-row class="question-row">
        <b-form @submit="onSubmit" @reset="onReset">
          <b-form-group id="input-group"
                        :label="getQuestion(1)"
                        label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.question_1"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2"
                        :label="getQuestion(2)"
                        label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.question_2"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3"
                        :label="getQuestion(3)"
                        label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="form.question_3"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-4"
                        :label="getQuestion(4)"
                        label-for="input-4">
            <b-form-input
              id="input-4"
              v-model="form.question_4"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-5"
                        :label="getQuestion(5)"
                        label-for="input-5">
            <!--
            TODO: set v-model value on js side. Like question1, question2, etc
            -->
            <b-form-input
              id="input-5"
              v-model="form.question_5"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-6"
                        :label="getQuestion(6)"
                        label-for="input-6">
            <b-form-input
              id="input-6"
              v-model="form.question_6"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-7"
                        :label="getQuestion(7)"
                        label-for="input-7">
            <b-form-input
              id="input-7"
              v-model="form.question_7"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-8"
                        :label="getQuestion(8)"
                        label-for="input-8">
            <b-form-input
              id="input-8"
              v-model="form.question_8"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-9"
                        :label="getQuestion(9)"
                        label-for="input-9">
            <b-form-input
              id="input-9"
              v-model="form.question_9"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-form-group id="input-group-10"
                        :label="getQuestion(10)"
                        label-for="input-10">
            <b-form-input
              id="input-10"
              v-model="form.question_10"
              required
              placeholder="Your answer here">
            </b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
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
  methods: {
    getAPI() {
      axios.get(`${BASE_API_URL}/demo_questions/`).then((response) => {
        this.questions = response.data;
      });
    },

    getQuestion(taskNumber) {
      const currentQuestion = this.questions[this.randomArray[taskNumber - 1]].demo_question;
      return `${taskNumber}) ${JSON.stringify(currentQuestion).replace(/['"]+/g, '')}`;
    },

    getRandomInt() {
      while (this.randomArray.length < 10) {
        const randomNumber = Math.floor(Math.random() * 10);
        if (this.randomArray.indexOf(randomNumber) === -1) this.randomArray.push(randomNumber);
      }
      return this.randomArray;
    },

    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },

    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
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
  mounted() {
    this.getAPI();
    this.getRandomInt();
  },
  data() {
    return {
      questions: {},
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
      randomArray: [],
    };
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
