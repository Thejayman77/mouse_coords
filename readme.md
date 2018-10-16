mouse_track.py - A utility for graphically displaying the mouse cursor positions on the screen in X/Y coordinates.
This has been tested with two monitors, but may be problematic outside of that.  It did work well under that capacity.

Very useful for determining where to programatically move your move cursor when creating automation scripts.

-----------------------------------------------------------------------------------------------------------------------------

coords_gui.py - This is the actual GUI class created through the QT Designer.  I've imported it in mouse_track as a library
to keep the code clean and separate from the gui spaghetti.

-----------------------------------------------------------------------------------------------------------------------------

coords.ui - Original designer file.  You can load this up, modify it (Being sure not to break existing linkage), and then use
pyuic5 to convert it back over to coords_gui.py.