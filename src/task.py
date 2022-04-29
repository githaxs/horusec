import os
from task_interfaces import StaticAnalysisTask, SubscriptionLevels


class Task(StaticAnalysisTask):
    """
    SAST analysis of your project from the code perspective
    """
    name = "Horusec"
    subscription_level = SubscriptionLevels.ENTERPRISE
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)