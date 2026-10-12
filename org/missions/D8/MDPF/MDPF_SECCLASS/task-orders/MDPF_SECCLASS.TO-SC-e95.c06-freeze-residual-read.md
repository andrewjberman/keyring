# TO MDPF_SECCLASS.TO-SC-e95 -- round 22 SC-e-95: READ: what C_06's first-build freeze leaves, what re-deriving would cost, who moves canonical

<to_id>MDPF_SECCLASS.TO-SC-e95</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~85</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-95` (`decompositions/MDPF_SECCLASS_DECOMP_R22.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-21 analysis section 2 and section 3 item 1, msg 4327

---

## WORKER FACE

### THE CELL

`SC-e-95`, rows MDPF_SECCLASS-D1-W83-S5 and D1-W80-S4, one structural fact: **C_06 freezes a date at its first build.** The incremental run
(`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`, `build()` :649-) builds only partitions dated after the watermark
(`gold/meta/client_timeseries_watermark.json`, `data_as_of` 2026-10-09) and keeps every already-written date; the firm daily dollars by class
live in `gold/views/mix_daily_summary.json` (`{'firm': {date: {<class>: $, 'total': $}}, 'advisors': ...}`, written by `_write_mix_summary`
:495-505 and accumulated per relationship as `mix[class] * total_mv`, :754-760). B_00
(`data/black_diamond/scripts/gold/B_00.canonical_holdings.py`) keeps moving a retained date's canonical bytes after that date was first built,
and each relationship's stored concentration list keeps only its top-10 holdings. The CTO will not choose between a rolling N-day re-derive, a
one-off rebuild and acceptance before the dollars and the cost are on the record. This cell puts them there, read-only.

**Read (no build, no edit of any product file, no write under `gold/` or `platinum/`):**
1. **The dollars, per retained date 2026-10-06, 07, 08 and 09.** For each date: (a) the SERVED firm snapshot, from `gold/views/mix_daily_summary.json`
   `firm[date]`, by class and in total; (b) a REBUILD of the same snapshot from the CURRENT canonical holdings partition of that date
   (`gold/canonical/holdings/<date>.parquet`; C_06 lists them in `_list_positions_cube_keys()` :324-332): run C_06's own per-partition path
   (`_process_partition`, :146, with the static tables `load_static_tables()` loads as `build()` does at :665-679) and accumulate
   `mix[class] * total_mv` per relationship exactly as :754-760 does, so the rebuilt figure is comparable class for class. Record served, rebuilt
   and delta (rebuilt minus served) by class and in total. The classes are C_06's `MIX_ASSET_CLASSES` (:183-184).
   Do NOT write the rebuilt snapshot anywhere under `gold/` or `platinum/`. SC-e-94 / worker ~78 reproduced 2026-10-08 to the cent this way; the
   harness is the same, so a date that reproduces is the proof it works.
