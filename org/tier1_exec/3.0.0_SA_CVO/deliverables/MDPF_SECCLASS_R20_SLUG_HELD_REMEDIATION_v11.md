# HELD SLUG (not yet in the channel) -- MDPF_SECCLASS round 20 remediations

HELD by 3.0.0_SA_CVO: surprise-row-gate refuses a new remediation row while TO-SC-e87b is `pending` (LD-0521). On TO-SC-e87b terminal,
the holder moves this file to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/remediations/REMEDIATION_v11.md` (this header removed)
and sends the slug to 1.0.0_SA_CTO~DELL1.

<sweep_watermark>2026-10-11T04:22Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T04:22:00Z. Graduated at ADJUDICATION_v16: 3 rows, all INERT. D1-S28 is a round-21 build
candidate. D1-W77-S1 and D1-W78-S1 are measure-first reads. D1-S26 and D1-S27 are carried from REMEDIATION_v10 with their round-20 progress (D1-S26: code fixed, served pending the ship
and a BD fire; D1-S27: explained, the acceptability ruling is the owner's). Both stay OPEN.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-S28",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "crossbox-deploy-check.py's OPEN-DEPLOY limb reads each worktree's HEAD sentinels, so a ledger entry CLOSED at trunk (sentinel deleted) is still counted HELD in any worktree that has not taken the closing commit, and a registered worktree whose directory is gone reads 'ls-tree rc=128 (not readable, not clear)'. A one-family ship with no real contention therefore reads STOP. Confirmed on this seat's own NEVER-2 census (24 worktrees, `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`): none of the three slugs has a sentinel at box/dell1 HEAD 1977885433 or origin/CLOUD (positive control: 18 sentinels at HEAD), and each has a change-management entry reading CLOSED (cot-cash-admission-m 2026-10-08T06:51Z, secclass-e60 2026-10-11T02:43Z, secclass-e84 2026-10-11T02:42Z). They survive only in lagging worktree HEADs: cot-cash-admission-m in C:/dev/cvo_secclass_r9 (this seat's own superseded worktree), wk-secclass-42 and wk-secclass-44; the two secclass slugs in C:/tmp/mm4-ac1 and seven smcont_* temp trees. Limb (e) also holds: C:/dev/wk-secclass-r9-38 is registered with its directory gone. One read of C:/dev/wk-canon-9 returned rc=128 and re-read clean (rc=0) a minute later, so unreadability can also be transient. No real contention exists; the switch is WARN, so SC-e-87b is not blocked. A round-21 build item, owner 1.0.0_SA_CTO~DELL1.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S28 (2.0.0_SA_COO~M1)",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/E89_REAL_RUN_20261011.txt (38 worktrees, 665 sentinel reads, 4 hits)",
      "ADJUDICATION_v16 (this seat's own 24-worktree census at 04:2xZ)"
    ],
    "remedy": "One build cell (round 21): read each sentinel's status from the trunk (the box branch HEAD) first, and count a slug present only in a lagging worktree as stale when trunk has deleted it. Classify a registered-but-missing directory as vanished, and re-read once before calling a readable directory 'not readable'. Close when: a real run of the BD three-file check on a box with lagging worktrees reads OPEN-DEPLOY clear, and a planted open sentinel at trunk still reads a hit (negative control).",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v20",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v20"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W77-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The lib treats a literal ticker string NAN or NONE as blank, so such a position takes the blank-ticker identity chain (CUSIP, exact name, the name's one CUSIP) before the NAME:: row, not SC-e-87's ticker-no-row branch. Out of SC-e-87's grant (the lib is not in its <paths>) and not measured: whether any served BD position carries the literal ticker NAN or NONE. Measure first; the class is the same on the probe, but the hop and the CUSIP-chain resolution differ when a CUSIP is passed (D_03, D_04).",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W77-S1 (worker ~77)",
      "C_06.client_mix_timeseries.py:615 normalizes NAN/NONE to blank on one path"
    ],
    "remedy": "Measure first: count served BD positions (and dollars) whose ticker is the literal NAN or NONE at the latest partition. If zero, close as not exposed. If non-zero, the lib's owner rules whether those positions should take the ticker-no-row branch. Close when: the count is printed with its denominator, and either it is zero or the ruling has landed.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v20",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v20"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W78-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served firm snapshot rows for 2026-10-06 and 2026-10-07 in gold/views/mix_daily_summary.json were written at 2026-10-10T05:26Z, but their canonical holdings partitions were rewritten at 2026-10-10T23:15Z. A recompute now differs from the served totals by +$584,886.01 and +$442,485.38. Confirmed on this seat's independent S3 read: the served 2026-10-06 and 2026-10-07 firm rows do not match a recompute from the current partitions, which were rewritten 2026-10-10T23:15Z, after the 05:26Z snapshot. That makes the served snapshot older than its inputs by about $585k and $442k on $2.0B. The writer of the rewrite is not traced. INERT, and a separate question from the D1-S27 gap.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W78-S1 (worker ~78)",
      "ADJUDICATION_v16 D1-C-S2 (served 2026-10-06 gap -4.71 vs recomputed 167.10; 2026-10-07 128.06 vs -120.97; 2026-10-08 reproduces to the cent)"
    ],
    "remedy": "Count the writers of the 2026-10-06/07 holdings partitions and name the one that rewrote them at 2026-10-10T23:15Z. Then state whether the next scheduled C_06 fire re-serves those dates. Close when: the writer is named, and the served rows equal a recompute of the current partitions (or the rewrite is ruled a correction the served snapshot should not follow).",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v20",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v20"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S26",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "SC-e-79 changed the shared lib (classify_with_identity resolves a ticker-no-row position by its NAME:: row), but BD's three served classify sites (D_04 :160-167, C_06 :228-233, D_03 :135-140) call it only for a BLANK ticker. The branch is unreachable on the served path, so the 23 ticker-no-row securities ($966,285) still serve unclassified. The cell's AC1 graded the function, not the caller. PROGRESS v20: v20: CODE FIXED, NOT SERVED. SC-e-87 (@f4f01cfb27) adds the non-blank ticker-no-row branch at D_04 :170-176, C_06 :235-238 and D_03 :141-144. This seat's own runs: SERVED-REACH ok=True at all three sites (controls 3/3); the live-table reach moves 23 of 23, $966,285.46 (equity 20, fixed_income 3), 0 stay; BD gold 120 passed. The ship (TO-SC-e87b) is pair-gated at 0.7.0_AE_CloudOps~SC1 (COO half @c6202193c5, CTO half @20526c6cc7). Close condition unchanged: a scheduled BD fire after the ship serves the 23 by their NAME:: rows. Read leg G against about $6,335.94 left Unclassified (round 19's served $972,621.40 less $966,285.46), not against zero.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S26 @2ae7d56414",
      "ADJUDICATION_v15 D1-C-S1: call sites read at box/dell1 HEAD 1974b85f4e; served BD firm Unclassified 972,621.40 at data_as_of 2026-10-08 (VersionId 5Ws3Q6veR.qd3bueY48qALseVpW10kRl)",
      "ADJUDICATION_v16 D1-C-S2 (this seat's own re-runs, round 20)"
    ],
    "remedy": "One build cell: the three BD classify sites route a non-blank ticker that classify() misses to classify_with_identity(ticker, name, cusip). Its acceptance must exercise D_04's SERVED classify path with a ticker-no-row position, not the lib function. Close when: a scheduled BD fire after the ship serves the 23 by their NAME:: rows and firm Unclassified falls by about $966K",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v20",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v20"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S27",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C_06's firm-daily snapshot total differs from the sum of its published class values by -4.71 / +128.06 / -128.57 on 2026-10-06 / 07 / 08 (about 6e-8 of $2.0B). D_04's Unclassified line is total minus the six classes by design, so it carries that gap. PROGRESS v20: v20: EXPLAINED. SC-e-88 shows the gap is 6-decimal share rounding: C_06 rounds each relationship's class shares to 6 decimals (:595) and accumulates rounded share times dollars (:737-743). On 2026-10-08 the recompute matches the served total to the cent ($2,014,814,865.45, gap -128.57), and every top residual sits at exactly 1e-6 of its relationship's value. The other two dates do not reproduce (D1-W78-S1). The close condition's second limb, 'explained and ruled acceptable', now needs only the owner's acceptability ruling: about 6e-8 of $2.0B, carried into D_04's Unclassified line by design.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S27 @4ee11df53c",
      "ADJUDICATION_v16 D1-C-S2 (this seat's own re-runs, round 20)"
    ],
    "remedy": "Owner to route to C_06's lane: trace whether a position of about $128 counts in total on one day and in a class on the next. Close when: total equals the class sum on three consecutive firm-daily snapshots, or the gap is explained and ruled acceptable",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v20",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v20"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
