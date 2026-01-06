# Regulatory Review Guide

**Purpose**: Navigate regulatory documentation by audience and jurisdiction.

**Scope**: Navigation aid only. No claims, no legal advice.

---

## For Regulatory Authorities

If you are reviewing this system in a regulatory capacity, refer to the document that matches your jurisdiction:

| Your Authority | Document to Review |
|----------------|-------------------|
| **Financial services regulation** (banking, securities, trading) | [docs/REG_MAP_FINANCE.md](docs/REG_MAP_FINANCE.md) |
| **Healthcare regulation** (clinical systems, medical devices, patient data) | [docs/REG_MAP_HEALTHCARE.md](docs/REG_MAP_HEALTHCARE.md) |
| **Legal practice regulation** (bar associations, ethics boards, UPL) | [docs/REG_MAP_LEGAL.md](docs/REG_MAP_LEGAL.md) |

**Cross-industry overview**: [REGULATORY_META_MAP.md](REGULATORY_META_MAP.md)

---

## For Compliance Teams

If you are evaluating this system for organizational adoption:

1. **Identify your regulatory risks** → Review industry-specific mapping above
2. **Understand control mechanisms** → Review [REGULATORY_META_MAP.md](REGULATORY_META_MAP.md)
3. **Verify attack resistance** → Review [ATTACK_TEST.md](ATTACK_TEST.md)
4. **Review audit capabilities** → Review [COMPLIANCE_GUIDE.md](COMPLIANCE_GUIDE.md)
5. **Reproduce demonstrations** → Run demos in [demos/](demos/)

---

## For Security Reviewers

If you are conducting security or adversarial review:

1. **Threat model** → [SECURITY.md](SECURITY.md)
2. **Attack test results** → [ATTACK_TEST.md](ATTACK_TEST.md)
3. **Constitutional specification** → [ADMISSION_CONSTITUTION.md](ADMISSION_CONSTITUTION.md)
4. **Reproducible demos** → [demos/README.md](demos/README.md)

---

## For Legal Counsel

If you are evaluating legal or liability implications:

1. **What this system does NOT claim** → See "Disclaimer" sections in all regulatory mapping documents
2. **Evidence artifacts** → [COMPLIANCE_GUIDE.md](COMPLIANCE_GUIDE.md)
3. **Professional responsibility implications** → [docs/REG_MAP_LEGAL.md](docs/REG_MAP_LEGAL.md)
4. **Audit trail structure** → [engine/audit.py](engine/audit.py)

---

## For Technical Reviewers

If you are evaluating implementation correctness:

1. **Constitutional specification** → [ADMISSION_CONSTITUTION.md](ADMISSION_CONSTITUTION.md)
2. **Attack verification** → [ATTACK_TEST.md](ATTACK_TEST.md)
3. **Core engine** → [engine/](engine/)
4. **Demos** → [demos/](demos/)

---

## What to Request from This Project

| If you need... | Request this... |
|----------------|-----------------|
| Understanding of risk-control mappings | Regulatory mapping documents (public, linked above) |
| Proof of attack resistance | Attack test reproduction (run demos/) |
| Audit trail samples | Generated artifacts (demos/output/) |
| Block point demonstrations | Specific attack scenario reproduction |

**Do not request**: Compliance claims, legal guarantees, performance metrics, accuracy benchmarks

---

## What This Project Does NOT Provide

This project does **not** provide:
- Legal compliance certification
- Regulatory approval
- Medical device certification
- Financial advisory registration
- Bar association endorsement
- Legal advice

**This project demonstrates how specified risks are blocked. It does not claim to satisfy any regulation.**

---

## Operational Details

Detailed clause mappings, operational thresholds, and legal phraseology are maintained separately and distributed selectively.

For access to private operational documentation, contact maintainers with:
- Your regulatory authority or organizational role
- Specific regulatory requirements you need to map
- NDA execution capability

---

**Version**: 1.0
**Last Updated**: 2026-01-07

---

**"Navigate, don't claim. Review, don't certify. Demonstrate, don't guarantee."**
