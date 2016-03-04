#!/usr/bin/env python
from sine_wave import SineWave
import time
import json
import sys
from threading import Thread, Lock
from random import gauss

# global flag indicating threads should terminate
terminate = False

# Critical section to serialize access to standard out and
# avoid interleaved output
lock = Lock()


def output_measurements(item):
    """
    Thread function for outputing measurements
    """
    global terminate
    sw = SineWave(float(item['amplitude']), float(item['frequency']))
    source = item['name']
    poll = item['sample'] / 1000.0
    noise = bool(item['noise'])
    mu = float(item['mu'])
    sigma = float(item['sigma'])
    while True:
        if terminate:
            break
        amplitude = sw.data[1]
        with lock:
	    if item['noise']:
                amplitude = amplitude + gauss(mu, sigma) 
            print("{0} {1} {2}".format("SINE_WAVE_AMPLITUDE", amplitude, source))
            sys.stdout.flush()
        time.sleep(poll)


class SineWavePlugin(object):
    def __init__(self):
        pass

    def _init(self):
        """
        Initialize the plugin by reading param.json and spawning
        a thread for each of the configuration items
        """
        with open('param.json') as f:
            parameters = json.load(f)
            for item in parameters['items']:
                t = Thread(target=output_measurements, args=(item,))
                t.start()

    def run(self):
        """
        Method to start the plugin
        """
        global terminate
        self._init()
        while True:
            try:
                if terminate:
                    break
                time.sleep(0.1)
            except KeyboardInterrupt:
                terminate = True


if __name__ == "__main__":
    w = SineWavePlugin()
    w.run()
