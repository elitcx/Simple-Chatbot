import re
import longresponses as long

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_cetainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognized_words:
            message_cetainty += 1
    
    percentage = float(message_cetainty) / float(len(recognized_words))
    percentage *= 100
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
        
    if has_required_words or single_response:
        return int(percentage)
    else :
        return 0
    
def check_all_messages(user_input):
    highest_prob_list = {}
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(user_input, list_of_words, single_response, required_words)
        
    #Response----------
    response('Hello!', ['hello', 'hi', 'hey','yo'], single_response=True)
    response("I'm doing fine, thank you!", ['how', 'are', 'you', 'doing'], required_words=['how'])
    response("Thank you!", ['i', 'love', 'you'], required_words=['love', 'you'])
    response(long.R_EATING, ['you', 'eat', 'like', 'eating'], required_words=['you','eat'])
    
    best_response = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    
    return long.unknown() if highest_prob_list[best_response] < 1 else best_response

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


#Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))