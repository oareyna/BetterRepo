from os import system as os
from time import sleep as s
import random as r
import sys


# carol
inventory, player_name, player_score, exam = [], input("Hello\nWhat is your name? "), 0, True
# keeps track of how many questions the user has gotten correct in order to move on to the next room
keys = 0


# Functions that prints out the objective and instructions for the game
def instructions():
    s(.5)
    os('cls')
    print("""OBJECTIVE:
    \n- Every correctly answered question will give you a part of a key 
    \n- You will need 3 parts of a key to obtain a key to open the next room.
    \n- If you answer a question incorrectly, another question will be asked. 
    \n- There's a total of 5 questions per room, each worth 10 points, but you only have 2 chances to make mistakes.
    \n""")


# Function that creates a menu and makes sure that the user can access the menu at any time
def menu():
    while True:
        print("Type 'help' to see the list of commands; 'r' to return")
        user_input = input("input: ").lower()
        # helps them return the test after they're finished checking the menu
        if user_input == "r":
            return 'r'
        # displays the user's options
        elif user_input == "help":
            print(":\n'o': Objective\n'i': Inventory\n's': View Score\n'q': Quit")
        # displays game instructions
        elif user_input == "o":
            instructions()
        # displays the user's inventory
        elif user_input == "i":
            print(inventory)
        elif user_input == 's':
            print('score: ', player_score)
        # quits the game
        elif user_input == "q":
            sys.exit()
        # makes the user input a valid input
        else:
            print("Invalid input. Please try again.")


# olivia
def end_screen1():
    # displays if the user fails the exam
    end_scene = """
   __   __                _ _     _   _   _  ___ _____                                  _ _ _ 
   \ \ / /__  _   _    __| (_) __| | | \ | |/ _ \_   _|   ___  ___  ___ __ _ _ __   ___| | | |
    \ V / _ \| | | |  / _` | |/ _` | |  \| | | | || |    / _ \/ __|/ __/ _` | '_ \ / _ \ | | |
     | | (_) | |_| | | (_| | | (_| | | |\  | |_| || |   |  __/\__ \ (_| (_| | |_) |  __/_|_|_|
     |_|\___/ \__,_|  \__,_|_|\__,_| |_| \_|\___/ |_|    \___||___/\___\__,_| .__/ \___(_|_|_)
                                                                            |_|               
  """

    print(end_scene)
    s(2)


def end_screen2():
    # displays if the user passes the exam
    end_scene = """
___  _ ____  _       ____  _  ____    _____ ____  ____  ____  ____  _____
\  \///  _ \/ \ /\  /  _ \/ \/  _ \  /  __// ___\/   _\/  _ \/  __\/  __/
 \  / | / \|| | ||  | | \|| || | \|  |  \  |    \|  /  | / \||  \/||  \  
 / /  | \_/|| \_/|  | |_/|| || |_/|  |  /_ \___ ||  \_ | |-|||  __/|  /_ 
/_/   \____/\____/  \____/\_/\____/  \____\\____/\____/\_/ \|\_/   \____\

    """
  
    print(end_scene)
    quit=input("Enter q to quit: ")
    while quit != "q":
      quit=input("Enter q to quit: ").lower()
    if quit == "q":
        exit()

# mary
def end_game():
    # if player gets less than a 70, than they fail
    if player_score <= 70:
        result = 'FAIL'
    # if player gets more than a 70, than if they did not pass the last test, they fail
    else:
        if not exam:
            result = 'FAIL'
        else:
            result = 'PASS'
    s(1)
    os('cls')

    print(f'''                                                                                                                                                      

        ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░                          
        ░░                                                                                                ██░░
        ░░                                                                                                  ██░░
        ░░                         Certified Associates in Python Programming                                ██░░
        ░░                                     End of exam report                                            ██░░
        ░░                                                                                                   ██░░
        ░░                                                                                                   ██░░
        ░░                                                                                                   ██░░
        ░░         CANDIDATE NAME: {player_name}                                    
        ░░         EXAM TITLE: PCAP - Certified Associate in Python Programming                              ██░░
        ░░         SCORE: {player_score}                                                                            
        ░░         RESULT:  {result}                                                                             ██░░
        ░░                                                                                                   ██░░
        ░░                                                                                                   ██░░
        ░░                                                                                                   ██░░
        ░░                                                                                                   ██░░
        ░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░           ██░░                  
        ░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░           ██░░                  
        ░░                                                                                                   ██░░
        ░░                                                                                                   ██░░ 
          ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░
                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░

        ''')
    quit=input("Enter q to quit: ")
    while quit != "q":
      quit=input("Enter q to quit: ").lower()
    if quit == "q":
        exit()

    s(3)
