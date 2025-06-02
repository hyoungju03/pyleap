import time
from pyleap import hand

def main():

    lead = hand.LeapNode('/dev/ttyUSB0',torque=True)
    # follow = hand.LeapNode('/dev/ttyUSB1',torque=True)

    # lead.set_zeros()
    # follow.set_zeros()

    while True:
        #Set to an open pose and read the joint angles 33hz
        # leader_pos = lead.read_pos()
        # print("Position: " + str(leader_pos))
        # # follow.set_leap(leader_pos)
        # time.sleep(0.03)
        lead.set_zeros()

if __name__=="__main__":
    main()