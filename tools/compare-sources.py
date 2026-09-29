import json

def run(claims_a: list, claims_b: list) -> str:
    """Takes multiple claims or sources and identifies conflicting claims or agreements."""
    if not isinstance(claims_a, list) or not isinstance(claims_b, list):
        return json.dumps({"error": "Inputs must be lists of strings."})
        
    # Mock deterministic logic
    comparison = {
        "agreements": [],
        "conflicts": [],
        "unique_to_a": claims_a.copy(),
        "unique_to_b": claims_b.copy()
    }
    
    # Very basic overlapping logic mock
    for claim in claims_a:
        for other in claims_b:
            if claim.lower() == other.lower():
                comparison["agreements"].append(claim)
                if claim in comparison["unique_to_a"]:
                    comparison["unique_to_a"].remove(claim)
                if other in comparison["unique_to_b"]:
                    comparison["unique_to_b"].remove(other)
            elif "argue" in claim.lower() and "agree" in other.lower():
                comparison["conflicts"].append({"claim_a": claim, "claim_b": other})
                if claim in comparison["unique_to_a"]:
                    comparison["unique_to_a"].remove(claim)
                if other in comparison["unique_to_b"]:
                    comparison["unique_to_b"].remove(other)

    return json.dumps(comparison)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        try:
            a = json.loads(sys.argv[1])
            b = json.loads(sys.argv[2])
            print(run(a, b))
        except Exception as e:
            print(json.dumps({"error": str(e)}))
