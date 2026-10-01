# ETFS_RIVALS task order -- `RIV-f-3` -- ROUND 4 (ENRICHMENT): PER-SOURCE IDENTITY FLOORS (THE CTO'S KEY-4 REFUSAL, RULING 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-f-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~12:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-4 decomposition; declared on RIV-v-2, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund. Rounds 1-3 built the live pipeline (package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg); the 2026-10-01 page serves 12 of 13 funds. **Round 4** fixes the daily trade pairing, unifies 'newest', grades identity per source and adds GQGU. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-f-3` -- per-source identity floors (ruling 3)

- `guardrails.identity_coverage(reports, cfg, source)`.
- `guardrails_config.json`: `min_resolved_fraction` per source {issuer, bloomberg, home_producer} (home funds by name). Values
  stay PROVISIONAL here; RIV-d-5 sets the measured ones.
- `guardrails.load_config()` merges the JSON in `RIVALFUNDS_GUARDRAILS_OVERRIDE` when it is set.
- The reason string names the source and its floor. `evaluate_fund` already receives `source`.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 48ec92238a)

- `guardrails.identity_coverage(reports, cfg)` (~line 154) grades ONE `min_resolved_fraction` (config value 0.0 PROVISIONAL,
  `guardrails_config.json`) for every fund; `evaluate_fund(day, dates, reports, trade_meta, cfg, source=None)` already receives
  the fund's source (publish_page passes `fund_source(...)`: issuer / bloomberg / home_producer) and passes it to freshness only.
- Measured on 2026-09-29: home funds 0.0, BASG 0.924, SCHY 0.982, others 1.0 -- one floor over mixed sources either fails the
  home funds or means nothing (CTO msg 27736).
- `publish_page.py` is RIV-v-2's this round: do NOT edit it; the per-source grading lives in guardrails, the test override is the
  environment variable `RIVALFUNDS_GUARDRAILS_OVERRIDE` (JSON merged over the config by `guardrails.load_config()`).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{1,2,3,4}/checks/`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check mirrors it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call, the vehicle, any file another round-4 cell owns. Tests go beside the code as `tests/test_f3_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; the issuer runs the whole suite at the drain.

<paths>
data/etfs/scripts/rivalfunds/guardrails.py
data/etfs/scripts/rivalfunds/guardrails_config.json
data/etfs/scripts/rivalfunds/tests/test_f3_*.py
data/etfs/scripts/rivalfunds/tests/test_p1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- with an impossible Bloomberg floor via the override, TXUE fails identity_coverage naming 'bloomberg'; IDVZ (home) and BASG (issuer) pass their own floors (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/f-3.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-f-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/f-3.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-f-3.per-source-identity-floors.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-f-3.per-source-identity-floors`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-3 analysis @d4a1e22801 (msg 27810), decomposition round 4 v1.0. Checks dry-run
at base 48ec92238a: f-3.AC1 FAIL -- each FAIL as expected.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<completion_note>2026-10-01 drain by 2.0.0_SA_COO~RV: worker 0.9.0_WK_ETFS_RIVALS~3 @46ee51aff0 (build a1a01427c9); proof instance VALID; f-3.AC1 PASS (TXUE fails an impossible bloomberg floor naming the source; IDVZ home and BASG issuer pass their own); per-source floors PROVISIONAL 0.0 + home_funds {IDVZ, PFOE}; env override RIVALFUNDS_GUARDRAILS_OVERRIDE; no rows.</completion_note>
<round>4</round>
<slot>~3</slot>
<fabric>site-z</fabric>
