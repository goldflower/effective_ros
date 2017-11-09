#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

if __name__ == '__main__':
	rospy.init_node('example1_b', anonymous=True)
	rospy.Subscriber('message', String, callback)
	rospy.spin()
