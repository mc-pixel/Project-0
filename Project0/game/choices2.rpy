label kitchen2_option2:
    show neutral1
    "Fridge opens and you look inside. You just kinda look in there waiting for something to happen. Nothing interesting happens. Better luck next time."
    hide neutral1
    return
label kitchen2_option1:
    show confuse2
    "You carefully peek at dishes from a safe distance. You’re not sure if it should be touched at all, although something tells you that it should be washed and organised."
    r    "Me, me is something. Please wash it...now?"
    hide confuse2
    show sad2
    mc    "No, gotta locate TOILET PAPER first. Dishes can wait, invaluable resource can’t!"
    r    "Was worth the try."
    hide sad2
    return
label kitchen2_option3:
    show neutral2
    "You shuffle through the drawers all around you and they silently judge your futile attempts to locate anything that would prove of any use. Nevertheless, you find a SPOON on the floor. It’s covered in something sticky and smells sweet."
    hide neutral2
    menu:
        "Lick it. It smells nice.":
            show confuse2
            "You look at the spoon in your hand. Cautiously sniff it again."
            r    "No. No, don’t. Please."
            mc    "Why not? It smells nice."
            r    "You don’t bother washing dishes. What tells you floors are better?"
            "Besides, gross, dude."
            hide confuse2
            show sad1
            "You give spoon a lick. Tastes sweet and faintly of vanilla. You don’t die, although a deep sense of shame sets in."
            hide sad1
            return
        "Have some good conscience and don’t.":
            show sad2
            "You give the spoon a thorough stare down. Spoon says nothing in its defence, so with heavy heart you toss it into the sink."
            r    "So, I see your good conscience won? For once?"
            hide sad2
            show neutral1
            mc    "Yes, just this once, no more."
            r    "Dang it."
            "You shrug at your own thoughts and decide that drawers keep their secrets too well for you to discover them and get going."
            hide neutral1
            return
label kitchen2_option4:
    show neutral1
    "You’ve been here before, nothing new appeared since you were gone, so why linger?"
    hide neutral1
    return
label bedroom2_option1:
    show neutral2
    "Laptop is the same. You poke it again."
    hide neutral2
    show confuse2
    r    "Not 69Ass69. I know it for sure."
    hide confuse2
    show sad1
    "You try the said combination. Nothing happens."
    r    "Called it."
    hide sad1
    return
label bedroom2_option2:
    show happy1
    "Bed is so welcoming and comfy. You lie down but never ending urge to find TOILET PAPER makes you jump out and keep moving."
    hide happy1
    return
label other_bedroom2_option1:
    show sad2
    r    "Come on! Do it! Touch them!"
    "I dare you!"
    c    "You speak my language!"
    "Break it! Set it on fire! Nothing matters anymore!"
    hide sad2
    show fear_ex2
    mc    "That’s new…"
    "You shudder as you hear a new part of you chime in with suggestions."
    "Maybe it’s this place that makes it worse…"
    "Also those cheeky drawers keep tempting you."
    "Bad place and bad thoughts…"
    hide fear_ex2
    return
label other_bedroom2_option2:
    show happy2
    "You take a step back and launch yourself forward towards the bright future, filled with pillows, blankets and sweet dreams."
    "You land in a pile of amazing goodness and feel happy."
    hide happy2
    show sad2
    "You have underestimated your quarantine munchies. Bed cracks, apparently one of the leg breaks and you roll down onto the floor."
    r     "....."
    "You silently stand up and pretend nothing happened."
    "Your elbow hurts though."
    hide sad2
    show neutral1
    "You ignore it and repress any feelings of guilt and shame."
    r    "I refuse to comment."
    hide neutral1
    return
label other_bedroom2_option3:
    show neutral1
    r    "Go, go. This room doesn’t do us any favours."
    c    "Stay. Stay."
    hide neutral1
    show fear_ex2
    "STAY."
    mc    "This isn’t right…"
    "You back out of the room and hurriedly close the door to avoid facing what’s in there."
    hide fear_ex2
    return
label bathroom2_option1:
    show neutral1
    r    "Hey, us! Can we shower?"
    mc    "No."
    r    "Why? We stink?"
    hide neutral1
    show sad1
    mc    "Can’t. There’s no toilet paper."
    r    "How does that connect?"
    hide sad1
    show happy1
    mc    "Everything’s connected!"
    "No!"
    r    "Okay, it’s not like I can decide anything here."
    "You manfully turn away from the girly duty of washing yourself. Men can’t meddle with showers while their TOILET PAPER is missing!"
    hide happy1
    return
label bathroom2_option2:
    show neutral1
    "Suspicious lack of TOILET PAPER makes you reconsider any ideas you had about the toilet."
    hide neutral1
    show fear1
    "It wasn’t a toilet joke, I swear."
    mc    "What? Who said that?"
    "Huh? No one."
    hide fear1
    return
label bathroom2_option3:
    show neutral2
    "You deem yourself clean enough. Yes."
    "Although you definitely decide against smelling yourself. You’re sure you smell nice."
    "Nice-smelling you turns away and walks out."
    hide neutral2
    return
label living_room2_option1:
    show confuse2
    "Some odd sentiment tells you that sofa isn’t the best idea, but you consider it anyway."
    r    "I’m the odd sensation. Please, listen."
    mc    "Hm….Should I though?"
    r    "No."
    c    "Maybe?"
    "You mull over the thought some more."
    mc    "Hmmm…."
    hide confuse2
    show neutral2
    r    "No…"
    "You decide that you will not do that."
    r    "Oh, God, thank you."
    hide neutral2
    return
label living_room2_option2:
    show confuse2
    "You give cupboard a long stare."
    "Nothing happens."
    hide confuse2
    show happy2
    "You feel easier."
    hide happy2
    show fear_ex2
    cvm    "Or do you?"
    "You really don’t. You’ve been bluffing this whole time."
    "This little statue insets a deep sense of primordial horror."
    "The ultimate deity to ever exist on the face of Earth is possessing this little statue on your cupboard. Nothing will ever be the same."
    c    "I’m not doing this I swear."
    r    "I know."
    hide fear_ex2
    show happy2
    "Nothing will ever be the same."
    hide happy2
    return
label living_room2_option3:
    show fear2
    "You carefully trace your steps back out of the room."
    "Watch your back and don’t listen to the voices."
    hide fear2
    show fear_ex2
    "Don’t listen to the voices."
    hide fear_ex2
    return
