<template>
  <div class="demo-test-grade">
    <Navigation />
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
    <b-container>
      <b-row>
        <div class="gradient-border">
          Grade
          <br>
          {{ grade }}
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Navigation from "../components/Navigation";

export default {
  name: "DemoTestGrade",
  components: {
    Navigation,
  },
  data() {
    return {
      grade: null,
      loading: false,
    };
  },
  mounted() {
    this.showPreloader().then(() => {
      this.grade = localStorage.getItem('demo-grade');
    });
  },

  methods: {
    async showPreloader() {
      this.loading = await localStorage.getItem('demo-grade') === "null";
    },
  },

};
</script>
