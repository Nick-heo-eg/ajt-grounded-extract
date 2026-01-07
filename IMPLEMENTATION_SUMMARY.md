# Implementation Summary: AJT Grounded Extract

**Status**: ✅ Complete
**Repository**: https://github.com/Nick-heo-eg/ajt-grounded-extract
**Visibility**: Public
**Date**: 2026-01-05

---

## Task Completion

### ✅ All Acceptance Criteria Met

1. **Demo shows ACCEPT and STOP**
   - `examples/accept_example.txt` → ACCEPT (found "Effective Date: 01/15/2025")
   - `examples/stop_example.txt` → STOP (no explicit effective date found)

2. **STOP includes explicit reason + preserved artifacts**
   - Stop reason: `no_candidates_found`
   - Stop proof: `{"searched": true, "candidates_found": 0}`
   - Artifacts archived in `evidence/manifest_*.json`

3. **Viewer navigates evidence spans correctly**
   - Green highlighting for ACCEPT spans
   - Red highlighting for STOP areas
   - "Why Stopped" panel with proof details
   - Sidebar navigation by field

4. **README states non-goals and STOP-first philosophy**
   - Philosophy section emphasizes evidence integrity > recall
   - Non-goals explicitly listed (no multi-domain, no fine-tuning, etc.)
   - STOP-first decision logic documented

---

## Architecture Delivered

### Pipeline Stages
```
Document → Ingest → Extract → Ground → Judge → Archive → Viewer
```

### Core Modules

| Module | File | Purpose |
|--------|------|---------|
| **Ingest** | `engine/ingest.py` | Load, hash, index document |
| **Extract** | `engine/extract.py` | Find candidate values (rule-based) |
| **Ground** | `engine/ground.py` | Map values to document spans |
| **Judge** | `engine/judge.py` | STOP-first decision engine |
| **Archive** | `engine/archive.py` | Write-once evidence artifacts |
| **Viewer** | `viewer/viewer_generator.py` | HTML evidence viewer |
| **Pipeline** | `engine/pipeline.py` | End-to-end orchestration |

---

## Demo Verification

### ACCEPT Case
```bash
$ python run.py examples/accept_example.txt
→ Decision: ACCEPT
→ Value: 01/15/2025
→ Confidence: 0.90
→ Evidence: "01/15/2025"
```

### STOP Case
```bash
$ python run.py examples/stop_example.txt
→ Decision: STOP
→ Reason: no_candidates_found
→ Proof: {"searched": true, "candidates_found": 0}
```

---

## Evidence Artifacts

Every extraction creates:
- `extraction_*.jsonl`: Line-delimited results
- `manifest_*.json`: Metadata + integrity hashes
- `*_viewer.html`: Interactive HTML viewer

All artifacts include:
- Document content hash (SHA-256)
- Trace signature (tamper detection)
- Timestamp (UTC, ISO 8601)

---

## Decision Taxonomy

| Decision | Meaning | When Applied |
|----------|---------|--------------|
| **ACCEPT** | Evidence found, verified, high confidence | All checks pass |
| **STOP** | Missing/conflicting/low-quality evidence | Any check fails |
| **NEED_REVIEW** | Edge case requiring human judgment | (Future use) |

### STOP Reasons

- `no_candidates_found`: No extraction candidates detected
- `conflicting_values`: Multiple different values found
- `insufficient_confidence`: Below min threshold (0.7)
- `missing_evidence`: No document span mapping
- `evidence_integrity_failed`: Quote/offset mismatch

---

## Reference Link

Inspired by: **[ajt-negative-proof-sim](https://github.com/Nick-heo-eg/ajt-negative-proof-sim)**
(Echo Judgment System)

Core principle: **Prove extraction succeeded OR prove why you stopped.**

---

## File Count

- **22 files** committed
- **1,371 lines** of code/docs
- **0 dependencies** (pure Python stdlib)

---

## Constraints Honored

✅ No modification to `ajt-negative-proof-sim` (sealed reference)
✅ Evidence integrity > recall
✅ Default behavior: STOP when evidence insufficient
✅ No fine-tuning
✅ Runnable locally
✅ Minimal dependencies (zero external packages)

---

**Task ID**: AJT-GROUNDED-EXTRACT-V0
**Execution**: Complete
