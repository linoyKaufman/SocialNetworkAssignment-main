#from posts import posts

class users:
    def __init__ (self, name, password):
        self.name = name
        self.password = password
        self.status=False
        self.following= []
        self.posts = []


    def set_status (self):
        self.status= not self.status

    def follow(self, user):
        if not any (user==self.following for user in self.following):
            self.following.append(user)
    
    def unfollow(self, user):
        if any(user==self.following for user in self.following):
            self.following.remove(user)

