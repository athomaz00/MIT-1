import lib601.sm as sm
import lib601.util as util
import math

# Use this line for running in idle
# import lib601.io as io
# Use this line for testing in soar
from soar.io import io

def is_between(x, theta1, theta2):
    """
    Returns true if x is between theta1 and theta2. This function handles
    the case where theta2 is above 2 pi.
    """
    return (theta1 < x < theta2) or (theta1 < x + 2 * math.pi < theta2)

class DynamicMoveToPoint(sm.SM):
    def getNextValues(self, state, inp):
        print 'DynamicMoveToPoint', 'state=', state, 'inp=', inp
        assert isinstance(inp,tuple), 'inp should be a tuple'
        assert len(inp) == 2, 'inp should be of length 2'
        assert isinstance(inp[0],util.Point), 'inp[0] should be a Point'

        goal_point, sensors = inp
        pose = sensors.odometry
        goal_theta = util.fixAngle02Pi(pose.point().angleTo(goal_point))
        
        if not util.nearAngle(goal_theta, pose.theta, 0.04):
            print "Goal theta is", goal_theta
            print "Pose theta is", pose.theta
            if is_between(goal_theta, pose.theta, pose.theta + math.pi):
                return (state, io.Action(rvel=0.03, fvel=0.0))
            else:
                return (state, io.Action(rvel=-0.03, fvel=0.0))
        return (state, io.Action(rvel=0.00, fvel=pose.point().distance(goal_point)))
