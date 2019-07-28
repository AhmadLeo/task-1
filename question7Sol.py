class Charactercout:
    strg = ""
    def function1(self,data):
        if(type(data) == str):
            self.strg = data
        else:
            print("Invalid Data")
    def function2(self):
        return len(self.strg)

obj = Charactercout()
obj.function1(data = "python basics")
print(obj.function2())
