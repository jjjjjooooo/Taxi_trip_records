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

![overview](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/bb39ded4-6df6-4ae7-b1be-3a2f60398414)

![seasonality-1](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/d5285557-c36b-4073-81ee-7f8938339a80)

![seasonality-2](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/7627eefc-86cd-444d-b15a-d652049ecdbd)

![covid](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/41e03ed6-3840-49c3-bc8f-3d9c74eb25ea)

![after covid](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/93bef769-aa42-47e0-a444-c365c9e964bd)


The provided figures seem to represent a time series analysis of the average trip length for yellow taxis in New York City, with a focus on both distance and duration. While I can't view the images directly, I will provide you with a general approach to analyze such time series data.

General Analysis Approach:

Trend Analysis:

Identify any long-term increase or decrease in trip length over time.
Look for significant changes that may correspond with external events (e.g., regulatory changes, economic events).
Seasonality:

Assess the presence of seasonal patterns or cyclical fluctuations that repeat over a specific period, such as weeks, months, or quarters.
Determine if there are particular times of the year when trip lengths are consistently longer or shorter.
Anomalies:

Spot any outliers or unusual spikes/drops that could indicate extraordinary events or data errors.
For instance, a sharp decline in trip distance and duration may align with the onset of the COVID-19 pandemic due to lockdowns and reduced travel.
Covariation:

Look at how trip distance and duration move in relation to each other.
For example, one might expect longer trips to also take more time, but if you see periods where distance increases without a corresponding increase in time, it could suggest faster travel speeds (possibly due to less traffic).
Contextual Events:

If known, correlate changes in the data with specific events, like natural disasters, transit strikes, or significant changes in urban infrastructure.
Before and After Comparisons:

Compare periods before and after a significant event (like pre-COVID vs. post-COVID) to understand the impact on taxi travel behavior.
Evaluate recovery patterns or permanent shifts in travel behavior post-event.
Given these approaches, let's attempt to derive insights based on the context provided for the images.

Insights Based on Contextual Information:

Pre-COVID vs. Post-COVID: Compare the rolling averages before the pandemic to the period during and after to understand its impact. A visible decline during the pandemic followed by a recovery phase would be expected.

Seasonality: There may be visible patterns that indicate seasonality. For example, trip lengths could vary with tourist seasons or school holidays.

Overall Trend: Over a long period, there could be a trend indicating that trips are getting longer or shorter. This could be due to changes in urban development, traffic conditions, or user behavior.

Anomalies during COVID: The "covid.jpg" and "after covid.jpg" files likely show significant deviations from the norm during 2020, which would be expected due to lockdowns and other restrictions.

Seasonality and Long-term Trends: The "overview.jpg", "seasonality-1.jpg", and "seasonality-2.jpg" files might show a combination of seasonal patterns superimposed on a longer-term trend, which might be upwards or downwards.

![monthly-average](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/efeeaf52-b07f-4fc1-b7a2-b579952631e6)


To provide a more detailed analysis, please ensure the images are accessible or describe the patterns observed in the images.




