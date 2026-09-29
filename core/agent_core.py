import json
import logging
from typing import Dict, Any, List

# Importing schemas
from contracts.schemas import ResearchRequest, SourceData, ResearchReport

import os
import importlib.util

def load_tool(name):
    path = os.path.join(os.path.dirname(__file__), "..", "tools", f"{name}.py")
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

research_topic = load_tool("research-topic")
analyze_source = load_tool("analyze-source")
extract_claims = load_tool("extract-claims")
compare_sources = load_tool("compare-sources")
generate_research_report = load_tool("generate-research-report")

logger = logging.getLogger(__name__)

class AgentCore:
    """Central engine for the News Research Agent."""
    
    def __init__(self):
        pass

    def run_research(self, request: ResearchRequest) -> ResearchReport:
        logger.info(f"Starting research on: {request.topic}")
        
        # 1. Gather
        sources_json = research_topic.run(request.topic)
        sources_data = json.loads(sources_json)
        
        sources: List[SourceData] = []
        for s in sources_data:
            sd = SourceData(
                title=s.get("title", ""),
                source=s.get("source", ""),
                url=s.get("url", ""),
                content=s.get("content", ""),
                date=s.get("date")
            )
            
            # 2. Extract Claims
            claims_json = extract_claims.run(sd.content)
            claims_data = json.loads(claims_json)
            sd.claims = claims_data.get("claims", [])
            sources.append(sd)
            
        # 3. Compare (Mock comparing first two sources if available)
        agreements = []
        conflicts = []
        if len(sources) >= 2:
            comp_json = compare_sources.run(sources[0].claims, sources[1].claims)
            comp_data = json.loads(comp_json)
            agreements = comp_data.get("agreements", [])
            conflicts = comp_data.get("conflicts", [])
            
        # 4. Generate Report
        sources_dict_list = [{"title": s.title, "source": s.source} for s in sources]
        report_json = generate_research_report.run(request.topic, sources_dict_list, agreements, conflicts)
        report_data = json.loads(report_json)
        
        return ResearchReport(
            topic=request.topic,
            sources=sources,
            agreements=agreements,
            conflicts=conflicts,
            markdown=report_data.get("markdown_report", "")
        )
