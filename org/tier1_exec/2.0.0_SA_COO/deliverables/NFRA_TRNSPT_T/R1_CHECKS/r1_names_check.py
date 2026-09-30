"""TR-i-1 AC2 -- every resource name in pull.tf is lib.opal_naming.name() output (issuer's check; base: FAIL as expected).

Reads data/transcripts/scripts/teams/NAMES.json: {"<logical>": {"system","scope","function","kind","qualifier","name"}}.
For each row: name(...) == row.name, and row.name appears verbatim in infra/aws/terraform/transcripts/pull.tf.
Prints NAMES-CONFORMANT n=N, else NAMES-BAD <reason>.
"""
import json
import sys


def main():
    sys.path.insert(0, ".")
    from lib.opal_naming import name  # noqa: E402
    try:
        rows = json.load(open("data/transcripts/scripts/teams/NAMES.json", encoding="utf-8"))
        tf = open("infra/aws/terraform/transcripts/pull.tf", encoding="utf-8").read()
    except Exception as e:  # noqa: BLE001
        print("NAMES-BAD unreadable: %s" % e)
        return 1
    if not rows:
        print("NAMES-BAD empty NAMES.json")
        return 1
    for logical, r in rows.items():
        try:
            built = name(r["system"], r["scope"], r["function"], r["kind"], r.get("qualifier"))
        except Exception as e:  # noqa: BLE001
            print("NAMES-BAD %s: builder refused (%s)" % (logical, e))
            return 1
        if built != r["name"]:
            print("NAMES-BAD %s: recorded %r != built %r" % (logical, r["name"], built))
            return 1
        if r["name"] not in tf:
            print("NAMES-BAD %s: %r not in pull.tf" % (logical, r["name"]))
            return 1
    print("NAMES-CONFORMANT n=%d" % len(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
