import pandas as pd

class Employee:
    def __init__(self, HoursWorked, Date):
        self.HoursWorked = HoursWorked
        self.Date = Date
        self.OtRate = 24              #From Data
        self.ST = 0.2                 #20% - Standard Tax 
        self.HT = 0.4                 #40% - Higher Tax   

    def EmpDB(self, EmployeeDB):
        Employee_data = pd.read_csv(EmployeeDB, sep=" ", header=0, index_col=False)
        self.RefID = [RD for RD in Employee_data['StaffID']]
        self.LastName = [LN for LN in Employee_data['LastName']]
        self.FirstName = [FN for FN in Employee_data['FirstName']]
        self.RegHr = [RH for RH in Employee_data['RegHours']]
        self.HourlyRate = [HR for HR in Employee_data['HourlyRate']]
        self.OTM = [OTM for OTM in Employee_data['OTMultiple']]
        self.TaxCredit = [TC for TC in Employee_data['TaxCredit']]
        self.StdBnd = [SB for SB in Employee_data['StandardBand']]

    def TaxCalc(self, StaffID):
        for i in range(len(StaffID)):
            if StaffID[i] == self.RefID[i]:
                overTime = self.HoursWorked[i] - self.RegHr[i]
                overTimePay = overTime * self.OtRate
                RegularRate = self.RegHr[i] * self.HourlyRate[i]
                GrossPay = (self.HourlyRate[i] * self.RegHr[i]) + (overTimePay)
                HighPayBand = GrossPay - self.StdBnd[i]
                StandardTax = self.StdBnd[i] * self.ST
                HighTax = HighPayBand * self.HT
                TotalTax = StandardTax + HighTax
                Name = self.FirstName[i] + self.LastName[i]
                NetDeductions = 74.8
                NetPay = 637.2
                Date = self.Date[i]
                return {'Name': Name, 'Date':Date, 'Regular Hours Worked': self.RegHr[i],
                'Overtime Hours Worked':overTime,'Regular Rate':self.HourlyRate,
                'Overtime Rate':self.OtRate, 'Regular Pay':RegularRate, 'Overtime Pay':overTimePay,
                'Gross Pay':GrossPay, 'Standard Rate Pay':self.StdBnd[i],'Higher Rate Pay':HighPayBand,
                'Standard Tax':StandardTax,'Higher Tax':HighTax, 'Total Tax': TotalTax, 'Tax Credit':self.TaxCredit[i],
                'Net Deductions':NetDeductions, 'Net Pay': NetPay}
            

class main:
    def __init__(self, EmployeeDB, Hours):
        Hours_data = pd.read_csv(Hours, sep=" ", header=0, index_col=False)
        StaffID = [StaffID for StaffID in Hours_data['StaffID']]
        HoursWorked = [HW for HW in Hours_data['HoursWorked']]
        Date = [DA for DA in Hours_data['Date']]
        E = Employee(HoursWorked, Date)
        E.EmpDB(EmployeeDB)
        print(E.TaxCalc(StaffID))

Emp = './DataFiles/Hours.txt'
Reference = './DataFiles/Employees.txt'
a = main(Reference, Emp)
