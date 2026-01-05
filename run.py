#!/usr/bin/env python3
"""
AJT Grounded Extract - CLI Runner

Extract structured data only when it can be proven; otherwise stop—and prove that you stopped.
"""
import sys
import json
from pathlib import Path

from engine.pipeline import ExtractionPipeline
from viewer.viewer_generator import EvidenceViewer


def main():
    """Run extraction pipeline with evidence viewer generation."""
    if len(sys.argv) < 2:
        print("Usage: python run.py <document_path>")
        print("\nExamples:")
        print("  python run.py examples/accept_example.txt")
        print("  python run.py examples/stop_example.txt")
        sys.exit(1)

    document_path = sys.argv[1]

    if not Path(document_path).exists():
        print(f"Error: Document not found: {document_path}")
        sys.exit(1)

    print("=" * 70)
    print("AJT GROUNDED EXTRACT")
    print("=" * 70)
    print()

    # Run pipeline
    pipeline = ExtractionPipeline()
    output = pipeline.run(document_path)

    print()
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()

    # Display results
    for result in output["results"]:
        print(f"Field: {result['field_name']}")
        print(f"  Decision: {result['decision']}")
        if result['decision'] == 'ACCEPT':
            print(f"  Value: {result['value']}")
            print(f"  Confidence: {result['confidence']:.2f}")
            print(f"  Evidence: \"{result['evidence']['quote']}\"")
        elif result['decision'] == 'STOP':
            print(f"  Reason: {result['stop_reason']}")
            print(f"  Proof: {json.dumps(result['stop_proof'], indent=4)}")
        print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Total fields: {output['summary']['total_fields']}")
    print(f"  Accepted: {output['summary']['accepted']}")
    print(f"  Stopped: {output['summary']['stopped']}")
    print(f"  Need Review: {output['summary']['need_review']}")
    print()

    # Generate viewer
    print("=" * 70)
    print("GENERATING VIEWER")
    print("=" * 70)

    # Load document content
    with open(document_path, 'r') as f:
        content = f.read()

    viewer = EvidenceViewer()
    doc_name = Path(document_path).stem
    viewer_path = viewer.generate(
        output["results"],
        content,
        f"viewer/{doc_name}_viewer.html"
    )

    print(f"  HTML viewer: {viewer_path}")
    print(f"  Evidence artifacts: {output['artifact_refs']['manifest_path']}")
    print()
    print("✓ Extraction complete")
    print()


if __name__ == "__main__":
    main()
