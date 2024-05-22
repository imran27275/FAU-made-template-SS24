import sqlite3
import pandas as pd
import os

class ProjectPipeline:
    def __init__(self, air_temperature_url, snow_depth_url, db_path):
        
        self.air_temperature_data = air_temperature_url
        self.snow_depth_data = snow_depth_url
        self.db_path = db_path

    def save_to_sqlite(self, url, table_name, conn):
        # Load the dataset
        df = pd.read_csv(url)

        # Remove the "water_year" column if it exists
        if 'water_year' in df.columns:
            df.drop(columns=['water_year'], inplace=True)

        # Rename air temperature column name
        if 'sme2_ta_C' in df.columns:
            df.rename(columns={'sme2_ta_C': 'sme2 temperature in celsius'}, inplace=True)
        if 'smf1_ta_C' in df.columns:
            df.rename(columns={'smf1_ta_C': 'smf1 temperature in celsius'}, inplace=True)
        if 'smg1_ta_C' in df.columns:
            df.rename(columns={'smg1_ta_C': 'smg1 temperature in celsius'}, inplace=True)
        if 'smg2_ta_C' in df.columns:
            df.rename(columns={'smg2_ta_C': 'smg2 temperature in celsius'}, inplace=True)
        if 'smm1_ta_C' in df.columns:
            df.rename(columns={'smm1_ta_C': 'smm1 temperature in celsius'}, inplace=True)
        if 'smm2_ta_C' in df.columns:
            df.rename(columns={'smm2_ta_C': 'smm2 temperature in celsius'}, inplace=True)

        # Rename snow depth column name
        if 'sme2_sd_mm' in df.columns:
            df.rename(columns={'sme2_sd_mm': 'sme2 snow depth in millimeters'}, inplace=True)
        if 'smf1_sd_mm' in df.columns:
            df.rename(columns={'smf1_sd_mm': 'sm1 snow depth in millimeters'}, inplace=True)
        if 'smg1_sd_mm' in df.columns:
            df.rename(columns={'smg1_sd_mm': 'smg1 snow depth in millimeters'}, inplace=True)
        if 'smg2_sd_mm' in df.columns:
            df.rename(columns={'smg2_sd_mm': 'smg2 snow depth in millimeters'}, inplace=True)
        if 'smm1_sd_mm' in df.columns:
            df.rename(columns={'smm1_sd_mm': 'smm1 snow depth in millimeters'}, inplace=True)
        if 'smm2_sd_mm' in df.columns:
            df.rename(columns={'smm2_sd_mm': 'smm2 snow depth in millimeters'}, inplace=True)

        # Merge "month", "day", and "calendar_year" columns into a single "date" column
        if all(col in df.columns for col in ['month', 'day', 'calendar_year']):
            df['date'] = pd.to_datetime(df[['calendar_year', 'month', 'day']].astype(str).agg('-'.join, axis=1), format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
            df.drop(columns=['month', 'day', 'calendar_year'], inplace=True)
            # Move the "date" column to the first position
            cols = ['date'] + [col for col in df if col != 'date']
            df = df[cols]

        # Save the transformed dataset to the SQLite database
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f'Transformed dataset saved to table {table_name}')

    def run(self):
        # Ensure the data directory exists
        
        if not os.path.exists(os.path.dirname(self.db_path)):
            os.makedirs(os.path.dirname(self.db_path))

        # Connect to the SQLite database (it will be created if it doesn't exist)
        conn = sqlite3.connect(self.db_path)

        # Transform and save the air temperature dataset to SQLite
        self.save_to_sqlite(self.air_temperature_data, 'air_temperature', conn)

        # Transform and save the snow depth dataset to SQLite
        self.save_to_sqlite(self.snow_depth_data, 'snow_depth', conn)

        # Close the database connection
        conn.close()

def main():
    # URLs of the datasets
    air_temperature_url = 'https://ndownloader.figshare.com/files/44334659'
    snow_depth_url = 'https://ndownloader.figshare.com/files/44334722'

    # SQLite database file path
    data_dir = './data'
    db_path = os.path.join(data_dir, 'climate_data.sqlite')

    # Initialize the processor
    processor = ProjectPipeline(air_temperature_url, snow_depth_url, db_path)

    # Run the processor
    processor.run()

if __name__ == "__main__":
    main()
