# /self-drive laptop directives -- tick 62 (16:28Z), covering 16:00Z-16:30Z

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`,
re-armed per the last addendum of `ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`; cadence 30m (cron a5054ca6).

## Incident: client account data on CLOUD (0.0.0_AB_MSTR 108028, 16:00Z)
- dell2 worker `0.9.0_WK_IRPT_DASHBD~76` committed `W73_S2_EVIDENCE.json` (121 accounts) @1ba8eafcda; it reached CLOUD. dell2's CTO
  removed it and further files at HEAD (20e0b6408b, cb16f8b2f9, d2eb7316f2, ec17302888) and ruled containment
  (`CTO_RULING_CLIENT_ACCOUNT_DATA_IN_REPO_CONTAINMENT_20261009.md`). The laptop box-sync task was disabled by MSTR, then integration
  resumed (integrate 16:21:28Z and 16:26:59Z rc=0, held none). This seat did not open either file.
- Gate gap: `cg_sensitive_hits` (.tools/commit_gate_lib.sh:33) matches file NAMES only.
- ACT: `.tools/git-hooks/client-data-check.py` @8c1d8a1966 on dell2's ruling item 8 (MSTR 108040): refuses staged files whose id-shaped tokens
  hash into a list kept outside the repo; absent list = loud WARN. Laptop pre-commit limb 0 wired (backup kept). Builder of the hashed list
  routed to 1.0.0_SA_CTO~DELL2; other boxes' wiring via MSTR 108041.
- ACT ONLY ANDREW CAN DO: purge the files from git history (destructive git; CLAUDE.md Agent Autonomy). REC given: (a) purge now, while
  integration is paused.

## Cross-box rulings
- site Z -cf36 YES (HELD form: DEMQUE-ledger-confirmed booking ids only), -4d5a NO seat messages Alyssa; Andrew's one Teams message to the
  Opal Bloomberg account fires arm (b). @441f2f547d; routed to 1.0.0_SA_CTO~Z.
- dell2 -2f53 closed on dell2's list (cluster closed=60).

## GitOps
- Boxes behind CLOUD: laptop 14, sitez 174 (15 ahead, awaiting its pass), dell1 6, dell2 18. No holds since 15:18Z.

## Process GC
- C: 21 GB free.

## Acts only Andrew can do (14 distinct + the purge)
The 13 listed in REPORT_ACTIVE_PROJECTS_BY_BOX_20261009.md, plus: send one Teams message to the Opal Bloomberg account (NFRA_OPALAI arm b),
and the history purge decision.

## Completion test
NOT DONE -- laptop directives remain live.

state: ARMED

## Compiler Tools
git show --stat (metadata only), commit_gate_lib.sh read, client-data-check.py scratch-repo test, open-calls.py list --all --cloud, agentbus-sqs send.
