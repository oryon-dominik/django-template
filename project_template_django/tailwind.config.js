/** @type {import('tailwindcss').Config} */
const plugin = require("tailwindcss/plugin");
const { spawnSync } = require("child_process");

// Calls Django to fetch template files
const getTemplateFiles = () => {
  const command = "python";
  const args = ["manage.py", "tailwind", "list_templates"];

  const options = { cwd: __dirname };
  const result = spawnSync(command, args, options);

  if (result.error) {
    throw result.error;
  }

  if (result.status !== 0) {
    console.log(result.stdout.toString(), result.stderr.toString());
    throw new Error(
      `Django management command exited with code ${result.status}`
    );
  }

  const templateFiles = result.stdout
    .toString()
    .split("\n")
    .map((file) => file.trim())
    .filter(function (e) {
      return e;
    }); // Remove empty strings, including last empty line.
  return templateFiles;
};

module.exports = {
  content: [
    "./assets/js/darkmode-toggle.js",
  ].concat(getTemplateFiles()),
  theme: {
    // existing colors might be overwritten easily.
    // colors: {
    //   transparent: 'transparent',
    //   current: 'currentColor',
    //   'white': '#ffffff',
    //   'tahiti': {
    //     light: '#67e8f9',
    //     DEFAULT: '#06b6d4',
    //     dark: '#0e7490',
    //     100: '#cffafe',
    //     200: '#a5f3fc',
    //     300: '#67e8f9',
    //     400: '#22d3ee',
    //     500: '#06b6d4',
    //     600: '#0891b2',
    //     700: '#0e7490',
    //     800: '#155e75',
    //     900: '#164e63',
    //   },
    // },
    extend: {
      // Use your own custom colors or patch a shade of an existing color.
      // Hint: for an intuitive approach use HSL and just change the lightness to get better gradients -> https://hslpicker.com/
      colors: {
        // Palette 5 of refactoringui.com/book
        // bluegrey: {
        //   50: '#F0F4F8',
        //   100: '#D9E2EC',
        //   200: '#BCCCDC',
        //   300: '#9FB3C8',
        //   400: '#829AB1',
        //   500: '#627D98',
        //   600: '#486581',
        //   700: '#334E68',
        //   800: '#243B53',
        //   900: '#102A43',
        //   950: '#020a12',
        // }
      }
    },
  },
  darkMode: 'class',
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/aspect-ratio"),
    require("@tailwindcss/container-queries"),
    plugin(function ({ addVariant }) {
      addVariant("htmx-settling", ["&.htmx-settling", ".htmx-settling &"]);
      addVariant("htmx-request", ["&.htmx-request", ".htmx-request &"]);
      addVariant("htmx-swapping", ["&.htmx-swapping", ".htmx-swapping &"]);
      addVariant("htmx-added", ["&.htmx-added", ".htmx-added &"]);
    }),
  ],
};
