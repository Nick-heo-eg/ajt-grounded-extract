# Output Format

This document describes the JSON structure of extraction decisions.

---

## Overview

All extraction decisions follow a consistent structure:
- **status**: `ACCEPT`, `STOP`, or `NEED_REVIEW`
- **metadata**: Timestamps, hashes, system info
- **payload**: Decision-specific data

---

## ACCEPT Output

```json
{
  "status": "ACCEPT",
  "field_name": "effective_date",
  "value": "01/15/2025",
  "evidence": {
    "quote": "Effective Date: 01/15/2025",
    "page": 1,
    "line_range": [15, 15],
    "integrity_hash": "a3f2b8..."
  },
  "confidence": 0.95,
  "metadata": {
    "timestamp": "2026-01-10T12:00:00Z",
    "document_hash": "b09b3641...",
    "decision_role": "advisory",
    "execution_authority": "external"
  }
}
```

**Fields:**
- `value`: Extracted value
- `evidence`: Grounded proof with document reference
- `confidence`: Extraction confidence score (0.0-1.0)
- `metadata`: System info and advisory markers

---

## STOP Output

```json
{
  "status": "STOP",
  "field_name": "effective_date",
  "reason": "no_candidates_found",
  "negative_proof": {
    "searched": ["effective_date", "start_date"],
    "checked_scope": "entire document (347 lines)",
    "found": [],
    "explanation": "No explicit date value present"
  },
  "metadata": {
    "timestamp": "2026-01-10T12:00:00Z",
    "document_hash": "382a5c2d...",
    "decision_role": "advisory",
    "stop_semantics": "non_blocking",
    "negative_proof_type": "intentional_non_execution"
  }
}
```

**Fields:**
- `reason`: Why extraction stopped (see STOP reasons below)
- `negative_proof`: Structured proof of what was checked
- `stop_semantics`: Always `"non_blocking"` (advisory only)

---

## STOP Reasons

| Reason | Description |
|--------|-------------|
| `no_candidates_found` | Target field not present in document |
| `conflicting_values` | Multiple candidates with no clear precedence |
| `insufficient_confidence` | Evidence present but weak/ambiguous |
| `evidence_integrity_failed` | Verification failed (hash mismatch) |

---

## NEED_REVIEW Output

```json
{
  "status": "NEED_REVIEW",
  "field_name": "payment_terms",
  "candidates": [
    {
      "value": "Net 30",
      "confidence": 0.65,
      "evidence": {...}
    },
    {
      "value": "Net 60",
      "confidence": 0.62,
      "evidence": {...}
    }
  ],
  "review_reason": "Multiple candidates with similar confidence",
  "metadata": {...}
}
```

**Fields:**
- `candidates`: All potential values with evidence
- `review_reason`: Why human judgment is needed

---

## Metadata Fields (Standard)

All outputs include these metadata fields:

- `timestamp`: ISO 8601 format
- `document_hash`: Content integrity hash
- `decision_role`: Always `"advisory"`
- `execution_authority`: Always `"external"`
- `stop_semantics`: `"non_blocking"` (for STOP outputs)
- `negative_proof_type`: `"intentional_non_execution"` (for STOP)

---

## Artifact Files

### Extraction Log (`.jsonl`)
One JSON object per line (newline-delimited):
```
{"status":"ACCEPT","field_name":"effective_date",...}
{"status":"STOP","field_name":"payment_terms",...}
```

### Manifest (`.json`)
Summary of extraction run:
```json
{
  "document_path": "examples/contract.txt",
  "document_hash": "b09b3641...",
  "extraction_timestamp": "2026-01-10T12:00:00Z",
  "results_summary": {
    "total_fields": 5,
    "accepted": 3,
    "stopped": 2,
    "need_review": 0
  },
  "artifact_refs": {
    "extraction_log": "evidence/extraction_2026-01-10T12-00-00.jsonl",
    "manifest": "evidence/manifest_2026-01-10T12-00-00.json"
  }
}
```

---

## Reading Outputs

### Python
```python
import json

# Read extraction log
with open("evidence/extraction_*.jsonl") as f:
    for line in f:
        decision = json.loads(line)
        if decision["status"] == "STOP":
            print(decision["negative_proof"])
```

### Command Line
```bash
# Count STOP decisions
grep '"status":"STOP"' evidence/extraction_*.jsonl | wc -l

# Extract all STOP reasons
jq -r 'select(.status=="STOP") | .reason' evidence/extraction_*.jsonl
```

---

## Versioning

Output format version: `2.1`

Breaking changes will increment major version.
Additions (new optional fields) increment minor version.
