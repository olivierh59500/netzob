# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Standard library imports
#+---------------------------------------------------------------------------+
import os

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+
from gi.repository import Gtk, Pango

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+

from netzob.Common.Plugins.Importers.AbstractImporterView import AbstractImporterView

class PCAPImporterView(AbstractImporterView):
    """View of PCAP importer plugin"""

    def __init__(self, controller):
        super(PCAPImporterView, self).__init__(controller)

        # Import and add configuration widget
        self.builderConfWidget = Gtk.Builder()
        curDir = os.path.dirname(__file__)
        self.builderConfWidget.add_from_file(os.path.join(curDir, "PCAPImportConfigurationWidget.glade"))
        self._getObjects(self.builderConfWidget, ["pcapConfigurationBox",
                "filterEntry", "layerRadioButton2", "layerRadioButton3",
                "layerRadioButton4"])
        self.layerRadioButton4.set_active(True)
        self.builderConfWidget.connect_signals(self.controller)
        self.setImportConfigurationWidget(self.pcapConfigurationBox)
        self._textCell = Gtk.CellRendererText()
        self.makeL4ImportTreeView()

    def addTreeViewTextColumn(self, text, modelColumn):
        column = Gtk.TreeViewColumn(text)
        column.pack_start(self._textCell, True)
        column.add_attribute(self._textCell, "text", modelColumn)
        column.set_sort_column_id(modelColumn)
        self.listTreeView.append_column(column)

    def addTreeViewSelectedToggleColumn(self):
        toggleCellRenderer = Gtk.CellRendererToggle()
        toggleCellRenderer.set_activatable(True)
        toggleCellRenderer.connect("toggled", self.controller.selectMessage)
        # Selected column
        column = Gtk.TreeViewColumn()
        column.pack_start(toggleCellRenderer, True)
        column.add_attribute(toggleCellRenderer, "active", 1)
        self.listTreeView.append_column(column)

    def removeAllTreeViewColumns(self):
        columnList = self.listTreeView.get_columns()
        for column in columnList:
            self.listTreeView.remove_column(column)

    def makeL2ImportTreeView(self):
        self.removeAllTreeViewColumns()
        # Liststore to displayer layer 2 packets
        # ID, Selected, Source Address, Destination Address, Payload
        self.listListStore = Gtk.ListStore(
                str, 'gboolean', str, str, str)
        self.listTreeView.set_model(self.listListStore)
        self.addTreeViewSelectedToggleColumn()
        self.addTreeViewTextColumn("Source Address", 2)
        self.addTreeViewTextColumn("Destination Address", 3)
        self.addTreeViewTextColumn("Payload", 4)

    def makeL3ImportTreeView(self):
        self.removeAllTreeViewColumns()
        # Liststore to display layer 3 packets
        # ID, Selected, Source IP, Destination IP, Payload
        self.listListStore = Gtk.ListStore(
                str, 'gboolean', str, str, str)
        self.listTreeView.set_model(self.listListStore)
        self.addTreeViewSelectedToggleColumn()
        self.addTreeViewTextColumn("Source IP", 2)
        self.addTreeViewTextColumn("Destination IP", 3)
        self.addTreeViewTextColumn("Payload", 4)

    def makeL4ImportTreeView(self):
        self.removeAllTreeViewColumns()
        # Liststore to display layer 4 packets
        # ID, Selected, Source IP, Destination IP, Protocol, 
        # Source Port, Destination Port, Payload
        self.listListStore = Gtk.ListStore(
                str, 'gboolean', str, str, str, str, str, str)
        self.listTreeView.set_model(self.listListStore)
        self.addTreeViewSelectedToggleColumn()
        self.addTreeViewTextColumn("Source IP", 2)
        self.addTreeViewTextColumn("Destination IP", 3)
        self.addTreeViewTextColumn("Protocol", 4)
        self.addTreeViewTextColumn("Source Port", 5)
        self.addTreeViewTextColumn("Destination Port", 6)
        self.addTreeViewTextColumn("Payload", 7)