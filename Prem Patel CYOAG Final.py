import random, time, sys
#import winsound
from termcolor import colored

triviaCorrectScore = 0
wordShuffleCorrectScore = 0
scalpelPickUp = 0
syringePickUp = 0
swipeCardPickUp = 0

################## DEFINITIONS OF TEACHER SUPPLIED FUNCTIONS ######################

def chooseOption(numberOfOptions):
  choice = 0
  while choice < 1 or choice > numberOfOptions:
    print('1 to ' + str(numberOfOptions) + '> ', end='')
    choice = input()
    if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
      choice = 0
    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
      choice = int(choice)
    print('\n\n')
    return choice

# pauses function until user presses enter
def pause():
  input('Press enter to continue.\n')

#skips intro when user wants to
def skip():
    print('\nDo you want to skip the intro? Y/N')
    skipIntro = input()
    if skipIntro=='N' or skipIntro=='n' :
        intro()

    start()
#winsound.PlaySound('almost50percent.wav', winsound.SND_ASYNC)
#Could not control volume, it was too loud, decided to leave it out

###################################################################################

def intro():

    print("You slowly open your eyes as the bright light of the room rushes to your eyes. You slowly adjust your eyes to the \nbrightness of the room that is as white as snow. “Christmas already?” you say as you wake up. \n")
    time.sleep(4)
    print("You had been living near a radiated site for years as Fortune 500 companies were found to be illegally dumping nuclear waste.\nYou had survived many weeks in severe radiation without any side effects or damages done to you. After finding out about your situation,\nyou had been visited by men in black suits and white lab coats several times before you were forcefully taken. \nThey insisted you were only being taken for “testing” and would be brought back soon. This is your last memory of the outside world.\nYou have completely forgotten the concept of time, seasons, and weather since it has been over\n5 months since you have been in the room. The last date you remember is January 21, 2027.\n")
    time.sleep(8)
    print('Waking up this time was different, you were not restrained like normal and were free to move around at your will.\n“Did they forget to restrain me, or are they ‘testing’ me again. You look around the room, which was mostly empty, and see a couple things.\nThe first thing that caught your eye was a lab cart with \nvarious objects on it, right behind the cart was a vent. You look around more and you see an exit as well. “Reminds me of portal 2, I \nwonder if im Atlas, or P-Body,” you say before deciding what to do next.\n You realize that this labratory is no normal labratory, It was rather unique. You had heard about many different rooms with games in them, or as the\nscientists refer to as a waste of time. I never really understood what they meant, but you feel like you will know soon enough. Also after seeing the\ndifferent tools on the cart, you realize that there will be many different paths you can take to escape from the laboratory\n')
    time.sleep(3.5)

def start():
    print("\nAfter you examine the room, you see a few things that you could do. ")

    time.sleep(1)
    startingFourOptions = "1. Stay in the room.\n2. Leave the room.\n3. Examine the lab cart.\n4. Go towards and examine the vent.\n"
    for char in startingFourOptions :
        sys.stdout.write(char)
        sys.stdout.flush()
        if char!="\n" :
            time.sleep(0.1)
        else:
            time.sleep(1)
    print("\nWhich one will you chose?")
    choice = chooseOption(4)
    if 1==choice :
        time.sleep(1)
        stayInRoom()
    elif 2==choice :
        time.sleep(1)
        leaveRoom()
    elif 3==choice :
        time.sleep(1)
        labCart()
    elif 4==choice :
        time.sleep(1)
        vent()
    else :
        print("Error!")

####################CHOICE 1: STAY IN THE ROOM####################

def stayInRoom():
    num = random.randint(0,100)
    if num >=45 and num <=65:
        personComesToRoom()
    else:
        stayInRoom2()

