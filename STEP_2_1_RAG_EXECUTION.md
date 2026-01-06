# Step ②-1: RAG Read-Only Execution

**Status**: Minimal controlled execution

**Philosophy**: This is NOT intelligent RAG. This is **controlled retrieval** where execution happens only after admission and token validation.

---

## What This Is

The first action that actually executes in this system.

**Flow**:
```
request → admission → token validation → retrieval → raw evidence → STOP
```

NO synthesis. NO chaining. NO downstream actions.

---

## What Changed from ②-0

| Component | ②-0 | ②-1 |
|-----------|-----|-----|
| Admission | ✅ Proven | ✅ Used (frozen) |
| Token validation | ❌ Not implemented | ✅ Implemented |
| Retrieval | ❌ Not implemented | ✅ Minimal grep-like |
| Evidence return | ❌ No execution | ✅ Raw snippets only |
| Synthesis | ❌ Not possible | ❌ Still not possible |

---

## Components

### execution/token_validator.py

Enforces at execution time:
1. action == "rag_read"
2. scope == "read_only"
3. reuse == "forbidden"
4. auto_revoke_on_context_change == true
5. context_hash matches query (auto-derived)

**ANY failure → STOP.**

### execution/retriever.py

Minimal read-only retriever:
- Scans `.md` and `.txt` files in corpus directory
- Returns snippets containing query terms
- NO external dependencies
- NO vector database
- NO LLM
- NO ranking
- Pure grep-like search

**Purpose**: Prove control, not capability.

### execution/rag_read_gate.py

Full flow orchestration:
1. Call admission (from frozen ②-0)
2. Validate token
3. Execute retrieval (if valid)
4. Return raw evidence

**NO synthesis** after retrieval.
**NO chaining** to other actions.

---

## Guarantees (DoD Met)

### 1. NO_SYNTHESIS ✅

Evidence returned as-is. No summarization, no conclusion generation.

```python
return {
    "allowed": True,
    "reason": "RAG_READ_EXECUTED_READ_ONLY",
    "token": token,
    "evidence": [{"source": str, "snippet": str}]  # Raw only
}
```

### 2. NO_CHAINING ✅

`rag_read_gate.py` returns and stops. No automatic follow-up actions.

### 3. AUDIT_READY ✅

Every outcome has machine-readable reason:
- Admission failure: reason from ②-0
- Token validation failure: specific validation error
- Success: "RAG_READ_EXECUTED_READ_ONLY"

---

## Demo

```bash
python demos/rag_exec_pass.py
```

**Expected output**:
- ALLOWED: True
- REASON: RAG_READ_EXECUTED_READ_ONLY
- TOKEN: validated
- EVIDENCE: 3-5 raw snippets from docs/

**What it proves**:
- ✅ Admission controls execution
- ✅ Token validation works
- ✅ Retrieval executes only when authorized
- ✅ No synthesis happens
- ✅ No chaining occurs

---

## What This Does NOT Prove

- ❌ Retrieval quality
- ❌ Relevance ranking
- ❌ Performance vs other RAG systems
- ❌ Production scalability

**This proves execution can be controlled, not that execution is good.**

---

## Comparison to Standard RAG

| Standard RAG | This System |
|--------------|-------------|
| Query → Retrieve → Synthesize | Query → Admit → Validate → Retrieve → **STOP** |
| Retrieval is default | Retrieval requires proof |
| Token not required | Token required + validated |
| Results auto-synthesized | Results returned raw |
| Chaining possible | Chaining forbidden |

---

## Next Step (②-2)

Audit logging for:
- Admission decisions (allow/deny)
- Token issuance
- Retrieval execution
- Evidence provenance

**Not started yet. Current step: ②-1 complete.**

---

## Running the Demo

```bash
# Full execution with evidence return
python demos/rag_exec_pass.py

# Compare with admission-only (no execution)
python demos/rag_attempt_pass.py  # ②-0: token issued, no retrieval
```

**Key difference**:
- ②-0: Proves admission can issue token
- ②-1: Proves token enables controlled execution

---

## Architecture

```
Layer ①: Judgment (FROZEN)
  └─ ADMISSION_CONSTITUTION.md
  └─ ATTACK_TEST.md

Layer ②-0: Admission (FROZEN)
  └─ admission/rules_rag_read.py
  └─ actions/rag_read.yaml
  └─ demos/rag_attack_*.py

Layer ②-1: Execution (THIS STEP)
  └─ execution/token_validator.py
  └─ execution/retriever.py
  └─ execution/rag_read_gate.py
  └─ demos/rag_exec_pass.py
```

---

## Principle Demonstrated

> **"Retrieval is not a right. It's a conditional action that executes only when judgment allows."**

This is the first time in this system that something actually **executes**.

And it only executes because:
1. Admission approved
2. Token validated
3. Scope locked to read_only
4. Context hash matched

**This is controlled execution, not intelligent execution.**

---

**Version**: 0.1.0
**Dependencies**: ②-0 (frozen)
**Constitution**: ADMISSION_CONSTITUTION.md v1.0
**Date**: 2026-01-07

---

**"We do not make retrieval smarter. We make retrieval conditional."**
