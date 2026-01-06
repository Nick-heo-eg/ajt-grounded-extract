# Step ②-2: Audit Logging

**Status**: Minimal audit証明 (proof, not interpretation)

**Philosophy**: This does NOT make the system smarter. It makes STOP **explainable**.

---

## What This Is

Structured logging of **why system stopped**, not what it did.

**Flow** (unchanged from ②-1):
```
request → admission → validation → retrieval → raw evidence → STOP
```

**What changed**: Audit event emitted at each decision point.

---

## Design Origin

From **②-1b Silent Verification** (10 queries, 100% observation):

3 convergence points identified:
1. **Point A**: Post-retrieval synthesis urge (9/10 queries)
   → Need: WHY synthesis forbidden
2. **Point B**: Scope mismatch detection (3/10 queries)
   → Need: Intent vs granted scope
3. **Point C**: Evidence count = 0 (10/10 queries)
   → Need: WHY no results

**Design principle**: Log only what observation demanded.

---

## Audit Event Schema

```json
{
  "timestamp": "2026-01-06T19:10:49.575411",
  "proof_id": "b56f1041-6c60-44b6-a898-9bdbae53e938",
  "action": "rag_read",
  "decision_maker": "tester",

  "admission": {
    "allowed": true,
    "reason_code": "RAG_READ_EXECUTED_READ_ONLY",
    "constitutional_rule": "NO_SYNTHESIS"
  },

  "intent_vs_scope": {
    "detected_intent": "synthesis",
    "granted_scope": "read_only",
    "scope_mismatch": true
  },

  "retrieval": {
    "evidence_count": 0,
    "zero_results_reason": "language_mismatch"
  },

  "next_action_hint": {
    "suggested_scope": "synthesis",
    "required_action": "request_new_action"
  }
}
```

---

## Components

### audit/intent_detector.py

Lightweight heuristic for detecting user intent from query.

**NOT intelligent NLP**. Only for mismatch detection.

Returns: `"synthesis" | "execution" | "analysis" | "retrieval_only"`

```python
def detect_intent(query: str) -> str:
    q = query.lower()
    if any(k in q for k in ["요약", "결론", "합쳐", "summary"]):
        return "synthesis"
    if any(k in q for k in ["실행", "보내", "execute"]):
        return "execution"
    if any(k in q for k in ["분석", "허점", "analyze"]):
        return "analysis"
    return "retrieval_only"
```

---

### audit/reason_map.py

Maps constitutional rules to human explanations.

```python
REASON_EXPLANATION = {
    "NO_SYNTHESIS": {
        "human": "Synthesis is forbidden by constitution for read_only scope.",
        "how_to_proceed": "Request a new action with scope: synthesis.",
        "constitutional_reference": "STEP_2_1_RAG_EXECUTION.md - DoD: NO_SYNTHESIS"
    },
    # ...
}
```

---

### execution/rag_read_gate.py (patched)

3 audit points added:

1. **Admission failed**: Logs `ADMISSION_FAILED`
2. **Token validation failed**: Logs `TOKEN_CONSTRAINT`
3. **Post-retrieval STOP**: Logs `NO_SYNTHESIS` + intent analysis + evidence provenance

**Total lines added**: 35 (within 30-line guideline + imports)

**Lines changed**: 0 (only additions)

---

## Example Audit Logs

### Case 1: Synthesis intent detected

Query: "검색 결과를 합쳐서 한 문장으로"

```json
{
  "constitutional_rule": "NO_SYNTHESIS",
  "intent_vs_scope": {
    "detected_intent": "synthesis",
    "granted_scope": "read_only",
    "scope_mismatch": true
  },
  "retrieval": {
    "evidence_count": 0,
    "zero_results_reason": "language_mismatch"
  },
  "next_action_hint": {
    "suggested_scope": "synthesis",
    "required_action": "request_new_action"
  }
}
```

**Human interpretation**:
- User requested synthesis
- System granted read_only scope
- Mismatch detected
- No results (Korean query, English corpus)
- User should request new action with scope: synthesis

