# SublimeWebColors
SublimeWebColors is a plugin for the growing popular editor [Sublime Text](http://www.sublimetext.com). It simply lists all CSS3 color names `indigo, gold, firebrick` etc and expands them to their representing hex codes; `#4B0082, #FFD700, #B22222`.

SublimeWebColors will also append all CSS3 color names such `indigo, gold, firebrick` into the query suggestions list.

## Compatibility
I originally wrote this plugin for Sublime Text 2, however changes have been made to bring compatibility to ST3, however it is possible that backwards compatibility is now broken. If so, file a bug report or send a pull request.

## Installation
Clone this directory to your Sublime Text `/Packages` directory. Boom. I'll get it in the Package Control directory as soon as I can.

## Usage
Completions will only be displayed when the cursor is under a CSS scope. This is currently static, however I plan on adding a way to add scopes via a configuration file.

- Windows: The default binding is set to `ctrl+shift+u`
- Linux: The default binding is set to `ctrl+shift+u`
- OSX: The default binding is set to `super+shift+u`

You can change these by overwriting the appropriate `*.sublime-keymap`

## Credit
`webcolors.py` is a Python library developed by James Bennett, see [BitBucket](https://bitbucket.org/ubernostrum/webcolors/) for his code.

## License
MIT - [http://jbrooksuk.mit-license.org](http://jbrooksuk.mit-license.org)