from employee import Employee
from department import Department
from review import Review
import pytest


class TestReviewProperties:
    '''Tests for the Review class in review.py'''

    @pytest.fixture(autouse=True)
    def reset_db(self):
        '''Drop and recreate tables before each test.'''
        Review.drop_table()
        Employee.drop_table()
        Department.drop_table()
        Department.create_table()
        Employee.create_table()
        Review.create_table()

    def test_review_valid(self):
        '''Validates that a correct review does not raise an error.'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)

        # Should not raise any exception
        Review.create(
            2023, "Excellent work ethic! Outstanding programming skills!", employee.id
        )

    def test_year_is_int(self):
        '''Raises ValueError if year is not an integer.'''
        with pytest.raises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department.id)

            # Invalid year (not an int)
            Review.create(
                "this century", "Excellent work ethic!", employee.id
            )

    def test_year_value(self):
        '''Raises ValueError if year is before 2000.'''
        with pytest.raises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department.id)

            # Invalid year (< 2000)
            Review.create(
                1999, "Excellent work ethic!", employee.id
            )

    def test_summary_string_length(self):
        '''Raises ValueError if summary is empty.'''
        with pytest.raises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department.id)

            # Invalid summary (empty string)
            Review.create(2023, "", employee.id)

    def test_employee_fk_property_assignment(self):
        '''Raises ValueError if employee_id is not valid.'''
        with pytest.raises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department.id)

            review = Review.create(
                2023, "Excellent work ethic! Outstanding programming skills!", employee.id
            )

            # Invalid employee_id reassignment (simulate non-existent FK)
            review.employee_id = 9999  # assuming 9999 is not a real employee ID
