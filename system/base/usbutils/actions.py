#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("lsusb.py", "share\/usb.ids", "share/misc/usb.ids")
    shelltools.system("./autogen.sh")
    autotools.configure("--datadir=/usr/share/misc \
                         --disable-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/sbin")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
