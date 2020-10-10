<template>
  <div class="registration">
    <b-form
      class="registration-form"
      @submit="onSubmit"
    >
      <mdb-input
        v-model="form.name"
        label="Name"
      />

      <mdb-input
        v-model="form.surname"
        label="Surname"
      />

      <mdb-input
        v-model="form.email"
        label="Email"
        type="email"
      />

      <mdb-input
        v-model="form.password"
        label="Password"
        type="password"
        @input="showCheckPasswordBlock"
      />

      <transition name="fade">
        <CheckPassword v-if="showCheckPassword" />
      </transition>

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
import {mdbInput} from 'mdbvue';
import CheckPassword from "./CheckPassword";

export default {
  name: 'RegistrationForm',
  components: {
    mdbInput,
    CheckPassword,
  },
  data() {
    return {
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
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
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
  }
};
</script>
