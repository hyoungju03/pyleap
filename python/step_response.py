import sys
import time

import pyleap
import pyleap.hand
import pyleap.leap_hand_utils
import pyleap.leap_hand_utils.leap_hand_utils






def main():

    leap = pyleap.hand.LeapNode(torque=True)

    def record_response(start_pos, goal_pos):

        with open("angles.txt", "w") as f:

            leap.set_leap(start_pos)
            time.sleep(1.5)
            leap.set_leap(goal_pos)
            try:
                while True:
                    # convert to json
                    f.write(str(leap.read_pos()))

            except KeyboardInterrupt:
                sys.exit()
        
    zero_pos = pyleap.leap_hand_utils.leap_hand_utils.allegro_to_LEAPhand([0.0]*16)
    goal_pos = zero_pos.copy()
    goal_pos[12] = 4.71

    record_response(zero_pos, goal_pos)



if __name__=="__main__":
    main()