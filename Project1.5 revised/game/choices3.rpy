label kitchen3_option1: #if you picked the spoon on kitchen 1 skip
"You shuffle through the drawers all around you and they silently judge your futile attempts to locate anything that would prove of any use. Nevertheless, you find a SPOON on the floor. It’s covered in something sticky and smells sweet."
menu:
    "Lick it. It smells nice.":
        show confuse2
        "You look at the spoon in your hand. Cautiously sniff it again."
        r    "No. No, don’t. Please."
        mc    "Why not? It smells nice."
        r    "You don’t bother washing dishes. What tells you floors are better?"
        "Besides, gross, dude."
        hide confuse2
        show sad2
        "You give spoon a lick. Tastes sweet and faintly of vanilla. You don’t die, although a deep sense of shame sets in."
        hide sad2
        return
    "Have some good conscience and don’t.":
        show confuse2
        "You give the spoon a thorough stare down. Spoon says nothing in its defence, so with heavy heart you toss it into the sink."
        r    "So, I see your good conscience won? For once?"
        mc    "Yes, just this once, no more."
        r    "Dang it."
        hide confuse2
        show neutral1
        "You shrug at your own thoughts and decide that drawers keep their secrets too well for you to discover them and get going."
        hide neutral1
        return
label bedroom3_option2:
    return
label other_bedroom3_option1:
    return
label other_bedroom3_option2:
    return
label other_bedroom3_option3:
    return
label bathroom3_option1:
    show confuse1
    "You look up, no weird thing floating above your head. "
    hide confuse1
    show neutral1
    "Huh, maybe we’re good. You decide to decide something."
    r    "Maybe shower?"
    mc    "Nope."
    "Ah, good, you can still decide stuff. You calm down a bit."
    hide neutral1
    show confuse1
    c    "Who told you to calm down though?"
    mc    "What?"
    r    "What?"
    "What?"
    hide confuse1
    return
label bathroom3_option2:
    show neutral1
    "You took a swift step outside."
    "Yet were still in the room."
    hide neutral1
    show confuse1
    "Weird."
    c    "Cool, isn’t it?"
    mc    "So, I talk, I talk and I talk?"
    r    "Yep."
    c    "Yep."
    "Maybe."
    hide confuse1
    show confuse2
    "Anyhow, you’re outside now."
    "Slightly confused, but outside."
    hide confuse2
    return
label good_ending_check:

    if picked_up_spoon == True and found_icecream==True and living_room_tv==True and phone==True:
        jump good_ending
    else:
        return
label good_ending:
        scene kitchen
        show neutral2

        "The whisper of a memory nugs at your brain. A tiny remnant of what once was and is no more. You ignore it at first, yet the pull gets stronger"
        "Finally, you choose to focus on it. Suddenly everything becomes clear"
        hide neutral2
        show confuse2
        mc"Could it really be?"
        "You hastily make your way to the fridge"
        "Your memory jiggles a bit and you suddenly realise - SPOON, ICE CREAM and NETFLIX, followed by the phone equals to another night in your house during Great Quarantine, where you sit and do nothing. ICE CREAM is from freezer. Freezer…Freezer!"
        hide confuse2
        menu:
            "LOOK IN THE FREEZER. NOW!":
                show confuse2
                "You open the freezer, almost breaking the door. There it is, your precious roll of TOILET PAPER. Life is good. Everything is fine. You feel at peace"
                hide confuse2
                show happy2
                "Finally. Thank God, finally. Can we go back to Netflix now? This has been too much."
                "Congratulations! You have beat the game!"
                hide happy2
                $renpy.quit()
                return
#livingroom none 3rd
#bathroom done
#other bedroom done
#bedroom 3rd time no options
#kitchen done
