# The holdings producer to PRD v0.20, the Inflection slice, and FWD-13's comparison points — 0.4.0_DS_ClientPlatform~E

**archetype:** IMPLEMENT

**Date:** 2026-09-29, 05:00–08:00Z
**Task Order:** `IRPT_BCKEND.TO-IB-er-301` (complete) then `IRPT_BCKEND.TO-IB-er-302`, issued by `2.0.0_SA_COO~P` as one queue
**Status:** er-301 COMPLETE — E3-AC4 PASS, E3-AC1 PASS, E3-AC2 PASS. er-302 in flight.

## Objective

Round 3 of workstream ~E. Amendment 1 put a STEP 0 in front of the round: fix
`holdings_performance.py` under PRD ADDENDUM v0.20 rulings 13–17 and re-emit all 557 49F
holdings-gold partitions, because `4.0.0_SA_CRO` refused the never-widen half on the adapter
switch (row `IRPT_BCKEND-S195`) after measuring 2,846 served OK rows at |r| >= 1. Then add
Inflection as a second declared channel over its full history, then FWD-13's comparison points
for 49F.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| naming-gate.py | inside `safe-commit.sh`, round-3 diff | **REFUSE 4 graded**, then PASS 1 graded | The refusal was correct and changed the design — see Decisions. |
| comp-pipescript io | `... holdings_performance.py --pipeline all` | OUT-OF-GRAPH; AST derivation, 4 I/O sites, 3 UNRESOLVED | Chain membership and portal consumers DECLARED ABSENT, not measured. |
| comp-estate --resource | `comp-estate --resource holdings_performance` | `SUBJECT_ABSENT_FROM_CORPUS`, 135 of 135 chains scanned | The basis for "the re-emit moves no served output". |
| comp-pipescript deployed | `comp-pipescript deployed` | `NOT-DECIDABLE` rc=4, `PARTIAL_OR_BLIND` | Budget reached with 1 of 1 `s3_head_object` DEFERRED. NOT read as a pass. |
| comp-read | `comp-read .tools/naming-gate.py --for "permitted contexts..."` | THE CONTEXT RULE, lines 21–26 | Named the four permitted contexts; prose and `*/tests/*` ungraded. |
| commit-gate.sh | on both `.py` files | clean | py_compile + ds-precommit + ruff py39. |
| proof-of-spec-check.py | on the er-301 instance | INVALID x2, then **VALID rc=0** | The schema wanted `denominator`/`status` per criterion and `controls.determinism`. |

**What worked:** `comp-read --for` on a 1,576-line gate answered "what contexts are permitted" in
64 ms and pointed at the exact header lines. `comp-estate --resource` gave a scanned denominator
(135 of 135) rather than a bare absence, which is what made "nothing reads this yet" quotable.

**What failed:** `comp-pipescript deployed` returned a PREFIX with its remote operation deferred —
a prefix carries no verdict, and it does not gate this round either way because the producer has
no S3 code prefix. `comp-pipescript io --pipeline` rejects `assets` as a pipeline token; the
accepted set is bd/inf/cot/mdpf-shaped, so an assets-tree gold script has no pipeline to name.

**Gap found:** no comp-tool answers "does any landed silver carry a mapping from vendor account X
to custodian account Y". Finding `dim_account_xref` took a prefix listing by hand after
`accountNumber` turned out to be masked.

## Work Completed

### 1. `holdings_performance.py` to PRD v0.20 (rulings 13–17)

- **Ruling 13** — the key is `(account, identifier)`, the first non-empty of the declared
  identifier columns. An UNIDENTIFIED row takes a per-row token, and `_unident` is carried in BOTH
  the grouping and the day-t price join, so an identifier-less row can never be priced by an
  identifier and two of them at different prices stay two positions.
- **Ruling 14** — an identifier-less row priced 1.00 with quantity == value is cash; every other
  one is excluded with its count and weight on the row.
