# TO IRPT_DASHBD.TO-DB-b-44 -- FWD-8: build, offline, the split Black Diamond pull (2,299 accounts, 2,299 calls, 4,598 ranges split at 2025-01-09) and its live runner, on Andrew's per-use word; the live run is the issuer's

<to_id>IRPT_DASHBD.TO-DB-b-44</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~25</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-19 analysis @b402b7b2e3 section 2 ("One
Black Diamond pull, split at 2025-01-09, for the accounts behind the 2,299 closure segments. Each segment range is requested as two
ranges, ending 2025-01-08 and starting 2025-01-10"), and Andrew's per-use word relayed by 0.0.0_AB_MSTR~DELL2 msg 1103 ("go with your
rec": ONE split, read-only pull, 2,299 accounts, 2,299 calls, 4,598 date ranges; nothing wider; record @5ef6d33141) | **Decomp cell:**
`DB-b-44` (decomposition section 26b) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-29 (merged; the 2,299 segments).

THIS CELL MAKES NO VENDOR CALL. It builds the plan and a runner, and runs the plan mode only. The LIVE run (`run --go`) is the issuer's
WORLD act, under the word above; the tie-out of what lands is the next cell.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-25`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~25/`.

**The cell (`DB-b-44`).** 2,299 closure segments (one per account) are in
`deliverables/0.9.0_WK_IRPT_DASHBD~14/CLOSURE_ALIGN_E1P.json` `rows` (`account`, `segment {start, end}`); every one is outside BD's
convention on the gross basis. The pull asks Black Diamond for each account's return over the same segment as TWO ranges,
(segment start .. 2025-01-08) and (2025-01-10 .. segment end), so BD's own figure either side of the 2025-01-09 closure can be compared
with Opal's. ONE call per account carries both ranges.

**What exists (reuse it; never restate a request body).** Round 14's pull and runner:
`deliverables/0.9.0_WK_IRPT_DASHBD~6/bd_population_pull_e3.py` (`build_plan`, `map_account`, `load_xref`, `_address`, the request body
built through `infra/aws/lambda/investor-reporting/performance/bd_adapter.py` helpers, `run`), its plan
`deliverables/0.9.0_WK_IRPT_DASHBD~6/BD_POPULATION_PLAN_E3.json` (its `request_list` entries carry `account`, `bd_account`, `body`,
`segments`), and the concurrent runner `deliverables/0.9.0_WK_IRPT_DASHBD~8/bd_population_concurrent_e3.py` (one coordinator owning the
shared bearer, a rate limiter, ramp, 429 halving, one retry per call, FAILED, abort rules, checkpointing, `sweep`). Import them by path,
as `~8` imports `~6`; do not copy them.

1. **`bd_split_pull.py`** in your folder, with three modes:
   - **`plan`** -- OFFLINE (DRY_RUN=1; S3 list reads only). For each of the 2,299 accounts: map it to its BD internal id with round 14's
     mapping; build ONE request body with the two ranges, through the same helpers round 14 used. Choose a `pull` token for a NEW
     `pull=` prefix that is not any prefix already landed under the round-14 landing template (list them from S3 into
     `existing_pull_prefixes`); each landing key is `_address(on, pull, bd_internal_id)`, verbatim builder output. Write
     `SPLIT_PULL_PLAN.json`: `dry_run` true, `vendor_calls` 0, `word` (msg 1103 and the record), `pull`, `existing_pull_prefixes`,
     `request_list` [{account, bd_account, ranges: [{start, end}, {start, end}], body, landing_key}], `unmapped` (any account round 14's
     mapping cannot place, with its reason; never guessed), and `request_bodies_sha256`. Print both denominators (record rows = planned +
     unmapped) and the request and range counts.
   - **`run --go`** -- LIVE, THE ISSUER'S, never yours. Refuses unless `--go` is given, the plan exists and re-derives identically, and
     the plan's counts are exactly 2,299 requests and 4,598 ranges (Andrew's word is for that pull and nothing wider). It runs the plan
     through round 14's concurrent coordinator rules (shared bearer, pace, ramp, retry, FAILED, abort, checkpoint) and lands each 200 at
     its plan landing key. Writes `SPLIT_PULL_RUN.json` per call, checkpointed. Never logs a credential, a bearer or a response body.
   - **`sweep --go`** -- LIVE, the issuer's: the run's FAILED set once more, under the same rules, inside the same 2,299.
2. **`tests/test_bd_split_pull.py`** in your folder: at least 6 offline tests (stub boto3, the helpers and time): each request has the two
   split ranges; one call per account and no account twice; the plan refuses a pull token already landed; `run` and `sweep` refuse
   without `--go`; `run` refuses a plan whose counts are not 2,299 and 4,598 (a widened plan); both denominators are printed. The words
   `split`, `--go` and `denominators` appear in the file.
3. **Run `plan` once**, then commit the script, the tests and the plan. Write `SPLIT_PULL_PLAN.md`, COUNTS ONLY.

If round 14's mapping leaves any of the 2,299 unmapped, the plan holds fewer than 2,299 requests and AC1 fails: file a row with the
unmapped list and stop on AC1; never fill the gap by hand.

<criterion id="DB26-3-AC1" cell_refs="DB-b-44"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_split_pull.py" . DB26-3-AC1</invocation><expect>DB26-3-AC1 PASS</expect></criterion>
`DB26-3-AC1` -- the plan: 2,299 requests over the record's 2,299 accounts, 4,598 ranges split at 2025-01-09, builder landing keys under a
new pull token, 0 vendor calls. Base: FAIL.

<criterion id="DB26-3-AC2" cell_refs="DB-b-44"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_split_pull.py" . DB26-3-AC2</invocation><expect>DB26-3-AC2 PASS</expect></criterion>
`DB26-3-AC2` -- the offline tests pass (at least 6) and cover the split, `--go` and the denominators. Base: FAIL.

<expected_criteria>DB26-3-AC1,DB26-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Round 14's scripts are read and imported, never edited.
- **AWS:** S3 reads and lists only. NO Black Diamond call, no token mint, no secret read, no `run`, no `sweep`, no S3 write, no bun, no
  download of any package, script or program.
- **Refusal clause.** Any vendor call, token mint or secret read, a `run` or `sweep`, a credential or bearer written anywhere, a hand-typed
  landing key, or a client figure in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~25/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-44.bd-split-pull-plan.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 26b (round 26, workstream BD), cell `DB-b-44`.
<owned_cells>DB-b-44</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB26-3-AC1, DB26-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~25/IRPT_DASHBD.TO-DB-b-44.bd-split-pull-plan.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB26-3-AC1,DB26-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the request, range and unmapped counts, the pull token, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline plan and a runner; no vendor call, no S3 write in this cell. The live run is the issuer's WORLD act under Andrew's per-use word (msg 1103) and lands only under a new pull= prefix of the BD bronze tree.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads and lists only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB26-3-AC1 and AC2 base FAIL (no plan, no tests), dry-run at base 1690130138 2026-10-07 ~21:4xZ; the denominator read from CLOSURE_ALIGN_E1P.json: 2,299 rows, 2,299 accounts, one segment each.
lane: the <paths> block IS the grant.
</preflight>
