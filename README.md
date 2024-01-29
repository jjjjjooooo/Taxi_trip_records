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
- **src/utils/**: Utility functions used across different components.
- **src/entity/__init__.py**: Defines class attributes for each project component.
- **src/config/config.py**: Manages application configuration.
- **src/components/**: Core code for each project component.
- **src/pipeline/**: Execution scripts for each component, managing the workflow.
- **main.py**: Entry point for running the pipeline scripts.
- **app.py**: Application entry point, orchestrating the overall process.
- **Dockerfile**: Provides instructions for Dockerizing the application.
- **tests/**: Contains unit tests for each component located in src/components.

## How to Run Tests

To execute tests for a specific component, use the command 'pytest tests/<component_name>.py'. Replace <component_name> with the appropriate component name, such as test_data_ingestion, test_data_transformation, or test_data_visualization, depending on which component you wish to test.

## How to Run Project

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

**Overall Trend**: The analysis of taxi trip data from 2009 to the present suggests a discernible evolution in the average distances and durations of taxi trips in New York City. This gradual shift could be attributed to urban development, evolving traffic patterns, or changes in commuter behaviors. The data indicates a tendency for taxi trips to become lengthier, with distance and duration generally showing a consistent correlation. However, external factors and specific events within the city may disrupt this trend periodically. Such a trend underscores the dynamic nature of urban mobility and reflects the city's ongoing infrastructural and socio-economic transformations.

![seasonality-1](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/d5285557-c36b-4073-81ee-7f8938339a80)

![seasonality-2](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/7627eefc-86cd-444d-b15a-d652049ecdbd)

**Seasonality**: There is a clear seasonal pattern observed with peaks and troughs occurring around the same time each year. Trip distances peak during the summer months, which could be due to increased tourism and outdoor activities when the weather is favorable. Conversely, trip durations appear to peak slightly later in the year, which may be influenced by increased traffic congestion and slower travel times as the weather deteriorates and the holiday season approaches. The shortest trip distances and durations tend to occur in the winter months, particularly around February, which may correspond with the coldest time of the year when there's likely to be a reduction in tourism and possibly more residents choosing to stay indoors or use alternative modes of transportation.

![covid](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/41e03ed6-3840-49c3-bc8f-3d9c74eb25ea)

**COVID-19 Impact**: In early 2020, everything changed. When COVID-19 hit, the correlation between how far and how long trips were broke down. Even though trips got longer, they took less time, probably because there were fewer cars on the road due to lockdowns. This was an unexpected twist that shows just how much the pandemic changed everyday life.

![after covid](https://github.com/jjjjjooooo/Taxi_trip_records/assets/50882720/93bef769-aa42-47e0-a444-c365c9e964bd)

**Recovery After COVID-19**: As the city advanced beyond the peak of the pandemic, the relationship between the length and time of taxi journeys started to realign with historical patterns. However, a 'new normal' seems to have taken shape, with distinct average trip lengths diverging from pre-pandemic figures. This shift could be a reflection of lasting changes in commuting habits or a rise in remote working practices.
