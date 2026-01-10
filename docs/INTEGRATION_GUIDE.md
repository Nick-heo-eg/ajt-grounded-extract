# Integration Guide

This guide describes integration patterns for AJT-Grounded-Extract.

It explains where this system fits, how it is called, and what the caller must do when STOP occurs.
This is not a capabilities expansion—it is a usage clarification within Phase 1 boundaries.

---

## Where This System Fits

AJT-Grounded-Extract is designed as an **advisory judgment component** in document processing pipelines.

Typical integration contexts:
- **Contract/legal document pipelines** — Extract key terms with evidence or stop when ambiguous
- **Medical record preprocessing** — Extract structured data or flag missing/conflicting information
- **Financial compliance ingestion** — Extract income verification with audit trails
- **RAG preprocessing** — Ensure retrieval results are grounded before downstream use

**Role**: Produces ACCEPT (with evidence) or STOP (with negative proof) judgments.
**Not a role**: Decision executor, workflow orchestrator, or policy enforcer.

---

## How to Integrate

### CLI Invocation

```bash
python run.py path/to/document.txt
```

Output written to `evidence/` directory as `.jsonl` and `.json` manifest files.

### Programmatic Invocation

```python
from engine.pipeline import ExtractionPipeline

pipeline = ExtractionPipeline()
result = pipeline.run("path/to/document.txt")

for decision in result["results"]:
    if decision["decision"] == "ACCEPT":
        # Use extracted value with evidence
        value = decision["value"]
        evidence = decision["evidence"]

    elif decision["decision"] == "STOP":
        # Route to manual review or request more context
        reason = decision["stop_reason"]
        proof = decision["stop_proof"]
```

**Key point**: Output is always interpreted by the caller.
This system produces judgments, not commands.

---

## Handling STOP Correctly

**STOP is an advisory judgment, not a block.**

When STOP occurs, the caller must decide what to do next.

### Caller Responsibilities

1. **Route to human review**
   - Flag document for manual inspection
   - Provide STOP reason and negative proof to reviewer

2. **Request additional documents**
   - If evidence is missing, request source material
   - Log STOP as justification for document request

3. **Log STOP as due diligence artifact**
   - STOP events prove the system did not guess
   - Use for audit trails, regulatory documentation

4. **Decide whether to proceed**
   - Execution authority remains with the caller
   - Ignoring STOP is permitted but should be logged

**Explicitly**: STOP does not block execution automatically.
It provides reasoning for external decision-making.

---

## What This System Does NOT Do

This system will not:

- ❌ Execute decisions on behalf of the caller
- ❌ Orchestrate workflows or trigger downstream actions
- ❌ Enforce policies or business rules
- ❌ Automatically retry or escalate on STOP
- ❌ Take responsibility for downstream outcomes

These are intentional non-capabilities, not missing features.

---

## Responsibility Boundary (Explicit)

**Execution authority remains external.**

- Caller owns consequences of using ACCEPT results
- Caller owns consequences of ignoring STOP judgments
- This system produces reasoning traces, not commands

**Liability model**:
- System provides evidence (ACCEPT) or negative proof (STOP)
- Caller decides what to do with that information
- Downstream outcomes are caller's responsibility

---

## Integration Patterns

### Pattern 1: Pre-validation for RAG

```python
# Before using retrieved document in RAG
result = pipeline.run(retrieved_doc)

if any(d["decision"] == "STOP" for d in result["results"]):
    # Document has insufficient evidence
    # Request more context or skip this document
    continue

# All fields ACCEPT—safe to use
proceed_with_rag(result)
```

### Pattern 2: Audit-ready extraction

```python
# Extract with full audit trail
result = pipeline.run(document)

# Archive decisions
save_to_audit_log(result["artifact_refs"])

# Use or escalate based on judgment
for decision in result["results"]:
    if decision["decision"] == "ACCEPT":
        use_extracted_value(decision["value"])
    elif decision["decision"] == "STOP":
        escalate_to_human(decision)
```

### Pattern 3: Compliance pipeline

```python
# Extract with regulatory trace
result = pipeline.run(compliance_document)

# Check for STOP events
stops = [d for d in result["results"] if d["decision"] == "STOP"]

if stops:
    # Log due diligence: system refused to guess
    log_negative_proof(stops)
    flag_for_compliance_review(document)
else:
    # All fields extracted with evidence
    proceed_to_approval(result)
```

---

## Cross-References

For detailed specifications:
- STOP meaning and semantics: [STOP_SEMANTICS.md](STOP_SEMANTICS.md)
- Output structure: [OUTPUT_FORMAT.md](OUTPUT_FORMAT.md)
- Boundary guarantees: [JUDGMENT_BOUNDARY_MATRIX.md](JUDGMENT_BOUNDARY_MATRIX.md)
- System architecture: [ARCHITECTURE.md](ARCHITECTURE.md)

---

## Summary

This system is a **judgment component**, not a decision executor.

Integration requires:
1. Calling the system with a document
2. Interpreting ACCEPT (with evidence) or STOP (with negative proof)
3. Making external decisions about what to do next

**Execution authority remains with the caller.**
