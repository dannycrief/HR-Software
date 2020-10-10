<template>
  <div class="check-password-block">
    <div class="check-letters">
      <div class="big-letter">
        <font-awesome-icon
          id="big-letter"
          :icon="['fas', 'check']"
          size="sm"
        />
        <div class="check-text">
          One big letter
        </div>
      </div>
      <div class="small-letter">
        <font-awesome-icon
          id="small-letter"
          :icon="['fas', 'check']"
          size="sm"
        />
        <div class="check-text">
          One small letter
        </div>
      </div>
    </div>
    <div class="check-numbers">
      <div class="one-number-min">
        <font-awesome-icon
          id="one-number"
          :icon="['fas', 'check']"
          size="sm"
        />
        <div class="check-text">
          One number
        </div>
      </div>
      <div class="eight-symbols-min">
        <font-awesome-icon
          id="eight-symbols"
          :icon="['fas', 'check']"
          size="sm"
        />
        <div class="check-text">
          Eight symbols
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CheckPassword",
  data() {
    return {
      show: true,
    };
  }
};
</script>

