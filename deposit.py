from pybricks.parameters import Color
from pybricks.tools import wait
from devices import *
from pid import *
from constants import *


def deposit_waiting(motor: Motor, angle: int):

    base.reset_angle()

    if motor is left_intake:
        line_track.rgb_move(
            right_color_sensor,
            500,
            [
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ],
            -1,
            lambda: base.angle() < 75,
            200,
            False,
        )
        base.brake()
        sensor = left_color_sensor

        def update_intake_posessions(
            car_color=None,
            car_type=None,
            number_of_batteries=None,
        ):
            intake.update_left_possessions(car_color, car_type, number_of_batteries)

        number_of_batteries = intake.left_batteries

        black_value = BLACK_RGB_LEFT
        white_value = WHITE_RGB_LEFT
        grey_value = GREY_RGB_LEFT
    elif motor is right_intake:
        base.brake()
        sensor = right_color_sensor

        def update_intake_posessions(
            car_color=None,
            car_type=None,
            number_of_batteries=None,
        ):
            intake.update_right_possessions(car_color, car_type, number_of_batteries)

        number_of_batteries = intake.right_batteries

        black_value = BLACK_RGB_RIGHT
        white_value = WHITE_RGB_RIGHT
        grey_value = GREY_RGB_RIGHT

    gyro_turn.turn(angle)
    base.brake()

    intake.open(motor)

    gyro_straight.move(-1400, angle, lambda: sensor.rgb()[0] > (black_value[0] + 5))
    gyro_straight.move(
        -1400, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5), False
    )
    gyro_straight.move(
        -1400, angle, lambda: sensor.rgb()[0] > (grey_value[0] + 5), False
    )

    if number_of_batteries == 1:
        wait(150)

    base.brake()

    wait(100)
    gyro_straight.move(800, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5))
    gyro_straight.move(
        800, angle, lambda: sensor.rgb()[0] > (black_value[0] + 5), False
    )
    gyro_straight.move(
        500, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5), False
    )

    if number_of_batteries == 2:
        base.hold()
        ev3.speaker.beep()
        intake.close(motor)
        wait(500)

    gyro_straight.move(800, angle, lambda: sensor.rgb()[0] > (grey_value[0] + 5), False)
    base.hold()
    if number_of_batteries == 1:
        base.run_target(-800, 800, -160, 160)
    else:
        base.run_target(-800, 800, -150, 150)

    intake.hold()
    update_intake_posessions(None, None, number_of_batteries - 1)


def deposit_waiting_without_battery(motor: Motor, angle: int):
    base.reset_angle()

    if motor is left_intake:
        line_track.rgb_move(
            right_color_sensor,
            500,
            [
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ],
            -1,
            lambda: base.angle() < 75,
            200,
            False,
        )
        base.brake()
        sensor = left_color_sensor

        def update_intake_posessions(
            car_color=None,
            car_type=None,
            number_of_batteries=None,
        ):
            intake.update_left_possessions(car_color, car_type, number_of_batteries)

        number_of_batteries = intake.left_batteries

        black_value = BLACK_RGB_LEFT
        white_value = WHITE_RGB_LEFT
        grey_value = GREY_RGB_LEFT
    elif motor is right_intake:
        line_track.rgb_move(
            right_color_sensor,
            500,
            [
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ],
            -1,
            lambda: base.angle() < 5,
            False,
        )
        base.brake()
        sensor = right_color_sensor

        def update_intake_posessions(
            car_color=None,
            car_type=None,
            number_of_batteries=None,
        ):
            intake.update_right_possessions(car_color, car_type, number_of_batteries)

        number_of_batteries = intake.right_batteries

        black_value = BLACK_RGB_RIGHT
        white_value = WHITE_RGB_RIGHT
        grey_value = GREY_RGB_RIGHT

    gyro_turn.turn(angle)
    base.brake()

    intake.open(motor)

    gyro_straight.move(-1400, angle, lambda: sensor.rgb()[0] > (black_value[0] + 5))
    gyro_straight.move(
        -1400, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5), False
    )
    gyro_straight.move(
        -500, angle, lambda: sensor.rgb()[0] > (grey_value[0] + 5), False
    )
    base.brake()
    wait(100)
    update_intake_posessions(None, None)
    gyro_straight.move(300, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5))
    if number_of_batteries == 2:
        base.brake()
        intake.close(motor)
        wait(500)
    elif number_of_batteries == 1:
        gyro_straight.move(
            800, angle, lambda: sensor.rgb()[0] > (black_value[0] + 5), False
        )
        ev3.speaker.beep()
        base.brake()
        intake.close(motor)
        wait(500)
    gyro_straight.move(
        800, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5), False
    )
    gyro_straight.move(800, angle, lambda: sensor.rgb()[0] > (grey_value[0] + 5), False)

    base.hold()
    base.run_target(-800, 800, -150, 150)

    intake.hold()


def collect_parked(motor: Motor, angle: int, car_color: Color):

    base.reset_angle()

    if motor is left_intake:
        line_track.rgb_move(
            right_color_sensor,
            500,
            [
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ],
            -1,
            lambda: base.angle() < 80,
            False,
        )
        base.brake()
        sensor = left_color_sensor

        def update_intake_posessions(
            car_color=None,
            car_type=None,
            number_of_batteries=None,
        ):
            intake.update_left_possessions(car_color, car_type, number_of_batteries)

        black_value = BLACK_RGB_LEFT
        white_value = WHITE_RGB_LEFT
        grey_value = GREY_RGB_LEFT
    elif motor is right_intake:
        line_track.rgb_move(
            right_color_sensor,
            500,
            [
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
                ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ],
            -1,
            lambda: base.angle() < 7,
            False,
        )
        sensor = right_color_sensor

        def update_intake_posessions(
            car_color=None,
            car_type=None,
            number_of_batteries=None,
        ):
            intake.update_right_possessions(car_color, car_type, number_of_batteries)

        black_value = BLACK_RGB_RIGHT
        white_value = WHITE_RGB_RIGHT
        grey_value = GREY_RGB_RIGHT

    gyro_turn.turn(angle)

    intake.open(motor)

    gyro_straight.move(-1400, angle, lambda: sensor.rgb()[0] > (black_value[0] + 5))
    gyro_straight.move(
        -1400, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5), False
    )
    base.brake()
    intake.close(motor)
    wait(400)
    update_intake_posessions(car_color, 1)

    gyro_straight.move(800, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5))
    gyro_straight.move(
        800, angle, lambda: sensor.rgb()[0] > (black_value[0] + 5), False
    )
    gyro_straight.move(
        800, angle, lambda: sensor.rgb()[0] < (white_value[0] - 5), False
    )
    gyro_straight.move(800, angle, lambda: sensor.rgb()[0] > (grey_value[0] + 5), False)
    base.hold()

    base.run_target(-800, 800, -150, 150)

    intake.hold()
