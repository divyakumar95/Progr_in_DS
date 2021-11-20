import unittest
import os
import Employee as MainFile

class Test(unittest.TestCase):
    def setUp(self):            #Check to create file 
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

    def tearDown(self):
        os.remove(self.get_file())     #use as a last function to delete the test file

    def test_expect_responce (self):
        Emp = MainFile.Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        comp = Emp.ComputePayment(42,'31/10/2021')
        self.assertIsNotNone(comp, msg="No response from the system")

    def test_verify_responce(self):
        Emp = MainFile.Employee(12346, 'Gi', 'Joe', 33, 17, 1.5, 60, 600)
        comp = Emp.ComputePayment(2,'31/10/2021')
        self.assertDictEqual(comp, 
        {'Date': '31/10/2021',
        'Gross Pay': 34,
        'Higher Rate Pay': 0,
        'Higher Tax': 0.0,
        'Name': 'Joe Gi',
        'Net Deductions': 0,
        'Net Pay': 34,
        'Overtime Hours Worked': 0,
        'Overtime Pay': 0,
        'Overtime Rate': 24,
        'Regular Hours Worked': 2,
        'Regular Pay': 34,
        'Regular Rate': 17,
        'Standard Rate Pay': 600,
        'Standard Tax': 6.8,
        'Tax Credit': 60,
        'Total Tax': 6.8 }, msg="Different message obtained")

    def test_Regular_WorkHr(self):
        Emp = MainFile.Employee(12350, 'Sing', 'Honey', 45, 20, 2, 65, 900)
        comp = Emp.ComputePayment(22,'01/11/2021')
        self.assertEqual(comp['Regular Hours Worked'],22, msg="Regular Hours Worked not exceeding hour worked")

    def test_Negative_Overtime(self):               # Test for Negative Over time 
        Emp = MainFile.Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        comp = Emp.ComputePayment(5,'31/10/2021')
        self.assertGreaterEqual(comp['Overtime Pay'], 0, msg="Value Emp['Overtime Pay'] is not Negative")
    
    def test_Negative_HigherTax(self):              # Test for Negative Over time 
        Emp = MainFile.Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        comp = Emp.ComputePayment(5,'31/10/2021')
        self.assertGreaterEqual(comp['Higher Tax'], 0, msg="Value Emp['Higher Tax'] is not Negative")
    
    def test_check_Pay(self):                       # Test Netpay and GrossPay
        Emp = MainFile.Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        comp= Emp.ComputePayment(2,'31/10/2021')
        self.assertLessEqual(comp['Net Pay'],comp['Gross Pay'], msg="Netpay and GrossPay")

    def test_wrong_ID(self):
        Emp = MainFile.Employee(11111, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        comp = Emp.ComputePayment(60,'03/02/2021')
        self.assertTrue(comp, msg="Wrong Staff ID")  

    def test_negative_NetPay(self):                 #Test Case to Check negative Netpay if Not worked
        Emp = MainFile.Employee(12349, 'Ji', 'Joe', 30, 10, 0, 12, 121)
        comp = Emp.ComputePayment(0,'01/11/2021')
        self.assertEqual(comp['Net Pay'] ,0, msg='Negative Netpay')
        
    def test_Exception_Arg(self):                    #Test case for missing arg
        with self.assertRaises(TypeError):                  
            Emp = MainFile.Employee(12349, 'Ji', 'Joe', 30, 0, 12, 121)
            comp = Emp.ComputePayment(2,'01/11/2021')

if __name__ == '__main__':
    unittest.main()