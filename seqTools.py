from Bio.Seq import Seq
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.button import Button
import re
import clipboard as clip

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '100')

def clipboard_content_manager(inst):
    seq = clip.paste()
    seq = Seq(re.sub(r'[\d\s]*', '', seq))
    try:
        if (inst.text=='Reverse'):
            clip.copy(str(seq[::-1]))
        elif (inst.text=='Complement'):
            clip.copy(str(seq.complement()))
        elif (inst.text=='Reversed\ncomplement'):
            clip.copy(str(seq.reverse_complement()))
        elif (inst.text=='Translate'):
            clip.copy(str(seq.translate()))
    except Exception as exc:
        print(exc)

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




