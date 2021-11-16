import unittest
import os
import Employee as EmployeeClass

class Test(unittest.TestCase):
    def test_create_file(self):
        with open(self.get_file(),'w') as f:
            f.write("""StaffID LastName FirstName RegHours HourlyRate OTMultiple TaxCredit StandardBand
12345 Green Joe 37 16 1.5 70 700
12346 Gi Joe 33 17 1.5 60 600
12350 Sing Honey 45 20 2 65 900
12351 Mark David 37 19 0 90 500
12352 Ali Mohamed 37 19 0 90 500
12349 Ji Joe 30 0 0 12 121""")
    
    def get_file(self): 
        TestDb='./DataFiles/testDb.txt'
        return TestDb

    def test_expect_responce (self):
        Emp = EmployeeClass.Employee(12345,EmplDb=self.get_file())
        Emp = Emp.ComputePayment(42,'31/10/2021')
        self.assertIsNotNone(Emp, msg="No response from the system")

    def test_verify_responce(self):
        Emp = EmployeeClass.Employee(12346,self.get_file())
        Emp = Emp.ComputePayment(2,'31/10/2021')
        self.assertDictEqual(Emp, 
        {'Date': '31/10/2021',
        'Gross Pay': 561,
        'Higher Rate Pay': 0,
        'Higher Tax': 0.0,
        'Name': 'Joe Gi',
        'Net Deductions': 60.0,
        'Net Pay': 501.0,
        'Overtime Hours Worked': 0,
        'Overtime Pay': 0,
        'Overtime Rate': 24,
        'Regular Hours Worked': 33,
        'Regular Pay': 561,
        'Regular Rate': 17,
        'Standard Rate Pay': 600,
        'Standard Tax': 120.0,
        'Tax Credit': 60,
        'Total Tax': 120.0 })

    @unittest.expectedFailure
    def test_Regular_WorkHr(self):
        Emp = EmployeeClass.Employee(12350,EmplDb=self.get_file())
        Emp = Emp.ComputePayment(55,'01/11/2021')
        self.assertLessEqual(Emp['Regular Hours Worked'],55, msg="Regular Hours Worked not exceeding hour worked")

    @unittest.expectedFailure
    def test_Negative_Overtime(self):               # Test for Negative Over time 
        Emp = EmployeeClass.Employee(12345,EmplDb=self.get_file())
        Emp = Emp.ComputePayment(5,'31/10/2021')
        self.assertLess(Emp['Overtime Pay'], 0, msg="Value Emp['Overtime Pay'] is not Negative")
    
    @unittest.expectedFailure
    def test_Negative_HigherTax(self):              # Test for Negative Over time 
        Emp = EmployeeClass.Employee(12345,EmplDb=self.get_file())
        Emp = Emp.ComputePayment(5,'31/10/2021')
        self.assertLess(Emp['Higher Tax'], 0, msg="Value Emp['Higher Tax'] is not Negative")
    
    def test_check_Pay(self):                       # Test Netpay and GrossPay
        Emp = EmployeeClass.Employee(12345,EmplDb=self.get_file())
        Emp= Emp.ComputePayment(2,'31/10/2021')
        self.assertLessEqual(Emp['Net Pay'],Emp['Gross Pay'], msg="Netpay and GrossPay")

    @unittest.expectedFailure
    def test_wrong_ID(self):
        Emp = EmployeeClass.Employee(11111,EmplDb=self.get_file())
        Emp = Emp.ComputePayment(60,'03/02/2021')
        self.assertTrue(Emp, msg="Wrong Staff ID")

    def test_negative_NetPay(self):
        Emp =EmployeeClass.Employee(12349,EmplDb=self.get_file())
        try:
            Emp = Emp.ComputePayment(2,'01/11/2021')
        except ValueError as error:
            self.assertEqual(type(error),ValueError)

    def test_delete(self):                         #use as a last function to delete the test file
        try:
            os.remove(self.get_file())
        except Exception as e:
            print(e)

if __name__ == '__main__':
    unittest.main()
    
