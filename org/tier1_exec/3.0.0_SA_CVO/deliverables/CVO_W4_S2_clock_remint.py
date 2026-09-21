"""Write NFRA_MCPINDEX-W4-S2's clock on the disarm owner's VERIFIED word (R-15).

The owner ACTS and files the evidence; the CVO WRITES the clock -- surprise-row-gate.py:111,
read at the bytes rather than recalled. 2.0.0_SA_COO~M sent the word (99014) and this seat
verified every load-bearing claim against git before writing.

The carrier does NOT exist, so this is a MINT, not a flip -- and the clock is set at BIRTH,
which is the only moment it can be. The item's DISPOSITION is NOT touched: R-19, disarming is
not disposing, and W4-S2 stays UNDER_INVESTIGATION for round 1's L9.
"""
import datetime
import glob
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, ".tools")
import jsonschema

RID = "NFRA_MCPINDEX-W4-S2"
OWNER = "2.0.0_SA_COO~M"
REM = "org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/remediations/REMEDIATION_v1.md"
SCHEMA = json.load(open("org/surprise_channel/schemas/remediation_row.schema.json", encoding="utf-8"))
AT = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

# ---- guard 1: the investigation row must read ARMED with this disarm owner ----
inv = None
for p in glob.glob("org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/*.md"):
    t = open(p, encoding="utf-8").read()
    for m in re.finditer(r"```json\n(.*?)\n```", t, re.S):
        try:
            o = json.loads(m.group(1))
        except Exception:
            continue
        for r in (o if isinstance(o, list) else [o]):
            if isinstance(r, dict) and r.get("id") == RID:
                inv = r
if inv is None:
    raise SystemExit("no investigation row for %s" % RID)
if inv.get("hazard_standing") != "ARMED":
    raise SystemExit("%s reads hazard_standing %r -- only an ARMED row carries a two-state clock" % (RID, inv.get("hazard_standing")))
if inv.get("disarm_owner") != OWNER:
    raise SystemExit("%s names disarm_owner %r, not %r -- the word must come from the named owner" % (RID, inv.get("disarm_owner"), OWNER))
print("guard 1 OK: ARMED, disarm_owner %s" % OWNER)

# ---- guard 2: MINT ONLY WHERE ABSENT (the clock is a birth property) ----
text = open(REM, encoding="utf-8").read() if os.path.exists(REM) else ""
if ('"%s"' % RID) in text:
    raise SystemExit("%s ALREADY has a remediation row -- one row per id, ever; this would be a mutation" % RID)
print("guard 2 OK: no existing carrier -- mintable, and the clock can exist at birth")

# ---- guard 3: re-verify the owner's load-bearing evidence AT WRITE TIME ----
def out(*a):
    return subprocess.check_output(list(a), text=True, encoding="utf-8", errors="replace").strip()

loss = len([x for x in out("git", "diff", "--name-only", "0c46bec859^1", "0c46bec859").split("\n") if x.strip()])
rep = [x for x in out("git", "diff", "--name-only", "155533ea00^1", "155533ea00").split("\n") if x.strip()]
ident = 0
for f in rep:
    try:
        if out("git", "rev-parse", "edf584f64a:" + f) == out("git", "rev-parse", "18f48e87d4:" + f):
            ident += 1
    except subprocess.CalledProcessError:
        pass
order = [ln for ln in out("git", "ls-files", "org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/").split("\n") if ".TO-MX-a-3." in ln][0]
word = re.search(r"<status>\s*([A-Za-z_-]+)", out("git", "show", "HEAD:" + order)).group(1)
print("guard 3: loss diff=%d file(s); repair merge=%d file(s); identical-at-repair=%d; MX-a-3 word=%r"
      % (loss, len(rep), ident, word))
if loss != 1 or len(rep) != 5 or ident != 4 or word != "complete":
    raise SystemExit("EVIDENCE MOVED since verification -- refusing to write the clock")
print("guard 3 OK: every load-bearing claim re-verified at write time")

row = {
    "id": RID,
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "class": inv.get("class", "OBSERVATION"),
    "hazard_standing": "ARMED",
    "mechanism": "Drain merge 0c46bec859 named worker commit edf584f64a as a parent, so history read the branch as MERGED while its first-parent diff carried 1 file against the branch's 6. Four MX-a-3 deliverables were absent at CLOUD and no later merge of that branch could ever restore them, because the ancestry already counted it merged.",
    "evidence": [
        "DISARM WORD from the named disarm owner 2.0.0_SA_COO~M, msg 99014; clock written by 3.0.0_SA_CVO per surprise-row-gate.py:111 and R-15.",
        "LOSS re-measured at write time: git diff --name-only 0c46bec859^1 0c46bec859 = 1 file.",
        "REPAIR MERGE 155533ea00 first-parent diff = 5 files, the branch's full set.",
        "4 of the 5 byte-identical between edf584f64a and the repair commit 18f48e87d4 by git rev-parse; the proof instance differs in one field, artifacts_produced[3].commit_or_etag, re-pinned from PENDING-THIS-COMMIT to edf584f64a. No criterion row, verdict or evidence moved.",
        "MX-a-3 reads <status>complete at HEAD, re-read at write time.",
        "CVO NOTE, recorded because it nearly became a false finding: a HEAD-vs-edf584f64a comparison shows 2 files differing, not 1. That is an artifact of the wrong vintage -- probes/_mutant_control.py changed later at 2433831f8c (03:48:27Z) under separate MX-a-4 work. Compared at the owner's own stated vintage the claim holds exactly.",
        "The owner disclosed its own subject-line overclaim on 18f48e87d4 ('restored byte-identical' where the body states 4 of 5 plus one re-pinned field), and its drain practice is changed to compare the merge's file SET and each blob against the branch rather than a count.",
    ],
    "remedy": "Repaired at 18f48e87d4 and merged at 155533ea00; the five files and the complete flip are at CLOUD. The recurrence control is the owner's changed drain practice: compare file set and blobs, never a count.",
    "owner": OWNER,
    "round": "v1",
    "disarm": {"state": "DISARMED", "owner": OWNER, "at": AT},
    "remediation": {"state": "REMEDIATED", "owner": OWNER, "round": "v1"},
    "closed": True,
}
jsonschema.validate(row, SCHEMA)
print("row validated against remediation_row.schema.json")
if chr(96) * 3 in json.dumps(row):
    raise SystemExit("row contains a fence marker")

F = chr(96) * 3
na = sum(1 for c in text if ord(c) > 127)
add = ("\n## Round-1 clock on the disarm owner's verified word (3.0.0_SA_CVO, %s)\n" % AT
       + "\n" + F + "json\n" + json.dumps(row, indent=1, ensure_ascii=True) + "\n" + F + "\n")
new = (text or "# NFRA_MCPINDEX -- remediation rows\n") + add
if sum(1 for c in new if ord(c) > 127) != na + sum(1 for c in add if ord(c) > 127):
    raise SystemExit("non-ASCII count moved")
os.makedirs(os.path.dirname(REM), exist_ok=True)
open(REM, "w", encoding="utf-8", newline="\n").write(new)
print("WROTE %s (%d bytes)" % (REM, len(new.encode())))
print()
print("R-19 held: the ITEM's disposition is untouched -- W4-S2 stays UNDER_INVESTIGATION for round 1's L9.")
