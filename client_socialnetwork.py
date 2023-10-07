import socialnetwork

class client_socialnetwork(socialnetwork.SocialNetwork): 
    def __init__(self, client):
        self.client = client