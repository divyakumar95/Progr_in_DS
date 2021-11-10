from typing import Dict
import unittest
from unittest import result
import Employee as EmployeeClass

class Test(unittest.TestCase):
    def test_expect_responce (self):
        Emp = EmployeeClass.Employee(12345)
        Emp = Emp.ComputePayment(42,'31/10/2021')
        self.assertIsNotNone(Emp, msg="No response from the system")

    def test_verify_responce(self):
        Emp = EmployeeClass.Employee(12346)
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

    def test_Regular_WorkHr(self):
        Emp = EmployeeClass.Employee(12349)
        Emp = Emp.ComputePayment(55,'01/11/2021')
        self.assertLessEqual(Emp['Regular Hours Worked'],55, msg="Regular Hours Worked not exceeding hour worked")

    @unittest.expectedFailure
    def test_Negative_Overtime(self):               # Test for Negative Over time 
        Emp = EmployeeClass.Employee(12345)
        Emp = Emp.ComputePayment(5,'31/10/2021')
        self.assertLess(Emp['Overtime Pay'], 0, msg="Value Emp['Overtime Pay'] is not Negative")
    
    @unittest.expectedFailure
    def test_Negative_HigherTax(self):              # Test for Negative Over time 
        Emp = EmployeeClass.Employee(12345)
        Emp = Emp.ComputePayment(5,'31/10/2021')
        self.assertLess(Emp['Higher Tax'], 0, msg="Value Emp['Higher Tax'] is not Negative")
    
    def test_check_Pay(self):                       # Test Netpay and GrossPay
        Emp = EmployeeClass.Employee(12345)
        Emp= Emp.ComputePayment(2,'31/10/2021')
        self.assertLessEqual(Emp['Net Pay'],Emp['Gross Pay'], msg="Netpay and GrossPay")

    @unittest.expectedFailure
    def test_wrong_ID(self):
        Emp = EmployeeClass.Employee(11111)
        Emp = Emp.ComputePayment(60,'03/02/2021')
        self.assertTrue(Emp, msg="Wrong Staff ID")

    def test_negative_NetPay(self):
        Emp =EmployeeClass.Employee(12349)
        try:
            Emp = Emp.ComputePayment(2,'01/11/2021')
        except ValueError as error:
            self.assertEqual(type(error),ValueError)

if __name__ == '__main__':
    unittest.main()
