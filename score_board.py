from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("rosy brown")
        self.penup()  #Makes it so there is no line
        self.goto(0, 270)   #make it go to the top of the screen
        self.hideturtle()   #hides the click mark
        self.update_score()

    def update_score(self):  #This ensures that a new score will present itself when food is eaten.
        self.clear()
        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", align="center", font=('Ariel', 24, 'normal'))

    # def game_over(self):  #when game is over, it will be printed in Center of screen
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align="center", font=('Ariel', 48, 'normal'))

    def reset_scoreboard(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):  #when food is eaten, increase the score by 1 and also clear the screen
        self.score += 1
        self.update_score()
