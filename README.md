# Trip Length Analysis for Taxis in New York City

## Introduction

This project analyzes the average trip length for yellow taxis in New York City, focusing on both trip duration and distance. It automates the tracking process through three primary components: data ingestion, transformation, and visualization.

- **Data Ingestion**: Downloads data in Parquet format from the [NYC Taxi & Limousine Commission](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), ensuring continuous data flow.
- **Data Transformation**: Prunes and applies feature engineering to the downloaded data to prepare it for analysis.
- **Data Visualization**: Visualizes both monthly and rolling averages of trip lengths over time, providing insights into temporal trends.

## Project Structure

The project is organized as follows:

- **params.yaml**: Defines parameters for data processing and analysis.
- **config/config.yaml**: Contains configuration values for the project.
- **requirements.txt**: Lists all the required Python packages.
- **research/**: Jupyter notebooks for component research.
- **src/utils**: Utility functions used across different components.
- **src/entity/__init__.py**: Defines class attributes for each project component.
- **src/config/config.py**: Manages application configuration.
- **src/components**: Core code for each project component.
- **src/pipeline**: Execution scripts for each component, managing the workflow.
- **main.py**: Entry point for running the pipeline scripts.
- **app.py**: Application entry point, orchestrating the overall process.
- **Dockerfile**: Provides instructions for Dockerizing the application.
- **tests/**: Unit tests for each component in `src/components`.

## How to Run

This project can be run either directly through Python or within a Docker container. Below are the instructions for both methods:

### Running Directly with Python

Before running the application, ensure you have Python installed and the virtual environment has been correctly set up by running:

'pip install -r requirements.txt'

Once the environment has been correctly set up, you can run the application:

- Direct Application Run: Use the command 'python main.py' in your terminal to start the main application process.
- Access via FastAPI: Use the command 'python app.py' to start the application with FastAPI. This will allow you to access the application's API endpoints.

### Running with Docker
To run the application using Docker, follow these steps:

1. Build the Docker Image:
Run 'docker build -t your-image-name .' in the terminal. Replace your-image-name with a name of your choice for the Docker image.

2. Run the Docker Container:
After the image is built, you can start the container using: 'docker run -p 80:80 your-image-name'. This command will map port 80 of the container to port 80 on your host machine.




## Analysis

The project includes an in-depth analysis of the rolling 45-day average for trip distance and duration of yellow taxis in NYC, starting from January 2009 to the present. This analysis aims to uncover trends and patterns in taxi usage over the years.
