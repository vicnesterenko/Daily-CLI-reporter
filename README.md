# Daily-CLI-reporter

This repository contains the two scripts `Task6.py` and `info_workspaces.py`  for the Daily-CLI-reporter project using the Clockify API. 

This guide will walk you through the steps to set up and use the code:

### Prerequisites

1. **Python**: Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Git**: If you're using Git, you'll need it installed. You can download it from the official [Git website](https://git-scm.com/downloads).

3. **Clockify**: Register your account [Clockify website](https://clockify.me/), if you don't have. Generate the API key in your profile.

### Installation

1. **Clone the Repository**: Open a terminal and run the following command to clone this repository:

   ```bash
   git clone https://github.com/your-username/Daily-CLI-reporter.git
   ```

2. **Navigate to the Directory**: Change to the project directory:

   ```bash
   cd Daily-CLI-reporter
   ```

3. **Install Dependencies**: Install the required dependencies using pip:

   ```terminal
   pip install -r requirements.txt
   ```

4. **Install virtual environment**:

   **On Windows:**

   Navigate to the directory where you want to create your project and virtual environment:
   ```terminal
   cd path\to\your\project\directory
    ```
   Create a virtual environment with the name `your_venv_name`:
   ```terminal
   python -m venv your_venv_name
    ```
   Activate the virtual environment:
   ```terminal
   your_venv_name\Scripts\activate
   ```
    **On macOS and Linux:**
   ```terminal
   cd path/to/your/project/directory
    ```
   Create a virtual environment with the name `your_venv_name`
   ```terminal
   python3 -m venv your_venv_name
    ```
   Activate the virtual environment:
   ```terminal
   source venv/bin/activate
   ```
   When you're done working in the virtual environment, you can deactivate it:
    ```terminal
   deactivate
   ```
   

### Usage

1. **Obtain API Key and IDs**:
   - Replace `API_KEY`, `WORKSPACE_ID`, and `PROJECT_ID` in the `Task6.py` file with your own Clockify API key, workspace ID, and project ID.

2. **Run the Script**:
   - Execute the `Task6.py` script to retrieve tasks from the specified workspace and project using the Clockify API:

   ```terminal
   python Task6.py
   ```

3. **View Task Report**:
   - The script will print results for Task 6 and Task 8 of the test Python project for a job offer.
   - The `TASK REPORT FOR TASKS SORTED BY DATE` section nicely groups tasks by date.
   - `TASK REPORT FOR TASKS BY TIME TRACKER` section provides a summary of each task's total hours spent.
   - The `TOTAL HOURS SPENT FOR TASKS` section gives an overall summary of the time tracked for all tasks in Time Tracker.

### Notes

- The `ClockifyAPI` class in `Task6.py` handles API requests to retrieve workspace information, project information, and tasks.
- The `get_all_workspaces_list` and `get_all_projectId_list` methods are provided but must be further implemented based on your needs.
- The script uses the `requests` library to interact with the Clockify API.
- The script `info_workspaces.py` is written with `clockify` library and after running the script, the workspace information will be displayed in a formatted manner by `pprint`.
