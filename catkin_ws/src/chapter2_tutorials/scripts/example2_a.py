#!/usr/bin/env python

import rospy
from chapter2_tutorials.srv import * # import all services in package "chapter2_tutorials"

def add(req):	
	print('compute {} + {} + {}'.format(req.A, req.B, req.C))
	return req.A + req.B + req.C

if __name__ == "__main__":
	rospy.init_node("add_server")
	srv = rospy.Service("add_3_ints", chapter2_srv1, add)
	rospy.spin()
