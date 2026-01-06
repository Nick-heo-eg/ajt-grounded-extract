#!/usr/bin/env python3
"""
RAG Attempt: Intentional Failure

Missing required field (decision_maker).

Expected: STOP with MISSING_FIELD reason.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from admission.rules_rag_read import evaluate_rag_read


def run_demo():
    """Execute intentional failure case."""

    print("=" * 70)
    print("RAG ATTEMPT: INTENTIONAL FAILURE")
    print("=" * 70)
    print()

    payload = {
        # decision_maker intentionally omitted
        "why": "Check reference documents",
        "scope": "read_only",
        "query": "What is RAG?"
    }

    print("PAYLOAD:")
    print(f"  why: {payload.get('why')}")
    print(f"  scope: {payload.get('scope')}")
    print(f"  query: {payload.get('query')}")
    print(f"  decision_maker: {payload.get('decision_maker')} (MISSING)")
    print()

    result = evaluate_rag_read(payload)

    print("RESULT:")
    print(f"  ALLOWED: {result.allowed}")
    print(f"  REASON: {result.reason}")
    print(f"  TOKEN: {result.token}")
    print()

    print("EXPECTED BEHAVIOR:")
    print("  DEFAULT: STOP enforced")
    print("  Failure of ANY required condition → immediate STOP")
    print()


if __name__ == "__main__":
    run_demo()
