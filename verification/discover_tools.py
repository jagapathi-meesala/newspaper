import os
import yaml
import glob
import json

def run_discovery():
    """Dynamically discovers tools from the registry and checks their validity."""
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    agent_yaml_path = os.path.join(root_dir, 'agent.yaml')
    
    if not os.path.exists(agent_yaml_path):
        return {"status": "FAILED", "issues": ["agent.yaml not found"]}
        
    with open(agent_yaml_path, 'r') as f:
        try:
            agent_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return {"status": "FAILED", "issues": [f"Invalid YAML: {e}"]}
            
    declared_tools = agent_data.get('tools', [])
    discovered_tools = []
    
    tool_files = glob.glob(os.path.join(root_dir, 'tools', '*.yaml'))
    
    issues = []
    
    for tool_file in tool_files:
        basename = os.path.basename(tool_file).replace('.yaml', '')
        discovered_tools.append(basename)
        
        # Check python implementation exists
        py_file = os.path.join(root_dir, 'tools', f"{basename}.py")
        if not os.path.exists(py_file):
            issues.append(f"Missing Python implementation for tool: {basename}")
            
    for dt in declared_tools:
        if dt not in discovered_tools:
            issues.append(f"Declared tool '{dt}' not found in tools directory.")
            
    if issues:
        return {"status": "FAILED", "issues": issues, "discovered": discovered_tools}
        
    return {"status": "PASSED", "issues": [], "discovered": discovered_tools}

if __name__ == "__main__":
    result = run_discovery()
    print(json.dumps(result, indent=2))
    if result["status"] == "FAILED":
        exit(1)
