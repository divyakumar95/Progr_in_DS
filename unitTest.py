import unittest
from unittest import result
import Employee as EmployeeClass

class Test(unittest.TestCase):
    def test_expect_responce (self):
        Emp = EmployeeClass.Employee(12345)
        Emp.ComputePayment(42,'31/10/2021')
        #self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])
        self.assertTrue(Emp.ComputePayment(42,'31/10/2021'))

    def test_verify_responce(self):
        Emp = EmployeeClass.Employee(12346)
        Emp.ComputePayment(2,'31/10/2021')
        self.assertEqual(Emp.ComputePayment(2,'31/10/2021'),{'Name': 'Joe Gi', 'Date': '31/10/2021', 'Regular Hours': 35})

if __name__ == '__main__':
    unittest.main()
