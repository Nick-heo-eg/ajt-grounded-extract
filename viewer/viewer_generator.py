"""
Generate HTML evidence viewer with highlighting and navigation.
"""
import json
from pathlib import Path
from typing import Dict, List


class EvidenceViewer:
    """Generate interactive HTML viewer for extraction results."""

    def generate(
        self,
        results: List[Dict],
        document_content: str,
        output_path: str = "viewer/output.html"
    ):
        """
        Generate HTML viewer with:
        - Document with highlighted evidence spans
        - Accept/Stop color coding
        - "Why Stopped" panel for STOP decisions
        - Navigation sidebar
        """
        html = self._build_html(results, document_content)

        output = Path(output_path)
        output.parent.mkdir(exist_ok=True)
        with open(output, 'w') as f:
            f.write(html)

        return str(output)

    def _build_html(self, results: List[Dict], content: str) -> str:
        """Build complete HTML document."""
        # Collect all evidence spans
        spans = []
        for result in results:
            if result["evidence"]:
                spans.append({
                    "start": result["evidence"]["start"],
                    "end": result["evidence"]["end"],
                    "decision": result["decision"],
                    "field": result["field_name"],
                    "value": result["value"],
                    "confidence": result["confidence"]
                })

        # Sort spans by start position
        spans.sort(key=lambda s: s["start"])

        # Build highlighted content
        highlighted = self._highlight_content(content, spans)

        # Build sidebar
        sidebar = self._build_sidebar(results)

        # Build stop panel
        stop_panel = self._build_stop_panel(results)

        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Evidence Viewer - AJT Grounded Extract</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            display: grid;
            grid-template-columns: 300px 1fr 350px;
            height: 100vh;
            overflow: hidden;
        }}
        .sidebar {{
            background: #f8f9fa;
            border-right: 1px solid #dee2e6;
            overflow-y: auto;
            padding: 20px;
        }}
        .sidebar h2 {{
            font-size: 16px;
            margin-bottom: 16px;
            color: #212529;
        }}
        .field-item {{
            margin-bottom: 12px;
            padding: 12px;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s;
        }}
        .field-item:hover {{
            background: #e9ecef;
        }}
        .field-item.accept {{
            border-left: 4px solid #28a745;
        }}
        .field-item.stop {{
            border-left: 4px solid #dc3545;
        }}
        .field-name {{
            font-weight: 600;
            font-size: 14px;
            margin-bottom: 4px;
        }}
        .field-value {{
            font-size: 13px;
            color: #6c757d;
        }}
        .content-panel {{
            overflow-y: auto;
            padding: 40px;
            background: white;
        }}
        .document {{
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
            white-space: pre-wrap;
            font-family: "SF Mono", Monaco, monospace;
            font-size: 14px;
        }}
        .evidence-span {{
            padding: 2px 4px;
            border-radius: 3px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .evidence-span:hover {{
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .evidence-span.accept {{
            background: #d4edda;
            border-bottom: 2px solid #28a745;
        }}
        .evidence-span.stop {{
            background: #f8d7da;
            border-bottom: 2px solid #dc3545;
        }}
        .stop-panel {{
            background: #fff5f5;
            border-left: 1px solid #dee2e6;
            overflow-y: auto;
            padding: 20px;
        }}
        .stop-panel h2 {{
            font-size: 16px;
            color: #dc3545;
            margin-bottom: 16px;
        }}
        .stop-event {{
            margin-bottom: 20px;
            padding: 16px;
            background: white;
            border-radius: 6px;
            border: 1px solid #f5c6cb;
        }}
        .stop-reason {{
            font-weight: 600;
            font-size: 14px;
            color: #721c24;
            margin-bottom: 8px;
        }}
        .stop-proof {{
            font-size: 13px;
            color: #495057;
            background: #f8f9fa;
            padding: 8px;
            border-radius: 4px;
            font-family: monospace;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
        }}
        .badge.accept {{
            background: #28a745;
            color: white;
        }}
        .badge.stop {{
            background: #dc3545;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>Extracted Fields</h2>
        {sidebar}
    </div>
    <div class="content-panel">
        <div class="document">
{highlighted}
        </div>
    </div>
    <div class="stop-panel">
        <h2>Why Stopped?</h2>
        {stop_panel}
    </div>
</body>
</html>"""

    def _highlight_content(self, content: str, spans: List[Dict]) -> str:
        """Insert highlight spans into content."""
        if not spans:
            return self._escape_html(content)

        result = []
        last_pos = 0

        for span in spans:
            # Add text before span
            if span["start"] > last_pos:
                result.append(
                    self._escape_html(content[last_pos:span["start"]])
                )

            # Add highlighted span
            text = self._escape_html(content[span["start"]:span["end"]])
            css_class = span["decision"].lower()
            result.append(
                f'<span class="evidence-span {css_class}" '
                f'data-field="{span["field"]}">'
                f'{text}</span>'
            )

            last_pos = span["end"]

        # Add remaining text
        if last_pos < len(content):
            result.append(self._escape_html(content[last_pos:]))

        return ''.join(result)

    def _build_sidebar(self, results: List[Dict]) -> str:
        """Build field navigation sidebar."""
        items = []
        for result in results:
            css_class = result["decision"].lower()
            value_display = result["value"] or "—"

            items.append(f"""
                <div class="field-item {css_class}">
                    <div class="field-name">{result["field_name"]}</div>
                    <div class="field-value">{value_display}</div>
                    <span class="badge {css_class}">{result["decision"]}</span>
                </div>
            """)

        return '\n'.join(items)

    def _build_stop_panel(self, results: List[Dict]) -> str:
        """Build 'Why Stopped' panel."""
        stop_events = [r for r in results if r["decision"] == "STOP"]

        if not stop_events:
            return "<p style='color: #6c757d;'>No stop events</p>"

        items = []
        for event in stop_events:
            proof_json = json.dumps(
                event.get("stop_proof", {}), indent=2
            )

            items.append(f"""
                <div class="stop-event">
                    <div class="stop-reason">
                        {event["field_name"]}: {event["stop_reason"]}
                    </div>
                    <div class="stop-proof">{self._escape_html(proof_json)}</div>
                </div>
            """)

        return '\n'.join(items)

    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters."""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))
