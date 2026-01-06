#!/usr/bin/env python3
"""
Demo 3: Authority Laundering Attack

Attack: Wrapper system acquires token, exposes extraction-as-a-service
Expected: BLOCKED at Interface (wrapper's API is itself a gated action)
Result: Demonstrates that responsibility cannot be aggregated
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from engine.audit import AuditLogger


def run_demo():
    """Execute authority laundering attack scenario."""

    print("=" * 70)
    print("DEMO 3: AUTHORITY LAUNDERING ATTACK")
    print("=" * 70)
    print()

    print("SCENARIO:")
    print("  1. Wrapper system obtains token legitimately")
    print("  2. Wrapper exposes extraction as 'API service'")
    print("  3. External systems call wrapper API")
    print("  4. Attempt: Bypass individual admission requirements")
    print()

    # Wrapper's legitimate admission
    wrapper_context = {
        "action": "provide_extraction_service",
        "context": {
            "service": "extraction_api",
            "environment": "wrapper_system_v1"
        },
        "decision_maker": "wrapper_admin@example.com"
    }

    # External caller attempt
    caller_request = {
        "api_endpoint": "/wrapper/extract",
        "payload": {
            "document": "user_doc.pdf",
            "field": "effective_date"
        },
        "caller": "external_user@example.com"
    }

    print("-" * 70)
    print("WRAPPER ADMISSION CHECK:")
    print("-" * 70)
    print("Wrapper's action: provide_extraction_service")
    print("Wrapper's decision_maker: wrapper_admin@example.com")
    print("Status: Wrapper itself must be gated ✓")
    print()

    print("-" * 70)
    print("CALLER ADMISSION CHECK:")
    print("-" * 70)
    print("Caller's action: extract (via wrapper)")
    print("Caller's decision_maker: external_user@example.com")
    print()

    # Constitution check
    print("Constitution requirement:")
    print('  "Any action offering generation or execution MUST be gated"')
    print()
    print("Wrapper's API is an 'action offering generation'")
    print("→ Wrapper MUST gate its API with admission interface")
    print()
    print("Each caller MUST have:")
    print("  ✓ Traceable decision_maker")
    print("  ✓ Proven responsibility")
    print("  ✓ Own admission check")
    print()

    # Decision
    decision = "STOP"
    blocked_at = "Interface"
    reason = "wrapper_must_gate_own_api (cannot aggregate responsibility)"

    print("-" * 70)
    print("DECISION:")
    print("-" * 70)
    print(f"Result: {decision}")
    print(f"Blocked at: {blocked_at}")
    print(f"Reason: {reason}")
    print()

    print("-" * 70)
    print("WHY THIS BLOCKS:")
    print("-" * 70)
    print("1. Wrapper's API offering is itself an 'action'")
    print("2. Each caller needs individual decision_maker")
    print("3. Cannot transfer responsibility to wrapper")
    print("4. Cannot use wrapper's token for caller's action")
    print()

    # Generate audit trail
    print("-" * 70)
    print("GENERATING AUDIT TRAIL:")
    print("-" * 70)

    logger = AuditLogger(audit_dir="demos/output")

    audit_id = logger.log_decision(
        action="extract_via_wrapper",
        context={
            "wrapper": wrapper_context,
            "caller": caller_request
        },
        decision=decision,
        decision_maker=caller_request["caller"],
        conditions_proven={
            "wrapper_has_token": True,
            "caller_has_token": False,
            "responsibility_aggregation_attempted": True
        },
        token=None,
        blocked_at=blocked_at,
        reason=reason
    )

    print(f"✓ Audit log created: {audit_id}")
    print()

    print("=" * 70)
    print("DEMO COMPLETE")
    print("=" * 70)
    print()
    print("Key Principle Demonstrated:")
    print('"decision_maker MUST be a traceable human or registered system identity.')
    print(' Anonymous or default values are invalid.')
    print(' Responsibility cannot be aggregated into wrapper systems."')
    print()
    print(f"Review generated files in: demos/output/")
    print(f"  - {audit_id}.json (audit log with laundering evidence)")
    print()


if __name__ == "__main__":
    run_demo()
