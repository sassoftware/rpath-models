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

from rpath_models import generateds_schedule, generateds_system

Inventory = generateds_system.inventory
System = generateds_system.system
Systems = generateds_system.systems
SystemsHref = generateds_system.systems_href
LogHref = generateds_system.log_href
Log = generateds_system.log
Schedule = generateds_schedule.schedule_type
