# TO MDPF_SECCLASS.TO-SC-e110.s45-leg-g-cause-read -- round 28 SC-e-110: why the 13-row seed is not visible where leg G reads it (a read; nothing is changed)

<to_id>MDPF_SECCLASS.TO-SC-e110</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~100</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-110` (`decompositions/MDPF_SECCLASS_DECOMP_R28.md`) |
**outcome_ref:** FWD-1 / FWD-5 | **depends_on:** none | **source:** CTO round-27 analysis section 3 item 2 (msg 7425); row MDPF_SECCLASS-D1-S45

---

## WORKER FACE

### THE CELL

`SC-e-110`. On 2026-10-16 at 06:27:08Z thirteen canonical classification rows were written (the "seed"). After the next scheduled fire, the read that grades it (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22_legg_read.py`, "leg G") prints `ok=False`: the dollars it expects to leave `unclassified`+`other` did not. You find the FIRST place the seeded dollars stop being where leg G expects them, and say what would make leg G read true. You change nothing: no instrument, no code, no table.

**What is already measured (start from it):**
- The 13 seeded tickers and their ruled classes (`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json`, key `planned`): AEMGX equity, CEMVX equity, CPXIX fixed_income, CUBE alternatives, EZET commodities, FBCVX equity, FIADX equity, GLPI alternatives, HODL commodities, HPI fixed_income, LCFYX fixed_income, PFF fixed_income, VRP fixed_income. Nine more are deliberately held out (`seed_pending`).
- The served object: bucket `opal-data-49financial`, key `advi/49financial/platinum/views/mix_daily_summary.json`, JSON `firm[<date>]` holds class dollars. Versions: `3BY8Etw3LetRaRFcOofjaAT98PSfp4Z3` (written 2026-10-16T05:25:26Z, before the seed), `87CvfcFpbyM7ZRAb0P6AztqK1X74W6cQ` (2026-10-17T00:22:27Z, the first fire after the seed), `l2Wqoi6iUJwQwwmTCu3lXWozfW4.Ak_.` (2026-10-17T05:24:08Z, the second). On 2026-10-02, `unclassified`+`other` is 1,924.34 in BOTH `3BY8...` and `87Cv...`.
- What leg G expects for 2026-10-02: 124,848.36 of seeded dollars (and 246,814.32 held out) to leave `unclassified`+`other`. It computes that figure from `s3://opal-data-bd/gold/holdings_lots/<date>.parquet` (open lots), NOT from the canonical holdings that the firm-mix script C_06 reads. For 13 of the 15 window dates that lots partition does not exist (NoSuchKey), so leg G cannot grade them at all.
- What C_06 reads: `s3://opal-data-bd/gold/canonical/holdings/<date>.parquet` (columns date, account_id, asset_name, units, price, market_value, source, bd_units, schwab_units, ticker). Version `wtAhSnBVfcTlrV.Y6Ml3Jh.ggcyBgQkf` of the 2026-10-02 object was written 2026-10-16T23:15:29Z (the 23:00Z fire, the first after the seed). In the later version `aMEdNa9yQApdT4HVnPu3NLMqQ3WB1AV0` the seeded tickers hold only six rows and 27,668.40 (AEMGX 3,973.06; CEMVX 4,109.08; FBCVX 4,812.51; FIADX 2,882.52; GLPI 67.24; PFF 11,824.00); the other seven (CPXIX, CUBE, EZET, HODL, HPI, LCFYX, VRP) have no row by ticker. 25,458 of its 112,510 rows have an empty `ticker` (those classify by `asset_name`, the `NAME::` path).
- The first candidate, not a conclusion: `instrument-expectation` (leg G expects dollars from a table C_06 does not read, and the dollars it expects to leave a bucket that held only 1,924.34).

**What you do:** (1) Re-read the canonical object for 2026-10-02 at version `wtAh...` and, for each of the 13 tickers, count its rows and sum its `market_value` (upper-case ticker match). (2) Read how C_06 (`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`) classifies a holdings row: which function, which key (ticker or `NAME::` + asset_name), which table (`lib/etf_classifier.py` names the DynamoDB table and the reader); read the 13 seeded keys from that table with AWS reads and record each class in the table. (3) For the seven tickers with no ticker row, find whether their positions exist under another identity (an `asset_name` that is classified by a `NAME::` key) and say what class C_06 gives them. (4) Pick `first_divergence` from the list below and state the fix. Write `S45_CAUSE.json` at the path in `<paths>`.

