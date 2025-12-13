import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import sqlite3

kivy.require('2.0.0')

class FruitShopApp(App):
    def build(self):
        self.conn = sqlite3.connect('inventory.db')
        self.create_table()

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.fruit_name_input = TextInput(hint_text='Fruit Name')
        self.fruit_price_input = TextInput(hint_text='Price')
        self.fruit_quantity_input = TextInput(hint_text='Quantity')
        
        self.add_button = Button(text='Add/Update Fruit')
        self.add_button.bind(on_press=self.add_fruit)

        self.view_button = Button(text='View Inventory')
        self.view_button.bind(on_press=self.view_inventory)

        self.layout.add_widget(self.fruit_name_input)
        self.layout.add_widget(self.fruit_price_input)
        self.layout.add_widget(self.fruit_quantity_input)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.view_button)

        self.output_label = Label(size_hint_y=None, height=44)
        self.layout.add_widget(self.output_label)

        return self.layout

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS fruits (
            name TEXT PRIMARY KEY,
            price REAL,
            quantity INTEGER
        )''')
        self.conn.commit()

    def add_fruit(self, instance):
        name = self.fruit_name_input.text
        price = self.fruit_price_input.text
        quantity = self.fruit_quantity_input.text

        if not name or not price or not quantity:
            self.output_label.text = 'Please fill all fields.'
            return

        try:
            price = float(price)
            quantity = int(quantity)
            cursor = self.conn.cursor()
            cursor.execute('INSERT OR REPLACE INTO fruits (name, price, quantity) VALUES (?, ?, ?)',
                           (name, price, quantity))
            self.conn.commit()
            self.output_label.text = f'{name} added/updated successfully.'
            self.fruit_name_input.text = ''
            self.fruit_price_input.text = ''
            self.fruit_quantity_input.text = ''
        except ValueError:
            self.output_label.text = 'Please enter valid price and quantity.'

    def view_inventory(self, instance):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM fruits')
        fruits = cursor.fetchall()

        if not fruits:
            self.output_label.text = 'Inventory is empty.'
            return
        
        inventory_text = 'Current Inventory:\n'
        for fruit in fruits:
            inventory_text += f'{fruit[0]}: Price = ${fruit[1]:.2f}, Quantity = {fruit[2]}\n'
        self.output_label.text = inventory_text

    def on_stop(self):
        self.conn.close()

if __name__ == '__main__':
    FruitShopApp().run()
