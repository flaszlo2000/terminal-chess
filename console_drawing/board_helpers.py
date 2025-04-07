def get_board_width(square_height: int) -> int:
    return (square_height * 2 + 1) * 8 + 9

def get_board_height(square_height: int) -> int:
    return square_height * 8 + 9 # +9 = dividers between squares

# d---d---d---d---d---d---d---d---d  ==> 9 dividers
# | R | N | B | Q | K | B | N | R |
# d---d---d---d---d---d---d---d---d
# | P | P | P | P | P | P | P | P |
# d---+---+---+---+---+---+---+---|
# |   |   |   |   |   |   |   |   |
# d---+---+---+---+---+---+---+---|
# |   |   |   |   |   |   |   |   |
# d---+---+---+---+---+---+---+---|
# |   |   |   |   |   |   |   |   |
# d---+---+---+---+---+---+---+---|
# |   |   |   |   |   |   |   |   |
# d---+---+---+---+---+---+---+---|
# | P | P | P | P | P | P | P | P |
# d---+---+---+---+---+---+---+---|
# | R | N | B | Q | K | B | N | R |
# d--------------------------------
#
# |
# V
# 9 dividers
#
# --------------------------------------
#
# SQUARE_HEIGHT == 1
# get_board_width() => 
# --- =  SQUARE_HEIGHT * 2 + 1 == 3
#
# (3) * 8 + 9 where 8 is the square count so we will have the following
# C = COUNTED, N = NOT COUNTED, the spaces are only for visual purposes
#
# N CCC N CCC N CCC N CCC N CCC N CCC N CCC N CCC N  => 9 not counted dividers, hence + 9
#