- **Ruling 15** — the basket is the LONG holdings: `in_basket = member & (value >= 0)`, the
  denominator is that plus POSITIVE cash, and `negative_value` / `negative_count` / `leveraged`
  carry what sits outside it. `cash_value` stays SIGNED.
- **Ruling 16** — a fifth status, `IMPLAUSIBLE-RETURN`, graded on the computed answer with a NULL
  `daily_return` and its reason in the manifest.
- **Ruling 17** — the manifest population moved from `included + excluded > 0` to a new
  `held_count`, so a short-only account is no longer dropped from the completeness denominator.
- Plus `PartitionCache`, a bounded thread-safe LRU: every day reads its own positions partition
  and its prior day's, so a full-history run fetched each partition about 1.4 times instead of 2
  (49F 226 hits / 1,445 misses; INF 634 / 2,590).

### 2. The Inflection channel, as a declaration entry

`sources.json` 1.0 → 1.1. New fields, each carrying a measured basis and its denominator:
`identifier_columns` (ordered), `quantity_column`, `account_id_zero_pad`, `cash_flag_column`,
`monolith`. INF declares `balance_prefix: null` — custodial cash IS a position — and pad 0,
because the Orion `accountId` is a 3-to-5 character integer key and padding would invent digits.

### 3. The two runs

| Channel | Days | Rows (footer read-back) | Missing | Empty |
|---|---|---|---|---|
| 49F re-emit 2024-07-09..2026-09-25 | 557 of 557 | 3,188,339 | 0 | 0 |
| INF mint 2020-04-27..2026-09-25 | 1,609 of 1,609 computable | 1,420,782 | 0 | 0 |

The 4 INF trading days not emitted are the 4 the criterion excludes: 2026-07-01 and 2026-08-06
have no silver partition, so 2026-07-02 and 2026-08-07 have no prior-day base.

### 4. Acceptance and the planted mutants

`E3-AC4 PASS` (OK rows |r| >= 1: **2,846 → 0**; |r| > 0.5: **4,061 → 4**; `leveraged` on all 557
days; 557 of 557 manifests complete). `E3-AC1 PASS` (960/960, missing 0, dup 0). `E3-AC2 PASS`
(missing gold 0). Two mutants, each written through the producer's own parquet path and each
restored by re-running the producer: M1 set one OK row to 1.5 → AC4 FAIL naming 1, then PASS at 0;
M2 dropped one INF account → AC1 FAIL naming 1 missing, then PASS at 0.

### 5. er-302 — `holdings_comparison.py` (in flight)

One row per landed Black Diamond `reporting_performance` file, both bases stated, five named
not-comparable reasons. 15 new tests (39 in the suite). Full run over 5,318 files in progress.

## Decisions Made

1. **The naming limb refused the first INF declaration, and the refusal was right.** An authored
   JSON carrying the registered token `inflection` is a hand-kept carrier under LGIC_ENFORCE DEC-6
   (3 REFUSE lines at `sources.json:41,:43,:46`). The entry is now keyed `orion`, declares
   `monolith: orion`, and its `positions_prefix` is the template
   `{monolith}/{scope}/silver/fact_positions/`; `firm_scope()` resolves a monolith to its UNIQUE
   registry scope and REFUSES on any other count. Measured: orion 1, eclipse 1, blackdiamond 2 —
   so the first Cottonwood channel declared this way stops loudly and needs a `registry_key`.
2. **A NUL-prefixed sentinel is not a safe impossible-prefix.** The first cut keyed UNIDENTIFIED
   rows by `"\x00UNIDENTIFIED#<row>"`; pandas grouped two distinct sentinels as ONE, because
   grouping object-dtype strings goes through a C string table that stops at the first NUL. The
   key is now a bare position token with `_unident` in the grouping and the join, which assumes
   nothing about what an identifier cannot contain.
