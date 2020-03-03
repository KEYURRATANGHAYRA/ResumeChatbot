<template>
  <div class="pb-3">

  <div style="float: right; margin-bottom: 10px;">
  <button v-for="item in buttons"
        v-on:click="buttonClick(item.value)"
        class="bg-gray-300 text-black font-bold py-2 px-4 rounded opacity-50" style="margin:5px;">
  {{ item.name }}
  </button>
  </div>

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
      buttons: [
          { name: 'Experience', value: 'Could you tell me about her work experience?'},
          { name: 'Education', value: 'What did she study?'},
          { name: 'Skills', value: 'Could you tell me about her skills?'},
          { name: 'Contact', value: 'How can I contact Lena?'},
          { name: '?', value: 'How can you help?'}
      ]
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
    buttonClick(buttonItem) {
      let message = buttonItem;
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