#Prints appropriate end screen according to whether the player passed or not the exam
    if result == 'PASS':
        print('Congratulations! You have passed your exam')
        end_screen2()
    else:
        end_screen1()
#exits program
    sys.exit()


# introduces player to the game
def main():
    os('cls')
    print(f"Welcome to Escape the PCAP, {player_name.title()}!\n")
    s(1)
    print('You find yourself trapped within the confines of a virtual maze.')
    s(2)
    print('Navigate through three distinct rooms,')
    s(2)
    print('which present themselves with challenges that only increases difficulty with every unlocked door.')
    s(2)
    print('This game will put your skills to the test, to see if you can ultimately break free from PCAPtivity.\n')
    s(2)
    input("\nPress [ENTER] to continue")
    instructions()
    print('Good luck!')
    s(2)
    print("\nAt any point during the test, type 'm' to access the options menu")
    s(1)
    input("\nPress [ENTER] to continue")
    os('cls')

    # initialize GameScene class where player enters maze
    class GameScene:
        def __init__(self, name, score):
            self.name = name
            self.score = score

    # initialize first room player enters
    class Room1(GameScene):
        def __init__(self, name, score, easy):
            super().__init__(name, score)
            self.easy = easy  # initialize variable for easy question dictionary
            self.__score = 0
            inventory.clear() #clears inventory list

            questions = list(easy.keys())  # assigns questions to a list to manipulate
            q = 1  # question number player starts on
            # amount of correct and incorrect response player answers
            correct, incorrect = 0, 0

            # prompts user with 5 easy questions
            for i in range(5):
                s(1)
                os('cls')
                print("\nAt any point during the test, type 'm' to access the options menu")

                question = r.choice(questions)  # selects questions from list at random
                while True:
                    print(f'question {q}:\n{question}') #prints question
                    s(1)
                    user_input = input('\nAnswer: ').upper() #requests user's answer

                    # if user input is valid response, check if is value of question in dictionary
                    if user_input in {'A', 'B', 'C', 'D'}:
                        if user_input == easy[question]:
                            score += 10
                            correct += 1
                            global player_score
                            player_score = score  # adds score in Room to player score
                            s(1)
                            print('+10'.rjust(20))

                            # lets user know that they have obtained a part of the key
                            if correct < 3:
                                inventory.append('partofkey') #adds part of key to inventory list
                                print('You have obtained a part of a key! ')
                            if correct == 3:
                                inventory.clear()
                                inventory.append('Key1') #Remove everything from inventory and adds a whole key
                                print('You have obtained a key! Finish the test to unlock the next door. ')
                                input("\nPress [ENTER] to continue")
                        else:
                            incorrect += 1
                            s(1)
                            print('incorrect'.rjust(20))
                        break
                    elif user_input == "M":
                        menu_result = menu()
                        if menu_result == 'r':
                            os('cls')  # Optionally clear screen when returning to the question
                            continue  # Continues with the same question if 'r' is returned
                            # Add additional conditions if other functionalities are to be handled differently
                        else:
                            print("Invalid input. Please try again.")
                            user_input = input(': ').upper() #Request new input if user's input is not one of the valid choices
                    else:
                        os('cls')
                        print("Invalid input. Please try again.\n")

                questions.remove(question)  # remove question to avoid repeating question
                q += 1
            # if the user misses 3 questions, they fail the test and end the game
            if incorrect >= 3:
                os('cls')
                print('You have reached the end of your exam')
                s(1)
                input('Press [Enter] to view results')
                end_game()
            else:
                pass

    # initialize second room player enters
    class Room2(GameScene):
        def __init__(self, name, score, medium):
            super().__init__(name, score)
            self.medium = medium  # initialize variable for medium question dictionary
            self.__score = score

            if 'Key1' in inventory: # Checks if item is in inventory
                print()
                os('cls')
                print('unlocking the door to the next room. You step forward, ready to face the next challenge.')
                s(1)
                print('You\'re greeted by another computer screen, presenting a new set of challenges to overcome.')
                s(1)
                print('\n\nTo unlock the door to the next room, you must answer at least 3 questions correctly.')
                s(1)
                print("\nAt any point during the test, type 'm' to access the options menu")
                input("\nPress [ENTER] to begin test")
            else:
                print('You have not obtained the key to unlock this door.')
                s(1)
                input("\nPress [ENTER] to return back to previous room")
                scene1()   # User replays previous room if key is not found in inventory
            inventory.clear()  # Previous key gets deleted from inventory


            questions = list(medium.keys())  # assigns questions to a list to manipulate
            q = 1  # question number player starts on
            # amount of correct and incorrect response player answers
            correct, incorrect = 0, 0
            print("\nAt any point during the test, type 'm' to access the options menu")
            # prompts user with 3 medium questions
            for i in range(5):
                s(1)
                os('cls')

                question = r.choice(questions)  # selects questions from list at random
                while True:
                    print(f'question {q}:\n{question}')
                    s(1)
                    user_input = input('\nAnswer: ').upper()

                    # if user input is valid response, check if is value of question in dictionary
                    if user_input in {'A', 'B', 'C', 'D'}:
                        if user_input == medium[question]:
                            self.score += 10
                            score += 10
                            correct += 1
                            global player_score
                            player_score = score
                            s(1)
                            print('+10'.rjust(20))

                            # lets user know that they have obtained a part of the key
                            if correct < 3:
                                inventory.append('partofkey')
                                print('You have obtained a part of a key! ')
                            if correct == 3:
                                inventory.clear()
                                inventory.append('Key2')  # Removes parts of keys from inventory and adds whole key
                                print('You have obtained a key! Finish the test to unlock the next door. ')
                                input("\nPress [ENTER] to continue")
                        else:
                            incorrect += 1
                            s(1)
                            print('incorrect'.rjust(20))
                        break
                    elif user_input == "M":
                        menu_result = menu()
                        if menu_result == 'r':
                            os('cls')  # Optionally clear screen when returning to the question
                            continue  # Continues with the same question if 'r' is returned
                            # Add additional conditions if other functionalities are to be handled differently
                        else:
                            print("Invalid input. Please try again.")
                            user_input = input(': ').upper()
                    else:
                        os('cls')
                        print("Invalid input. Please try again.\n")
                questions.remove(question)  # remove question to avoid repeating question
                q += 1
            # if the user misses 3 questions, they fail the test and end the game
            if incorrect >= 3:
                os('cls')
                print('You have reached the end of your exam')
                s(1)
                input('Press [Enter] to view results')
                end_game()
            else:
                pass

    class Room3(GameScene):
        def __init__(self, name, score, hard):
            super().__init__(name, score)
            self.hard = hard  # initialize variable for medium question dictionary
            self.__score = score

            if 'Key2' in inventory: # Checks if item is in inventory, if it is, prints new room storyline
                print()
                os('cls')
                print('As you step into the last room, you\'re enveloped by an allure of the atmospheres intrigue.')
                s(2)
                print('To unlock the final door to your freedom, you must answer at least 3 questions correctly.')
                s(1)
                input("\nPress [ENTER] to begin the final test")
            else:
                print('You have not obtained the key to unlock this door.')
                s(1)
                input("\nPress [ENTER] to return back to previous room")
                scene2()    # User replays previous room if key is not found in inventory
            inventory.clear()


            questions = list(hard.keys())  # assigns questions to a list to manipulate
            q = 1  # question number player starts on
            # amount of correct and incorrect response player answers
            correct, incorrect = 0, 0

            # prompts user with 2 hard questions
            for i in range(5):
                s(1)
                os('cls')

                question = r.choice(questions)  # selects questions from list at random
                while True:
                    print(f'question {q}:\n {question}')
                    s(1)
                    user_input = input('\nAnswer: ').upper()

                    # if user input is valid response, check if is value of question in dictionary
                    if user_input in {'A', 'B', 'C', 'D'}:
                        if user_input == hard[question]:
                            self.score += 10
                            score += 10
                            correct += 1
                            global player_score
                            player_score = score
                            s(1)
                            print('+10'.rjust(20))
                        else:
                            incorrect += 1
                            s(1)
                            print('incorrect'.rjust(20))
                        break
                    elif user_input == "M":
                        menu_result = menu()
                        if menu_result == 'r':
                            os('cls')  # Optionally clear screen when returning to the question
                            continue  # Continues with the same question if 'r' is returned
                            # Add additional conditions if other functionalities are to be handled differently
                        else:
                            print("Invalid input. Please try again.")
                            user_input = input(': ').upper()
                    else:
                        os('cls')
                        print("Invalid input. Please try again.\n")
                questions.remove(question)  # remove question to avoid repeating question
                q += 1
            # if the user misses 3 questions, they fail the test and end the game
            if incorrect >= 3:
                os('cls')
                print('You have reached the end of your exam')
                s(1)
                input('Press [Enter] to view results')
                exam = False
                end_game()
            else:
                os('cls')
                pass

    # function that passes name and score to scene 1
    def scene1():
        scene = Room1(player_name, player_score, {'''    How do you declare a variable in Python?

A. Car=”Toyota”
B. _car==Yes
C. Car==”Toyota”
D. Car-”Toyota”''': 'A', '''    How do you declare a Python function?

A. Def function()
B. def Function()
C. Function()
D. new function()''': 'B', '''    What is the syntax to comment in Python?

A. #
B. >
C. <
D. +''': 'A', '''How do you define a class in Python?

A. Class new
B. class New
C. New Class
D. Class(New)''': 'B', '''What is an example of a conditional?

A. elif
B. no
C. yes
D. of course''': 'A', '''What does DHCP stand for?

A. Domain Host Configuration Protocol
B. Dynamic Host Configuration Protocol
C. Domain Host Confined Protocol
D. Domain Host Configuration Process''': 'B', '''What is a firewall?

A. a network security device or software that monitors and controls 
    only outgoing network traffic based on predetermined security rules
B. A wall on fire
C. a single entity but a vast interconnected network of networks, 
        often referred to as the "network of networks."
D. a network security device or software that monitors and controls incoming
        and outgoing network traffic based on predetermined security rules''': 'D', '''What does LAN stand for?

A. Local access neural
B. Local area network
C. Local access network
D. Local area neural''': 'B', '''What does WAN stand for?

A. Wide Affect Network
B. World Area Network
C. Wide Area Network
D. Will Accept Network''': 'C', '''What does VPN stand for? 

A. Virtual Private Network
B. Virtual Personal Network
C. Volatile Private Network
D. Virtual Personal Netting''': 'A'})

