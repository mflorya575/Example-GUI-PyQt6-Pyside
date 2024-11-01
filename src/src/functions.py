# GUI functions
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader
from Custom_Widgets.Qss.colorsystem import settings

from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow
        self.ui = MainWindow.ui

        # init app theme
        self.initializeAppTheme()

    # initialize app theme
    def initializeAppTheme(self):
        """Initialize the application theme from settings"""
        settings = QSettings()
        current_theme = settings.value('THEME')
        # print('Current theme is', current_theme)

        # Add theme to the theme list
        self.populateThemeList(current_theme)

    def populateThemeList(self, current_theme):
        """Populate the list from available app themes"""
        theme_count = -1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)
            # check default theme/current theme
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.themeList.setCurrentIndex(theme_count)  # select the theme
