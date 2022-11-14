import matplotlib.pyplot as plt
import PySimpleGUI as sg
import os

'''
    Simple Image Browser 

    This is an early demo program, so perhaps not quite as sophisticated as later ones.

    Copyright 2021 PySimpleGUI
'''


def main():
    # Get the folder containing the images from the user
    folder = 'Graphs'

    # get list of PNG files in folder
    png_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith('.png')]
    filenames_only = [f for f in os.listdir(folder) if f.lower().endswith('.png')]

    # define layout, show and read the window
    col_pict = [[sg.Image(filename=png_files[0], key='-IMAGE-')],
           [sg.Button('Poprzednie', size=(8, 2)), sg.Button('Następne', size=(8, 2)),
            sg.Text('File 1 of {}'.format(len(png_files)), size=(15, 1), key='-FILENUM-'),
            sg.Slider(range=(0, 5000), default_value=1, resolution=1, orientation='h',enable_events = True, key='N_PICT')]]


    layout_pict = [ [sg.Col(col_pict)]]

    window = sg.Window('Image Browser', layout_pict, return_keyboard_events=True, use_default_focus=False)

    # loop reading the user input and displaying image, filename
    filenum, filename = 0, png_files[0]
    while True:

        event, values = window.read()
        # --------------------- Button & Keyboard ---------------------
        if event == sg.WIN_CLOSED:
            break
        elif event in ('Następne') and filenum < len(png_files) - 1:
            filenum += 1
            filename = os.path.join(folder, filenames_only[filenum])
            window['N_PICT'].update(value=filenum)
        elif event in ('Poprzednie') and filenum > 0:
            filenum -= 1
            filename = os.path.join(folder, filenames_only[filenum])
            window['N_PICT'].update(value=filenum)
        elif event == 'Exit':
            break
        elif event == 'N_PICT':
            filenum= int(values['N_PICT'])#int(values.get('N_PICT'))
            filename = os.path.join(folder, filenames_only[filenum])
        # update window with new image
        window['-IMAGE-'].update(filename=filename)
        # update page display
        window['-FILENUM-'].update('File {} of {}'.format(filenum + 1, len(png_files)))

    window.close()


if __name__ == '__main__':
    main()
