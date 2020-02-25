<template>
  <div :class="{'mb-5 flex justify-end': message.sender === 'user', 'mb-5 flex': message.sender === 'bot'}">
    <div
      class="p-4 rounded-lg"
      :class="{
        'lg:mr-24 md:mr-12 sm:mr-12 bg-gray-200': message.sender === 'bot',
        'lg:ml-24 md:ml-12 sm:ml-12 bg-blue-200': message.sender === 'user',
      }"
    >
      <span class="text-lg">{{ message.text }}</span>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    message: {
      type: Object,
      required: true,
    },
  },
};
</script>
