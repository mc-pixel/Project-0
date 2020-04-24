label bathroom_intro2:
    if corrupted_bathroom==3:
        jump bathroom_intro3
    else:
        "Same little bathroom, with same lonely toothbrush and toothpaste and flowery soap."
        jump corrupted_bathroom1

label corrupted_bathroom1:

    $corrupted_bathroom=3
    if phone==False:

        menu:
            "Look there’s a shower! Let’s shower, please?":
                call bathroom2_option1
                jump corrupted_bathroom1
            "Don’t even look at the toilet, we ain’t doin’ this.":
                call bathroom2_option2
                jump corrupted_bathroom1
            "We’re cleansed enough, let’s get outta here.":
                call bathroom2_option3
                jump living_room_intro

    else:
        menu:
            "Cupboard? Cupboard!":
                call bathroom_option3
                call good_ending_check
                jump corrupted_bathroom1
            "Look there’s a shower! Let’s shower, please?":
                call bathroom2_option1
                jump corrupted_bathroom1
            "Don’t even look at the toilet, we ain’t doin’ this.":
                call bathroom2_option2
                jump corrupted_bathroom1
            "We’re cleansed enough, let’s get outta here.":
                call bathroom2_option3
                jump living_room_intro

label living_room_intro2:
    if corrupted_living_room==3:
        jump living_room_intro3
    else:

        jump corrupted_living_room
label corrupted_living_room:
    show neutral1
    "You’re back to your den of comfortable sofas with questionable abilities and oddly satisfying soap operas on TV that have indefinite amount  of seasons."
    "You don’t know why you’re back but you can swear that room feels better somehow."
    hide neutral1
    if caveman_spawned==False:
        menu:
            "Check the TV we deserve a break.":

                call living_room_option1
                call good_ending_check
                jump corrupted_living_room

            "Sofa, maybe?":
                call living_room2_option1
                jump corrupted_living_room
            "Souvenirs look cool, also maybe TOILET PAPER?":
                $caveman_spawned=True
                call living_room_option2
                jump corrupted_living_room

            "Slowly back out of this room...And watch your back while you’re at it.":
                call living_room2_option3
                jump corrupted_living_room_menu
    else:
        menu:
            "Check the TV we deserve a break.":

                call living_room_option1
                call good_ending_check
                jump living_room
            "Sofa, maybe?":
                call living_room2_option1
                jump corrupted_living_room
            "Re-examine the cupboard, but something tells you not to.":

                call living_room2_option2
                jump corrupted_living_room

            "Slowly back out of this room...And watch your back while you’re at it.":
                call living_room2_option3
                jump corrupted_living_room_menu

label corrupted_living_room_menu:
    mc"So many rooms. So many choices. Where to go, where to go..."
    $corrupted_living_room=2
    menu:
        "Let’s go look in the kitchen.":
            jump kitchen_intro
        "I wonder what is in the bathroom. Wouldn't hurt to check.":
            jump bathroom_intro
        "My bedroom, I wonder what’s there?":
            jump bedroom_intro
        "Some other bedroom, that was once inhabited by some people. I can’t recall the time before the Great Quarantine…":
            jump other_bedroom_intro



    return
label bedroom_intro2:
    if corrupted_bedroom==3:
        jump bedroom_intro3
    else:
        show sad1
        "You open door and step in. Bed still looks comfy. Slight jab of shame at your man cave is still there."
        hide sad1
        jump corrupted_bedroom1
label corrupted_bedroom1:
    $corrupted_bedroom=3
    if found_icecream ==False:
        menu:
            "Laptop? Laptop. Maybe I wrote down something useful that would point you to TOILET PAPER?":
                call bedroom2_option1
                jump bedroom

            "That bed and blanket sure looks comfy. Lay down maybe?":
                $found_icecream=True
                call bedroom_option2
                call good_ending_check
                jump bedroom

            "Nope. Looks like a man cave. I don’t want to face the reality.":
                call bedroom2_option2
                jump living_room_intro
    else:
        menu:
            "Laptop? Laptop. Maybe I wrote down something useful that would point you to TOILET PAPER?":
                call bedroom2_option1
                jump bedroom

            "Nope. Looks like a man cave. I don’t want to face the reality.":
                call bedroom2_option3
                jump living_room_intro


    return
