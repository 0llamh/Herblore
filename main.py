#       main.py
#       handles main function and GUI

import xlsxwriter
import kivy
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.base import runTouchApp

import Catalog
import Herb

SEARCH_FILTERS = ['Random', '---USAGE---', 'Potion', 'Poison', 'Drug', '---ENVIRONMENT---', 'Bushes/Shrubs',
                  'Desert/Wastelands',
                  'Forests/Jungle', 'Fresh Water', 'Grass', 'Mountains/Cliffs', 'Swamp/Marshes', 'Tundra',
                  'Underground']


# ui.theme('Dark Green 3')
# layout = [[Text(text='Generate an herb!')],
#           [Text(text='Roll an Herb'), DropDown(key='filter', values=SEARCH_FILTERS, default_value='Random', readonly=True, enable_events=True), Button(text='Generate Herb')],
#           [Text(size=(30, 1), key="name", font=('Helvetica', 15, 'bold')), Text(size=(15, 1), key="rarity")],
#           [Text(size=(60, 4), key="description")],
#           [Button(text='Export', key='export', visible=False)]]
# window = ui.Window('Herblore', layout)

class MainMenu(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add Components
        self.add_widget(Label(text='Generate an herb!'))        # static
        self.add_widget(Label(text='Roll and Herb:'))           # static

        # Dropdown Filter
            # todo: break up filter dropdowns into separate Type vs. Environment
        self.dropdown = DropDown()
        for index in range(0, len(SEARCH_FILTERS)):
            f = Button(text=SEARCH_FILTERS[index], size_hint_y=None, height=20)
            f.bind(on_release=lambda f: self.dropdown.select(f.text))
            self.dropdown.add_widget(f)
        self.generate = Button(text='Generate Herb', size_hint=(None, None))
        self.generate.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.generate, 'text', x))
        runTouchApp(self.generate)

        self.bind(pos=self.update)
        self.bind(size=self.update)
        # self.update()

    def update(self, *args):
        self.canvas.clear()
        with self.canvas:
            background_color = Color(0, 0.38, 0.21, 1)  # color code #02792F
            background = Rectangle(pos=self.pos, size=self.size)


class Herblore(App):
    def build(self):
        return MainMenu()


if __name__ == "__main__":
    Herblore().run()

# already_exported = False          # define error checker variable pre-loop
#         while True:
#             event, values = window.read()
#             if event in (None, 'Exit'):
#                 break
#             elif event in 'Generate Herb':
#                 # check selected value in filter dropdown, enter infinte loop checking selected value against generated herb
#                 # POTIONS, POISON, DRUG FILTERING
#                 if 'Potion' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'ailment' in h.use:
#                             break
#                 elif 'Poison' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'poison' in h.use:
#                             break
#                 elif 'Drug' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'drug' in h.use:
#                             break
#                 # ENVIRONMENT FILTERING
#                 elif 'Bushes/Shrubs' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Bushes' in h.origin:
#                             break
#                 elif 'Desert' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Desert' in h.origin:
#                             break
#                 elif 'Forest' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Forestation' in h.origin:
#                             break
#                 elif 'Fresh Water' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Lakes' in h.origin:
#                             break
#                 elif 'Grass' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Grass' in h.origin:
#                             break
#                 elif 'Mountains/Cliffs' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Mountains' in h.origin:
#                             break
#                 elif 'Swamp/Marshes' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Marshes' in h.origin:
#                             break
#                 elif 'Tundra' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Ice' in h.origin:
#                             break
#                 elif 'Underground' in values['filter']:
#                     while True:
#                         h = Herb.Herb()
#                         if 'Underground' in h.origin:
#                             break
#                 # otherwise just roll a random
#                 else:
#                     h = Herb.Herb()
#
#                 # Display the Generated Herb by updated the UI elements
#                 window["name"].update(h.name)
#                 window["rarity"].update("Herb Rarity: %i" % h.rarity)
#                 # todo: attribute specific descriptions based on texture and origins
#                 window["description"].update("A " + h.color.lower() + " " + h.type.lower() + " from " + h.origin.lower() + " that is prepared " +
#                                              (h.preparation.lower() if h.preparation == 'Raw' else 'by ' + h.preparation.lower()) + " into " +          # syntax checking for 'by' for raw
#                                              ('an ' + h.delivery.lower() if h.delivery == 'Oily liquid' else 'a ' + h.delivery.lower()) +               # syntax checking for a/an for oily liquid
#                                              " for " + h.use + " " +
#                                              ('with ' + h.expiration.lower() if h.expiration == 'No expiration' else 'best if used ' + h.expiration.lower() if h.expiration == 'Immediately' else 'best if used within ' + h.expiration.lower()) + ".")
#                 window["export"].update(visible=True)       # show the export button after generation
#             elif event in 'Export':
#                 try:
#                     if already_exported:      # if both last and current events were exports
#                         ui.popup_error('Herb already exported. Please generate another.', title='Export Error')
#                     else:               # otherwise just export like normal
#                         Catalog.write(h)
#                         already_exported = True  # save what happened this event loop for the next (duplicate export checking)
#                 except(xlsxwriter.exceptions.FileCreateError):
#                     ui.popup_error("Spreadsheet currently open in another process. Please close it.", title='Export Error')
#
#         window.close()
