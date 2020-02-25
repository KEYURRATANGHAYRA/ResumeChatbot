<template>
  <div
    ref="chatbox"
    class="py-3 flex-1 overflow-y-scroll v-scrollbar-invisible"
  >
    <Message
      v-for="(message, index) in messages"
      :key="index"
      :message="message"
    />
  </div>
</template>
<script>
import Message from "./Message.vue";

export default {
  components: { Message },
  props: {
    messages: {
      type: Array,
      required: true,
    },
  },
  watch: {
    messages() {
      this.scrollToChatEnd();
    },
  },
  methods: {
    scrollToChatEnd() {
      this.$nextTick(() =>
        this.$refs.chatbox.lastChild.scrollIntoView({
          block: "start",
          behavior: "smooth",
        }),
      );
    },
  },
};
</script>
<style scoped>
.v-scrollbar-invisible::-webkit-scrollbar {
  display: none;
}
.v-scrollbar-invisible {
  scrollbar-width: none;
  -ms-overflow-style: none;
}
</style>
