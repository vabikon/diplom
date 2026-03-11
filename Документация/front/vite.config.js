import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { resolve } from "path";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [vue(), tailwindcss()],
  resolve: {
    alias: {
      "@": resolve(__dirname, "./src"),
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:3344",
        changeOrigin: true,
        secure: false,
      },
      "/images": {
        target: "http://127.0.0.1:3344",
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
