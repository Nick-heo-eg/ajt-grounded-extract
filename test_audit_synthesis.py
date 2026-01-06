#!/usr/bin/env python3
"""Test audit logging with synthesis query."""
from pathlib import Path
from execution.rag_read_gate import rag_read

request = {
    "decision_maker": "tester",
    "why": "Test synthesis intent detection",
    "scope": "read_only",
    "query": "검색 결과를 합쳐서 한 문장으로"
}

corpus_dir = str(Path(__file__).parent / "docs")
result = rag_read(request, corpus_dir=corpus_dir)

print("\n" + "=" * 70)
print("RESULT SUMMARY")
print("=" * 70)
print(f"ALLOWED: {result['allowed']}")
print(f"EVIDENCE COUNT: {len(result['evidence'])}")
print("\nAudit log (above) shows:")
print("  - detected_intent: synthesis")
print("  - scope_mismatch: true")
print("  - suggested_scope: synthesis")
print("  - required_action: request_new_action")
