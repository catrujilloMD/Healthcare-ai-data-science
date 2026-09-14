"""Refactored solution for the Reeborg's World maze project.

This program runs inside Reeborg's World. Functions such as move(),
turn_left(), front_is_clear(), right_is_clear(), and at_goal() are
provided by the Reeborg environment.
"""


def turn_right():
    """Turn Reeborg 90 degrees to the right."""
    for _ in range(3):
        turn_left()


def move_to_wall_or_goal():
    """Move forward until reaching a wall or the goal."""
    while front_is_clear() and not at_goal():
        move()


def follow_right_wall():
    """Perform one navigation decision using the right-hand rule."""
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


move_to_wall_or_goal()

if not at_goal():
    turn_left()

while not at_goal():
    follow_right_wall()