import requests
from dateutil.parser import parse
from datetime import datetime
from pprint import pprint


class ClockifyAPI:
    def __init__(self, api_key, workspace_id, project_id, user_id):
        self.api_key = api_key
        self.workspace_id = workspace_id
        self.project_id = project_id
        self.user_id = user_id
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
                    return [task["name"] for task in tasks]
                else:
                    print("No tasks found")
        except Exception as e:
            print("Error getting tasks list. Status code:", response.status_code)

    def get_timer_records(self) -> list:
        try:
            url = f"https://api.clockify.me/api/v1/workspaces/{self.workspace_id}/user/{self.user_id}/time-entries"
            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:
                time_records = response.json()
                if time_records:
                    return time_records
                else:
                    print("No time records found")
            else:
                print("Error getting time records. Status code:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def generate_task_report(self):
        try:
            timer_records = self.get_timer_records()
            if timer_records:
                total_hours_spent = 0
                for record in timer_records:
                    task_name = record["description"]
                    task_id = record["id"]
                    interval = record["timeInterval"]

                    start_time = parse(interval["start"])
                    end_time = parse(interval["end"])

                    duration = end_time - start_time
                    hours_spent = duration.total_seconds() / 3600
                    total_hours_spent += hours_spent
                    print(
                        f"Task description in Time Tracker: {task_name}\nTask ID: {task_id}\nHours Spent: {hours_spent:.2f} hours\n"
                    )
                print(
                    f"Total hours spent fixed by Timer: {total_hours_spent:.2f} hours"
                )
            else:
                print("No timer records found")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    API_KEY = "MTc3NGY1YzgtOTMyYS00Y2U3LWI2ZGMtMGM2MTkxYzMwZTFj"
    WORKSPACE_ID = "64dcc03aee1545789668e1d6"
    PROJECT_ID = "64dcc07a528dfc262c9867fe"
    USER_ID = "64dcc03aee1545789668e1d0"

    clockify_api = ClockifyAPI(API_KEY, WORKSPACE_ID, PROJECT_ID, USER_ID)
    tasks = clockify_api.get_all_tasks()
    # pprint(tasks)

    timer_records = clockify_api.get_timer_records()
    # pprint(timer_records)

    clockify_api.generate_task_report()
