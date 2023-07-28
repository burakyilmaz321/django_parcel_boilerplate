import { fontFamily as _fontFamily } from 'tailwindcss/defaultTheme'

/** @type {import('tailwindcss').Config} */
export const content = [
    "./src/**/*.{html,js,ts,jsx,tsx,py}",
];
export const theme = {
    extend: {
        fontFamily: {
            sans: ['Inter var', ..._fontFamily.sans],
        },
    },
}
export const plugins = [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
]