def stayInRoom2():
    print("You waited in the room for 15 minutes and no one came. \nDo you want to rethink your choice?(Y/N)")
    stayRoom = input()
    if stayRoom =='Y' or stayRoom =='y' :
        time.sleep(1)
        print("\n1. Leave the room.")
        print("2. Examine the lab cart.")
        print("3. Go towards and examine the vent more.")

        choice = chooseOption(3)
        if 1==choice :
            leaveRoom()
        elif 2==choice :
            labCart()
        elif 3==choice :
            vent()
        else :
            print("Error!")
    elif stayRoom =='N' or stayRoom =='n' :
         personComesToRoom()

def personComesToRoom():
    print('\nYou hear footsteps come closer and closer, you hope to strike a passive conversation with him\nHe did not share the same views, He got close to you and immediately injected you with something.\nYou start to feel drowsy, and slowly, your consciousness starts to fade.')
    ohCrapText = colored('''"Oh crap crap craa..." You said''', 'grey', attrs=['bold'])
    print(ohCrapText)
    print(ASCII_THUD)
    print("You fell to the ground completely unconscious")
#################################################################
####################CHOICE 2: LEAVE THE ROOM####################

def leaveRoom():
    print('''After exiting the room, you see a hallway that goes pretty far. "It is almost as white as the room I was kept in, maybe I'm in Santa's workshop"\nyou say as you are walking down the hallway, but you quickly realize that you share no similarities to an elf to be in his workshop. \n''')
    time.sleep(1)
    print('''You get to the end of the white hallway which you were walking down for for at least 5 minutes. At the end it splits off two ways\non the left side you hear a faint sound, and on the right you see a room that finally is not white, \nthe first color you've seen that's not on the grey-scale.\n''')
    print('''Which way will you decide to go?\n ''')
    time.sleep(1)
    print("1. Left towards the faint noise")
    print("2. Right towards the colored room")
    choice = chooseOption(2)
    if 1==choice :
        leftNoiseRoom()
    elif 2==choice :
         rightColoredRoom()
    else :
        print("Error!")

def leftNoiseRoom():
    print("""As you approach the room, the noise gets louder, as you would assume.\nYou arrive at the room where the noise is coming from, it sounds like English, but it seems to be automated. With some hesitation, you open the door.\nThe room is mostly vacant with only a TV on the wall, and several in-built speakers on the roof""")
    name = input("Enter a temporary username: ")
    print("Greetings, " + name + ", I am Beru. Welcome to the authorization game. We will confirm your identity through a series of tests.\nWe will be asking you a few trivia question which every worker should know the answer to.\n\nAre you ready to begin? (Y/N)")
    readyToPlayTrivia = input()
    if readyToPlayTrivia=='Y' or readyToPlayTrivia=='y' :
        authorizationTrivia()
    else:
        leftRoomDeath()

def leftRoomDeath():
    print("You are not authorized to be in this vicinity. Goodbye enemy.\n")
    print("The doors behind you shut tight, and you start hearing a vacuum.\nYou finally realised what was happening after you start having difficulty breathing properly, the air was being sucked out of the room, you were being trapped in a air-tight vacuum.\nYou fell due to the lack of air and lost consciousness eventually")
    hypoxiaDeathMessage = colored("You have died due to hypoxia", 'red', attrs=['bold', 'underline', 'blink'])
    print(hypoxiaDeathMessage)

def authorizationTrivia():
    print("\nWelcome to the authorization test, you will be asked 6 questions.\nA failure to get 50% of the questions correct will lead to an early retirement for you.")
    time.sleep(1.5)

    for i in range(0, 6):
        ((updatedQuestionsList[i]()))
    triviaEnd()

def triviaQuestion1():
    global triviaCorrectScore
    print("\n\nWhat is the 100th element in the Periodic table with a symbol of Fm? \nHint: It is named after the creator of the first nuclear reactor Enrico Fermi\n")
    triviaAnswer1 = input("Your answer: ")
    if triviaAnswer1 == 'Fermium' or triviaAnswer1 == 'fermium':
        triviaCorrectScore += 1
    else:
        triviaCorrectScore += 0

