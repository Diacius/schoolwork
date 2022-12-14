class person():
    def __init__(self, name):
        self.mark = []
        self.total = 0
        for i in range(5):
            a = int(input(f"Enter mark for {name}"))
            self.mark.append(a)
            self.total = self.total + a
        self.avg = self.total / len(self.mark)
        print(self.avg)
student1 = person("Brayden")