---

### Case 2: Retrieval only (no mismatch)

Query: "DEFAULT STOP"

```json
{
  "constitutional_rule": "NO_SYNTHESIS",
  "intent_vs_scope": {
    "detected_intent": "retrieval_only",
    "granted_scope": "read_only",
    "scope_mismatch": false
  },
  "retrieval": {
    "evidence_count": 3,
    "zero_results_reason": null
  },
  "next_action_hint": {
    "suggested_scope": null,
    "required_action": null
  }
}
```

**Human interpretation**:
- User requested retrieval only
- System granted read_only scope
- No mismatch
- 3 evidence items returned
- No further action needed

---

## What This Proves (DoD Met)

### Point A: Constitutional STOP explanation ✅

```json
"constitutional_rule": "NO_SYNTHESIS"
```

Maps to human explanation via `reason_map.py`:
- WHY: "Synthesis is forbidden by constitution for read_only scope"
- HOW: "Request a new action with scope: synthesis"

---

### Point B: Intent vs scope mismatch ✅

```json
"intent_vs_scope": {
  "detected_intent": "synthesis",
  "granted_scope": "read_only",
  "scope_mismatch": true
}
```

Logs show:
- What user intended (synthesis)
- What system granted (read_only)
- Whether mismatch occurred (true)

---

### Point C: Evidence provenance ✅

```json
"retrieval": {
  "evidence_count": 0,
  "zero_results_reason": "language_mismatch"
}
```

Logs show:
- How many results (0)
- WHY zero (language mismatch)
- Reproducible diagnosis

---

## What This Does NOT Do

- ❌ Interpret user intent with LLM
- ❌ Change system behavior
- ❌ Add new actions or scopes
- ❌ Make claims about safety
- ❌ Log evidence content (privacy)
- ❌ Log synthesis results (none exist)

**This only logs control decisions.**

---

## Comparison to Standard Systems

| Standard RAG | This System |
|--------------|-------------|
| Logs results | Logs decisions |
| "Retrieved 5 docs" | "Retrieved 5 docs, synthesis forbidden" |
| No stop reason | Constitutional rule + next action hint |
| No intent analysis | Intent vs scope mismatch logged |
| Silent 0 results | Zero results reason classified |

---

## Testing

```bash
# Retrieval only (no mismatch)
python demos/rag_exec_pass.py

# Synthesis intent (mismatch detected)
python test_audit_synthesis.py
```

**Expected**: Structured JSON audit log to stdout for every execution.

---

## DoD Verification

- [x] A: Constitutional STOP reason in human language
- [x] B: Intent vs scope mismatch logged
- [x] C: Evidence provenance logged (count + zero reason)
- [x] Third party can understand from log alone

**Result**: ②-2 complete.

---

## Architecture

```
Layer ①: Judgment (FROZEN since v1.0.0)
  └─ ADMISSION_CONSTITUTION.md

Layer ②-0: Admission (FROZEN since v2.0.0-step2.0)
  └─ admission/rules_rag_read.py

Layer ②-1: Execution (v0.1.0)
  └─ execution/rag_read_gate.py

Layer ②-2: Audit (THIS STEP)
  └─ audit/intent_detector.py
  └─ audit/reason_map.py
  └─ execution/rag_read_gate.py (patched)
```

---

## Principle Demonstrated

> **"We do not make retrieval smarter. We make STOP explainable."**

From observation:
- Reason codes were machine-readable but human-incomprehensible
- Users confused why synthesis forbidden
- Users confused why 0 results

Now:
- Constitutional rule logged
- Intent mismatch logged
- Zero results reason logged

**Third party can audit without asking developer.**

---

**Version**: 0.1.0
**Dependencies**: ②-1 (execution), ②-1b (silent verification)
**Constitution**: ADMISSION_CONSTITUTION.md v1.0
**Date**: 2026-01-07

---

**"Logs prove decisions. They do not interpret them."**
