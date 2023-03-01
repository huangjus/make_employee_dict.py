# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/28/23
# Description: takes in four lists of employee data and creates a dictionary of Employee objects,
# where the key is the ID number and the value is the corresponding Employee object.

class Employee:
    def __init__(self, name, id_number, salary, email_address):
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        return self._name

    def get_id_number(self):
        return self._id_number

    def get_salary(self):
        return self._salary

    def get_email_address(self):
        return self._email_address


def make_employee_dict(names, ids, salaries, emails):
    """
    Creates a dictionary of Employee objects based on the input lists of names, IDs, salaries, and email addresses.
    The keys of the dictionary are the ID numbers and the values are the corresponding Employee objects.

    name: List of strings containing employee names.
    ids: List of strings containing employee ID numbers.
    salaries: List of integers containing employee salaries.
    emails: List of strings containing employee email addresses.
    """

    employee_dict = {}
    for i in range(len(ids)):
        employee = Employee(names[i], ids[i], salaries[i], emails[i])
        employee_dict[ids[i]] = employee
    return employee_dict
