#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from voice_mv.msg import custom
from std_msgs.msg import Bool

speed = 0.3
angular_speed = 0.6
current_angle = 0
deltaT = 0
estado = False

def callback(data):
    global speed, angular_speed, current_angle, deltaT, estado
    t0 = rospy.Time.now().to_sec()
    relative_angle = 1.57
    offset = 0.0075
    velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
    angle_publisher = rospy.Publisher('state', Bool, queue_size = 10)
    vel_msg = Twist()
    print("Comando recebido:")
    if(data.para == True):
        print "Parado"
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        current_angle = 0
        deltaT = 0
        velocity_publisher.publish(vel_msg)
    else:
        if(data.frente == True):
            if(data.direita == True):
                print "Frente: Curva a direita"
                vel_msg.linear.x = abs(speed)
                vel_msg.angular.z = -abs(angular_speed)
                if(current_angle < relative_angle):
                    estado = True
                    velocity_publisher.publish(vel_msg)
                    t1 = rospy.Time.now().to_sec()
                    deltaT = deltaT + (t1 - t0) + offset
                    current_angle = current_angle + angular_speed*(deltaT)
                    print current_angle
                else:
                    estado = False
                    deltaT = 0
                    current_angle = 0
            else:
                if(data.esquerda == True):
                    print "Frente: Curva a esquerda"
                    vel_msg.linear.x = abs(speed)
                    vel_msg.angular.z = abs(angular_speed)
                    if(current_angle < relative_angle):
                        estado = True
                        velocity_publisher.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        deltaT = deltaT + (t1 - t0) + offset
                        current_angle = current_angle + angular_speed*(deltaT)
                    else:
                        estado = False
                        deltaT = 0
                        current_angle = 0
                else:
                    print "Frente"
                    vel_msg.linear.x = abs(speed)

        else:
            if(data.tras == True):
                if(data.direita == True):
                    print "Re: Curva a direita"
                    vel_msg.linear.x = -abs(speed)
                    vel_msg.angular.z = abs(angular_speed)
                    if(current_angle < relative_angle):
                        estado = True
                        velocity_publisher.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        deltaT = deltaT + (t1 - t0) + offset
                        current_angle = current_angle + angular_speed*(deltaT)
                    else:
                        estado = False
                        deltaT = 0
                        current_angle = 0
                else:
                    if(data.esquerda == True):
                        print "Re: Curva a esquerda"
                        vel_msg.linear.x = -abs(speed)
                        vel_msg.angular.z = -abs(angular_speed)
                        if(current_angle < relative_angle):
                            estado = True
                            velocity_publisher.publish(vel_msg)
                            t1 = rospy.Time.now().to_sec()
                            deltaT = deltaT + (t1 - t0) + offset
                            current_angle = current_angle + angular_speed*(deltaT)
                        else:
                            estado = False
                            deltaT = 0
                            current_angle = 0
                    else:
                        print "Re"
                        vel_msg.linear.x = -abs(speed)
            else:
                if(data.frente == False):
                    if(data.direita == True):
                        print "Giro: 90 graus a direita"
                        vel_msg.angular.z = -abs(angular_speed)
                        if(current_angle < relative_angle):
                            estado = True
                            velocity_publisher.publish(vel_msg)
                            t1 = rospy.Time.now().to_sec()
                            deltaT = deltaT + (t1 - t0) + offset
                            current_angle = current_angle + angular_speed*(deltaT)
                        else:
                            estado = False
                            deltaT = 0
                            current_angle = 0
                    else:
                        if(data.esquerda == True):
                            print "Giro: 90 graus a esquerda"
                            vel_msg.angular.z = abs(angular_speed)
                            if(current_angle < relative_angle):
                                estado = True
                                velocity_publisher.publish(vel_msg)
                                t1 = rospy.Time.now().to_sec()
                                deltaT = deltaT + (t1 - t0) + offset
                                current_angle = current_angle + angular_speed*(deltaT)
                                print current_angle
                            else:
                                estado = False
                                deltaT = 0
                                current_angle = 0
                        else:
                            vel_msg.linear.x = 0
                            vel_msg.angular.z = 0
                            current_angle = 0
                            deltaT = 0
                            velocity_publisher.publish(vel_msg)
                            print "Parado"
    if(data.rapido == True):
        if(speed < 0.8):
            print "Acrescimo de velocidade"
            speed = speed + 0.1*speed
            print speed
        else:
            speed = 0.8
            print "Velocidade Maxima"
            print speed
    else:
        if(data.devagar == True):
            if(speed > 0.1):
                print "Decrescimo de velocidade"
                speed = speed - 0.1*speed
                print speed
            else:
                speed = 0.1
                print "Velocidade Minima"
                print speed

    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    velocity_publisher.publish(vel_msg)
    angle_publisher.publish(estado)

def move():
    rospy.init_node('robot_cleaner', anonymous=True)
    rospy.Subscriber("comando", custom, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        print "Executando"
        move()
    except rospy.ROSInterruptException: 
    	pass