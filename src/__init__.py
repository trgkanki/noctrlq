# -*- coding: utf-8 -*-
#
# addon_template v20.5.4i8
#
# Copyright: trgk (phu54321@naver.com)
# License: GNU AGPL, version 3 or later;
# See http://www.gnu.org/licenses/agpl.html

from aqt import mw
from aqt.main import AnkiQt
from aqt.utils import askUser
from anki.hooks import wrap

from .utils import openChangelog
from .utils import uuid  # duplicate UUID checked here


def newCloseEvent(self, event, *, _old):
    if self.state == "profileManager":
        return _old(self, event)

    if askUser("Really close?"):
        return _old(self, event)
    else:
        event.ignore()


AnkiQt.closeEvent = wrap(AnkiQt.closeEvent, newCloseEvent, "around")

# mw.form.action** is inited on setupUI(), before any addon has been initialized.
mw.form.actionExit.setShortcuts([])
