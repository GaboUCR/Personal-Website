#!/bin/bash
cd static
npx tailwindcss -i ./src/tailwind.css -c ./tailwind.config.js -o ./dist/tailwind.css --watch
