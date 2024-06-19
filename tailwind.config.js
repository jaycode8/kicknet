/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.html", "./static/src/**/*.js"],
    theme: {
        extend: {
            colors: {
                bgColor: "#121212",
                whitish: "hsl(0, 0%, 100%)",
            },
            gridTemplateColumns: {
                homeCols: ".2fr .6fr .2fr"
            }
        },
    },
    plugins: [],
};

