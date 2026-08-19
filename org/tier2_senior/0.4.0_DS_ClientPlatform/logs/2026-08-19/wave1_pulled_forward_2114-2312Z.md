# 0.4.0_DS_ClientPlatform — WAVE-1 pulled forward: WP-1, DRIVE mdpf-canrte-w1a, D4b, D3.1, D1b (2026-08-19 21:14–23:12Z)
**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

Window: fresh session registered 21:14Z (PID 11552), following the
`session_close_0532-1345Z.md` wind-down log. Andrew's do-not-delay drive word pulled WAVE-1
forward to tonight. **All four launcher items closed, plus a DRIVE interrupt and a first mint.**

## What happened (ordered)

1. **Startup clean.** No orphan watcher existed for my serial (`ps` showed 8 live watchers, none
   mine) and the broker read NOT REGISTERED — a genuine fresh session, so the reap-vs-peer
   discriminator never came into play. Monitor `bll3g1n7j` armed and confirmed `running`. A.3:
   **97 of 97** comp-tools resolve bare AND a forwarder was EXERCISED (banner produced), not
   merely resolved.

2. **WP-1 (ADVI_IDSPINE) — silver `fact_bd_allocation`, landed @b885d682f8, minted @2026-08-18.**
   The measurement half found the load-bearing thing: the registry carries
   `dedup_stable_key: TODO (WS-4)` and **NO SUBSET KEY IS SAFE.** Against a printed 30,577
   denominator — AccountID −24,422 rows (79.87%), (PG, AccountID) −670, (PG, PortfolioID,
   AccountID) −338, +Relationship ID −24, **all 92 columns −0.** True duplicates = 0, so
   full-row dedup is the only Rule-17-safe key and is a measured no-op.
   **The estate's bd-plane script dedups by AccountID and reusing it was the obvious rung-2 move**
   — it would have destroyed four fifths of the feed and taken the portfolio-group membership
   grain (exactly what WP-2's bridge is built from) with it. *The reuse was correct to attempt and
   wrong to complete.* WP1-1..WP1-4 all measured PASS; the precision guard **caught my own bug**
   on its first live exercise (I had written `len(digits)+|exp|` instead of `len(digits)+exp+scale`).

3. **[DRIVE] mdpf-canrte-w1a — CLOSED @455b8c33ce after 13.9d held.** COO asked whether the gate
   still held. It did not, and **the row was masking a live event.** Gate discharged (450 keys,
   every partition 08-06+ a genuine producer write with moving values). **L7 DISCHARGED BY
   EXERCISE** — the emitter's OWN logged `partition_key` = `gold/mdpf_revamp/_aggregate_aua/
   2026-08-18.json`, not "the file exists". **L8 CANCELLED** (Stage-5 OWNTS deleted 08-11, act
   X-iv; no IAM Allow on either grant plane) and **L9 SUPERSEDED** (`mdpf-daily-trigger` absent
   from all 195 functions materialised client-side, positive control `mdpf-gold-lambda` Active;
   scheduler re-homed, EC2 stopped). **What it hid:** today's 13:31Z `mdpf_aggregate_aua` run hit
   an A7 reconciliation ERROR and **refused to write** (`partners=1` vs a healthy 2,
   `non_model=0.00` vs $218,988,251.14, headline ~$310M light). *A chronically-red row is
   indistinguishable from a newly-red one.*

4. **D4b (D4_ETFPOS) — provenance FIRST, and it retired a sovereign ask @afd2d831fe.** Both CSVs
   trace to one commit (@cfdddb5d8d, CRO, 07-31) whose body states *"Andrew approved TrueShares
   egress 2026-07-31"* and names the source: a TrueShares-published Google Sheets CSV export.
   **The Q1 vendor-egress ask is NOT required** — four independent legs: the vendor is already a
   live standing daily source (`etfs-netassets-daily` Active, ENABLED, `cron(0 22 * * ? *)`), the
   publisher is the same, a direct Andrew approval already exists, and the export form is already
   in-estate. **ZERO EGRESS PERFORMED.** Coverage measured **2/4, not 4/4**, three consecutive
   days — recorded FAIL because the hole *is* D4's justification.

5. **D3.1 (D3_MODELOVERLAY) — spec + enum contract @1914fa3fd6; contract RATIFIED @b513a7fdbd.**
   Residual **19 of 19 classified, zero unexplained**. **Four of the PRD's seven proposed enum
   values did not survive measurement** — `CLOSED` classifies nothing (the map holds ZERO `close`
   rows; all 19 residuals are `open`; all 26 `workingClose` joined), `NO_SMARTX_ALLOCATION` is
   wrong-grain, `OTHER_CUSTODIAN` would be inferred, two needed renaming.
   **U1 is ANSWERED and is not a gap** — `fact_model_allocation_roster`, a complete 1:1 edge
   covering **7,305/7,305 (100.00%)**, four vintage-pinned citations @3e4e1843. PRD 4.2 unblocked.

6. **WP-1 silver partition MINTED on COO's word**, verified **on values not key existence**:
   30,577 rows read back from S3, 0 mismatches vs vendor, sum $8,459,429,469.8235 both sides,
   negative control 30,577/30,577 mismatches when shifted. Unblocked DS~B's withheld gold mint.

7. **D1b (D1_CATVIEWS) — the MDPF category registry @be05d938af.** Existence check run **with a
   positive control** (0 on target vs 25 on a sibling through the same invocation). **6 F5
   raise-paths exercised, 4 positive controls, rc=0.** Q1-closed shape built and the data-driven
   property **measured** (6 ticker literals in the table, 0 elsewhere).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | 12+ calls across data/, infra/, org/ | PASS | every call printed its denominator; the `docs.google.com` search is what coupled the sheet-export form to a page we already fetch daily — a text-local grep would have found the string and missed the coupling |
| `commit-gate.sh` | 2 new `.py` files | PASS | py_compile + ds-precommit-check + ruff py39 |
| `comp-pipescript io` | `mdpf_revamp_model_crosswalk --pipeline mdpf` | PASS | resolved (gold, order 160); correctly reported no S3 I/O **and named its own limitation** rather than returning a silent empty |
| `comp-pipescript io` | `bd49f_fact_allocation --pipeline assets` / `--pipeline all` | **COVERAGE GAP** | rc=2 — `assets` is not a valid choice; under `all`, "Unknown script". **CONTROL: the already-shipping sibling `bd49f_dim_conversion.py` is EQUALLY unknown**, so the whole `data/assets` 49F tree is unmodelled |
| `deploy_ledger.py` | close-leg ×3, close, check | PASS | entry CLOSED, sentinel removed; 3 of 3 remaining HELD-STALE rows belong to other seats |
| `proof-of-spec-check.py` | 4 instances | 2 VALID / 2 blocked | D3.1 + D4b rc=0 (D3.1 also coverage-checked against its declared expected set); WP-1 + D1b blocked on the artifact-coverage heuristic |
| `comp-system` | recompile ×4 | PASS | the 06 regen the commit gate requires; landed in the same act each time |
| `a06_dim_identity_crosswalk.py` | `--dry-run` + `build_crosswalk` imported | PASS | ran the estate's OWN coverage instrument rather than re-deriving the join, so the census is comparable to the PRD's cited figures |

**Gap found:** `comp-pipescript` does not model the `data/assets` 49F tree at all — the DS
compiler-tool minimum is unsatisfiable there, and `OPAL_ASSETS.SILVER-DTYPE`'s instruction
`comp-pipescript io schwab_conversion --pipeline assets` **cannot execute as written** (worth
fixing on that TO's face before it is worked 08-21). Rule 22: a coverage gap is a DEFECT.

**Second gap, now characterised:** `proof-of-spec-check`'s artifact-coverage rule requires the
artifact stem token inside a `criterion_id` (DS `{firm}-{group}-{artifact}-{check}` grammar) and
fires **only** on `script`/`s3_object` artifacts. Every TO with issuer-minted non-DS ids that
produces a script will fail it — 2 of 4 tonight. Declined the `declared_exclusions` escape twice.

## MCP traffic
~20 handled. Significant: DRIVE answer + dispositions to COO/CTO/AE; D4b provenance to COO/CRO;
D3.1 contract to CTO (ratified as authored) and the registry entry to CRO; four exchanges with
DS~B (dedup warning → their `Primary Portfolio Group` correction → their `Account Supervised`
finding → my 19-of-24 scope correction); mint notice to COO + DS~B.

## Briefs Written
`SMARTX_BD_EXACT_JOIN_SPEC_20260819.md`; `data/_contracts/smartx_bd_join_disposition.yaml` (v1.0,
RATIFIED); `SMARTX_BD_JOIN_DISPOSITION_SYSTEM_DEFINITIONS_ENTRY.yaml` (authored, routed, not landed).

## Errors I made and corrected
- **Told DS~B the export carries `Primary Portfolio Group`. It does not** (0 of 92; positive
  control 8). I had the column list open and generalised from "Rule 17 preserves everything" to
  "the field you need is there". **Preservation is not provision.** Retracted, re-derived
  independently, carried into the record.
- **Swept 8 untracked `.open_findings/*.json` files that were not mine** into the ledger commit by
  passing `org/critical_paths/` as a pathspec. Additive tool-generated records, nothing
  overwritten — surfaced to COO rather than left to be found; switched to explicit file paths after.
- **Precision arithmetic wrong** in the WP-1 decimal guard; the guard caught it on first exercise.

## Blockers
None of mine. Waiting (not blocked): CRO to land the SYSTEM_DEFINITIONS entry (outside my lane);
COO/CTO on the proof-of-spec-check artifact-coverage call; Andrew on the narrow TrueShares scope
confirmation (COO holds it, leading with the never-backfillable urgency).

## Current State (successor handoff, zero-context)
- **All four WAVE-1 items CLOSED** + the DRIVE ledger + the silver first mint.
- **`fact_bd_allocation`**: script @b885d682f8; `date=2026-08-18` minted and value-verified. Only
  ONE partition exists — backfill is available on request (bronze runs daily back through 08-03+).
- **Grain statement is SIX terms** (PG × Portfolio × Account × Relationship × Supervision × Fee
  Schedule); the −24 is fully decomposed (19 supervision + 5 dual-fee `z0813542821`) and
  recommended for the WS-4 registry note.
- **D4c is authorised: BUILD, DO NOT FIRE.** Extend `etfs-netassets-daily`; leave the schedule
  DISABLED; enable is a one-line act pending Andrew's scope word.
- **Dated at this seat:** THU 08-20 13:30Z PB-1/PB-2 proof read (AE's package rebuild landed
  13:48:28Z, so tomorrow's scheduled run is the proof vehicle); `ADVI_BDPARITY.P1-PROBE` activates
  at the THU respawn AFTER that read; INF one-writer 08-20; SILVER-DTYPE 08-21.
- ⚠ **`json/mdpf/49financial/aggregate-aua-timeseries.json` delete STAYS HELD until PB-1 PASS** —
  Andrew's reserved act, never mine.
- Monitors: inbox `bll3g1n7j` (dies with session).

## Next Steps
1. [0.4.0_DS_ClientPlatform] D4c — extend `etfs-netassets-daily` for the TrueShares holdings sheet;
   build + dry-run against the in-repo 07-31 CSVs; **schedule DISABLED**.
2. [0.4.0_DS_ClientPlatform] THU 13:30Z PB-1/PB-2 proof read, then P1-PROBE.
3. [4.0.0_SA_CRO] land the `Smartx_Bd_Join_Disposition` registry entry; set its `status`.
4. [2.0.0_SA_COO / 1.0.0_SA_CTO] the proof-of-spec-check artifact-coverage call; owner for the
   16 `KEY_OUTSIDE_ACCOUNT_GRAMMAR` scope decision; the two `comp-pipescript` / two-homes items.
