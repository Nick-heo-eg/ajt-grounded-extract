# AJT Grounded Extract

**Judgment-first grounded extraction engine.**
**Returns ACCEPT with evidence or STOP with proof. Nothing in between.**

---

## STOP Is Not Failure

**STOP is a judgment.**
**STOP is an audit artifact.**
**STOP is how this system succeeds when evidence is insufficient.**

Most systems explain answers. **This one explains why it stopped.**

---

## Status

**v2.1.0** — Audit-ready | Constitution: Frozen | Attack Tests: 10/10 blocked

---

## Installation

```bash
pip install ajt-grounded-extract
```

**Zero dependencies.** Pure Python stdlib.

---

## Core Principle

**Extract structured data only when it can be proven; otherwise stop—and prove that you stopped.**

> **Most systems explain answers. This one explains why it stopped.**

---

## Philosophy: STOP-first

- **This project does not aim to extract everything.**
- **Extraction occurs only when evidence is sufficient.**
- **When evidence is insufficient, the system stops and proves why.**
- **Evidence Integrity > Recall**: Only extract values with verifiable document evidence
- **Default: STOP**: When evidence is insufficient, conflicting, or missing → stop extraction
- **Negative Proof**: Every STOP includes explicit reason + preserved artifacts
- **No Fine-tuning**: Rule-based + LLM extraction without training pipelines
- **Local Execution**: Runs entirely on local machine

---

## What This System Is

**A judgment trace generator for grounded extraction.**

- ✅ **Records reasoning** about extraction decisions (STOP/ACCEPT)
- ✅ **Produces negative proof** when intentional non-execution occurs
- ✅ **Generates audit artifacts** with evidence grounding
- ✅ **Explains why extraction did NOT proceed** (primary output for STOP events)

**This is a judgment recording component, not an autonomous decision system.**

---

## What This System Is NOT

**This system records judgments; it does not make decisions on behalf of the caller.**

- ❌ **Decision engine** — Does not execute, enforce, or decide for you
- ❌ **Policy executor** — Does not implement business rules or enforce outcomes
- ❌ **Automation controller** — Does not trigger actions based on judgments
- ❌ **Enforcement system** — Does not block, allow, or control execution flow
- ❌ Multi-domain rule engine
- ❌ Enterprise extraction with thresholds
- ❌ Training/fine-tuning pipeline
- ❌ High-recall extraction system

**What we provide**:
- ✅ **Advisory judgment signals** (STOP = recommendation, not block)
- ✅ **Negative proof artifacts** (evidence of intentional non-execution)
- ✅ **Traceability** (decision_maker identity required)
- ✅ **Audit trail** (write-once logs with reasoning)

---

## Responsibility Boundary

**This system does NOT own execution authority, decision outcomes, or result responsibility.**

### What This System Does
- **Recommend** extraction actions based on evidence sufficiency
- **Record** the rationale for STOP/ACCEPT judgments
- **Explain** why execution did NOT proceed (for STOP events)
- **Produce** audit artifacts with evidence grounding

### What This System Does NOT Do
- **Execute** business logic or trigger downstream actions
- **Enforce** policies or prevent operations
- **Decide** on behalf of the caller or end user
- **Own** the outcome or consequences of extraction results

### Execution Authority
**Execution authority and result ownership remain with the external caller.**

- The caller decides whether to act on STOP/ACCEPT signals
- The caller owns the consequences of using (or ignoring) extraction results
- This system generates reasoning traces, not commands
- STOP is an **advisory interruption**, not a hard block

---

## STOP Semantics

**STOP is not a failure. STOP is not a block. STOP is an advisory judgment signal.**

### What STOP Means
- **STOP = Advisory signal**: "Extraction did not proceed due to insufficient evidence"
- **STOP = Intentional non-execution**: A deliberate decision not to extract, with reasoning
- **STOP = Negative proof**: Evidence that the system evaluated alternatives and chose not to proceed

### What STOP Is NOT
- ❌ **Not a hard block** — Does not prevent the caller from taking action
- ❌ **Not a failure** — Successful operation that produced a judgment artifact
- ❌ **Not enforcement** — Does not control or restrict external systems
- ❌ **Not a command** — Does not instruct the caller what to do

