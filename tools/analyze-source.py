import json

def run(source_text: str) -> str:
    """Analyzes a given source text to determine its structure, sentiment, and basic attributes."""
    if not source_text:
        return json.dumps({"error": "Empty source text provided."})
        
    analysis = {
        "word_count": len(source_text.split()),
        "has_quotes": '"' in source_text or "'" in source_text,
        "is_opinion": "critics argue" in source_text.lower() or "opinion" in source_text.lower(),
        "summary": source_text[:100] + "..." if len(source_text) > 100 else source_text
    }
    
    return json.dumps(analysis)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(run(sys.argv[1]))
