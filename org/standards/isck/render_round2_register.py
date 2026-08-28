#!/usr/bin/env python3
"""Render ROUND{N}_FINDING_REGISTER.md from ROUND{N}_FINDING_REGISTER.json (default round 2; --round 3 ...).

Every statistic in the rendered file is DERIVED here from the rows; none is typed. Run:
    python org/standards/isck/render_round2_register.py            # writes the .md
    python org/standards/isck/render_round2_register.py --check    # exit 1 if the .md is stale
"""
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROUND = sys.argv[sys.argv.index("--round") + 1] if "--round" in sys.argv else "2"
SRC = HERE / f"ROUND{ROUND}_FINDING_REGISTER.json"
OUT = HERE / f"ROUND{ROUND}_FINDING_REGISTER.md"
OPEN_MARKERS = ("OPEN-CITATION", "OPEN-CLAIM-TEXT")


def render(reg):
    rows = reg["findings"]
    ids = [r["finding_id"] for r in rows]
    dupes = [i for i, n in Counter(ids).items() if n > 1]
    if dupes:
        raise SystemExit("ERROR: duplicate finding_id(s): %s" % dupes)
    by_seat = Counter(r["source_seat"] for r in rows)
    by_class = Counter(r["finding_class"] for r in rows)
    by_disp = Counter(r["disposition"] for r in rows)
    by_incl = Counter(r["boundary_inclusion"] for r in rows)
    refuted = [r for r in rows if r["disposition"] in ("SELF-REFUTED", "REFUTED")]
    verifier_self = [r for r in rows if r["finding_class"] == "VERIFIER-SELF"]
    open_rows = [r for r in rows if any(m in (r["fix_commit"] + r["verification_ref"] + r["claim"] + r["disposition"]) for m in OPEN_MARKERS)]
    substantive = [r for r in rows if r["finding_class"] != "VERIFIER-SELF" and r["disposition"] not in ("SELF-REFUTED", "REFUTED")]
    upheld = [r for r in substantive if r["disposition"] not in ("OPEN-CITATION",)]

    L = []
    L.append("# ISCK ROUND-%d FINDING REGISTER (rendered -- do not edit; source is %s)\n" % (reg["round"], SRC.name))
    L.append("Round %d · attacked input `%s` · charter `%s` · boundary pin `%s` · boundary record `%s`\n"
             % (reg["round"], reg["attacked_input"], reg["charter"],
                reg.get("boundary_pin") or "(round open)", reg.get("boundary_record") or "(round open)"))
    L.append("## 0. STATISTICS (every number below is derived from the rows by render_round2_register.py)\n")
    L.append("- **Rows (one id per finding): %d.** The boundary record's \"~40 listed contributions\" is NOT this number; acceptances, inputs, corroborations and censuses are listed in `not_rows` and excluded." % len(rows))
    L.append("- **Substantive findings (excluding verifier self-corrections and self-refuted claims): %d.** Upheld: %d." % (len(substantive), len(upheld)))
    L.append("- **Refuted: %d of %d claims filed (%s).** A refutation rate is quotable only from this line."
             % (len(refuted), len(substantive) + len(refuted), ", ".join(r["finding_id"] for r in refuted) or "none"))
    L.append("- **Verifier self-corrections on the record: %d** (%s)." % (len(verifier_self), ", ".join(r["finding_id"] for r in verifier_self)))
    L.append("- **Rows with an OPEN-CITATION or OPEN-CLAIM-TEXT gap: %d of %d** (%s) -- honest gaps, listed in sec 3, to be closed by re-reading the origin message / re-deriving the commit."
             % (len(open_rows), len(rows), ", ".join(r["finding_id"] for r in open_rows)))
    L.append("- By seat: " + " · ".join("`%s` %d" % (k, v) for k, v in sorted(by_seat.items())))
    L.append("- By class: " + " · ".join("%s %d" % (k, v) for k, v in sorted(by_class.items())))
    L.append("- By disposition: " + " · ".join("%s %d" % (k, v) for k, v in sorted(by_disp.items())))
    L.append("- By boundary inclusion: " + " · ".join("%s %d" % (k, v) for k, v in sorted(by_incl.items())))
    L.append("")
    L.append("## 1. CLASSES AND DISPOSITIONS (the closed vocabularies)\n")
    for k, v in reg["classes"].items():
        L.append("- **%s** -- %s" % (k, v))
    L.append("")
    for k, v in reg["dispositions"].items():
        L.append("- **%s** -- %s" % (k, v))
    L.append("")
    L.append("## 2. THE REGISTER\n")
    L.append("| id | seat | source | class | claim | disposition | basis | fix commit | verification | boundary |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        L.append("| %s | `%s` | %s | %s | %s | %s | %s | %s | %s | %s |" % tuple(
            str(r[k]).replace("|", "\\|") for k in ("finding_id", "source_seat", "source_ref", "finding_class", "claim", "disposition", "disposition_basis", "fix_commit", "verification_ref", "boundary_inclusion")))
    L.append("")
    L.append("## 3. OPEN GAPS IN THIS REGISTER (a register that hides its own holes is the tally it replaces)\n")
    for r in open_rows:
        L.append("- **%s** -- %s" % (r["finding_id"], "; ".join(
            "%s: %s" % (k, r[k]) for k in ("claim", "fix_commit", "verification_ref", "disposition") if any(m in str(r[k]) for m in OPEN_MARKERS))))
    L.append("")
    L.append("## 4. NOT ROWS (counted by the boundary tally, excluded here, so the exclusion is visible)\n")
    for k, v in reg["not_rows"].items():
        if k.startswith("$"):
            continue
        L.append("- **%s:** %s" % (k, "; ".join(v)))
    L.append("")
    return "\n".join(L)


def main():
    reg = json.loads(SRC.read_text(encoding="utf-8"))
    text = render(reg)
    if "--check" in sys.argv:
        cur = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if cur != text:
            print("STALE: %s does not match its source; re-run without --check" % OUT.name)
            sys.exit(1)
        print("OK: %s is current (%d rows)" % (OUT.name, len(reg["findings"])))
        return
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote %s (%d rows)" % (OUT.name, len(reg["findings"])))


if __name__ == "__main__":
    main()
