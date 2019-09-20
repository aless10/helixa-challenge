import pytest

from helixa_app.tasks.task_executor import TaskExecutor


def test_task_executor_no_strategy():
    with pytest.raises(Exception):
        TaskExecutor(strategy=None)