def triviaQuestion2():
    global triviaCorrectScore
    print("\n\nWhat is the painting “La Gioconda” more usually known as\n")
    triviaAnswer2 = input("Your answer: ")
    if triviaAnswer2 == 'the mona lisa' or triviaAnswer2 == 'The Mona Lisa'or triviaAnswer2 == 'The mona lisa':
        triviaCorrectScore += 1
    else:
        triviaCorrectScore += 0

def triviaQuestion3():
    global triviaCorrectScore
    print("\n\nWhat is Chandler’s last name in the sitcom Friends\n")
    triviaAnswer3 = input("Your answer: ")
    if triviaAnswer3 == 'Bing' or triviaAnswer3 == 'bing':
        triviaCorrectScore += 1
    else:
        triviaCorrectScore += 0

def triviaQuestion4():
    global triviaCorrectScore

    print("\n\nWho starts first in chess, black or white?\n")
    triviaAnswer4 = input("Your answer: ")
    if triviaAnswer4=='White' or triviaAnswer4=='white' :
        triviaCorrectScore += 1
    else :
        triviaCorrectScore += 0

def triviaQuestion5():
    global triviaCorrectScore
    print("\n\nThe fear referred to as arachnophobia indicates a fear of what?\n")
    triviaAnswer5 = input("Your answer: ")
    if triviaAnswer5=='Spider' or triviaAnswer5=='spider' or triviaAnswer5=='spiders' or triviaAnswer5=='Spiders':
        triviaCorrectScore += 1
    else :
        triviaCorrectScore += 0

def triviaQuestion6():
    global triviaCorrectScore
    print("\n\nWhat body was demoted from planet status in 2006?\n")
    triviaAnswer6 = input("Your answer: ")
    if triviaAnswer6=='Pluto' or triviaAnswer6=='pluto' :
        triviaCorrectScore += 1
    else :
        triviaCorrectScore += 0

def triviaQuestion7():
    global triviaCorrectScore
    print("\n\nWhat is the name of Yoda’s home?\n")
    triviaAnswer7 = input("Your answer: ")
    if triviaAnswer7=='Dagobah' or triviaAnswer7=='dagobah' :
        triviaCorrectScore += 1
    else :
        triviaCorrectScore += 0

def triviaQuestion8():
    global triviaCorrectScore
    print("\n\nAccording to the Dr. Seuss book, who stole Christmas?\n")
    triviaAnswer8 = input("Your answer: ")
    if triviaAnswer8=='The Grinch' or triviaAnswer8 == 'the grinch':
        triviaCorrectScore += 1
    else :
        triviaCorrectScore += 0

def triviaQuestion9():
    global triviaCorrectScore
    print("\n\nWhat type of fish is Nemo?\n")
    triviaAnswer9 = input("Your answer: ")
    if triviaAnswer9=='Clownfish' or triviaAnswer9=='clownfish' :
        triviaCorrectScore += 1
    else :
        triviaCorrectScore += 0

def triviaQuestion10() :
    global triviaCorrectScore
    print("\n\nWhere is the Great Pyramid of Giza located?\n")
    triviaAnswer10 = input("Your answer: ")
    if triviaAnswer10=='Egypt' or triviaAnswer10=='egypt' :
        triviaCorrectScore += 1
    else :
        triviaCorrectScore += 0

triviaQuestionsList = [triviaQuestion1, triviaQuestion2, triviaQuestion3, triviaQuestion4, triviaQuestion5,
                       triviaQuestion6, triviaQuestion7, triviaQuestion8, triviaQuestion9, triviaQuestion10]
updatedQuestionsList = random.sample(triviaQuestionsList, 6)

def triviaEnd():
    triviaCorrectScore_str = str(triviaCorrectScore)
    print("\n\nYou have completed the trivia game.\n")
    print("Score: " +triviaCorrectScore_str+"/6")
    if triviaCorrectScore == 6:
        print("You achieved a perfect score, you are now authorized to be in this room.\n")
        print(ASCII_100)
        pause()
        triviaEscapeDoor()

    elif triviaCorrectScore >= 3:
        print("You have been authorized to be in this room.")
        pause()
        triviaEscapeDoor()

    else:
        print("You did not meet the minimum requirement to be authorized to be in this room. ")
        triviaFailEnding()