### STOP Output
When STOP occurs, this system produces:
- **stop_reason**: Machine-readable reason code (e.g., `no_candidates_found`)
- **stop_proof**: Artifact showing what was evaluated and why extraction did not proceed
- **decision_log**: Timestamped record of the judgment process

**Example STOP message:**
> "This STOP is an advisory judgment signal. Execution authority remains with the caller. This system records the rationale for intentional non-execution."

---

## Negative Proof

**Negative proof is a first-class artifact produced when intentional non-execution occurs.**

### Definition
A **negative proof** is evidence that:
1. The system **evaluated** extraction candidates
2. The system **determined** that evidence was insufficient
3. The system **recorded** the reasoning and evaluated alternatives
4. The system **chose** not to extract (intentional non-execution)

### Structure
Negative proof includes:
- **What was searched**: Fields, patterns, or rules evaluated
- **What was found**: Number of candidates, conflicting values, confidence scores
- **Why extraction stopped**: Explicit reason code with supporting data
- **When the judgment was made**: Timestamp and hash for integrity

### Purpose
Negative proof serves as:
- **Audit trail** for regulatory compliance
- **Debugging evidence** for system operators
- **Transparency artifact** for end users
- **Accountability record** showing the system did NOT blindly execute

**Negative proof is not a failure report—it is evidence of intentional non-execution.**

---

## Architecture

```
Document → Ingest → Extract → Ground → Judge → Archive
           ↓        ↓         ↓        ↓        ↓
           Hash     Candidates Evidence STOP?   Artifacts
```

### Pipeline Stages

1. **Ingest**: Load document, compute hash, build line index
2. **Extract**: Find candidate values (rule-based or LLM)
3. **Ground**: Map each value to exact document span (quote + offsets)
4. **Judge**: STOP-first decision: `ACCEPT | STOP | NEED_REVIEW`
5. **Archive**: Write-once artifacts with timestamps + integrity hashes

### Decision Taxonomy

- **ACCEPT**: Evidence found, confidence sufficient, integrity verified
- **STOP**: No candidates, conflict, low confidence, or integrity failure
- **NEED_REVIEW**: Edge cases requiring human judgment

---

## Quick Start

### Run Extraction

```bash
# ACCEPT case (has clear "Effective Date: 01/15/2025")
python run.py examples/accept_example.txt

# STOP case (no explicit effective date)
python run.py examples/stop_example.txt
```

### View Results

Open generated HTML viewer:
```bash
open viewer/accept_example_viewer.html
open viewer/stop_example_viewer.html
```

---

## Output Format

### JSON Result (ACCEPT)
```json
{
  "field_name": "effective_date",
  "decision": "ACCEPT",
  "value": "01/15/2025",
  "evidence": {
    "quote": "01/15/2025",
    "start": 245,
    "end": 255,
    "line": 12,
    "context": "...Effective Date: 01/15/2025..."
  },
  "confidence": 0.9,
  "decision_role": "advisory",
  "execution_authority": "external"
}
```

**Metadata fields**:
- `decision_role`: Always `"advisory"` — This system recommends, does not decide
- `execution_authority`: Always `"external"` — Caller owns execution decisions

---

### STOP Event
```json
{
  "field_name": "effective_date",
  "decision": "STOP",
  "value": null,
  "stop_reason": "no_candidates_found",
  "stop_proof": {
    "searched": true,
    "candidates_found": 0
  },
  "decision_role": "advisory",
  "execution_authority": "external",
  "stop_semantics": "non_blocking",
  "negative_proof_type": "intentional_non_execution"
}
```

**Metadata fields**:
- `decision_role`: Always `"advisory"` — STOP is a recommendation, not enforcement
- `execution_authority`: Always `"external"` — Caller decides how to handle STOP
- `stop_semantics`: Always `"non_blocking"` — STOP does not prevent caller action
- `negative_proof_type`: Always `"intentional_non_execution"` — Evidence of deliberate non-extraction

---

## HTML Viewer Features

- **Evidence Highlighting**: Green (ACCEPT) / Red (STOP)
- **Navigation Sidebar**: Jump to extracted fields
- **"Why Stopped" Panel**: Explicit reasons with proof artifacts
- **Offset Mapping**: Click evidence span → see exact document location

---

## Directory Structure

