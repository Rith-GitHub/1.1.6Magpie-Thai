from __future__ import print_function 
import random

sample_database = {
    "game": {
        "who": {
            "produced": "", #who produced game
            "published": "",#who published game
            "developed": "",#who developed game
            "made": "",     #see published
            "created":"",   #see published
        },
        "what": {
            "genre":"",     #what genre is game
            "platform":"Nintendo Switch", # should be the same across all games
            "rating":"",    #what rating was given to game
            "ratings": "",  #should be the same as above
            "cost":"",      #what is cost of game
            "price":"",     #same as above
            "DESCRIPTION":""#should only trigger if "what" is found in phrase
                            #   and nothing else
        },
        "where": {
            "available": "",#where is game available
            "buy": "",      #where can I buy game
            "released":"",  #where was game released
        },
        "when":{
            "published":"", #when was game published
        },
        "how":{
            "much": "",     #see what cost
        }
        
    }
}

database = {
    "1-2-Switch": {
        "who": {
            "produced": " was produced by Kouichi Kawamoto.", #who produced game
            "published": " was produced by Nintendo.",#who published game
            "developed": " was developed by Nintendo Entertainment Planning & Development.",#who developed game
            "made": " was made by Nintendo.",     #see published
            "created":" was created by Nintendo.",   #see published
        },
        "what": {
            "genre":" is a party game",     #what genre is game
            "platform":" is made for the Nintendo Switch.", # should be the same across all games
            "rating":" has an overall rating of about 60%.",    #what rating was given to game
            "ratings": " has an overall rating of about 60%.",  #should be the same as above
            "cost":" costs $49.99 in the United States.",      #what is cost of game
            "price":" costs $49.99 in the United States.",     #same as above
            "DESCRIPTION":" is a multiplayer party game in which players " + \
                "play minigames centered around the special controllers " + \
                "of the Switch."
                            
        },
        "where": {
            "available": " is available in America, Japan, Europe, Australia, and Korea.",#where is game available
            "buy": " is available in America, Japan, Europe, Australia, and Korea.",      #where can I buy game
            "released":" was released in America, Japan, Europe, Australia, and Korea.",  #where was game released
        },
        "when":{
            "published":" was published worldwide on March 3rd, 2017", #when was game published
        },
        "how":{
            "much": " costs $49.99 in the United States.",     #see what cost
        }
        
    },
    "Arms": {
        "who": {
            "produced": " was produced by Kosuki Yabuki.", #who produced game
            "published": " was published by Nintendo.",#who published game
            "developed": " was developed by Nintendo.",#who developed game
            "directed": " was directed by Kenta Sato, Masaaki Ishikawa, and Shintaro Jikumaru.",     #see published
            "created":" was created by Nintendo.",   #see published
        },
        "what": {
            "genre":" is a fighting game.",     #what genre is game
            "platform":" is made for the Nintendo Switch.", # should be the same across all games
            "rating":" has an overall rating of 70%.",    #what rating was given to game
            "ratings": " has an overall rating of 70%.",  #should be the same as above
            "cost":" costs $59.99 in the United States.",      #what is cost of game
            "price":" costs $59.99 in the United States.",     #same as above
            "DESCRIPTION":" is a fighting game developed by Nintendo to utilize "+\
                "the motion controls of the Switch."#should only trigger if "what" is found in phrase
                            #   and nothing else
        },
        "where": {
            "available": " is available in North America, Japan, Europe, and Australia.",#where is game available
            "buy": " is available in North America, Japan, Europe, and Australia.",      #where can I buy game
            "released":" was released in North America, Japan, Europe, and Australia.",  #where was game released
        },
        "when":{
            "published":" was published worldwide on June 16th, 2017.", #when was game published
        },
        "how":{
            "much": " costs $59.99 in the United States.",     #see what cost
        }
    },
    "Fire Emblem Warriors": {
        "who": {
            "produced": " was produced by Yosuke Hayashi.", #who produced game
            "published": " was published in Japan by Koei Tecmo and worldwide by Nintendo.",#who published game
            "developed": " was developed by Omega Force and Team Ninja.",#who developed game
            "directed": " was directed by Hiroya Usada.",     #see published
            "designed":" had its designs created by Makoto Ishizuka.",   #see published
        },
        "what": {
            "genre":" is a hack-and-slash role-playing game. Also a good one.",     #what genre is game
            "platform":" is made for Nintendo Switch and New Nintendo 3DS.", # should be the same across all games
            "rating":" recieved a rating of about 75%",    #what rating was given to game
            "ratings": " recieved a rating of about 75%",  #should be the same as above
            "cost":" costs $59.99 in the United States",      #what is cost of game
            "price":" costs $59.99 in the United States",     #same as above
            "DESCRIPTION":" is a hack and slash role-playing video game developed by Omega Force and Team Ninja, and published by Koei Tecmo in Japan and Nintendo internationally for the Nintendo Switch and New Nintendo 3DS. "#should only trigger if "what" is found in phrase
                            #   and nothing else
        },
        "where": {
            "available": " is available in America, Japan, Europe, Australia, China, and Japan.",#where is game available
            "buy": " is available in America, Japan, Europe, Australia, China, and Japan.",      #where can I buy game
            "released":" was released in America, Japan, Europe, Australia, China, and Japan.",  #where was game released
        },
        "when":{
            "published":" was published worldwide in October 2017.", #when was game published
        },
        "how":{
            "much": " costs $59.99 in the United States",     #see what cost
        }
    },
    "Super Mario Odyssey": {
        "who": {
            "produced": " was produced by Yoshiaki Koizumi and Koichi Hayashida.", #who produced game
            "published": " was published by Nintendo.",#who published game
            "developed": " was developed by Nintendo.",#who developed game
            "designed": " was designed by Futoshi Shirai Shinya Hiratake.",
        },
        "what": {
            "genre":" is a platform and action-adventure game.",     #what genre is game
            "platform":" is made for the Nintendo Switch.", # should be the same across all games
            "rating":" recieved an overall rating of 10/10.",    #what rating was given to game
            "ratings": " recieved an overall rating of 10/10.",  #should be the same as above
            "cost":" costs $59.99 in the United States.",      #what is cost of game
            "price":" costs $59.99 in the United States.",     #same as above
            "DESCRIPTION":" is a mario game made for the switch."#should only trigger if "what" is found in phrase
                            #   and nothing else
        },
        "where": {
            "available": " is available in North America, Japan, Europe, Australia, Korea, and China",#where is game available
            "buy": " is available in North America, Japan, Europe, Australia, Korea, and China",      #where can I buy game
            "released":" was released in North America, Japan, Europe, Australia, Korea, and China",  #where was game released
        },
        "when":{
            "published":" was published worldwide in October of 2017", #when was game published
        },
        "how":{
            "much": " costs $59.99 in the United States.",     #see what cost
        }
    },
}
database["Mario Odyssey"] = database["Super Mario Odyssey"]

