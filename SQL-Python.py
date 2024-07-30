import mysql.connector
from mysql.connector import Error

# function containing information to update member 
def update_member(table_one):
    sql_update_member = f"""
            INSERT INTO {table_one} (id, name, age)
            VALUES (%s, %s, %s)
            """
    return sql_update_member

# function containing information to add workout 
def add_workout_session(table_two):
    sql_add_workout = f"""
            INSERT INTO {table_two} (session_id, member_id, session_date, session_time, activity)
            VALUES (%s, %s, %s, %s, %s)
            """
    return sql_add_workout

# function containing information to update member age
def update_member_age(table_one):
    sql_update_member = f"""UPDATE {table_one}
    SET age = %s
    WHERE id = %s
    """
    return sql_update_member

# function containing information to delete workout 
def delete_workout_session(table_two):
    sql_delete_workout = f"""
    DELETE FROM {table_two} WHERE session_id = %s"""
    return sql_delete_workout

# function containing information to pick out members between a certain age  
def show_certain_ages(floor_age, ceiling_age, table_one):
    sql_select_ages = f"""SELECT * FROM {table_one}
    WHERE age BETWEEN %s AND %s;"""
    return sql_select_ages

# main function executes all edits to database     
def main():
    db_name = "fitness_db"
    user = "root"
    password = "843RnR$$"
    host = "127.0.0.1"
    port = 3306
    member_data = ('8', 'Jack Johnson', '51')
    session_data = ('8', '8', '2024-12-31', '4:14pm', 'treadmill')
    update_data = ('22', '8')  # new_age and update_session
    table_one = 'Members'
    table_two = 'WorkoutSessions'
    age_range = ('25', '30')  # floor_age and ceiling_age

    try: 
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )

        if conn.is_connected():
            # Create cursor 
            cursor = conn.cursor()
      
            # Call functions that change data through cursor 
            cursor.execute(update_member(table_one), member_data)
            cursor.execute(add_workout_session(table_two), session_data)
            cursor.execute(update_member_age(table_one), update_data)
            cursor.execute(delete_workout_session(table_two), (update_data[1],))  # delete by session id
            
            # Execute the query to show certain ages
            cursor.execute(show_certain_ages(*age_range, table_one), age_range)
            results = cursor.fetchall()

            # Print the results
            for row in results:
                print(row)

            # Commit changes
            conn.commit()
            print("Records updated successfully")

    except Error as e: 
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed.")

# Call the main function
if __name__ == "__main__":
    main()