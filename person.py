
class Person(object): 
    def __init__(self, name, address):
        self._name = name
        self._address = address
    
    def get_name(self):
        return self._name
    
    def get_address(self):
        return self._address 
    
    def set_address(self, address):
        self._address = address

    def to_string(self): 
        return f"Person[name={self._name}, address={self._address}]"

    