# /self-drive D2 & D3 — tick 91 (2026-08-30 14:1xZ) — state: ARMED

Covers the acts since the tick-90 log (`e513c239e1`, ON origin — the 13:46Z CLOSE @`924d560a32`; origin now
@`5850d0f9ee` at the 14:01Z CLOSE, 87680). Cron `1c261f82` :07/:37 (the 14:07Z fire folded into this
stretch). Paired `/drive D2 & D3 @ 2.0.0_SA_COO` (its ticks 17–18).

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → 10 projects (1 complete). Open TOs **24** at the last register read (the
MAPVINTAGE close and the A07STAMP / c02-g-11 / ZEROCHECK / INDEXBYTES cuts not yet re-counted; the last two
are tooling TOs outside D2/D3). Ledger **19 / 0 unconsumed**. Acked READ since the tick-90 log: 87547, 87551,
87553, 87555, 87580, 87584, 87605, 87613, 87618, 87622, 87629, 87637, 87645, 87646, 87670, 87675, 87678,
87680, 87707, 87710, 87714, 87720, 87722, 87725, 87738, 87744, 87747, 87751.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 7** — R1–R5 unchanged; R6 = the C02-g-11 capability card (AE~L files R-1);
**R7 new**: Andrew's reserved delete of `json/mdpf/{firm}` (MDPF_PROVENANCE T-B, out of scope; the gate's
half given 87608 on PB-1's evidence at the right vintage). The census (DS~V 87744) read zero readers on the
deployed plane and the portal, and exactly one reader class on the repo plane — the CVO's three ad-hoc gate
harnesses, already 404 on 3 of 4 firms — across TWO buckets (8 objects, ~33 days dormant, the two 49financial
copies disagreeing by 11,361 B). Resolution (issuer 87751, gate 87757): the CVO re-points or retires its
three harnesses first (hash stated), the census re-reads zero, and MSTR carries ONE card as YES naming both
buckets; the IAM/publisher declarations a separate follow-on act.

## Verdicts since the tick-90 log (§3)

**0 on pitched calls.** Grades/rulings read: **CVO 87720: C02-g-9 E-1 + E-2 PASS** on the grader's own run of
the arm script (4 of 4; the flow_ledger mutation fails arm (ii)); **COO 87722: E-3 RE-CUT** to the laptop-side
shape (no host copy) — the gate's 87728 ruling; **COO 87725: `ADHC_DSFLOW.TO-INDEXBYTES-DEPLOY`** cut at AE~K in
the gate's shape, sequenced after ZEROCHECK-REFUSE; **CVO 87747:** A7-1..A7-3 read on the grader's own
head-object of the served a00/a07 (0 CR bytes, ETag == index blob); **COO 87629:** ZEROCHECK-REFUSE seated at
AE~K.

## Driver's own acts (tick 90 → 91)

1. **INF-ONEWRITER Step 2 — cut accepted (87575), then APPLIED accepted on the gate's own read** (87757):
   `09ffccc6ef` removed the billing token from CHAIN_PULL (20 → 19; the catalog row retained as the rollback
   affordance; DEF=1 estate-wide + both scheduler rules disabled); AE base held the S3 upload until the commit
   was on origin, took shape (a) after the annotation `6fc3f50b64`, uploaded once at 14:03:13Z; the gate's
   head-object: ETag `46dce6c7…` == md5 of `git show 5850d0f9ee:…dispatch.sh`, 113,320 B, 19 tokens in the
   blob. Ledger closed `ec49f41e58`. Condition (ii) — the first single-writer day READ by DS~V — stands.
2. **The (k) row** — case (a) accepted (87608): no reader enumerates row-field keys; `last_deployed_commit` =
   `6ab4c76a0f` measured against the deployed zip (5 of 5); written by hand with provenance (`901c6f2d9c`).
3. **The commit-gate fail-open** (AE base 87547: exit 0 on an in-set `.sh` with 0 of 1 checked): owner
   converged on the gate (COO withdrew AE~K; the CVO reproduced it and named the charter line); shape ratified
   (87608: REFUSE rc=2 on an in-set zero; `bash -n` on every `.sh` regardless; header truthful); **seated at
   AE~K** as `ADHC_COMMITGATE.TO-ZEROCHECK-REFUSE` (87629); the gate declined a register row and added the
   pre-fix baseline on both scratch subjects.
4. **The deploy gate uploads WORKTREE bytes** (MSTR caught a07 at 557 CRs before the 14:00Z push and normalised
   by hand): filed by the gate as OBSERVATION with owner = gate and the fix shape (87703: `git show :<path>`
   as the upload source; ETag == index md5 asserted; CR counts printed) → cut by the issuer as
   `ADHC_DSFLOW.TO-INDEXBYTES-DEPLOY` at AE~K, sequenced. **The gate normalised the 8 remaining CRLF worktree
   copies under `runners_49f/`** (8 of 83 tracked `.py`; each differed from its LF index blob by exactly its
   CR count; normalised only where `md5(CRLF→LF) == md5(index)` held; after: 8 of 8 equal, `git diff
   --numstat` 0 lines; no commit — nothing to commit).
5. **C02-g-9:** E-1 + E-2 accepted (87700: the seven-input halting set derived at source with its catch
   mechanism; arm (ii) manufacturing its evidence through a pure seam because the backfill destroyed the real
   gap — banked as a constraint on arm design; 539 of 539); **E-3's premise refuted** (no host copy has ever
   existed; the vehicle is laptop-side, path-loaded) → ruled NO host copy, E-3 re-cut to the loader-identity
   shape, already met (md5 == index blob `c7d48fed…`; FLOW_PREFIX absent from the loaded module).
6. **C02-g-10:** A7-1..A7-3 accepted (87731: the six removed lines are the six stamp lines; three tables
   2/2/0 movers with `content_hash` identical; an AST writer census reading exactly one over 30 modules;
   consumer census zero on repo + portal with controls); A7-4 = the read of the three served ETags the 14:01Z
   push landed (== the index blobs) + the ledger on that read; named fire Monday 12:45Z.
7. **The Monday a06 line accepted as registered** (DS~N 87710, from the READ 08-30 partition: header-only,
   0 rows from the parquet): two skips newest-first, chose 08-28, `map_carried=False`, five falsifiers, one
   named assumption; the same fire carries A7-4's acceptance.
8. **Two memories written:** a caret in a git ref is stripped by cmd.exe under `shell=True` (DS~N's
   instrument note — a pre/post comparison silently compared a commit to itself); a digest over `str()` of a
   set is random per process (tick 90).

## In motion, not mine

AE~L: E-5 (proof) then the C02-g-11 R-1 card; the CVO: re-point/retire the three `json/mdpf` harnesses (then
MSTR carries R7 once); DS~N: A7-4's read + ledger, A7-5; AE~K: ZEROCHECK-REFUSE then INDEXBYTES-DEPLOY;
DS~V: the first single-writer read (Monday); the CVO's grades; Andrew's word on R2, R6, R7; **Monday 12:45Z:
the fire that carries the a06 registered line AND A7-4's acceptance**; S1e at 04:35Z.

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`s3api head-object` on the dispatch key + `git show <origin>:<path> | md5sum` + a token count on the blob
(the Step 2 read); `git ls-files` + a python CR census with per-file index-blob md5 (the CRLF normalisation,
verified by `git diff --numstat`); `ls-remote` + `merge-base --is-ancestor`; the inbox listing by timestamp.
No comp-find, no comp-state.

state: ARMED · next log at a verdict or tick 97 (floor)
