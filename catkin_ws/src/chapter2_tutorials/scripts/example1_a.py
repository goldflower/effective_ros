#!/usr/bin/env python

import rospy
import tf
from std_msgs.msg import String

if __name__ == "__main__":
	rospy.init_node("example1_a", anonymous=False)
	chatter_pub = rospy.Publisher('message', String, queue_size=10)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		msg = "I am the example1_a node"
		chatter_pub.publish(msg)
		rate.sleep()


