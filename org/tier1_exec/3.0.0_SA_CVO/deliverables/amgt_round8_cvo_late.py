"""Admit only committed late S63; never sweep the peer's investigation draft."""

import datetime
import json
import re
import subprocess
from amgt_round8_cvo_intake import ROOT, HOME, PROJECT, records

path = PROJECT + "/surprise-channel/investigations/INVESTIGATION_v1.md"
pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
blob = subprocess.check_output(["git", "show", pin + ":" + path], cwd=ROOT).decode(
    "utf-8"
)
original = next((r for r in records(blob) if r["id"] == "AMGT_RESAPP-Z-S63"), None)
if original is None:
    print("S63 remains an uncommitted peer draft; no review artifact changed.")
    raise SystemExit(0)
utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
evidence_path = "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND8_CVO_LATE_20260913_Z.json"
world = "The timed evidence corroborates S45: this CVO read exact packet 22183 and produced round-8 evidence while its receipt remained QUEUED. The owner used the deliverables-plane veto successfully, satisfying the stated same-sweep condition. The proposed automatic nudge was not sent. File reading is not broker-client polling; archiving is after the authorized act, and the repository sendguard also rejects a COO ACK. This does not establish that all Codex seats lack worktrees or universally ACK only at session boundaries."
row = {
    "id": "AMGT_RESAPP-Z-C-S139",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": utc,
    "one_line": "S63: timed corroboration of the existing receipt-versus-production distinction",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZZZ",
    "grounding": {
        "status": "GROUNDED",
        "evidence": [evidence_path, path + "@" + pin + "#AMGT_RESAPP-Z-S63"],
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [original["id"]],
    "spec_asserts": original["spec_asserts"],
    "world_is": world,
    "dismissal_reason": world,
    "notes": "Corroborating recovery/probe evidence, not another runtime or worker task. Keep the functioning progress veto; do not infer unread content from QUEUED or misdiagnose source files as lost on process termination.",
}
adj = ROOT / PROJECT / "surprise-channel/adjudications/ADJUDICATION_v8.md"
text = adj.read_text(encoding="utf-8")
rr = records(text)
assert not any(r["id"] == row["id"] for r in rr)
rr.append(row)
b = next(re.finditer(r"```json\s*(.*?)```", text, re.S))
head = (
    text[: b.start()]
    .replace("121 originals", "122 originals")
    .replace("27 reviewed here", "28 reviewed here")
)
head += "Late S63 is admitted only after its owner's commit. C-S139 records the timed receipt/progress distinction and accepts the already-functioning veto; it adds no duplicate remedy. The final original watermark is 122, with 28 reviewed this round.\n\n"
adj.write_text(
    head + "```json\n" + json.dumps(rr, indent=2) + "\n```\n", encoding="utf-8"
)
rem = ROOT / PROJECT / "surprise-channel/remediations/REMEDIATION_v8.md"
text = (
    rem.read_text(encoding="utf-8")
    .replace("all 121 original", "all 122 original")
    .replace("after 27 CVO reviews", "after 28 CVO reviews")
    .replace("late S61/S62", "late S61/S62/S63")
)
rem.write_text(text, encoding="utf-8")
compile_path = HOME / "AMGT_RESAPP_ROUND8_CVO_COMPILE_20260913_Z.json"
c = json.loads(compile_path.read_text())
c.update(originals=122, adjudication_rows=37, late_pin=pin)
c["reviewed_originals"].append(original["id"])
compile_path.write_text(json.dumps(c, indent=2) + "\n", encoding="utf-8")
(ROOT / evidence_path).write_text(
    json.dumps(
        {
            "utc": utc,
            "pin": pin,
            "original": original,
            "cvo_disposition": row,
            "limits": "Peer investigation committed before admission; original bytes untouched. Receipt diagnosis bounded to this seat/run.",
        },
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
print(
    json.dumps(
        {
            "late_pin": pin,
            "admitted": original["id"],
            "originals": 122,
            "new_adjudications": 37,
        }
    )
)
