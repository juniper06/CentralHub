/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/**/*.{html,js}"],
	theme: {
		extend: {
			colors: {
				primary: {
					100: "#f3dbe8",
					200: "#e8b7d1",
					300: "#dc93b9",
					400: "#d16fa2",
					500: "#c54b8b",
					600: "#9e3c6f",
					700: "#762d53",
					800: "#4f1e38",
					900: "#270f1c",
				},
			},
		},
	},
	plugins: [require("@tailwindcss/aspect-ratio")],
};
