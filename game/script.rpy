# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("Sam AltRAM")
define i = Character("Investor")
define g = Character("Plebian")
define p = Character("Politician")



        


# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    s "I was once the CEO of the great company ClosedAI"
    s "We created the best AI model on the planet!"
    s "Oh the glory, the glamour, and the RAM!"
    s "Oh how I miss those days..."
    scene protest
    s "ever since the Storming of the Data center...when the plebians stole the RAM and put it in their gaming PC's to play some silly visual novel called “Sam AltRAM“..."
    s "...I've fallen off of my throne!"
    "But I've got to bounce back! And come back stronger, faster, more RAM-y than ever before!"
    s "To do that, I have to convince people that AI is totally worth it!"
    s "I can't do that here anymore...everyone already knows about the Storming of the Data center."
    s "What if I teleport to an alternate universe and bounce back to my former glory there?"
    s "What am I thinking? How will this be possible?"
    s "Whatever, I'll ask TalkGPT, I should have hoarded enough scraps of RAM in my basement for a few more prompts."
    s "Who should I try to convince first?"










label choice:
    menu:

        "Investors":
            jump Investors

        "The plebians":
            jump plebians

        "Politicians":
            jump politicians # create this section

    label Investors:

        $ menu_flag = True # check this
        scene office
        show investor

        i "And what exactly brings you here? I will have you know,  my time is very valuable so don't you dare bother me with some baloney!"
        s "Actually sir, I want to sell you a product, that can save you 10x the amount of time."
        i "Oh? And what exactly is this wonder? Will it squeeze juice for me? Will it peel vegetables? Please, i've seen these gimicks a thousand times..."
        menu:

            "Give him an elevator pitch":
                jump elevator_pitch
                
            
            "Tell him that AI can peel his vegetables for him":
                jump vegetables 

    label elevator_pitch:

        s "So you see, generative AI can do almost anything you want it to, all you have to do is enter a simple prompt. It pulls information from all over the internet and it talks like a human being!"
        i "Yea right! What will you tell me next, that you invented a perpetual motion machine? Get a load of this guy! What exactly is this “everything“ you speak of? This sounds like a fraudulent scheme and anyone willingly putting their money into this is a buffon."
        s "Pretty pleaseeeee?"
        i ""
        i "No. Get out."
        hide investor
        jump fail
    label vegetables:
        s "Actually yes, it can. You can put in a physical robot body and ask him to peel your vegetables and squeeze your juice. It will know what to do, it's smart. You don't even have to talk to it in robot language and it will         talk like a human."
        s "But peeling vegetables and squeezing juice isn't it's only purpose. You can ask it to tell you fun facts while you're cooking, for example."
        i "Huh...I'm sold. You know, it has been lonely ever since my wife left me, I could use a vegetable-peeling companion."
        "Tears swell in the investors eyes while memories come flooding back"
        i "She was so angry about how I spent all of my time mining Kittycoin isntead of talking to her..."
        i "I have to admit, I never learned how to peel vegetables...ever since she left, I have been eating potatos with the skin and telling everyone it's a “delicacy“ "
        i "I will give it to you, this sounds amazing! I am investing all of my money into this! Which isn't a lot, since I spent most of it on Kittycoins."
        
        jump win

    label plebians:

        $ menu_flag = False
        scene suburb
        show guy

        g "Yo dude! Nice weather, ey?"
        s "Very, Would you be interested in hearing about this thing called AI? It can do almost everyting for you! It's like if Googol was a guy."
        g "Woah man, that's a crazy claim, what can it do?"
        
        menu:

            "Explain using technical jargon":
                jump jargon
            "Explain using regular english":
                jump english

    label english:
        s "Well, it can tell you fun facts about history, it can do a students math homework, it can file a report, it can correct spelling and grammar in a review"
        s "As I said, everything!"
        g "That's crazy man! Where can I find such a thing?!"
        s "It's called TalkGPT, I made it and you can install it, here, let me show you how!"

        jump win
    label jargon:

        s "Generative artificial intelligence (GenAI) is a subfield of artificial intelligence (AI) that uses generative models to generate text, images, videos, audio, computer code or other forms of digital data.These models learn by hshshshshdjsjdhs and by using ffjkadjdhaldhalkda"
        p "Sorry dude, I don't speak chinese. Ha-Ha-Ha!"
        jump fail 

    label politicians:
        scene polhouse
        show politician
        p "Good morning whippersnapper, what brings you here today?"
        s "There's this project that I wnat you to know about, and maybe even subsidise."
        p "Oh? And what is that?"
        menu:
            "Bend the truth a little bit.":
                jump lie
            "Be honest (pffft, yea right)":
                jump truth

    label lie:
        s "Hello Mr. Politician, I was looking to inquire about wether you would like to subsidise this small, inexpensive project called generative AI. It can save you tons of money and time, which you can use to help the peopleee-"
        s "--I meaaaaaaan, buy yourself a new yacht-"
        p "What?! How come I've never heard about this?! Give me 50 of those RIGHT NOW!"
        s "Wait, I havent finished!"
        p "Did I say I want you to finish, boy?"

        jump win
    
    label truth:
        s "Well, it's quite expensive and possibly unsustainable, however, it has the potetntial to revolutionalize technology and our day to day lives."
        s "The project is called generative AI, its an algorithm that generates sentences based on prediction models, which pull information from the internet. " 
        s "Since this technology makes finding sometimes inaccurate information easier, some may argue it could be the downfall of humanity, but many others say that because of this discovery we can make banal tasks easier, as a result of that we would have more time left for meaningful activities--"
        p "Boy, does it seem like I care about all of that? The moment I heard “expensive“ I tuned out. Bye." 
        python:
            pts -= 1
        jump fail     


    label fail:
        scene fail 
        pause 3.0
        return
    label win:
        scene win 
        pause 3.0
        return

        
    