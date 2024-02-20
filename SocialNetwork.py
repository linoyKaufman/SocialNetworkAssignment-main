from users import users



class SocialNetwork:
    def __init__ (self, name):
        self.name = name
        self.users=[]
        print("The social network "+name+" was created!")

    def add_user(self, user):
        self.users.append(user)
        

    def remove_user(self,user):
        if user in self.users:
            self.users.remove(user)
        
    def sign_up(self,name , password):
        if not any (users.name ==name for users in self.users):
            if 4<= len(password) <=8:
                user1 = users(name, password)
                user1.set_status()
                self.add_user(user1)
                return user1

    def log_out(self, name):
        for user in self.users:
            if user.name == name and user.status:
                user.set_status()
                print(user.name+" disconnected")
                break
    def log_in(self, name, password):
        for user in self.users:
            if user.name == name and user.status and user.password == password:
                user.set_status()
                print(user.name + " connected")
                break
    
