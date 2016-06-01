

call pyuic4 res\ui\autonimo_main_window.ui -o views\gen\ui_autonimo_main_window.py
call pyuic4 res\ui\task_widget.ui -o views\gen\ui_task_widget.py



call pyrcc4 res\autonimo.qrc -o autonimo_rc.py

timeout 3