"""TR-w-2 AC1 -- the round-2 planted-token gate record carries the two new classes with a stated outcome (issuer's check).

usage: python r2_wipe_record_check.py <WIPE_GATE_RECORD_R2.json>
Requires: result == "the planted classes were removed"; not_claimed == "no PII remains"; classes
"lowercase_standalone_name" and "sentence_start_word_surname" present, each with planted >= 1 and outcome in
{"removed", "stated_limit"}, and a limit_text when stated_limit; every round-1 class still present with removed == planted.
Prints WIPE-RECORD-OK classes=N new_removed=R new_limits=L, else WIPE-RECORD-BAD <reason>. Base: FAIL (no record).
"""
import json
import sys

NEW = ("lowercase_standalone_name", "sentence_start_word_surname")


def main(path):
    try:
        rec = json.load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print("WIPE-RECORD-BAD unreadable: %s" % e)
        return 1
    if rec.get("result") != "the planted classes were removed" or rec.get("not_claimed") != "no PII remains":
        print("WIPE-RECORD-BAD result/not_claimed wording changed")
        return 1
    classes = rec.get("classes") or {}
    if not classes:
        print("WIPE-RECORD-BAD no per-class table (expected classes: {name: {planted, removed, outcome}})")
        return 1
    removed_new = limits = 0
    for c in NEW:
        row = classes.get(c)
        if not row or int(row.get("planted", 0)) < 1:
            print("WIPE-RECORD-BAD new class %s absent or not planted" % c)
            return 1
        if row.get("outcome") == "removed" and int(row.get("removed", 0)) == int(row["planted"]):
            removed_new += 1
        elif row.get("outcome") == "stated_limit" and row.get("limit_text"):
            limits += 1
        else:
            print("WIPE-RECORD-BAD class %s outcome %r without removal or limit_text" % (c, row.get("outcome")))
            return 1
    for c, row in classes.items():
        if c in NEW:
            continue
        if int(row.get("removed", -1)) != int(row.get("planted", -2)):
            print("WIPE-RECORD-BAD round-1 class %s regressed: removed %s of %s" % (c, row.get("removed"), row.get("planted")))
            return 1
    print("WIPE-RECORD-OK classes=%d new_removed=%d new_limits=%d" % (len(classes), removed_new, limits))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("WIPE-RECORD-BAD usage")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
