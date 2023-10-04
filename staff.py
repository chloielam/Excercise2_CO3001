from person import Person

class Staff(Person): 
    def __init__(self, name, address, school, pay): 
        super().__init__(name, address)
        self._school = school
        self._pay = pay

    def get_school(self):
        return self._school
    
    def set_school(self, school):
        self._school = school

    def get_pay(self):
        return self._pay
    
    def set_pay(self, pay):
        self._pay = pay
    
    def to_string(self):
            return f"Staff[Person[name={self._name},address={self._address}],school={self._school},pay={self._pay}]"
    