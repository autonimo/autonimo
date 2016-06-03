

call pyuic4 res\ui\main_view.ui -o views\gen\ui_main_view.py
call pyuic4 res\ui\task_view.ui -o views\gen\ui_task_view.py
call pyuic4 res\ui\component_view.ui -o views\gen\ui_component_view.py



call pyrcc4 res\autonimo.qrc -o autonimo_rc.py

timeout 3