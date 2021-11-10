import unittest
from unittest import result
import Employee as EmployeeClass

class Test(unittest.TestCase):
    def test_01 (self):
        Emp = EmployeeClass.Employee(12345)
        Emp.ComputePayment(42,31/10/2021)

if __name__ == '__main__':
    unittest.main()