2. **The control date.** Pick ONE earlier date whose canonical partition did NOT change after its first build (every version of its key has the
   same ETag; use `list_object_versions` on its key and print the version count and ETags) and run the same rebuild on it. It must reproduce the
   served figure (the record's `control_date.delta_total` within $1.00); if it does not, the harness is moving, not the data: stop and file a row.
3. **The cost, N = 1, 3 and 5 trading days.** For the N most recent trading days ending at the watermark (use `lib/trading_calendar.py`; print the
   dates), measure the wall time and peak memory of re-deriving exactly those partitions by the same path, run once cold and once warm if the
   second differs, and the write set it would imply: relationships with an entry on any of those dates (`relationships_rewritten`), the keys
   (`keys_written`: each relationship's `gold/entities/clients/{id}.json`, its legacy `gold/client_timeseries/{id}.json` copy and its `_views.json`) and
   `bytes_written` (the sum of the current objects' ContentLength for those keys, read with `head_object` or the list, not downloaded twice). Read
   the chain window beside it: the 04:00:46Z fire's launch-to-stop (runner instance `i-01003b035d2988dfb`, `describe-instances` / the stop event) and
   C_06's wall time in its last fire from the runner telemetry (`logs/gold-layer/telemetry/bd-gold-layer-runner/C_06/*.jsonl`, first and last `ts`).
   The 3,793-JSON, 4.77 GB read the SC-e-91 pass adds per no-new-partition fire is already measured in
   `NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_RETAINED_UNCLASSIFIED_20261012.md`; cite it, do not repeat it.
4. **The mover.** For each of the canonical partitions 2026-10-02 .. 2026-10-09, from `list_object_versions` (paginated to exhaustion, page count
   printed): the number of versions, the number of CONTENT changes (consecutive versions whose ETags differ), and the `LastModified` of the last
   content change. Name the writer (SC-e-94 named `B_00.canonical_holdings.py`, runner run 608de09d26a6, in
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/W78_PARTITION_REWRITE_WRITER_20261012.json`; read it, then confirm or correct it from
   B_00's own code and the telemetry for a content-change timestamp), how far back in trading days a content change has reached, and how often
   (per fire, per week; state what the data shows).
5. **Who holds the unlisted unclassified dollars at 2026-10-09 (row D1-W80-S4).** From the rebuild of 2026-10-09: the unclassified dollars that are
   NOT in any relationship's stored top-10 holdings list (the rebuilt per-relationship holdings, ranked by market value, minus the top ten), by
   SECURITY: the total dollars and positions, and the top 20 as (ticker, name, dollars, has_name_row) with `has_name_row` from a `get_item` of
   `NAME::<NAME>` (read-only). Security level only: no relationship id, account id or client name in the record or the report.
6. Write the record as JSON at
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESIDUAL_READ_C06_FREEZE_20261012.json` with exactly these keys (the checker's header lists
   every sub-key; read it first): `claim` (`measured: read-only, <date and time of the read>`), `read_only` (true), `classes`, `dates` (four entries),
   `control_date` (with `why`), `rederive` (the three N entries), `chain_window` (`launch_to_stop_seconds`, `c06_wall_seconds_last_fire`, `source`),
   `canonical_movers` (`writer`, `dates`, `how_far_back_days`, `how_often`), `unlisted_unclassified` (`date`, `usd`, `positions`, `top`, `why`).
7. In your report, in plain words and without recommending: the drift per date and class (largest three terms), the runtime and write set per N
   against the chain window, the mover. The ruling is the CTO's; do not draw it.

### ACCEPTANCE

<criterion id="SC22-e95-AC1" cell_refs="SC-e-95"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R22_CHECKS/r22_residual_read_check.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESIDUAL_READ_C06_FREEZE_20261012.json</invocation><expect>R22-RESIDUAL ok=True</expect></criterion>
`SC22-e95-AC1` -- the record exists with its four dates, its control date reproducing, its three N entries, its chain window, its mover and its unlisted-unclassified section, and its arithmetic is internally consistent (a copy with one field broken fails the same check first).

<expected_criteria>SC22-e95-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~10:3xZ): SC22-e95-AC1 FAIL as expected (`R22-RESIDUAL ok=False error=absent`). A synthetic valid record reads
`ok=True control=ok`; the same record with a $50 move on the control date reads `ok=False`; one with a relationship key in the security list reads `ok=False`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, list_object_versions, DynamoDB get_item, CloudTrail lookup, ec2 describe): no write to any bucket or table, no
  deploy, no invoke. Never push. The rebuilt snapshot lives in memory and in `.scratch/` only.
- A command that needs more than `timeout 120` runs in the background (`run_in_background`) and is read when it ends; split the rebuild by date and
  keep each date's result on disk under `.scratch/` so a stop loses nothing. The static-table load is the slow part: do it once per process.
- **Client data stays out.** Security-level and aggregate figures only: no relationship id, account id or client name in the record, the report or a
  surprise row.
- **Refusal clause.** If a figure cannot be read as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W85-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not estimate a figure and do not fill a field you did not read.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESIDUAL_READ_C06_FREEZE_20261012.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R22.md</decomp_doc> (round 22), cell `SC-e-95`.
<owned_cells>SC-e-95</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC22-e95-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~85/MDPF_SECCLASS.TO-SC-e95.c06-freeze-residual-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC22-e95-AC1`.
</proof_of_spec>

**REPORT:** the per-date drift by class (largest three terms each), the control date and its reproduction, the runtime, memory and write set per N beside the chain window, the mover and how far back and how often, the unlisted holders (top five), commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE a read the seat's role already makes (the same reads as SC-e-93 and SC-e-94).
comp-adversary: RUN -- a rebuild that does not reproduce an untouched date (the control date is the arm; the checker refuses a control that moves more than $1.00); a per-date figure taken on a sample or a stale partition (each partition key, version and LastModified is printed); a runtime taken warm and quoted as the fire's (cold and warm are both recorded when they differ); a writer named from timing alone (SC-e-94's rule: UNRESOLVED-BY-TIMING-ONLY is allowed and says so); a relationship id leaking through the security list (the checker bans the keys). BLIND: the cost of the BD chain's OTHER scripts when C_06 runs longer (this read does not model it), and any partner-facing meaning of a restated date (the CTO's ruling).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-21 analysis section 2 and section 3 item 1 (msg 4327); rows D1-W83-S5 (worker ~83) and D1-W80-S4 (worker ~80); SC-e-94's record; DECOMP_R22.
