import time
import random
import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='demogame',
    user='root',
    password='Lontoo2023',
    autocommit=True
)


# FUNCTIONS

import textwrap

def introduction():

    print("                                   !Welcome to Time Travel Adventure!          ")
    time.sleep(1.5)
    print("Year 1919, the world was engulfed in chaos. There was no safe haven, and the roads were fraught with peril.")
    time.sleep(1.5)
    print("As you wake up in this turbulent time, the world around you is a battlefield, a place of uncertainty and danger")
    time.sleep(1.5)
    print("The deafening sounds of artillery and gunfire echo in the distance. You initially think it's a dream, but reality soon sets in.")
    time.sleep(1.5)
    print("Beside you lies an unconscious soldier, severely injured and in immediate need of medical attention.")
    time.sleep(1.5)
    print("As you sit up, you discover a mysterious letter and a map tucked away in your pocket. ")
    time.sleep(1.5)
    print("With trembling hands, you open the letter, its words explaining your incredible situation: ")



def part_1():

    print("\nPart 1: The Letter")
    time.sleep(1.5)
    print("Greetings, intrepid traveler!")
    time.sleep(1.5)
    print("In a world on the brink of destruction, the fate of humanity rests in your hands as the chosen temporal protector.")
    time.sleep(1.5)
    print("You have always yearned for an adventurous life, and now you stand amid history's most turbulent moments.")
    time.sleep(1.5)
    print("Armed with unique abilities, you embark on a high-stakes journey through time and space.")
    time.sleep(1.5)
    print("Beside you is a brave soldier, and his life holds a crucial piece of information for the government, information that could help end this devastating war.")
    time.sleep(1.5)

introduction()
part_1


# select 30 airports for the game
def get_airports():
    sql = "SELECT iso_country, ident, name, type, latitude_deg, longitude_deg FROM airport WHERE iso_country IN ('VN', 'BD', 'IN', 'NP', 'CN', 'PH', 'MY', 'ID', 'FJ', 'CL', 'AR', 'BR', 'CR', 'JM', 'MX', 'US') AND type = 'large_airport' limit 20;"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# get all goals
def get_goals():
    sql = "SELECT * FROM goal;"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# create new game
def create_game(start_money, p_range, cur_airport, p_name, a_ports):
    sql = "INSERT INTO game (money, player_range, location, screen_name) VALUES (%s, %s, %s, %s);"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (start_money, p_range, cur_airport, p_name))
    g_id = cursor.lastrowid

    # add goals / loot boxes
    goals = get_goals()
    goal_list = []
    for goal in goals:
        for i in range(0, goal['probability'], 1):
            goal_list.append(goal['id'])

    # exclude starting airport
    g_ports = a_ports[1:].copy()
    #random.shuffle(g_ports)

    for i, goal_id in enumerate(goal_list):
        sql = "INSERT INTO ports (game, airport, goal) VALUES (%s, %s, %s);"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, (g_id, g_ports[i]['ident'], goal_id))

    return g_id


# get airport info
def get_airport_info(icao):
    sql = f'''SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


# check if airport has a goal
def check_goal(g_id, cur_airport):
    sql = f'''SELECT ports.id, goal, question, answer, wrong_answer, wrong_answer2
    FROM ports
    JOIN goal ON goal.id = ports.goal
    WHERE ports.game = %s
    AND ports.airport = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (g_id, cur_airport))
    result = cursor.fetchone()
    if result is None:
        return False
    return result


# calculate distance between two airports
def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km


# get airports in range
def airports_in_range(icao, a_ports, p_range):
    in_range = []
    for a_port in a_ports:
        dist = calculate_distance(icao, a_port['ident'])
        if dist <= p_range and not dist == 0:
            in_range.append(a_port)
    return in_range


# set loot box opened

# update location
def update_location(icao, p_range, u_money, g_id):
    sql = f'''UPDATE game SET location = %s, player_range = %s, money = %s WHERE id = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao, p_range, u_money, g_id))


# game starts
# ask to show the story
# storyDialog = input('Do you want to read the background story? (Y/N): ')
# if storyDialog == 'Y':
#     # print wrapped string line by line
#     for line in story.getStory():
#         print(line)

# GAME SETTINGS
print('When you are ready to start, ')
print(time)
player = input('type player name: ')

# boolean for game over and win
game_over = False
win = False

#start money = 1000
money = 1000
# start range in km = 2000
player_range = 10000

# score = 0
score = 0

# boolean for diamond found
questions = 0
right_answers = 0
wrong_answers = 0
travel = 0

# all airports
all_airports = get_airports()
# start_airport ident
start_airport = all_airports[0]['ident']

# current airport
current_airport = start_airport

# game id
game_id = create_game(money, player_range, start_airport, player, all_airports)

# GAME LOOP
while not game_over:
    # get current airport info
    airport = get_airport_info(current_airport)
    # show game status
    print(f'''You are at {airport['name']}.''')
    input('\033[32mPress Enter to continue...\033[0m')
    print(f"You have traveled to {travel} airports.")
    print(f'''You have answered to {questions} questions.\n
    Right answers: {right_answers}, Wrong answers: {wrong_answers}.
    You have {money:.0f}$ and {player_range:.0f}km of range.''')
    # pause
    # if airport has goal ask if player wants to open it
    # check goal type and add/subtract money accordingly
    goal = check_goal(game_id, current_airport)
    if goal:
        print(f'Theres a question in this airport!')
        print('If you answer correctly you will be awarded 500km of range!')
        print('If you answer incorrectly you will lose 500km of range!')
        print(f"{goal['question']} (Answer in A,B,C)")
        print(f"{goal['answer']}, {goal['wrong_answer']}, {goal['wrong_answer2']}")
        user = input('Enter you answer here: ').upper()
        if user == goal['answer'][0]:
            print(f'Your answer was correct! As a reward you get 500$ and 500km of range!')
            #money += 500
            player_range += 1
            00
            questions = 1
            right_answers += 1
            travel += 1
        else:
            print(f'Your answer was incorrect! As a penalty, you lose 500km of range')
            player_range -= 100
            wrong_answers += 1
            questions += 1
            travel += 1

    if wrong_answers >= 3:
        game_over = True
        print(f"You lost the game! You gave the wrong answer for three times. Better luck next time!")

    # if no range, game over
    # show airports in range. if none, game over
    airports = airports_in_range(current_airport, all_airports, player_range)
    print(f'''\033[34mThere are {len(airports)} airports in range: \033[0m''')
    if len(airports) == 0:
        print('You are out of range.')
        print('You lost the game as you are not able to travel to any other airport. Better luck next time!')
        game_over = True
    else:
        print(f'''Airports: ''')
        for airport in airports:
            ap_distance = calculate_distance(current_airport, airport['ident'])
            print(f'''Country: {airport['iso_country']}, {airport['name']}, icao: {airport['ident']}, distance: {ap_distance:.0f}km''')
        # ask for destination
        dest = input('Enter destination icao: ').upper()
        selected_distance = calculate_distance(current_airport, dest)
        player_range -= selected_distance
        update_location(dest, player_range, money, game_id)
        current_airport = dest
        if player_range < 0:
            game_over = True

    #if current_airport == #Laittakaa tähän USA lentokenttä mihin tämä peli loppuu!:
        #print(f'''You won! You managed to navigate back to USA! You have {money}$ and {player_range}km of range left.''')
        #game_over = True


# if game is over loop stops
# show game result