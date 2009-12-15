#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir="SOAPpy-0.12.0"

def install():
    pythonmodules.install()

    pisitools.dodoc("ChangeLog", "PKG-INFO", "LICENSE","README", "TODO")
