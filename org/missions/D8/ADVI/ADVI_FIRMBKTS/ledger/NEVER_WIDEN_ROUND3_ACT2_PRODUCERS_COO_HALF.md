# NEVER-WIDEN co-sign, ROUND 3 -- the COO half: window act 2, the MODE MOVE of the platinum producers (`BD_PLATINUM_MODE=canonical`)

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~08:5xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-9` phase B, on the
dormant build of phases A, A2 and A3 (merged `b0eebb018d`, `628d9f241b`, `19fb066b50`) | **Read against:**
`ledger/ROUND_ANALYSIS.round2.md` ADDENDA 2, 3, 4 and 5 (the CTO's), `deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json`,
`deliverables/2.0.0_SA_COO~B1/round3/checks/r3_reads.py` (the read census), rows `D1-S14`, `D1-W16-S7..S9`, `D1-W19-S1..S35`,
`D1-W20-S1..S5`, `data/black_diamond/scripts/gold/{gold_dispatch.sh,run_gold_layer.sh}` and `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh`
| **The other half:** `1.0.0_SA_CTO~DELL1`, `ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_CTO_HALF.md`. No act begins until both
halves are files at HEAD, the CTO half reads SIGNED, `FB-f-8` is `complete`, and the actor's change-management entry is open.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| object | what moves | how it is measured | rollback |
|---|---|---|---|
| `s3://opal-data-bd/code/gold/` -- 19 `.py` objects: the 14 writers (`C_05 C_06 C_07 C_08 D_00 D_00b D_00c D_00f D_01 D_02 D_03 D_04 E_01 E_24`) and `lib/{platinum_dest,platinum_dest_view,gold_utils,helpers,etf_classifier}.py` | the dormant build reaches the runner's code prefix (it ships by the push hook's `file_to_s3_target` at the next CLOUD push; this leg READS that it did and does not copy by hand unless the hook has not) | `git diff --name-only 96f3212d22 HEAD -- data/black_diamond/scripts/gold` (non-test: 19 files) hashed against each S3 object's bytes: 19 of 19 equal | the prior object versions (bucket versioning on `opal-data-bd`: read by the actor before the leg; recorded per key) |
| `s3://opal-data-bd/code/gold/gold_dispatch.sh` -- ONE object | gains one conditional export (below); nothing else in the file changes | the object's bytes equal the repository file's; the diff against the prior object is that block only; the deployed bytes read back (`aws s3 cp - \| cmp`) | re-upload the prior object version (recorded) -- the line removed, the same hour |
| the producers' runtime behavior | on a SCHEDULED PRODUCTION CHAIN run (`--chain`, not `--dry-run`, not the QA runner), every platinum write of the 11 served classes lands at `address()`'s key in `opal-data-49financial`, and every read, list and delete of a served-class key follows it (88 routed sites of 127 in the read census) | after the first such run: the new home's served keys carry `LastModified` after the move; the legacy home's 11 classes carry none after it (bounded listing per class) | the export removed and the script re-deployed; the next chain run writes the legacy home again; the new-home objects already written are inert |

**The export (the whole carrier, per ADDENDUM 4):** in `gold_dispatch.sh`, after argument parsing, one block that sets
`BD_PLATINUM_MODE=canonical` ONLY when `MODE = chain` AND `DRY_RUN = 0` AND `GOLD_KEEP_ALIVE` is not `1` AND `/tmp/GOLD_QA_REBUILD`
does not exist. `--single`, `--group`, `--from` and `--dry-run` runs, the QA runner (`GOLD_KEEP_ALIVE=1`, the rebuild marker),
and any run whose environment already sets the variable are untouched by the block (it never overrides a value already set).
`run_gold_layer.sh` delegates to `gold_dispatch.sh --chain full` and `ssm-run-gold.sh` is an operator wrapper over the same
script: the one block reaches both.

**Writers of the named property, counted (N writers = N rules read).** The property is the bucket a served key's write lands
in. LIVE: 1 rule decides it, `lib/platinum_dest.py destination()` (read at HEAD, with its sibling reads `source()` and `list_target()` resolving
through the same class table: the generated view of 11 classes), reached by 66 writer lines in 14 scripts (census 66 of 66; `r3_producers.py` D1: identity in `legacy` and equal to the
F7 placement in `canonical` for all 52,910 manifest keys). The carrier of the MODE: 1 (the export above; none of the nine
`BD_S3_BUCKET` files sets it, row of ADDENDUM 4). DECLARED after: the same 1 rule, the same 66 lines, plus 88 routed
read/list/delete sites. N printed: 1 rule, 1 carrier.

