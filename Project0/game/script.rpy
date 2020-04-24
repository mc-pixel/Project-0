define mc = Character("main",color="#000000")
define r = Character("RaTiOnAl",color="#296d98")
define c  = Character("Crazy",color="#8B0000")
define cvm=Character("Caveman",color="#a52a2a")
default picked_up_spoon=False
default found_icecream=False
default bed_broke=False
default caveman_spawned=False
default living_room_tv=False
default phone=True

image neutral1 = im.Scale("neutral_body1.png", 900, 1200)
image neutral2 = im.Scale("neutral_body2.png", 900, 1200)
image confuse1 = im.Scale("confuse_body1.png", 900, 1200)
image confuse2 = im.Scale("confuse_body2.png", 900, 1200)
image sad1 = im.Scale("sad_body1.png", 900, 1200)
image sad2 = im.Scale("sad_body2.png", 900, 1200)
image happy1 = im.Scale("happy_body1.png", 900, 1200)
image happy2 = im.Scale("happy_body2.png", 900, 1200)
image fear1 = im.Scale("fear_body1.png", 900, 1200)
image fear2 = im.Scale("fear_body2.png", 900, 1200)
image fear_ex1 = im.Scale("fear_extra_body1.png", 900, 1200)
image fear_ex2 = im.Scale("fear_extra_body2.png", 900, 1200)
image bathroom = im.Scale("bathroom.png", 1920, 1080)
image bedroom = im.Scale("bedroom_2.png", 1920, 1080)
image your room = im.Scale("your_bedroom.png", 1920, 1080)
image kitchen = im.Scale("kitchen.png", 1920, 1080)
image living room = im.Scale("living_room.png", 1920, 1080)

