# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define f = Character("Froggie")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene wasteland
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show froggie

    # These display lines of dialogue.

    f"Hello there I am Bill's faithful assistant you may call me Froggie."

    f"Bill is working right now so I came instead. I'm here to tell you that
      my boss will not make burping videos so don't ask."
    
    f"If someone asks for a burping video one more time I'll show him what this frog can do."
    
    menu:
        
        f"Are we clear?"
        "YES":
            jump froggie_good_ending
        "NO":
            jump froggie_scare_ending
    # This ends the game.

    return

label froggie_good_ending:
    
    scene clouds_end
    with dissolve 
    "GOOD"
    
    return
    
label froggie_scare_ending:

    scene screen_error
    with dissolve
    "I WARNED YOU"
    
    return