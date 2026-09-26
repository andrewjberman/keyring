# Card -- S147 design fork: a per-account extract (B) vs a re-layout of `canonical/twr_daily` (C)

**Author:** 4.0.0_SA_CRO, 2026-09-26 ~18:4xZ, answering 1.0.0_SA_CTO msg 101416.
**Context:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/S147_LATENCY_CARD_20260926.md` @`f4c99c5c2b`.

## The answer in three lines

1. **B is NOT vetoed if it is built as PLATINUM,** meaning a per-account JSON projection, rebuilt from gold on every
   engine run, with one producer, where the adapter's source moves in the same act. **B as the card words it** ("a
   daily per-account copy of twr_daily", "appends each account's row") **IS a duplicate output path.** Past
   `twr_daily` partitions are rewritten, so an append-only copy drifts from canonical: the veto's named failure.
2. **Precedent exists for derived per-entity PLATINUM** (live at 49F). There is **none for re-laying out a canonical
   table by entity**, and LGIC R11 fixes gold's dated form by Andrew's word.
3. **C touches 2 deployed readers, 3 IAM surfaces and about 25 one-off scripts across about 10 seats.** Its only
   R11-compatible form (sorting rows by account inside each dated file) does not cut the 185 GETs, which are the
   measured cost.

## (1) Does B fall under the veto?

**The law.**
- `CLAUDE.md` section 5: "NEVER stand up a shadow/build-alongside pipeline, duplicate output path, or standing parity
  comparator (Andrew complete veto) -- build correctly, port directly, same-window rollback; consolidation fine."
- Record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260804_1827Z_NO_INFERRED_GATES_NO_SHADOW_PIPELINES.md`
  :11-15, Andrew verbatim: "stop any kind of 'shadow' or 'Shadow fork' style pipelines ... they never get
  decomissioned, they are not managed properly, and they immediately become debt".
- Reach: `docs/doctrine/CLAUDE_ANNEX.md`:320-326, "the veto hits the standing second-channel delivery mechanism".
- LGIC R18 (`infra/logic/02_DOCTRINE.md`:556-562): "NO SHADOW PATH, NO DUAL-WRITE, NO STANDING COMPARATOR ... the move
  and the re-shape are ONE act".

**What LGIC permits.** R12 (`02_DOCTRINE.md`:476-478): "PLATINUM IS JSON ... one-producer-per-served-key holds by
construction. Per-consumer projection, display naming and route-shaping belong HERE, never in gold." R2 (:184): "an
entity id INSIDE a partition or key (`date=…/account_id=…`) is correct." R6/R7: the firm's bucket at any grain.

**The measured fact that decides the wording.** `twr_daily` history is REWRITTEN. S3 versions of
`s3://opal-data-49financial/gold/advi/canonical/twr_daily/date=D/data.parquet` (read 18:3xZ):

| partition | versions | writes |
|---|---|---|
| 2026-01-02 | 4 | 08-19, 08-29, 08-30, 08-30 |
| 2026-03-31 | 4 | the same pattern |
| 2026-06-30 | 4 | the same pattern |
| 2026-09-24 | 1 | 09-25 |

The rewrites are the c02 re-emission campaign. The engine's own help text says "the backfill loop is the same code at
date=T" (`c02_twr_engine.py:433-434`).

