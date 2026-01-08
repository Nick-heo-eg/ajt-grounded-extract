# EU AI Act Alignment

This document maps EU AI Act requirements—specifically Article 12 (Record-Keeping)—to the concrete behavior of this system.

---

## EU AI Act — Article 12 (Record-Keeping)

| EU AI Act Requirement | Interpretation | This System |
|---|---|---|
| Automatic recording of events | Decisions and non-decisions are events | Judgment trace (STOP / ACCEPT) |
| Traceability over system lifetime | Logs must be reconstructable | Preserved audit artifacts |
| Events relevant to risk | Silence must be explainable | Negative proof on STOP |
| Post-market monitoring support | Decisions must be reviewable | Deterministic trace output |

---

## Interpretation: Silence Is a Decision

No output is not neutral.

Under Article 12, a decision not to extract is an event.

This system treats STOP as a first-class audit artifact.

---

## Technical Implementation

### Judgment Trace
Every extraction attempt produces a judgment record:
- **ACCEPT**: Document-grounded evidence with byte offsets
- **STOP**: Negative proof with explicit reason and evaluated alternatives

### Preserved Artifacts
All judgments are written to immutable JSONL logs with:
- Timestamp (ISO 8601)
- Document hash (SHA-256)
- Decision metadata (`decision_role`, `execution_authority`)
- Trace signature for integrity verification

### Negative Proof
When extraction does not proceed, the system records:
- What was searched (field definitions, patterns)
- What was found (candidate count, conflicting values)
- Why extraction stopped (reason code with supporting data)
- When the judgment was made (timestamped proof artifact)

---

## Scope

This alignment applies to:
- Document extraction in compliance-critical contexts
- Systems requiring audit trails for AI decisions
- High-risk AI systems under EU AI Act Article 6

This document does not claim regulatory compliance. It demonstrates how specified requirements are implemented.
