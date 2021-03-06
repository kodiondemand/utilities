# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# platformtools
# ------------------------------------------------------------
# Herramientas responsables de adaptar los diferentes
# cuadros de dialogo a una plataforma en concreto,
# en este caso Kodi.
# version 2.0
# ------------------------------------------------------------

from __future__ import division
from __future__ import absolute_import
import sys
PY3 = False
if sys.version_info[0] >= 3: PY3 = True; unicode = str; unichr = chr; long = int

import xbmc
import xbmcgui
from dependencies import config


class XBMCPlayer(xbmc.Player):

    def __init__(self, *args):
        pass


xbmc_player = XBMCPlayer()


def makeMessage(line1, line2, line3):
    message = line1
    if line2:
        message += '\n' + line2
    if line3:
        message += '\n' + line3
    return message

def dialog_ok(heading, line1, line2="", line3=""):
    dialog = xbmcgui.Dialog()
    return dialog.ok(heading, makeMessage(line1, line2, line3))


def dialog_notification(heading, message, icon=0, time=5000, sound=True):
    dialog = xbmcgui.Dialog()
    try:
        l_icono = xbmcgui.NOTIFICATION_INFO, xbmcgui.NOTIFICATION_WARNING, xbmcgui.NOTIFICATION_ERROR
        dialog.notification(heading, message, l_icono[icon], time, sound)
    except:
        dialog_ok(heading, message)


def dialog_yesno(heading, line1, line2="", line3="", nolabel="No", yeslabel="Si", autoclose=0, customlabel=None):
    # customlabel only on kodi 19
    dialog = xbmcgui.Dialog()
    if config.get_platform() == 'kodi-matrix':
        if autoclose:
            return dialog.yesno(heading, makeMessage(line1, line2, line3), nolabel=nolabel, yeslabel=yeslabel, customlabel=customlabel, autoclose=autoclose)
        else:
            return dialog.yesno(heading, makeMessage(line1, line2, line3), nolabel=nolabel, yeslabel=yeslabel, customlabel=customlabel)
    else:
        if autoclose:
            return dialog.yesno(heading, makeMessage(line1, line2, line3), nolabel=nolabel, yeslabel=yeslabel, autoclose=autoclose)
        else:
            return dialog.yesno(heading, makeMessage(line1, line2, line3), nolabel=nolabel, yeslabel=yeslabel)


def dialog_select(heading, _list):
    return xbmcgui.Dialog().select(heading, _list)


def dialog_multiselect(heading, _list, autoclose=0, preselect=[], useDetails=False):
    return xbmcgui.Dialog().multiselect(heading, _list, autoclose=autoclose, preselect=preselect, useDetails=useDetails)


def dialog_progress(heading, line1, line2=" ", line3=" "):
    dialog = xbmcgui.DialogProgress()
    dialog.create(heading, makeMessage(line1, line2, line3))
    return dialog


def dialog_progress_bg(heading, message=""):
    try:
        dialog = xbmcgui.DialogProgressBG()
        dialog.create(heading, message)
        return dialog
    except:
        return dialog_progress(heading, message)


def dialog_input(default="", heading="", hidden=False):
    keyboard = xbmc.Keyboard(default, heading, hidden)
    keyboard.doModal()
    if keyboard.isConfirmed():
        return keyboard.getText()
    else:
        return None


def dialog_numeric(_type, heading, default=""):
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(_type, heading, default)
    return d


def dialog_textviewer(heading, text):  # disponible a partir de kodi 16
    return xbmcgui.Dialog().textviewer(heading, text)


def dialog_browse(_type, heading, default=""):
    dialog = xbmcgui.Dialog()
    d = dialog.browse(_type, heading, 'files')
    return d

def log(texto):
    xbmc.log(texto, xbmc.LOGNOTICE)

