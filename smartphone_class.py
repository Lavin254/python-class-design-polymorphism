# Base Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"Smartphone: {self.brand} {self.model}, Price: ${self.price}"

# Derived Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gaming_mode):
        super().__init__(brand, model, price)
        self.gaming_mode = gaming_mode  # Unique attribute for GamingSmartphone

    def toggle_gaming_mode(self):
        if self.gaming_mode:
            self.gaming_mode = False
            return "Gaming mode is now OFF."
        else:
            self.gaming_mode = True
            return "Gaming mode is now ON."

# Test the classes
phone = Smartphone("Samsung", "Galaxy S23", 999)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1299, False)

print(phone.display_info())
print(gaming_phone.display_info())
print(gaming_phone.toggle_gaming_mode())
