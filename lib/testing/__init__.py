def __init__(self, year, summary, employee_id, id=None):
    self.id = id
    self.year = year  # this triggers the setter below
    self.summary = summary
    self.employee_id = employee_id
