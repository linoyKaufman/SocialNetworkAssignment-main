class posts:
    def __init__ (self,user,type,info,price,place):
            self.likes = []
            self.comments = []
            self.type = type
            self.info=info
            self.availble=True
            self.price=price
            self.place=place
            self.user=user

    def like(self,user1):
            if not any(user1 == self.likes for users in self.likes):
                    self.likes.append(user1)

    def unlike(self, user1):
        if any(user1 == self.likes for users in self.likes):
            self.likes.remove(user1)

    def comment(self, user1, comm):
            self.comments.append((user1, comm))

    def discount(self,percent,password):
        if self.type=="Sale" and password==self.user.password:
            self.price= self.price * (1 - 0.01 * percent)


    def sold(self,password):
        if self.type=="Sale" and password==self.user.password:
            self.availble=False

    def display (self):
        if self.type == "Image":
            self.availble = False
