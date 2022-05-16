class File:
    def __init__(self, name):
        self.name = name
        self.contentList = []
        self.orderIDList = []
        self.UNSPSCCodeList = []
        self.priceList = []

    def organizeFile(self):
        with open("amazonReportEW.txt") as self.name:
            contents = self.name.readlines()
            for content in contents:
                self.contentList.append(content.split("  "))

    def writeCleanReport(self):
        for item in self.contentList:
            try:
                self.orderIDList.append(item[1])
                self.UNSPSCCodeList.append(item[5])
                self.priceList.append(item[7])
            except IndexError:
                continue
            
        with open("AmazonCleanedReport.txt", "w") as new:
            for i in range(len(self.orderIDList)):
                new.write(self.orderIDList[i])
                new.write('\t')
                new.write(self.UNSPSCCodeList[i])
                new.write('\t')
                new.write(self.priceList[i])
                new.write('\n')
        new.close()
        
        
            


file1 = File("Amazon") 

file1.organizeFile()
file1.writeCleanReport()