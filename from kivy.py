from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.uix.recycleview import RecycleView
import random

# Sample data (you can replace this with your own data)
data = [{'Name': 'Alice', 'Age': 30, 'Country': 'USA'},
        {'Name': 'Bob', 'Age': 25, 'Country': 'Canada'},
        {'Name': 'Charlie', 'Age': 35, 'Country': 'UK'}]

class DataGridItem(BoxLayout):
    orientation = 'horizontal'
    cols = 4  # Number of columns

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        for key, value in data.items():
            self.add_widget(Label(text=f"{key}: {value}"))

class DataGrid(RecycleView):
    data_items = ListProperty([])

class DataGridApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=10)  # Use a GridLayout for the root layout

        # Create a label to display the selected item
        self.selected_item_label = Label(text="Selected item will appear here")
        layout.add_widget(self.selected_item_label)

        # Create a data grid view (RecycleView)
        data_grid = DataGrid()
        data_grid.data_items = data
        layout.add_widget(data_grid)

        # Create a box layout for the buttons to align them vertically
        button_layout = BoxLayout(orientation='vertical', size_hint=(None, None), width=150)

        # Create buttons and add them to the button_layout
        button1 = Button(text="Add", on_press=self.button1_action, size_hint_y=None, height=80)
        button2 = Button(text="All time", on_press=self.button2_action, size_hint_y=None, height=80)
        button3 = Button(text="Close", on_press=self.button3_action, size_hint_y=None, height=80)
        button4 = Button(text="Save", on_press=self.button4_action, size_hint_y=None, height=80)
        button5 = Button(text="Delete", on_press=self.button5_action, size_hint_y=None, height=80)
        button6 = Button(text="Associate Report", on_press=self.button6_action, size_hint_y=None, height=80)
        button7 = Button(text="Leave Report", on_press=self.button7_action, size_hint_y=None, height=80)
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        button_layout.add_widget(button4)
        button_layout.add_widget(button5)
        button_layout.add_widget(button6)
        button_layout.add_widget(button7)

        # Add the button_layout to the root layout
        layout.add_widget(button_layout)

        return layout

    def button1_action(self, instance):
        self.selected_item_label.text = "Button 1 clicked"

    def button2_action(self, instance):
        self.selected_item_label.text = "Button 2 clicked"

    def button3_action(self, instance):
        self.selected_item_label.text = "Button 3 clicked"
    
    def button4_action(self, instance):
        self.selected_item_label.text = "Button 4 clicked"
        
    def button5_action(self, instance):
        self.selected_item_label.text = "Button 5 clicked"
        
    def button6_action(self, instance):
        self.selected_item_label.text = "Button 6 clicked"
        
    def button7_action(self, instance):
        self.selected_item_label.text = "Button 7 clicked"

if __name__ == '__main__':
    DataGridApp().run()
