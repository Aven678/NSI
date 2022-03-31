class RugbyGame:
    def __init__(self, equipe_1, equipe_2):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.score = "0-0"

    def get_score(self):
        return self.score

    def drop(self, equipe):
        scores = self.score.split("-")
        if equipe == self.equipe_1:
            scores[0] = int(scores[0]) + 3

        elif equipe == self.equipe_2:
            scores[1] = int(scores[1]) + 3

        self.set_score(scores)

    def essai(self, equipe):
        scores = self.score.split("-")
        if equipe == self.equipe_1:
            scores[0] = int(scores[0]) + 5

        elif equipe == self.equipe_2:
            scores[1] = int(scores[1]) + 5

        self.set_score(scores)

    def transformation(self, equipe):
        scores = self.score.split("-")
        if equipe == self.equipe_1:
            score = int(scores[0])
            if score // 5 > 0:
                scores[0] = score + 2

        elif equipe == self.equipe_2:
            score = int(scores[1])
            if score // 5 > 0:
                scores[1] = score + 2

        self.set_score(scores)

    def set_score(self, scores):
        new_score = ""
        for score in scores:
            if new_score != "":
                new_score += "-"

            new_score += str(score)

        self.score = new_score