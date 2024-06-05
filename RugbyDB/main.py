import sqlite3

def connect_to_db():
    db = sqlite3.connect('rugby.db')
    return db

def get_player_names(db):
    c = db.cursor()
    sql = "SELECT first_name,last_name FROM player"
    c.execute(sql)
    results = c.fetchall()
    print("{:<20} {:<20}".format('First Name', 'Last Name'))
    print("-" * 40)
    for result in results:
        print("{:<20} {:<20}".format(result[0], result[1]))

def get_all_player_details(db):
    c = db.cursor()
    sql = "SELECT * FROM player"
    c.execute(sql)
    results = c.fetchall()
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('ID', 'First Name', 'Last Name', 'Position', 'Debut Year', 'Tests', 'Tries Scored', 'Points Scored'))
    print("-" * 160)
    for result in results:
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))
        
def get_best_scorer(db):
    c = db.cursor()
    sql = "SELECT * FROM player ORDER BY points_scored DESC LIMIT 1"
    c.execute(sql)
    result = c.fetchone()
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('ID', 'First Name', 'Last Name', 'Position', 'Debut Year', 'Tests', 'Tries Scored', 'Points Scored'))
    print("-" * 160)
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))

def get_most_tests(db):
    c = db.cursor()
    sql = "SELECT * FROM player ORDER BY test_caps DESC LIMIT 1"
    c.execute(sql)
    result = c.fetchone()
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('ID', 'First Name', 'Last Name', 'Position', 'Debut Year', 'Tests', 'Tries Scored', 'Points Scored'))
    print("-" * 160)
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))


def close_db(db):
    db.close()

def main():
    db = connect_to_db()
    while True:
        print("1. Get player names")
        print("2. Get all player details")
        print("3. Get best scorer")
        print("4. Most Tests Played")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            results = get_player_names(db)
            print(results)
        elif choice == '2':
            results = get_all_player_details(db)
            print(results)
        elif choice == '3':
            results = get_best_scorer(db)
            print(results)
        elif choice == '4':
            results = get_most_tests(db)
            print(results)
        elif choice == '0':
            close_db(db)
            break
        else:
            print("Invalid choice. Please choose again.")
            
main()