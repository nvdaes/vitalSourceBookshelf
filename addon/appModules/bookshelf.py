# -*- coding: UTF-8 -*-
#bookshelf.py
#Copyright (C) 2017 Noelia Ruiz Martínez
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import appModuleHandler
import controlTypes
import NVDAObjects.IAccessible
import windowUtils
import api
import winUser
from NVDAObjects.window import Window

def getDocument():
	try:
		document = NVDAObjects.IAccessible.getNVDAObjectFromEvent(
			windowUtils.findDescendantWindow(api.getForegroundObject().windowHandle, className="Internet Explorer_Server"),
			winUser.OBJID_CLIENT, 0)
		return document
	except LookupError:
		return None

class EnhancedPane(Window):

	def event_gainFocus(self):
		document = getDocument()
		if document:
			getDocument().setFocus()

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_PANE:
			clsList.insert(0, EnhancedPane)
