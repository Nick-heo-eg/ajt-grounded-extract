# Architecture

This document describes the extraction pipeline and decision flow.

---

## Pipeline Overview

```
Document → Ingest → Extract → Ground → Judge → Archive
           ↓        ↓         ↓        ↓        ↓
           Hash     Candidates Evidence STOP?   Artifacts
```

---

## Pipeline Stages

### 1. Ingest
- Load document content
- Compute content hash (integrity verification)
- Build line index for evidence grounding

### 2. Extract
- Find candidate values using:
  - Rule-based patterns (regex, field definitions)
  - LLM-based extraction (optional)
- Candidates are unverified at this stage

### 3. Ground
- Map each candidate to exact document span
- Record: quote text, line range, page number
- Verify evidence integrity (hash check)

### 4. Judge (STOP-first)
- Apply decision rules in priority order:
  1. No candidates → STOP
  2. Conflicting candidates → STOP
  3. Low confidence → STOP or NEED_REVIEW
  4. Evidence integrity failure → STOP
  5. All checks pass → ACCEPT

### 5. Archive
- Write immutable artifacts:
  - Extraction decisions (`.jsonl`)
  - Manifest with metadata (`.json`)
- Include timestamps and reproducibility hashes

---

## Decision Taxonomy

### ACCEPT
- Evidence found
- Confidence sufficient
- Integrity verified
- Includes: value, evidence object, confidence score

### STOP
- Evidence insufficient, conflicting, or missing
- Includes: reason, negative proof (what was checked)
- Triggers manual review

### NEED_REVIEW
- Edge cases requiring human judgment
- Evidence present but ambiguous
- Routes to review queue

---

## Evidence Structure

Every ACCEPT decision includes grounded evidence:

```json
{
  "value": "01/15/2025",
  "evidence": {
    "quote": "Effective Date: 01/15/2025",
    "page": 1,
    "line_range": [15, 15],
    "integrity_hash": "a3f2..."
  },
  "confidence": 0.95
}
```

Every STOP decision includes negative proof:

```json
{
  "decision": "STOP",
  "reason": "no_candidates_found",
  "negative_proof": {
    "searched": ["effective_date"],
    "checked_scope": "entire document",
    "found": []
  }
}
```

---

## Viewer

The HTML viewer (`viewer/`) visualizes:
- Evidence highlighting in document
- STOP reasoning with searched locations
- Negative proof as audit artifact

Generate viewer:
```bash
python viewer/viewer_generator.py examples/stop_example.txt
```

---

## Key Design Principles

1. **STOP-first**: Judgment rules prioritize stopping over guessing
2. **Evidence grounding**: All ACCEPT decisions must reference exact document spans
3. **Negative proof**: STOP decisions document what was checked
4. **Immutable artifacts**: All decisions written once, never modified
5. **Advisory semantics**: System produces judgments, not enforcement

---

## Extension Points

- `engine/extract.py`: Add custom extraction rules
- `engine/judge.py`: Modify judgment thresholds
- `schema/extraction_schema.json`: Define fields and requirements

**Note**: Changes to judgment logic require careful testing against adversarial cases.
