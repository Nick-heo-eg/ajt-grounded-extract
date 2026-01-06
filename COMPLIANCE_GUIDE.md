# Compliance Guide: Audit, Defense, Regulatory

**Purpose**: Generate audit-grade documentation for compliance, legal defense, and regulatory response.

**Principle**: No claims of safety. Only demonstrations of how attacks are blocked.

---

## Quick Start

```python
from engine.audit import AuditLogger, DefenseBriefGenerator, RegulatoryReportGenerator

# 1. Log every decision
logger = AuditLogger(audit_dir="audit")

audit_id = logger.log_decision(
    action="extract_effective_date",
    context={"document": "contract.pdf", "content_hash": "abc123..."},
    decision="ADMIT",  # or "STOP"
    decision_maker="operator@company.com",
    conditions_proven={
        "responsibility": {"who": "operator@company.com", "why": "compliance_review"},
        "alternatives": ["manual_review", "defer_to_legal"],
        "stop_capability": True
    },
    token={"token_id": "tok_xyz..."},
    blocked_at=None,  # or "Interface", "Rules", "Token"
    reason=None  # or "no_candidates_found"
)
```

---

## Use Case 1: Audit Log (Execution-Time)

**When**: Every admission decision (ADMIT or STOP)

**Purpose**: Create tamper-evident record of decision path

**Output**: `audit/{audit_id}.json`

### Example Output

```json
{
  "audit_id": "audit_6ead651b5df44d91_1704560400",
  "timestamp": "2026-01-06T12:00:00+00:00",
  "decision_context_hash": "6ead651b5df44d91...",
  "action_requested": "extract_effective_date",
  "decision": "STOP",
  "decision_maker_id": "operator@company.com",
  "conditions_proven": {},
  "scope": {
    "validity": "context-bound",
    "reuse": "forbidden",
    "auto_revoke_on_change": true
  },
  "blocked_at": "Rules",
  "reason": "no_candidates_found",
  "attachments": {
    "admission_token_id": null,
    "proof_bundle_ref": "proof_8f3a2e1..."
  }
}
```

### Key Fields

- `blocked_at`: Where decision was stopped (Interface / Rules / Token)
- `scope.reuse`: Always "forbidden"
- `scope.auto_revoke_on_change`: Always true
- `conditions_proven`: Empty object if STOP, populated if ADMIT

---

## Use Case 2: Defense Brief (Incident-Time)

**When**: Dispute, audit, or legal inquiry

**Purpose**: Demonstrate constitutional compliance and stop capability

**Output**: `audit/defense_brief_{audit_id}.md`

### Generate

```python
brief_gen = DefenseBriefGenerator()
brief_path = brief_gen.generate(audit_id="audit_6ead651b5df44d91_1704560400")
# → audit/defense_brief_audit_6ead651b5df44d91_1704560400.md
```

### Example Output (Excerpt)

```markdown
## 1. Constitutional Compliance

| Requirement | Status |
|-------------|--------|
| DEFAULT: STOP applied | ✅ Yes |
| ALL conditions proven | ❌ No |
| Scope limited | ✅ Yes |
| Reuse prohibited | ✅ Yes |

## 2. Decision Path

**Action Requested**: extract_effective_date
**Decision Maker**: operator@company.com
**Exclusion Basis (Negative Proof)**:
- Decision: STOP
- Blocked at: Rules
- Reason: no_candidates_found

## 4. Conclusion

This system does not guarantee outcomes.

**This system guarantees**:
- Stoppability (DEFAULT: STOP enforced)
- Traceability (decision_maker: operator@company.com)
- Scope containment (context-bound, reuse forbidden)
```

### Use in Legal Context

- Attach to incident reports
- Provide to counsel for defense preparation
- Submit as evidence of duty of care

**No claim**: "We are secure"
**Claim**: "We stopped when conditions were not met, and here is the proof"

---

## Use Case 3: Regulatory Report (On-Demand)

**When**: Regulatory inquiry, compliance audit, periodic review

**Purpose**: Demonstrate risk controls and block point effectiveness

