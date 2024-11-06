import os, base64

class SessionStore:
    
    def __init__(self):
        #initialize our data
        #members will be dictionaries 
        self.sessionData = {}

    
    def generateSessionId(self):
        #generate a large random numnber for the session id
        rnum = os.urandom(32)
        rstr = base64.b64encode(rnum).decode("utf-8")
        return rstr
    
        #create a new session ID
    def createSession(self):
        sessionId = self.generateSessionId()
        #add a new session to the session store
        self.sessionData[sessionId] = {}
        return sessionId
    
    def getSession(self, session_id):
        #retrieve an existing session from the session store
        if session_id in self.sessionData:
            #returning dictionary in a dictionary
            #pass by reference, it will make changes if we make changes
            return self.sessionData[session_id]
        else:
            return None
