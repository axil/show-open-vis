#SingleInstance force
#IfWinActive ahk_class LVDChild
^`::
Send ^{Space}
WinWait Quick Drop
Send ^4
return
