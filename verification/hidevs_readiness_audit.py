import os
import sys
import json
import yaml

def audit():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    issues = []
    details = []
    
    # 1. Check basic files
    required_files = ['agent.yaml', 'SOUL.md', 'EXPLAINABILITY.md', 'README.md', '.gitignore']
    for rf in required_files:
        if not os.path.exists(os.path.join(root_dir, rf)):
            issues.append(f"Missing required file: {rf}")
        else:
            details.append(f"Found {rf}")
            
    # 2. Check agent.yaml validity and OpenGAP schema compliance
    agent_yaml_path = os.path.join(root_dir, 'agent.yaml')
    if os.path.exists(agent_yaml_path):
        try:
            with open(agent_yaml_path, 'r') as f:
                agent_data = yaml.safe_load(f)
                
            # Basic OpenGAP schema checks
            for req in ['name', 'version', 'description']:
                if req not in agent_data:
                    issues.append(f"agent.yaml missing required field: {req}")
            
            # Check for invalid root keys
            invalid_keys = ['id', 'passport', 'capabilities']
            for ik in invalid_keys:
                if ik in agent_data:
                    issues.append(f"agent.yaml contains invalid root key per OpenGAP schema: {ik}")
                    
        except yaml.YAMLError:
            issues.append("agent.yaml is not valid YAML")
            
    # 3. Check for secrets
    env_path = os.path.join(root_dir, '.env')
    if os.path.exists(env_path):
        # We don't fail just for existing, but ensure it's in gitignore
        gitignore_path = os.path.join(root_dir, '.gitignore')
        if os.path.exists(gitignore_path):
            with open(gitignore_path, 'r') as f:
                if '.env' not in f.read():
                    issues.append(".env not found in .gitignore")
                    
    # 4. Check documentation headings
    explain_path = os.path.join(root_dir, 'EXPLAINABILITY.md')
    if os.path.exists(explain_path):
        with open(explain_path, 'r') as f:
            content = f.read()
            for heading in ['Purpose', 'Inputs and Data Sources', 'Decision and Reasoning']:
                if heading not in content:
                    issues.append(f"EXPLAINABILITY.md missing heading: {heading}")
                    
    # 5. Discover tools
    sys.path.insert(0, root_dir)
    try:
        import verification.discover_tools as dt
        discovery_result = dt.run_discovery()
        if discovery_result['status'] == 'FAILED':
            issues.extend(discovery_result['issues'])
        else:
            details.append(f"Discovered tools: {discovery_result['discovered']}")
    except Exception as e:
        issues.append(f"Failed to run tool discovery: {str(e)}")

    if issues:
        return {"status": "FAILED", "issues": issues, "details": details}
    return {"status": "PASSED", "issues": [], "details": details}

if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, indent=2))
    if result['status'] == 'FAILED':
        sys.exit(1)
    else:
        sys.exit(0)
