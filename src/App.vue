<template>
  <div class="container m-auto max-w-xl md:px-6 sm:px-3 flex flex-col h-full">
    <div>
      <div class="mb-3" style="text-align:center">
        <h1 class="text-5xl">ResumeBot</h1>
        <h3 class="text-3xl">
          by
          <a href="https://shakurova.io" target="_blank" class="text-blue-600"
            >Lena Shakurova</a
          >
        </h3>
      </div>
    </div>
    <ChatBox :messages="messages" />
    <UserInput @addMessage="addMessage" />
  </div>
</template>
<script>
import ChatBox from "./components/ChatBox.vue";
import UserInput from "./components/UserInput.vue";

export default {
  components: { ChatBox, UserInput },
  data() {
    return {
      messages: [
        {
          text:
            "👋 Hi! I'm ResumeBot, you can ask me questions about Lena Shakurova and I'll try to do my best to answer you!",
          sender: "bot",
        },
      ],
    };
  },
  mounted() {},
  methods: {
    addMessage(message) {
      this.messages.push(message);
    },
  },
};
</script>
