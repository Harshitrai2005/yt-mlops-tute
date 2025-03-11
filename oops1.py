
class employee:

    def __init__(self):
        self.id=123
        self.salary=50000
        self.designation="SDE"
    
    def travel(self,destination):
        print(f"employee is new travelling to {destination}")
        print("employee is travelling")
sam=employee()
print(sam.salary)        

sam.travel("Kerala")



