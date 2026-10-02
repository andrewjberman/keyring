"""Apply the HARVST reconciliation: advance 14 existing rows in place (clocks only) and write REMEDIATION_v5.md from the draft."""
import json
import sys

S = sys.argv[1]
NOW = sys.argv[2]  # e.g. 2026-10-02T20:31Z
D = "org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/remediations/"

adv = json.load(open(S + "/advance_existing.json", encoding="utf-8"))
adv = adv if isinstance(adv, list) else adv.get("rows")
by_file = {}
for a in adv:
    by_file.setdefault(a["file"].replace("\\", "/").split("/")[-1], []).append(a)

for fname, items in by_file.items():
    path = D + fname
    t = open(path, encoding="utf-8", newline="").read()
    s = t.index("```json\n") + 8
    e = t.index("\n```", s)
    rows = json.loads(t[s:e])
    assert json.dumps(rows, indent=2) == t[s:e], fname
    idx = {r["id"]: r for r in rows}
    for a in items:
        r = idx[a["id"]]
        r["remediation"]["state"] = "REMEDIATED"
        r["closed"] = True
        if a.get("new_disarm_state") == "DISARMED" and isinstance(r.get("disarm"), dict) and r["disarm"].get("state") != "DISARMED":
            r["disarm"]["state"] = "DISARMED"
            if not r["disarm"].get("at"):
                r["disarm"]["at"] = NOW
    t = t[:s] + json.dumps(rows, indent=2) + t[e:]
    open(path, "w", encoding="utf-8", newline="").write(t)
    print(fname, "advanced", len(items))

draft = open(S + "/REMEDIATION_v5.draft.md", encoding="utf-8", newline="").read()
draft = draft.replace("Recorded: 2026-10-02 (DRAFT, not committed).", "Recorded: %s." % NOW.replace("Z", ":00Z"), 1)
assert "DRAFT" not in draft.split("```json")[0], "header still says DRAFT"
table = ["", "**The 14 older rows advanced in place (clocks only: remediation REMEDIATED, closed true, an ARMED disarm DISARMED; where a",
         "row carried no disarm time, `at` is this seat's recording minute %s, not the fix's own time):**" % NOW, "",
         "| row | file | evidence |", "|---|---|---|"]
for a in adv:
    ev = a["evidence"] if isinstance(a["evidence"], str) else "; ".join(a["evidence"])
    table.append("| `%s` | %s | %s |" % (a["id"].replace("AMGT_HARVST-", ""), a["file"].replace("\\", "/").split("/")[-1], ev.replace("|", "/")))
table.append("")
head, sep, rest = draft.partition("```json")
draft = head.rstrip("\n") + "\n" + "\n".join(table) + "\n" + sep + rest
open(D + "REMEDIATION_v5.md", "w", encoding="utf-8", newline="").write(draft)
print("v5 written, nonascii", len(draft.encode("utf-8")) - len(draft))
