from database.db_connection import execute_query

acs = """ 
      
██     ██  ██████  ██████  ██      ██████       ██████  ███████     ██   ██ ███████ ██████   ██████  ███████ 
██     ██ ██    ██ ██   ██ ██      ██   ██     ██    ██ ██          ██   ██ ██      ██   ██ ██    ██ ██      
██  █  ██ ██    ██ ██████  ██      ██   ██     ██    ██ █████       ███████ █████   ██████  ██    ██ ███████ 
██ ███ ██ ██    ██ ██   ██ ██      ██   ██     ██    ██ ██          ██   ██ ██      ██   ██ ██    ██      ██ 
 ███ ███   ██████  ██   ██ ███████ ██████       ██████  ██          ██   ██ ███████ ██   ██  ██████  ███████ 
                                                                                                            
  
  1. create hero
  2. about current hero
  3. change hero info (NOT WORKING)
"""
def start_game():
    start_response = input('Press ENTER')
    if start_response == "":
        print(acs)
        display_menu()
# start_game()
# get user input for start_response
# if start_response is empty:
# print acs
# call display_menu function
        
def display_menu():
    response = input("What will you select ")
    if response == "1":
        create_hero()
    elif response == "2":
        select_hero()
    elif response == '3':
        print(create_hero())
#displays a menu to the user and waits for their response. Based on the user's input, it either selects create hero or heros already made

def show_heroes():
     query = """
        SELECT name from heroes
     """
    #Define a SQL query that selects the name column from the heroes table.
     hero_list = execute_query(query).fetchall()
    #Execute the SQL query using a database connection.
     for num, value in enumerate(hero_list):
    # Fetch all the rows returned by the SQL query and store them in the variable hero_list.
         print(f"{num + 1}: {value[0]}")
    # Loop through the hero_list and print the index of each item in the list by plus 1 and the value of its "name" attribute.
     return hero_list


def select_hero():
    show_heroes()
    # Get user input for hero pick
    hero_pick = input('Choose a hero')
    # Call the show_hero function with hero_pick as argument
    show_hero(hero_pick)
    return_home()

def show_hero(pick):
    query = f"""
        SELECT
            id,
            name,
            about_me,
            biography
        FROM heroes
        WHERE heroes.id = {pick}; 
    """
    # Construct a SQL query string that retrieves the hero's ID, name, about me and biography from the heroes table in the database where the hero's ID is equal to pick
    hero = execute_query(query).fetchall()
    # Execute the SQL query using execute_query function and fetch all the results
    for count in range(len(hero)):
        value = hero[count]
        print(f"""
        {value[0]}: {value[1]}
        {value[2]}
        {value[3]}    
        """)
# f string
# string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.
#  the output format assumes that the value variable is a tuple with exactly four elements.
#  If the number of elements is different, the string formatting will need to be adjusted accordingly.
# Loop through each row in the hero result set and
    
def create_hero():
    name = input('Welcome to create a hero, input info now')
    # Ask the user to input information about the hero
    about = input('welcome ' + name + '! input for info ')
    bio = input('BIO HERE')
    # Call the function to add the hero with the provided information
    add_hero(name, about, bio)
    # Return to the home screen
    return_home()


def add_hero(name, about, bio):
    # Create the SQL query to insert a new hero into the database
    query = """
        INSERT INTO heroes (name, about_me, biography)
         VALUES (%s, %s, %s)
    """
    # Execute the SQL query with the provided information
    execute_query(query, (name, about, bio))
    # Show the list of all heroes in the database
    show_heroes()

def return_home():
    while True:
# Ask the user if they want to go back to the home screen
        answer = input("go home")
        if answer == "":
            print(acs)
            display_menu()
 # If the user pressed enter, display the menu and break out of the loop
            break
start_game()
