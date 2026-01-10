# Real-World Scenarios

These scenarios illustrate why STOP-first judgment prevents catastrophic errors.

---

## Scenario 1: Contract Processing - When STOP Saves You

**Situation**: Your legal team receives 500 vendor contracts to process. You need to extract the "termination notice period" from each contract.

**What happens with typical AI systems**:
- **Contract A**: "30-day notice required" → Extracts "30 days" ✓
- **Contract B**: No termination clause mentioned → Extracts "30 days" (unsupported inference from Contract A) ✗
- **Contract C**: "Notice period TBD in amendment" → Extracts "TBD" or makes up a number ✗

**Result**: Your procurement team schedules vendor terminations based on wrong dates. Legal liability, business disruption, vendor disputes.

**What happens with this system**:
- **Contract A**: "30-day notice required" → **ACCEPT**: Extracted "30 days" with proof (quote + page location)
- **Contract B**: No termination clause → **STOP**: "Searched: termination_notice. Found: nothing. Cannot extract."
- **Contract C**: "Notice period TBD" → **STOP**: "Conflicting signals detected. Requires human review."

**Why this matters**:
- **Contract B** flags for legal review before you make a costly mistake
- **Contract C** gets routed to procurement, not auto-processed
- You have an audit trail showing the system *did not guess*

**Business impact**: Avoid contractual breaches, reduce legal risk, maintain audit compliance.

---

## Scenario 2: Medical Records - When Extraction Errors Kill

**Situation**: Hospital extracts "drug allergy" information from patient intake forms to populate the prescription system.

**What happens with typical AI systems**:
- **Patient X**: "Allergic to penicillin" → Extracts correctly ✓
- **Patient Y**: Form says "allergies: none known" → Extracts "none" ✓
- **Patient Z**: Allergy section left blank (patient forgot to fill it) → Extracts "none" (assumed from context) ✗

**Result**: Patient Z receives penicillin. Allergic reaction. Malpractice lawsuit. Patient harm.

**What happens with this system**:
- **Patient X**: **ACCEPT**: "penicillin" (evidence: quote from line 7 of intake form)
- **Patient Y**: **ACCEPT**: "none known" (evidence: explicit statement in allergy field)
- **Patient Z**: **STOP**: "Allergy field blank. No evidence of 'none' statement. Requires nurse verification."

**Why this matters**:
- **Patient Z's record** gets flagged before prescription
- Nurse confirms allergies in person
- System proves it *did not assume* missing data means "none"

**Business impact**: Patient safety, malpractice risk reduction, regulatory compliance (HIPAA audit trail).

---

## Scenario 3: Financial Compliance - When Silence is Evidence

**Situation**: Bank processes loan applications, extracting "income verification" from submitted tax documents.

**What happens with typical AI systems**:
- **Applicant A**: W-2 shows $85,000 salary → Extracts correctly ✓
- **Applicant B**: Self-employed, 1099 shows $120,000 → Extracts correctly ✓
- **Applicant C**: Submits blank tax form with handwritten note "will provide later" → Extracts "$0" or skips field ✗

**Result**: Loan approved for Applicant C without income verification. Default risk. Regulatory violation (Know Your Customer failure).

**What happens with this system**:
- **Applicant A**: **ACCEPT**: $85,000 (evidence: W-2 line 1, box "Wages")
- **Applicant B**: **ACCEPT**: $120,000 (evidence: 1099 total, box 7)
- **Applicant C**: **STOP**: "No income figure found. Handwritten note detected. Cannot proceed with automated approval."

**Why this matters**:
- **Applicant C** gets routed to manual underwriting
- Compliance officer sees audit trail: system *refused* to guess
- Regulatory examiner sees proof of due diligence

**Business impact**: Regulatory compliance (KYC/AML), reduced default risk, auditable decision trail.

---

## Key Principle: The Cost of Being Wrong vs. The Cost of Stopping

| Decision | Typical AI | This System |
|----------|-----------|-------------|
| **Clear evidence** | Extract (correct) | **ACCEPT** (with proof) |
| **No evidence** | Extract anyway (guesses) | **STOP** (with explanation) |
| **Ambiguous evidence** | Extract (risky) | **STOP** or **NEED_REVIEW** |

**Why executives care**:
- **Liability**: Wrong extraction = legal exposure. STOP = documented due diligence.
- **Compliance**: Regulators ask "how do you know?" STOP events provide proof you didn't guess.
- **Operational Risk**: Silent failures compound. Visible stops get fixed.
- **Trust**: Stakeholders trust a system that says "I don't know" over one that fabricates answers.

**Bottom line**: This system costs you review time on edge cases. It saves you liability costs on catastrophic errors.
