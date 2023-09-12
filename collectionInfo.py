
from sample import Sample

import threading
from time import time, ctime, localtime, strftime


class SaveInfo (threading.Thread):
        
    def __init__(self, character:Sample):
        super().__init__()
        self.name = f"{character.name} {ctime(time())}".replace(":", "-")
        self.character = character
        self.path = f"battleReports/{self.name}.md"


        self.creatingReport()


    def creatingReport(self):
        #создание файла для отчета
        report_file = open(self.path, "w")
        report_file.write(f"{self.name} {type(self.character)}")
        report_file.close()


    def recordReport(self, report:str):
        #запись данных в файл
        report_file = open(self.path, "a")
        line = "----------------------------"
        time_report = strftime("%H:%M:%S", localtime())
        report_str = f"{line}\n{time_report}{report}{line}"
        
        report_file.write(report_str)
        report_file.close()
    
    def run(self, report:str):
        self.recordReport(report)


