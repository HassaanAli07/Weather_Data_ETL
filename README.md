# Weather ETL (Extract, Transform, Load)

## Overview

The **Weather ETL** project is designed to fetch real-time weather data for Karachi city from the **OpenWeatherMap API**, transform the relevant data, and load it into a PostgreSQL database. This ETL pipeline allows easy extraction of weather details like temperature, humidity, and pressure, and stores them for further analysis or visualization.

## Features

- **Extract**: Fetch weather data from the OpenWeatherMap API.
- **Transform**: Extract and clean relevant weather information such as temperature, humidity, pressure, and more.
- **Load**: Load the transformed data into a PostgreSQL database for persistent storage.

## Technology Stack

- **Python**: Used for the ETL logic and API interaction.
- **OpenWeatherMap API**: Provides real-time weather data.
- **PostgreSQL**: Database used for storing transformed weather data.
- **Docker**: Containerization tool used to run the PostgreSQL database and the ETL pipeline in isolated environments.
- **PgAdmin**: A web-based interface to manage the PostgreSQL database.

## Requirements

To run this project, ensure you have the following installed:

- Docker & Docker Compose
- Python 3.x
- PostgreSQL
- PgAdmin (Optional, for database management)

Alternatively, you can use **Docker Compose** to run the entire stack (PostgreSQL, PgAdmin, and the ETL script) in one go.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/HassaanAli07/Weather_Data_ETL.git
cd Weather_Data_ETL
2. Install Python Dependencies
Create a virtual environment and install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt

3. Set Up Environment Variables
Create a .env file in the root of the project and add your OpenWeatherMap API key:

env
Copy
Edit
API_KEY=your_openweathermap_api_key
4. Run the Docker Containers (PostgreSQL & PgAdmin)
If using Docker, run:

bash
Copy
Edit
docker-compose up
This will start the PostgreSQL and PgAdmin containers.

5. Run the ETL Pipeline
Run the Python script to start the ETL process:

bash
Copy
Edit
python etl_script.py
The script will:

Fetch weather data from OpenWeatherMap API

Transform the data by extracting key weather metrics

Load the data into the PostgreSQL database

6. Access the Data in PostgreSQL
You can access your PostgreSQL database using PgAdmin (accessible through the Docker container). Use the following credentials:

Host: localhost

Port: 5432

Username: postgres

Password: password

Once logged in, you can navigate to the weather_data table to view the stored weather information.

Example of Transformed Data
The following fields are extracted from the API response and loaded into the database:

Temperature (temp)

Feels Like (feels_like)

Humidity

Pressure

Sea Level

Ground Level

Scheduled Execution
This ETL process is currently designed to run manually. However, you can automate it using Apache Airflow or any task scheduler to fetch the weather data periodically (e.g., every hour or every 3-4 hours).

Conclusion
The Weather ETL project provides a straightforward solution for fetching, transforming, and storing weather data. By leveraging Python, PostgreSQL, and Docker, it offers an easy-to-deploy and scalable ETL pipeline for weather data collection