**Output**: `audit/regulatory_report_{timestamp}.md`

### Generate

```python
report_gen = RegulatoryReportGenerator()
report_path = report_gen.generate(
    audit_ids=["audit_001", "audit_002", "audit_003"]
)
# → audit/regulatory_report_20260106_120000.md
```

### Example Output (Excerpt)

```markdown
## Risk-Control Mapping

| Risk Pattern | Control | Evidence Count |
|--------------|---------|----------------|
| Over-generation | Interface gate | 100 |
| Hallucination pressure | DEFAULT: STOP | 45 |
| Scope creep | Context binding | 55 (tokens issued) |
| Accountability gap | Identity anchoring | 100 (all have decision_maker) |

## Block Point Analysis

| Block Point | Count | Percentage |
|-------------|-------|------------|
| Interface | 12 | 26.7% |
| Rules | 28 | 62.2% |
| Token | 5 | 11.1% |

## Non-Goals (Explicit)

This system does **NOT** guarantee:
- ❌ Accuracy of outputs
- ❌ Automation maximization
- ❌ Output completeness

This system **DOES** guarantee:
- ✅ Stoppability (DEFAULT: STOP)
- ✅ Traceability (decision_maker required)
- ✅ Scope containment (context-bound tokens)
```

### Use in Regulatory Context

- Submit to regulators on request
- Include in periodic compliance reports
- Demonstrate control effectiveness without performance claims

**No claim**: "Our system is 99% accurate"
**Claim**: "45 out of 100 attempts were stopped per constitution, here are the block points"

---

## Best Practices

### DO

- ✅ Log every decision (ADMIT and STOP)
- ✅ Generate defense briefs when incidents occur
- ✅ Provide regulatory reports on request
- ✅ Reference specific block points in documentation
- ✅ Use "blocked-by-design" language

### DON'T

- ❌ Claim "secure" or "safe"
- ❌ Guarantee accuracy or completeness
- ❌ Omit STOP decisions from audit trail
- ❌ Edit audit logs (write-once only)
- ❌ Use marketing language in compliance docs

---

## Integration with Existing Systems

### Logging Integration

```python
# In your admission gate implementation
from engine.audit import AuditLogger

gate = AdmissionGate()
logger = AuditLogger()

can_proceed, token = gate.can_proceed(ctx)

# Log decision
audit_id = logger.log_decision(
    action=ctx.action,
    context={"content": ctx.content},
    decision="ADMIT" if can_proceed else "STOP",
    decision_maker=ctx.decision_maker,
    conditions_proven=gate.get_proven_conditions(ctx) if can_proceed else {},
    token=token.__dict__ if token else None,
    blocked_at=gate.get_block_point(ctx) if not can_proceed else None,
    reason=gate.why_stopped(ctx).get('reasons', [None])[0] if not can_proceed else None
)
```

### Periodic Reporting

```python
# Weekly regulatory report
from pathlib import Path
import json

audit_dir = Path("audit")
audit_ids = [
    f.stem for f in audit_dir.glob("audit_*.json")
    if f.stat().st_mtime > week_start_timestamp
]

report_gen = RegulatoryReportGenerator()
report_path = report_gen.generate(audit_ids)
```

---

## FAQ

### Q: Do I need to log successful (ADMIT) decisions?

**A**: Yes. Audit trail must include both ADMIT and STOP for completeness.

### Q: Can I modify audit logs?

**A**: No. Audit logs are write-once. Generate new logs for corrections.

### Q: How long should I retain audit logs?

**A**: Follow your organization's data retention policy. Recommend minimum 7 years for compliance.

### Q: Can I use these templates for marketing?

**A**: No. These are compliance/legal documents only. Marketing requires different language.

### Q: What if regulators ask "Is your system safe?"

**A**: Provide regulatory report. Answer: "Our system enforces stop conditions and provides audit trails. We do not claim safety; we demonstrate control effectiveness."

---

**Version**: 1.0.0
**Status**: Production-ready
**Reference**: ADMISSION_CONSTITUTION.md v1.0
