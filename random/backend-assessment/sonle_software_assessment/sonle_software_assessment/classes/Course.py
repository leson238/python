"""Import"""
from classes.utilities import read_file
from classes.Test import Test

COURSES_TABLE = read_file('courses')


class Course:
    """Courses data"""

    def __init__(self, course_id):
        self.course_id = str(course_id)
        self._set_course_information()
        self.weights = {}
        self._add_tests()

    def _set_course_information(self):
        for row in COURSES_TABLE:
            if row['id'] == self.course_id:
                self.name = row['name']
                self.teacher = row['teacher']

    def _add_tests(self):
        self.tests = []
        for test_id in Test.TEST_ID:
            if Test(test_id).course_id == self.course_id:
                self.tests.append(Test(test_id))
        self._weight_calibrate()

    def _weight_sum(self):
        """
        Return total weight of course's tests
        """
        s = sum([test.weight for test in self.tests])
        if s != 100:
            raise Exception(
                f"Sum of test weights in {self.name} is not equal to 100")
        return s

    def _weight_calibrate(self):
        """Calibrate test's weight to have the sum of 100"""
        self._weight_sum()
        for test in self.tests:
            self.weights[test.test_id] = round(
                test.weight / 100, 2)

    def __str__(self):
        return f"{self.weights}"
