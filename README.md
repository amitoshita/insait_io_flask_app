# Insait Backend Internship Home Assignment

## Overview
This project implements a simple Flask server that accepts a question via an API endpoint, sends the question to the OpenAI API for an answer, and stores both the question and the answer in a PostgreSQL database. The project is fully dockerized and includes one test using `pytest`.

## Features
- **Flask Server**: Handles the `/ask` endpoint to accept questions.
- **OpenAI API Integration**: Sends questions to OpenAI and retrieves answers.
- **PostgreSQL Database**: Stores the questions and answers.
- **Alembic for Migrations**: Manages database schema migrations.
- **Docker**: The application is dockerized, including both the Flask server and PostgreSQL database.
- **Docker Compose**: Simplifies the orchestration of the Docker containers.
- **Pytest Testing**: Includes a test to validate the `/ask` endpoint.


## Project video explanation
https://www.loom.com/share/1bfdaf0afed0435baf1ef6d2975cafa2?sid=64118fda-d402-4df5-9601-9fdf44fd3a40

