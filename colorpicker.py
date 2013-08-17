import sublime, sublime_plugin

sublime_version = 2
if not sublime.version() or int(sublime.version()) > 3000:
	sublime_version = 3

if sublime_version == 2:
	import webcolors
else:
	import SublimeWebColors.webcolors as webcolors

class WebColorsCommand(sublime_plugin.WindowCommand):
	colorList = []
	def __init__(self, *args, **kwargs):
		super(WebColorsCommand, self).__init__(*args, **kwargs)
		colorList = []
		self.generateColorDialog()

	def run(self):
		self.window.show_quick_panel(self.colorList , self.callback)

	def callback(self, index):
		if (index > -1): # No value is -1
			colorValue = self.colorList[index][1]
			self.window.active_view().run_command("insert_web_colors", {"value": colorValue})

	def generateColorDialog(self):
		for name, color in webcolors.css3_names_to_hex.items():
			self.colorList.append([name, color.upper()])


class InsertWebColorsCommand(sublime_plugin.TextCommand):
	def run(self, edit, value):
		for region in self.view.sel():
			self.view.replace(edit, region, value)


class WebColorsCompleteCommand(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		if not view.match_selector(locations[0], 'source.css'):
			return []

		return[(str(x),) * 2 for x in webcolors.css3_names_to_hex]
