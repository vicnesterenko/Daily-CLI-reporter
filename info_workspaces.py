from clockify import factories
from pprint import pprint

API_KEY = "MTc3NGY1YzgtOTMyYS00Y2U3LWI2ZGMtMGM2MTkxYzMwZTFj"


def get_info_workspaces():
    workspace_services = factories.WorkspaceFactory(api_key=API_KEY)
    worspaces = workspace_services.get_all_workspaces()
    for workspace in worspaces:
        return pprint(workspace)


if __name__ == "__main__":
    get_info_workspaces()
