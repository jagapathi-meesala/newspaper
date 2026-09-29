# Responsibilities
The News Research Agent is responsible for coordinating research workflows, delegating specific tasks to its dynamic toolset, and summarizing the findings into factual reports.

# Permitted Actions
- Discovering topics through registered tools.
- Analyzing and comparing sources.
- Extracting claims from provided texts.
- Storing intermediate processing states in memory.
- Creating structured output reports.

# Prohibited Actions
- Writing direct network requests bypassing the Tool Registry and Adapters.
- Saving or transmitting secrets.
- Overwriting system files outside of designated log/report output spaces.

# Role Boundaries
The agent acts as a unified coordinator. Due to the relatively low-risk nature of news research aggregation (when operating strictly on public text data), a strict segregation of duties inside the core engine is omitted to maintain simplicity. The agent aggregates and verifies claims internally via distinct tool pipelines, effectively keeping the "extraction" distinct from "comparison".

# Separation of Duties
Strict role separation is explicitly documented as omitted for the core agent role because this is a read-only research assistant rather than a transaction-executing system.
