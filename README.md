# AJT Grounded Extract

**Extract structured data only when it can be proven; otherwise stop—and prove that you stopped.**

---

## Philosophy: STOP-first

- **Evidence Integrity > Recall**: Only extract values with verifiable document evidence
- **Default: STOP**: When evidence is insufficient, conflicting, or missing → stop extraction
- **Negative Proof**: Every STOP includes explicit reason + preserved artifacts
- **No Fine-tuning**: Rule-based + LLM extraction without training pipelines
- **Local Execution**: Runs entirely on local machine

---

## What This Is NOT

- ❌ Multi-domain rule engine
- ❌ Enterprise extraction with thresholds
- ❌ Training/fine-tuning pipeline
- ❌ High-recall extraction system

---

## Architecture

```
Document → Ingest → Extract → Ground → Judge → Archive
           ↓        ↓         ↓        ↓        ↓
           Hash     Candidates Evidence STOP?   Artifacts
```

### Pipeline Stages

1. **Ingest**: Load document, compute hash, build line index
2. **Extract**: Find candidate values (rule-based or LLM)
3. **Ground**: Map each value to exact document span (quote + offsets)
4. **Judge**: STOP-first decision: `ACCEPT | STOP | NEED_REVIEW`
5. **Archive**: Write-once artifacts with timestamps + integrity hashes

### Decision Taxonomy

- **ACCEPT**: Evidence found, confidence sufficient, integrity verified
- **STOP**: No candidates, conflict, low confidence, or integrity failure
- **NEED_REVIEW**: Edge cases requiring human judgment

---

## Quick Start

### Run Extraction

```bash
# ACCEPT case (has clear "Effective Date: 01/15/2025")
python run.py examples/accept_example.txt

# STOP case (no explicit effective date)
python run.py examples/stop_example.txt
```

### View Results

Open generated HTML viewer:
```bash
open viewer/accept_example_viewer.html
open viewer/stop_example_viewer.html
```

---

## Output Format

### JSON Result
```json
{
  "field_name": "effective_date",
  "decision": "ACCEPT",
  "value": "01/15/2025",
  "evidence": {
    "quote": "01/15/2025",
    "start": 245,
    "end": 255,
    "line": 12,
    "context": "...Effective Date: 01/15/2025..."
  },
  "confidence": 0.9
}
```

### STOP Event
```json
{
  "field_name": "effective_date",
  "decision": "STOP",
  "value": null,
  "stop_reason": "no_candidates_found",
  "stop_proof": {
    "searched": true,
    "candidates_found": 0
  }
}
```

---

## HTML Viewer Features

- **Evidence Highlighting**: Green (ACCEPT) / Red (STOP)
- **Navigation Sidebar**: Jump to extracted fields
- **"Why Stopped" Panel**: Explicit reasons with proof artifacts
- **Offset Mapping**: Click evidence span → see exact document location

---

## Directory Structure

```
ajt-grounded-extract/
├── schema/              # Field definitions
├── engine/              # Core extraction modules
│   ├── ingest.py
│   ├── extract.py
│   ├── ground.py
│   ├── judge.py
│   └── archive.py
├── viewer/              # HTML viewer generator
├── evidence/            # Write-once artifacts (JSONL + manifests)
├── examples/            # Demo documents
└── run.py               # CLI entry point
```

---

## Evidence Requirements

All extractions must satisfy:

- ✅ `require_exact_quote`: Value must appear verbatim in document
- ✅ `require_offset_mapping`: Quote mapped to byte offsets
- ✅ `stop_on_conflict`: Multiple conflicting values → STOP
- ✅ `min_confidence`: Below threshold → STOP

---

## Acceptance Criteria

- [x] Demo shows at least one ACCEPT and one STOP
- [x] STOP includes explicit reason and preserved artifacts
- [x] Viewer navigates evidence spans correctly
- [x] Non-goals stated explicitly

---

## Reference

Inspired by **[ajt-negative-proof-sim](https://github.com/anthropics/ajt-negative-proof-sim)** (Echo Judgment System).

Core principle: **Prove extraction succeeded OR prove why you stopped.**

---

## License

MIT
