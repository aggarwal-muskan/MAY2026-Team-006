<template>
  <div class="chatbot">
    <section v-if="isOpen" class="chat-panel" aria-label="SocioNeed AI Assistant">
      <header class="chat-header">
        <div>
          <h2>SocioNeed AI Assistant</h2>
          <p>Ask about using SocioNeed</p>
        </div>
        <button class="chat-close" type="button" aria-label="Close chat" @click="isOpen = false">×</button>
      </header>

      <div class="chat-messages" aria-live="polite">
        <div v-if="!messages.length" class="chat-empty">
          Ask a question about bookings, complaints, notices, or services.
        </div>
        <div
          v-for="(message, index) in messages"
          :key="`${message.role}-${index}`"
          class="chat-message"
          :class="`chat-message-${message.role}`"
        >
          {{ message.text }}
        </div>
        <div v-if="isLoading" class="chat-message chat-message-assistant chat-loading">Thinking...</div>
      </div>

      <form class="chat-form" @submit.prevent="sendMessage">
        <input
          ref="messageInput"
          v-model="message"
          type="text"
          placeholder="Type your question..."
          aria-label="Chat message"
          :disabled="isLoading"
        />
        <button class="chat-send" type="submit" aria-label="Send message" :disabled="isLoading || !message.trim()">
          Send
        </button>
      </form>
      <p v-if="errorMessage" class="chat-error">{{ errorMessage }}</p>
    </section>

    <button v-else class="chat-launcher" type="button" aria-label="Open SocioNeed AI Assistant" @click="openChat">
      <span aria-hidden="true">✦</span>
      <span>AI Assistant</span>
    </button>
  </div>
</template>

<script setup>
import { nextTick, ref } from 'vue'
import { useAuthStore } from '@/stores/authStore'

const authStore = useAuthStore()
const isOpen = ref(false)
const isLoading = ref(false)
const message = ref('')
const errorMessage = ref('')
const messageInput = ref(null)
const messages = ref([])

async function openChat() {
  isOpen.value = true
  await nextTick()
  messageInput.value?.focus()
}

async function sendMessage() {
  const text = message.value.trim()
  if (!text || isLoading.value) return

  messages.value.push({ role: 'user', text })
  message.value = ''
  errorMessage.value = ''
  isLoading.value = true

  try {
    const reply = await authStore.aiChat(text)
    messages.value.push({ role: 'assistant', text: reply || 'I could not generate a response.' })
  } catch (error) {
    errorMessage.value = error.message || 'Unable to get a response right now.'
  } finally {
    isLoading.value = false
    await nextTick()
    messageInput.value?.focus()
  }
}
</script>

<style scoped>
.chatbot {
  position: fixed;
  right: var(--space-6);
  bottom: var(--space-6);
  z-index: var(--z-modal);
}

.chat-launcher {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  min-height: 44px;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-full);
  color: var(--color-text-inverse);
  background: linear-gradient(135deg, var(--color-primary-dark), var(--color-primary-light));
  box-shadow: var(--shadow-lg);
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
}

.chat-launcher:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-xl);
}

.chat-launcher span:first-child {
  font-size: var(--text-lg);
}

.chat-panel {
  display: flex;
  flex-direction: column;
  width: min(360px, calc(100vw - 2 * var(--space-6)));
  height: min(500px, calc(100vh - 2 * var(--space-6)));
  overflow: hidden;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  background: var(--color-surface);
  box-shadow: var(--shadow-xl);
}

.chat-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-4);
  color: var(--color-text-inverse);
  background: linear-gradient(135deg, var(--color-primary-dark), var(--color-primary-light));
}

.chat-header h2 {
  color: inherit;
  font-size: var(--text-base);
}

.chat-header p {
  margin-top: var(--space-1);
  color: rgba(255, 255, 255, 0.82);
  font-size: var(--text-xs);
}

.chat-close {
  color: inherit;
  font-size: 1.5rem;
  line-height: 1;
}

.chat-messages {
  display: flex;
  flex: 1;
  flex-direction: column;
  gap: var(--space-3);
  overflow-y: auto;
  padding: var(--space-4);
  background: var(--color-background);
}

.chat-empty,
.chat-error {
  color: var(--color-text-secondary);
  font-size: var(--text-xs);
  line-height: var(--leading-relaxed);
}

.chat-message {
  max-width: 84%;
  padding: var(--space-3);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  white-space: pre-wrap;
}

.chat-message-user {
  align-self: flex-end;
  color: var(--color-text-inverse);
  background: var(--color-primary);
  border-bottom-right-radius: var(--radius-sm);
}

.chat-message-assistant {
  align-self: flex-start;
  color: var(--color-text-primary);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-bottom-left-radius: var(--radius-sm);
}

.chat-loading {
  color: var(--color-text-muted);
  font-style: italic;
}

.chat-form {
  display: flex;
  gap: var(--space-2);
  padding: var(--space-3);
  border-top: 1px solid var(--color-border);
  background: var(--color-surface);
}

.chat-form input {
  min-width: 0;
  padding: var(--space-3);
}

.chat-send {
  flex: 0 0 auto;
  padding: 0 var(--space-3);
  border-radius: var(--radius-md);
  color: var(--color-text-inverse);
  background: var(--color-primary);
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
}

.chat-send:disabled {
  cursor: not-allowed;
  opacity: 0.55;
}

.chat-error {
  padding: 0 var(--space-3) var(--space-3);
  color: var(--color-danger-dark);
}

@media (max-width: 480px) {
  .chatbot {
    right: var(--space-3);
    bottom: var(--space-3);
  }

  .chat-panel {
    width: calc(100vw - 2 * var(--space-3));
    height: min(500px, calc(100vh - 2 * var(--space-3)));
  }
}
</style>
