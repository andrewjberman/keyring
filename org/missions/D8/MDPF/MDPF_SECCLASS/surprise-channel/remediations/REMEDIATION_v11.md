# MDPF_SECCLASS -- round 20 remediations (dell1)

<sweep_watermark>2026-10-11T04:22Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T04:22:00Z. Graduated at ADJUDICATION_v16: 3 rows, all INERT; plus D1-S30, graduated INERT at ADJUDICATION_v18 on the un-park (2026-10-12). D1-S28 is a round-21 build
candidate. D1-W77-S1 and D1-W78-S1 are measure-first reads. D1-S26 and D1-S27 stay OPEN in REMEDIATION_v10 (an id is one row); their round-20 progress is recorded in ADJUDICATION_v18 D1-C-S5: (D1-S26: code fixed, served pending the ship
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
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v20"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
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
      "state": "CLOSED_UNREMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v20",
      "closure": {
        "reason": "ACCEPTED_BY_RULING",
        "pointer": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_20_20261012.md:30"
      }
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
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
    "id": "MDPF_SECCLASS-D1-S30",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C_06.client_mix_timeseries is incremental: it builds only new dates, and reclassify_retained revisits only retained holdings whose asset_class is OUTSIDE the served set, which includes 'unclassified'. So SC-e-87's fix (shipped by TO-SC-e87b) reaches D_04's served mix_summary only on a date C_06 builds new. At the same as_of 2026-10-09, D_04 Unclassified is $1,846,332.73 before and after the ship, while D_03's firm_composition unclassified moved 92 / $3,325,002.64 -> 66 / $2,760,199.32. Monday's fire still answers Friday 10-09 (T-1), so the first new date C_06 builds is read on Tuesday 2026-10-13's fire.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S30 (2.0.0_SA_COO~M1, @cf1dbb8d31)",
      "3.0.0_SA_CVO read s3://opal-data-bd/platinum/firm/mix_summary.json versions 2026-10-12T08:5xZ: 2026-10-11T05:45:16Z (pre-ship) data_as_of 2026-10-09 mix.Unclassified market_value 1846332.7278; 2026-10-12T02:01:03Z and 2026-10-12T05:44:00Z (post-ship) the same data_as_of and the same 1846332.7278",
      "C_06.client_mix_timeseries.py :274-311 (SERVED_HOLDING_CLASSES and reclassify_retained), cited by the row at box/dell1 HEAD"
    ],
    "remedy": "Either let reclassify_retained revisit a retained date's 'unclassified' holdings, or run one bounded backfill of C_06 over the retained dates under its own pair. Close when: a post-fix D_04 mix_summary at a data_as_of C_06 built after the ship reads Unclassified near the ~$6,335.94 leg G expects (not $1,846,332.73), beside D_03's unclassified at the same as_of.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v20",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v20"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  }
]
```