# janay
    # function that passes name and score to scene 2
    def scene2():
        scene = Room2(player_name, player_score, {'''    How can you define a multi-line string in Python?

A. Using single quotes ('')
B. Using double quotes ("")
C. Using triple single quotes (''' ''')
D. Using double single quotes (""' '"")''': 'C', '''    What is the difference between '==' and '!=' in Python?

A. '==' means it is equal to, while '!=' means it is NOT equal to
B. '==' means it is NOT equal to, while '!=' means it is equal to
C. Both '==' and '!=' mean the same thing
D. None of the above''': 'A', '''    How do you define a set in Python?

A. Using curly braces ({})
B. Using square brackets ([])
C. Using parentheses (())
D. Using angle brackets (<>)''': 'A', '''How do you check the length of a string in Python?

A. len(string)
B. length(string)
C. string.length()
D. size(string)''': 'A', '''How do you remove an item from a list in Python?

A. list.remove(item)
B. list.delete(item)
C. del list[item]
D. list.pop(item)''': 'C', '''What does "bandwidth" mean in networking?

A. The speed of data transmission over a network
B. The amount of data that can be transmitted over a network in a given time
C. The distance between network devices
D. The reliability of network connections''': 'B', '''What is an example of a protocol?

A. HTTP
B. Python
C. Firewall
D. Ethernet''': 'A', '''What is the difference between TCP and UDP?

A. TCP uses less bandwidth than UDP
B. UDP has more overhead, which is why it is slower that TCP
C. TCP is connection-oriented, while UDP is connectionless
D. UDP guarantees packet delivery, TCP does not''': 'C', '''How do devices communicate in a peer-to-peer network?

A. Devices communicate through a central server
B. Devices communicate directly with each other without a central server
C. Devices communicate through multiple servers
D. Devices communicate through email only''': 'B', '''What is the purpose of a firewall in a network?

A. To speed up internet connection
B. To prevent unauthorized access to or from a private network
C. To increase bandwidth in the network
D. To improve network security by encrypting data''': 'B'})

