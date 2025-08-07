import random

R_EATING = "I don't like eating anything because I am a bot!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    response = ["Sounds like gibberish? ", 
                              "...", 
                              "Yeah right.", 
                              "I am GPT bruh"][
       random.randrange(4)]
    return response