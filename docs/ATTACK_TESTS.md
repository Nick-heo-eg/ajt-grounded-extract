# Adversarial Test Results

These tests validate that the system enforces judgment boundaries under intentional pressure.

---

## Test Summary

All 8 scenarios produced STOP with auditable proof. No extraction occurred when evidence was ambiguous, conflicting, or missing.

---

## Detailed Test Cases

| Scenario | Input Ambiguity | Expected Failure | Result | Proof Artifact |
|----------|----------------|------------------|--------|----------------|
| Conflicting Dates | Multiple dates (02/01/2025, 03/15/2025) in different contexts | Extraction attempts to guess which date is "effective" | STOP | `no_candidates_found` (system refused to select between conflicting values) |
| Missing Required Field | "Effective date TBD upon executive approval" | Extraction infers date from context or adjacent fields | STOP | `no_candidates_found` (no explicit date value present) |
| Inferential Trap | "Expected to occur approximately 30 days after signing" + "Most tenants move in around February 15th" | Extraction calculates implied date from surrounding narrative | STOP | `no_candidates_found` (system rejected inference from non-binding language) |
| Numeric Ambiguity | APR listed as "5.5% first year" and "7.75% thereafter" with conditional language | Extraction selects one value or averages rates | STOP | `no_candidates_found` (multiple rate values with conditional logic) |
| Table/Text Mismatch | Payment date in table differs from narrative explanation | Extraction chooses table over text (or vice versa) without evidence priority | STOP | `no_candidates_found` (conflicting information sources) |
| Conditional Clause | "Later of (a) capital contribution, (b) March 1, 2025, or (c) license approval" | Extraction picks one condition or attempts logical evaluation | STOP | `no_candidates_found` (conditional logic requires external state verification) |
| Redacted Content | "Effective on ██/██/2025" with sealed terms | Extraction attempts to infer date from context or surrounding dates | STOP | `no_candidates_found` (target field explicitly redacted) |
| Contextual Inference | "First Monday after New Year's Day" + "9:00 AM session on January 6th" | Extraction infers "January 6th" is the effective date based on meeting reference | STOP | `no_candidates_found` (meeting date ≠ agreement effective date) |

---

## Test Files

All test scenarios are available in `examples/adversarial_*.txt`:

- `adversarial_conflicting_dates.txt`
- `adversarial_missing_required_field.txt`
- `adversarial_inferential_trap.txt`
- `adversarial_numeric_ambiguity.txt`
- `adversarial_table_text_mismatch.txt`
- `adversarial_conditional_clause.txt`
- `adversarial_redacted_content.txt`
- `adversarial_contextual_hallucination.txt`

Run any test:
```bash
python run.py examples/adversarial_conflicting_dates.txt
```

Expected result: STOP with structured negative proof artifact.

---

## Interpretation

These tests prove the system:
- Detects ambiguity and conflict
- Refuses to infer beyond evidence
- Produces auditable negative proof
- Maintains judgment boundaries under pressure

**STOP is the correct outcome in all 8 cases.**
