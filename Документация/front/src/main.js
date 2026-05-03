import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Глобальная обработка ошибок
const app = createApp(App)

// Глобальный обработчик ошибок
app.config.errorHandler = (err, vm, info) => {
  console.error('Vue Error:', err)
  console.error('Component:', vm)
  console.error('Info:', info)
  
  // Показываем пользователю понятное сообщение
  const notification = document.createElement('div')
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: #dc2626;
    color: white;
    padding: 12px 24px;
    border-radius: 4px;
    font-size: 14px;
    z-index: 9999;
    animation: slideIn 0.3s ease;
  `
  notification.textContent = 'Произошла ошибка в приложении'
  document.body.appendChild(notification)
  
  setTimeout(() => {
    notification.style.animation = 'slideOut 0.3s ease'
    setTimeout(() => {
      if (document.body.contains(notification)) {
        document.body.removeChild(notification)
      }
    }, 300)
  }, 5000)
}

// Перехват необработанных промисов
window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled Promise Rejection:', event.reason)
  event.preventDefault()
})

app.use(store)
app.use(router)
app.mount('#app')
