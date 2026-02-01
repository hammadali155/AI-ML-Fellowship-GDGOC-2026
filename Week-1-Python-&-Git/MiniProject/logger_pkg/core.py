from datetime import datetime

class LogEntry:
    """Base class for all log entries."""
    def __init__(self, date, description):
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "Date": self.date,
            "Description": self.description
        }

class StudyLog(LogEntry):
    """Class representing a study session."""
    def __init__(self, date, description, hours):
        super().__init__(date, description)
        self.category = "Study"
        self.hours = float(hours)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "Category": self.category,
            "Hours/Amount": self.hours
        })
        return data

class ExpenseLog(LogEntry):
    """Class representing a fellowship related expense."""
    def __init__(self, date, description, amount):
        super().__init__(date, description)
        self.category = "Expense"
        self.amount = float(amount)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "Category": self.category,
            "Hours/Amount": self.amount
        })
        return data

class LogTracker:
    """Manager class to handle a collection of logs."""
    def __init__(self):
        self.logs = []

    def add_log(self, entry):
        if not isinstance(entry, LogEntry):
            raise TypeError("Only LogEntry objects can be added.")
        self.logs.append(entry)

    def get_all_logs_as_dicts(self):
        return [log.to_dict() for log in self.logs]

    def clear(self):
        self.logs = []
