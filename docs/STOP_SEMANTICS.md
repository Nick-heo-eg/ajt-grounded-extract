# STOP Semantics

STOP is a core output type in this system, with specific meaning and constraints.

---

## What STOP Is

**STOP is an advisory judgment signal** indicating:
- Evidence was insufficient for reliable extraction
- Conflicting information detected
- Responsibility boundary reached

STOP produces **structured negative proof**:
- What was searched
- What was found (or not found)
- Why extraction did not proceed
- What would be required to proceed

---

## What STOP Is NOT

STOP is not:
- ❌ A failure or error
- ❌ A hard block preventing execution
- ❌ An enforcement mechanism
- ❌ A policy decision

STOP is:
- ✅ A documented judgment boundary
- ✅ An advisory signal for external decision-making
- ✅ Structured negative proof

---

## STOP vs. Error

| Aspect | STOP | Error |
|--------|------|-------|
| **Meaning** | Evidence insufficient | System malfunction |
| **Output** | Structured negative proof | Stack trace / exception |
| **Next action** | Manual review or additional evidence | Fix bug |
| **Audit value** | High (proves system did not guess) | Low (indicates failure) |

---

## Non-Blocking Semantics

**Critical**: STOP does not prevent the caller from taking action.

- STOP is a recommendation
- Execution authority remains external
- Caller can:
  - Route to manual review
  - Request additional evidence
  - Proceed with caution (logged)
  - Cancel operation

STOP documents the boundary—it does not enforce it.

---

## Negative Proof

Negative proof is evidence of intentional non-execution.

Example:
```json
{
  "decision": "STOP",
  "reason": "no_candidates_found",
  "negative_proof": {
    "searched": ["effective_date"],
    "checked_scope": "entire document (347 lines)",
    "found": [],
    "explanation": "No explicit date value present"
  }
}
```

**Value**: Proves the system:
- Did perform the search
- Did not find matching evidence
- Did not guess or infer

This is legally and operationally valuable.

---

## When STOP Occurs

STOP triggers when:
1. **No candidates found** — Target field not present in document
2. **Conflicting values** — Multiple candidates with no clear precedence
3. **Insufficient confidence** — Evidence present but weak/ambiguous
4. **Evidence integrity failure** — Verification failed (hash mismatch, etc.)

---

## STOP Rate as a Metric

STOP rate is not a measure of system failure.

**High STOP rate** may indicate:
- Documents are low-quality (good to detect)
- Schema expectations are too strict (tune if needed)
- System is correctly enforcing boundaries (expected)

**Low STOP rate** may indicate:
- Documents are high-quality (ideal)
- System is inferring beyond evidence (bad)

Monitor STOP patterns, not just rate.

---

## Summary

> **STOP is not an exception to handle.**
>
> **STOP is a judgment type to respect.**

The system produces STOP when proceeding would require
assumption, inference, or interpretation beyond available evidence.

**This is correct behavior.**
