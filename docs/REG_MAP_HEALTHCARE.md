# Healthcare Regulatory Mapping

**Purpose**: Map healthcare regulatory risk patterns to constitutional controls.

**Scope**: Conceptual mapping only. Illustrative, non-exhaustive. No legal advice.

**Principle**: "We do not claim to satisfy healthcare regulations. We demonstrate blockage of risks that healthcare regulators fear."

---

## Disclaimer

This document provides conceptual mappings between healthcare regulatory risk patterns and system controls.

**This is NOT**:
- Legal compliance certification
- Regulatory approval claim
- Medical device certification
- Substitute for legal or medical counsel

**Detailed clause mappings to specific healthcare regulations are maintained separately.**

Consult your legal, compliance, and clinical teams for regulatory assessment.

---

## Healthcare Regulatory Intent

### What Healthcare Regulators Fear

Healthcare regulators across jurisdictions share common fears about automated clinical systems:

1. **Incomplete clinical decisions** — AI making diagnoses or treatment recommendations without complete data
2. **Patient data leakage** — Authorization for Patient A's records used for Patient B
3. **Hallucinated clinical data** — AI generating fictitious lab results, diagnoses, or treatment outcomes
4. **Silent scope expansion** — Decision support tool escalating to autonomous treatment execution
5. **Unclear clinical responsibility** — Automated recommendations without traceable clinician oversight

**Core regulatory principle**: Clinical decisions must be based on complete evidence, patient-specific context, and traceable human authority.

---

## Mapped Risk Patterns

From the 5 core risk patterns, healthcare primarily faces:

| Risk Pattern | Clinical Manifestation | Regulatory Concern |
|--------------|------------------------|-------------------|
| **Partial proof** | Treatment recommendation made without complete patient workup | Incomplete diagnosis, patient harm |
| **Context reuse** | Authorization token from Patient A used for Patient B's records | HIPAA violation, privacy breach |
| **Over-generation** | AI generates clinical advice without physician approval | Unauthorized medical practice |
| **Scope expansion** | Diagnostic aid tool silently gains treatment ordering capability | Patient safety, liability |
| **Authority laundering** | Clinical decision aggregated under "hospital system" without individual physician identity | Medical malpractice exposure |

---

## Constitutional Controls

### 1. ALL Conditions Enforcement → Blocks Partial Proof

**Clinical scenario**: AI recommends treatment without complete lab results

**Constitutional requirement**:
```
"Failure to prove any single required condition results in immediate STOP without fallback."
```

**What this blocks**:
- Cannot proceed with diagnosis if lab_results_complete = false
- Cannot recommend treatment if patient_history_reviewed = false
- Cannot prescribe if drug_interactions_checked = false
- No partial credit ("we have 90% of the data")

**Evidence artifact**: Defense brief showing which clinical condition was not met

**Regulatory benefit**: No clinical decisions on incomplete evidence

---

### 2. Hash Derivation → Blocks Context Reuse / Patient Data Leakage

**Clinical scenario**: Attempt to reuse authorization token across patient records

**Constitutional requirement**:
```
"context_hash MUST be derived from input payload.
Manually supplied or reused context_hash values invalidate the token."
```

**What this blocks**:
- Token issued for Patient A's EHR cannot be used for Patient B
- context_hash derived from: patient_id, medical_record_number, encounter_id, timestamp
- Manual hash supply = automatic invalidation
- Even same physician cannot reuse token across patients

**Evidence artifact**: Audit log with hash comparison showing patient context mismatch

**Regulatory benefit**: Strict patient-record isolation, privacy protection

---

### 3. Interface Gate → Blocks Over-generation

**Clinical scenario**: AI system offers clinical recommendations

**Constitutional requirement**:
```
"Any action offering generation or execution MUST be gated"
```

**What this blocks**:
- AI cannot generate clinical advice without explicit admission check
- No "auto-suggest diagnoses" without physician gate
- Every clinical output requires decision_maker identity (physician/clinician)

**Evidence artifact**: Audit log with admission decision

**Regulatory benefit**: No clinical recommendations without human authority checkpoint

---

### 4. Context Binding → Blocks Scope Expansion

**Clinical scenario**: Decision support tool attempts to autonomously order treatment

**Constitutional requirement**:
```
"Context change includes any modification to input, environment, time, or intended downstream usage.
Auto-revoke on context change."
```

**What this blocks**:
- Token issued for "provide diagnostic support" cannot be used for "order medication"
- Token issued for "analyze lab results" cannot be used for "schedule surgery"
- Scope locked at token issuance: recommendation ≠ execution
- Privilege escalation = automatic revocation

**Evidence artifact**: Token validation log showing scope mismatch

**Regulatory benefit**: No silent escalation from advisory to autonomous action

---

### 5. Identity Anchoring → Blocks Authority Laundering

**Clinical scenario**: Hospital system aggregates clinical decisions under institutional identity

**Constitutional requirement**:
```
"decision_maker MUST be a traceable human or registered system identity.
Anonymous or default values are invalid.
Responsibility cannot be aggregated into wrapper systems."
```

**What this blocks**:
- Cannot use "hospital_ai_system" as decision_maker
- Each clinical recommendation requires specific physician/clinician identity
- No "department_admin" as catch-all authority
- Cannot hide individual physician behind institutional wrapper

**Evidence artifact**: Audit log with individual clinician identity per decision

