<template>
  <div class="registration">
    <Error
      v-if="errorMessage"
      :message="errorMessage"
    />
    <b-form
      class="registration-form"
      novalidate
      @submit="onSubmit"
    >
      <mdb-input
        v-model="form.name"
        label="Name"
        outline
        required
        alid-feedback="Look's good."
        invalid-feedback="Please enter your name."
      />

      <mdb-input
        v-model="form.surname"
        label="Surname"
        outline
        invalid-feedback="Please enter your surname."
        alid-feedback="Look's good."
        required
      />

      <mdb-input
        v-model="form.email"
        label="Email"
        type="email"
        outline
        invalid-feedback="Please provide a valid email."
        required
      />

      <mdb-input
        v-model="form.password"
        label="Password"
        type="password"
        outline
        required
        invalid-feedback="Please provide a valid password."
        @input="showCheckPasswordBlock"
      />

      <transition name="fade">
        <CheckPassword v-if="showCheckPassword" />
      </transition>

      <div class="form-group">
        <div class="form-check pl-0">
          <input
            id="invalidCheck"
            class="form-check-input"
            type="checkbox"
            value=""
            required
          >
          <label
            class="form-check-label"
            for="invalidCheck"
          >Agree to
            <router-link
              to="/"
              style="color: inherit; text-decoration: underline"
            >
              terms and conditions
            </router-link>
          </label>
          <div class="invalid-feedback">
            You must agree before submitting.
          </div>
        </div>
      </div>
      <b-button
        type="submit"
        variant="primary"
      >
        Submit
      </b-button>
    </b-form>
  </div>
</template>

<script>
import CheckPassword from "./CheckPassword";
import Error from '../Error';
import {mdbInput} from 'mdbvue';

export default {
  name: 'RegistrationForm',
  components: {
    mdbInput,
    CheckPassword,
    Error,
  },
  data() {
    return {
      errorMessage: '',
      showCheckPassword: false,
      characters: [0],
      name: '',
      form: {
        name: '',
        surname: '',
        email: '',
        password: '',
      },
    };
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();
      event.target.classList.add('was-validated');
      this.checkPasswordValidation();
      // TODO: here must be axios.post & create a new user
      // setTimeout(() => {
      // if (this.errorMessage === '') axios.post
      // }, 0);
    },

    showCheckPasswordBlock() {
      const password = this.form.password;
      const characters = this.characters;
      let number = 0, bigLetter = 0, smallLetter = 0;

      characters.push(password.length);
      this.showCheckPassword = password !== '';
      setTimeout(() => {
        characters[0] = password === '';
        if (password.slice(-1) !== ' ') {
          if (characters[characters.length - 1] > characters[characters.length - 2]) {
            // TODO: make it better by searching in all password, not only at last symbol
            /\d/.test(password.slice(-1))
              ? this.changeColorOnType('#one-number', '#007bff')
              : /^[A-Z]/.test(password.slice(-1)) && this.changeColorOnType('#big-letter', '#007bff')
              || /^[a-z]/.test(password.slice(-1)) && this.changeColorOnType('#small-letter', '#007bff');
          } else {
            for (let char of password) {
              if (/\d/.test(char)) number += 1;
              if (/^[A-Z]/.test(char)) bigLetter += 1;
              if (/^[a-z]/.test(char)) smallLetter += 1;
            }
            number === 0 && this.resetAttributes('#one-number', 'style');
            bigLetter === 0 && this.resetAttributes('#big-letter', 'style');
            smallLetter === 0 && this.resetAttributes('#small-letter', 'style');
          }
        }
        password.length === 8 && this.changeColorOnType('#eight-symbols', '#007bff');

        password.length < 8 && this.resetAttributes('#eight-symbols', 'style');
      }, 0);

    },

    changeColorOnType(element, color) {
      document.querySelector(`${element}`).style.backgroundColor = `${color}`;
      document.querySelector(`${element}+div`).style.textDecoration = 'line-through';
      document.querySelector(`${element}+div`).style.color = 'grey';
    },

    resetAttributes(element, attribute) {
      if (document.querySelector(`${element}`).hasAttribute(attribute)) {
        document.querySelector(`${element}`).removeAttribute(attribute);
        document.querySelector(`${element}+div`).removeAttribute(attribute);
      }
    },

    checkPasswordValidation() {
      this.errorMessage = '';
      const bigLetter = document.querySelector('#big-letter');
      const smallLetter = document.querySelector('#small-letter');
      const eightSymbols = document.querySelector('#eight-symbols');
      const oneNumber = document.querySelector('#one-number');
      const rightColor = 'rgb(0, 123, 255)';
      if (bigLetter.style.backgroundColor !== rightColor) this.errorMessage += 'Password must contain minimum one big letter';
      if (smallLetter.style.backgroundColor !== rightColor) this.errorMessage += ' Password must contain minimum one small letter';
      if (eightSymbols.style.backgroundColor !== rightColor) this.errorMessage += ' Password must contain minimum eight symbols';
      if (oneNumber.style.backgroundColor !== rightColor) this.errorMessage += ' Password must contain minimum one number';
    }
  }
};
</script>
