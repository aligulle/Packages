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
    shelltools.export("DEFS", "NO_ASM")
    shelltools.export("CPPFLAGS", "-DHAVE_LSTAT")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add missing gzcat
    pisitools.dosym("zcat", "/usr/bin/gzcat")

    pisitools.remove("/usr/bin/uncompress")

    pisitools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO")
