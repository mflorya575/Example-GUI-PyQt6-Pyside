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

        # apply font
        self.loadProductSansFont()

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

        # Connect theme change signal to change app theme
        self.ui.themeList.currentTextChanged.connect(self.changeAppTheme)

    def populateThemeList(self, current_theme):
        """Populate the list from available app themes"""
        theme_count = 0
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)

            # Check if it's the default theme/current theme
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.themeList.setCurrentIndex(theme_count)  # Select the theme
            theme_count += 1  # Increment the theme count

    # change app theme
    def changeAppTheme(self):
        """Change app theme based on user selection"""
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value('THEME')

        if current_theme != selected_theme:
            # apply new theme
            settings.setValue('THEME', selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    # apply custom font
    def loadProductSansFont(self):
        """Load and apply product sans font"""
        font_id = QFontDatabase.addApplicationFont('../fonts/ProductSans-Regular.ttf')
        # if font loaded
        if font_id == -1:
            print('Failed to load Product Sans font')
            return

        # Apply font
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        if font_family:
            product_sans = QFont(font_family[0])
        else:
            product_sans = QFont('Sans Serif')

        # Apply to main window
        self.main.setFont(product_sans)
