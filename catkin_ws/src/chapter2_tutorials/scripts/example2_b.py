#!/usr/bin/env python
import rospy
from chapter2_tutorials.srv import *
import sys


def add_3_ints_client(A, B, C):
	rospy.wait_for_service('add_3_ints')
	try:
		sess = rospy.ServiceProxy('add_3_ints', chapter2_srv1)
		resp = sess(A, B, C)
		return resp.sum
	except rospy.ServiceException, e:
		print("Service call failed: {}".format(e))

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('usage: {} [A B C]'.format(sys.argv[0]))
		sys.exit(1)
	A, B, C = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
	rospy.init_node('add_3_ints_client')
	print('requesting {}+{}+{}'.format(A, B, C))
	print('result is:', add_3_ints_client(A, B, C))
