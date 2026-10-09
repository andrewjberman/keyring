# /self-drive laptop directives -- ticks 47-49 (2026-10-09 ~08:5xZ-09:5xZ)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`
(30m cadence per the ~06:0xZ addendum). Cron `a5054ca6`. **state: ARMED**

## Measurements (09:57Z)

- Register: `live=15 projects=398 open_projects=64 open_tos=187`. Inbox: 0 unread.
- Cluster open calls: 4 of 4 boxes read, open=10, all `act` (fork 0), closed=55.
- **GitOps: healthy.** Integrate rc=0 at 09:51Z and 09:53Z. Laptop box pass rc=0 at 09:21Z, 09:23Z and 09:51Z, after the LGIC v8 move
  (@8897a19ad4). Behind CLOUD: laptop 11, sitez 14, dell1 0, dell2 0. Each box pushed within 5 minutes of the read.
- **GC.** C: 23 GB free. Laptop worktrees: main plus one temp apply tree, COO~C's TO-APPLY A18.
- **Graph.** Overlay live.

## Acts since tick 46

| item | act | commit |
|---|---|---|
| 107835/107836, the dual-written LGIC v8 channel docs | 3.0.0_SA_CVO moved its copies out; the laptop box pass resumed | 8897a19ad4 |
| 107849, the svc-irpt reader window for st28 | YES, TO-APPLY-23 form, X1 or 4 h | 3843761961 |
| 107845, six tool-fix rows | comp-secrets `--json --reveal` refused, by this seat (text `--reveal` kept for its six readers); deploy_ledger to 4.0.0_SA_CRO~A (landed 00d3393ff3); kill-maint to 4.0.0_SA_CRO~B; BD gold test and the comp-secrets test patch to 0.8.0_AE_CloudComp as ADHOC orders via 2.0.0_SA_COO~C | 9e4730450c |
| 107861, `_last_deploy_recorded` in lambda-source-map.json | folded into D1-S7: the recorder stops writing one global key | relay |
| sitez -b865 / XA-20261009T093754Z-26ac, the 08403355 gold build | (a) none | 7e6802dae0 |
| 107905, rule-24 record D1-S20 | `ddb_rows` ACCEPTED; schema enum and resolver skip | 72a2636203 |
| 107908, safe-commit admits an unknown author | WARN now, a refusal after a week once announced; built by 4.0.0_SA_CRO~A | relay |

## Completion test

NOT DONE: 64 open projects; ARMED.

## Acts only Andrew can do (10, all `act`)

- site Z `-9f24`: Barron's sign-in (his login).
- dell1 `-86a2`: mint a new anthropic-api-key in the Anthropic console (his login; the key leaked into a transcript).
- dell1 `-2caa`: walk the redesigned Security Analysis page on PROD (portal-v2.1.206), signed in as himself (DSGN_AMGTV1 FWD-1).
- dell1 `-f23d`: delete one stray S3 object (an S3 delete needs his confirmation).
- dell1 `-203a`: is Opal_Muni_Sleeve ($550,823) Opal's Muni SMA? (a business fact only he holds).
- dell2 `-62ea`: delete C:/dev/_scratch265 (21 MB; a recursive delete needs his confirmation).
- dell2 `-3082`: Research Team Meeting transcripts are refused (Graph 3003). Invite his account to that series, or have an M365 admin grant the gateway app a transcript access policy (his tenant act).
- dell2 `-20b4`: provide one real market-update deck (.pptx) from the SharePoint market-updates folder; the gateway returns a hint, not bytes, for an Office file.
- dell2 `-3cb1`: Alyssa's Analysis request on portal DEV. dell2 `-fbb1`: close test ticket TCK-20261009-a1052909.

## Compiler Tools

`directives-check.py`, `open-calls.py list --all --cloud`, `git rev-list`, the BOX-SYNC rows, `xadj.py rule`, `proof-of-spec-check.py`, `pytest`.
