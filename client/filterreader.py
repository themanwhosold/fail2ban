# This file is part of Fail2Ban.
#
# Fail2Ban is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Fail2Ban is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Fail2Ban; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# Author: Cyril Jaquier
# 
# $Revision: 1.6 $

__author__ = "Cyril Jaquier"
__version__ = "$Revision: 1.6 $"
__date__ = "$Date: 2005/11/20 17:07:47 $"
__copyright__ = "Copyright (c) 2004 Cyril Jaquier"
__license__ = "GPL"

import logging
from configreader import ConfigReader

# Gets the instance of the logger.
logSys = logging.getLogger("fail2ban.client.config")

class FilterReader(ConfigReader):
	
	def __init__(self, file, name):
		ConfigReader.__init__(self)
		self.file = file
		self.name = name
	
	def setFile(self, file):
		self.file = file
	
	def getFile(self):
		return self.file
	
	def setName(self, name):
		self.name = name
	
	def getName(self):
		return self.name
	
	def read(self):
		ConfigReader.read(self, "filter.d/" + self.file)
	
	def getOptions(self, pOpts):
		opts = [["string", "logpath", "/var/log/sshd.log"],
				["string", "timeregex", ""],
				["string", "timepattern", ""],
				["string", "failregex", ""],
				["int", "maxtime", 600],
				["int", "maxretry", 3]]
		self.opts = ConfigReader.getOptions(self, "DEFAULT", opts, pOpts)
	
	def convert(self):
		stream = list()
		for opt in self.opts:
			if opt == "logpath":
				stream.append(["set", self.name, "logpath", self.opts[opt]])
			elif opt == "timeregex":
				stream.append(["set", self.name, "timeregex", self.opts[opt]])
			elif opt == "timepattern":
				stream.append(["set", self.name, "timepattern", self.opts[opt]])
			elif opt == "failregex":
				stream.append(["set", self.name, "failregex", self.opts[opt]])
			elif opt == "maxtime":
				stream.append(["set", self.name, "maxtime", self.opts[opt]])
			elif opt == "maxretry":
				stream.append(["set", self.name, "maxretry", self.opts[opt]])
		return stream
		