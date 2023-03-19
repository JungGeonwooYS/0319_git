class dsl(object):
    def __init__(self, name):
        self.name = name
    def whois(self):
        if self.name == "soeun":
            print(f"{self.name} is vice president")
        elif self.name == "geonwoo":
            print(f"{self.name} is president")
        elif self.name == "chawon":
            print(f"{self.name} is HongBoKing")
        elif self.name == "chanhyung":
            print(f"{self.name} is StudyKing")
        else:
            print(f"{self.name} 이 누구임?")