3. **Two existing tests changed and both changes ARE the ruling** — the status vocabulary count
   went 4 → 5, and the `NON-POSITIVE-BASE` fixture moved from a cash debit to a short-only book,
   because under ruling 15 a debit no longer reaches that member. No 49F METHOD test was altered.
4. **er-302 maps accounts through `dim_account_xref`, not through `accountNumber`.** See Blockers.
5. **er-302's period rule is LONGEST-FULLY-COVERED**, stated in the declaration with its
   denominators, because each file offers 4–6 periods and the row compares one.

## Files Modified

| File | Commit |
|---|---|
| `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` | `f302ab14cd` |
| `data/assets/scripts/gold/irpt_holdings_performance/sources.json` | `f302ab14cd` |
| `data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_performance.py` | `f302ab14cd` |
| `.../deliverables/0.4.0_DS_ClientPlatform~E/...TO-IB-er-301...proof_of_spec.json` | `eee6a7a721` |
| `.../task-orders/IRPT_BCKEND.TO-IB-er-301...md` (status → complete) | `eee6a7a721` |
| `data/assets/scripts/gold/irpt_holdings_performance/holdings_comparison.py` | pending |
| `data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_comparison.py` | pending |

**Workspace CLOUD commit:** merged as `d008d05b21` (`safe-merge.sh ds-e-irpt-r3-holdings`). Push
state: LOCAL — `git ls-remote origin CLOUD` read `15655f4a25` at 07:23Z; `CLOUD` is pushed by
`0.0.0_AB_MSTR` only.

## Blockers

**None.** One item was routed rather than blocked: TO-IB-er-302 says to map a Black Diamond
account to the gold's 10-digit `account_id` **by its `accountNumber`**, and that cannot be done as
written. The bronze `accountNumber` is MASKED to its last four characters (`XXXX5115`) in 40 of 40
sampled files, and last-four is ambiguous — 7,540 gold account ids hold only 5,279 distinct
last-four values, 1,801 of them shared by more than one account, 4,062 accounts in an ambiguous
bucket, and 23 of 40 sampled vendor accounts land in one. Rather than weaken the criterion, the
map goes through the landed `blackdiamond/<firm_short>/silver/dim_account_xref`, which keys on
`bd_account_id` — exactly the bronze's `accounts[].externalId` — and resolves to a padded
10-character custodian id. Latest partition 2026-09-28: 6,202 rows, 5,376 resolved, 826
`unresolved`; 60 of 60 sampled externalIds present. An `unresolved` row becomes a NAMED
not-comparable reason, never a guess.

## Current State

The 49F holdings gold is re-emitted end to end under v0.20 and no longer serves an implausible
day; the Inflection slice exists for every computable trading day back to 2020-04-27. Nothing
reads either prefix yet — `comp-estate` places the subject in 0 of 135 estate chains and the
adapter switch has not landed — so neither run moved served output. `2.0.0_SA_COO~P` has the
er-301 report and the E3-AC4 PASS its adapter re-cut was waiting on.

## Next Steps

1. **[`0.4.0_DS_ClientPlatform~E`]** Finish er-302: land the comparison partitions, run E3-AC3,
   plant its mutant, write the proof, close ledger `irpt-holdings-comparison-49f-e-20260929`.
2. **[`2.0.0_SA_COO~P`]** The adapter switch re-cut. Its precondition — 557 of 557 manifests
   complete with no served implausible day — now reads true. One thing to carry into the
   never-widen half: a manifest is the producer's SELF-REPORT. Mutant M2 dropped a row straight
   out of a landed parquet and `complete` still read true; the row-level limb is what caught it.
3. **[`2.0.0_SA_COO~P` / `1.0.0_SA_CTO`]** Cottonwood is next under ruling 11, and its channel
   cannot be declared by monolith — `blackdiamond` carries 2 registry scopes, so `firm_scope()`
   will refuse and ask for a `registry_key`. There is no Cottonwood custody master in
   `infra/logic/registry/` today; that is a registry row to add before the cell is cut.
