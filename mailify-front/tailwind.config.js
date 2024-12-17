/** @type {import('tailwindcss').Config} */
export default {
    darkMode: ["class"],
    content: [
    "./index.html",
    "./src/**/*.{svelte,js,ts}",
  ],
  theme: {
  	extend: {
  		colors: {
  			transparent: 'transparent',
  			current: 'currentColor',
  			white: '#ffffff',
  			mist: '#DAD6D6',
  			midnight: '#232121',
  			blaze: '#FF634A'
  		},
  		fontFamily: {
  			helvetica: [
  				'Helvetica',
  				'Arial',
  				'sans-serif'
  			]
  		},
  	}
  },
  plugins: [],
}

