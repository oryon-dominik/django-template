const defaulttheme = 'dark'

document.addEventListener('alpine:init', () => {
  Alpine.store('theme', {
    init() {
      // On page load or when changing themes, best to add inline in `head` to avoid FOUC
      if (localStorage.theme === 'dark' || (!('theme' in localStorage) || defaulttheme === 'dark' && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark')
        localStorage.theme = 'dark'
        this.dark = true
      } else {
        document.documentElement.classList.remove('dark')
        localStorage.theme = 'light'
        this.dark = false
      }
    },
    dark: defaulttheme === 'dark',

    toggle() {
      if (this.dark) {
        localStorage.theme = 'light'
        document.documentElement.classList.remove('dark')
        this.dark = false
      }
      else {
        localStorage.theme = 'dark'
        document.documentElement.classList.add('dark')
        this.dark = true
      }
    }
  })
})

const toLightMode = `
<svg
  xmlns="http://www.w3.org/2000/svg"
  class="transition ease-in-out delay-150 w-8 h-8 stroke-1 hover:stroke-zinc-100 stroke-zinc-50 hover:fill-zinc-900 fill-zinc-950"
>
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
</svg>
<span class="sr-only">light</span>
`

const toDarkMode  = `
<svg
  xmlns="http://www.w3.org/2000/svg"
  class="transition ease-in-out delay-150 w-8 h-8 stroke-1 stroke-zinc-950 hover:stroke-zinc-900 hover:fill-zinc-100 fill-zinc-50"
>
  <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
</svg>
<span class="sr-only">dark</span>
`
