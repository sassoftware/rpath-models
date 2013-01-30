#!/usr/bin/python
#
# Copyright (c) SAS Institute Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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

class Survey(SerializableObject):
    """
    Wrapper object that serializes a cElementTree object
    """
    def __init__(self, dom):
        self.dom = dom

    def export(self, stream, level, namespace_=None, name_=None, namespacedef_=None):
        from xml.etree import ElementTree as etree
        if etree.iselement(self.dom):
            self.dom.tag = name_
            etree.ElementTree(self.dom).write(stream)

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
