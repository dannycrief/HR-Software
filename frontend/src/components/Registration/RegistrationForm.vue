<template>
  <div class="registration">
    <b-form
      class="registration-form"
      @submit="onSubmit"
    >
      <b-form-group
        id="name-input-group"
        label="Name"
        label-for="name"
      >
        <b-form-input
          id="name"
          v-model="form.name"
          required
          placeholder="Enter name"
        />
      </b-form-group>

      <b-form-group
        id="surname-input-group"
        label="Surname"
        label-for="surname"
      >
        <b-form-input
          id="surname"
          v-model="form.surname"
          required
          placeholder="Enter surname"
        />
      </b-form-group>

      <b-form-group
        id="email-input-group"
        label="Email"
        label-for="email"
      >
        <b-form-input
          id="email"
          v-model="form.email"
          type="email"
          required
          placeholder="Enter email"
        />
      </b-form-group>

      <b-form-group
        id="password-input-group"
        label="Password"
        label-for="password"
      >
        <b-form-input
          id="password"
          v-model="form.password"
          type="password"
          required
          placeholder="Enter password"
          @input="showCheckPasswordBlock"
        />
      </b-form-group>
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
import CheckPassword from "./CheckPassword";

export default {
  name: 'RegistrationForm',
  components: {
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

    showCheckPasswordBlock: function () {
      const password = this.form.password;
      this.characters.push(password.length);
      this.showCheckPassword = password !== '';
      // TODO: Make something like this on deleting. When characters.length - 1 < characters.length - 2
      setTimeout(() => {
        if (password.slice(-1) !== ' ' && this.characters[this.characters.length - 1] > this.characters[this.characters.length - 2]) {
          /\d/.test(password.slice(-1))
            ? this.changeColorOnType('#one-number', '#007bff')
            : /^[A-Z]/.test(password.slice(-1)) && this.changeColorOnType('#big-letter', '#007bff')
            || /^[a-z]/.test(password.slice(-1)) && this.changeColorOnType('#small-letter', '#007bff');
        }
        password.length === 8 && this.changeColorOnType('#eight-symbols', '#007bff');
      }, 0);

    },
    changeColorOnType(element, color) {
      document.querySelector(`${element}`).style.backgroundColor = `${color}`;
      document.querySelector(`${element}+div`).style.textDecoration = 'line-through';
      document.querySelector(`${element}+div`).style.color = 'grey';
    },
  }
};
</script>
