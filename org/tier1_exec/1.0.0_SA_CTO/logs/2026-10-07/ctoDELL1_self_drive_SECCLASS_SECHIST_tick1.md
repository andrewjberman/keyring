# /self-drive 60m MDPF_SECCLASS + MDPF_SECHIST -- tick 1 (1.0.0_SA_CTO~DELL1, dell1)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_0715Z_SELF_DRIVE_60M_MDPF_SECCLASS_MDPF_SECHIST_DELL1.md`
@78756a9b74. Cron `0290895f` runs at minute :23 of each hour, session-only. state: **ARMED**

## Scope (denominators)

| Project | status | dep_stage | TOs (non-terminal / total) | PRD | Seat |
|---|---|---|---|---|---|
| MDPF_SECCLASS | active | EXECUTING | 2 / 26: e20 pending (worker ~20, laptop round 7), e12 parked (0.7.0_AE_CloudOps) | v0.12 ADMITTED | 2.0.0_SA_COO~M1 (issuer); laptop ~M writes R8 |
| MDPF_SECHIST | active | PRD | 0 / 0 | v0.1 ADMITTED | 2.0.0_SA_COO~H1 |

- Device dell1. SEQUENCE v6 places both projects here; the `fabric: laptop` value is the two-value enum, per the control-plane brief section 3.
- Sequence: SECCLASS stage 2, no flags. SECHIST stage 1, NEEDS-SLOT. The reader does not map `~H1` to the project, although H1 is seated
  (a reader gap, not a slot gap).
- Inbox: 3 messages (1, 4, 6), all READ-acked. `active-commitments.py` returned 0 lines for this scope.

## Calls (3): 1 ruled, 2 already ruled upstream and recorded

1. dell1 committer identity is unset, so every seat commit fails with rc=128. RULED: each seat sets `GIT_COMMITTER_*` to its own serial
   for each commit. The box config stays with MSTR~DELL1.
2. M -> M1 boundary: laptop CTO ruling 106036 (relay msg 6). M1 issues round 8 from R8 once R8 is on origin.
3. SECHIST manual gate: MET @9b1121219b (laptop CTO); re-measured here.

Ledger: `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/ctoDELL1_SECCLASS_SECHIST/VERDICTS.jsonl`.

## Acts

- 78756a9b74: arming record and LIVE_ARMS rows.
- ea7b1706a9: pull-merge of origin/CLOUD e37552ef87, requested by MSTR~DELL1 msg 4.
- This commit: LIVE_ARMS reconcile. The laptop's AUTHORITY-UNVERIFIED self-drive row is folded into the DIRECTED DELL1 row, and this seat's
  unverified `/govern` sub-row is dropped for the laptop's two DIRECTED `/govern` rows.
- Who rules what (brief section 5) is open at Andrew. Meanwhile this driver rules in-scope calls under his self-drive word and copies
  `1.0.0_SA_CTO` on decisions only (Rule 31).

## Completion test

NOT DONE: 0 of 2 complete. REACHABLE 2, UNREACHABLE 0.

## Acts only Andrew can do

None.

## Compiler Tools

- `sequence-check.py --project` x3: worked. It surfaced the NEEDS-SLOT reader gap.
- `directives-check.py --json`: D8 is LAPTOP with 15 open TOs; both projects are members.
- `prd-signoff.py status` x2: both ADMITTED.
- `active-commitments.py`: 0 in-scope lines.
- Gap: `safe-commit` has no committer fallback on a fresh box, which surfaced as rc=128.
