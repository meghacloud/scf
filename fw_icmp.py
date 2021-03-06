#
# Copyright (C) 2008 Red Hat, Inc.
# Authors:
# Thomas Woerner <twoerner@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from fw_config import _

class _ICMPType:
    def __init__ (self, key, name, description=None, type=None): 
        self.key = key
        self.name = name
        self.description = description
        self.type = type # type None means ipv4 and ipv6

icmp_list = [
    _ICMPType("echo-request", _("Echo Request (ping)"),
              _("This message is used to test if a host is reachable mostly "
                "with the <i>ping</i> utility.")),
    _ICMPType("echo-reply", _("Echo Reply (pong)"),
              _("This message is the answer to an <i>Echo Request</i>.")),
    _ICMPType("destination-unreachable", _("Destination Unreachable"),
              _("This error message is generated by a host or gateway if the "
                "destination is not reachable.")),
    _ICMPType("parameter-problem", _("Parameter Problem"),
              _("This error message is generated if the IP header is bad, "
                "either by a missing option or bad length.")),
    _ICMPType("redirect", _("Redirect"), 
              _("This error message informs a host to send packets on another "
                "route.")),
    _ICMPType("router-advertisement", _("Router Advertisement"), 
              _("This message is used by routers to periodically announce "
                "the IP address of a multicast interface.")),
    _ICMPType("router-solicitation", _("Router Solicitation"),
              _("This message is used by a host attached to a multicast "
                "link to request a <i>Router Advertisement</i>")),
    _ICMPType("source-quench", _("Source Quench"),
              _("This error message is generated to tell a host to reduce the "
                "pace at which it is sending packets."),
              "ipv4"),
    _ICMPType("time-exceeded", _("Time Exceeded"),
              _("This error message is generated if the time-to-live was "
                "exceeded either of a packet or of the reassembling of a "
                "fragmented packet.")),
    ]

def getByKey(key):
    for x in icmp_list:
        if x.key == key:
            return x
    return None

def getByName(name):
    for x in icmp_list:
        if x.name == name:
            return x
    return None
