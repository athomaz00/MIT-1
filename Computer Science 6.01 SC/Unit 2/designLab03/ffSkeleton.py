import lib601.sm as sm

class FollowFigure(sm.SM):
    def __init__(self, goal_points):
        assert goal_points, "Goal points needs to contain more then one point."
        self.startState = (0, goal_points)

    def getNextValues(self, state, inp):
        goal_index, goals = state
        if inp.odometry.point().isNear(goals[goal_index], 0.01):
            goal_index = min(goal_index + 1, len(goals) - 1)
            return ((goal_index, goals), goals[goal_index])
        else:
            return (state, goals[goal_index])
