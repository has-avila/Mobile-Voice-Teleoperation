#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from std_msgs.msg import String
from std_msgs.msg import Bool
from voice_mv.msg import custom
import numpy as np

last_data = ""
msg = custom()
msg.para = True
started = False
state = False
pub = rospy.Publisher('/comando', custom, queue_size=1000)

def callback2(data):
	global state
	state = data.data

def callback(data):
    print "Nova mensagem recebida"
    global started, last_data, msg, state
    last_data = data
    if(last_data.data == "frente" or last_data.data == "forward"):
    	state = True
    	msg.frente = True
    	msg.tras = False
    	msg.para = False
    	msg.direita = False
    	msg.esquerda = False
    	msg.rapido = False
    	msg.devagar = False
    else:
    	if(last_data.data == "tras" or last_data.data == "backward"):
    		state = True
    		msg.frente = False
    		msg.tras = True
    		msg.para = False
    		msg.direita = False
    		msg.esquerda = False
    		msg.rapido = False
    		msg.devagar = False
    	else:
    		if(last_data.data == "para" or last_data.data == "stop"):
    			state = True
    			msg.frente = False
    			msg.tras = False
    			msg.para = True
    			msg.direita = False
    			msg.esquerda = False
    			msg.rapido = False
    			msg.devagar = False
    		else:
    			if(last_data.data == "direita" or last_data.data == "right"):
    				state = True
    				msg.para = False
    				msg.direita = True
    				msg.esquerda = False
    			else:
    				if(last_data.data == "esquerda" or last_data.data == "left"):
    					state = True
    					msg.para = False
    					msg.direita = False
    					msg.esquerda = True
    				else:
    					if(last_data.data == "rapido" or last_data.data == "fast"):
    						state = True
    						msg.rapido = True
    						rospy.loginfo(msg)
    						pub.publish(msg)
    						msg.rapido = False
    					else:
    						if(last_data.data == "devagar" or last_data.data == "slow"):
    							state = True
    							msg.devagar = True
    							rospy.loginfo(msg)
    							pub.publish(msg)
    							msg.devagar = False
    						else:
    							state = True
    							msg.frente = False
    							msg.tras = False
    							msg.para = True
    							msg.direita = False
    							msg.esquerda = False
    if (not started):
        started = True
    
def timer_callback(event):
    global started, pub, msg, state
    if (started):
    	if(state == False):
    		msg.esquerda = False
    		msg.direita = False
    	rospy.loginfo(msg)
    	pub.publish(msg)
        print "Ultima mensagem publicada"


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.Subscriber('state', Bool, callback2)
    timer = rospy.Timer(rospy.Duration(0.1), timer_callback)
    rospy.spin()    
    timer.shutdown()

if __name__ == '__main__':
    print "Executando"
    listener()