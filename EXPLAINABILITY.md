## Purpose
This document explains how the News Research Agent arrives at its conclusions, ensuring complete transparency in its operations.

## Inputs and Data Sources
The agent receives inputs via standardized tool parameters (such as `topic` or `source_texts`). Data sources are either dynamically retrieved via external APIs or fallback mock data when APIs are disconnected. Every piece of data used in a report retains metadata tracking its origin.

## Decision and Reasoning
The agent's internal reasoning separates extraction from interpretation:
1. **Gather**: Pull raw texts via `research-topic`.
2. **Extract**: Isolate discrete claims via `extract-claims` and `analyze-source`.
3. **Compare**: Identify overlapping or conflicting facts via `compare-sources`.
4. **Synthesize**: Format data via `generate-research-report`.

## Tools and Capabilities
- `research-topic`: Resolves a string query to a list of source materials.
- `analyze-source`: Parses metadata and structure from a source.
- `extract-claims`: Pulls out factual statements for comparison.
- `compare-sources`: Performs deterministic grouping of conflicting/agreeing claims.
- `generate-research-report`: Creates human-readable documentation.

## Limitations and Constraints
- The agent does not magically know facts outside its source texts.
- If a source API returns an error or rate limits the agent, the agent gracefully fails and informs the user.

## Portability
The AgentCore is built devoid of framework-specific logic. It communicates through defined python dataclasses (Contracts) and relies on Framework Adapters to plug into larger orchestration systems (like CrewAI, LangChain, etc.).

## Verification
Verification is handled via standard unit tests testing pure deterministic logic, and dynamic discovery scripts that check structural compliance against the OpenGAP standard.

## Failure Handling
Network failures, missing credentials, and malformed responses are captured by specific try-except blocks, emitting safe fallback states and warning logs without exposing sensitive traceback information.

## Expected Output
Structured JSON payloads internally, serialized to deterministic Markdown reports for users.
