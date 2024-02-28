from users import users


class SocialNetwork:
    instance = None

    @staticmethod
    def get_instance():
        if not SocialNetwork.instance:
            SocialNetwork.instance = SocialNetwork("SocialNetwork")
        return SocialNetwork.instance

    def __init__(self, name):
        if SocialNetwork.instance is not None:
            raise Exception("already exist")
        self.name = name
        self.usersL = []
        SocialNetwork.instance = self
        print("The social network " + name + " was created!")

    def add_user(self, user):
        self.usersL.append(user)

    def remove_user(self, user):
        if user in self.usersL:
            self.usersL.remove(user)

    def sign_up(self, name, password):
        for user in self.usersL:
            if user.name == name:
                return False
        if 4 <= len(password) <= 8:
            user1 = users(name, password)
            user1.set_status()
            self.add_user(user1)
            return user1

    def log_out(self, name):
        for user in self.usersL:
            if user.name == name and user.status:
                user.set_status()
                print(user.name + " disconnected")
                break

    def log_in(self, name, password):
        for user in self.usersL:
            if user.name == name and not user.status and user.password == password:
                user.set_status()
                print(user.name + " connected")
                break

    def __str__(self):
        result = (self.name + " social network:\n")
        for user in self.usersL:
            result += str(user) + "\n"
        return result
