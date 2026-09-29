import logging
from core.agent_core import AgentCore
from contracts.schemas import ResearchRequest

logger = logging.getLogger(__name__)

class FrameworkAdapter:
    """
    Structural adapter intended to wrap the AgentCore for integration 
    into external frameworks (e.g. LangChain, CrewAI).
    """
    def __init__(self, core_engine: AgentCore):
        self.core = core_engine
        
    def execute_task(self, task_definition: dict) -> dict:
        logger.info("Executing task via structural Framework Adapter.")
        topic = task_definition.get("topic", "Unknown Topic")
        request = ResearchRequest(topic=topic)
        
        # Execute core logic
        report = self.core.run_research(request)
        
        # Format response for external framework consumption
        return {
            "status": "success",
            "topic": report.topic,
            "markdown_report": report.markdown
        }
