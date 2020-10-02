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

<style scoped lang="scss">
.container {
  height: calc(100vh - 72px);
  display: flex;
  justify-content: center;
  align-items: center;

  .gradient-border {
    --border-width: 3px;

    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 12rem;
    height: 12rem;
    font-family: Lato, sans-serif;
    font-size: 2.5rem;
    text-transform: uppercase;
    text-align: center;
    color: white;
    background: #222;
    border-radius: 50%;

    &::after {
      position: absolute;
      content: "";
      top: calc(-1 * var(--border-width));
      left: calc(-1 * var(--border-width));
      z-index: -1;
      width: calc(100% + var(--border-width) * 2);
      height: calc(100% + var(--border-width) * 2);
      background: linear-gradient(60deg, hsl(224, 85%, 66%), hsl(269, 85%, 66%), hsl(314, 85%, 66%), hsl(359, 85%, 66%), hsl(44, 85%, 66%), hsl(89, 85%, 66%), hsl(134, 85%, 66%), hsl(179, 85%, 66%));
      background-size: 300% 300%;
      background-position: 0 50%;
      border-radius: calc(2 * var(--border-width));
      animation: moveGradient 4s alternate infinite;
    }
  }

  @keyframes moveGradient {
    50% {
      background-position: 100% 50%;
    }
  }

}
</style>
