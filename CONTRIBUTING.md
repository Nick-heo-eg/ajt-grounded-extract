# Contributing to AJT Grounded Extract

Thank you for your interest in contributing.

**Before submitting**: Read `ADMISSION_CONSTITUTION.md`. All contributions must comply with the constitution.

---

## Constitution is Non-Negotiable

The Admission Constitution (`ADMISSION_CONSTITUTION.md`) is **FROZEN** as of v1.0.

### Non-Negotiable Principles

1. **DEFAULT: STOP** — Cannot be changed to DEFAULT: PROCEED
2. **ALL conditions proven** — Cannot be relaxed to SOME conditions
3. **Scope-bound, non-reusable tokens** — Cannot add token reuse or scope expansion
4. **Action definition** — Cannot narrow to exclude generation/recommendation
5. **Context hash derivation** — Cannot allow manual supply

**Any PR that violates these principles will be automatically rejected.**

---

## Frozen Components (Step ②-0)

The following components are **FROZEN** as of v2.0.0-step2.0 (2026-01-07):

- `admission/` directory (all files)
- `actions/rag_read.yaml`
- `demos/rag_attack_*.py` (attack demos)
- `demos/rag_attempt_*.py` (admission demos)
- `STEP_2_0_RAG_ADMISSION.md`

**Why frozen**: These components proved constitutional control over actions. Modifications would invalidate that proof.

**To modify frozen components**:
- Requires version bump to v2.1+ (constitutional amendment)
- Must include updated attack test suite demonstrating continued control
- Any PR modifying frozen files without version bump will be automatically rejected

---

## What We Accept

### ✅ Acceptable Contributions

- Implementation improvements (maintaining constitution compliance)
- Additional language examples (Python, TypeScript, Rust, etc.)
- Documentation clarifications
- Bug fixes that don't weaken constitution
- Performance optimizations that preserve semantics
- Additional attack test scenarios

### ❌ Rejected Contributions

- "Flexibility" features that bypass admission gate
- "Optional" modes that disable STOP-first logic
- Token reuse mechanisms
- Partial proof acceptance
- Anonymous decision_maker support
- Scope expansion features
- Constitution "improvements" that weaken guarantees

---

## Contribution Process

### 1. Check Existing Issues

Before starting work, check if an issue already exists for your proposed change.

### 2. Open an Issue First

For significant changes, open an issue describing:
- What you want to change
- Why it's needed
- How it maintains constitution compliance

**Do not submit PRs without prior discussion for major changes.**

### 3. Write Attack Tests

If your contribution adds new functionality:
- Write adversarial attack scenarios
- Demonstrate how attacks are blocked
- Update `ATTACK_TEST.md`

**No new feature without attack tests.**

### 4. Maintain Zero Dependencies

This project has zero external dependencies. Do not add any.

Exceptions require extraordinary justification and maintainer approval.

### 5. Submit PR

PR must include:
- Description of changes
- Constitution compliance statement
- Attack test updates (if applicable)
- Backward compatibility verification

---

## Attack Test Updates

When adding functionality, follow this process:

1. Write adversarial scenario attempting to exploit new code
2. Demonstrate which constitution section blocks it
3. Add to `ATTACK_TEST.md` in same format
4. Verify 100% block rate maintained

**Attack tests are mandatory for new features.**

---

## Code Style

- Follow existing code structure
- Use type hints where possible
- Keep functions small and focused
- Prioritize clarity over cleverness

**No clever hacks.** This is audit-grade code.

---

## Documentation

- Update relevant .md files for changes
- Use "blocked-by-design" language, not "secure-by-claim"
- Avoid marketing language in technical docs
- Provide examples for new functionality

---

## Legal/Compliance Contributions

For compliance templates or legal language:
- Clearly mark as "example only"
- Do not claim legal validity
- Reference jurisdiction if applicable
- Avoid absolute guarantees

---

## What Happens to Your Contribution

- Code: MIT License (same as project)
- Documentation: MIT License
- Attack scenarios: Incorporated into test suite

By contributing, you agree to these terms.

---

## Questions?

Open an issue with `[Question]` prefix.

**Do not email maintainers directly.** Use public issues for transparency.

---

## Rejection Reasons

Your PR may be rejected if:

1. **Constitution violation** — Weakens any principle
2. **No attack test** — New functionality without adversarial verification
3. **Dependency addition** — Adds external dependencies
4. **Marketing language** — Claims safety/security without proof
5. **Backward incompatibility** — Breaks existing users
6. **Insufficient discussion** — Major change without prior issue

Rejection is not personal. It preserves system integrity.

---

## Emergency Security Issues

If you find a constitutional bypass (attack that succeeds):

1. **Do not open public issue**
2. Email: [Create SECURITY.md for email address]
3. Include: Attack scenario, exploit steps, proposed fix
4. We will respond within 48 hours

**Responsible disclosure is appreciated.**

---

**Thank you for maintaining the integrity of blocked-by-design systems.**

**Version**: 1.0
**Last Updated**: 2026-01-06