## What the act may NOT touch

`opal-data-bd` served keys of the 11 classes (nothing is deleted or rewritten there by the act; under `canonical` no code path
lists or deletes them), the router's registry and map value (act 4), any bronze, silver or gold-canonical key, the QA runner's
behavior, any other `code/gold/` object, the runner's launch files (`run-gold-layer.sh`, `setup-instance.sh`, the nine
`BD_S3_BUCKET` files), IAM, schedules, alarms. No delete of any kind, no copy of data (act 3 copies), no alert.

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** the 19 objects equal the build and `gold_dispatch.sh` equals the repository file with the diff
  being the one block; the actor's recorded prior versions exist for all 20; the next scheduled chain runs to its normal exit;
  every served-class write of that run is at the new home (listing: the 11 classes, newest `LastModified` after the move
  where the run writes the class that day; a class the day's run does not write reads "not written today" with its
  denominator); the legacy home's 11 classes are quiet (0 keys newer than the move); the producers' served reads came from
  the new home (the run log's read lines name no legacy prefix; the census's negative arm says 0 by construction). The
  expected destinations are read from the module's own rule, not predicted from the input's shape.
  **State of the world between act 2 and act 4, stated:** the router still serves the OLD home, so users read the last
  pre-move day until act 4; acts 2, 3 and 4 close in one window (round-2 analysis, section 2 item 1).
- **Branch B -- NOT SIGNED, the act stops and rolls back:** any object of the 19 differs from the build; the dispatch diff is
  more than the one block; a QA, `--single`, `--group` or `--dry-run` run reads `canonical` in its log; a served write
  appears at the legacy home after the move; a write lands in neither home; the chain exits non-zero on a mode-related
  error (a `ValueError` for a mode or a prefix spanning two classes, a `NoSuchKey` on a served read); a served-class read
  or delete names the legacy prefix. Rollback: the export removed and `gold_dispatch.sh` re-deployed from its recorded prior
  version, the same hour, the order stays open with a BLOCKING row.

## Authorization

The role is `bd-exporter-ec2-role` for the producers' runtime (reads the new bucket's prefix and writes it: its policy read by
the actor with `simulate-principal-policy` on the two bucket-prefix ARNs, `s3:PutObject` and `s3:GetObject` and
`s3:ListBucket` each `allowed` at `arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/*`, BEFORE the move; any
`implicitDeny` is a STOP and the grant is a separate act). The actor's own identity writes `code/gold/` on `opal-data-bd`: read
the same way. No grant, role or policy is created by this act.

## What this half does not know (stated)

- **E_24.** A manual rebuild tool, no schedule, no caller, 0 of 4,010 SendCommand events naming it in 45 days, one
  StartSession in the window (row `D1-S14`). Under `canonical` a hand run without the export writes its served key
  (`gold/artifacts/advisor_fee_efficiency.json`) at the legacy home, which no reader follows. This half proposes it retired
  from the census on that denominator; the CTO rules, and until he does the act does not move the mode.
- **E_01** writes keys outside every served prefix (3 of 3 objects, newest 2026-04-07): no served write at either home.
- **The schedule.** The producers rewrite the served keys daily in a window the analysis puts at about 06:15Z closing; the exact
  start of the next scheduled chain, and that no run straddles the move, is read by the actor from the runner's schedule
  immediately before the leg (`comp-schedule`), not assumed here.
- **Non-writer readers of a served key** (the router at act 4, other gold scripts outside the 14, QA diagnostics, the portal's
  API) are not inside this act's reads: the router follows at act 4; the others read the frozen legacy home until their own
  change. The read census covers the 14 writers and the 8 lib modules they import only; 3 call sites are EXEMPT with printed
  reasons (caller-supplied bucket on non-served keys).
- Display-only: log text beside routed calls names the pipeline bucket under `canonical` (row `D1-W20-S4`).
- The legacy-copy PUTs (D_01 and others) now land at the canonical home: nothing is left at the legacy home for them, by the
  CTO's ADDENDUM 5 (row `D1-W20-S1`).

## Provenance

`ROUND_ANALYSIS.round2.md` ADDENDA 2-5 and section 2 item 1; the census and the read census at the merged tree; the live
reads of 2026-10-11 (CloudTrail SendCommand read complete over 81 pages; destination versioning `Enabled`). Push state: LOCAL.
