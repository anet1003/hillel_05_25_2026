import unittest
from homework_08 import Student
from homework_11 import Numera
from homework_09 import Rhombus


class MyTest(unittest.TestCase):

    def setUp(self):
        self.student =  Student("Anna", "Malko", 18, 100)

    def test_student_creation(self):

        self.assertEqual(self.student.name, "Anna")
        self.assertEqual(self.student.surname, "Malko")
        self.assertEqual(self.student.age, 18)
        self.assertEqual(self.student.rating, 100)

    def test_change_rating(self):
        self.student.change_rating(55)

        self.assertEqual(self.student.rating, 55)

    def test_zero_rating(self):
        self.student.change_rating(0)

        self.assertEqual(self.student.rating, 0)



class TestNumbers(unittest.TestCase):

    def test_sum_numbers(self):
        result = Numera.sum_numbers("1,2,3,4")

        self.assertEqual(result, 10)

    def test_sum_numbers_negative(self):
        self.assertEqual(Numera.sum_numbers("-1,2,3"), 4)

    def test_sum_numbers_invalid(self):
        self.assertEqual(
            Numera.sum_numbers("abc,2,3"),
            "Не можу це зробити!"
        )

    def test_sum_numbers_one_number(self):
        self.assertEqual(Numera.sum_numbers("5"), 5)



    def test_t_rhombus_creation(self):
        rhombus = Rhombus(20, 70)
        self.assertEqual(rhombus.side_a, 20)
        self.assertEqual(rhombus.corner_a, 70)
        self.assertEqual(rhombus.corner_b, 110)

    def test_corner_b_calculation(self):
        rhombus = Rhombus(15, 50)

        self.assertEqual(rhombus.corner_b, 130)

        def test_zero_side(self):
            with self.assertRaises(ValueError):
                Rhombus(0, 70)



if __name__ == "__main__":
    unittest.main()