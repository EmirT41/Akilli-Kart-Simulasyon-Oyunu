import os
import csv

class AccountService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        storage_dir = os.path.join(base_dir, "Storage")
        
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
            
        self.filename = os.path.join(storage_dir, "user.csv")

        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["username", "password"])

    def registerUser(self, userName, password):
        userName = str(userName).strip().lower()
        password = str(password).strip()

        if not (1 < len(userName) < 18):
            return False
        
        if not (password.isdigit() and 4 <= len(password) <= 8):
            return False
        
        if not os.path.exists(self.filename):
            self.__init__()
        
        with open(self.filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            try:
                next(reader)
            except StopIteration:
                pass

            for i in reader:
                if i and len(i) >= 2:
                    if i[0].strip().lower() == userName:
                        return False

        with open(self.filename, "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([userName, password])
            return True

    def logIn(self, userName, password):
        userName = userName.lower().strip()
        password = str(password).strip()

        if not os.path.exists(self.filename):
                    return False

        with open(self.filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for i in reader:
                if i[0] == userName and i[1] == password:
                    return True
                
            return False