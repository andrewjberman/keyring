"""TR-k-1 AC1 -- the commentary gold contract file carries C-GOLD-FIELDS exactly (issuer's check; base: FAIL as expected).

Prints GOLD-CONTRACT-OK fields=N, else GOLD-CONTRACT-BAD <reason>.
"""
import json
import sys

PATH = "org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json"
REQUIRED = ["record_id", "sent_at", "recipient_firm", "yc_variant", "models_referenced", "account_type", "themes",
            "body_text", "paragraph_hashes", "body_hash", "pdf_sha256", "has_pdf", "holdings", "request_text"]
NULLABLE = {"holdings", "request_text"}
FORBIDDEN = {"approved", "finder_status", "sent_external"}


def main():
    try:
        c = json.load(open(PATH, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print("GOLD-CONTRACT-BAD unreadable: %s" % e)
        return 1
    for k in ("contract", "version", "table", "fields", "one_opal_shape"):
        if k not in c:
            print("GOLD-CONTRACT-BAD missing top-level %s" % k)
            return 1
    fields = {f["name"]: f for f in c["fields"]}
    missing = [f for f in REQUIRED if f not in fields]
    extra_forbidden = FORBIDDEN & set(fields)
    if missing or extra_forbidden:
        print("GOLD-CONTRACT-BAD missing=%s forbidden=%s" % (missing, sorted(extra_forbidden)))
        return 1
    for nm, f in fields.items():
        for k in ("type", "nullable", "derivation", "claim"):
            if k not in f:
                print("GOLD-CONTRACT-BAD field %s lacks %s" % (nm, k))
                return 1
        if (nm in NULLABLE) != bool(f["nullable"]):
            print("GOLD-CONTRACT-BAD field %s nullable=%r (contract says %r)" % (nm, f["nullable"], nm in NULLABLE))
            return 1
        if f["claim"] not in ("measured", "inferred", "held", "absent"):
            print("GOLD-CONTRACT-BAD field %s claim=%r off the enum" % (nm, f["claim"]))
            return 1
    if c["table"] != "analysis_commentary":
        print("GOLD-CONTRACT-BAD table=%r" % c["table"])
        return 1
    print("GOLD-CONTRACT-OK fields=%d version=%s" % (len(fields), c["version"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
