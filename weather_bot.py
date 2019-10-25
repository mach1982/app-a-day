import pyowm
from fbchat import log, Client
from fbchat.models import *

class WeatherBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        

        #print(w.get_temperature('celsius').get('temp')) # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

        

        new_msg ="What city do waht to get the weather for, ie current weather in London 'London' or  'London,GB'"

        if author_id != self.uid and message_object.text.lower()=='weather': 
               
                
             # You MUST provide a valid API key
                
            msg = Message(new_msg)
            
            self.send( msg , thread_id=thread_id, thread_type=thread_type)
                
        elif message_object.text != new_msg and author_id != self.uid:
            c = u"\u00b0"
            owm = pyowm.OWM('64c45a572899067dd41b4e88a80725a5') 
            observation = owm.weather_at_place(message_object.text)
            w = observation.get_weather()
            weather=Message(f"The Tempature in {message_object.text} is {w.get_temperature('celsius').get('temp')} {c}C and {w.get_status()}")
            self.send( weather , thread_id=thread_id, thread_type=thread_type)



username = input("Facebook user ID or e-mail:")
password = input("Enter in you Facebook Password:")

client = WeatherBot(username , password)
client.listen()