# AJT Core

**AJT (Judgment-Anchored Transparency) Core** is a two-layer architecture for making AI judgment handling auditable.

It does not automate decisions.
It does not prevent actions.
It does not enforce policies.

**It makes ignoring judgments visible.**

---

## What AJT Core Is

AJT Core consists of **exactly two independent layers:**

### Phase 1: Judgment Generation
**Repository:** [ajt-grounded-extract](https://github.com/Nick-heo-eg/ajt-grounded-extract)

**Responsibility:** Produce ACCEPT (with evidence) or STOP (with negative proof) decisions.

**Does:**
- Extract structured data from documents
- Ground extractions in source evidence
- Produce STOP when evidence is insufficient

**Does NOT:**
- Enforce downstream actions
- Make business decisions
- Execute based on judgments

---

### Phase 2: Judgment Visibility & Responsibility
**Repository:** [ajt-judgment-gate](https://github.com/Nick-heo-eg/ajt-judgment-gate)

**Responsibility:** Enforce visibility and attribution for judgment handling.

**Does:**
- Require explicit handling for STOP judgments
- Log overrides with full attribution
- Track ACCEPT usage
- Maintain tamper-evident audit trail

**Does NOT:**
- Re-evaluate Phase 1 judgments
- Make routing decisions
- Prevent overrides
- Claim compliance

---

## What AJT Core Is NOT

Even when both phases are combined, AJT Core is **not:**

- ❌ A decision system (judgments are advisory, not commands)
- ❌ An automation engine (no automatic actions)
- ❌ A policy enforcement tool (no business rules)
- ❌ A compliance framework (no regulatory guarantees)
- ❌ A workflow orchestrator (no multi-step coordination)
- ❌ A blocking mechanism (overrides are allowed)

**These are permanent non-capabilities, not missing features.**

---

## AJT Core's Single Output

When Phase 1 and Phase 2 are integrated, the only guaranteed output is:

> **Auditable judgment history**

This history includes:
- What judgments were made (ACCEPT/STOP)
- What evidence or negative proof supported them
- How judgments were handled (honored/overridden)
- Who made handling decisions (attribution)
- When actions occurred (timestamps)
- Whether logs were tampered with (hash chain)

**Nothing more. Nothing less.**

---

## What Happens Outside AJT Core

### Execution Authority
- **Caller/operator** decides whether to honor or override judgments
- **External systems** execute downstream actions
- **Business logic** remains outside both phases

### Policy Enforcement
- **External policy engines** define what should happen on STOP
- **Approval workflows** manage override authorization
- **Compliance systems** interpret audit trails

### Observability
- **Dashboards** visualize judgment patterns
- **Alerting systems** notify on anomalous overrides
- **Analytics** identify systemic issues

**AJT Core provides the data. External systems decide what to do with it.**

---

## Why Two Layers, Not One

### Separation of Concerns

**Phase 1** requires:
- Document processing expertise
- Evidence evaluation logic
- LLM integration (if used)

**Phase 2** requires:
- None of the above

Combining them would:
- Create responsibility confusion
- Weaken trust boundaries
- Make audit trails ambiguous

**Separation is architectural, not organizational.**

---

### Independent Trust Properties

**Phase 1 trust:**
- "Did this system extract correctly?"
- "Was evidence sufficient?"
- "Why did extraction stop?"

**Phase 2 trust:**
- "Was STOP handling explicit?"
- "Were overrides attributed?"
- "Was log integrity maintained?"

These are **different trust questions** requiring **different verification methods**.

---

## Integration Pattern

```
External System
      │
      ▼ (document)
Phase 1: Judgment Generation
      │
      ▼ (STOP/ACCEPT with evidence/proof)
Phase 2: Judgment Visibility
      │
      ▼ (auditable log with hash chain)
External Audit/Policy Systems
```

**Adapter layer** (external, not part of AJT Core):
- Converts Phase 1 output to Phase 2 input
- Minimal format translation
- No decision logic

---

## What AJT Core Guarantees

When both phases are correctly implemented:

1. **STOP cannot proceed silently**
   - Explicit handling is structurally required
   - No default "continue" path exists

2. **Overrides are attributable**
   - Actor, reason, scope, risk acknowledgment recorded
   - Override events are first-class audit artifacts

3. **ACCEPT usage is tracked**
   - Who used extracted value for what action
   - Consumer identity preserved

4. **Logs are tamper-evident** (if hash chain enabled)
   - Any modification breaks cryptographic verification
   - Tampering location is detectable

**These are structural guarantees, not policy promises.**

---

## What AJT Core Does NOT Guarantee

AJT Core does **not** guarantee:

- ❌ Extraction correctness (Phase 1 may have bugs)
- ❌ Override prevention (overrides are allowed by design)
- ❌ Regulatory compliance (audit trails ≠ compliance)
- ❌ Operational safety (execution authority is external)
- ❌ Business outcomes (decisions remain with operators)

**Responsibility for outcomes remains with the caller, always.**

---

## Stability Commitment

### Phase 1 Status
- **Version:** 2.1.0
- **Status:** Feature-complete (extraction + STOP boundaries)
- **Future:** Bug fixes, evidence grounding improvements only

### Phase 2 Status
- **Version:** 0.2.0
- **Status:** Feature-complete by design (sealed)
- **Future:** Bug fixes, security patches only
- **1.0.0:** Planned (stability declaration, no feature changes)

**Neither phase will expand scope.**

New capabilities belong in **Phase 3** (not yet defined).

---

## Phase 3: Intentionally Undefined

**Phase 3 is not planned.**

Potential Phase 3 capabilities (if ever built):
- Orchestration across multiple systems
- Policy engines and approval workflows
- Real-time dashboards and alerting
- Workflow definitions and automation
- External system integrations

**Why Phase 3 is undefined:**

1. **Misuse must be understood first**
   - AJT Core must be deployed in real systems
   - Failure modes must be documented
   - Misapplication patterns must be identified

2. **Trust boundaries must remain clear**
   - Phase 3 will involve policy decisions
   - Policy decisions require different trust assumptions
   - Mixing policy with judgment creates liability confusion

3. **External extensions are safer**
   - Organizations can build Phase 3 equivalents externally
   - Custom integrations avoid architectural constraints
   - AJT Core remains stable while extensions evolve

**Phase 3 is intentionally deferred, not forgotten.**

---

## When to Use AJT Core

Use AJT Core when:
- Wrong extractions create liability
- Silent failures are unacceptable
- Audit trails are mandatory
- "I don't know" is a valid output
- Trust requires proof, not promises

---

## When NOT to Use AJT Core

Do NOT use AJT Core when:
- Real-time blocking is required (AJT is logging, not prevention)
- Decisions must be fast (judgment + logging adds latency)
- Audit trails are unnecessary overhead
- Business needs "the answer" regardless of confidence
- Responsibility must remain with AI (AJT externalizes it)

**See each repository's "When You Should NOT Use This" section.**

---

## Core Principle

> **AJT Core does not decide what is right.**
> **It ensures that ignoring a judgment is never invisible.**

This principle is:
- Permanent
- Non-negotiable
- Architecturally enforced

Any change that weakens this principle will be rejected.

---

## Cross-References

### Phase 1 Documentation
- [ajt-grounded-extract README](https://github.com/Nick-heo-eg/ajt-grounded-extract/blob/master/README.md)
- [STOP Semantics](https://github.com/Nick-heo-eg/ajt-grounded-extract/blob/master/docs/STOP_SEMANTICS.md)
- [Judgment Boundary Proofs](https://github.com/Nick-heo-eg/ajt-grounded-extract/blob/master/docs/JUDGMENT_BOUNDARY_PROOFS.md)

### Phase 2 Documentation
- [ajt-judgment-gate README](https://github.com/Nick-heo-eg/ajt-judgment-gate/blob/master/README.md)
- [MVP Rules](https://github.com/Nick-heo-eg/ajt-judgment-gate/blob/master/docs/MVP_RULES.md)
- [Phase 1→Phase 2 Demo](https://github.com/Nick-heo-eg/ajt-judgment-gate/blob/master/docs/PHASE1_PHASE2_DEMO.md)

---

## Architectural Identity

**AJT Core is not a product. It is a boundary.**

It does not solve problems.
It makes problem-solving auditable.

It does not automate decisions.
It makes decision consequences visible.

It does not prevent misuse.
It makes misuse detectable.

**This is the architecture.**

---

**Last Updated:** 2026-01-10
**Status:** Core definition sealed
**Phase 3:** Intentionally undefined
