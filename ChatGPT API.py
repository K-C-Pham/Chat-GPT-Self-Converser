
import os
#Program will request your own API key here.
key = input("Please enter your API key: ")
os.environ['OPENAI_API_KEY']=key
#import wandb
from openai import OpenAI
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


#function that calls the first chatgpt api, a helpful assistant

def chatter1(promptinput, i):
    #Debug double messages
    #print("The input for the first bot is: \n" + promptinput)
    #print(f"Inputs received: {i}")
    
    #Prompt for the first chatbot
    gpt_assistant_prompt = "You are a helpful assistant"

    #Function 1 code
    message=[{"role": "assistant", "content": gpt_assistant_prompt}, {"role": "user", "content": promptinput}]
    temperature=0.2
    max_tokens=256
    frequency_penalty=0.0
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = message,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty
    )
    return response


#function that calls the scond chatgpt api, a perpetually confused computer user
def chatter2(promptinput, i):
    #Debug double messages
    #print("The input for the second bot is: \n" + promptinput)
    #print(f"Inputs received: {i}")
    
    #Prompt for the second chatbot
    gpt_assistant_prompt = "You are a perpetually confused, technologically challenged computer user. No matter what solutions are provided to you, you always run into new problems. You must respond to all solutions with a new question."
    
    #Function 2 code
    message=[{"role": "assistant", "content": gpt_assistant_prompt}, {"role": "user", "content": promptinput}]
    temperature=0.2
    max_tokens=256
    frequency_penalty=0.0
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = message,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty
    )
    return response

#Main program
number_of_repetitions =  int(input("How many times would you like the bots to converse? "))
i = 1
gpt_user_prompt = input ("What would you like to be the initial prompt? ") 
while i<= number_of_repetitions:
    print(f"\n\n\n*************ROUND {i}*************\n\n\n")
    if i == 1:
        x=str(chatter1(gpt_user_prompt,i).choices[0].message.content)
    else:
        x=str(chatter1(y,i).choices[0].message.content)
    print("\n\nThe first bot responded with: \n" + x)
    y=str(chatter2(x,i).choices[0].message.content)
    print("\n\nThe second bot responded with: \n" +y)
    i=i+1