```
ajt-grounded-extract/
├── schema/              # Field definitions
├── engine/              # Core extraction modules
│   ├── ingest.py
│   ├── extract.py
│   ├── ground.py
│   ├── judge.py
│   └── archive.py
├── viewer/              # HTML viewer generator
├── evidence/            # Write-once artifacts (JSONL + manifests)
├── examples/            # Demo documents
└── run.py               # CLI entry point
```

---

## Evidence Requirements

All extractions must satisfy:

- ✅ `require_exact_quote`: Value must appear verbatim in document
- ✅ `require_offset_mapping`: Quote mapped to byte offsets
- ✅ `stop_on_conflict`: Multiple conflicting values → STOP
- ✅ `min_confidence`: Below threshold → STOP

---

## Acceptance Criteria

- [x] Demo shows at least one ACCEPT and one STOP
- [x] STOP includes explicit reason and preserved artifacts
- [x] Viewer navigates evidence spans correctly
- [x] Non-goals stated explicitly

---

## Regulatory Mapping & Review

This system includes industry-specific regulatory risk mappings for:
- **Financial Services** — Authorization scope, customer isolation, advisory vs execution separation
- **Healthcare** — Patient data isolation, complete clinical evidence requirements, clinician traceability
- **Legal Practice** — Attorney responsibility, client-matter isolation, conflict-of-interest prevention

**Navigation**: See [REGULATORY_REVIEW_GUIDE.md](REGULATORY_REVIEW_GUIDE.md) for audience-specific entry points.

**Key documents**:
- [REGULATORY_META_MAP.md](REGULATORY_META_MAP.md) — Cross-industry risk-control mappings
- [docs/REG_MAP_FINANCE.md](docs/REG_MAP_FINANCE.md) — Financial services mapping
- [docs/REG_MAP_HEALTHCARE.md](docs/REG_MAP_HEALTHCARE.md) — Healthcare mapping
- [docs/REG_MAP_LEGAL.md](docs/REG_MAP_LEGAL.md) — Legal practice mapping
- [COMPLIANCE_GUIDE.md](COMPLIANCE_GUIDE.md) — Audit artifact generation
- [ATTACK_TEST.md](ATTACK_TEST.md) — Adversarial verification results

**Principle**: This project demonstrates how specified risks are blocked. It does not claim regulatory compliance.

---

## Reference

### Normative Specification

This implementation follows the **AJT (AI Judgment Trail)** constitutional framework:
- **Spec Repository**: [spec](https://github.com/Nick-heo-eg/spec) — Normative rules and judgment structure
- **Reference Implementation**: This repository (ajt-grounded-extract) — Executable proof of concept

**Relationship**:
- `spec`: Constitutional rules (what must be proven)
- `ajt-grounded-extract`: Execution + case law (how it's proven in practice)

---

### Motivation

**Motivated by [ajt-negative-proof-sim](https://github.com/Nick-heo-eg/ajt-negative-proof-sim) (sealed reference).**

Core principle: **Prove extraction succeeded OR prove why you stopped.**

---

## Recent Changes (v2.1.0 → Boundary Seal)

**Purpose**: Seal responsibility boundary and STOP semantics to eliminate ambiguity about system role.

**Changes**:
1. **Responsibility Boundary Documentation** — Explicit declaration that this system does not execute, enforce, or decide on behalf of the caller. Execution authority and result ownership remain external.
2. **STOP Semantics Clarification** — STOP is an advisory signal (non-blocking recommendation), not a hard block or failure. STOP events produce negative proof artifacts as first-class outputs.
3. **Negative Proof Definition** — Formal definition of negative proof as evidence of intentional non-execution, including what was evaluated and why extraction did not proceed.
4. **Decision Log Metadata** — All judgment outputs now include fixed metadata fields: `decision_role=advisory`, `execution_authority=external`, `stop_semantics=non_blocking`, `negative_proof_type=intentional_non_execution`.
5. **Runtime Advisory Messages** — CLI output includes explicit advisory notice when STOP occurs: "This STOP is an advisory judgment signal. Execution authority remains with the caller."

**No functional changes**: Judgment logic, STOP conditions, and LLM behavior unchanged. This release clarifies system boundaries and removes interpretation ambiguity.

---

## License

MIT
