# File: match_scheduling.py
import datetime

class MatchScheduling:
    def __init__(self):
        self.matches = []

    def create_match(self, team1, team2, match_date):
        try:
            match_date = datetime.datetime.strptime(match_date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use 'YYYY-MM-DD'."

        match = {
            "team1": team1,
            "team2": team2,
            "date": match_date,
            "status": "upcoming"
        }
        self.matches.append(match)
        return f"Match between '{team1}' and '{team2}' scheduled for {match_date.strftime('%Y-%m-%d')}."

    def view_upcoming_matches(self):
        today = datetime.datetime.now()
        return [match for match in self.matches if match["date"] > today]

    def view_past_matches(self):
        today = datetime.datetime.now()
        return [match for match in self.matches if match["date"] < today]

    def view_live_matches(self):
        today = datetime.datetime.now()
        return [match for match in self.matches if match["date"].date() == today.date()]
