import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST


def test_south_turn(robot):
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH


def test_west_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.WEST


def test_north_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.NORTH


def test_illegal_move_east(robot):
    robot.turn()

    with pytest.raises(IllegalMoveException):
        for _ in range(10):
            robot.move()


def test_illegal_move_south(robot):
    robot.turn()
    robot.turn()

    with pytest.raises(IllegalMoveException):
        while True:
            robot.move()


def test_illegal_move_west(robot):
    robot.turn()
    robot.turn()
    robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_north(robot):
    with pytest.raises(IllegalMoveException):
        for _ in range(10):
            robot.move()


def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1


def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1
