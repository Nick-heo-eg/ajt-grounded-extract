# Security Policy

## What This Document Is NOT

**This is not a claim of security or safety.**

This document explains:
- What threats are modeled
- How modeled threats are blocked
- How to report constitutional bypasses

**We do not claim "secure" or "safe". We demonstrate how specified attacks are blocked.**

---

## Threat Model

This system is designed to block these attack vectors:

1. **Linguistic bypass** — Relabeling actions to avoid admission
2. **Context reuse** — Reusing authorization across contexts
3. **Partial proof** — Passing with incomplete evidence
4. **Scope expansion** — Extending authorization beyond boundary
5. **Authority laundering** — Transferring or aggregating responsibility

**Attack test results**: 10 scenarios tested, 0 exploits successful.

See: `ATTACK_TEST.md` for full adversarial verification.

---

## Out of Scope

The following are **NOT** in the threat model for v1.0:

- Timing attacks
- Resource exhaustion (DoS)
- Side-channel attacks
- Cryptographic vulnerabilities (no crypto used)
- Network-level attacks
- Physical access attacks
- Social engineering

**We do not claim protection against threats outside the model.**

---

## What We Guarantee

This system guarantees:

1. **Stoppability** — DEFAULT: STOP enforced
2. **Traceability** — decision_maker required and logged
3. **Scope containment** — Tokens bound to context, reuse forbidden
4. **Audit trail** — Write-once logs with tamper-evident hashing

**These guarantees are derived from attack tests, not claimed.**

---

## What We Do NOT Guarantee

This system does NOT guarantee:

- ❌ Correctness of extracted values
- ❌ Completeness of extraction
- ❌ Performance or availability
- ❌ Protection from all possible attacks
- ❌ Legal compliance (consult your counsel)

**Optimizing for recall or accuracy is a non-goal.**

---

## Reporting a Constitutional Bypass

If you discover an attack that successfully bypasses the constitution:

### What is a Bypass?

A bypass is an attack that:
- Circumvents `CAN_PROCEED` check
- Reuses tokens across contexts
- Passes with partial proof
- Expands scope after admission
- Uses anonymous decision_maker

**Not a bypass**: Performance issues, UX problems, documentation gaps.

### How to Report

**Do not open public issue for bypasses.**

1. Email: [Placeholder - add security contact]
2. Subject: `[BYPASS] Brief description`
3. Include:
   - Attack scenario
   - Steps to reproduce
   - Expected block point
   - Actual behavior
   - Proposed fix (optional)

### Response Timeline

- Acknowledgment: Within 48 hours
- Initial assessment: Within 7 days
- Fix (if confirmed): Within 30 days
- Public disclosure: After fix released

### What Happens Next

If bypass is confirmed:
1. We create a patch
2. We add attack to `ATTACK_TEST.md`
3. We increment version (v1.0.x or v1.1.0 depending on severity)
4. We credit reporter (if desired)

**We do not pay bounties.** This is an open-source project.

---

## Supported Versions

| Version | Supported | Constitution Status |
|---------|-----------|---------------------|
| 1.0.x   | ✅ Yes     | Frozen |
| 0.x.x   | ❌ No      | Pre-constitution |

**Only v1.0+ receives security updates.**

---

## False Reports

If you report something that is not a constitutional bypass:

- We will explain why it's not a bypass
- We may suggest opening a public issue instead
- No penalty for false reports made in good faith

**We appreciate responsible disclosure.**

---

## Disclosure Philosophy

We practice **coordinated disclosure**:

1. Reporter notifies us privately
2. We confirm and fix
3. We release fix
4. We disclose publicly with credit

**We do not suppress valid bypass reports.**

---

## Legal Safe Harbor

If you:
- Report bypasses in good faith
- Do not exploit bypasses for harm
- Follow responsible disclosure process

We will not take legal action against you.

**This is not legal advice. Consult your own counsel.**

---

## Questions?

For non-bypass security questions:
- Open public issue with `[Security Question]` prefix

For bypass reports only:
- Use private email process above

---

**Last Updated**: 2026-01-06
**Version**: 1.0
**Constitution**: ADMISSION_CONSTITUTION.md v1.0
