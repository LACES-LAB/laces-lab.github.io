module.exports = {
  darkMode: 'class',
  content: [
    "./themes/**/layouts/**/*.html",
    "./content/**/layouts/**/*.html",
    "./layouts/**/*.html",
    "./content/**/*.html"
  ],
  theme: {
    extend: {
      colors: {
        'rpi-red': '#d6001c',
        'rpi-dark-gray': '#54585a',
        'rpi-light-gray': '#9ea2a2',
        'rpi-dark-red-100': '#ab2328',
        'rpi-dark-red-75': '#c35442',
        'rpi-dark-red-50': '#d58570',
        'rpi-dark-red-25': '#eabcad',
        'rpi-dark-blue-100': '#00205b',
        'rpi-dark-blue-75': ' #2b517f',
        'rpi-dark-blue-50': '#667ba2',
        'rpi-dark-blue-25': '#a5b0cb',
        'rpi-light-blue-100': '#7fa9ae',
        'rpi-light-blue-75': '#94c0c6',
        'rpi-light-blue-50': '#b3d3d5',
        'rpi-light-blue-25': '#d4e6e8',

      }
    },
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/line-clamp'),
    require('@tailwindcss/typography'),
  ]
}