label start:
    $ corrupted_bathroom=1
    $ corrupted_kitchen=1
    $ corrupted_living_room=1
    $ corrupted_bedroom=1
    $ corrupted_other_bedroom=1


    scene living_room
    show  sad1




    mc "Oh,unspecified deity in the sky, my head! My eyes, my everything!"
    mc "What happened? Why does everything hurt and who am I again?"
    mc "Oh, well. Question for the future me, now me needs bathroom.Bathroom and coffee. Let's go, me!"
    r "What? Not that easy, huh? Choices, choices, my dear! What did we do yesterday?"
    mc "Shut up, me! We did... something...somewhere...yesterday. See? Easy."
    r "Sure sure, now go find out who's we and if we are hot, I'm dying to know!"

    jump bathroom_intro

    label bathroom_intro:
        scene bathroom
        show neutral1
        call good_ending_check
        if corrupted_bathroom==2:
            jump bathroom_intro2
        elif corrupted_bathroom==3:
            jump bathroom_intro3
        elif corrupted_bathroom ==4:
            jump game_over
        else:
            $corrupted_bathroom=2
        "Small, cozy and somewhat familiar bathroom.You can see a pile of laundry that hasn't been touched in a while, sink with exactly one toothbrush and some sort of flowery smelling soap, small cupboard and a shower. There's also a mirror, that begs to look into it and discover something new about you."

        mc "Okaaaay, here we are! What now?"
        hide neutral1
        jump bathroom

    label bathroom:



            menu:
                "Look into the mirror, who knows what you'll find there. Maybe meaning of life or something...":
                    call bathroom_option1
                    jump bathroom
                "Brush your teeth and wash your face. With your eyes closed,because that mirror is scary. We don't like scary.":
                    call bathroom_option2
                    jump bathroom
                "Cupboard? Cupboard!":
                    call bathroom_option3
                    call good_ending_check
                    jump bathroom
                "No, just no. Let's get out of here.":
                    call bathroom_option4
                    jump living_room_intro
    label living_room_intro:
        scene living_room

        if corrupted_living_room==2:
            jump living_room_intro2

        else:
            $corrupted_living_room=2
            
            "Spacious room with sofa that bears an indentation in the shape of… a human? An exercise bike covered in copious amount of dust and a really cool TV. You see a bunch of cool little memorabilia rested on top of a cupboard."

        jump living_room
    label living_room:
        scene living_room
        menu:
            "Check the TV we deserve a break.":

                call living_room_option1
                call good_ending_check
                jump living_room
            "Souvenirs look cool, also maybe TOILET PAPER?":
                $caveman_spawned=True
                call living_room_option2
                jump living_room
            "Check the sofa? For...something…?":
                jump living_room_option3


            "Living room that nobody lives in. Boring! Let’s go!":
                show sad2
                "Living room looks not that living and that creepy caveman statue is giving you a death stare from the top of the cupboard. You feel unwelcome."
                "You turn around and leave."
                hide sad2

                jump living_room_menu



    label living_room_menu:
        show happy1
        "Hmmmmmm where are we off to then?"
        hide happy1
        menu:
            "Let’s go look in the kitchen.":
                jump kitchen_intro
            "I wonder what is in the bathroom. Wouldn't hurt to check.":
                jump bathroom_intro
            "My bedroom, I wonder what’s there?":
                jump bedroom_intro
            "Some other bedroom, that was once inhabited by some people. I can’t recall the time before the Great Quarantine…":
                jump other_bedroom_intro

    label bedroom_intro:
        show neutral1
        scene your_bedroom
        if corrupted_bedroom==2:
            jump bedroom_intro2
        elif corrupted_bedroom==3:
            jump bedroom_intro3
        elif corrupted_bedroom ==4:
            jump game_over
        else:
            $corrupted_bedroom=2
        "Little messy room with a crowning jewel of a laptop in the middle. Everything looks vaguely familiar, although you struggle to remember anything specific.Maybe, if you look around - you’ll feel better?"
        jump bedroom
        hide neutral1

    label bedroom:

        menu:
            "Laptop? Laptop. Maybe I wrote down something useful that would point you to TOILET PAPER?":
                call bedroom_option1
                jump bedroom

            "That bed and blanket sure looks comfy. Lay down maybe?":
                $found_icecream=True
                call bedroom_option2
                call good_ending_check
                jump bedroom

            "Nope. Looks like a man cave. I don’t want to face the reality.":
                call bedroom_option3
                jump living_room_intro
    label kitchen_intro:
        show neutral 2
        scene kitchen
        if corrupted_kitchen==2:
            jump kitchen_intro2
        elif corrupted_kitchen==3:
            jump kitchen_intro3
        elif corrupted_kitchen==4:
            jump game_over
        else:
            $corrupted_kitchen=2
        "You find yourself in a kitchen, that undoubtedly looks like one. Which is good, we need stability and reassurance, in those troubling times of lack of TOILET PAPER."
        "You notice a sink, filled to brim with dishes, you begin to fear that whatever is in there might bite your hand. There’s a fridge, coffee machine and more drawers filled with...kitchen stuff, you think. "
        hide neutral2
        jump kitchen


    label kitchen:

        menu:
            "Cautiously look at dishes. No touching tho.":
                call kitchen_option1
                jump kitchen

            "Peek in fridge, food is cool.":
                call kitchen_option2

                jump kitchen

            "Check around for TOILET PAPER. We need it.":
                $picked_up_spoon=True
                call kitchen_option3
                call good_ending_check
                jump kitchen

            "Let’s go elsewhere. I sense no luck here.":
                call kitchen_option4
                jump living_room_intro

    label other_bedroom_intro:
        scene bedroom_2
        show neutral1
        if corrupted_other_bedroom==2:
            jump other_bedroom_intro2
        elif corrupted_other_bedroom==3:
            jump other_bedroom_intro3
        elif corrupted_other_bedroom==4:
            jump game_over
        else:
            $corrupted_other_bedroom=2
        show neutral1
        "A room like any other, except more tidy and organised than yours. A big, and I mean really big, maybe like a queen size or something is occupying majority of the room’s space. Two nightstands and a little dresser table can be seen as well. You have few recollections of who the inhabitants were , actually…"
        "Parents…? Yes, parents. They lived here. Too long has passed since the beginning of the Great Quarantine, you struggle to remember...What are parents anyway…?"
        hide neutral1
        jump other_bedroom

    label other_bedroom:

        menu:
            "Examine nightstands, maybe there’s some TOILET PAPER stashed in there? Memory jiggling artifacts also could be useful to, ya know, remember stuff…":
                call other_bedroom_option1
                jump other_bedroom

            "The bed looks comfy. Go jump on it!":
                $bed_broke=True
                call other_bedroom_option2
                jump other_bedroom
            "This room has memories of the past and it’s tidiness unnerves you too much.You decide to leave as soon as possible.":
                call other_bedroom_option3
                jump living_room_intro










    # This ends the game.

    return
