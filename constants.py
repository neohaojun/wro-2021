BLACK_LEFT = 9
BLACK_RGB_LEFT = [7, 10, 9]
WHITE_LEFT = 100
WHITE_RGB_LEFT = [86, 96, 100]
GREY_LEFT = 24
GREY_RGB_LEFT = [22, 28, 41]
GREEN_LEFT = 0
GREEN_RGB_LEFT = [18, 34, 19]

BLACK_RIGHT = 5
BLACK_RGB_RIGHT = [5, 7, 4]
WHITE_RIGHT = 70
WHITE_RGB_RIGHT = [76, 94, 96]
GREY_RIGHT = 18
GREY_RGB_RIGHT = [19, 25, 23]
GREEN_RIGHT = 0
GREEN_RGB_RIGHT = [15, 31, 10]

# red 98 37 26
# green 31 56 45
# blue 28 43 73
RED_WAITING = [70, 0, 0]
GREEN_WAITING = [0, 45, 33]
BLUE_WAITING = [0, 63, 60]

# red 18 10 6
# green 15 15 15
# blue 9 12 20
RED_PARKED = [10, 0, 10]
GREEN_PARKED = [0, 13, 0]
BLUE_PARKED = [0, 0, 17]
BARRIER = [0, 0, 0]

car_order = []

collected_red_parked = False
collected_green_parked = False
collected_blue_parked = False

red_parked_position = None
green_parked_position = None
blue_parked_position = None

robot_position = None
