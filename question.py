class Question:
    def __init__(self, given, answer):
        self.given = given
        self.answer = answer
        self.timesAsked = 0
        self.rating = 0
        self.askedYet = False
        
    def answered(self, correctly):
        self.timesAsked += 1
        if correctly:
            if self.timesAsked > 100:
                self.rating += 1
            else:
                self.rating += 100. / (self.timesAsked + 1)
        else:
            if self.timesAsked > 100:
                self.rating -= 2
            else:
                self.rating -= 200. / self.timesAsked
        if self.rating < 0:
            self.rating = 2.3 


