
label bathroom_option1:
    show happy1
    r "Come on! Adventures, mirrors and undiscovered faces!"
    mc "Here we go"
    r "If you say so... what’s that on your face? What is it, oh my god?"
    hide happy1
    show fear_ex2
    mc "What? What is it?"
    r "Oh, wait, that’s just you."
    hide fear_ex2
    show sad2
    mc "...."
    mc "That was such a useful insight, thank you."
    hide sad2
    return
label bathroom_option2:
    show neutral1
    r "Teeth. Brush. Do it stinky, nameless person!"
    hide neutral1
    show confuse1
    mc "I maybe should, but what’s the point? Can’t exactly go anywhere or bless someone with my minty fresh kiss…"
    r "No, your breath stinks and you’ll feel better, go!"
    hide confuse1
    show neutral1
    "Teeth were brushed, breath was… minty-ed. Nothing really changed though, but good on you for being a decent human."
    hide neutral1
    return
label bathroom_option3:
    show neutral1
    "Little cupboard under the sink presented all sorts of exploring mysteries and was calling to you to be…. explored."
    hide neutral1
    menu:
        "Look inside the cupboard, maybe there something cool there, like money or food, or… maybe even toilet paper?":
            show neutral1
            "Little cupboard opened with a creak to reveal it’s fascinating contents - one deodorant and some soap bars covered with dust. You debated for a second using that deodorant but ruled against touching that dusty thing. You close it back,disappointed in the lack of adventures."
            hide neutral1

        "Look under, who knows of all sorts of intriguing items that were conveniently dropped there for us to find?":
            show happy2
            "Your back, knees and everything involved in the grotesque movement of crouching lets you know that it hates you with passion and you mildly regret doing that in the first place. However, your efforts are rewarded - under cupboard in a pile of dust and god knows what else you find a PHONE, which is cool."
            hide happy2
            $phone=True
            show confuse2
            "Although, you can’t seem to recall the password which dims the excitement of such discovery."
            hide confuse2
        "Look around and stare uncomfortably at your toilet...maybe there’s some sort of mystery there, I don’t know…":
            show neutral1
            "You peek around the small cupboard to reveal a toilet, which you could see already anyway, but you couldn’t resist a grotesque energy wasting movement. Toilet was boringly the same, with no Nessies in sight. Boooooring!"
            hide neutral1
    return
label bathroom_option4:
    show neutral1
    "Okay. We don’t like this room anymore. Let’s go! You look one final time at the room and note suspicious lack of  TOILET PAPER, which is going to be a problem in the near future."
    hide neutral1
    show confuse2
    mc"There should be toilet paper, where did it go?"
    "This kingdom won’t last long without its most valuable resource! We can’t
    get more, we’re locked in! Gotta. Find. My. Precious!"
    hide confuse2
    show happy2
    r    "Bro...No."
    mc    "Bro, yes."
    r    "Okay, then we shall do that to restore our peace, I guess?"
    mc    "Yes. Yes. Yes. We need THAT TOILET PAPER!"
    hide happy2
    return

label kitchen_option1:
    scene kitchen
    show neutral2
    "You carefully peek at dishes from a safe distance. You’re not sure if it should be touched at all, although something tells you that it should be washed and organised."
    r    "Me, me is something. Please wash it...now?"
    hide neutral2
    show sad1
    mc    "No, gotta locate TOILET PAPER first. Dishes can wait, invaluable resource can’t!"
    r    "Was worth the try."
    hide sad1
    return
label kitchen_option2:
    show confuse2
    "Fridge opens and you look inside. You just kinda look in there waiting for something to happen. Nothing happens. Better luck next time."
    hide confuse2
    return
label kitchen_option3:
    "You shuffle through the drawers all around you and they silently judge your futile attempts to locate anything that would prove of any use. Nevertheless, you find a SPOON on the floor. It’s covered in something sticky and smells sweet."
    $picked_up_spoon=True
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

label kitchen_option4:
    show sad2
    "Kitchen is dull. Imbedded sense of responsibility and lack of TOILET PAPER in sight makes you upset, so you do the most logical thing and leave."
    hide sad2
    return

label bedroom_option1:
    show confuse2
    "Laptop is new and shiny. You poke a button and it comes back to life."
    "Password:?"
    mc    "Uh, password…"
    r    "Yes, password. Knowing you, maybe 696969?"
    hide confuse2
    show happy1
    "You put in the desired sequence with a childish giggle and press Enter."
    "Incorrect password."
    r    "42069, that’s definitely it."
    hide happy1
    show sad2
    "Incorrect password."
    "What were you hoping for, exactly? You turn away and decide to focus on something else."
    hide sad2
    return
label bedroom_option2:
    show neutral2
    "You look at a bed covered in equal amounts by blankets and some clothes of questionable cleanliness. Still comfy enough to lie down."
    hide neutral2
    show confuse2
    "You lie down and there’s something under you. Empty ICE CREAM pack. Still sticky and you think how long it’s been there and why in the first place…"
    r    "Not surprised. At all."
    hide confuse2
    show sad2
    mc    "Ouch."
    "Shame makes you turn away and pretend there’s something more interesting to do."
    hide sad2
    return
