#List to do for this project:
#1. Try to make the chatbot more complex
#2. Add new comand, such as !help for lists for instruction a user can type to use the Bot.(Done)
#3. If possible, create a HTML page for my Bot.
#4. Add some stuff just for fun (Put something here if you have an idea: )
# Added ci.yml

from client import key, Responses

#Input names 
user_name = str(input("Welcome to C2C Chat Bot system, may I have your first name? "))
chatbot_name  = "C2D2"

print(f"{chatbot_name}: Hi {user_name}, my name is {chatbot_name}, C2C's chatbot. If you confuse of what to ask me, you can type !help  for a list of prompt you can use. If you want to end the chat session, just simply type quit! ")

#The key to end the chat bot
quit = "quit"

#Algorithm that promt the user a question so that my bot can answer. 
user_input = str.lower(input(f"{user_name}: "))

while user_input != quit:
  
  if user_input in key:
    print(chatbot_name + ": " + Responses[user_input])
  
  else:
    print (f"{chatbot_name}: Sorry, I don't understand that")
  
  user_input = str.lower(input(f"{user_name}: "))
