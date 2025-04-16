# see also: https://python-snap7.readthedocs.io/en/latest/_modules/snap7/server.html

import time
from tango import AttrQuality, AttrWriteType, DispLevel, DevState, Attr, CmdArgType, UserDefaultAttrProp
from tango.server import Device, attribute, command, DeviceMeta
from tango.server import class_property, device_property
from tango.server import run
import os
import datetime
import snap7
from snap7.server import Server
from snap7.server import mainloop
from threading import Thread

class Snap7Simulator(Device, metaclass=DeviceMeta):
    pass
    port = device_property(dtype=int, default_value=10002)

    def runServer(self):
        mainloop(tcp_port=self.port, init_standard_values=False)

    def init_device(self):
        self.set_state(DevState.INIT)
        self.get_device_properties(self.get_device_class())
        self.info_stream("Connecting to port: " + str(self.port))
        Thread(target=self.runServer, daemon=True).start()
        self.set_state(DevState.ON)

if __name__ == "__main__":
    deviceServerName = os.getenv("DEVICE_SERVER_NAME")
    run({deviceServerName: Snap7Simulator})
