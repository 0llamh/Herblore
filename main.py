#       main.py
#       handles main function and GUI

import PySimpleGUI as ui
import xlsxwriter

import Catalog
import Herb

SEARCH_FILTERS = ['Random', '---USAGE---', 'Potion', 'Poison', 'Drug', '---ENVIRONMENT---', 'Bushes/Shrubs', 'Desert/Wastelands',
                  'Forests/Jungle', 'Fresh Water', 'Grass', 'Mountains/Cliffs', 'Swamp/Marshes', 'Tundra', 'Underground']

ui.theme('Dark Green 3')
layout = [[ui.Text('Generate an herb!')],
          [ui.Text('Roll an Herb'), ui.DropDown(key='filter', values=SEARCH_FILTERS, default_value='Random', readonly=True, enable_events=True), ui.Button('Generate Herb')],
          [ui.Text(size=(30, 1), key="name", font=('Helvetica', 15, 'bold')), ui.Text(size=(15, 1), key="rarity")],
          [ui.Text(size=(60, 4), key="description")],
          [ui.Button('Export', key='export', visible=False)]]
window = ui.Window('Herblore', layout)

def main():
    already_exported = False          # define error checker variable pre-loop
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in 'Generate Herb':
            # check selected value in filter dropdown, enter infinte loop checking selected value against generated herb
            # POTIONS, POISON, DRUG FILTERING
            if 'Potion' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'ailment' in h.use:
                        break
            elif 'Poison' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'poison' in h.use:
                        break
            elif 'Drug' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'drug' in h.use:
                        break
            # ENVIRONMENT FILTERING
            elif 'Bushes/Shrubs' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Bushes' in h.origin:
                        break
            elif 'Desert' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Desert' in h.origin:
                        break
            elif 'Forest' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Forestation' in h.origin:
                        break
            elif 'Fresh Water' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Lakes' in h.origin:
                        break
            elif 'Grass' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Grass' in h.origin:
                        break
            elif 'Mountains/Cliffs' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Mountains' in h.origin:
                        break
            elif 'Swamp/Marshes' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Marshes' in h.origin:
                        break
            elif 'Tundra' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Ice' in h.origin:
                        break
            elif 'Underground' in values['filter']:
                while True:
                    h = Herb.Herb()
                    if 'Underground' in h.origin:
                        break
            # otherwise just roll a random
            else:
                h = Herb.Herb()

            # Display the Generated Herb by updated the UI elements
            window["name"].update(h.name)
            window["rarity"].update("Herb Rarity: %i" % h.rarity)
            # todo: attribute specific descriptions based on texture and origins
            window["description"].update("A " + h.color.lower() + " " + h.type.lower() + " from " + h.origin.lower() + " that is prepared " +
                                         (h.preparation.lower() if h.preparation == 'Raw' else 'by ' + h.preparation.lower()) + " into " +          # syntax checking for 'by' for raw
                                         ('an ' + h.delivery.lower() if h.delivery == 'Oily liquid' else 'a ' + h.delivery.lower()) +               # syntax checking for a/an for oily liquid
                                         " for " + h.use + " " +
                                         ('with ' + h.expiration.lower() if h.expiration == 'No expiration' else 'best if used ' + h.expiration.lower() if h.expiration == 'Immediately' else 'best if used within ' + h.expiration.lower()) + ".")
            window["export"].update(visible=True)       # show the export button after generation
        elif event in 'Export':
            try:
                if already_exported:      # if both last and current events were exports
                    ui.popup_error('Herb already exported. Please generate another.', title='Export Error')
                else:               # otherwise just export like normal
                    Catalog.write(h)
                    already_exported = True  # save what happened this event loop for the next (duplicate export checking)
            except(xlsxwriter.exceptions.FileCreateError):
                ui.popup_error("Spreadsheet currently open in another process. Please close it.", title='Export Error')

    window.close()


if __name__ == "__main__":
    main()
