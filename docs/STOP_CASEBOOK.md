# STOP Casebook

This casebook documents recurring STOP patterns
observed in real extraction scenarios.

STOP is not an exception.
It is a repeatable, classifiable outcome.

---

## STOP Pattern: No Evidence

**Observed when**
- Target information is implied but never explicitly stated
- Field mentioned as "TBD", "pending", or deferred
- Placeholder text present instead of actual value

**Risk if accepted**
- Unsupported inference propagates to downstream systems
- Placeholder values treated as real data
- Legal or factual liability from assumed information

**Correct action**
- STOP with explicit missing-evidence proof
- Document what was searched
- Specify what would constitute acceptable evidence

**Example scenarios**
- Contract effective date listed as "TBD"
- Payment terms marked "to be determined in amendment"
- Dates referenced as "approximately 30 days after signing"

**Negative proof artifact**
```json
{
  "decision": "STOP",
  "reason": "no_candidates_found",
  "searched": ["effective_date"],
  "found": [],
  "explanation": "Field mentioned but no definitive value present"
}
```

---

## STOP Pattern: Conflicting Values

**Observed when**
- Multiple candidate values exist for same field
- Different sections of document provide different values
- Table and text narrative disagree
- Conditional values with unclear precedence

**Risk if accepted**
- Arbitrary selection among valid alternatives
- Loss of critical conditional information
- Contract interpretation without authority

**Correct action**
- STOP with conflict documentation
- List all conflicting candidates
- Specify what disambiguation would require

**Example scenarios**
- Date appears as "02/01/2025" in one clause, "03/15/2025" in another
- Interest rate varies by time period without single answer
- Payment table shows different date than narrative description

**Negative proof artifact**
```json
{
  "decision": "STOP",
  "reason": "conflicting_values",
  "candidates": [
    {"value": "02/01/2025", "source": "Section 1.2"},
    {"value": "03/15/2025", "source": "Execution clause"}
  ],
  "explanation": "Multiple values detected, no precedence rule available"
}
```

---

## STOP Pattern: Inference Required

**Observed when**
- Value can be calculated or inferred from context
- Narrative suggests value through implication
- Surrounding information could be combined to derive answer

**Risk if accepted**
- Calculation errors
- Inference from non-binding language
- Mixing of separate semantic fields

**Correct action**
- STOP with inference rejection proof
- Document what inference would have been
- Specify why inference is unreliable

**Example scenarios**
- "Approximately 30 days after signing" + signing date present
- "First Monday after New Year's Day"
- "Same terms as Contract A" (cross-reference)

**Negative proof artifact**
```json
{
  "decision": "STOP",
  "reason": "no_candidates_found",
  "rejected_inference": "30 days from January 1 = January 31",
  "explanation": "Inference from approximate language is not extraction"
}
```

---

## STOP Pattern: Conditional Logic

**Observed when**
- Value depends on external events or state
- "Later of", "earlier of", "upon" language present
- Future determination required

**Risk if accepted**
- Ignoring contractual conditions
- Selecting one branch of conditional without state information
- Time-dependent values treated as static

**Correct action**
- STOP with external-dependency explanation
- Document conditional structure
- Specify what external information is required

**Example scenarios**
- "Later of (a) funding, (b) March 1, or (c) approval"
- "Effective upon board vote"
- "Rate adjusts based on LIBOR" (external index)

**Negative proof artifact**
```json
{
  "decision": "STOP",
  "reason": "no_candidates_found",
  "conditional_structure": "Later of [funding | March 1 | approval]",
  "explanation": "Requires external state verification"
}
```

---

## STOP Pattern: Redacted Content

**Observed when**
- Target field is explicitly redacted
- Sealed or confidential markers present
- Information intentionally obscured

**Risk if accepted**
- Violation of redaction intent
- Attempted recovery of sealed information
- Legal or privacy breach

**Correct action**
- STOP with redaction detection
- Do not attempt inference from surrounding text
- Document redaction presence

**Example scenarios**
- "Effective on ██/██/2025"
- "[REDACTED]" markers
- Blacked-out fields in scanned documents

**Negative proof artifact**
```json
{
  "decision": "STOP",
  "reason": "no_candidates_found",
  "explanation": "Target field contains redaction marker"
}
```

---

## STOP Pattern: Ambiguous Format

**Observed when**
- Value present but format is ambiguous
- Multiple interpretations possible (e.g., 01/02/2025 = Jan 2 or Feb 1?)
- Unit or type unclear

**Risk if accepted**
- Misinterpretation due to format assumption
- Wrong data type extraction
- Regional format confusion

**Correct action**
- STOP with format ambiguity explanation
- Request clarification or format specification
- Document interpretation uncertainty

**Example scenarios**
- Date in ambiguous format without locale context
- Numeric value without unit specification
- Abbreviated text with multiple expansions

**Negative proof artifact**
```json
{
  "decision": "STOP",
  "reason": "insufficient_confidence",
  "ambiguity": "01/02/2025 could be MM/DD or DD/MM",
  "explanation": "Format interpretation requires context not present"
}
```

---

## Pattern Classification Summary

| Pattern | Trigger | Key Risk | Negative Proof Type |
|---------|---------|----------|---------------------|
| No Evidence | Missing/TBD value | Placeholder propagation | Searched scope + null result |
| Conflicting Values | Multiple candidates | Arbitrary selection | Conflict documentation |
| Inference Required | Implied value | Calculation error | Inference rejection |
| Conditional Logic | External dependency | Ignored conditions | Condition structure |
| Redacted Content | Sealed information | Privacy/legal breach | Redaction detection |
| Ambiguous Format | Interpretation needed | Misinterpretation | Format uncertainty |

---

## Use of This Casebook

**For developers:**
- Pattern recognition during extraction design
- Test case generation
- Error handling specification

**For compliance/legal:**
- Risk documentation
- Audit trail interpretation
- Due diligence evidence

**For operations:**
- STOP triage prioritization
- Manual review routing
- Quality assurance validation

---

## Key Principle

> STOP is not a bug to be fixed.
>
> STOP is a documented pattern showing
> where the system correctly enforced
> a judgment boundary.

Every STOP case in this casebook
represents a scenario where proceeding
would have required assumption, inference,
or interpretation beyond available evidence.

**These are correct outcomes.**
