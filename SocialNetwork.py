from users import users


class SocialNetwork:
    def __init__ (self, name):
        self.name = name
        self.users=[]

    def add_user(self, user):
        self.users.append(user)
        

    def remove_user(self,user):
        if user in self.users:
            self.users.remove(user)
        
    def sign_up(self,name , password):
        if not any (users.name ==name for users in self.users):
            if 4<= len(password) <=8:
                user = users(name, password)
                user.set_status()
                self.add_user(user)
                return user
            
    def log_out (self,name):
        for users in self.users:
            if self.users.name == name and self.users.status:
                users.set_status()


    def log_in (self, name, password):
        for users in self.users:
            if self.users.name == name and self.users.status and self.users.password== password:
                users.set_status()
    
