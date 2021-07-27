# LOOK FOR "ACTIVITY HERE" COMMENTS


# importing mysql library
from mysql.connector import connect, Error

# establishing connection to mysql database with try catch statement
try:
    connection = connect(
        host="pythonactivities.cotpafanc2of.eu-west-2.rds.amazonaws.com",
        user="admin",
        password="admin1234",
        database="PythonActivities",
    )
except Error as e:
    print(e)

# initailising all variables
cursor = connection.cursor()
possibleCommands = ["help", "add new recipe", "quit", "list all recipes", "search recipe", "sort recipes"]

# starting a while loop to iterate through commands
while True:
    # converting entered command to lower case
    command = input("Please enter command: ").strip().lower()

    # checking if command is equal to "quit"
    if command == possibleCommands[2]:
        # Displaying "bye" message and closing program

        # ACTIVITY 1
        # print goodbye message

        print("")
        exit()

    # checking if command is equal to "help"
    elif command == possibleCommands[0]:
        # printing all supported commands
        print("Possible Commands: ", possibleCommands)
        print("")

    # checking if command is equal to "list items"
    elif command == possibleCommands[3]:
        # running sql query to retrive item list

        # ACTIVITY 2
        # Please insert list item (select) sql command here
        sql_select_Query = ""

        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        # printing item list with for loop
        print("List of Recipes:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
        print("")

    # checking if command is equal to "add item"
    elif command == possibleCommands[1]:
        # taking new item name as input
        NewItemName = input("Please enter new Pizza name: ")
        NewItemPrice = input("Please enter new Pizza price: ")
        NewItemDescription = input("Please enter new Pizza Ingredients: ")
        # inserting new item into database
        
        # ACTIVITY 3
        # Please insert add item (insert) sql command here
        sql = ""

        val = ("NULL", NewItemName, NewItemPrice, NewItemDescription)
        cursor.execute(sql, val)
        connection.commit()
        # running sql query to retrive updated item list

        # ACTIVITY 4
        # Please insert list item (select) sql command here
        sql_select_Query = ""
        
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        # printing updated item list with for loop
        print("Updated List of Recipes:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
        print("")

    # checking if command is equal to "search item"
    elif command == possibleCommands[4]:
        # taking input for search
        searchKey = input("Type here to search for recipes: ")
        # running sql query to retrive item list where item name is like entered string
        sql = """SELECT * FROM PizzaRecipes WHERE pizzaName LIKE %s"""
        adr = ("%"+searchKey+"%", )
        cursor.execute(sql, adr)
        records = cursor.fetchall()
        # printing search results
        print("Search result:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
        print("")
    
    # checking if command is equal to "sort list"
    elif command == possibleCommands[6]:
        # printing possible sorting options
        print("Please choose sorting type: \n1 - ID Ascending\n2 - ID Descending\n3 - Name Ascending\n4 - Name Descending")
        # taking sort type as input
        sortID = input("Please enter sort type (number): ").strip().lower()
        # checking if sort type 1 is chosen
        if sortID == "1":
            # running sql query to retrive sorted item list
            sql_select_Query = "select * from PizzaRecipes ORDER BY pizzaID"
            cursor.execute(sql_select_Query)
        # checking if sort type 2 is chosen
        if sortID == "2":
            # running sql query to retrive sorted item list
            sql_select_Query = "select * from PizzaRecipes ORDER BY pizzaID DESC"
            cursor.execute(sql_select_Query)
        # checking if sort type 3 is chosen
        if sortID == "3":
            # running sql query to retrive sorted item list
            sql_select_Query = "select * from PizzaRecipes ORDER BY pizzaName"
            cursor.execute(sql_select_Query)
        # checking if sort type 4 is chosen
        if sortID == "4":
            # running sql query to retrive sorted item list
            sql_select_Query = "select * from PizzaRecipes ORDER BY pizzaName DESC"
            cursor.execute(sql_select_Query)
        # fetching queried data
        records = cursor.fetchall()
        # printing item list with for loop
        for row in records:
            print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
        print("")

    # If no valid commands are entered
    else:
        # Error message, for invalid command
        # printing all supported commands

        # ACTIVITY 5 & 6
        # print error message here and all possible commands (use seperate print statements)
        
        print("")
