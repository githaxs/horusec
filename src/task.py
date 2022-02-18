import os
from task_interfaces import TaskInterface, SubscriptionLevels, TaskTypes


class Task(TaskInterface):
    """
    SAST analysis of your project from the code perspective
    """

    name = "Horusec"
    slug = "horusec"
    pass_summary = ""
    pass_text = ""
    fail_summary = ""
    fail_text = ""
    subscription_level = SubscriptionLevels.ENTERPRISE
    actions = None

    # For code format tasks, specify if they can automatically fix errors.
    # If they can there will be a button for users to click in github ui.
    can_fix = False

    type = TaskTypes.CODE_FORMAT
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)
    handler = "task"

    # Use the execute function if the task type is WORKFLOW
    def execute(self, github_body, settings) -> bool:
        pass
