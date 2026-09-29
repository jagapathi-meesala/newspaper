import json

def run(source_text: str) -> str:
    """Isolates specific factual claims from a text."""
    if not source_text:
        return json.dumps({"error": "Empty source text provided."})
        
    # Deterministic mock extraction based on simple heuristics
    claims = []
    sentences = [s.strip() for s in source_text.split('.') if s.strip()]
    for s in sentences:
        if "announced" in s.lower() or "agree" in s.lower() or "argue" in s.lower():
            claims.append(s)
            
    if not claims and sentences:
        claims.append(sentences[0])
        
    return json.dumps({"claims": claims})

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(run(sys.argv[1]))
