from posts import posts


class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.status = False
        self.followers = []
        self.post = []
        self.notifications=[]

    def set_status(self):
        self.status = not self.status

    def follow(self, user1):
        if not any(user1.followers == self for users in user1.followers):
            user1.followers.append(self)
            print(self.name+" started following "+user1.name)

    def unfollow(self, user1):
        if any(user1.followers == self for users in user1.followers):
            user1.followers.remove(self)
            print(self.name+" unfollowed "+user1.name)

    def publish_post(self, type, info,price=None, place=None):
        if not any(self.post.info == info for post in self.post):
            if type == "Text":
                post1 = posts(self,type, info,price,place)
                self.post.append(post1)
                print(self.name+" published a post:")
                print(info)
            if type == "Image":
                post1 = posts(self,type, info,price,place)
                self.post.append(post1)
                print(self.name+" posted a picture")
            if type == "Sale":
                post1 = posts(self,type, info, price, place)
                self.post.append(post1)
                priceS=str(price)
                print(self.name+" posted a product for sale:")
                print("For sale! "+info+", price: "+priceS+", pickup from: "+place)
            if type == "Text" or type == "Image" or type == "Sale":
                for user in self.followers:
                    user.add_notifications(self.name+" has a new post")
            return post1

    def print_notifications(self):
        print(self.name+"'s notifications:")
        for notification in self.notifications:
            print(notification)

    def add_notifications(self,notif):
        self.notifications.append(notif)