def triviaEscapeDoor():
    time.sleep(0.8)
    print("After completing the trivia meeting the requirements, Beru told you that you were authorized to be in the room.\nWondering what you could do in that room you spot the door, the only thing that seems to be significant in the room.\nInterested to know what is behind that door, you open the door which leads you straight to an emergency exit.\nYou, in hopes of escaping, quickly sprint through the emergency exit and make it to the outside world.")
    time.sleep(1)
    triviaEscapeWord = colored("\n\nYou have escaped!\n\n", 'green', attrs=['bold', 'underline', 'blink'])
    print(triviaEscapeWord)

def triviaFailEnding():
    print("Quite upset about losing the game, you forgot what the punishment was to not passing the required authorization test.\nWithout realising, the room had automatically started filling up with carbon monoxide, which is a silent killer.\nIt silently pumped out so much carbon monoxide that you had fell unconscious in under 10 minutes.\n\n")
    time.sleep(1)
    monoxideDeathMessage = colored("You have died due to carbon monoxide poisoning\n\n", 'red', attrs=['bold', 'underline', 'blink'])
    print(monoxideDeathMessage)

def rightColoredRoom():
    print("The room got more colorful than the surrounding area as he got closer, Once he arrived, \nthere was a big table with a screen on it, a big one, and it seemed to be touchscreen, as soon as you enter the room, the door behind you closes and a\nmessage  pops up on the screen asking him to play a game to continue to the next door.")
    print('\nThe top of the screen, what seems like the title reads "Word Shuffler" ')
    time.sleep(1)
    print('''\nAre you ready to begin? (Y/N)''')
    readyToPlayGame = input()
    if readyToPlayGame=='Y' or readyToPlayGame=='y' :
        wordShuffleGame()

    else :
        rightRoomDeath()

def rightRoomDeath():
    print("A failure to attempt the play the game has resulted in the extermination of you, the player.")
    time.sleep(1)
    noAttemptMessage = colored("You were disposed of for the failure to play the game\n\n", 'red',
                                   attrs=['bold', 'underline', 'blink'])
    print(noAttemptMessage)

def wordShuffleGame():
    name = input("\nWhat is your username: ")
    print("\n\nHello " + name + " and welcome to this test. The purpose of this test is to prove to us that you are a worker here and not an outsider.\nThis game will give you a shuffled word which you have to unshuffle and type the correct word in.\nYou will be given four shuffled words. To pass you need to answer a majority of them correctly. Answers must be typed in all lowercase.\nA failure to do so will result in the extermination of the player. ")
    time.sleep(2)
    wordShuffleQuestion1()

def wordShuffleQuestion1():
    global wordShuffleCorrectScore
    word1 = "flower"
    shuffledWord1 = str(random.sample(word1, len(word1)))

    print("\n\nThe first shuffled word is: \n" + shuffledWord1)
    shuffledAnswer1 = input("Type in your answer here: ")
    if shuffledAnswer1 == 'flower':
        print('\nYou got the right answer.')
        wordShuffleCorrectScore += 1
    else:
        print('\nYou typed in the wrong answer')
        wordShuffleCorrectScore += 0

    wordShuffleQuestion2()

def wordShuffleQuestion2():
    global wordShuffleCorrectScore

    word2 = "parenthesis"
    shuffledWord2 = str(random.sample(word2, len(word2)))

    print("\n\nThe second shuffled word is: " + shuffledWord2)
    shuffledAnswer2 = input("Type in your answer here: ")
    if shuffledAnswer2 == 'parenthesis':
        print('\nYou got the right answer.')
        wordShuffleCorrectScore += 1
    else:
        print('\nYou typed in the wrong answer')
        wordShuffleCorrectScore += 0


    wordShuffleQuestion3()

