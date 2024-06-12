import sqlite3

def check_database():
    try:
        conn = sqlite3.connect('climate_data.sqlite')
        print("Connected to the database.")
        print("Database exists.")
        conn.close()
    except sqlite3.Error as e:
        print("Database does not exist.")

def check_table_presence(table_name):
    try:
        conn = sqlite3.connect('climate_data.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except sqlite3.Error as e:
        print(f"Error checking table presence: {e}")
        return False


def check_columns_presence(table_name, column_names):
    conn = sqlite3.connect('climate_data.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    table_columns = cursor.fetchall()
    cursor.close()
    conn.close()
    existing_columns = [column[1] for column in table_columns]
    return all(column in existing_columns for column in column_names)

def test_case_1():
    table_name = "air_temperature"
    print("\nTest case 1:")
    print("Checks if the air_temperature table exists and if it has the required columns.")
    print("Required columns: 'sme2 temperature in celsius', 'smf1 temperature in celsius','smg1 temperature in celsius','smg2 temperature in celsius','smm1 temperature in celsius','smm2 temperature in celsius'")
    if check_table_presence(table_name):
        column_names = ['sme2 temperature in celsius', 'smf1 temperature in celsius','smg1 temperature in celsius','smg2 temperature in celsius','smm1 temperature in celsius','smm2 temperature in celsius']
        if check_columns_presence(table_name, column_names):
            print("Test case 1 passed.")
        else:
            print("Test case 1 failed. Missing columns in air_temperature table.")
    else:
        print("Test case 1 failed. air_temperature table does not exist.")


def test_case_2():
    table_name = "snow_depth"
    print("\nTest case 2:")
    print("Checks if the snow_depth table exists and if it has the required columns.")
    print("Required columns: 'sme2 snow depth in millimeters', 'smf1 snow depth in millimeters','smg1 snow depth in millimeters','smg2 snow depth in millimeters','smm1 snow depth in millimeters','smm2 snow depth in millimeters'")
    if check_table_presence(table_name):
        column_names = ['sme2 snow depth in millimeters', 'smf1 snow depth in millimeters','smg1 snow depth in millimeters','smg2 snow depth in millimeters','smm1 snow depth in millimeters','smm2 snow depth in millimeters']
        if check_columns_presence(table_name, column_names):
            print("Test case 2 passed.")
        else:
            print("Test case 2 failed. Missing columns in snow_depth table.")
    else:
        print("Test case 2 failed. snow_depth table does not exist.")


def main():
    check_database()
    test_case_1()
    test_case_2()
    print("Automated testing done.")

if __name__ == '__main__':
    main()