# SublimeWebColors
SublimeWebColors is a plugin for the growing popular editor [Sublime Text](http://www.sublimetext.com). It simply lists all CSS3 color names `indigo, gold, firebrick` etc and expands them to their representing hex codes; `#4B0082, #FFD700, #B22222`.

SublimeWebColors also appends all CSS3 color names such `indigo, gold, firebrick` into the query suggestions list.

## Compatibility
This plugin is fully compatible with Sublime Text 2 and 3!

## Installation
Easiest way is to install via [Package Control](https://sublime.wbond.net/installation), just search for "SublimeWebColors".

If you don't have Package Control (which you should do, it's amazing) then you can use Git. Just clone this directory to your Sublime Text `/Packages` directory.

## Usage
Completions will only be displayed when the cursor is under a CSS scope. This is currently static, however I plan on adding a way to add scopes via a configuration file.

- Windows: The default binding is set to <kbd>ctrl+shift+u</kbd>
- Linux: The default binding is set to <kbd>ctrl+shift+u</kbd>
- OSX: The default binding is set to <kbd>super+shift+u</kbd>

You can change these by overwriting the appropriate `*.sublime-keymap`

## Credit
`webcolors.py` is a Python library developed by James Bennett, see [BitBucket](https://bitbucket.org/ubernostrum/webcolors/) for his code.

## License
MIT - [http://jbrooksuk.mit-license.org](http://jbrooksuk.mit-license.org)