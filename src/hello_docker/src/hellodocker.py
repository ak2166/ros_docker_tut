#!/usr/bin/env python
import rospy

rospy.init_node('hello_docker')
rate=rospy.Rate(2)

while not rospy.is_shutdown():
    print 'Hello docker!'
    rate.sleep()
