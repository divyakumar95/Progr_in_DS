from datetime import date
from logging import error
from typing import List
import pandas as pd

class Employee:
    def __init__(self, StafID=None, EmplDb=None, StaffDb=None):
        self.OtRate = 24              #From Data
        self.ST = 0.2                 #20% - Standard Tax 
        self.HT = 0.4                 #40% - Higher Tax   
        self.StaffID = StafID
        self.EmplDb = EmplDb
        self.StaffDb = StaffDb
        if self.EmplDb is None:      #check for external file source
            self.EmplDb = './DataFiles/Employees.txt'
            try:
                self.Employee_data = pd.read_csv(self.EmplDb, sep=" ", header=0, index_col=False)
            except Exception as Error:
                print('Please fill the table fully if unknown specify 0')
            self.EmpDB()
        if self.StaffID is None and self.StaffDb is None:  #check if no specific Employee
            self.StaffDb = 'DataFiles/Hours.txt'
            Hours_data = pd.read_csv(self.StaffDb, sep=" ", header=0, index_col=False)
            self.HoursWork = [HW for HW in Hours_data['HoursWorked']]
            self.date = [DA for DA in Hours_data['Date']]
            self.StafID = [StaffID for StaffID in Hours_data['StaffID']]
            for i in range(len(self.StafID)):
                self.StaffID = self.StafID[i]
                self.HoursWorked = self.HoursWork[i]
                self.Date = self.date[i]
                print(self.ComputePayment(self.HoursWorked, self.Date))
        
    def EmpDB(self):
        #Employee_data = pd.read_csv(self.EmployeeDB, sep=" ", header=0, index_col=False)
        self.RefID = [RD for RD in self.Employee_data['StaffID']]
        self.LastName = [LN for LN in self.Employee_data['LastName']]
        self.FirstName = [FN for FN in self.Employee_data['FirstName']]
        self.RegHr = [RH for RH in self.Employee_data['RegHours']]
        self.HourlyRate = [HR for HR in self.Employee_data['HourlyRate']]
        self.OTM = [OTM for OTM in self.Employee_data['OTMultiple']]
        self.TaxCredit = [TC for TC in self.Employee_data['TaxCredit']]
        self.StdBnd = [SB for SB in self.Employee_data['StandardBand']]

    def ComputePayment(self, HoursWorked=None , Date=None):  
        self.HoursWorked = HoursWorked
        self.Date = Date
        #print(self.StaffID, self.HoursWorked, self.Date)
        for i in range(len(self.RefID)):
            if self.StaffID == self.RefID[i]:
                if self.HoursWorked > self.RegHr[i]:            # Check for Overtime 
                    overTime = self.HoursWorked - self.RegHr[i]
                else:
                    overTime = 0
                overTimePay = overTime * self.OtRate
                RegularRate = self.RegHr[i] * self.HourlyRate[i]
                GrossPay = (self.HourlyRate[i] * self.RegHr[i]) + (overTimePay)
                if GrossPay > self.StdBnd[i]:                   # Check for High Payment Rate 
                    HighPayBand = GrossPay - self.StdBnd[i]
                else:
                    HighPayBand = 0
                StandardTax = self.StdBnd[i] * self.ST
                HighTax = HighPayBand * self.HT
                TotalTax = StandardTax + HighTax
                Name = self.FirstName[i] +' '+ self.LastName[i]
                NetDeductions = self.TaxCredit[i] + HighTax
                if GrossPay != 0:
                    NetPay = GrossPay - NetDeductions
                else:
                    raise ValueError('Regular hour or hourly rate can not be zero')
                Date = self.Date
                
                return {'Name': Name, 'Date':Date, 'Regular Hours Worked': self.RegHr[i],
                'Overtime Hours Worked':overTime,'Regular Rate':self.HourlyRate[i],
                'Overtime Rate':self.OtRate, 'Regular Pay':RegularRate, 'Overtime Pay':overTimePay,
                'Gross Pay':GrossPay, 'Standard Rate Pay':self.StdBnd[i],'Higher Rate Pay':HighPayBand,
                'Standard Tax':StandardTax,'Higher Tax':round(HighTax,2), 'Total Tax': TotalTax, 'Tax Credit':self.TaxCredit[i],
                'Net Deductions':NetDeductions, 'Net Pay': NetPay}


if __name__ == '__main__':
    Employee()