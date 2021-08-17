import os
from kivy.uix.popup import Popup
import kivy.uix.widget
from kivy.app import App                                 #importing framework
from kivy.logger import Logger
from database import select_all_tasks                    #importing database
#kivy.require("1.10.1")
from kivy.uix.floatlayout import FloatLayout             #selecting which layout to use
from kivy.uix.screenmanager import ScreenManager,Screen  #for switching screen
import database
import around_you
from kivy.uix.boxlayout import BoxLayout                 #importing boxLayout
from kivy.properties import  ObjectProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
#from jnius import autoclass
#from android.runnable import run_on_ui_thread
from kivy.lang import Builder
from kivy.utils import platform

from kivy.lang import Builder
from kivy.uix.actionbar import ActionBar                 #action bar on then top of screen
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import StringProperty               #importing StringProperty to pass variables between classes
class FirstScreen(Screen):                               #first screen - mainmenu
    pass
class SecondScreen(Screen):                       
    pass

class ThirdScreen(Screen):
   #id = find_id(conn=,ward_data=,district_data=,beat_data=,community_area_data=,primary_type_data=,location_description_data=)
   #text = root.ids.input.text
   #print(text)
   ward = ObjectProperty(None)                           #Declaring as objectproperty to get value from .kv file
   district = ObjectProperty(None)
   resultt = ObjectProperty(None)
   beat = ObjectProperty(None)
   community_area = ObjectProperty(None)
   primary_type = ObjectProperty(None)
   location = ObjectProperty(None)
   def btn(self):                                        #function to get the values from .kv 
       x = database.find_id(self.ward.text, self.district.text,self.beat.text, self.community_area.text, self.primary_type.text,
               self.location.text)
       self.resultt.text ="Possible Suspect Ids are: \n 1) " + str(x[0][1]) + "\n 2) " + str(x[1][1]) + "\n 3) " + str(x[2][1]) + "\n 4) " + str(x[3][1]) + "\n 5) " + str(x[4][1])

class FourthScreen(Screen):
    report = ObjectProperty(None)
    report_file = ObjectProperty(None)
    def btn1(self):
        app_folder = os.path.dirname(os.path.abspath(__file__))               #setting the file's location in os path
        #app_folder = "C:\\text.txt"
        file_obj = open(app_folder, 'w')
        file_obj.write(
            self.report.text                                                  #writing from text input in the .kv
        )
        file_obj.close()
        self.report_file.text = "Succesfully reported"                         #if file has been written succesfully
class FifthScreen(Screen):
    pass
class SixthScreen(Screen):
    ward1 = ObjectProperty(None)
    district1 = ObjectProperty(None)
    beat1 = ObjectProperty(None)
    community_area1 = ObjectProperty(None)
    ress = ObjectProperty(None)

    def btn2(self):
        b = around_you.find_id(self.ward1.text, self.district1.text, self.beat1.text, self.community_area1.text)
        self.ress.text = "Possible Suspect Ids are: \n 1) " + str(b[0][1]) + "\n 2) " + str(
            b[1][1]) + "\n 3) " + str(b[2][1]) + "\n 4) " + str(b[3][1]) + "\n 5) " + str(b[4][1])

class MyScreenManager(ScreenManager):                                        #MyScreenManager has been used to manage all the screens
    pass
class Mainmenu(App):
    def build(self):
        return MyScreenManager()                                              #returning MysScreenManager to get all the screens too

if __name__ == "__main__":
    Mainmenu().run()
