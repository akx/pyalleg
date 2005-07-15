# Graphics modes.
WINDOWED=0
FULLSCREEN=1


# Key modifiers.
SHIFT=0x1
CTRL=0x2
ALT=0x4
LWIN=0x8
RWIN=0x10
MENU=0x20
COMMAND=0x40
SCROLOCK=0x100
NUMLOCK=0x200
CAPSLOCK=0x400
INALTSEQ=0x800
ACCENT1=0x1000
ACCENT2=0x2000
ACCENT3=0x4000
ACCENT4=0x8000

# Keys.
KEY_A=1
KEY_B=2
KEY_C=3
KEY_D=4
KEY_E=5
KEY_F=6
KEY_G=7
KEY_H=8
KEY_I=9
KEY_J=10
KEY_K=11
KEY_L=12
KEY_M=13
KEY_N=14
KEY_O=15
KEY_P=16
KEY_Q=17
KEY_R=18
KEY_S=19
KEY_T=20
KEY_U=21
KEY_V=22
KEY_W=23
KEY_X=24
KEY_Y=25
KEY_Z=26
KEY_0=27
KEY_1=28
KEY_2=29
KEY_3=30
KEY_4=31
KEY_5=32
KEY_6=33
KEY_7=34
KEY_8=35
KEY_9=36
KEY_0_PAD=37
KEY_1_PAD=38
KEY_2_PAD=39
KEY_3_PAD=40
KEY_4_PAD=41
KEY_5_PAD=42
KEY_6_PAD=43
KEY_7_PAD=44
KEY_8_PAD=45
KEY_9_PAD=46
KEY_F1=47
KEY_F2=48
KEY_F3=49
KEY_F4=50
KEY_F5=51
KEY_F6=52
KEY_F7=53
KEY_F8=54
KEY_F9=55
KEY_F10=56
KEY_F11=57
KEY_F12=58
KEY_ESC=59
KEY_TILDE=60
KEY_MINUS=61
KEY_EQUALS=62
KEY_BACKSPACE=63
KEY_TAB=64
KEY_OPENBRACE=65
KEY_CLOSEBRACE=66
KEY_ENTER=67
KEY_COLON=68
KEY_QUOTE=69
KEY_BACKSLASH=70
KEY_BACKSLASH2=71
KEY_COMMA=72
KEY_STOP=73
KEY_SLASH=74
KEY_SPACE=75
KEY_INSERT=76
KEY_DEL=77
KEY_HOME=78
KEY_END=79
KEY_PGUP=80
KEY_PGDN=81
KEY_LEFT=82
KEY_RIGHT=83
KEY_UP=84
KEY_DOWN=85
KEY_SLASH_PAD=86
KEY_ASTERISK=87
KEY_MINUS_PAD=88
KEY_PLUS_PAD=89
KEY_DEL_PAD=90
KEY_ENTER_PAD=91
KEY_PRTSCR=92
KEY_PAUSE=93
KEY_ABNT_C1=94
KEY_YEN=95
KEY_KANA=96
KEY_CONVERT=97
KEY_NOCONVERT=98
KEY_AT=99
KEY_CIRCUMFLEX=100
KEY_COLON2=101
KEY_KANJI=102
KEY_EQUALS_PAD=103
KEY_BACKQUOTE=104
KEY_SEMICOLON=105
KEY_COMMAND=106
KEY_UNKNOWN1=107
KEY_UNKNOWN2=108
KEY_UNKNOWN3=109
KEY_UNKNOWN4=110
KEY_UNKNOWN5=111
KEY_UNKNOWN6=112
KEY_UNKNOWN7=113
KEY_UNKNOWN8=114
KEY_MODIFIERS=115
KEY_LSHIFT=115
KEY_RSHIFT=116
KEY_LCONTROL=117
KEY_RCONTROL=118
KEY_ALT=119
KEY_ALTGR=120
KEY_LWIN=121
KEY_RWIN=122
KEY_MENU=123
KEY_SCRLOCK=124
KEY_NUMLOCK=125
KEY_CAPSLOCK=126
KEY_MAX=127

keyNames=[	"Foobar!", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
		"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
		"Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
		"0 Pad", "1 Pad", "2 Pad", "3 Pad", "4 Pad", "5 Pad", "6 Pad",
		"7 Pad", "8 Pad", "9 Pad", "F1", "F2", "F3", "F4", "F5", "F6",
		"F7", "F8", "F9", "F10", "F11", "F12", "Esc", "Tilde", "Minus",
		"Equals", "Backspace", "Tab", "Open Brace", "Close Brace", "Enter",
		"Colon", "Quote", "Backslash", "Backslash 2", "Comma", "Stop", "Slash",
		"Space", "Insert", "Del", "Home", "End", "Pgup", "Pgdn", "Left",
		"Right", "Up", "Down", "Slash Pad", "Asterisk", "Minus Pad",
		"Plus Pad", "Del Pad", "Enter Pad", "Print Screen", "Pause", "Abnt C1",
		"Yen", "Kana", "Convert", "No Convert", "At", "Circumflex", "Colon 2",
		"Kanji", "Equals Pad", "Backquote", "Semicolon", "Command",
		"Unknown1", "Unknown2", "Unknown3", "Unknown4", "Unknown5",
		"Unknown6", "Unknown7", "Unknown8", "Modifiers", "Lshift", "Rshift",
		"Lcontrol", "Rcontrol", "Alt", "Altgr", "Lwin", "Rwin", "Menu",
		"Scrlock", "Numlock", "Capslock", "Max"
	]
	
# Sprites.
NORMAL=0
VFLIP=XFLIP=1
HFLIP=YFLIP=2
VHFLIP=XYFLIP=HVFLIP=3

# Draw modes.
SOLID=0
XOR=1
COPY_PATTERN=2
SOLID_PATTERN=3
MASKED_PATTERN=4
TRANS=5

# Font drawing.
LEFT=0
CENTER=1
RIGHT=2

blenders=[	"alpha",	# Transparency by alpha channel.
		"walpha",	# Alpha written, as well.
		"trans",	# Classic transparency. d=d*(255-a)+s*a
		"add",		# d=d+s - useful for flares, fire, etc
		"burn",
		"color",
		"diff",
		"dissolve",
		"dodge",
		"hue",
		"invert",
		"lumi",
		"mult",		# d=d*s - useful for many things
		"sat",
		"screen"
	]