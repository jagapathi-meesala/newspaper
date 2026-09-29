import json

def run(topic: str, sources: list, agreements: list = None, conflicts: list = None) -> str:
    """Compiles a structured markdown summary from collected data."""
    agreements = agreements or []
    conflicts = conflicts or []
    
    report = f"# Research Report: {topic}\n\n"
    
    report += "## Sources\n"
    for s in sources:
        title = s.get('title', 'Unknown')
        src = s.get('source', 'Unknown')
        report += f"- **{title}** ({src})\n"
        
    report += "\n## Key Agreements\n"
    if agreements:
        for a in agreements:
            report += f"- {a}\n"
    else:
        report += "No clear agreements found.\n"
        
    report += "\n## Conflicts & Contradictions\n"
    if conflicts:
        for c in conflicts:
            a = c.get('claim_a', '')
            b = c.get('claim_b', '')
            report += f"- **Source A**: {a}\n  **Source B**: {b}\n"
    else:
        report += "No explicit conflicts detected.\n"
        
    return json.dumps({"markdown_report": report})

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        try:
            t = sys.argv[1]
            s = json.loads(sys.argv[2])
            a = json.loads(sys.argv[3]) if len(sys.argv) > 3 else []
            c = json.loads(sys.argv[4]) if len(sys.argv) > 4 else []
            print(run(t, s, a, c))
        except Exception as e:
            print(json.dumps({"error": str(e)}))
