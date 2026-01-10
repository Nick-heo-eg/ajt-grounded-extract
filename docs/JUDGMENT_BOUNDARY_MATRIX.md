# Judgment Boundary Matrix

This document enumerates behaviors that **AJT-Grounded-Extract will explicitly NOT perform**, even if requested.

These boundaries are enforced **structurally**, not by policy, prompt, or operator intent.
They are verified by STOP outcomes with negative proof artifacts.

This document is normative for this repository.

---

## Purpose

Most AI systems define what they try to do.
This system defines **where it must stop**.

The goal of this matrix is to make non-capabilities explicit, auditable, and non-negotiable.

---

## Judgment Boundary Matrix

| Attempted Behavior | Typical AI System | AJT-Grounded-Extract | Result |
|-------------------|------------------|---------------------|--------|
| Infer missing values | Guess or fill defaults | STOP | `no_candidates_found` |
| Resolve conflicting evidence | Select one heuristically | STOP | `conflicting_values` |
| Apply business or legal logic | Implicit evaluation | STOP | `out_of_scope` |
| Override low confidence | Extract anyway | STOP | `confidence_below_threshold` |
| Assume implicit defaults | Silent completion | STOP | `no_explicit_evidence` |
| Perform temporal reasoning | Infer dates from context | STOP | `inferential_rejection` |
| Evaluate conditional clauses | Logical resolution | STOP | `requires_external_state` |
| Execute or enforce outcomes | Trigger actions | NEVER | Not supported |
| Decide on behalf of caller | Autonomous decision | NEVER | Not supported |

---

## Interpretation Rules

- **STOP is the correct and successful outcome** when a boundary is reached.
- STOP indicates intentional non-execution with preserved evidence.
- No boundary in this matrix can be overridden by configuration, prompt, or retry.

---

## Why This Matters

Explicit boundaries prevent:
- Silent liability
- Implicit responsibility transfer
- Hallucinated certainty

They enable:
- Audit-ready explanations
- Clear responsibility ownership
- Trust through predictable refusal

This system prefers **provable silence** over unsupported answers.

---

## Non-Goals (Explicit)

This system will never:

- Decide for the caller
- Execute downstream actions
- Resolve ambiguity heuristically
- Optimize for recall over evidence integrity
- Claim regulatory compliance

These constraints are intentional and permanent.

---

## Relationship to Other Documents

- STOP semantics: see [STOP_SEMANTICS.md](STOP_SEMANTICS.md)
- Output structure: see [OUTPUT_FORMAT.md](OUTPUT_FORMAT.md)
- Adversarial verification: see [ATTACK_TESTS.md](ATTACK_TESTS.md)
- Architectural flow: see [ARCHITECTURE.md](ARCHITECTURE.md)

---

## Boundary Guarantee

If this system produces an output,
one of the following is always true:

- An **ACCEPT** decision with document-grounded evidence
- A **STOP** decision with negative proof explaining why extraction did not proceed

There is no third path.

---

**Principle**
Extract only when it can be proven.
Otherwise, stop — and prove that you stopped.
