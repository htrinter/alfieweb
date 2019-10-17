# Alfie Web

Alfie is a Python script made by [hertze](https://github.com/hertze/Alfie) that creates diary inserts in various formats and layouts. The script generates LaTeX files and compiles them with XeTeX. This project makes it into a web app.

The web app is built with Python, Flask, WTForms and Bootstrap. It is deployed as a Docker container and uses the Gunicorn webserver.

The app is deployed on my playground: [https://alfieweb.7c8.de/](https://alfieweb.7c8.de/)

You can run the app locally by executing `boot-local.sh`. The script sets up the virtual environment, installs the dependencies and starts Flask's development server. For the PDF generation to work you need to have xetex installed. Take a look at the Dockerfile for all required dependencies, or just build the Docker image for testing.

