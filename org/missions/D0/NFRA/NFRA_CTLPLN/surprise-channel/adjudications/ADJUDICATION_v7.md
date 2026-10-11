# NFRA_CTLPLN: CVO adjudication -- the four undispositioned gating rows (2026-10-11)

L8 compile by `3.0.0_SA_CVO~L` (laptop), on 1.0.0_SA_CTO msgs 108374, 108380 and 108382.

**Denominator.** The row gate's own resolvers (`.tools/surprise-row-gate.py` `_latest_dispositions`, `_gating_item_ids`) over the
index at HEAD 55fb1a8739: 259 items; 183 UNDER_INVESTIGATION, 54 DISMISSED_WITH_REASON, 22 GRADUATED. 55 items gate a slug
(BLOCKING or ARMED); 4 of them are undispositioned: W53-S1, W56-S1, D2-S2, D1-S8. The other 179 undispositioned items are
OBSERVATION/INERT; the gate notes them at the round's close and counts them against nothing (`_gating_item_ids` docstring).
They are not dispositioned here.

**Re-read at HEAD 49edd60d43 (2026-10-11 ~18:3xZ)** by a fresh `3.0.0_SA_CVO~L` session, after the drafting session died
uncommitted. Each `world_is` below re-ran or re-printed the same: AGENT-SUITE ok=True (127 passed, 9/9),
INBOUND-CLOUD-TEST ok=True 9/9, FABRIC-ENUM ok=True, `.tools/to-pipeline-gate.py:93` and `.tools/kill-maint.ps1:328-333`
unchanged, and c4e8c31098 an ancestor of HEAD.

**This version dismisses three of the four** (C-S13 to C-S15).

**D1-S8 is HELD to GRADUATE.** Its instance is disarmed: `s3://opal-data-mdpf/code/scripts/gold/mdpf_gold_consolidator.py` reads
sha256 2cd88dc41ce6a0bb..., the pinned build (read by this seat 2026-10-11 ~18:1xZ; row D1-S9). The gap it names is still in the
code: `.tools/git-hooks/pre-push-safe-deploy.sh:56-57,82,104` bounds the deploy set by the box's diff against origin/CLOUD, so a
pinned file that reaches CLOUD by integrate before its box push is never deployed by a push. The remedy needs a remediation row,
and the row gate refuses one while an NFRA_CTLPLN order reads non-terminal: `NFRA_CTLPLN.TO-CT-x-1` (round 6, issued to
`0.7.0_AE_CloudOps~CT1`) reads pending at HEAD. The graduation lands when that order is terminal. The order lives at
`org/tier2_senior/0.7.0_AE_CloudOps~CT1/task_orders/`, as does its sibling TO-CT-x-2 (also pending). Its worker committed
the exercise at 2008d30670 (2026-10-09). Only the issuer's close, by `2.0.0_SA_COO~C`, makes both terminal.

<sweep_watermark>2026-10-11T18:20Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S13",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-11T18:20Z",
    "one_line": "W56-S1 overtaken: CT-i-14's amendment 1 wrapped the fake drafting replies, the order is complete, and the agent suite reads ok=True at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CTi14-AC2: the agent's seven pytest files and the mail-reply script pass (127 and 9/9) after the drafting contract lands.",
    "world_is": "Run by this seat at HEAD 55fb1a8739: check_agent_suites.py prints 'pytest 127 passed', 'INBOUND-MAIL-REPLY-TEST ok=True cases=9/9', 'AGENT-SUITE ok=True pytest_rc=0 mail_reply_rc=0'. The sibling the row also named, test_inbound_cloud.py, prints 'INBOUND-CLOUD-TEST ok=True cases=9/9'. The order reads <status>complete; its amendment 52713e9dbb wrapped the two test files' fake replies, and the issuer's drain bde0c0fc90 re-ran AC1-AC3 PASS.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/checks/check_agent_suites.py at HEAD 55fb1a8739: AGENT-SUITE ok=True",
        "python data/transcripts/scripts/tests/test_inbound_cloud.py at HEAD 55fb1a8739: INBOUND-CLOUD-TEST ok=True cases=9/9",
        "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-i-14.draft-contract-post-and-to-andrew.md <status>complete",
        "git log: 52713e9dbb (amendment 1), bde0c0fc90 (drain, AC1-AC3 PASS)"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W56-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The disarm owner's amendment landed, the order is complete, and the criterion's own check passes at HEAD. No remedy is owed."
  },
  {
    "id": "NFRA_CTLPLN-C-S14",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-11T18:20Z",
    "one_line": "D2-S2 fixed in code: kill-maint.ps1 now disables the ORPHANED class when liveness parses to zero live owners while sessions are up (c4e8c31098, in HEAD).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "kill-maint.ps1 header and line 311: an owner verdict that cannot be read disables the ORPHANED class for that run; a live seat's poller is kept.",
    "world_is": ".tools/kill-maint.ps1:328-333 at HEAD 55fb1a8739: 'if ($null -ne $liveSerials -and $liveSerials.Count -eq 0 -and @($sessions).Count -gt 0)' prints a WARN and sets $liveSerials = $null, so line 535 classes no poller ORPHANED. c4e8c31098 (0.0.0_AB_MSTR~DELL1) is an ancestor of HEAD. Limit: the commit adds 6 lines to the script and no test; the disarm owner's text asked for a test feeding an empty map beside a non-empty process list. This seat did not execute the script (it kills processes); the grade is a read of the branch.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/kill-maint.ps1:328-333 read at HEAD 55fb1a8739",
        "git merge-base --is-ancestor c4e8c31098 HEAD: true; git show --stat c4e8c31098: .tools/kill-maint.ps1 | 6 ++++++"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-D2-S2"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The fail-open branch is closed in code at HEAD. The missing regression test is noted for the script's owner. It does not re-arm the hazard."
  },
  {
    "id": "NFRA_CTLPLN-C-S15",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-11T18:20Z",
    "one_line": "W53-S1 dismissed: the gate's FABRIC_ENUM literal equals the register today, and a register box the index does not know is refused loudly (ROW-ENUM). It is never accepted silently.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-t-3 BUILD 2: the gate obtains the box list from the register; the census lists none of the worker's files.",
    "world_is": "At HEAD 55fb1a8739, .tools/to-pipeline-gate.py:93 holds FABRIC_ENUM = ('laptop', 'site-z', 'dell1', 'dell2') and lib/devices.py placement_values() returns the same four. python .tools/tests/test_fabric_enum_dell.py prints 'FABRIC-ENUM admitted=5/5 refused=1/1 tree_selftest=ok gate_selftest=ok ok=True'. The residual case is a fifth box added to org/devices/DEVICES.json: the gate admits it and missions-tree-index refuses a project row naming it with ROW-ENUM. That is a refusal at commit time, so the box's first project would surface it, and nothing is accepted silently. A one-line literal edit closes it when a box is added.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/to-pipeline-gate.py:93 read at HEAD 55fb1a8739",
        "python -c 'import devices; devices.placement_values()' (lib/): ('laptop', 'site-z', 'dell1', 'dell2')",
        "python .tools/tests/test_fabric_enum_dell.py at HEAD 55fb1a8739: ok=True"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W53-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No drift today. The only reachable failure is a loud commit-time refusal when a fifth box is registered, and it is closed by a one-line edit then. Building the register read now would be ahead of need."
  }
]
```
