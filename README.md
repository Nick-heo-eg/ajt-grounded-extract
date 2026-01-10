# AJT Grounded Extract

**Judgment-first grounded extraction engine.**
**Returns ACCEPT with evidence or STOP with proof. Nothing in between.**

---

## What This Repository Is

AJT-Grounded-Extract is not just an extraction tool.

It is a reference implementation of a judgment-oriented architecture
that explicitly defines where an AI system must stop
when evidence is insufficient or conflicting.

This repository demonstrates:
- Explicit stopping as a first-class outcome
- Structured negative proof instead of silent failure
- Judgment boundaries enforced by design, not heuristics

Extraction happens only after a judgment boundary is passed.

---

## Executive Summary

**The Problem**: Traditional AI extraction systems guess when evidence is unclear. In contracts, medical records, and financial documents, a confident wrong answer costs more than no answer.

**This Solution**: A system that extracts only when it can prove the answer—or stops and explains why it can't.

**Business Value**:
- **Legal/Compliance**: Audit trail shows the system refused to guess (regulatory defense)
- **Risk Reduction**: Wrong extraction = liability. STOP = documented due diligence.
- **Operational Trust**: Visible failures (STOP events) get fixed. Silent failures compound.

**What makes this different**: Most systems explain their answers. This one explains why it stopped.

---

## Real-World Scenarios

This system is designed for high-risk domains where a wrong extraction is more costly than no extraction.

Examples include:
- **Contract processing** — Avoiding liability from incorrect termination dates
- **Medical records** — Preventing prescription errors from missing allergy data
- **Financial compliance** — Maintaining KYC/AML audit trails

See detailed scenarios: [docs/REAL_WORLD_SCENARIOS.md](docs/REAL_WORLD_SCENARIOS.md)

---

## Quick Start

### ACCEPT Example (Evidence Found)

```bash
python run.py examples/accept_example.txt
```

![ACCEPT Viewer](docs/images/accept_viewer.png)

*Evidence grounded: exact quote, page location, and integrity verification.*

### STOP Example (Evidence Missing)

Run the system on a document with missing required evidence. The expected and correct behavior is to STOP.

```bash
python run.py examples/stop_example.txt
```

```json
{
  "status": "STOP",
  "reason": "insufficient evidence",
  "searched": ["effective_date"],
  "found": []
}
```

STOP is a successful outcome. It represents intentional non-execution with auditable proof.

### Visual Example: STOP Viewer

![STOP Viewer](docs/images/stop_viewer.png)

*The HTML viewer shows exactly why extraction stopped, what was searched, and the auditable proof artifact.*

---

## STOP Is Not Failure

**STOP is an advisory judgment signal.**

- STOP means evidence was insufficient for reliable extraction
- STOP produces structured negative proof (what was checked, why it stopped)
- STOP does not prevent the caller from taking action
- STOP is not a hard block—it is a documented boundary

Most systems explain answers. **This one explains why it stopped.**

---

## Status

**Latest**: v2.1.0 — Judgment boundary skeleton with documented proofs

Adversarial tests: 8/8 produced correct STOP decisions
See: [docs/ATTACK_TESTS.md](docs/ATTACK_TESTS.md)

---

## Installation

```bash
pip install ajt-grounded-extract
```

Or from source:
```bash
git clone https://github.com/Nick-heo-eg/ajt-grounded-extract.git
cd ajt-grounded-extract
pip install -e .
```

---

## Core Principle

> **Extraction systems should optimize for integrity, not recall.**

When evidence is ambiguous, conflicting, or missing:
- Traditional systems guess (high recall, low integrity)
- This system stops (lower recall, high integrity)

The cost of being wrong exceeds the cost of stopping.

---

## When You Would Use This

- Contract/legal document extraction where incorrect values create liability
- Regulatory compliance pipelines requiring audit trails for AI decisions
- RAG systems with strict grounding requirements (healthcare, finance)
- Document processing where silent failures are unacceptable
- Systems where "I don't know" is a valid and valuable output

---

## Architectural Scope

This repository represents Phase 1 of the AJT approach:

**Phase 1 — Internal Judgment**
- Judgment rules are enforced inside the extraction pipeline
- STOP is a valid and expected outcome
- Evidence grounding is mandatory

Later phases extend this concept outward,
but are intentionally out of scope for this repository.

---

## Responsibility Boundary

**This system is advisory only.**

- Does not enforce policies or prevent operations
- Produces judgment signals (STOP / ACCEPT) for external decision-making
- Execution authority remains with the caller
- STOP is a recommendation, not a block

The system documents where it stopped and why.
The caller decides what to do with that information.

---

## Documentation

### Core Concepts
- [STOP Semantics](docs/STOP_SEMANTICS.md) — What STOP means and doesn't mean
- [Judgment Boundary Proofs](docs/JUDGMENT_BOUNDARY_PROOFS.md) — Concrete proof cases
- [STOP Casebook](docs/STOP_CASEBOOK.md) — Reusable patterns and classification

### Implementation
- [Architecture](docs/ARCHITECTURE.md) — Pipeline stages and decision flow
- [Output Format](docs/OUTPUT_FORMAT.md) — JSON structure and metadata
- [Attack Tests](docs/ATTACK_TESTS.md) — Adversarial test results

### Alignment
- [Regulatory Alignment](docs/REGULATORY_ALIGNMENT.md) — Audit-ready artifacts and traceability

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## License

MIT
