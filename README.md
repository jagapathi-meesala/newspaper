# News Research Agent

## Project Overview
The News Research Agent is a completely independent AI agent designed to help users research news topics using structured, transparent workflows. It complies strictly with the OpenGAP v0.1.0 specification.

## Purpose
The agent aims to help users gather, compare, and summarize news information accurately without fabricating claims or sources. It provides a transparent, deterministic pathway to conduct research.

## Architecture
The system is built on an adaptable, decoupled architecture:
1. **AgentCore**: The single source of truth that coordinates requests.
2. **Execution Engine**: Determines how workflows run.
3. **Tool Registry**: Dynamically discovers and loads compliant tools.
4. **Domain Tools**: Specialized logic components (e.g., source comparison, claim extraction).
5. **Adapter Layer**: Replaceable interface for external frameworks (if required).

## Features
- Real-time/mock topic research capabilities.
- Source analysis and claim extraction.
- Factual verification logic.
- Independent core engine completely separate from any specific downstream framework.

## Tools
The agent uses the following dynamically discovered domain tools:
- `research-topic`: Searches for a topic.
- `analyze-source`: Analyzes the text and attributes of a source.
- `compare-sources`: Compares claims between two or more sources.
- `extract-claims`: Isolates specific factual claims from a text.
- `generate-research-report`: Compiles findings into a markdown report.

## Project Structure
```text
news-research-agent/
├── agent.yaml           # OpenGAP manifest
├── SOUL.md              # Agent identity and values
├── DUTIES.md            # Role boundaries
├── EXPLAINABILITY.md    # Reasoning and logic documentation
├── README.md            # Project overview
├── core/                # Agent core components
├── tools/               # Dynamic OpenGAP tools (YAML schemas + implementations)
├── adapters/            # Framework adapters
├── contracts/           # Data schemas
├── tests/               # Pytest suite
└── verification/        # Readiness audit and tool discovery
```

## Installation
Ensure you have Python 3.9+ installed.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration
Use environment variables for external configurations. Copy `.env.example` to `.env` and configure accordingly.

## Environment variables
- `NEWS_API_KEY`: API key for the real news provider (if testing live mode).
- `LOG_LEVEL`: Application logging level (e.g., INFO, DEBUG).

## Running the agent
*Usage docs to be updated once execution framework adapter is invoked.*

## Running tests
```bash
python3 -m pytest -q
```

## Running readiness audit
```bash
python3 verification/hidevs_readiness_audit.py
```

## OpenGAP validation
```bash
npx -y @open-gitagent/opengap validate
```

## Security
No secrets are hardcoded. `.env` is ignored by version control. Secure environment variable injection is strictly enforced.

## Framework integration status
Structural adapter implemented; live framework execution not performed (designed to be agnostic).

## Limitations
- Operates in a deterministic local fallback mode if `NEWS_API_KEY` is missing.
- Only compares text strictly provided to it.

## Verification
Verification is handled via dynamic scripts that read the repository structure instead of using hardcoded assertions.

## HiDevs readiness
Compliant with HiDevs Agent Passport program requirements for an independent agent.
