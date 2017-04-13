# -*- coding: utf-8 -*-
# This is an example of popping a packet from the Emotiv class's packet queue


import time

from emokit.emotiv import Emotiv

if __name__ == "__main__":
    with Emotiv(display_output=True, verbose=False) as headset:
        while True:
            packet = headset.dequeue()
            if packet is not None:
                print str(packet.sensors['F3']['value']) + " " + \
                  str(packet.sensors['F4']['value']) + " " + \
                  str(packet.sensors['P7']['value']) + " " + \
                  str(packet.sensors['FC6']['value']) + " " + \
                  str(packet.sensors['F7']['value']) + " " + \
                  str(packet.sensors['F8']['value']) + " " + \
                  str(packet.sensors['T7']['value']) + " " + \
                  str(packet.sensors['P8']['value']) + " " + \
                  str(packet.sensors['FC5']['value']) + " " + \
                  str(packet.sensors['AF4']['value']) + " " + \
                  str(packet.sensors['T8']['value']) + " " + \
                  str(packet.sensors['O2']['value']) + " " + \
                  str(packet.sensors['O1']['value']) + " " + \
                  str(packet.sensors['AF3']['value'])
            time.sleep(0.001)
