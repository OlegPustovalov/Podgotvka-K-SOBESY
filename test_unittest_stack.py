import unittest
import stack160922

class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")
        
    def tearDown(self):
        print("method tearDown")
        
    def test_stack_1(self):
        print('test1')
        str1 = '(((([{}]))))'
        result = stack160922.balance_str(str1)
        self.assertEqual(result,'Cбалансированно')
    
    def test_stack_2(self):
        print('test2')
        str1 = '[([])((([[[]]])))]'
        result = stack160922.balance_str(str1)
        self.assertEqual(result,'Cбалансированно')
    
    def test_stack_3(self):
        print('test3')
        str1 = '{{[()]}}'
        result = stack160922.balance_str(str1)
        self.assertEqual(result,'Cбалансированно')  
           
    def test_stack_4(self):
        print('test4')
        str1 = '[[{())}]'
        result = stack160922.balance_str(str1)
        self.assertEqual(result,'Несбалансированно')  
     
    def test_stack_5(self):
        print('test5')
        str1 = '{{[(])]}}'
        result = stack160922.balance_str(str1)
        self.assertEqual(result,'Несбалансированно')
    
    def test_stack_6(self):
        print('test6')
        str1 = '}{}'
        result = stack160922.balance_str(str1)
        self.assertEqual(result,'Несбалансированно')

if __name__ == '__main__':
    unittest.main()
    
