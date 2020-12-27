class Test:
    staticVariable = 0
    instanceVariable = 0

    def __init__(self):
        print("Wait a moment..We are constructing the test...**")
        self.instanceVariable +=1
        Test.staticVariable +=1
    
t1 = Test()
print("After creating First Object :")
print("Instance Varible :", t1.instanceVariable)
print("Static Variable :", t1.staticVariable)

t2 = Test()
print("After creating Second Object :")
print("Instance Varible :", t2.instanceVariable)
print("Static Variable :", t2.staticVariable)