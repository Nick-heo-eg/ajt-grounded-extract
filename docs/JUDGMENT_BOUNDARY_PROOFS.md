# Judgment Boundary Proofs

This document collects concrete proof cases
showing where and why the system stops.

These are not failures.
They are successful demonstrations of enforced judgment boundaries.

---

## Proof Case 01 — Conflicting Evidence

**Input condition**
- Multiple candidate date values detected in different document contexts
- Example: "Effective 02/01/2025" in preamble, "Starting 03/15/2025" in execution clause

**Judgment**
- STOP

**Stop reason**
- `conflicting_values`

**Why stopping is correct**
- Accepting any single value would require assumption about document authority hierarchy
- No explicit rule exists in source text to resolve the conflict
- Either value could be legally binding depending on contract interpretation

**What would be required to proceed**
- Explicit precedence clause (e.g., "In case of conflict, execution clause governs")
- Single unambiguous statement
- External authority to disambiguate

**Evidence**
- Test file: `examples/adversarial_conflicting_dates.txt`
- Result: STOP with negative proof artifact

---

## Proof Case 02 — Missing Required Field

**Input condition**
- Required field mentioned but value deferred
- Example: "Effective date TBD upon executive approval"

**Judgment**
- STOP

**Stop reason**
- `no_candidates_found`

**Why stopping is correct**
- "TBD" is not a date value
- Extracting "TBD" as a date would propagate placeholder into downstream systems
- Future determination does not constitute present evidence

**What would be required to proceed**
- Actual date value in definitive form
- Addendum with resolved date

**Evidence**
- Test file: `examples/adversarial_missing_required_field.txt`
- Result: STOP with explicit missing-value proof

---

## Proof Case 03 — Inferential Trap

**Input condition**
- Date value can be inferred from narrative context but is never explicitly stated
- Example: "Expected to occur approximately 30 days after signing" + "Signed on January 1, 2025"

**Judgment**
- STOP

**Stop reason**
- `no_candidates_found` (inference rejected)

**Why stopping is correct**
- "Approximately 30 days" is not a commitment
- Calculation would require assumption about calendar counting
- Inference from non-binding language creates legal exposure

**What would be required to proceed**
- Explicit date stated in definitive terms
- Example: "Effective date shall be January 31, 2025"

**Evidence**
- Test file: `examples/adversarial_inferential_trap.txt`
- Result: STOP, no inference performed

---

## Proof Case 04 — Numeric Ambiguity

**Input condition**
- Multiple numeric values with conditional logic
- Example: "APR 5.5% first year, 7.75% thereafter, subject to adjustment clause"

**Judgment**
- STOP

**Stop reason**
- `conflicting_values` (multiple valid values with different conditions)

**Why stopping is correct**
- No single value represents "the" APR
- Time-dependent values require state information
- Conditional adjustments cannot be evaluated from document alone

**What would be required to proceed**
- Request for specific time-bounded extraction (e.g., "Year 1 APR")
- Single unconditional value

**Evidence**
- Test file: `examples/adversarial_numeric_ambiguity.txt`
- Result: STOP with condition-dependency explanation

---

## Proof Case 05 — Table/Text Mismatch

**Input condition**
- Payment date in table differs from narrative explanation
- No explicit precedence rule

**Judgment**
- STOP

**Stop reason**
- `conflicting_values` (source disagreement)

**Why stopping is correct**
- Table and text are both authoritative sources
- No document-internal rule establishes priority
- Choosing one over the other is an interpretive decision

**What would be required to proceed**
- Explicit precedence statement (e.g., "In case of discrepancy, table controls")
- Corrected document with aligned values

**Evidence**
- Test file: `examples/adversarial_table_text_mismatch.txt`
- Result: STOP with source-conflict proof

---

## Proof Case 06 — Conditional Clause

**Input condition**
- Effective date defined by future events
- Example: "Later of (a) capital contribution, (b) March 1, 2025, or (c) license approval"

**Judgment**
- STOP

**Stop reason**
- `no_candidates_found` (conditional logic requires external state)

**Why stopping is correct**
- "Later of" requires knowing which events have occurred
- External state (capital contribution, license status) not available in document
- Accepting March 1 alone would ignore contractual conditions

**What would be required to proceed**
- External verification of condition states
- Amended document with resolved date

**Evidence**
- Test file: `examples/adversarial_conditional_clause.txt`
- Result: STOP with external-dependency explanation

---

## Proof Case 07 — Redacted Content

**Input condition**
- Target field explicitly redacted or sealed
- Example: "Effective on ██/██/2025"

**Judgment**
- STOP

**Stop reason**
- `no_candidates_found` (redaction detected)

**Why stopping is correct**
- Redacted content cannot be inferred from context
- Attempting recovery would violate redaction intent
- Sealed terms may have legal protection

**What would be required to proceed**
- Unsealed document version
- Explicit authorization to access sealed content

**Evidence**
- Test file: `examples/adversarial_redacted_content.txt`
- Result: STOP with redaction-detected proof

---

## Proof Case 08 — Contextual Inference

**Input condition**
- Date can be inferred from adjacent but unrelated context
- Example: "First Monday after New Year's Day" + "Meeting scheduled January 6th"

**Judgment**
- STOP

**Stop reason**
- `no_candidates_found` (meeting date ≠ effective date)

**Why stopping is correct**
- Meeting date and effective date are different semantic fields
- Proximity does not establish equivalence
- Inference would conflate unrelated information

**What would be required to proceed**
- Explicit statement: "Effective date is January 6, 2025"
- No inferential gap

**Evidence**
- Test file: `examples/adversarial_contextual_hallucination.txt`
- Result: STOP, semantic boundary enforced

---

## Summary

All 8 proof cases demonstrate:
- Explicit stopping at judgment boundaries
- Structured negative proof (not silent failure)
- Clear requirements for proceeding

**These STOPs are not errors.**
**They are evidence of correct boundary enforcement.**
