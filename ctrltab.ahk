#SingleInstance force
#IfWinActive ahk_class LVDChild
^Tab::
Send ^{Space}
WinWait Quick Drop
Send ^4
