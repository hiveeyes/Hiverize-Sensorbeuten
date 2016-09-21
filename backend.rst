####################
The Hiverize Backend
####################


************
Introduction
************
The Hiverize backend could reuse system components of the Hiveeyes project,
a flexible, open source beehive monitoring infrastructure platform and toolkit.

It is built on top of InfluxDB for storing
measurement data and Grafana for displaying it.

The system can be operated as an open, collaborative platform
for a whole beekeeper collective as well as in a private setup.

There are ready-made Debian-compatible distribution packages for all system components
offering a wash-and-go setup on Intel (x86) and RaspberryPi (ARM) architectures.

See also:

- https://hiveeyes.org/
- https://github.com/hiveeyes
- https://github.com/influxdata/influxdb
- https://github.com/grafana/grafana


***************
backend_test.py
***************


About
=====
This script acts as an example blueprint for sending measurement data to the data acquisition backend.


Platform
========
Send dummy measurement data to the Hiveeyes backend platform ``swarm.hiveeyes.org``
in the context of *Hiverize*. All data is processed, stored and can be accessed
anonymously. The platform is fully managed by a Berlin-based beekeeper collective
and is ready to receive measurements from other beekeeper collectives around the world.

Setup::

    pip install paho-mqtt

Run::

    python backend_test.py

Go to:

    https://swarm.hiveeyes.org/grafana/dashboard/db/ea2a38ce-791e-11e6-b152-7cd1c38000be


Self-hosted
===========
When aiming at a local or private setup

#. Just follow the guidelines about how to
   `install the data acquisition system on a RaspberryPi <https://hiveeyes.org/docs/system/setup-backend.html>`__.

#. Then, configure the backend for the *Hiverize* realm by copying
   and activating the included configuration file ``backend.ini``::

    cp backend.ini /etc/kotori/apps-available/hiverize.ini
    ln -s /etc/kotori/apps-available/hiverize.ini /etc/kotori/apps-enabled/
    systemctl restart kotori

#. After that, the backend should be happy to receive measurement data on ``localhost`` or any other host
   the backend was installed to, so just enable the appropriate host name in ``backend_test.py``::

    mqtt_host = 'localhost'

   or::

    mqtt_host = 'backend.hiverize.org'


************
Grafana demo
************
What you can expect from this backend is an instant-on, interactive graph visualization in Grafana, like:

.. figure:: https://ptrace.hiveeyes.org/2016-09-13_hiverize_grafana_testdrive.jpg
    :alt: Screenshot of Hiverize dummy measurement data in Grafana

    Screenshot of Hiverize dummy measurement data in Grafana


*******
Outlook
*******
To get a rough idea about additional features...

- There are different ways to send measurement data to the backend, see `data acquisition`_.
- The system can send alerts on significant events, see `Schwarmalarm`_.
- Data can be exported easily in different ways, see `data export`_.


.. _data acquisition: https://hiveeyes.org/docs/system/handbook.html#data-acquisition
.. _Schwarmalarm: https://hiveeyes.org/docs/system/schwarmalarm-mqttwarn.html
.. _data export: https://getkotori.org/docs/handbook/export/

