class userRepo:
    def __init__(self,uid,email,name,username,dob="") -> None:
        self.uid = uid
        self.email = email
        self.name = name
        self.username = username
        self.dob = dob
        self.friends = []
    
    def get_uid(self):
        return self.uid
    
    def get_email(self):
        return self.email
    
    def get_name(self):
        return self.name
    
    def get_username(self):
        return self.username
    
    def add_freinds(self,friend):
        self.friends.append(friend)


        
    