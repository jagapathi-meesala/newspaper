import os
import json
import logging

logger = logging.getLogger(__name__)

def run(topic: str) -> str:
    """Searches for a topic and returns relevant news sources or articles."""
    api_key = os.environ.get("NEWS_API_KEY")
    
    if api_key:
        logger.info("Live API execution is disabled for safety/mock scope. Falling back to deterministic data.")
    
    # Deterministic mock data for testing/fallback
    mock_data = [
        {
            "title": f"Recent developments in {topic}",
            "source": "Global News Network",
            "date": "2023-10-25",
            "url": "https://example.com/news/1",
            "content": f"Today, major advancements were announced regarding {topic}. Experts agree it will change the industry."
        },
        {
            "title": f"The controversy surrounding {topic}",
            "source": "Tech Daily",
            "date": "2023-10-26",
            "url": "https://example.com/news/2",
            "content": f"Some critics argue that {topic} is overhyped and lacks fundamental evidence."
        }
    ]
    
    return json.dumps(mock_data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(run(sys.argv[1]))
