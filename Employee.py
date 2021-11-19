import pandas as pd

class Employee:
    def __init__(self, RefID, LastName, FirstName, RegHr, HourlyRate, OTM, TaxCredit, StdBnd):
        self.RefID = RefID
        self.LastName = LastName
        self.FirstName = FirstName
        self.RegHr = RegHr
        self.HourlyRate = HourlyRate
        self.OTM = OTM
        self.TaxCredit = TaxCredit
        self.StdBnd = StdBnd
        self.OtRate = 24                #From Data
        self.ST = 0.2                   #20% - Standard Tax 
        self.HT = 0.4                   #40% - Higher Tax  

    def ComputePayment(self, HoursWorked=None , Date=None):  
        self.HoursWorked = int(HoursWorked)
        self.Date = Date
        if self.HoursWorked > self.RegHr:                           # Check for Overtime 
            overTime = self.HoursWorked - self.RegHr
            RegHourworked = self.RegHr
        else:
            overTime = 0
            RegHourworked = self.HoursWorked
        overTimePay = overTime * self.OtRate
        RegularRate = self.RegHr * self.HourlyRate
        GrossPay = (self.HourlyRate * self.RegHr) + (overTimePay)
        if GrossPay > self.StdBnd:                                  # Check for High Payment Rate 
            HighPayBand = GrossPay - self.StdBnd
        else:
            HighPayBand = 0
        StandardTax = self.StdBnd * self.ST
        HighTax = HighPayBand * self.HT
        TotalTax = StandardTax + HighTax
        Name = self.FirstName +' '+ self.LastName
        NetDeductions = self.TaxCredit + HighTax
        if GrossPay != 0:
            NetPay = GrossPay - NetDeductions
        else:
            raise ValueError('Regular hour or hourly rate can not be zero')
        Date = self.Date
                
        return {'Name': Name, 'Date':Date, 'Regular Hours Worked': RegHourworked,
                'Overtime Hours Worked':overTime,'Regular Rate':self.HourlyRate,
                'Overtime Rate':self.OtRate, 'Regular Pay':RegularRate, 'Overtime Pay':overTimePay,
                'Gross Pay':GrossPay, 'Standard Rate Pay':self.StdBnd,'Higher Rate Pay':HighPayBand,
                'Standard Tax':round(StandardTax,2),'Higher Tax':round(HighTax,2), 'Total Tax': round(TotalTax,2), 'Tax Credit':self.TaxCredit,
                'Net Deductions':NetDeductions, 'Net Pay': NetPay}

def main(EmplDb=None, StaffDb=None):
    if EmplDb == None and StaffDb is None:                     #check for external file source 
        EmplDb = './DataFiles/Employees.txt'
        StaffDb = './DataFiles/Hours.txt'
        Employee_data = pd.read_csv(EmplDb, sep=" ", header=0, index_col='StaffID')
        Hours_data = pd.read_csv(StaffDb, sep=" ", header=0, index_col='StaffID')
    elif EmplDb != None and StaffDb != None:
        Employee_data = pd.read_csv(EmplDb, sep=" ", header=0, index_col='StaffID')
        Hours_data = pd.read_csv(StaffDb, sep=" ", header=0, index_col='StaffID')
    else:
        raise Exception('Invalid file path or buffer object type')
    for index, row in Hours_data.iterrows():
        x = Employee_data.loc[[index]]
        Emp = Employee(index, x.iloc[0]['LastName'], x.iloc[0]['FirstName'], x.iloc[0]['RegHours'], x.iloc[0]['HourlyRate'], x.iloc[0]['OTMultiple'], x.iloc[0]['TaxCredit'], x.iloc[0]['StandardBand'])
        comp = Emp.ComputePayment(row.HoursWorked,str(row.Date))
        print(comp)

def createFile():
    EmpDB = """StaffID LastName FirstName RegHours HourlyRate OTMultiple TaxCredit StandardBand
12345 Green Joe 37 16 1.5 70 700
12346 Gi Joe 33 17 1.5 60 600
12347 Chi Bing 45 20 2 65 900
12348 Mark Bud 37 19 0 90 500
12349 Ji Joe 30 05 0 12 121"""

    HourDB = """StaffID Date HoursWorked
12345 31/10/2021 42
12348 30/11/2021 20
12345 31/09/2021 05
12349 30/09/2021 30"""

    with open('./DataFiles/Employees.txt','w') as f:
        f.write(EmpDB)

    with open('./DataFiles/Hours.txt','w') as f:
        f.write(HourDB)


if __name__ == '__main__':
    createFile()
    main()