#       main.py
#       handles main function and GUI

import PySimpleGUI as ui
import xlsxwriter

import Catalog
import Herb

ui.theme('Dark Green 3')
layout = [[ui.Text('Generate an herb!')],
          [ui.Button('Roll a Random Herb'), ui.Button('Export')],
          [ui.Text(size=(30, 1), key="name", font=('Helvetica', 15, 'bold')), ui.Text(size=(15, 1), key="rarity")],
          [ui.Text(size=(60, 4), key="description")]]
window = ui.Window('Herblore', layout)


def main():
    lastevent = ''          # define error checker variable pre-loop
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in 'Roll a Random Herb':
            h = Herb.Herb()
            window["name"].update(h.name)
            window["rarity"].update("Herb Rarity: %i" % h.rarity)
            # todo: attribute specific descriptions based on texture and origins
            window["description"].update("A " + h.color.lower() + " " + h.type.lower() + " from " + h.origin.lower() + " that is prepared " +
                                         (h.preparation.lower() if h.preparation == 'Raw' else 'by ' + h.preparation.lower()) + " into " +          # syntax checking for 'by' for raw
                                         ('an ' + h.delivery.lower() if h.delivery == 'Oily liquid' else 'a ' + h.delivery.lower()) +               # syntax checking for a/an for oily liquid
                                         " for " + h.use + " " +
                                         ('with ' + h.expiration.lower() if h.expiration == 'No expiration' else 'best if used ' + h.expiration.lower() if h.expiration == 'Immediately' else 'best if used within ' + h.expiration.lower()) + ".")
        # todo: generate herb with filters
            # same as roll a random herb, but loops infinitely when a check on attributes selected in a drop-down
        elif event in 'Export':
            try:
                if lastevent == event:      # if both last and current events were exports
                    ui.popup_error('Herb already exported. Please generate another.', title='Export Error')
                else:               # otherwise just export like normal
                    Catalog.write(h)
            except(UnboundLocalError):
                ui.popup_error('Generate an herb before exporting', title='Export Error')
            except(xlsxwriter.exceptions.FileCreateError):
                ui.popup_error("Spreadsheet currently open in another process. Please close it.", title='Export Error')
        lastevent = event           # save what happened this event loop for the next (duplicate export checking)

    window.close()


if __name__ == "__main__":
    main()
