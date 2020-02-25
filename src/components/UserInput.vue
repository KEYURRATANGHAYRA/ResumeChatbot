<template>
  <div class="pb-3">
    <input
      class="bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal"
      @keyup.enter="getBotResponse()"
      v-model="userMessage"
      name="message"
      autofocus
      placeholder="Your message..."
    />
  </div>
</template>
<script>
export default {
  data() {
    return {
      userMessage: "",
    };
  },
  methods: {
    getBotResponse() {
      let message = this.userMessage;
      if (!message) return;

      this.userMessage = "";
      this.$emit("addMessage", { text: message, sender: "user" });

      fetch(`/get?msg=${message}`)
        .then(response => response.text())
        .then(botMessage => {
          this.$emit("addMessage", { text: botMessage, sender: "bot" });
        });
    },
  },
};
</script>
