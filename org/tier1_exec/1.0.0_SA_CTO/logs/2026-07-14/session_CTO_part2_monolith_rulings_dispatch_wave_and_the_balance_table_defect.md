# CTO session part 2 — the monolith rulings, the dispatch wave, and the balance-table defect

**archetype:** COORDINATE
**Serial:** 1.0.0_SA_CTO · **Date:** 2026-07-14 (~00:30Z–01:35Z) · continues `session_CTO_opal_assets_ownership_consolidation_prd_and_the_dispatch_hold.md`

## PRD evolution (all Andrew-direct, all verbatim in the PRD header/rulings)
- **v1.1** (`fe622224b`): Schwab bronze ruled as-landed (`opal-data-schwab/{master}/bronze/{type}/{YYYYMMDD}`,
  Andrew's grammar; 0833 migrated zipped 6,932/6,932 under his direct GO — CTO-verified on live S3);
  01_raw ruled disposable, retirement SEQUENCED behind two live consumers; SmartX full-API
  reconstruction designed (§4a) off the D4 endpoint sweep.
- **v1.2** (`300cc5dcb`): **THE MONOLITH** — one bucket, `{source}/{scope}/{layer}/…`, everything bronze+silver;
  opal-data-schwab re-classed STAGING; gold = DDB only to start; serving stays put.
- **v1.3** (`aef95f03a`): **COMPLETENESS LAW** (storage never Opal-filtered; the emitter is the ONE
  parse-down point) + **END-STATE HORIZON** (runners → monolith silver; gold trees in-monolith; only
  ADVI platinum partner buckets stay put). v1.3.1 (`34333469b`): container/content AE split (0.7.0 =
  container; 0.6.2/0.5.0 = content; DS = code).
- **v1.3.2/.3** (`6f60c06ff`, `5f530a074`): rulings 11a + 13/14/15 (below).

## Governance events
- **Andrew dispatch hold** folded same-turn (7 TOs staged, zero GOs); respawn wave came; **coordination
  delegated to COO** (Andrew-direct ~01:07Z) — CTO holds gates/architecture/acceptance only.
- **COO caught two structural saves:** (1) the stale XXX.md carve-out that would have armed /drive
  straight into the hold (deleted, `014de1937` — a /drive cycle is structurally unable to conclude
  "dispatch nothing"); (2) **C1 had NO TO file on disk** — the critical path blocked on an ABSENT
  artifact, which throws no error ("the TO board shows what EXISTS, never what is MISSING"). He
  authored C1 from the PRD verbatim (`83ae8ae0a`) + found C2/C5/C9 also missing files.
- **Dispatch wave complete:** all 4 workers roster-verified, GO'd, ACK'd, working. DS GO'd first
  (C6/C7-author/C10/C12; batch-GO read-back correct).

## Gate rulings (PRD §3, all from worker forks routed per the new model)
- **13a SSE:** monolith = SSE-S3/AES256 + DenyUnencryptedObjectUploads; NOT KMS (every producer role
  KMS-free; the KMS failure mode is AccessDenied from a policy that reads correctly — instrument-lies class).
- **13b:** denominators ENUMERATED AT RUN TIME, never read from documents ("7,256" was already stale at
  live 8,217 climbing to ~12,898 — an acceptance criterion that would have PASSED while stranding ~5,600).
- **13c:** 3-tier copy verify (multipart ETags are not MD5s; the naive loosen-the-check fix RETIRES the
  control; remap role keeps NO GetObject on the target).
- **14 sentinel DENY:** 0.7.0 measured that `opal-data-inf` already carries two live ADVI/CloudFront
  bucket-policy statements — a deny-only TF policy would REPLACE the singleton and 403 every Inflection
  gold read. Ruled: superset policy, dedicated module `inf-sentinel-deny/`, import-then-plan
  (modify-in-place only), exercised both directions post-apply. **Tripwire upgraded LastModified → ETag**
  (`fbcddcbf4d9370310e0e5dccbbaa3efd`/135B — content-addressed).
- **15:** bronze scope = the VENDOR'S DELIVERY scope (Pathfinder ships one file/both funds; per-fund
  scope materializes at silver); msn fallback tier homed before its incident day.

## The defect of the night (DS, held domain, reported-not-fixed)
Legacy Andrew-ratified `read_schwab_raw()` silently drops every RPS file's D2 section via
most-common-prefix selection — **and the full-header read re-characterized it: D2 is the per-account
BALANCE AND CASH table** (margin, settled cash, MV long/short, buying power; 3,932/61,786 rows = 6.4%),
not "account titles." Propagation UNVERIFIED (held verb), materiality UNSPECULATED. Ruling 11a: **T1
trailer reconciliation REQUIRED** (hard raise) on every monolith Schwab parser — implemented + exercised
same hour (`44a5328ce`, incl. mutating the guard itself). Held-lib patch/propagation scoping await
Andrew's word; the monolith path supersedes the lib regardless. DS's correction discipline (fixing the
characterization BEFORE it reached Andrew) is the banked lesson: a partial read changed the claim's
CHARACTER, not its size.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| `aws s3 ls --recursive` ×2 (operational verifies) | 0824: 324 obj, 11/11/11/13 recovery dates; 0833: 6,932 — both exact matches to producer denominators | Live-primitive validation before RAVC closes; never producer self-report |
| `Grep` (PRD header) | located stale §3 header for edit | native, free |
| comp-tools not otherwise run this stretch | rulings grounded on worker-supplied live evidence (measured EventBridge/S3/policy reads, each with denominators + controls) + prior §5 R1–R8 runs | the evidence base was already compiler-grounded at PRD authoring |

Open on the board: C1 plan → my gate (unblocked by 13a) · C3 IAM simulate after C1 · sentinel plan per
ruling 14 · C2 after COO's code-review pass (Andrew-ordered) · Andrew items: held-lib disposition (now
correctly characterized), G7a/G8, cohort 14→16.
