# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DockWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(340, 578)
        DockWidget.setFloating(False)
        DockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_8.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tabVector = QtWidgets.QWidget()
        self.tabVector.setObjectName("tabVector")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabVector)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.tabVector)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 287, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidgetVector = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidgetVector.setMinimumSize(QtCore.QSize(0, 488))
        self.stackedWidgetVector.setObjectName("stackedWidgetVector")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidgetVector.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidgetVector.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidgetVector, 0, 0, 1, 1)
        self.groupBoxGeometryTypeFilter = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxGeometryTypeFilter.setCheckable(True)
        self.groupBoxGeometryTypeFilter.setChecked(False)
        self.groupBoxGeometryTypeFilter.setObjectName("groupBoxGeometryTypeFilter")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxGeometryTypeFilter)
        self.gridLayout_2.setContentsMargins(9, 9, -1, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chkPolygon = QtWidgets.QCheckBox(self.groupBoxGeometryTypeFilter)
        self.chkPolygon.setObjectName("chkPolygon")
        self.gridLayout_2.addWidget(self.chkPolygon, 0, 3, 1, 1)
        self.chkPoint = QtWidgets.QCheckBox(self.groupBoxGeometryTypeFilter)
        self.chkPoint.setObjectName("chkPoint")
        self.gridLayout_2.addWidget(self.chkPoint, 0, 1, 1, 1)
        self.chkLine = QtWidgets.QCheckBox(self.groupBoxGeometryTypeFilter)
        self.chkLine.setObjectName("chkLine")
        self.gridLayout_2.addWidget(self.chkLine, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxGeometryTypeFilter, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabVector, "")
        self.tabRaster = QtWidgets.QWidget()
        self.tabRaster.setObjectName("tabRaster")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabRaster)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tabRaster)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 302, 608))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.stackedWidgetRaster = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents_4)
        self.stackedWidgetRaster.setMinimumSize(QtCore.QSize(0, 488))
        self.stackedWidgetRaster.setObjectName("stackedWidgetRaster")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidgetRaster.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidgetRaster.addWidget(self.page_8)
        self.gridLayout_11.addWidget(self.stackedWidgetRaster, 0, 0, 1, 1)
        self.groupBoxRasterTypeFilter = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBoxRasterTypeFilter.setCheckable(True)
        self.groupBoxRasterTypeFilter.setChecked(False)
        self.groupBoxRasterTypeFilter.setObjectName("groupBoxRasterTypeFilter")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBoxRasterTypeFilter)
        self.gridLayout_10.setContentsMargins(10, 9, -1, 9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.chkGray = QtWidgets.QCheckBox(self.groupBoxRasterTypeFilter)
        self.chkGray.setObjectName("chkGray")
        self.gridLayout_10.addWidget(self.chkGray, 0, 0, 1, 1)
        self.chkPalette = QtWidgets.QCheckBox(self.groupBoxRasterTypeFilter)
        self.chkPalette.setObjectName("chkPalette")
        self.gridLayout_10.addWidget(self.chkPalette, 0, 1, 1, 1)
        self.chkMultiband = QtWidgets.QCheckBox(self.groupBoxRasterTypeFilter)
        self.chkMultiband.setObjectName("chkMultiband")
        self.gridLayout_10.addWidget(self.chkMultiband, 1, 0, 1, 1)
        self.chkColorLayer = QtWidgets.QCheckBox(self.groupBoxRasterTypeFilter)
        self.chkColorLayer.setObjectName("chkColorLayer")
        self.gridLayout_10.addWidget(self.chkColorLayer, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.groupBoxRasterTypeFilter, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tabRaster, "")
        self.tabConfiguration = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabConfiguration.sizePolicy().hasHeightForWidth())
        self.tabConfiguration.setSizePolicy(sizePolicy)
        self.tabConfiguration.setObjectName("tabConfiguration")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabConfiguration)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tabConfiguration)
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 348, 486))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setContentsMargins(6, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_14.addItem(spacerItem1, 0, 0, 1, 1)
        self.chkGroups = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkGroups.sizePolicy().hasHeightForWidth())
        self.chkGroups.setSizePolicy(sizePolicy)
        self.chkGroups.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chkGroups.setChecked(True)
        self.chkGroups.setObjectName("chkGroups")
        self.gridLayout_14.addWidget(self.chkGroups, 1, 0, 1, 1)
        self.chkLayersOff = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkLayersOff.sizePolicy().hasHeightForWidth())
        self.chkLayersOff.setSizePolicy(sizePolicy)
        self.chkLayersOff.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chkLayersOff.setChecked(True)
        self.chkLayersOff.setObjectName("chkLayersOff")
        self.gridLayout_14.addWidget(self.chkLayersOff, 2, 0, 1, 1)
        self.chkDoNotEmpty = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkDoNotEmpty.sizePolicy().hasHeightForWidth())
        self.chkDoNotEmpty.setSizePolicy(sizePolicy)
        self.chkDoNotEmpty.setChecked(True)
        self.chkDoNotEmpty.setObjectName("chkDoNotEmpty")
        self.gridLayout_14.addWidget(self.chkDoNotEmpty, 3, 0, 1, 1)
        self.chkSort = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkSort.sizePolicy().hasHeightForWidth())
        self.chkSort.setSizePolicy(sizePolicy)
        self.chkSort.setChecked(True)
        self.chkSort.setObjectName("chkSort")
        self.gridLayout_14.addWidget(self.chkSort, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(25, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.chkReverseSort = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkReverseSort.sizePolicy().hasHeightForWidth())
        self.chkReverseSort.setSizePolicy(sizePolicy)
        self.chkReverseSort.setObjectName("chkReverseSort")
        self.horizontalLayout_3.addWidget(self.chkReverseSort)
        self.gridLayout_14.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.chkCaseInsensitive = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkCaseInsensitive.sizePolicy().hasHeightForWidth())
        self.chkCaseInsensitive.setSizePolicy(sizePolicy)
        self.chkCaseInsensitive.setChecked(True)
        self.chkCaseInsensitive.setObjectName("chkCaseInsensitive")
        self.gridLayout_14.addWidget(self.chkCaseInsensitive, 6, 0, 1, 1)
        self.chkAccentInsensitive = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkAccentInsensitive.sizePolicy().hasHeightForWidth())
        self.chkAccentInsensitive.setSizePolicy(sizePolicy)
        self.chkAccentInsensitive.setChecked(False)
        self.chkAccentInsensitive.setObjectName("chkAccentInsensitive")
        self.gridLayout_14.addWidget(self.chkAccentInsensitive, 7, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.chkSearchParentLayer = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkSearchParentLayer.setObjectName("chkSearchParentLayer")
        self.gridLayout_13.addWidget(self.chkSearchParentLayer, 0, 0, 1, 1)
        self.chkAddParentLayerName = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkAddParentLayerName.setChecked(True)
        self.chkAddParentLayerName.setObjectName("chkAddParentLayerName")
        self.gridLayout_13.addWidget(self.chkAddParentLayerName, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_2, 8, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtNumLayersToConfirm = QtWidgets.QLineEdit(self.groupBox)
        self.txtNumLayersToConfirm.setMaximumSize(QtCore.QSize(50, 25))
        self.txtNumLayersToConfirm.setObjectName("txtNumLayersToConfirm")
        self.horizontalLayout_2.addWidget(self.txtNumLayersToConfirm)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox, 10, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_14.addItem(spacerItem3, 11, 0, 1, 1)
        self.chkStyles = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.chkStyles.setObjectName("chkStyles")
        self.gridLayout_14.addWidget(self.chkStyles, 9, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabConfiguration, "")
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tabAbout)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tabAbout)
        self.scrollArea_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_4.setLineWidth(1)
        self.scrollArea_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 358, 486))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem4, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName("label_4")
        self.gridLayout_12.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem5, 2, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem6, 0, 0, 1, 1)
        self.btnHelp = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.btnHelp.setObjectName("btnHelp")
        self.gridLayout_9.addWidget(self.btnHelp, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem7, 0, 2, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_9, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem8, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font:10pt \"Sans Serif\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 5, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem9, 6, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/plugins/loadthemall/logo_80x94.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 8pt \"Sans Serif\";")
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 8pt \"Sans Serif\";")
        self.label_3.setWordWrap(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem12)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 8pt \"Sans Serif\";")
        self.label_7.setWordWrap(True)
        self.label_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.gridLayout_12.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem15, 8, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabAbout, "")
        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.progressBar = QtWidgets.QProgressBar(self.dockWidgetContents)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.btnLoadLayers = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnLoadLayers.setObjectName("btnLoadLayers")
        self.horizontalLayout.addWidget(self.btnLoadLayers)
        self.btnCancel = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.gridLayout_8.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "  Load Them All"))
        self.groupBoxGeometryTypeFilter.setTitle(_translate("DockWidget", "Geometry type filter"))
        self.chkPolygon.setText(_translate("DockWidget", "Polygon"))
        self.chkPoint.setText(_translate("DockWidget", "Point"))
        self.chkLine.setText(_translate("DockWidget", "Line"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVector), _translate("DockWidget", "Vector"))
        self.groupBoxRasterTypeFilter.setTitle(_translate("DockWidget", "Raster type filter"))
        self.chkGray.setText(_translate("DockWidget", "Gray or Undefined"))
        self.chkPalette.setText(_translate("DockWidget", "Palette"))
        self.chkMultiband.setText(_translate("DockWidget", "Multiband"))
        self.chkColorLayer.setText(_translate("DockWidget", "Color Layer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRaster), _translate("DockWidget", "Raster"))
        self.chkGroups.setText(_translate("DockWidget", "Create groups based on directories\' names"))
        self.chkLayersOff.setText(_translate("DockWidget", "Turn off the loaded layers"))
        self.chkDoNotEmpty.setText(_translate("DockWidget", "Do not load empty vector layers "))
        self.chkSort.setText(_translate("DockWidget", "Sort loaded layers by name"))
        self.chkReverseSort.setText(_translate("DockWidget", "Reverse sort order"))
        self.chkCaseInsensitive.setText(_translate("DockWidget", "Ignore case in the alphanumeric filter"))
        self.chkAccentInsensitive.setToolTip(_translate("DockWidget", "This option requires the Python lib \'unidecode\'"))
        self.chkAccentInsensitive.setText(_translate("DockWidget", "Ignore accents in the alphanumeric filter"))
        self.groupBox_2.setTitle(_translate("DockWidget", "SubLayers"))
        self.chkSearchParentLayer.setText(_translate("DockWidget", "Include parent in search"))
        self.chkAddParentLayerName.setText(_translate("DockWidget", "Include parent name in loaded sublayers"))
        self.txtNumLayersToConfirm.setText(_translate("DockWidget", "50"))
        self.label_6.setText(_translate("DockWidget", "Number of layers to show you a confirmation dialog before the load"))
        self.chkStyles.setText(_translate("DockWidget", "Apply styles"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfiguration), _translate("DockWidget", "Configuration"))
        self.label_4.setText(_translate("DockWidget", "The <i>Load Them All</i> plugin allows you to load at the same time a number of layers stored in a directory structure, based on a variety of filters you may customize."))
        self.btnHelp.setText(_translate("DockWidget", "Help"))
        self.label_5.setText(_translate("DockWidget", "<html><head/><body><p>Feel free to report bugs, suggest improvements or say hello at gcarrillo@linuxmail.org or directly at the <a href=\"https://github.com/gacarrillor/loadthemall\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub repository</span></a></p></body></html>"))
        self.label.setText(_translate("DockWidget", "Copyright (C) 2010-2018 Germán Carrillo"))
        self.label_3.setText(_translate("DockWidget", "<i>Licensed under the terms of GNU GPL 2</i>"))
        self.label_7.setText(_translate("DockWidget", "<html><head/><body><p><span style=\" font-style:italic;\">Code contributors:</span><br/><br/>     David Bakeman (v2.1 and v2.4)<br/>     Soeren Gebbert (v2.3)<br/>     Jean Hemmi (V3.0.2 and french translation)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbout), _translate("DockWidget", "About"))
        self.btnLoadLayers.setText(_translate("DockWidget", "Load layers"))
        self.btnCancel.setText(_translate("DockWidget", "Cancel"))

import resources_rc
