# STOP Triggers Protocol

**Status**: Locked
**Version**: v0.1

---

## Decision Taxonomy

```python
class Decision(str, Enum):
    ACCEPT = "ACCEPT"
    STOP = "STOP"
    NEED_REVIEW = "NEED_REVIEW"
```

---

## STOP Triggers (Locked)

| Trigger | Enum Value | When Activated | Machine-Readable Proof |
|---------|-----------|----------------|------------------------|
| **No Candidates** | `no_candidates_found` | No extraction candidates detected in document | `{"searched": true, "candidates_found": 0}` |
| **Conflicting Values** | `conflicting_values` | Multiple different values extracted for same field | `{"candidates": [{"value": ..., "confidence": ..., "evidence": ...}]}` |
| **Confidence Below Threshold** | `insufficient_confidence` | Best candidate confidence < 0.7 | `{"threshold": 0.7, "actual": 0.XX, "value": "..."}` |
| **Missing Evidence Spans** | `missing_evidence` | No document span mapping for extracted value | `{"value": "..."}` |
| **Evidence Integrity Failure** | `evidence_integrity_failed` | Quote/offset mismatch or verification failed | `{"issues": [...], "value": "..."}` |

---

## STOP-First Logic

```python
# Evaluation order (all checked sequentially):
1. No candidates? → STOP
2. Conflicting values? → STOP
3. Confidence too low? → STOP
4. Missing evidence spans? → STOP
5. Evidence integrity failed? → STOP
6. All checks passed → ACCEPT
```

---

## Evidence Requirements

```json
{
  "min_confidence": 0.7,
  "require_exact_quote": true,
  "require_offset_mapping": true,
  "stop_on_conflict": true
}
```

---

## Negative Proof Structure

Every STOP decision includes:

```python
{
  "field_name": "effective_date",
  "decision": "STOP",
  "value": null,
  "evidence": null,
  "confidence": 0.0,
  "stop_reason": "no_candidates_found",  # enum value
  "stop_proof": {
    # Machine-readable proof of why STOP occurred
    "searched": true,
    "candidates_found": 0
  }
}
```

---

## Determinism Guarantee

- STOP triggers evaluated in fixed order
- Same document + same schema → same STOP decision
- All proof artifacts timestamped with UTC ISO 8601
- SHA-256 hashes for tamper detection

---

**Modification Policy**: No changes to STOP triggers without major version bump (v1.x)
