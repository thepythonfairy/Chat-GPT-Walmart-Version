import re
#import spacy
import the_responses as resp

#Test
# nlp = spacy.load('en_core_web_sm')
#doc = nlp("We have ChatGPT at home!")
#print([(token.text, token.ent_type_) for token in doc])

#project needs to be updated for more responses
#will do eventually....


def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
             
    #Calculate the percent of recognized words in a user message
    percentage = float(message_certainty) / float(len(recognized_words))
    
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break


    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    

def check_all_messages(message):
    highest_prob_list = {}


    def response(bot_response, list_of_words, single_response=False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
        

    #First part is what the computer will respond to any of the given instances
    response('Hello!', ['hello', 'hi', 'hey', 'hola', 'wassupi'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words = ['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('As do I! Oh wait you did not hear that!', ['i', 'love', 'coding', 'everyday'], required_words=['coding', 'everyday'])


    response(resp.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(resp.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
       
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)
    #return best_match

    return resp.unknown() if highest_prob_list[best_match] < 1 else best_match
        


def get_response(user_input):
    #doc = nlp(user_input)
    split_message = re.split(r'\s+|[,:?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


#Testing the response system
while True:
    print('ChatGPT (Walmart Ver.): ' + get_response(input('You: ')))