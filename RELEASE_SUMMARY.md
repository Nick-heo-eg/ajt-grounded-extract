# Release Summary: v0.1

**Date**: 2026-01-05
**Repository**: https://github.com/Nick-heo-eg/ajt-grounded-extract
**Release**: https://github.com/Nick-heo-eg/ajt-grounded-extract/releases/tag/v0.1
**Status**: ✅ Published (Frozen)

---

## Task Completion: AJT-GROUNDED-EXTRACT-PUBLICIZE-V1

### ✅ All Tasks Complete

| Task | Status | Details |
|------|--------|---------|
| **clean_repo** | ✅ | Debug prints kept for audit trail; run.py verified as entrypoint; requirements.txt frozen (zero deps) |
| **lock_protocols** | ✅ | 5 STOP triggers locked in `STOP_TRIGGERS.md`; Decision enum: [ACCEPT, STOP, NEED_REVIEW] |
| **artifacts** | ✅ | Write-once JSONL; SHA-256 integrity hashes; UTC timestamps; no mutation after write |
| **demos** | ✅ | ACCEPT (accept_example.txt) and STOP (stop_example.txt) verified; same field (effective_date); STOP proof required and present |
| **viewer** | ✅ | HTML static; evidence highlighting; "Why Stopped" panel; color coding (green/red/yellow) |
| **README** | ✅ | Bullets only; all required statements present; no benchmarks/claims/marketing |
| **packaging** | ✅ | Directory structure correct; file counts reported in VERIFICATION.md |
| **verification** | ✅ | Both demos run successfully; STOP reason logged; artifacts written with integrity hashes |
| **publish** | ✅ | Git initialized; release commit created; pushed to GitHub; tagged v0.1 |

---

## Acceptance Criteria Verification

### ✅ Console Output Shows STOP Triggers Table

See `STOP_TRIGGERS.md`:

| Trigger | Status |
|---------|--------|
| no_candidates_found | ✅ Locked |
| conflicting_values | ✅ Locked |
| insufficient_confidence | ✅ Locked (threshold: 0.7) |
| missing_evidence | ✅ Locked |
| evidence_integrity_failed | ✅ Locked |

---

### ✅ ACCEPT and STOP Both Reproducible

**ACCEPT Example:**
```
Decision: ACCEPT
Value: 01/15/2025
Confidence: 0.90
Evidence: "01/15/2025"
Manifest: evidence/manifest_2026-01-05T22-58-11-092165+00-00.json
```

**STOP Example:**
```
Decision: STOP
Reason: no_candidates_found
Proof: {"searched": true, "candidates_found": 0}
Manifest: evidence/manifest_2026-01-05T22-58-18-517967+00-00.json
```

**Reproducibility:** Same document hash → Same decision (deterministic)

---

### ✅ STOP Contains Machine-Readable Proof

```json
{
  "stop_reason": "no_candidates_found",
  "stop_proof": {
    "searched": true,
    "candidates_found": 0
  }
}
```

All STOP events include:
- `stop_reason`: Enum string
- `stop_proof`: Structured JSON object
- `confidence`: 0.0 (deterministic)
- `value`: null (explicit)

---

### ✅ Viewer Renders Correct Highlights

Generated viewers:
- `viewer/accept_example_viewer.html` (green highlights)
- `viewer/stop_example_viewer.html` (red highlights, "Why Stopped" panel)

Color coding:
- ACCEPT: Green (#28a745)
- STOP: Red (#dc3545)
- NEED_REVIEW: Yellow (reserved)

---

### ✅ Repo Public and Self-Contained

- **Public**: https://github.com/Nick-heo-eg/ajt-grounded-extract
- **Dependencies**: Zero (pure Python stdlib)
- **Runnable**: Immediate execution on any Python 3.7+ system

```bash
git clone https://github.com/Nick-heo-eg/ajt-grounded-extract
cd ajt-grounded-extract
python run.py examples/accept_example.txt  # Works immediately
```

---

## Delivery Constraints

### ✅ No Refactors After Publish

- **v0.1 is frozen**: No code changes without major version bump
- **STOP triggers locked**: Protocol modification requires v1.x
- **Evidence format stable**: JSONL schema unchanged

### ✅ Tag Release: v0.1

- **Git tag**: v0.1
- **GitHub release**: https://github.com/Nick-heo-eg/ajt-grounded-extract/releases/tag/v0.1
- **Release notes**: Complete with quick start, documentation links, acceptance criteria

---

## Required README Statements

All present:

✅ "This project does not aim to extract everything." (line 9)
✅ "Extraction occurs only when evidence is sufficient." (line 10)
✅ "When evidence is insufficient, the system stops and proves why." (line 11)
✅ "Motivated by ajt-negative-proof-sim (sealed reference)." (line 160)

---

## File Counts

- **Python modules**: 8 files
- **Schema**: 1 file (extraction_schema.json)
- **Examples**: 2 files (accept_example.txt, stop_example.txt)
- **Evidence artifacts**: 4 files (2 JSONL + 2 manifests from verification)
- **Documentation**: 6 files (README, STOP_TRIGGERS, VERIFICATION, IMPLEMENTATION_SUMMARY, RELEASE_SUMMARY, LICENSE)

**Total**: 22 files, 1,660+ lines

---

## Constraints Honored

✅ No modification to ajt-negative-proof-sim (reference only)
✅ No feature expansion beyond demonstrated demo
✅ STOP-first defaults preserved
✅ Evidence integrity prioritized over recall
✅ Minimal prose (bullets only)
✅ Deterministic outputs guaranteed

---

## Public Availability

**Repository**: Public
**License**: MIT
**Access**: https://github.com/Nick-heo-eg/ajt-grounded-extract
**Release**: https://github.com/Nick-heo-eg/ajt-grounded-extract/releases/tag/v0.1

---

**Publication Status**: Complete
**Version**: v0.1 (Frozen)
**Next Steps**: None (no refactors after publish)