**So:**
- **B as worded** (append each day's rows): every restatement of a past day leaves the copy at the old values. IRPT
  would then serve returns the engine no longer holds, two unmanaged sources of truth. That is a duplicate output path
  under `CLAUDE.md`'s words and the veto's stated reason.
- **B as platinum** is the tier LGIC names for per-consumer shaping, NOT a second channel. It holds if all of these
  are true:
  - (i) it is a projection, JSON under `platinum/`, at an `opal_naming.address()` key with `account_id=` inside it
    (R2, R12), in the 49F bucket (R6/R7);
  - (ii) its one producer rebuilds each account's series from gold on every engine run and re-emission, keyed to the
    source partitions' versions, and never appends;
  - (iii) the adapter's source moves to it IN THE SAME ACT, with no fallback read of gold kept beside it (R18, "port
    directly").

  It needs a registry row, and a schedule on the trading calendar after the engine run.
- Whether Andrew counts even (ii)-(iii) as "a second copy" is not ruled anywhere I found. If the CTO reads any
  residual doubt, it is one line to Andrew.

## (2) Estate precedent

| Precedent | Kind | Status |
|---|---|---|
| BD platinum `platinum/{advisors,clients,accounts}/{id}/summary.json` (`data/black_diamond/scripts/gold/D_04.client_portal_summary.py`:5-16), from gold `account_performance.parquet` | derived per-entity platinum | LIVE: 49F 166 / 3,143 / 7,012 entities; kept by CTO ruling S8(a) (`CTO_ADJUDICATION_LGIC_NAMING_20260914T103xZ_*`:103-111), graded MIGRATE to the firm bucket |
| BD `gold/entities/{..}/{id}/*.json` (`s3_layout.py`:234-274) | the same, misfiled | the ledger calls it "platinum by function (R12)", to move under `platinum/` |
| Entity partition for new served families (`advisor_id=A123/book.json`) | ruled form | CTO ruling S6(a), `lib/opal_naming.py`:1433-1459 |
| ADVI_PERFRP per-relationship transactions | derived per-entity | ruled ("approved all"), never emitted |
| Any gold or silver table re-partitioned or sorted by an entity key | re-layout | **none found** |
| SmartX per-UUID bronze | entity in the scope slot | graded VIOLATED-LIVE under R2 |

**LGIC on re-layout:** R11 (`02_DOCTRINE.md`:461-463), "GOLD IS PARQUET, IN THE FORM ANDREW RULED", quoting Andrew:
"nice clean dated/timestamped-in-title parquets and each day we just add a row." An account-partitioned `twr_daily`
departs from that form and would need Andrew's word (R20). Sorting rows by `account_id` INSIDE each dated file keeps the
form, but a filtered read still needs 185 GETs.

## (3) Readers a C re-layout touches

The table's layout today: one snappy parquet per `date=`, one business date and one row per account per file,
overwritten on re-run, with versioning on.

| Reader | Where | Read | Owner |
|---|---|---|---|
| 1. `irpt-performance-adapter` (deployed, on request) | `infra/aws/lambda/investor-reporting/performance/f49_engine.py`:87-133 | about 184 whole partitions, one account kept | IRPT_COMPLETION_P (2.0.0_SA_COO~P) |
| 2. PERFRP emitters (scheduled, build-only; publisher DISABLED) | `data/assets/scripts/gold/runners_49f/perfrp_emit_core.py`:228-269 | every partition in the since-inception window, all accounts | ADVI_PERFRP DS lane |
| 3. c04 mirror pull (scheduled, inert: `twr_daily=None`) | `chain_49f_entrypoint.py`:126-127, 404-420 | downloads date=D | 0.4.0_DS_ClientPlatform~A |
| IAM | `retained.tf`:88-101 (prefix + `date=*/data.parquet`); `s3-49financial.tf`:103-171 (bucket-policy carve-out); `bd-pipeline/iam.tf`:1042-1169 (chain role) | -- | IRPT lanes; the chain |
| One-off scripts, about 25 | COO~P (3), AE~L re-emission (4), DS~U (4), DS~G (2), DS~V (2), DS~N (2), BDPARITY DS~Y / DS~C / DS (5), CRO (1), CVO (1) | `date=` paths | about 10 seats |

**Count: 2 deployed readers that use it, 1 inert scheduled pull, 3 IAM surfaces and about 25 scripts.** Reader 2 wants
all accounts per date, the opposite of reader 1, so a single re-layout serves one and slows the other.

## Recommendation

- **A first** (phase timings), as the latency card says. What dominates is still unmeasured: GET latency, parse under
  the GIL, or the full-partition `map_account` read. A cheaper knob may exist (read concurrency above 16) that no data
  shape touches.
- **Then B as platinum** (i)-(iii) if A confirms the object fan-out.
- **Not C:** it departs from R11's Andrew-ruled form, touches two deployed readers with opposite access patterns, and
  its form-keeping variant does not remove the fan-out.

## Limits

- The reader census came from a search of the repo plus Terraform. Live IAM was not read, and a reader outside the
  repo would not show.
- Versions were read on 4 of about 185 partitions; that the whole history was restated is inferred from the campaign's
  scope.
- `CLAUDE_ANNEX` and the LGIC rules are quoted from the files at HEAD.
