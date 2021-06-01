import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

a=[]

class MainApp(App):
    def build(self):
        layout=GridLayout(cols=2)
        self.PName=TextInput(text="Enter Patient's Name")
        self.DName=TextInput(text="Enter Doctor's Name")
        submit=Button(text="Submit", on_release=self.submit)
        layout.add_widget(self.PName)
        layout.add_widget(self.DName)
        layout.add_widget(submit)
        
        
        return layout
    def submit (self,obj):
        print("Patient's Name: " + self.PName.text)
        print("Doctor's Name: " + self.DName.text)

        a.append(self.PName.text) 
        a.append(self.DName.text)
        
        with open('data.txt', 'a') as data:
            for i in a:
                 data.write(str(i) + '\n')
if __name__ == "__main__":
    MainApp().run()