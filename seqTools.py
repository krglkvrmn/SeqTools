from Bio.Seq import Seq
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.button import Button
import win32clipboard as wclip
import re

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '100')

def clipboard_content_manager(inst):
	wclip.OpenClipboard()
	seq = wclip.GetClipboardData()
	seq = Seq(re.sub(r'[\d\s]*', '', seq))
	wclip.EmptyClipboard()

	if (inst.text=='Reverse'):
		wclip.SetClipboardText(str(seq[::-1]))
	elif (inst.text=='Complement'):
		wclip.SetClipboardText(str(seq.complement()))
	elif (inst.text=='Reversed\ncomplement'):
		wclip.SetClipboardText(str(seq.reverse_complement()))
	elif (inst.text=='Translate'):
		wclip.SetClipboardText(str(seq.translate()))
	wclip.CloseClipboard()


class SeqToolsApp(App):
	def build(self):
		main = BoxLayout()
		main.add_widget(Button(text='Reverse', on_press=clipboard_content_manager))
		main.add_widget(Button(text='Complement', on_press=clipboard_content_manager))
		main.add_widget(Button(text='Reversed\ncomplement', on_press=clipboard_content_manager))
		main.add_widget(Button(text='Translate', on_press=clipboard_content_manager))
		return main

if __name__ == '__main__':
	SeqToolsApp().run()




