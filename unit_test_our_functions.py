import unittest

import our_functions

class test_is_valid_date(unittest.TestCase):
    def test_correct_date_format(self):
        date_str = "2023-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)

    def test_incorrect_date_format(self):
        date_str = "03-12-2023"
        res = our_functions.is_valid_date("date_str")
        self.assertEqual(res, False)
        
    def test_incorrect_second_month(self):
        date_str = "2024-02-30"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
        
    def test_correct_second_month(self):
        date_str = "1999-02-28"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)
        
    def test_incorrect_day(self):
        date_str = "2005-01-00"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
        
    def test_correct_leap_date(self):
        date_str = "2000-02-29"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)
        
    def test_incorrect_month_range_1(self):
        date_str= "2000-00-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
        
    def test_incorrect_month_range_2(self):
        date_str = "2000-13-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
        
    def test_incorrect_int_day(self):
        date_str = "2000-01-xx"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
        
    def test_incorrect_int_month(self):
        date_str = "2000-xx-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
        
    def test_incorrect_int_year(self):
        date_str = "20xx-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
        
    def test_correct_year_inrange(self):
        date_str = "1001-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)
    
    def test_incorrect_year_inrange(self):
        date_str = "0000-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
        

class test_is_valid_username(unittest.TestCase):
    def test_username_more_than_min(self):
        username_str = "myname"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_username_equal_min(self):
        username_str = "myname"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)
        
    def test_username_blank(self):
        username_str = None
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)
        
    def test_username_less_than_min(self):
        username_str = "mynam"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)
        
    def test_minlen_less_than_one(self):
        username_str = "myname"
        min_username_chars = 0
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

    def test_username_requirements(self):
        self.test_username_match_requirement_1()
        self.test_username_match_requirement_2()

    def test_username_match_requirement_1(self):
        username_str = "hello#"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)
        
    def test_username_match_requirement_2(self):
        username_str = "<alert>hi</alert>"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)
        
    def test_username_begin_with_number(self):
        username_str = "0alphabet"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

if __name__ == "__main__":
    unittest.main()