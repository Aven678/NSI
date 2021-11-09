class File:
    def __init__(self):
        self.data = []

    def est_vide(self):
        return len(self.data) == 0

    def enfile(self, x):
        self.data.append(x)

    def defile(self):
        if self.est_vide() == True:
            raise IndexError("Vous avez essayé de vider une file vide.")
        return self.data.pop(0)

    def __str__(self) -> str:
        if self.est_vide() == True:
            return "None"

        text = "|"
        for i in self.data:
            text += str(i)+"|"

        return text