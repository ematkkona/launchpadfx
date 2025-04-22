import pytest
from lpfx.scripting.script_runner import ScriptRunner

class DummyController:
    def __init__(self):
        self.effects_triggered = []

    def send_note(self, note, velocity):
        pass

    def clear_grid(self):
        pass

@pytest.fixture
def dummy_controller():
    return DummyController()

def test_fx_execution(dummy_controller):
    runner = ScriptRunner(dummy_controller)
    runner.fx("wave", duration=0.01)  # should not crash

def test_wait_and_loop(dummy_controller):
    runner = ScriptRunner(dummy_controller)
    runner.wait(0.01)  # simple delay
    runner.loop(2, ["wait(0.01)"])  # loop internal wait