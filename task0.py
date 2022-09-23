#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		    HolA Bot (HB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of HolA Bot (KB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_0.py
# Functions:
# 					[ Comma separated list of functions in this file ]
# Nodes:		    Add your publishing and subscribing node


####################### IMPORT MODULES #######################
import sys
import traceback
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time 
from std_srvs.srv import Empty

##############################################################


def callback(data):
	global x
	global y,z,yaw
	x= data.x
	y=data.y
	yaw=data.theta+3.14
	"""
	Purpose:
	---
	This function should be used as a callback. Refer Example #1: Pub-Sub with Custom Message in the Learning Resources Section of the Learning Resources.
    You can write your logic here.
    NOTE: Radius value should be 1. Refer expected output in document and make sure that the turtle traces "same" path.

	Input Arguments:
	---
        `data`  : []
            data received by the call back function

	Returns:
	---
        May vary depending on your logic.

	Example call:
	---
        Depends on the usage of the function.
	"""


def main():
	rospy.init_node('turtlesim_move_pos',anonymous=True)
	cmd_vel_topic='/turtle1/cmd_vel'
	velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)
	position_topic = '/turtle1/pose'
	pose_subscriber = rospy.Subscriber(position_topic,Pose,callback)
	time.sleep(2)
	velocity_message = Twist()
	global x,y,k
	k=0.002
	rospy.loginfo("Turtlesim starts moving in circle")
	velocity_message.linear.x=0
	velocity_message.angular.z=0
	init_y=y
	print("initial position : "+str(init_y),end="")
	velocity_publisher.publish(velocity_message)
	velocity_message.linear.x=speed
	velocity_message.angular.z=speed/radius
	velocity_publisher.publish(velocity_message)
	while not(abs(y-(init_y+2*radius))<k):
		velocity_publisher.publish(velocity_message)
		print("  "+str(init_y)+"  "+str(yaw)+" dif "+str(abs(y-(init_y+2))))
		#rospy.Rate(10)
	velocity_message.linear.x=0
	velocity_publisher.publish(velocity_message)
	while (abs(yaw - 1.57)>k):
		velocity_publisher.publish(velocity_message)
		print("  "+str(yaw)+" dif "+str(abs(yaw - 1.57)))
	velocity_message.linear.x= speed
	velocity_message.angular.z=0
	velocity_publisher.publish(velocity_message)
	while (abs(y-init_y)>k):
		velocity_publisher.publish(velocity_message)
		print("  "+str(init_y)+"  "+str(yaw)+" dif "+str(abs(y-init_y)))
	velocity_message.linear.x= 0
	velocity_message.angular.z=0
	velocity_publisher.publish(velocity_message)
	#moveforward(0.5,2.0,True)
################# ADD GLOBAL VARIABLES HERE #################
x=0
y=0
z=0
yaw=0
radius=1
speed=0.28
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################

##############################################################


######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS PART #########
if __name__ == "__main__":
    try:
        print("------------------------------------------")
        print("         Python Script Started!!          ")
        print("------------------------------------------")
        main()

    except:
        print("------------------------------------------")
        traceback.print_exc(file=sys.stdout)
        print("------------------------------------------")
        sys.exit()

    finally:
        print("------------------------------------------")
        print("    Python Script Executed Successfully   ")
        print("------------------------------------------")
