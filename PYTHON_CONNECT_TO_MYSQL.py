import matplotlib.pyplot as plt
import mysql.connector

try:
    # Connect to the PAMS database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jamesharden014",
        database="PAMS"
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Query the database to retrieve data on successful adoptions
    cursor.execute("SELECT COUNT(*) FROM AdoptionApplications WHERE Status = 'Approved'")
    successful_adoptions = cursor.fetchone()[0]

    # Query the database to retrieve data on failed adoptions
    cursor.execute("SELECT COUNT(*) FROM AdoptionApplications WHERE Status != 'Approved'")
    failed_adoptions = cursor.fetchone()[0]

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Create a pie chart
    labels = ['Successful Adoptions', 'Failed Adoptions']
    sizes = [successful_adoptions, failed_adoptions]
    colors = ['lightgreen', 'lightcoral']
    explode = (0.1, 0)  # explode the 1st slice

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Distribution of Adoption Application Status')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show plot
    plt.show()

except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)
except Exception as e:
    print("An error occurred:", e)
