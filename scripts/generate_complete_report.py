"""Generate a complete organized MCATalyst report from extracted JSON rows.

Usage:
  python scripts/generate_complete_report.py \
      --input all_questions.json \
      --output MCATALYST_COMPLETE_REPORT.md
"""

import argparse
import json
from collections import defaultdict


def build_report(rows):
    by_mode = defaultdict(list)
    for row in rows:
        by_mode[(row.get("category", "unknown"), row.get("mode", "unknown"))].append(row)

    for key in by_mode:
        by_mode[key].sort(key=lambda x: (x.get("question") or "").lower())

    by_category = defaultdict(list)
    for (category, mode), questions in by_mode.items():
        by_category[category].append((mode, questions))

    for category in by_category:
        by_category[category].sort(key=lambda pair: pair[0])

    lines = []
    lines.append("# MCATalyst Complete Quiz & Variant Report")
    lines.append("")
    lines.append("Source: `https://app.mcat-alyst.com/home`")
    lines.append("")
    lines.append(f"Total active questions extracted: **{len(rows)}**")
    lines.append("")
    lines.append("## Inventory by Category and Mode")
    lines.append("")

    for category in sorted(by_category):
        category_total = sum(len(questions) for _, questions in by_category[category])
        lines.append(f"### {category} (total {category_total})")
        for mode, questions in by_category[category]:
            lines.append(f"- `{mode}`: {len(questions)} questions")
        lines.append("")

    lines.append("## Full Question Bank by Category and Mode")
    lines.append("")

    for category in sorted(by_category):
        lines.append(f"## Category: {category}")
        lines.append("")
        for mode, questions in by_category[category]:
            lines.append(f"### Mode: {mode} ({len(questions)} questions)")
            lines.append("")
            for index, row in enumerate(questions, 1):
                question = (row.get("question") or "").replace("\n", " ").strip()
                lines.append(f"{index}. **Question:** {question}")

                options = row.get("options") or []
                if options:
                    lines.append("   - **Choices:**")
                    for option_index, option in enumerate(options, 1):
                        lines.append(f"     {option_index}. {str(option).strip()}")
                else:
                    lines.append("   - **Choices:** _(none provided)_")

                lines.append(f"   - **Correct Answer:** {row.get('answer')}")

                explanation = row.get("explanation")
                if explanation is None or str(explanation).strip() == "":
                    lines.append("   - **Feedback:** None / empty")
                else:
                    normalized = str(explanation).replace("\n", " ").strip()
                    lines.append(f"   - **Feedback:** {normalized}")

                if row.get("image"):
                    lines.append(f"   - **Image:** {row.get('image')}")

                lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="all_questions.json")
    parser.add_argument("--output", default="MCATALYST_COMPLETE_REPORT.md")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as handle:
        rows = json.load(handle)

    report = build_report(rows)

    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(report)

    print(f"Wrote report for {len(rows)} questions to {args.output}")


if __name__ == "__main__":
    main()