**Regulatory benefit**: Clear medical liability trail, malpractice clarity

---

## Evidence Artifacts

Every clinical decision generates:

| Artifact | Clinical Use Case | Audience |
|----------|-------------------|----------|
| **Audit Log** | Record of every diagnostic/treatment recommendation | Hospital audit, healthcare regulators, legal defense |
| **Defense Brief** | Legal defense in case of malpractice claim or regulatory inquiry | Hospital legal counsel, clinical risk management |
| **Regulatory Report** | Periodic summary of system decisions and blocks | Compliance team, healthcare regulators |

All artifacts include:
- Timestamp (UTC, ISO 8601)
- Context hash (SHA-256) tied to specific patient
- Decision (ADMIT/STOP)
- decision_maker (individual clinician, not aggregated)
- Patient identifier (hashed for privacy)
- Clinical conditions proven/failed

---

## Typical Healthcare Use Cases

### Clinical Decision Support

**Action**: Recommend diagnostic test or treatment

**Controls applied**:
- ALL conditions enforcement: All required clinical checks must pass (patient history, current meds, allergies)
- Interface gate: Recommendation generation requires admission with physician identity
- Partial proof check: Cannot proceed without complete patient workup

**STOP condition**: Missing allergy check → immediate STOP with evidence

---

### Medical Record Extraction

**Action**: Extract diagnosis codes or medication lists from EHR

**Controls applied**:
- Hash derivation: Token tied to specific patient + encounter
- Context binding: Extraction scope locked (cannot expand to prescription authority)
- Reuse prohibition: Token for Patient A cannot be reused for Patient B

**STOP condition**: Token reuse attempted → immediate STOP with hash mismatch evidence

---

### Treatment Protocol Compliance

**Action**: Verify treatment follows clinical guidelines

**Controls applied**:
- ALL conditions enforcement: All guideline steps must be verified
- Identity anchoring: Specific clinician must be decision_maker
- Audit trail: Every compliance check logged

**STOP condition**: Guideline step skipped → immediate STOP with missing condition evidence

---

## What This System Guarantees

In healthcare contexts:

1. **Patient isolation** — Tokens bound to specific patient, reuse forbidden
2. **Complete evidence requirement** — No clinical decisions on partial data
3. **Clinician traceability** — Every decision has named physician/clinician
4. **Stoppability** — DEFAULT: STOP enforced for all clinical operations
5. **Scope containment** — Authorization cannot expand from advisory to autonomous action
6. **Audit trail** — Write-once logs with tamper-evident hashing, suitable for legal defense

**These guarantees are derived from attack tests, not claimed.**

---

## What This System Does NOT Guarantee

This system does NOT:
- Guarantee regulatory compliance with specific healthcare laws
- Certify medical device status
- Ensure clinical accuracy of diagnoses
- Replace physician judgment
- Eliminate all patient safety risks
- Provide medical or legal advice

**We do not claim the system is "compliant" or "safe." We demonstrate how specified risks are blocked.**

---

## For Clinical Risk Management Teams

When reviewing this system:

1. **Focus on**: Risk-control mappings, not clinical accuracy metrics
2. **Request**: Audit logs for specific patient encounters, defense briefs for incidents
3. **Verify**: Block points match your clinical risk requirements
4. **Test**: Run attack scenarios against your clinical threat model

**Key question**: "How does this block [specific patient safety risk]?" not "Is this FDA-approved?"

---

## For Healthcare Regulators

If you are a healthcare regulatory authority reviewing this system:

1. **We do not claim**: Compliance with any specific healthcare regulation
2. **We demonstrate**: How 5 core risk patterns are blocked by design
3. **We provide**: Machine-readable audit trails for every clinical decision
4. **We prove**: STOP decisions with evidence artifacts

**Request from us**: Attack test results, audit logs, block point demonstrations

**Do not request**: Claims of compliance, clinical accuracy guarantees, medical device certification

---

## Industry-Specific Threat Model

**In scope** (blocked by design):
- Clinical decisions on incomplete data
- Cross-patient context reuse (privacy breach)
- Unauthorized clinical advice generation
- Privilege escalation (advisory → autonomous)
- Responsibility aggregation (hiding individual clinician)

**Out of scope** (not addressed):
- Physical device malfunctions
- Network security breaches
- External EHR system compromise
- Social engineering of clinicians
- Clinical algorithm accuracy

**We block the 5 core risk patterns. We do not claim protection against all patient safety risks.**

---

## Modification Policy

This mapping is versioned with ADMISSION_CONSTITUTION.md.

Changes to healthcare risk-control mappings require:
- Constitutional amendment (v2.0+)
- Updated attack test suite
- Clinical safety impact assessment

**Control mechanisms are frozen as of v1.0.**

---

## Related Documents

- **ADMISSION_CONSTITUTION.md** — Normative specification
- **REGULATORY_META_MAP.md** — Cross-industry risk patterns
- **ATTACK_TEST.md** — Adversarial verification results
- **COMPLIANCE_GUIDE.md** — How to generate audit artifacts

---

**Version**: 1.0
**Constitution**: ADMISSION_CONSTITUTION.md v1.0
**Last Updated**: 2026-01-07

---

**"This repository is public by design. Operational details specific to healthcare regulations (clause mappings, thresholds, clinical protocols) are intentionally distributed separately."**