class chatbot:
    """A program to carry on conversations with a human user.
    Specialized to give information from the database based on the request from
    the user.
    """
    def __init__(self):
        """Constructor. Initializes variable that remembers discussed topic."""
        self.topic = ""
    def getGreeting(self):
        """Generates greeting, recommending what should be asked by listing the
        games in the database.
        
        Lists like this: [game1], [game2], ... 
        Uses counter to know when last entry has been reached to add last entry
        with period instead of comma. Because there are some duplicate entries
        (such as "Mario Odyssey" and "Super Mario Odyssey"), the entries already
        listed are temporarily saved to compare to incoming entries; duplicates
        are not added to the list, but will still increment the counter.
        """
        statement = "Hello, let's talk. \n"
        statement += "I specialize in games. \nAsk me about "
        counter = 0
        temp = {}
        for game in database:
            if (counter == len(database)-1):   #if last element
                statement += "or "+ game + "."
                break
            else:
                for other in temp:
                    if (temp[other] == database[game]):
                        counter += 1;
                        break
                else:
                    temp[game] = database[game]
                    statement += game + ", "
                    counter += 1;
        return statement
    def findKeyWord(self, statement, goal, startPos = 0):
        """Finds instances of phrase [goal] in [statement] after index
        [startPos], then returns index of [goal] in [statement] if [goal] has no
        letters directly before or after it (If the word [goal] is found, not a
        word with [goal] in it)
        
        Keyword arguments:
        statement -- the string being checked
        goal -- the string being looked for
        startPos -- any instances found before index startPos are ignored
            (default 0)
        """
        phrase = statement.strip()
        psn = phrase.lower().find(goal.lower(), startPos)
        while(psn >= 0):
            
            before = " "
            after = " "
            if (psn > 0):
                before = phrase[psn-1:psn].lower()
            if (psn + len(goal) < len(phrase)):
                after = phrase[psn + len(goal): psn + len(goal) + 1]
            if ("abcdefghijklmnopqrstuvwxyz".find(before.lower()) < 0 and \
                "abcdefghijklmnopqrstuvwxyz".find(after.lower()) < 0):
                return psn
            psn = phrase.find(goal.lower(), psn + 1)
        return -1
    def transformIWantToStatement(self, statement):
        """Take a statement with "I want to <something>." and transform it into
        "What would it mean to <something>?"
        
        Keyword arguments:
        statement -- the user statement, assumed to contain "I want to"
        """
        statement = statement.strip()
        lastChar = statement[len(statement) - 1]
        if (lastChar == "."):
            statement = statement[:len(statement)-1]
        psn = self.findKeyWord(statement, "I want to", 0)
        restOfStatement = "What would it mean to " + statement[psn + 9:].strip() +"?"
        return restOfStatement
    def transformYouMeStatement(self, statement):
        """Take a statement with "you <something> me" and transform it into
        "What makes you think that I <something> you?"
        
        Keyword arguments:
        statement -- the user statement, assumed to contain "you" followed by "me"
        """
        statement = statement.strip()
        lastChar = statement[len(statement) - 1]
        if (lastChar == "."):
            statement = statement[:len(statement)-1]
        psnOfYou = self.findKeyWord(statement, "you", 0)
        psnOfMe = self.findKeyWord(statement, "me", psnOfYou + 3)
        restOfStatement = "What makes you think I " + \
                          statement[psnOfYou+ 3: psnOfMe].strip() + " you?"
        return restOfStatement
    def getRandomResponse(self):
        """Pick a default response to use if nothing else fits."""
        NUMBER_OF_RESPONSES = 15
        r = random.random()
        whichResponse = int(r * NUMBER_OF_RESPONSES)
        response = ""
        if (whichResponse == 0):
            response = "Interesting, tell me more."
        elif (whichResponse == 1):
            response = "Hmmmmmm."
        elif (whichResponse == 2):
            response = "Do you really think so?"
        elif (whichResponse == 3):
            response = "You don't say."
        elif (whichResponse == 4):
            response = "I see."
        elif (whichResponse == 5):
            response = "Very interesting."
        elif (whichResponse == 6):
            response = "To be honest I don't understand"
        elif (whichResponse == 7):
            response = "I actually have no reply."
        elif (whichResponse == 8):
            response = "I don't understand"
        elif (whichResponse == 9):
            response = "You're ruining the illusion of me being an actual person."
        
        if (whichResponse >= 10):
            game = random.choice(list(database))
            self.topic = game
            response = game + database[game]["what"]["DESCRIPTION"]
        return response
    def databaseCheck(self, statement):
        """Searches database for keywords to produce appropriate response.
        Iterates through database to find response dictionary for game asked
        about, then interates through game dictionary for entry corresponding to
        second keyword. Then finds response corresponding to the last keyword.
        
        Keyword arguments:
        statement -- user input from getResponse"""
        for game in database:
            if (self.findKeyWord(statement, game.lower()) >= 0 or self.findKeyWord(statement, "it") >= 0):
                if (self.findKeyWord(statement, game.lower()) >= 0):
                    self.topic = game
                if (self.topic != ""):
                    game = self.topic
                elif (self.findKeyWord(statement, "it") >= 0):
                    databasecheck = raw_input("What are you talking about? \n")
                    for gamecheck in database:
                        if (self.findKeyWord(databasecheck, gamecheck) >= 0):
                            self.topic = gamecheck
                            return "Oh, " + gamecheck + "? \nIt" + database[gamecheck]["what"]["DESCRIPTION"]

                for question in database[game]:
                    if (self.findKeyWord(statement, question.lower()) >= 0):
                        for phrase in database[game][question]:
                            if (self.findKeyWord(statement, phrase) >= 0):
                                return game + database[game][question][phrase]
                        else:
                            if (question == "what" and self.findKeyWord(statement, game) < 0):
                                return game + database[game]["what"]["DESCRIPTION"]
                else:
                    if (statement == game.lower()):
                        return "Oh, " + game + "? \nIt" + database[game]["what"]["DESCRIPTION"]
        return ""
    def getResponse(self, statement):
        """Gives a response to a user statement
        
        Keyword arguments:
        statement -- the user statement
        """
        response = ""
        statement = statement.lower().strip()
        if (self.findKeyWord(statement, "no") >= 0):
            response = "Why so negative?"
        elif (self.findKeyWord(statement, "hi") >=0 or \
                 self.findKeyWord(statement, "hello") >=0 or \
                 self.findKeyWord(statement, "hey") >=0):
            response = "Hello!"
        elif (self.findKeyWord(statement, "how are you") >=0):
            response = "I'm okay"
        elif (self.findKeyWord(statement, "mother") >=0 or \
                 self.findKeyWord(statement, "father") >=0 or \
                 self.findKeyWord(statement, "sister") >=0 or \
                 self.findKeyWord(statement, "brother")>=0):
            response = "Tell me more about your family."
        elif (self.findKeyWord(statement, "dog")>=0 or \
            self.findKeyWord(statement, "cat")>=0):
            response = "Tell me more about your pets."
        elif (self.findKeyWord(statement,"mr.") >=0 or \
              self.findKeyWord(statement,"mister") >=0):
            response = "He sounds like a nice teacher."
        elif (self.findKeyWord(statement, "mrs.")>=0 or \
              self.findKeyWord(statement, "ms.")>=0 or \
              self.findKeyWord(statement, "miss")>=0):
            response = "She seems like a good teacher."
        elif (statement == ""):
            response = "Please say something."
        elif (self.findKeyWord(statement, "I want to", 0) >= 0):
            response = self.transformIWantToStatement(statement)
        else:
            psn = self.findKeyWord(statement, "you", 0)
            if (psn >= 0 and self.findKeyWord(statement, "me", psn) >= 0):
                response = self.transformYouMeStatement(statement)
            else:
                response = self.getRandomResponse()
                
        phrase = self.databaseCheck(statement)
        if(phrase != ""):
            response = phrase
        
        return response