import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from math import pi


class Navigator:
    def __init__(self):
        self.navigator = BasicNavigator()

    def create_pose(self, pos_x, pos_y, rot_z):
        q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, rot_z)
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.navigator.get_clock().now().to_msg()
        pose.pose.position.x = pos_x
        pose.pose.position.y = pos_y
        pose.pose.position.z = pos_x
        pose.pose.orientation.x = q_x
        pose.pose.orientation.y = q_y
        pose.pose.orientation.z = q_z
        pose.pose.orientation.w = q_w
        return pose

    def follow_waypoints(self, waypoints):
        self.navigator.followWaypoints(waypoints)
        while not self.navigator.isTaskComplete():
            print(self.navigator.getFeedback())


def main():
    rclpy.init()

    navigator = Navigator()

    waypoints = [
        navigator.create_pose(3.5, 2.0, 3.5),
        navigator.create_pose(0.0, 1.5, 1.5),
        navigator.create_pose(0.0, 0.0, 0.0),
    ]

    navigator.follow_waypoints(waypoints)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
