import sys
import os

# Ensure the root directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from core.agent_core import AgentCore
from contracts.schemas import ResearchRequest

def test_core_deterministic_run():
    core = AgentCore()
    req = ResearchRequest(topic="Artificial Intelligence")
    report = core.run_research(req)
    
    assert report.topic == "Artificial Intelligence"
    assert len(report.sources) > 0
    assert report.markdown.startswith("# Research Report: Artificial Intelligence")
    assert "Agreements" in report.markdown or "Conflicts" in report.markdown
