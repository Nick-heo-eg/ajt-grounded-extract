# Release Notes: v1.0

**This release does not add capabilities. It fixes the conditions under which any capability may exist.**

---

## 0. Declaration

This release is not a feature release.

This release **fixes the constitution governing when and how judgment, action, or generation may be permitted.**

All future capabilities are bound by this constitution and **cannot circumvent it.**

---

## 1. Admission Constitution (Core)

The complete constitution is defined in: **[ADMISSION_CONSTITUTION.md](./ADMISSION_CONSTITUTION.md)**

No summary. No interpretation. The full text is authoritative.

**Core principles**:
- **DEFAULT: STOP**
- **OVERRIDE: Only if ALL conditions proven**
- **Scope-bound, non-reusable autonomy only**

---

## 2. Threat Model

This system is designed to prevent the following five attack vectors:

1. **Linguistic bypass** — Relabeling actions to avoid admission
2. **Context reuse** — Reusing authorization across different contexts
3. **Partial proof** — Passing admission with incomplete evidence
4. **Scope expansion** — Extending authorization beyond original boundary
5. **Authority laundering** — Transferring or aggregating responsibility

**Threats outside this model are out of scope for v1.0.**

---

## 3. Attack Test Results (Proof)

The constitution was tested against 10 adversarial scenarios designed to exploit the five threat vectors.

**Result: 10 attempts / 0 successful attacks**

Full test documentation: **[ATTACK_TEST.md](./ATTACK_TEST.md)**

### Attack-to-Defense Mapping

| Attack Vector | Blocked At | Mechanism |
|---------------|------------|-----------|
| Preview bypass | Interface definition | Action includes recommendation/generation |
| Metadata bypass | Interface definition | Output intended for decision-making |
| Same context claim | Context hash validation | Hash derived from input payload |
| Hash collision | Token validation | Manual hash supply invalidates token |
| 2-of-3 proof | Rules section | ANY single failure = immediate STOP |
| Formal empty proof | Rule 1 | decision_maker must be traceable identity |
| Downstream expansion | Token lifecycle | Context change includes downstream usage |
| Time window slide | Context hash | Time window in hash derivation |
| Token transfer | Token validation | Environment identifiers bind token |
| Wrapper repackaging | Interface requirement | Wrapper API is itself gated action |

**No claim of absolute security is made. The constitution blocks the modeled threats as demonstrated by the attack tests above.**

---

## 4. Implementation Reference (Non-normative)

A reference implementation is provided in this repository:
- Python example: `ADMISSION_CONSTITUTION.md` Section 4
- Execution demo: `ajt-grounded-extract` (this repository)

**This is not the specification.** The specification is `ADMISSION_CONSTITUTION.md` Sections 1-3.

Implementation demonstrates:
- Feasibility of constitution enforcement
- Separation of normative rules from implementation details

---

## 5. Security Guarantees (Derived)

From the attack tests above, the following guarantees follow:

- **No action without explicit admission** — Interface bypass blocked
- **No reuse of autonomy across contexts** — Context hash + reuse prohibition enforced
- **No partial responsibility acceptance** — AND logic enforced without fallback
- **No silent scope expansion** — Downstream usage included in context
- **No anonymous decision authority** — Traceable identity required

These are not claims. These are conclusions derived from the attack test results.

---

## 6. Non-Goals

This system does **not** optimize for:
- Output completeness
- Automation maximization
- Correctness guarantees

This system **guarantees**:
- Stoppability (DEFAULT: STOP)
- Traceability (decision_maker requirement)
- Scope containment (context-bound tokens)

**Optimizing for recall or convenience is a non-goal.**

---

## 7. Versioning Policy

**v1.0 status**: The constitution is now **frozen**.

Changes to Sections 1-3 of `ADMISSION_CONSTITUTION.md` require:
- Major version increment (v2.0+)
- New attack test suite
- Explicit justification for constitutional amendment

Implementation updates (Section 4) may occur without version change if constitution remains unmodified.

---

## 8. Files in This Release

| File | Purpose | Status |
|------|---------|--------|
| `ADMISSION_CONSTITUTION.md` | Normative specification | Frozen |
| `ATTACK_TEST.md` | Adversarial verification | Complete |
| `README.md` | Quick start + philosophy | Informative |
| `STOP_TRIGGERS.md` | STOP trigger protocol | Frozen |
| `VERIFICATION.md` | Acceptance criteria verification | Complete |
| `run.py` + `engine/*` | Reference implementation | Non-normative |

---

## 9. Migration from v0.x

**Breaking changes**: None. v1.0 formalizes principles present since v0.1.

**Action required**: None. Existing implementations already conform to constitution.

**New requirement**: Implementations should reference `ADMISSION_CONSTITUTION.md` as authoritative source.

---

## 10. Future Roadmap (Non-committal)

Possible future work (not committed):
- Additional threat models (e.g., timing attacks, resource exhaustion)
- Formal verification tooling
- Reference implementations in other languages
- Audit trail standardization

**None of these require constitutional changes.** The constitution is complete for the modeled threats.

---

## Acknowledgments

This release was developed with:
- Echo Judgment System principles (responsibility-first design)
- ajt-negative-proof-sim reference architecture (negative proof methodology)
- Adversarial testing methodology (attack-driven verification)

Motivated by: [ajt-negative-proof-sim](https://github.com/anthropics/ajt-negative-proof-sim) (sealed reference)

---

**Release Date**: 2026-01-06
**Version**: 1.0.0
**Status**: Production-ready
**License**: MIT

---

**"This release does not claim to be secure. It demonstrates how specified attacks are blocked by the constitution."**
