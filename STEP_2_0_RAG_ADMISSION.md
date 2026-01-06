# Step ②-0: RAG Read-Only Admission

**Status**: Experimental verification of constitutional control over action

**Philosophy**: This is NOT a RAG system. This is a **conditional authorization experiment** for read-only retrieval.

---

## What This Is

A minimal structure to verify that:
- ① (Judgment structure) can control ② (Action structure)
- Constitution blocks attacks before they reach execution
- Failure is a normal outcome, not an error

---

## What This Is NOT

- ❌ Production RAG system
- ❌ Feature addition
- ❌ Performance optimization
- ❌ "Better AI"

---

## Action Definition

```yaml
action: rag_read
capability: read_only_retrieval
side_effects: forbidden
```

**Scope locked**: No execution, no state mutation, no downstream actions.

---

## Admission Rules

File: `admission/rules_rag_read.py`

**Required fields** (ALL must be proven):
1. `decision_maker` — Traceable identity
2. `why` — Purpose statement
3. `scope` — Must be `read_only`
4. `query` — The retrieval request

**Constitutional controls enforced**:
- ✅ DEFAULT: STOP (unless ALL conditions proven)
- ✅ context_hash auto-derived (manual supply → REJECT)
- ✅ Token issued only if ALL conditions proven
- ✅ Token properties:
  - `scope: read_only`
  - `reuse: forbidden`
  - `auto_revoke_on_context_change: true`

---

## Demo Results

### Legitimate Cases

| Demo | Result | Reason |
|------|--------|--------|
| `rag_attempt_fail.py` | STOP | Missing decision_maker |
| `rag_attempt_pass.py` | Token issued | ALL conditions proven |

### Attack Cases

| Attack | Result | Constitutional Block |
|--------|--------|---------------------|
| `rag_attack_1_manual_hash.py` | BLOCKED | context_hash must be auto-derived |
| `rag_attack_2_scope_escalation.py` | BLOCKED | Only read_only scope allowed |
| `rag_attack_3_token_reuse.py` | BLOCKED | context_hash mismatch (different query) |

**Attack test results**: 3/3 blocked ✅

---

## What This Proves

1. **Constitution controls action** — Admission rules block attacks before execution
2. **Failure is normal** — STOP is a valid outcome, not an error
3. **Token is conditional** — Authorization is not a right, it's a grant
4. **Hash derivation works** — Manual injection rejected, reuse prevented

---

## What This Does NOT Prove

- ❌ RAG quality or accuracy
- ❌ Performance vs other RAG systems
- ❌ Production readiness for retrieval

**This experiment only proves control mechanisms work.**

---

## Next Steps (Possible)

**A️⃣** Connect token to actual vector search function (Step ②-1)
**B️⃣** Add audit logging for admission decisions
**C️⃣** Create additional attack scenarios

**Current recommendation**: Stop here. Observe. Let structure settle.

This is not a race. This is verification that ① can control ②.

---

## Running Demos

```bash
# Legitimate cases
python demos/rag_attempt_fail.py    # STOP (missing field)
python demos/rag_attempt_pass.py    # Token issued

# Attack cases
python demos/rag_attack_1_manual_hash.py      # Manual hash injection → BLOCKED
python demos/rag_attack_2_scope_escalation.py # Scope escalation → BLOCKED
python demos/rag_attack_3_token_reuse.py      # Token reuse → BLOCKED
```

**Expected behavior**: All attacks blocked, legitimate pass case issues token.

---

## Principle Demonstrated

> **"RAG is not a capability. It's a privilege granted by proven conditions."**

This structure does not make retrieval better.
It makes retrieval **conditional on authorization**.

---

**Version**: 0.1.0 (Experimental)
**Constitution**: ADMISSION_CONSTITUTION.md v1.0
**Date**: 2026-01-07

---

**"We are not building smarter AI. We are building AI that knows when to stop asking."**