label bedroom_option3:
    show confuse1
    "Nope. You don’t feel better. The room is the same as it’s been before, all those days in Great Quarantine make you question how long it’s actually been."
    hide confuse1
    show sad1
    "Man cave is depressive. You quickly exit the room and close the door behind you, just to be sure you don’t catch a glimpse of it again."
    hide sad1
    return
label other_bedroom_option1:
    show neutral2
    "Two big nightstands, made from nice dark wood reside on each side of the bed, silently judging your financial situation. You know you didn’t pay for those. But who did?"
    "More questions without answers."
    "You see photos in frames, smiling people, having fun together. They all look vaguely familiar, but you prefer not to think about it too much…"
    r    "Uh, not to be a party pooper, but those are your parents."
    mc    "What’s that? Who...is that?"
    r    "Uhm, parents…? No? Nothing?"
    "It’s okay, buddy, a bit more Netflix and you’ll not remember anything, so, don’t worry too much."
    hide neutral2
    show sad2
    mc    "Okay, sure. If you say so…"
    r    "God help me."
    hide sad2
    show happy1
    "Drawers, drawers, a lot of drawers!"
    hide happy1
    menu:
        "Let’s peek inside, who knows, TOILET PAPER maybe?":
            show neutral2
            "Three drawers per night stand is a lot of interesting stuff hiding in there."
            hide neutral2
            show confuse2
            "You try to pull one out eagerly but, as you might have expected, those strangers that inhabited your house locked them. Evil bastards!"
            "You push and pull at them for no avail. Life seems hard."
            r    "Done?"
            "You push and pull at them some more in the hopes that something different happens."
            r    "Sure. You know what? Do it some more!"
            hide confuse2
            show sad1
            "Slightly ashamed, you pull at it some more, except with nearly not as much enthusiasm and childish wonder."
            mc    "Debbie Downer…"
            "You leave the drawers alone and turn your attention elsewhere."
            hide sad1
            return

        "We don’t know these people, let’s be decent again, please?":
            show neutral2
            r    "Decent decision after decent decision. You alright?"
            "Drawers call to you with shined handles, but you must resist."
            "Must….resist…."
            hide neutral2
            return
label other_bedroom_option2:
    show happy2
    "You take a step back and launch yourself forward towards the bright future, filled with pillows, blankets and sweet dreams."
    "You land in a pile of amazing goodness and feel happy."
    hide happy2
    show fear_ex2
    "You have underestimated your quarantine munchies. Bed cracks, apparently one of the leg breaks and you roll down onto the floor."
    r     "....."
    "You silently stand up and pretend nothing happened."
    "Your elbow hurts though."
    hide fear_ex2
    show fear1
    "You ignore it and repress any feelings of guilt and shame."
    r    "I refuse to comment."
    hide fear1
    return
label other_bedroom_option3:
    show neutral2
    "Looking around, there is nothing worth exploring here. Some bedroom of some people you have no memory of, feels wrong to scavenge, so you just leave."
    hide neutral2
    return
label living_room_option1:
    show neutral2
    $living_room_tv=True
    "You pick up the remote and mindlessly click a button, hoping there’s not a password or something. "
    "TV comes back to life with some dubious quality TV show playing."
    "You’re mildly revulsed but you can also see yourself watching that."
    "Mindlessly watching… while…"
    r    "While what?"
    hide neutral2
    show confuse1
    mc    "What? I don’t know."
    r    "Maybe eating?"
    mc    "Ye, like ice cream or something…"
    "I don’t know though…"
    c    "Of course you don’t."
    hide confuse1
    return
label living_room_option2:
    show confuse2

    "You shift your loving but confused gaze towards a cupboard that is covered in memorabilia. Little sea shells, figurines and statuettes."
    "Is... is that a caveman figurine?"
    hide confuse2
    show happy2
    "it is a little caveman figurine. Sweet."
    r    "So, uh, why is that here?"
    mc    "You ask me? I don’t know."
    cvm    "Ye, me neither."
    hide happy2
    show fear_ex2
    mc    "What?"
    cvm    "What?"
    r    "Put it down slowly and don’t think about it."
    cvm    "Ye, don’t think about it."
    "No questions asked."
    hide fear_ex2
    show confuse1
    "You put it down and do your best to ignore it."
    "No TOILET PAPER in sight either."
    "You slowly back off, not letting your gaze escape the little caveman, in case something else happens."
    cvm    "Wait a sec, I didn’t get this last thingie. Do you mind repeating that?"
    hide confuse1
    show fear1
    "You shudder from unexplainable horror and do your best to ignore."
    hide fear1
    return

label living_room_option4:
    show neutral1
    "Living room looks not that living and that creepy caveman statue is giving you a death stare from the top of the cupboard. You feel unwelcome."
    "You turn around and leave."
    hide neutral1
    return
label break_game:
    show neutral1
    "This sofa is kinda sketchy. Are you sure you want to sit on it?"
    hide neutal1
    menu:
        "Sure why not. Whats the worst thing that could happen?":
            return
        "Nah on second thought this might not be the best idea":
            show happy2
            "Good call fam"
            hide happy2
            jump living_room

label living_room_option3:
    show happy1
    "Sofa looks surprisingly welcoming."
    r    "No, it doesn’t."
    mc    "Yes, it does."
    r    "This is gonna break if you do it."
    "No, it won’t"
    r    "Yes, it will"
    call break_game
    mc    "Eh, let’s do this anyway."
    r    "Oh, here we go."
    hide happy1

    return
