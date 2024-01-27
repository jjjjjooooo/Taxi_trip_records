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

## Analysis

The project includes an in-depth analysis of the rolling 45-day average for trip distance and duration of yellow taxis in NYC, starting from January 2009 to the present. This analysis aims to uncover trends and patterns in taxi usage over the years.

## How to Run

(Include instructions on how to set up and run the project, including any necessary commands or steps to build the Docker container, if applicable.)
