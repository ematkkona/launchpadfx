import pytest
import json
from pathlib import Path
from lpfx.config import load_config, save_config

CONFIG_PATH = Path.home() / ".lpfx_config.json"

def test_save_and_load_config(tmp_path, monkeypatch):
    fake_config = {"device": {"name": "Launchpad MK2 MIDI", "grid_size": [8, 8]}}
    fake_path = tmp_path / "config.json"

    # Patch CONFIG_FILE path
    monkeypatch.setattr("lpfx.config.CONFIG_FILE", fake_path)

    save_config(fake_config)
    loaded = load_config()
    assert loaded == fake_config