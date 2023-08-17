import requests
from dateutil.parser import parse
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
                    return pprint(workspaces)
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
                    return pprint(projects)
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

    def get_task_by_id(self, task_id: str) -> list:
        response = requests.get(
            f"https://api.clockify.me/api/v1/workspaces/{self.workspace_id}/projects/{self.project_id}/tasks/{task_id}",
            headers=self.headers,
        )
        if response.status_code == 200:
            tasks_info = response.json()
            if tasks_info:
                return tasks_info["name"]
        else:
            [f"Error getting workspace list. Status code: {response.status_code}"]

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

    def prepare_task_date(self, timer_records):
        task_date_dict = {}
        for record in timer_records:
            id = record["taskId"]
            description = record["description"]
            interval = record["timeInterval"]
            dates = parse(interval["start"]).date()
            if dates in task_date_dict:
                task_date_dict[dates][id] = description
            else:
                task_date_dict[dates] = {id: description}
        return task_date_dict

    def prepare_task_hours_data(self, timer_records):
        task_hours_dict = {}
        total_hours_spent = 0
        for record in timer_records:
            id = record["taskId"]
            interval = record.get("timeInterval")
            if interval and interval.get("start") and interval.get("end"):
                try:
                    start_time = parse(interval["start"])
                    end_time = parse(interval["end"])
                    duration_calculate = end_time - start_time
                    hours_spent = duration_calculate.total_seconds() / 3600
                    total_hours_spent += hours_spent
                    if id in task_hours_dict:
                        task_hours_dict[id] += hours_spent
                    else:
                        task_hours_dict[id] = hours_spent
                except Exception as e:
                    print(f"Error processing interval for record {record}: {e}")
            else:
                print(f"Skipped record with missing or invalid interval: {record}")

        return task_hours_dict, total_hours_spent

    def generate_task_report(self):
        try:
            timer_records = self.get_timer_records()
            if timer_records:
                task_hours_dict, total_hours_spent = self.prepare_task_hours_data(
                    timer_records
                )
                task_date_dict = self.prepare_task_date(timer_records)
                if task_date_dict:
                    print("{: ^70}".format("📅TASK REPORT FOR TASKS SORTED BY DATE📅"))
                for date, tasks in task_date_dict.items():
                    formatted_date = date.strftime("%Y-%m-%d")
                    frame_line = "=" * (len(formatted_date) + 6)
                    print(frame_line, f"Date: {formatted_date}", frame_line, sep="\n")
                    for id, description in tasks.items():
                        tasks_info = self.get_task_by_id(id)
                        hours_spent = task_hours_dict.get(id, 0)
                        print(
                            "\n".join(
                                [
                                    "-" * (len(formatted_date) + 60),
                                    f"Task Name: {tasks_info}",
                                    f"Hours Spent: {hours_spent:.2f} hours",
                                    f"Description: {description}",
                                    "-" * (len(formatted_date) + 60),
                                ]
                            )
                        )
                print("{: ^70}".format("⌚TASK REPORT FOR TASKS BY TIME TRACKER⌚"))
                for id, hours_spent in task_hours_dict.items():
                    tasks_info = self.get_task_by_id(id)
                    print(
                        "\n".join(
                            [
                                "-" * (len(formatted_date) + 60),
                                tasks_info,
                                f"Total hours spent for this task: {hours_spent:.2f} hours",
                                "-" * (len(formatted_date) + 60),
                            ]
                        )
                    )
                print(
                    "\n".join(
                        [
                            "{: ^70}".format("🌟TOTAL HOURS SPENT FOR TASKS🌟"),
                            f"Total hours fixed by Time Tracker: {total_hours_spent:.2f} hours",
                            "\n",
                        ]
                    )
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
    # You can uncomment and check how Task6 works:
    # tasks = clockify_api.get_all_tasks()
    # pprint(tasks)
    clockify_api.generate_task_report()