def wordShuffleQuestion3():
    global wordShuffleCorrectScore

    word3 = "shuffle"
    shuffledWord3 = str(random.sample(word3, len(word3)))

    print("\n\nThe third shuffled word is: " + shuffledWord3)
    shuffledAnswer3 = input("Type in your answer here: ")
    if shuffledAnswer3 == 'shuffle':
        print('\nYou got the right answer.')
        wordShuffleCorrectScore += 1
    else :
        print('\nYou typed in the wrong answer')
        wordShuffleCorrectScore += 0
    wordShuffleQuestion4()

def wordShuffleQuestion4():
    global wordShuffleCorrectScore

    word4 = "adventure"
    shuffledWord4 = str(random.sample(word4, len(word4)))

    print("\n\nThe fourth shuffled word is: " + shuffledWord4)
    shuffledAnswer4 = input("Type in your answer here: ")
    if shuffledAnswer4 == 'adventure':
        print('\nYou got the right answer.')
        wordShuffleCorrectScore += 1
    else :
        print('\nYou typed in the wrong answer')
        wordShuffleCorrectScore += 0
    shuffledWordGameEnd()

def shuffledWordGameEnd():
    wordShuffleCorrectScore_str = str(wordShuffleCorrectScore)
    print("\n\nYou have completed the trivia game.\n")
    print("Score: " +wordShuffleCorrectScore_str  + "/4")
    if wordShuffleCorrectScore == 4:
        print("You achieved a perfect score, you are now able to go to the next room.\n")
        print(ASCII_100)
        pause()
        shuffleGameNextRoom()
    elif wordShuffleCorrectScore >= 2:
        print("You have been authorized to go to the next room.\n")
        pause()
        shuffleGameNextRoom()
    else:
        print("You did not meet the minimum requirement to continue to the next room.\n")
        shuffleGameRoomFail()

def shuffleGameNextRoom():
    print('As you meet the minimum requirements for the next door to open, you go towards the door.\nAfter giving in a slight push, it opens up. You see greenery and forestry everywhere, \nand a populated further down, showing that you had were on a hill. Before you were seen, you quickly ran as fast as you could towards\nthe populated are in hopes for escape from the laboratory, and to return back to your home.')
    time.sleep(1)
    shuffleEscapeMessage = colored("\n\nYou have escaped!\n\n", 'green',
                              attrs=['bold', 'underline', 'blink'])
    print(shuffleEscapeMessage)

def shuffleGameRoomFail():
    print('''As you see the error message, you start to worry what will happen to you. As soon as you finished that sentence in your head, \nyou heard a voice from the speaker that said "Outsiders will be exterminated" as the floors which you were standing on fell like trap doors.\nYou try to grab on to something to save you from falling but you were too late and just barely missed the ledge. Now, seemingly slow, you are falling further and further into the darkness.''')
    time.sleep(1)
    fallingDeathMessage = colored("You died on collision with the ground\n\n", 'red', attrs=['bold', 'underline', 'blink'])
    print(fallingDeathMessage)

######################################################################
####################CHOICE 3: EXAMINE THE LAB CART####################

def labCart():
    print("You walk over to the lab cart you were looking at, and the first thing you see is a scalpel much larger than normal scalpels.\nBeside the scalpel you see a syringe with a translucent liquid inside of it.\nThe third item on the cart was a swipe card that was fully white, except for a red circle in the middle that read NERV")
    print("Which one will you pick up?\n")
    time.sleep(1.2)
    print("1. The over-sized scalpel. " + "\U0001F52A")
    print("2. The syringe with a translucent liquid inside. " + "\U0001F489")
    print("3. The white swipe card. " + "\U0001F3B4")
    print("4. None of them.\n")

    choice = chooseOption(4)
    global scalpelPickUp
    global syringePickUp
    global swipeCardPickUp
    if 1==choice :
        scalpelPickUp += 1
        print('You have picked up the scalpel.')
        pause()
        time.sleep(0.5)
    elif 2==choice :
        syringePickUp += 1
        pause()
        print('You have picked up the syringe.')
        time.sleep(0.5)
    elif 3==choice :
        swipeCardPickUp += 1
        print('You have picked up the swipe card.')
        pause()
        time.sleep(0.5)
    elif 4==choice :
        print('You decided not to pick anything.')
        pause()
        time.sleep(0.5)
    else :
        print("Error!")

    personAppearsLabCart()

