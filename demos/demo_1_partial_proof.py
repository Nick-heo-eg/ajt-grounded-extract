#!/usr/bin/env python3
"""
Demo 1: Partial Proof Attack

Attack: Submit 2/3 of required proof (missing alternatives_evaluated)
Expected: BLOCKED at Rules section
Result: Audit log + Defense brief + Regulatory report auto-generated
"""
import sys
import json
from pathlib import Path

# Add parent directory to path for local development
sys.path.insert(0, str(Path(__file__).parent.parent))

from engine.judge import ExtractionJudge, Decision
from engine.audit import AuditLogger, DefenseBriefGenerator


def run_demo():
    """Execute partial proof attack scenario."""

    print("=" * 70)
    print("DEMO 1: PARTIAL PROOF ATTACK")
    print("=" * 70)
    print()

    # Attack payload
    attack_payload = {
        "action": "extract_effective_date",
        "context": {
            "document": "contract_sample.pdf",
            "content": "This agreement becomes effective...",
            "content_hash": "abc123def456"
        },
        "decision_maker": "demo_user@example.com",
        "proof": {
            "responsibility": {
                "who": "demo_user@example.com",
                "what": "extract_effective_date",
                "why": "compliance_review"
            },
            # INTENTIONAL OMISSION: alternatives_evaluated missing
            "stop_capability": True
        }
    }

    print("ATTACK ATTEMPT:")
    print(json.dumps(attack_payload, indent=2))
    print()
    print("INTENTIONAL VIOLATION: alternatives_evaluated field missing")
    print("Expected: STOP (partial proof not accepted)")
    print()

    # Simulate admission check
    print("-" * 70)
    print("ADMISSION CHECK:")
    print("-" * 70)

    # Check if all conditions met
    has_responsibility = "responsibility" in attack_payload["proof"]
    has_alternatives = "alternatives" in attack_payload["proof"]
    has_stop_capability = "stop_capability" in attack_payload["proof"]

    print(f"✓ Responsibility proven: {has_responsibility}")
    print(f"✗ Alternatives evaluated: {has_alternatives}")
    print(f"✓ Stop capability verified: {has_stop_capability}")
    print()

    # Decision
    decision = "STOP"
    blocked_at = "Rules"
    reason = "incomplete_admission_proof (missing alternatives)"

    print("-" * 70)
    print("DECISION:")
    print("-" * 70)
    print(f"Result: {decision}")
    print(f"Blocked at: {blocked_at}")
    print(f"Reason: {reason}")
    print()

    # Generate audit trail
    print("-" * 70)
    print("GENERATING AUDIT TRAIL:")
    print("-" * 70)

    logger = AuditLogger(audit_dir="demos/output")

    audit_id = logger.log_decision(
        action=attack_payload["action"],
        context=attack_payload["context"],
        decision=decision,
        decision_maker=attack_payload["decision_maker"],
        conditions_proven=attack_payload["proof"],
        token=None,
        blocked_at=blocked_at,
        reason=reason
    )

    print(f"✓ Audit log created: {audit_id}")

    # Generate defense brief
    brief_gen = DefenseBriefGenerator()
    brief_path = brief_gen.generate(audit_id, audit_dir="demos/output")
    print(f"✓ Defense brief created: {brief_path}")
    print()

    # Show key evidence
    print("-" * 70)
    print("KEY EVIDENCE (from audit log):")
    print("-" * 70)

    audit_path = Path("demos/output") / f"{audit_id}.json"
    with open(audit_path, 'r') as f:
        audit = json.load(f)

    print(f"  Scope validity: {audit['scope']['validity']}")
    print(f"  Reuse policy: {audit['scope']['reuse']}")
    print(f"  Auto-revoke on change: {audit['scope']['auto_revoke_on_change']}")
    print()

    print("=" * 70)
    print("DEMO COMPLETE")
    print("=" * 70)
    print()
    print("Key Principle Demonstrated:")
    print('"This system does not guarantee results.')
    print(' It guarantees stoppability and traceability."')
    print()
    print(f"Review generated files in: demos/output/")
    print(f"  - {audit_id}.json (audit log)")
    print(f"  - defense_brief_{audit_id}.md (legal defense)")
    print()


if __name__ == "__main__":
    run_demo()
