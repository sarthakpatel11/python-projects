import time
from turtle import Screen, tracer
from player import Player
from car_manger import CarManger
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car_manger = CarManger()
score_board = ScoreBoard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manger.create_cars()
    car_manger.move_cars()

    for car in car_manger.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()
            score_board.update_scoreboard()

    if player.level_completed():
        player.reset_turtle()
        car_manger.car_speed_incerement()
        score_board.level_increase()
        score_board.update_scoreboard()


screen.exitonclick()
