import csv
import os
from .core import StudyLog, ExpenseLog

class FileHandler:
    @staticmethod
    def save_logs(file_path, logs):
        try:
            dirname = os.path.dirname(file_path)
            if dirname:
                os.makedirs(dirname, exist_ok=True)
            
            fieldnames = ["Date", "Category", "Description", "Hours/Amount"]
            with open(file_path, mode='w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for log in logs:
                    writer.writerow(log)
        except Exception as e:
            raise

    @staticmethod
    def load_logs(file_path):
        logs = []
        if not os.path.exists(file_path):
            return logs
            
        try:
            with open(file_path, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        row['Hours/Amount'] = float(row['Hours/Amount'])
                        logs.append(row)
                    except ValueError:
                        continue
        except Exception as e:
            pass
        return logs
