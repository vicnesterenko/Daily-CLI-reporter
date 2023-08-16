import requests
import json
from pprint import pprint


class ClockifyAPI:
    def __init__(self, api_key, workspace_id, project_id):
        self.api_key = api_key
        self.workspace_id = workspace_id
        self.project_id = project_id
        self.headers = {
            "X-Api-Key": self.api_key,
        }

    def get_all_workspaces_list(self) -> list:
        response = requests.get(
            "https://api.clockify.me/api/v1/workspaces", headers=self.headers
        )

        if response.status_code == 200:
            workspaces = response.json()
            if workspaces:
                try:
                    return pprint(workspaces)  # print(json.dumps(workspaces, indent=4))
                except Exception as e:
                    return print(f"No workspaces found: {type(e).__name__}")
        else:
            return print(
                "Error getting workspace list. Status code:", response.status_code
            )

    def get_all_projectId_list(self) -> list:
        response = requests.get(
            f"https://api.clockify.me/api/v1/workspaces/{self.workspace_id}/projects",
            headers=self.headers,
        )
        if response.status_code == 200:
            projects = response.json()
            if projects:
                try:
                    return pprint(projects)  # print(json.dumps(workspaces, indent=4))
                except Exception as e:
                    return print(f"No workspaces found: {type(e).__name__}")
        else:
            return print(
                "Error getting workspace list. Status code:", response.status_code
            )

    def get_all_tasks(self) -> list:
        try:
            response = requests.get(
                f"https://api.clockify.me/api/v1/workspaces/{self.workspace_id}/projects/{self.project_id}/tasks",
                headers=self.headers,
            )

            if response.status_code == 200:
                tasks = response.json()
                if tasks:
                    return tasks
                else:
                    print("No tasks found")
        except Exception as e:
            print("Error getting tasks list. Status code:", response.status_code)


if __name__ == "__main__":
    API_KEY = "MTc3NGY1YzgtOTMyYS00Y2U3LWI2ZGMtMGM2MTkxYzMwZTFj"
    WORKSPACE_ID = "64dcc03aee1545789668e1d6"
    PROJECT_ID = "64dcc07a528dfc262c9867fe"

    clockify_api = ClockifyAPI(API_KEY, WORKSPACE_ID, PROJECT_ID)
    tasks = clockify_api.get_all_tasks()
    pprint(tasks)
