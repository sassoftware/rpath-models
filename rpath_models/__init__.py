#!/usr/bin/python
#
# Copyright (c) 2010 rPath, Inc.
#
# This program is distributed under the terms of the Common Public License,
# version 1.0. A copy of this license should have been distributed with this
# source file in a file called LICENSE. If it is not present, the license
# is always available at http://www.rpath.com/permanent/licenses/CPL-1.0.
#
# This program is distributed in the hope that it will be useful, but
# without any warranty; without even the implied warranty of merchantability
# or fitness for a particular purpose. See the Common Public License for
# full details.
#

import sys
from xml.dom import minidom

from rpath_models import generateds_schedule_1_0 as generateds_schedule
from rpath_models import generateds_system_1_0 as generateds_system


class SerializableObject(object):
    attrs = []
    RootNode = None

    class InvalidXML(Exception):
        "Raised when the XML data is invalid"


    def serialize(self, stream):
        self._writeToStream(stream)

    def parseStream(self, fromStream):
        if isinstance(fromStream, (str, unicode)):
            func = minidom.parseString
        else:
            func = minidom.parse
        try:
            doc = func(fromStream)
        except Exception, e:
            raise self.InvalidXML(e), None, sys.exc_info()[2]
        rootNode = doc.documentElement
        self.__init__()
        self.build(rootNode)

    def _writeToStream(self, stream):
        if self.attrs:
            namespacedef = ' '.join('%s="%s"' % a for a in self.attrs)
        else:
            namespacedef = None

        self.export(stream, 0, namespace_ = '', name_ = self.RootNode,
            namespacedef_ = namespacedef)

class System(generateds_system.system, SerializableObject):
    RootNode = "system"

Inventory = generateds_system.inventory
Network = generateds_system.network
Networks = generateds_system.networks
Systems = generateds_system.systems
SystemsHref = generateds_system.href_node
LogHref = generateds_system.href_node
Log = generateds_system.log
Schedule = generateds_schedule.schedule_type
SystemLogEntry = generateds_system.system_log_entry
SystemLog = generateds_system.system_log
SystemLogHref = generateds_system.href_node
CurrentState = generateds_system.current_state
ManagementInterface = generateds_system.management_interface