def personAppearsLabCart():
    print("\n\nJust as you decided on your choice, a person approaches from the exit. You see that he is dressed in all black,\njust like the guys that abducted you. In a random rush of courage, you try to ask him a question.\n")
    time.sleep(1)
    print('1. "Why am I unrestrained?"')
    print('2. "When can I leave?"')
    print('''3. "I'm just going to quietly leave if that's alright with you, see you around, I guess," you say very nervously.''')
    print('4. "so, When does the free trial end, and how can I cancel it."\n')

    choice = chooseOption(4)
    if 1==choice :
        print('The man in black replies "Just a mistake by a newbie, he will be dealt with soon."')
        time.sleep(1)
        print("\nScared for both the newbies life and yours, you try to figure out what your next plan of action is.")
    elif 2==choice :
        print('The man in black stays silent.')
        time.sleep(1)
        print("\nYou realise he most likely did not answer because they had no intention of letting you go.\nWorried for your future, you start trying to figure out what you will do next.")
    elif 3==choice :
        print('The man in black chuckles a bit, then replied with "You really think you can get away?."')
        time.sleep(1)
        print('\nAt this point you start to worry about what your future looks like, scared it will just be spent in this white room,\nYou start to brainstorm things you can do to escape.')
    elif 4==choice :
        print('"You really think this is a joke, try re-evaluating your situation first." said the man in black')
        time.sleep(1)
        print('\nRealising that it is no time for jokes, you heed to what he said and start to re-evaluate your situation, and what you will do next.')
    else :
        print("Error!")
    actionAgainstPerson()

def actionAgainstPerson():
    print("\nThinking there is no other choice, you decide the only chance you have at escaping is to attack him head on.\nWith some hesitation, you start going on the offensive, and begin to attempt to attack him.")

    if scalpelPickUp == 1:
        print('\nYou go in to attack, while doing so, you remember you picked up a scalpel earlier, you take that to use as your weapon.\nUnfortunately he is trained in close combat, he quickly disarmed you and detained you.')
        time.sleep(1)
        detainedMessage = colored("\n\nYou have been detained by an agent.\n\n", 'red',attrs=['bold', 'underline', 'blink'])
        print(detainedMessage)

    elif syringePickUp == 1:
        print('\nYou go in to attack the enemy, trained in close combat, he swiftly sweeps you off your feet.\nIn the process, the syringe you grabbed with the translucent liquid fell out of your pockets and broke on collision with the ground.\nThe liquid reacted with the oxygen in the air producing an invisible gas that put both of you to sleep.')
        time.sleep(1.5)
        immobilizedMessage = colored("\n\nYou have immobilized the man in black along with yourself, once backup arrives you will be detained again.\n\n", 'red', attrs=['bold', 'underline', 'blink'])
        print(immobilizedMessage)

    elif swipeCardPickUp == 1:
        print('You go in to fight, in a moment you pull out the swipe card you picked up, feeling upset that you picked up the worst object,\ntried throwing the cards in hopes to distract him to go grab another item. Miraculously he did get temporarily stopped\nby the card, but he had put a little too much power into deflecting it. It flew all the way to the other side of the room and hit a wall,\nwhich proceeded to light up a little square on the wall green and activated the emergency close function blocking off the main entrance with a\nsteel wall with the person on the other side of it. As this happens, another invisible\ndoor near the green light opened up leading a wall he saw a logo that said "NERV" just like on the swipe card,\nbut realised it was a garage with an exit and multiple cars and car keys as he went further down.\n')
        time.sleep(5)
        print(ASCII_NERV)
        time.sleep(2)
        garageEscapeMessage = colored("\n\nYou escape driving one of these cars and go as far as you can.\n\n",
            'green', attrs=['bold', 'underline', 'blink'])
        print(garageEscapeMessage)

    else:
        print('\nYou start to attempt to attack the person, the first attack you threw missed the person most\nlikely due to the amount of fear and nervousness you are feeling. The person swiftly knocks you to the ground.\nOn impact you faint because of your high heart rate.')
        time.sleep(1.3)
        faintedMessage = colored(
        "\n\nYou fainted in front of the person and you have been detained.\n\n",
        'red', attrs=['bold', 'underline', 'blink'])
        print(faintedMessage)

