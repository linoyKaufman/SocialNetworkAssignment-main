from users import users


class SocialNetwork:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.usersL = []
        return cls._instance

    def __init__(self, name):
        self.name = name
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
