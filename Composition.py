class Persona:
    def __init__(self, name, PIN, sold) -> None:
        self.name=name
        self.PIN=PIN
        self.sold=sold
        self.contract={}
        
    def add_contract(self, number_contract :str, type_of_contract :str, salary:int):
        self.contract[number_contract]={type_of_contract: salary}
        
    def read_contract(self):
        print(self.contract)
        return f"Contract: {self.contract}"
    
    def resignation(self, number_contract: str):
        for key, values in self.contract.copy().items():
            if key == number_contract:
                del self.contract[key]
                print("Resignation accepted.")
            
            else:
                print("There is no contract.")
                
    def collect_salary(self, number_contract: str, type_of_contract : str):
        salary=self.contract[number_contract][type_of_contract]
        self.sold+=salary
        
    def show_balance(self):
        print(f"Balance: {self.sold} ")
        

class Banca:
    def __init__(self, name_bank, founds, registration_code) -> None:
        self.name_bank=name_bank
        self.founds=founds
        self.rc=registration_code
        self.founded_contract={}
        
    def loan_money(self, client: Persona, salary, type_of_contract, amount_borrowed, salary_necesary=2000):
        for key, values in client.contract.items():
            if salary >=salary_necesary and type_of_contract == "Indeterminated":
                self.founded_contract[key]=values
                salary=self.founded_contract[key]["Indeterminated"]
                found_after_loan=self.founds-amount_borrowed
                self.founds=found_after_loan
                client.sold += amount_borrowed
                print("Loan accepted.")
                print(client.sold)
        else:
            print("Salary is to small or the contract is not indeteminated")

            
    def show_founds(self):
        print(f"Fonduri disponibile: {self.founds}")
            
        
        
            
            
            

 
person=Persona(name=input("Name: "), PIN=input("PIN:"), sold=100)
bank=Banca(name_bank="BT", founds=100000000, registration_code="164")
person.add_contract(number_contract="15/21.04.2024", type_of_contract="determinated", salary=2000)
person.read_contract()
person.collect_salary(number_contract="15/21.04.2024", type_of_contract="determinated")
person.show_balance()
person.resignation(number_contract="15/21.04.2024")
bank.loan_money(person, 2000, "Indeterminated", 300, 2000)
bank.show_founds()



