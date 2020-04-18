# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define main_character = Character("main",color="#000000")
define dude_rational = Character("RaTiOnAl",color="#296d98")
define dude_crazy  = Character("Crazy",color="#8B0000")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    main_character "My head hurts, and where tf is my tp?"

    dude_rational "we should search for it."

    dude_crazy "Fuck that, let's blaze it and down a six pack"
    # This ends the game.

    return
