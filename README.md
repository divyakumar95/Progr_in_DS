# Subject Programming for Data Science 

# Assignment 01 

Create and test a function to compute net pay from payment, work and tax credit information.

-----------------------

Read in a file named Employees.txt, which contains the following information: (space separated)

```bash
<StaffID> <LastName> <FirstName> <RegHours> <HourlyRate> <OTMultiple> <TaxCredit> <StandardBand>

For Example:

12345 Green Joe 37 16 1.5 70 700
```

Create Employee Objects from these 
Read in a file named Hours.txt which contains the following information:

```bash
<StaffID> <Date> <HoursWorked>

12345 31/10/2021 42
```

Create a method computePayment in class Employee which takes HoursWorked and date as input, and returns a payment information dictionary as follows: (if jg is an Employee object for worker Joe Green)

We will assume a standard rate of 20% and a higher rate of 40% (we will ignore PRSI, USC etc.)

```bash
>>>jg.computePayment(42 '31/10/2021')

{'name': 'Joe Green', 'Date':'31/10/2021', 'Regular Hours Worked':37,'Overtime Hours Worked':5,'Regular Rate':16,'Overtime Rate':24, 'Regular Pay':592,'Overtime Pay':120,'Gross Pay':712, 'Standard Rate Pay':700,'Higher Rate Pay':12, 'Standard Tax':140,'Higher Tax':4.8,'Total Tax':144.8,'Tax Credit':70,'Net Deductions':74.8, 'Net Pay': 637.2}
```

Include test cases testing the following:

Net pay cannot exceed gross pay 

# TestMethod

```bash
def testNetLessEqualGross(self):
  e=Employee(#Joe Green's Information)
  pi=e.computePayment(1,'31/10/2021')
  self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])
```

Overtime pay or overtime hours cannot be negative.

Regular Hours Worked cannot exceed hours worked

Higher Tax cannot be negative.

Net Pay cannot be negative.

I would like you to solve for Joe Green

___________________---------------------------------______________________

# Getting started
To get started with the code on this repo, you need to either clone or download this repo into your machine just as shown below;

```bash
git clone https://github.com/divyakumar95/Progr_in_DS.git
```

## Dependencies
Before you begin playing with the source code you might need to install deps just as shown below;

```bash
pip3 install -r requirements.txt
```

## Running the App 

To run this code you need to have your textual document in your project directory with extension .txt and then when you run the script, it will automatically loads all the document with that extension and then compute the similarity between them just as shown below;

```bash
$-> cd /Progr_in_DS
$ /Progr_in_DS -> python3 unitTest.py
```