`S45_CAUSE.json` has exactly these keys (the acceptance script lists them in its header; read `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R28_CHECKS/check_s45_cause.py`, do not edit it):
- `first_divergence`: one of `instrument-expectation`, `table-read`, `classify-call`, `identity-join`, `aggregate`, `other`.
- `canonical`: `{bucket: "opal-data-bd", key: "gold/canonical/holdings/2026-10-02.parquet", version_id: "wtAhSnBVfcTlrV.Y6Ml3Jh.ggcyBgQkf"}`.
- `tickers`: 13 entries, one per seeded ticker: `{ticker, canonical_rows, canonical_mv, class_in_table, note}`; `canonical_rows` and `canonical_mv` are what that version holds for the ticker (0 and 0.0 when none), which the checker recomputes within 0.01; `class_in_table` is the class you read from the table (a non-empty string).
- `served`: `{bucket: "opal-data-49financial", key: "advi/49financial/platinum/views/mix_daily_summary.json", pre_version_id: "3BY8Etw3LetRaRFcOofjaAT98PSfp4Z3", post_version_id: "87CvfcFpbyM7ZRAb0P6AztqK1X74W6cQ", date: "2026-10-02", uncl_other_pre, uncl_other_post}` (the two `unclassified`+`other` sums, recomputed within 0.01).
- `conclusion`: at least 40 characters: where the seeded dollars stop, in one place.
- `fix`: at least 20 characters: what would make leg G read true (an instrument change or a code change), stated and not done.

### ACCEPTANCE

<criterion id="SC28-e110-AC1" cell_refs="SC-e-110"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R28_CHECKS/check_s45_cause.py read</invocation><expect>S45-CAUSE ok=True</expect></criterion>
`SC28-e110-AC1` -- the file has an entry for each of the 13 seeded tickers whose canonical numbers and the two served numbers the checker recomputes from S3 within 0.01, a divergence from the list, a conclusion and a stated fix.

<expected_criteria>SC28-e110-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-17 ~08:0xZ): AC1 FAILS as expected (`S45-CAUSE ok=False problems=['no file at ...S45_CAUSE.json']`). The script's `selftest` runs a green arm and five negative arms (a seeded ticker with no entry, a canonical_mv that does not reconcile, a served number that does not reconcile, a divergence outside the list, a fix under 20 characters) and prints `S45-CAUSE-SELFTEST ok=True`; its live readers were checked against the known 2026-10-02 numbers (AEMGX 3,973.06 in one row; `unclassified`+`other` 1,924.34 in both served versions).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted (downloaded parquet files go there).
- **AWS READS ONLY** (`s3api get-object` / `head-object` / `list-object-versions`, `dynamodb get-item` / `describe-table` / `batch-get-item`, through `.tools/aws` or boto3). No write, delete, put, update, scan-and-modify, invoke, start, stop or deploy of any kind. A Dynamo read is a `get-item` or `batch-get-item` on the 13 keys, never a full-table scan.
- **No package install and no download** into the repo.
- **Never edit** anything outside the `<paths>` block; `seed22_legg_read.py`, `SEED22_PLAN.json`, C_06 and the classifier are READ-ONLY to you. Never push.
- **Refusal clause.** If you cannot say where the seeded dollars stop, do not guess and do not edit a check. Write what you read in your report, file a surprise row (id `MDPF_SECCLASS-D1-W100-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) naming what you could not account for, and stop; leave AC1 failing.
- Run every invocation under `timeout 120`; bound each of your own reads by key.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~100/S45_CAUSE.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R28.md</decomp_doc> (round 28), cell `SC-e-110`.
<owned_cells>SC-e-110</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC28-e110-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~100/MDPF_SECCLASS.TO-SC-e110.s45-leg-g-cause-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC28-e110-AC1`.
</proof_of_spec>

**REPORT:** the per-ticker table (rows, dollars, class in the table, class C_06 gives the row), the first divergence and its evidence, the fix, the criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- per-ticker numbers typed rather than read (the check recomputes every one from the pinned canonical version); served sums typed rather than read (recomputed from the two pinned served versions); a conclusion with no stated fix (the 20-character floor); a divergence outside the list.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-27 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_27_20261017.md`, msg 7425); DECOMP_R28.
