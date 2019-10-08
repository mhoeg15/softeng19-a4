from pmgr.project import Project, TaskException
import pytest
import os

PROJECT_NAME = "___hi"

@pytest.fixture(scope='function')
def p():
    p = Project(PROJECT_NAME)
    yield p


def test_class(p):
    assert p.name == PROJECT_NAME


def test_add(p):
    p.add_task("eat")
    p.add_task("steal_money_from_the_register")
    assert sorted(p.get_tasks()) == ["eat","steal_money_from_the_register"]


def test_already_added(p):
    with pytest.raises(TaskException):
        p.add_task("eat")


def test_remove(p):
    p.remove_task("eat")
    p.remove_task("steal_money_from_the_register")
    p.get_tasks() == []


def test_remove_fail(p):
    p.add_task("eat")
    with pytest.raises(TaskException):
        p.remove_task("eat")
        p.remove_task("eat")
        
