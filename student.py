from person import Person

class Student(Person): 
    def __init__(self, name, address, program, year, fee): 
        super().__init__(name, address)
        self._program = program
        self._year = year
        self._fee = fee

    def get_program(self):
        return self._program
    
    def set_program(self, program):
        self._program = program

    def get_year(self):
        return self._year
    
    def set_year(self, year):
        self._year = year

    def get_fee(self):
        return self._fee
    
    def set_fee(self, fee):
        self._fee = fee
    
    def to_string(self):
            return f"Student[Person[name={self._name},address={self._address}],program={self._program},year={self._year},fee={self._fee}]"
    