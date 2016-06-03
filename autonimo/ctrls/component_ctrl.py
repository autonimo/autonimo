#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect
from PyQt4 import QtGui
from components.component import Component



class ComponentController(object):
    """
    Control components.
    """
    def __init__(self, model):


        self.model = model

        self.import_components_manually()


    def import_components_manually(self):


        from components.timer import Timer



        comps = [Timer]
        comps_by_category = {}




        # get categories and comps
        for comp in comps:
            if comp.CATEGORY not in comps_by_category:
                comps_by_category[comp.CATEGORY] = []
            comps_by_category[comp.CATEGORY].append(comp)

        # make category items
        for category in comps_by_category:
            item_category = QtGui.QStandardItem(category)
            for comp in comps_by_category[category]:
                item = QtGui.QStandardItem(comp.NAME)
                # item_desc = QtGui.QStandardItem(comp.DESCRIPTION)
                # item.appendRow(item_desc)
                item.setData(comp)
                item_category.appendRow(item)

            self.model.comps_available_model.appendRow(item_category)



    def create_comp(self, index):
        comp = self.model.comps_available_model.itemFromIndex(index).data()
        if comp is not None and issubclass(comp, Component):
            return comp(self.model)


