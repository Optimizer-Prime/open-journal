Open Journal uses PyQt5 for the program GUI. The layout and windows were created in Qt Creator and Designer.

### UI Files

The **.ui** files are included in the source files for future editing under /openjournal/ui. It is recommended that you use Qt Designer for edits to them, unless you are familiar with PyQt, or at least Qt.

After all edits are done, you need to create a **.py** file from the **.ui** file to import into **main.py**. This is done using **pyuic5**, for example.
~~~
$ pyuic5 mainwindow.ui -o MainWindow.py
~~~

Any python files created this way must be imported into the **main.py** file in the proper format.

from openjournal.ui.MainWindow import Ui_MainWindow

### Resource File

Any python file imported into the main file must themselves import the **resources_rc.py** file. It is created with the following command:
~~~
$ pyrrc5 resources.qrc -o resources_rc.py
~~~

At the bottom of all ui python files such as MainWindow.py, it must be imported like this:

import openjournal.ui.resources_rc

Failure to modify the import will result in the program not working correctly, if at all.
