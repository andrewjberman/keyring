"""Grade P's four read-only securities_info responses against the maintained comparison catalogue (CTO 102028 (1)).

    python comparison_identity.py --catalogue <templates.json> --evidence <evidence.json> [--out <record.json>]

The evidence file is what P's window retains (P_COMPARISON_IDENTITY_READ_ACT_20260927.md):
    {"retrieved_at": "...Z", "reads": [{"identity": "P:1728413", "status": 200, "content_type": "application/json",
      "waf_action": null, "login_destination": false, "body": <the response JSON, verbatim>}, ...]}

Each catalogue entry is graded on its own read, by the research worker's rules (variant_worker.security_info and the
comparison checks): exactly one returned row carries the entry's security_id; its security_name equals the entry's
label; its detailed_security_type is model_portfolio. It grades IDENTITY only. The reporting permission (entitlement)
is Andrew's word (CTO 102028 (2)); nothing here reads it, and the output says so. No network call, no write but --out.
"""
import argparse
import hashlib
import json
import sys

VERDICTS = ("IDENTITY_VERIFIED", "READ_REFUSED", "NOT_UNIQUE", "NAME_DRIFT", "TYPE_MISMATCH", "NO_READ")
ADMITTED_TYPES = ("model_portfolio",)


def grade(entry, read):
    """One entry against its read: (verdict, measured)."""
    if read is None:
        return "NO_READ", {}
    if (read.get("status") != 200 or read.get("content_type") != "application/json" or read.get("waf_action")
            or read.get("login_destination")):
        return "READ_REFUSED", {"status": read.get("status"), "waf_action": read.get("waf_action"),
                                "login_destination": read.get("login_destination")}
    rows = [r for r in read.get("body") or [] if isinstance(r, dict) and r.get("security_id") == entry["security_id"]]
    if len(rows) != 1:
        return "NOT_UNIQUE", {"matching_rows": len(rows)}
    row = rows[0]
    measured = {"security_id": row["security_id"], "security_name": row.get("security_name"),
                "detailed_security_type": row.get("detailed_security_type"), "instance_id": row.get("instance_id")}
    if not isinstance(row.get("security_name"), str) or row["security_name"].strip() != entry["label"].strip():
        return "NAME_DRIFT", measured
    if row.get("detailed_security_type") not in ADMITTED_TYPES:
        return "TYPE_MISMATCH", measured
    return "IDENTITY_VERIFIED", measured


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--catalogue", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    catalogue = json.load(open(a.catalogue, encoding="utf-8"))["comparison_catalog"]
    raw = open(a.evidence, "rb").read()
    evidence = json.loads(raw)
    reads = {}
    for read in evidence["reads"]:
        reads.setdefault(read["identity"], []).append(read)
    results = []
    for entry in catalogue["entries"]:
        mine = reads.get(entry["security_id"], [])
        verdict, measured = grade(entry, mine[0] if len(mine) == 1 else None) if len(mine) <= 1 else \
            ("NOT_UNIQUE", {"reads": len(mine)})
        results.append({"key": entry["key"], "security_id": entry["security_id"], "label": entry["label"],
                        "verdict": verdict, "measured": measured})
        print("%-18s %-24s %-11s %s" % (verdict, entry["key"], entry["security_id"], json.dumps(measured)[:150]))
    stray = sorted(set(reads) - {e["security_id"] for e in catalogue["entries"]})
    verified = sum(r["verdict"] == "IDENTITY_VERIFIED" for r in results)
    record = {"catalogue_version": catalogue["candidate_version"], "evidence_sha256": hashlib.sha256(raw).hexdigest(),
              "retrieved_at": evidence.get("retrieved_at"), "identity": "%d/%d" % (verified, len(results)),
              "reads_outside_catalogue": stray, "entitlement": "NOT_READ_HERE (Andrew's word, CTO 102028 (2))",
              "results": results}
    print("\nIDENTITY %s | reads outside the catalogue %s | entitlement not read here" % (record["identity"], stray))
    if a.out:
        json.dump(record, open(a.out, "w", encoding="utf-8"), indent=1)
        print("WROTE", a.out)
    return 0 if verified == len(results) and not stray else 1


if __name__ == "__main__":
    sys.exit(main())
