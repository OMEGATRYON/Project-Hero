from database.db_connection import execute_query

acs = """ 
      
██     ██  ██████  ██████  ██      ██████       ██████  ███████     ██   ██ ███████ ██████   ██████  ███████ 
██     ██ ██    ██ ██   ██ ██      ██   ██     ██    ██ ██          ██   ██ ██      ██   ██ ██    ██ ██      
██  █  ██ ██    ██ ██████  ██      ██   ██     ██    ██ █████       ███████ █████   ██████  ██    ██ ███████ 
██ ███ ██ ██    ██ ██   ██ ██      ██   ██     ██    ██ ██          ██   ██ ██      ██   ██ ██    ██      ██ 
 ███ ███   ██████  ██   ██ ███████ ██████       ██████  ██          ██   ██ ███████ ██   ██  ██████  ███████ 
                                                                                                            
  
  1. create hero
  2. about current hero
  3. change hero info
"""
def initiate_game():
    start_response = input('Press ENTER to START')
    if start_response == "":
        print(acs)
        main_menu()
        
def main_menu():
    response = input("What would you like to do first? ")
    if response == "1":
        input_create_hero()
    elif response == "2":
        input_select_hero()
    elif response == '3':
        print(input_update_hero())

def show_all_heroes():
     query = """
        SELECT name from heroes
     """
     hero_list = execute_query(query).fetchall()
     for num, value in enumerate(hero_list):
         print(f"{num + 1}: {value[0]}")
     return hero_list

# Shows the list of heroes and asks for user to type in a number corresponding with hero id number
def input_select_hero():
    show_all_heroes()
    hero_pick = input('Choose a hero to get to know...')
    select_a_hero(hero_pick)
    return_to_main_menu()

def select_a_hero(pick):
     query = f"""
        SELECT
            id,
            name,
            about_me,
            biography
        FROM heroes
        WHERE heroes.id = {pick}; 
     """
     hero = execute_query(query).fetchall()
     for count, value in enumerate(hero):
        print(f"""
        {value[0]}: {value[1]}
        {value[2]}
        {value[3]}    
        """)
    
def input_create_hero():
    name = input('Welcome to create a hero, input info now')
    about = input('welcome ' + name + '! input for info ')
    bio = input('BIO HERE')
    create_new_hero(name, about, bio)
    return_to_main_menu()


def create_new_hero(name, about, bio):
    query = """
        INSERT INTO heroes (name, about_me, biography)
         VALUES (%s, %s, %s)
    """
    execute_query(query, (name, about, bio))
    show_all_heroes()

def return_to_main_menu():
    while True:
        answer = input("Press enter to return to the main menu, or type 'back' to go back to the hero selection menu: ")
        if answer == "":
            print(acs)
            main_menu()
            break
        elif answer.upper() == "BACK":
            input_select_hero()
            break

initiate_game()