# Student name: Minhui Roh
# McGill ID: 261120462

ROOM_NAME = "No cheating"
AUTHOR = "Minhui"
PUBLIC = True

def escape_room():
    """ () -> NoneType
    Takes no input and returns nothing.
    It allows the user to play the escape room game using various commands as user inputs.
    
    >>> escape_room()
    You have sneaked into a high school, trying to get the answer key ahead for finals.
    You walk into an empty classroom and start searching everywhere.
    But all of a sudden, the security alarm goes off and the door is locked behind you!

    You desperately try to reopen the door but find out that it is impossible.
    Suddenly, you realize that the moonlight coming from a window points at a desk in front of you.
    You found a dictionary on the desk and a drawer attached to the desk!
    What can you do to escape?

    > list commands
    examine window
    examine dictionary
    examine drawer

    > examine wInDoW
    This window seems to be locked as well.
    However, there is a keyhole and a keypad connected to it.

    > examine DiCTioNary
    The word CALCULUS is highlighted! Why though?

    > Examine DraWer
    You found a key! Where do you use it?

    > Examine Doors
    Try different commands

    > put the key into the keyhole and enter CALCULUS to the keypad
    Congratulations! You unlocked the window and escaped!
    """
    print(
        "You have sneaked into a high school, trying to get the answer key ahead for finals.\n"
        "You walk into an empty classroom and start searching everywhere.\n"
        "But all of a sudden, the security alarm goes off and the door is locked behind you!\n\n"
        "You desperately try to reopen the door but find out that it is impossible.\n"
        "Suddenly, you realize that the moonlight coming from a window points at a desk in front of you.\n"
        "You found a dictionary on the desk and a drawer attached to the desk!\n"
        "What can you do to escape?\n"
    )
    
    command = input("> ")
    while final_command(command) == False:
        if command == "list commands":
            print(
                "examine window\n"
                "examine dictionary\n"
                "examine drawer"
            )
        elif contain_window(command) != -1:
            print(
                "This window seems to be locked as well.\n"
                "However, there is a keyhole and a keypad connected to it."
            )
        elif contain_dictionary(command) != -1:
            print("The word CALCULUS is highlighted! Why though?")
        elif contain_drawer(command) != -1:
            print("You found a key! Where do you use it?")
        else:
            print("Try different commands")
        command = input("\n> ")
    print("Congratulations! You unlocked the window and escaped!")

def contain_window(command):
    """ (string) -> int
    Takes a string as an input and returns where does the word window first appears.
    If window is not contained in the string, return -1.
    
    >>> contain_window("examine window")
    8
    >>> contain_window("try to open WindOw")
    12
    >>> contain_window("examine door")
    -1
    """
    lower_command = command.lower()
    return lower_command.find("window")

def contain_dictionary(command):
    """ (string) -> int
    Takes a string as an input and returns where does the word dictionary first appears.
    If dictionary is not contained in the string, return -1.
    
    >>> contain_dictionary("examine dictionary")
    8
    >>> contain_dictionary("open DicTionary")
    5
    >>> contain_dictionary("examine door")
    -1
    """
    lower_command = command.lower()
    return lower_command.find("dictionary")

def contain_drawer(command):
    """ (string) -> int
    Takes a string as an input and returns where does the word drawer first appears.
    If drawer is not contained in the string, return -1.
    
    >>> contain_drawer("examine drawer")
    8
    >>> contain_drawer("try to open the DrAwer")
    16
    >>> contain_drawer("examine door")
    -1
    """
    
    lower_command = command.lower()
    return lower_command.find("drawer")

def final_command(command):
    """ (string) -> bool
    Takes a string as an input and returns a boolean indicating whether all keywords are contained
    in the string or not.
    
    >>> final_command("put the key into the keyhole and enter CALCULUS to the keypad")
    True
    >>> final_command("Key to keyhole and Calculus to keypad")
    True
    >>> final_command("key to keyhole")
    False
    """
    lower_command = command.lower()
    keyword_1 =lower_command.find("calculus")
    keyword_2 =lower_command.find("keypad")
    keyword_3 =lower_command.find("key")
    keyword_4 =lower_command.find("keyhole")
    if keyword_1 != -1 and keyword_2 != -1 and keyword_3 != -1 and keyword_4 != -1:
        return True
    else:
        return False

    
    