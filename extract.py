import requests
import psycopg2
import json
import os
from dotenv import load_dotenv


load_dotenv()

myData = []
api_key = os.getenv('API_KEY')
city = 'Karachi'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'


# Extracting the data from API

def extract(url):

    try :
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    
    except Exception as e:
        print(f'Cannot fetch the URL : {e}') 
    
# Transforming the data as per our need

def transformation(data):
    try :
        temp = data.get('main',{}).get('temp')
        feels_like = data.get('main',{}).get('feels_like')
        humidity = data.get('main',{}).get('humidity')
        pressure = data.get('main',{}).get('pressure')
        sea_level = data.get('main',{}).get('sea_level')
        ground_level = data.get('main',{}).get('grnd_level')

        data_dict = {
            'temp' : temp,
            'feels_like' : feels_like,
            'humidity' : humidity,
            'pressure': pressure,
            'sea_level': sea_level,
            'ground_level' : ground_level
        }

        myData.append(data_dict)

        return "Success"
    
    except Exception as e:
        print(f'Cannot extract the required data : {e}')


# Loading the data to Postgres

def load(transformmed_Data):
    try:
        # Connect to PostgreSQL using credentials from .env
        conn = psycopg2.connect(
            host='postgres',           # or 'postgres' if inside Docker
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port= os.getenv("PORT")
        )
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id SERIAL PRIMARY KEY,
                temp REAL,
                feels_like REAL,
                humidity INTEGER,
                pressure INTEGER,
                sea_level INTEGER,
                ground_level INTEGER,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Insert data
        for record in transformmed_Data:
            cursor.execute("""
                INSERT INTO weather (temp, feels_like, humidity, pressure, sea_level, ground_level)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                record.get('temp'),
                record.get('feels_like'),
                record.get('humidity'),
                record.get('pressure'),
                record.get('sea_level'),
                record.get('ground_level')
            ))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"Error inserting data: {e}")


if __name__ == "__main__":
    raw_data = extract(url)
    if raw_data:
        transformation(raw_data)
        load(myData)



