label bathroom_intro3:
    if corrupted_bathroom==4:
        jump game_over
    else:
        show confuse1
        "Bathroom looks smallfully suffocating this time. You don’t know why you ended here again."
        hide confuse1
        show confuse2
        "You were sure that you decided you don’t really need anything here, yet here you are"
        hide confuse2
        show fear2
        "Feels odd and unsettling. Like you’re in SIMmS or something…"
        hide fear2
        jump corrupted_bathroom2

label corrupted_bathroom2:
    $corrupted_bathroom=4
    if phone==False:
        menu:
            "Check we’re not in SIMmS or some other game…":
                call bathroom3_option1
                jump corrupted_bathroom2
            "Cupboard? Cupboard!":
                call bathroom_option3
                call good_ending_check
                jump bathroom
            "Just get out and defy that deity up above!":
                call bathroom3_option2
                jump living_room_intro

    else:
        menu:
            "Check we’re not in SIMmS or some other game…":
                call bathroom3_option1
                jump corrupted_bathroom2

            "Just get out and defy that deity up above!":
                call bathroom3_option2
                jump living_room_intro




label bedroom_intro3:
    if corrupted_bedroom==4:
        jump game_over
    else:
        show fear2
        "Unsettling feeling. You have been here before. Not once. Bed no longer looks welcoming, more like a Black Hole that won’t ever let you go. Laptop is the next Terminator.Run, John Konnor, RUN!"
        hide fear2
        jump corrupted_bedroom2
label corrupted_bedroom2:

    $corrupted_bedroom=4
    show confuse1
    "Unsettling feeling. You have been here before. Not once. Bed no longer looks welcoming, more like a Black Hole that won’t ever let you go. Laptop is the next Terminator.Run, John Konnor, RUN!"
    hide confuse1
    show fear2
    r "Breathe. Please breathe."
    "Everything is going to be ok, just calm down."
    mc"Is it, is it okay?"
    "Nothing is okay, I’m here again!"
    r"Quarantine isn’t helping I know, but please calm down. We live here, everything is
    Okay, we only so many rooms we can go in."
    c"Keep telling yourself that, of course."
    "Only so many rooms…"
    "Only so many days inside…"
    "So many reasons to keep doing the same thing over and over again…"
    hide fear2
    show fear_ex2
    mc"I need to get out here, get out, get out, get out!"
    "Panic starts digging its way up from the depths of your mind, you can feel it coming in waves, each next worse than the previous. You have to get out of this room, maybe THEY want to get you out of the room? You don’t know anymore."
    hide fear_ex2

    jump living_room_intro
label kitchen_intro3:
    if corrupted_kitchen==4:
        jump game_over
    else:
        show fear1
        "Kitchen? Why kitchen? Oh, God, why kitchen? You’ve been here! Why again?"
        hide fear1
        show fear_ex2
        "Deep sense of unease sets in, you feel paranoid and worried, as if there’s someone else watching over you, seeing every move and as if influencing you…"
        "You slowly breathe in and out...Surely, there can’t be anyone there. Nobody is allowed out, so maybe it’s just you…?"
        hide fear_ex2

        jump corrupted_kitchen2
label corrupted_kitchen2:
    $corrupted_kitchen=4
    if picked_up_spoon==False:
        menu:
            "Check around for TOILET PAPER. We need it.":
                $picked_up_spoon=True
                call kitchen3_option1
                call good_ending_check
                jump corrupted_kitchen2
    else:
        show sad1
        "There’s nothing new. There is never anything new, it’s all the same yet YOU are expecting something else."
        hide sad1
        show sad2
        r "It’s okay, it’s okay, just don’t worry."
        c"Huh, nothing is OKAY! Never was, never will be!"
        hide sad2
        show fear2
        mc"I should go, I should go somewhere else. I can’t be here."
        "We need to go, we need to go, we need to go.."
        "There’s nothing new. There is never anything new, it’s all the same yet YOU are expecting something else."
        r "It’s okay, it’s okay, just don’t worry."
        hide fear2
        show fear_ex2
        c"Huh, nothing is OKAY! Never was, never will be!"
        mc"I should go, I should go somewhere else. I can’t be here."
        hide fear_ex2
        menu:

            "We need to go, we need to go, we need to go..":
                jump living_room_intro


label other_bedroom_intro3:
    if corrupted_other_bedroom==4:
        jump game_over
    else:
        show confuse2
        "You’re here once more. The door opened and closed behind you without you remembering any of it."
        hide confuse2
        show fear2
        "The voice inside your head starts whispering but you can’t tell apart the words…"
        hide fear2
        show fear_ex2
        "The room closes in more and more, it’s hard to breathe…"
        hide fear_ex2


        jump corrupted_other_bedroom2
label corrupted_other_bedroom2:

    $corrupted_other_bedroom=4
    menu:
        "LEAVE!":
            jump living_room_intro
        "LEAVE NOW":
            jump living_room_intro
        "GO AND DON’T LOOK BACK":
            jump living_room_intro
