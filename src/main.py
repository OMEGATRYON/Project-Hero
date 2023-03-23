from database.db_connection import execute_query

art = """ 
      
██   ██ ███████ ██████   ██████  ███████ ██ ██ ██ ██ 
██   ██ ██      ██   ██ ██    ██ ██      ██ ██ ██ ██ 
███████ █████   ██████  ██    ██ ███████ ██ ██ ██ ██ 
██   ██ ██      ██   ██ ██    ██      ██             
██   ██ ███████ ██   ██  ██████  ███████ ██ ██ ██ ██ 
                                                                              
  
"""

def select_all_heroes():
    query = "SELECT name FROM heroes"
    hero_list = execute_query(query).fetchall()
    return hero_list

def print_heroes(hero_list):
    for num, hero in enumerate(hero_list, start=1):
        print(f"{num}: {hero[0]}")

def main_menu():
    response = input("view the hero list? y or n ")
    if response == "y":
        hero_list = select_all_heroes()
        print_heroes(hero_list)

main_menu()