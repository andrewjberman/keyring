"""Append two late original decisions before the round-7 commit watermark."""

import datetime
import json
import subprocess
from amgt_round7_cvo_write_review import (
    ROOT,
    PROJECT,
    CHANNEL,
    EVIDENCE,
    rows,
    SERIAL,
)

utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
investigation = PROJECT + "/surprise-channel/investigations/INVESTIGATION_v1.md"
late = {
    r["id"]: r
    for r in rows(ROOT / investigation)
    if r["id"] in ["AMGT_RESAPP-Z-S44", "AMGT_RESAPP-Z-S45"]
}
assert len(late) == 2
stamps = {
    str(n): json.loads((ROOT / PROJECT / "prd/stamps" / f"L10.r{n}.json").read_text())
    for n in [5, 6]
}
assert all(
    s["signed_by"] == SERIAL and "Late stamp" in s["note"] for s in stamps.values()
)
evidence_path = EVIDENCE[0].replace("_INTAKE_", "_LATE_")
(ROOT / evidence_path).write_text(
    json.dumps(
        {
            "utc": utc,
            "pin": pin,
            "rows": late,
            "backfill_stamps": stamps,
            "receipt_correction": "Exact root file 22013 read in this session before intake; exact 22017 read and archived; exact 22019 read and incorporated. Filesystem reads are not broker-client polling. The queued receipt is therefore not proof that every message is unread.",
        },
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)

world44 = "The missing L10.r5/r6 sidecars are independently confirmed by the recorded stamp listing. The slugs at bd523222a1 and CTO analyses establish that the handoffs occurred. CVO has now written both canonical stamps with explicit late/backfill notes; their current utc does not pretend to be the earlier slug vintage. This closes the owned recording omission, not a new gate or a change to either historical outcome."
world45 = "The reported artifact movement is corroborated by this session own round-7 files. The reported escalation veto worked, so no actual false STUCK delivery is established here. The final assertion that any queued inbox message is unread is false: CVO read exact 22013 before intake, read and archived exact 22017, and read exact 22019 while receipts remained QUEUED. A repository file read is not broker-client polling. The row itself properly leaves the earlier access route unmeasured, but its final universal unread claim outruns that limit."
new = []
for n, suffix, world in [(101, "S44", world44), (102, "S45", world45)]:
    original = late["AMGT_RESAPP-Z-" + suffix]
    row = {
        "id": f"AMGT_RESAPP-Z-C-S{n}",
        "project": "AMGT_RESAPP",
        "fabric": "site-z",
        "surfaced_by": SERIAL,
        "surfaced_at": utc,
        "one_line": suffix + ": " + world.split(". ")[0],
        "class": "OBSERVATION",
        "hazard_standing": original["hazard_standing"],
        "grounding": {
            "status": "GROUNDED",
            "evidence": EVIDENCE
            + [evidence_path, investigation + "@" + pin + "#" + original["id"]],
        },
        "disposition": "GRADUATED" if suffix == "S44" else "DISMISSED_WITH_REASON",
        "adjudicates": [original["id"]],
        "spec_asserts": original["spec_asserts"],
        "world_is": world,
    }
    if suffix == "S44":
        row["disarm_owner"] = SERIAL
        row["notes"] = (
            "Canonical L10.r5/r6 stamps restore the record; preserve their explicit backfill notes and historical artifact pins."
        )
    else:
        row["dismissal_reason"] = world
        row["notes"] = (
            "Keep the successful existing progress-probe veto. Do not infer failed delivery or unread content solely from QUEUED, and do not invent a new runtime helper or approval gate."
        )
    new.append(row)


def replace(path, header, records):
    path.write_text(
        header.rstrip()
        + "\n\n```json\n"
        + json.dumps(records, indent=2, ensure_ascii=True)
        + "\n```\n",
        encoding="utf-8",
    )


adj = CHANNEL / "adjudications/ADJUDICATION_v7.md"
text = adj.read_text()
rr = rows(adj)
assert not any(r["id"] in [x["id"] for x in new] for r in rr)
header = text.split("```json")[0]
header += "\nLate watermark: S44 and S45 landed after the initial intake. C-S101/C-S102 bring the final census to **94 originals, 29 newly dispositioned, zero pending**. S44 graduates and is REMEDIATED/DISARMED by two explicitly late canonical L10 stamps; S45 is dismissed with a correction distinguishing file reads from broker polling. The earlier 92/27 figures above remain labeled as the source intake, not the final count.\n"
replace(adj, header, rr + new)
rem = CHANNEL / "remediations/REMEDIATION_v7.md"
text = rem.read_text()
rr = rows(rem)
rr.append(
    {
        "id": "AMGT_RESAPP-Z-S44",
        "project": "AMGT_RESAPP",
        "fabric": "site-z",
        "class": "OBSERVATION",
        "hazard_standing": "ARMED",
        "mechanism": world44,
        "evidence": [evidence_path],
        "remedy": "Executed: write the two owned canonical L10 stamps with present utc and explicit historical/backfill notes. Preserve the actual slug and response pins.",
        "owner": SERIAL,
        "round": "v7",
        "remediation": {"state": "REMEDIATED", "owner": SERIAL, "round": "v7"},
        "closed": True,
        "disarm": {"state": "DISARMED", "owner": SERIAL, "at": utc},
    }
)
header = (
    text.split("```json")[0]
    .replace("all 92 original investigations", "all 94 original investigations")
    .replace("after the 27 decisions", "after the 29 decisions")
)
header = header.replace(
    "16 new remedy rows: 7 executed", "17 new remedy rows: 8 executed"
)
header += "\nLate S44/S45 are included before the commit: the owned L10 stamp omission is repaired with explicitly late round-5/6 stamps, and the queued-equals-unread assertion is corrected. Final original-item census: 94/94 disposed.\n"
replace(rem, header, rr)
for stage in ["L8", "L9", "L10"]:
    subprocess.run(
        [
            "python",
            ".tools/prd-stamp.py",
            "stamp",
            PROJECT + "/prd/AMGT_RESAPP_PRD.md",
            "--stage",
            stage,
            "--round",
            "7",
            "--note",
            "Final round-7 review includes late S44/S45: 94 originals, 29 new decisions, zero pending; 43 orders terminal, 41 VALID proofs. Three scoped judgment PASS, three FAIL; two mechanical FAIL. ADJUDICATION_v7 and REMEDIATION_v7 carry findings and limitations.",
        ],
        cwd=ROOT,
        check=True,
    )
print(
    json.dumps(
        {
            "pin": pin,
            "originals": 94,
            "late_ids": list(late),
            "adjudication_rows": len(rows(adj)),
            "remediation_rows": len(rr),
        }
    )
)
