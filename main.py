from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class MainApp(App):
   def build(self):
       self.icon = "Calculator.png"
       self.operators = ["÷", "x", "+", "-", "+/-", "%", "mc", "m+", "m-", "mr"]
       self.last_was_operator = None
       self.last_button = None
       main_layout = BoxLayout(orientation="vertical")
       self.solution = TextInput(background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1],
                                 multiline=False, readonly=True, halign="right", font_size=55)
       main_layout.add_widget(self.solution)
       buttons = [
           ["mc", "m+", "m-", "mr"],
           ["C", "←", "+/-", "÷"],
           ["7", "8", "9", "x"],
           ["4", "5", "6", "-"],
           ["1", "2", "3", "+"],
           [".", "0", "=", "%"]
       ]
       for row in buttons:
           h_layout = BoxLayout()
           for label in row:
               button = Button(
                   text=label, font_size=30, background_color=[0.5, 0.5, 0.5, 1],
                   pos_hint={"center_x": 0.5, "center_y": 0.5},
               )
               button.bind(on_press=self.on_button_press)
               h_layout.add_widget(button)
           main_layout.add_widget(h_layout)
       return main_layout
   def on_button_press(self, instance):
       current = self.solution.text
       button_text = instance.text
       if button_text == "C":
           self.solution.text = ""
       elif button_text == "x":
           self.solution.text = current + "*"
        
       elif button_text ==  "÷":
           self.solution.text = current + "/"
           
       elif button_text == "%":
           self.solution.text = current + "/100"
           
       elif button_text == "+/-":
            if "-" in self.solution.text:
                self.solution.text = self.solution.text.replace("-", "")
            else:
                self.solution.text = "-" + self.solution.text   
           
       elif button_text ==  "mc":
           self.solution.text = ""
           
       elif button_text == "m+":
           if hasattr(self, 'memory'):
               self.memory += float(current)
           else:
               self.memory = float(current)
           
       elif button_text == "m-":
           if hasattr(self, 'memory'):
               self.memory -= float(current)
           else:
               self.memory = -float(current)
           
       elif button_text ==  "mr":
           self.solution.text = str(self.memory)
           
        
       elif button_text == "←":
           self.solution.text = current[:-1]
       elif button_text == "=":
           try:
               solution = str(eval(current))
               self.solution.text = solution
           except Exception as e:
               self.solution.text = "Error"
       else:
           if current and (self.last_was_operator and button_text in self.operators):
               return
           elif current == "0" and button_text in self.operators:
               return
           else:
               new_text = current + button_text
               self.solution.text = new_text
       self.last_button = button_text
       self.last_was_operator = self.last_button in self.operators
if __name__ == "__main__":
   app = MainApp()
   app.run()
