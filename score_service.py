import os
import csv

class ScoreService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        storage_dir = os.path.join(base_dir, "Storage")

        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

        self.filename = os.path.join(storage_dir, "scores.csv")

        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["username", "difficulty", "score"])

    def addScore(self, userName, difficulty, score):
        userName = userName.lower().strip()
        difficulty = difficulty.lower().strip()
        new_score = int(score)
        
        all_data = []
        found = False
        updated = False

        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row and len(row) >= 3:
                        if row[0] == userName:
                            found = True
                            if new_score > int(row[2]):
                                all_data.append([userName, difficulty, new_score])
                                updated = True
                            else:
                                all_data.append(row)
                        else:
                            all_data.append(row)

        if not found:
            all_data.append([userName, difficulty, new_score])
            updated = True

        if updated:
            with open(self.filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["username", "difficulty", "score"])
                writer.writerows(all_data)
            return True
        
        return False

    def getLeaderboard(self):

        scores = []
        if not os.path.exists(self.filename):
            return scores

        with open(self.filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                scores.append({
                    "username": row["username"],
                    "difficulty": row["difficulty"],
                    "score": int(row["score"])
                })

        return sorted(scores, key=lambda x: x['score'], reverse=True)