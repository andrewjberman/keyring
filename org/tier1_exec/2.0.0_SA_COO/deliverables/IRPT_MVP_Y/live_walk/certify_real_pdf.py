"""Grade a real vendor PDF through the deployed publication boundary, and print WHY a row fails.

Usage: python certify_real_pdf.py --package <resident package root> --pdf <vendor.pdf> --census <census.json>

Runs the package's own ycharts/extract code, the same path the resident's publisher runs:
extract.extract, then publication.verify_extraction (scalar certify, then the chart rows through
publication._chart and certify.certify). On a refusal it re-runs the failing certify step and prints
every non-PASS row's verdict and reason. It is a local read: no AWS, no vendor.
"""
import argparse
import json
import os
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--census", required=True)
    ap.add_argument("--label", default="vendor_real")
    a = ap.parse_args()
    root = os.path.abspath(a.package)
    sys.path.insert(0, os.path.join(root, "ycharts", "extract"))
    import certify
    import extract
    import publication

    for name, mod in (("certify", certify), ("extract", extract), ("publication", publication)):
        if not os.path.samefile(os.path.dirname(mod.__file__), os.path.join(root, "ycharts", "extract")):
            raise SystemExit("ERROR: %s loaded from %s, not the package" % (name, mod.__file__))
    pdf = open(a.pdf, "rb").read()
    census = extract.load_census(a.census)
    result = extract.extract(pdf, census, specimen_label=a.label, specimen_id="real-overview")
    print("EXTRACT: sections=%d charts=%d disclosures=%d unlocated=%d unit_conflicts=%d"
          % tuple(len(result[k]) for k in ("sections", "charts", "disclosures", "unlocated", "unit_conflicts")))
    try:
        publication.verify_extraction(pdf, census, result)
        print("RESULT: PUBLISHED (no refusal)")
        return 0
    except publication.PublicationRefused as refusal:
        print("RESULT: REFUSED", refusal)
    scalars = certify.certify(result["sections"], pdf, census=census)
    print("SCALARS:", scalars["denominator"], scalars["by_verdict"])
    pages = extract.read_pages(pdf)
    charts = [c for c in (publication._chart(row, pages) for row in result["charts"]) if c is not None]
    graded = certify.certify(charts, pdf, census=census)
    print("CHARTS:", graded["denominator"], graded["by_verdict"])
    for row, grade in zip(charts, graded["rows"]):
        if grade["verdict"] != "CERTIFIED":
            detail = {k: v for k, v in grade.items() if k not in ("row",)}
            print("  FAIL", row["section_id"], "page", row["page"], "claim", row["date_claim"],
                  "as_of", row.get("as_of_date"), "|", json.dumps(detail, default=str)[:400])
    return 1


if __name__ == "__main__":
    sys.exit(main())
