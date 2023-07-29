#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 Ryusei Baba <babaryusei.kw@gmail.com>
# SPDX-License-Identifier: BSD 3-Clause

import rospy
import time
import roslib
roslib.load_manifest('zundam_orne')
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from playsound import playsound


class ZundamNode(): 
    def __init__(self):
        self.sub = rospy.Subscriber('cmd_vel', Twist, self.callback, queue_size = 1)
        self.vel = Twist()
        self.flg = 0
        self.time = 0
               
    def timer(self):
        self.time += 0.1

    def callback(self, Twist): 
        if self.time <= 5:
            if self.flg != 1 and Twist.linear.x == 0.0:
                playsound(roslib.packages.get_pkg_dir('zundam_orne') + '/voice/004_ずんだもん（ノーマル）_お休み中なのだ.wav')               
                self.flg = 1
                self.time = 0
                return Twist
            elif self.flg != 2 and Twist.linear.x > 0.2 and Twist.angular.z < 0.2 and Twist.angular.z > -0.2:
                playsound(roslib.packages.get_pkg_dir('zundam_orne') + '/voice/001_ずんだもん（ノーマル）_まっすぐ進むのだ.wav')
                self.flg = 2
                self.time = 0
                return Twist
            elif self.flg != 3 and Twist.angular.z <= -0.2:
                playsound(roslib.packages.get_pkg_dir('zundam_orne') + '/voice/002_ずんだもん（ノーマル）_右に曲がるのだ.wav')
                self.flg = 3
                self.time = 0
                return Twist
            elif self.flg != 4 and Twist.angular.z >= 0.2:
                playsound(roslib.packages.get_pkg_dir('zundam_orne') + '/voice/003_ずんだもん（ノーマル）_左に曲がるのだ.wav')
                self.flg = 4
                self.time = 0
                return Twist
        else:
            if self.flg == 1:
                playsound(roslib.packages.get_pkg_dir('zundam_orne') + '/voice/004_ずんだもん（ノーマル）_お休み中なのだ.wav')               
                self.time = 0
                return Twist
            elif self.flg == 2:
                playsound(roslib.packages.get_pkg_dir('zundam_orne') + '/voice/001_ずんだもん（ノーマル）_まっすぐ進むのだ.wav')
                self.time = 0
                return Twist
            elif self.flg == 3:
                playsound(roslib.packages.get_pkg_dir('zundam_orne') + '/voice/002_ずんだもん（ノーマル）_右に曲がるのだ.wav')
                self.time = 0
                return Twist
            elif self.flg == 4:
                playsound(roslib.packages.get_pkg_dir('zundam_orne') + '/voice/003_ずんだもん（ノーマル）_左に曲がるのだ.wav')
                self.time = 0
                return Twist
        
        rospy.loginfo("time: time=%f", self.time)        
        # rospy.loginfo("Velocity: Linear=%f angular=%f" % (Twist.linear.x,Twist.angular.z))

def main():
    rospy.init_node('zundam_node')
    rate = rospy.Rate(10)
    node = ZundamNode()
    while not rospy.is_shutdown():
        # rospy.spin()
        node.timer()
        rate.sleep()

if __name__ == '__main__':
    main()
