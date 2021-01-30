class PrintTasks:
    def PrintContent(self,content):
        print(f"Content to be printed : \n{content}")
    
    def TakePhotoCopy(self,content):
        print(f"Content to be photo copied : \n{content}")

    def ScanContent(self, content):
        print(f"Content to be scanned : \n{content}")

class FaxTask:
    def FaxContent(self,content):
        print(f"Content to be faxed : \n{content}")
    

class PrintDuplexTasks:
    def PrintDuplexContent(self,content):
        print(f"Content is printing with duplex Mode : \n {content}")
    
    def StapleContent(self,content):
        print(f"Content will be stapled : \n{content}")

class BasicPrinter(PrintTasks):
    pass

class IntertmediatePrinter(BasicPrinter,FaxTask):
    pass

class AdvancedPrinter(IntertmediatePrinter,PrintDuplexTasks):
    pass

message = "***Practicing interface segregation principle***"
prefix = "Basic Printer Performing : \n"
content = prefix + message

bp = BasicPrinter()
bp.PrintContent(content)
bp.TakePhotoCopy(content)
bp.ScanContent(content)
print("--------------------------------")

message = "***Practicing interface segregation principle***"
prefix = "Intermediate Printer Performing : \n"
content = prefix + message

ip = IntertmediatePrinter()
ip.PrintContent(content)
ip.TakePhotoCopy(content)
ip.ScanContent(content)
ip.FaxContent(content)
print("---------------------------------")

message = "***Practicing interface segregation principle***"
prefix = "Advanced Printer Performing : \n"
content = prefix + message

ap = AdvancedPrinter()
ap.PrintContent(content)
ap.TakePhotoCopy(content)
ap.ScanContent(content)
ap.FaxContent(content)
ap.PrintDuplexContent(content)
ap.StapleContent(content)
print("---------------------------------")