# Regulatory Alignment

**Important**: This project does not claim regulatory compliance.

It demonstrates how audit-ready artifacts (STOP decisions with negative proof)
can support alignment with documentation and traceability expectations.

---

## Audit-Ready Artifacts

This system produces structured artifacts for every extraction decision:

- **ACCEPT decisions**: Include evidence references, document quotes, and integrity hashes
- **STOP decisions**: Include negative proof (what was searched, why stopped)
- **Manifest files**: Timestamped, immutable records of all decisions

These artifacts enable:
- Post-hoc audit of AI decisions
- Traceability from output back to input evidence
- Proof of due diligence ("system did not guess")

---

## Alignment Areas

### Documentation Requirements

Many regulatory frameworks require documentation of AI decision-making:
- EU AI Act (Articles 12-13): Technical documentation and transparency
- FDA guidance: Traceability in medical device software
- Financial regulations: Explainability for automated decisions

This system's artifacts provide:
- Decision rationale (evidence-based)
- Negative proof (what was not found)
- Reproducible judgment paths

---

### Risk Management

High-risk AI systems often require:
- Human oversight mechanisms
- Documented limitations
- Error detection and logging

This system provides:
- STOP as a boundary signal (triggers human review)
- Explicit limitation documentation (negative proof)
- Structured logging (all decisions archived)

---

### Transparency Obligations

Some jurisdictions require explanations of automated decisions.

This system provides:
- **For ACCEPT**: Evidence quotes, document locations, confidence
- **For STOP**: Structured explanation of why extraction did not proceed

---

## What This System Does NOT Claim

This system does not:
- ❌ Guarantee regulatory compliance
- ❌ Replace legal/compliance review
- ❌ Constitute a safety certification
- ❌ Eliminate human responsibility

---

## Recommended Use

For organizations subject to AI regulations:

1. **Audit trails**: Use manifest files as evidence of AI decision-making
2. **Human oversight**: Route STOP events to manual review
3. **Documentation**: Include STOP semantics in system documentation
4. **Risk assessment**: Evaluate STOP patterns as part of risk monitoring

---

## Further Reading

Regulatory mapping documents (informational only):
- [EU AI Act Alignment](EU_AI_ACT_ALIGNMENT.md)
- [Finance Sector Mapping](REG_MAP_FINANCE.md)
- [Healthcare Sector Mapping](REG_MAP_HEALTHCARE.md)
- [Legal Sector Mapping](REG_MAP_LEGAL.md)

**Note**: These documents describe potential alignment areas.
They do not constitute compliance certification.

---

## Summary

This system produces audit-ready artifacts that support
documentation and traceability expectations.

**Alignment ≠ Compliance**

Organizations remain responsible for:
- Legal review
- Risk assessment
- Compliance validation
- Regulatory approval (where required)

The system provides tools. Organizations provide governance.
