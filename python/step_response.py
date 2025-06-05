import sys
import time
import json

import pyleap
import pyleap.hand
import pyleap.leap_hand_utils
import pyleap.leap_hand_utils.leap_hand_utils


def main():
    leap = pyleap.hand.LeapNode(torque=False)

    def record_response(start_pos, goal_pos):
        dict = {}
        with open("angles.json", "w") as f:
            start_time = time.time()
            leap.set_leap(start_pos)
            time.sleep(1.0)
            leap.set_leap(goal_pos)
            try:
                while True:
                    end_time = time.time()
                    t = end_time - start_time
                    dict[t] = leap.read_pos().tolist()
            except KeyboardInterrupt:
                json_obj = json.dumps(dict, indent=4)
                f.write(json_obj)
                sys.exit()
    
    # zero_pos: open hand position
    zero_pos = pyleap.leap_hand_utils.leap_hand_utils.allegro_to_LEAPhand([0.0]*16)
    # settng goal position
    goal_pos = zero_pos.copy()
    goal_pos[12] = 4.71

    record_response(zero_pos, goal_pos)


if __name__=="__main__":
    main()