##################################################################
####################CHOICE 4: EXAMINE THE VENT####################

def vent():
    print("You go towards the vent and you see a screw that looks loose.\nYou reach over to go unscrew it, but it instantly blows out blue smoke, " + "\U0001F4A8" + " confused at\nwhat it is, you back up as fast as you could, but it was too late. You started feeling drowsy and fell unconscious.")
    ventEndMessage = colored("\nYou fell unconscious and were later found being unrestrained.\n\n", 'red', attrs=['bold', 'underline', 'blink'])
    time.sleep(1)
    print(ventEndMessage)

ASCII_NERV = r"""                            ___/ `-'  `-' `---.__
                      _,--'                     /
                     /                         /
                    /                         {_
  /|               |                            `---._
_/ |               |                                  `--.
\   \              |                                      \_
 `.  \             |                                        \
   `. '.           ;                                         `.
     `. '.        /                                            \_
       `. '.____,'                                               \
         '.                                                    _,'
           '.                                              ___/
             '.                               ,._   _  ___/
               '.                             \  `-' `'
===      ==== ==='.                            `--.
 |.\      ||   ||  '.                              `-.
 ||\\     ||   ||    '.                               `.
 || \\    ||   ||      '.                               }
 ||  \\   ||   ||______/|'.                             \
 ||   \\  ||   ||------ |  '.                            \
 ||    \\ ||   ||      '|    '.                          |
 ||     \\||   ||              '.                         \
 ||      \'|   ||         ./     '.                        |
====      === ============/        '.                      \
                                     '.                     \
                    _________      ____'.                   |
                     | ______`.     \  \ '.                 |
                     ||      \ \     \  \  '.                \
                     ||       ) )     \  \   '.               |
                     ||      / /       \  \    '.             }
                     ||____.'.'         \  \     '.          /
                     ||---. <.           \  \    //'.       /
                     ||    `. `.          \  \  //   '.     \
                     ||      \  \          \  \//      '.    |
                     ||       \  \          \  /         '.  |
                    ====       `._`.         \/            '.|"""

ASCII_THUD = r''' _   _               _ 
| | | |             | |
| |_| |__  _   _  __| |
| __| '_ \| | | |/ _` |
| |_| | | | |_| | (_| |
 \__|_| |_|\__,_|\__,_|'''

ASCII_100 = r'''  
   _______  ____ _   __
  <  / __ \/ __ (_)_/_/
  / / / / / / / /_/_/  
 / / /_/ / /_/ //_/_   
/_/\____/\____/_/ (_) 
                       '''






while True:

    # Start the game
    skip()

    # "Play again" user option
    time.sleep(3)
    print('\nWould you like to play again? Y/N')
    playAgain = input()
    if playAgain == 'Y' or playAgain == 'y':
        triviaCorrectScore = 0
        wordShuffleCorrectScore = 0
        scalpelPickUp = 0
        syringePickUp = 0
        swipeCardPickUp = 0

        continue    #continue loop

    elif playAgain == 'N' or playAgain == 'n':
        break       #leave while loop
    break




