# -*- coding: utf-8 -*-
# (c) 2015-2016 Andreas Motl, Hiveeyes <andreas@hiveeyes.org>
# (c) 2015-2016 Richard Pobering, Hiveeyes <richard@hiveeyes.org>
# License: GNU LGPL, see https://www.gnu.org/licenses/lgpl-3.0.txt
"""
Example program to send measurement data to the MQTT software bus to
store it persistently in a time series database, draw beautiful graphs,
and optionally get alerted for important events (e.g. "Schwarmalarm").

Suitable even for many beekeepers having multiple hives at different sites.
"""
import os
import json
import logging
import paho.mqtt.client as mqtt

logger = logging.getLogger(__name__)


def send_dummy_measurement():


    # --------------------------------
    # A. Where to send measurements to
    # --------------------------------

    # The MQTT host
    mqtt_host = 'swarm.hiveeyes.org'

    # The MQTT topic
    # See also: https://hiveeyes.org/docs/system/vendor/hiveeyes-one/topology.html#rationale
    mqtt_topic = u'{realm}/{network}/{gateway}/{node}/message-json'.format(
        realm   = 'hiverize',                                   # Kollektiv
        network = 'ea2a38ce-791e-11e6-b152-7cd1c38000be',       # Imker
        gateway = 'clar14',                                     # Standort
        node    = '1'                                           # Beute
    )


    # ---------------------------
    # B. Define dummy measurement
    # ---------------------------
    measurement = {
        'temp-inside':  33.33,
        'temp-outside': 42.42,
        'hum-inside':   79.12,
        'hum-outside':  83.34
    }


    # -------------------------------------------------------------
    # C. Publish measurement data to software bus / send to backend
    # -------------------------------------------------------------

    # Serialize data as JSON
    payload = json.dumps(measurement)

    # Publish to MQTT
    pid = os.getpid()
    client_id = '{}:{}'.format('hiverize', str(pid))
    backend = mqtt.Client(client_id=client_id, clean_session=True)
    backend.connect(mqtt_host)
    backend.publish(mqtt_topic, payload)
    backend.disconnect()


if __name__ == '__main__':
    send_dummy_measurement()