label kitchen_intro2:
    if corrupted_kitchen==3:
        jump kitchen_intro3
    else:

        jump corrupted_kitchen1
label corrupted_kitchen1:
    show confused1
    "Once more, you find yourself in a kitchen. It seems redundant coming here, although you’re hopeful, that maybe TOILET PAPER manifested itself into  existence. So, you check around again."
    hide confused1
    $corrupted_kitchen=3
    if picked_up_spoon==False:

        menu:
            "Cautiously look at dishes. No touching tho.":
                call kitchen2_option1
                jump kitchen

            "Peek in fridge, food is cool.":
                call kitchen2_option2
                jump kitchen

            "Check around for TOILET PAPER. We need it.":
                $picked_up_spoon=True
                call kitchen2_option3
                call good_ending_check
                jump kitchen

            "Let’s go elsewhere. I sense no luck here.":
                call kitchen2_option4
                jump living_room_intro

    else:
        menu:
            "Cautiously look at dishes. No touching tho.":
                call kitchen2_option1
                jump kitchen

            "Peek in fridge, food is cool.":
                call kitchen2_option2
                jump kitchen



            "Let’s go elsewhere. I sense no luck here.":
                call kitchen2_option4
                jump living_room_intro


label other_bedroom_intro2:
    if corrupted_other_bedroom==3:
        jump other_bedroom_intro3
    else:

        jump corrupted_other_bedroom1
label corrupted_other_bedroom1:
    show sad1

    "We’re back here. Room full of unnerving memories that seem to keep escaping your grasp and closed drawers that unapologetically stay closed, despite your best efforts."
    "You look around and sigh."
    hide sad1

    $corrupted_other_bedroom=3
    if bed_broke==False:
        menu:
            "Examine nightstands, maybe there’s some TOILET PAPER stashed in there? Memory jiggling artifacts also could be useful to, ya know, remember stuff…":
                call other_bedroom2_option1
                jump other_bedroom

            "The bed looks comfy. Go jump on it!":
                $bed_broke=True
                call other_bedroom2_option2
                jump other_bedroom
            "This room has memories of the past and it’s tidiness unnerves you too much.You decide to leave as soon as possible.":
                call other_bedroom2_option3
                jump living_room_intro
    else:
        menu:
            "Examine nightstands, maybe there’s some TOILET PAPER stashed in there? Memory jiggling artifacts also could be useful to, ya know, remember stuff…":
                call other_bedroom2_option1
                jump other_bedroom


            "This room has memories of the past and it’s tidiness unnerves you too much.You decide to leave as soon as possible.":
                call other_bedroom2_option3
                jump living_room_intro

    return

label game_over:
    show confuse1
    mc"How many times have I been here?"
    "How many times have I done this?"
    r "It’s okay just calm down, everything is fine…"
    c "Is it... Is it?"
    hide confuse1
    show fear1
    mc"No, it’s not!"
    "Everything is weird! I have no memories!"
    "No family, no friends!"
    hide fear1
    show fear2
    "And I hear voices! Voices in my head…"
    c"They are all your voice."
    r "They are."
    "They are."
    cvm"They are."
    hide fear2
    show fear_ex2
    mc"Are they?"
    c"You failed your simple quest."
    "Failed."
    "Failed."
    "Failed."
    "Just like everything else in life."
    hide fear_ex2
    show sad2
    "Go curl in the corner and cry."
    "You indeed feel the need to curl up in the ball."
    "You do it."
    "You curl in a ball and stay like this for as long as you can remember."
    hide sad2
