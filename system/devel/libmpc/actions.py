#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mpc-%s" % get.srcVERSION()


def setup():
    shelltools.export("EGREP", "egrep")
    shelltools.export("CFLAGS", "%s -std=gnu99" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -std=gnu99" % get.CXXFLAGS())

    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING.LIB", "README*", "NEWS")

