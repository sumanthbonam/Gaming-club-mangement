# File: team_management.py
class TeamManagement:
    def __init__(self):
        self.teams = {}

    def create_team(self, team_name):
        if team_name in self.teams:
            return f"Team '{team_name}' already exists."
        self.teams[team_name] = []
        return f"Team '{team_name}' created successfully."

    def delete_team(self, team_name):
        if team_name not in self.teams:
            return f"Team '{team_name}' does not exist."
        del self.teams[team_name]
        return f"Team '{team_name}' deleted successfully."

    def view_teams(self):
        return list(self.teams.keys())

    def add_team_member(self, team_name, member_name, member_id):
        if team_name not in self.teams:
            return f"Team '{team_name}' does not exist."
        if member_id in [member['id'] for member in self.teams[team_name]]:
            return f"Member ID '{member_id}' already exists in team '{team_name}'."
        self.teams[team_name].append({'id': member_id, 'name': member_name})
        return f"Member '{member_name}' added to team '{team_name}'."

    def update_member_details(self, team_name, member_id, new_member_name):
        if team_name not in self.teams:
            return f"Team '{team_name}' does not exist."
        for member in self.teams[team_name]:
            if member['id'] == member_id:
                member['name'] = new_member_name
                return f"Member ID '{member_id}' updated successfully."
        return f"Member ID '{member_id}' not found in team '{team_name}'."

    def delete_team_member(self, team_name, member_id):
        if team_name not in self.teams:
            return f"Team '{team_name}' does not exist."
        for member in self.teams[team_name]:
            if member['id'] == member_id:
                self.teams[team_name].remove(member)
                return f"Member ID '{member_id}' deleted successfully."
        return f"Member ID '{member_id}' not found in team '{team_name}'."

    def view_team_members(self, team_name):
        if team_name not in self.teams:
            return f"Team '{team_name}' does not exist."
        return [f"ID: {member['id']}, Name: {member['name']}" for member in self.teams[team_name]]
