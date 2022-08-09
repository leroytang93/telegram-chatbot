from datetime import datetime

def responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hello", "hi", "sup"):
        return "Hey! How's it going?"
    
    if user_message in ("who are you", "who are you?"):
        return "I am here to help you!"
    
    if user_message in ("time", "time?", "*time*"):
        now = datetime.now()
        date_time = now.strftime("it is now %d/%m/%y, %H:%M:%S")
        
        return str(date_time)
    
    else:
        return "I don't understand"