from posts import posts


class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.status = False
        self.following = []
        self.post = []
        self.notifications=[]

    def set_status(self):
        self.status = not self.status

    def follow(self, user1):
        if not any(user1 == self.following for users in self.following):
            self.following.append(user1)

    def unfollow(self, user1):
        if any(user1 == self.following for users in self.following):
            self.following.remove(user1)

    def publish_post(self, type, info,price=None, place=None):
        if not any(self.post.info == info for post in self.post):
            if type == "Text" or type == "Image":
                post1 = posts(self,type, info,price,place)
                self.post.append(post1)
            if type == "Sale":
                post1 = posts(self,type, info, price, place)
                self.post.append(post1)
            if type == "Text" or type == "Image" or type == "Sale":
                for user in self.following:
                    user.add_notifications(self.name+" posted "+type)
            return post1

    def print_notifications(self):
        for notification in self.notifications:
            print(notification)

    def add_notifications(self,notif):
        self.notifications.append(notif)