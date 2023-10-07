import socialnetwork

class client_socialnetwork(socialnetwork.Socialnetwork): 
    def __init__(self, client):
        self.client = client