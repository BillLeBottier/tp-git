class calculator:
    def addition(self,a,b):
        result = a+b 
        return result

    def substraction(self,a,b):
        result = a-b
        return result 
    

    def division(self,a,b):
        result = a/b
        return result
    

calculator = calculator()
print(calculator.addition(2,3))