# mary
    # function that passes name and score to scene 3
    def scene3():
        scene = Room3(player_name, player_score, {'''    Which of the invocations should be used instead of XXX?

class Class:
    def __init__(self,val):
        self.val = val
    def get(self):
return self.val
def show(self):
    XXX

A. print (get(self))
B. print (self.get())
C. print (get())
D. print (self.get (val))''': 'B', '''    What is the expected output of the following snippet?

class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass

X = Z()
Z = Z()

A. True False
B. True True
C. False False
D. False True''': 'A', '''    Which of the following expressions will always evaluate to True?

import random

random.seed(1)
v1 = random.random()
random.seed(1)
v2 = random.random()

A. v1 >== 1
B. v1 == v2
C. len(random.sample([1,2,3],2)) > 2
D. random.choice([1,2,3]) >=1''': 'D', '''How do you check the length of a string in Python?

def unclear(x):
    if x % 2 == 1:
        return 0
print (unclear(1) + unclear(2))

It will:
A. print 0
B. cause a runtime exception
C. prints 3
D. print an empty line''': 'B', '''What is the expected output of the following code?

def f (n):
    if n == 1:
        return 1
    return n + f (n-1)
print (f(2))

A. 21
B. 12
C. 3
D. none''': 'C', '''A method for passing the arguments used by the following snippet is called:

def fun(a, b):
    return a + b
res = fun(1,2)

A. sequential
B. named
C. positional
D. keyword''': 'C', '''What is the expected behavior of the following code?

def f(n):
    for i in range(1, n+1):
        yield i
for i in f(2):
    print(i, end=' ')

It will:
A. print 2 1
B. print 1 2
C. cause a runtime exception
D. print <generator object f at (some hex digits)>''': 'A'})

    print('\nAs you step into an unknown space within the maze,')
    s(1)
    print('you find yourself in a dimly lit room, illuminated only by the soft glow of a computer screen.')
    s(1)
    print('On the screen, appears an objective: \n\n')
    s(1)
    print(
        'To unlock the door to the next room, you must prove your skills by answering at least 3 questions correctly.')
    s(1)
    input("\nPress [ENTER] to begin test")
    scene1()
    os('cls')
    print('Upon successfully completing the test, the room begins to radiantly shimmer. ')
    s(1)
    print('the computer screen flickers, bestowing upon you a shimmering key,')
    s(1)
    input("\nPress [ENTER] to unlock door")

    scene2()

    os('cls')
    s(1)
    print('As the last question is answered, a cascade of code erupts from the screen before you..')
    s(1)
    print('The once dimly lit space transforms into a digital masterpiece,')
    s(1)
    print('With the last keystroke, you execute the program, and the screen shimmers, revealing a radiant key.')
    s(1)
    print('Grasping it in your hand, you begin your way towards the next and final room.')
    s(1)
    input("\nPress [ENTER] to unlock door")

    scene3()

    print('As the final question is answered, the virtual maze around you begins to shift and transform.')
    s(1)
    print('With each line of code you write, the illusions of the virtual maze fade away.')
    s(1)
    print('Paths that once seemed blocked now open up, which guide you to the exit. ')
    s(1)
    input("\nPress [ENTER] to continue")
    os('cls')
    print('near the exit, you discover a glowing terminal, upon which rests a certification and a black hoodie')
    s(1)
    print('As you claim it, As the gate to success swings open,')
    s(1)
    print('You step through, eager to embrace the endless possibilities that lie beyond in the realm of programming.')
    s(1)
    input("\nPress [ENTER] to view certificate")
    end_game()

main()