<template>
  <div class="try-free">
    <!--  Navigation starts  -->
    <Navigation></Navigation>

    <b-container>
      <b-row class="question-row">
        <b-form @submit="onSubmit" @reset="onReset">
          <b-form-group id="input-group"
                        v-for="(question, index) in questions"
                        :key="question.id"
                        label-for="input">
            <p>{{ index + 1 }}) {{ question.demo_question }} - ?</p>
            <!--
            TODO: set v-model value on js side. Like question1, question2, etc
            -->
            <b-form-input
              id="input"
              v-model="form.question"
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

const BASE_API_URL = 'http://localhost:8080/hr-api/';

export default {
  name: 'TryForFree',
  components: {
    Navigation,
  },
  methods: {
    getAPI() {
      axios.get(`${BASE_API_URL}demo_questions/`).then((response) => {
        this.questions = response.data;
      });
    },

    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = '';
      // Trick to reset/clear native browser form validation state
    },
  },
  mounted() {
    this.getAPI();
  },
  data() {
    return {
      questions: {},
      form: {
        question1: '',
        question2: '',
        question3: '',
        // question4: '',
        // question5: '',
        // question6: '',
        // question7: '',
        // question8: '',
        // question9: '',
        // question10: '',
      },
    };
  },
};
</script>

<style scoped lang="scss">
.questions-block {
  height: calc(100vh - 72px);
  /*background-color: #F7FAFF;*/
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
