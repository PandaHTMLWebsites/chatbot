import random

class Chatbot:
    def __init__(self, name):
        self.name = name
        self.responses = {}

    def train(self, data):
        for question, answer in data.items():
            self.responses[question] = answer

    def respond(self, question):
        if question in self.responses:
            return self.responses[question]
        else:
            return "I don't know how to answer that."

    def __str__(self):
        return "I am a chatbot named {}.".format(self.name)

if __name__ == "__main__":
    chatbot = Chatbot("Bard")
    chatbot.train({
        "Who is DJ SMOOTH PANDA":"Ok,here is the requested information: He is a 13-year-old DJ and producer from England who has been making music for a year. He has released several tracks on Spotify and Bandcamp, and is active on Twitter with over 90 followers. His music is a mix of genres, including hip hop, house, and electronica. He is known for his catchy beats and energetic live performances. He has performed at several clubs and festivals in England, and is quickly gaining a following. DJ Smooth Panda is a talented young DJ and producer who is sure to make a big impact on the music scene. He is passionate about music and is always looking for new ways to express himself through his art. He is also a kind and down-to-earth person who is always willing to help others.",
        "What songs has DJ SMOOTH PANDA released":"He has released 1 album with 9 songs,and he has released 8 singles. If you go would like to know individual song information ask 'Give me more info on DJ SMOOTH PANDA songs",  
        "Give more info on DJ SMOOTH PANDA songs":"What info would you like? Information on the Album or information on his singles?",        
        "Album":"DJ SMOOTH PANDA", 
        "Singles":"", 
        "How old is DJSP":"", 
        "What school did djsp go to":"I am sorry but as a chatbot i cannot answer that question to protect the privacy", 
        "Who is Steak Youtube":"(born July 31, 2001) also known as steakwads or Snooze, is an American YouTuber who is known for uploading shorts about Roblox facts, and streaming himself doing certain challenges, most challenges being about his subscriber count.", 
         "What is Steak Youtube real name":"klein linton", 
        "What is Steak Youtube Birthday":"July 31st 2001.", 
		"How many years has steak been uploading to youtube?":"", 
         " stop":"Thank you for natta with me. Goodbye!"
    })

    while True:
        question = input("What would you like to ask Bard? ")
        response = chatbot.respond(question)
        print(response)
        if question == "stop":
            break