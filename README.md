Subject Programming for Data Science 

* Assignment 01 

Create and test a function to compute net pay from payment, work and tax credit information.

-----------------------

Read in a file named Employees.txt, which contains the following information: (space separated)

<StaffID> <LastName> <FirstName> <RegHours> <HourlyRate> <OTMultiple> <TaxCredit> <StandardBand>

For Example:

12345 Green Joe 37 16 1.5 70 700

Create Employee Objects from these 
Read in a file named Hours.txt which contains the following information:

<StaffID> <Date> <HoursWorked>

12345 31/10/2021 42

Create a method computePayment in class Employee which takes HoursWorked and date as input, and returns a payment information dictionary as follows: (if jg is an Employee object for worker Joe Green)

We will assume a standard rate of 20% and a higher rate of 40% (we will ignore PRSI, USC etc.)

>>>jg.computePayment(42 '31/10/2021')

{'name': 'Joe Green', 'Date':'31/10/2021', 'Regular Hours Worked':37,'Overtime Hours Worked':5,'Regular Rate':16,'Overtime Rate':24, 'Regular Pay':592,'Overtime Pay':120,'Gross Pay':712, 'Standard Rate Pay':700,'Higher Rate Pay':12, 'Standard Tax':140,'Higher Tax':4.8,'Total Tax':144.8,'Tax Credit':70,'Net Deductions':74.8, 'Net Pay': 637.2}

Include test cases testing the following:

Net pay cannot exceed gross pay 

#TestMethod

def testNetLessEqualGross(self):
  e=Employee(#Joe Green's Information)
  pi=e.computePayment(1,'31/10/2021')
  self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])

Overtime pay or overtime hours cannot be negative.

Regular Hours Worked cannot exceed hours worked

Higher Tax cannot be negative.

Net Pay cannot be negative.

I would like you to solve for Joe Green