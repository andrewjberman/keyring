# NFRA_IAMROLES202609.TO-IAM-u-1 -- THE POSTURE NUMBER, a rollup of the committed 219-role census

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R4.md</decomp_doc>
<owned_cells>IAM-u-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~10</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-1; the round-3 analysis calls this R4-A)

```
IAM-u-1. ACT: produce the estate's least-privilege POSTURE NUMBER as a rollup of round 3's committed
permission-grain census. No cloud call: every figure is recomputed from the committed bundle.

FWD-1, verbatim:
  "Someone can state our least-privilege posture with a number, what it is out of, and when it was
   taken."
  DONE WHEN  EXERCISED -- a reviewer has actually answered the question with that evidence attached,
             rather than an opinion
  ACCEPT     Asked "are we following least privilege?", someone answers with how many things were
             checked, out of how many exist, and as of when.

THE INPUT (read only, never edited):
  org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/permission-cold-raw-bundle.json
  Top-level keys: produced_by, to_id, instrument, instrument_blobs, account, run_date_utc (2026-09-10),
  lookback_days (90), population_rule, attempted (219), returned_rc0 (219), note, per_role_rc, results.
  results is {role_name: {role, role_arn, lookback_days, granted_read_ok, advisor_read_ok,
  rows: [{permission, status, ...}]}} where status is one of never-used / used / unobservable.
  Its human rendering is PERMISSION_USAGE_EXERCISE.md in the same directory.

  Recomputed by the issuer at the cut from that bundle (your script must reproduce these exactly):
    all 219 roles:          granted 5494 = used 421 + never-used 1437 + unobservable 3636
    excluding opal-drift-producer-codebuild-role (218 roles):
                            granted 2576 = used 418 + never-used 695 + unobservable 1463
  That one role carries 2918 of 5494 grants off a single AWS-managed ReadOnlyAccess attachment, so every
  aggregate is printed WITH and WITHOUT it, and the reader is told to read the WITHOUT row first.

THE POPULATION QUALIFIER MUST TRAVEL INTO THE FIGURE (surprise row Z-W8-S2, carried by the analysis):
  219 is every live role at Path "/" -- 229 roles in the account at 2026-09-10 MINUS the 10 at
  Path "/aws-service-role/" (AWS service-linked, excluded and named in the bundle's population_rule).
  A posture figure inherits its population's qualifier or it is wrong, and this is exactly the grain at
  which a number gets quoted onward without it.

WHAT TO PRODUCE, in deliverables/0.9.0_WK_NFRA_IAMROLES202609~10/:

  (a) posture-rollup.py -- stdlib only, takes the bundle path as its one argument, makes NO network or
      AWS call, and prints at least these two lines, exactly in this shape:
        TOTALS roles=219 granted=5494 used=421 never-used=1437 unobservable=3636
        TOTALS-EXCL-CODEBUILD roles=218 granted=2576 used=418 never-used=695 unobservable=1463
      plus whatever per-role or distribution lines you find the posture needs.

  (b) POSTURE_NUMBER_ESTATE.md -- the answer to "are we following least privilege?". It MUST carry a
      headline line that begins `POSTURE: ` and states, on that one line: the figure, the word
      `denominator` with what it is out of, `as of 2026-09-10`, and the qualifier naming the 10
      `service-linked` roles excluded. A second headline line beginning `POSTURE-EXCL-CODEBUILD: ` gives
      the same figure without opal-drift-producer-codebuild-role.

      WHAT FIGURE: your call, defended in the document, but it must keep three things in view at once:
      of the grants that CAN be observed, what share were used in the 90-day lookback (421 of 1858 on
      all roles); what share of all grants can be observed at all (1858 of 5494); and the unobservable
      share (3636 of 5494, 66 percent). C-COVERAGE-OVER-COUNT: a figure that hides the unobservable
      two-thirds is wrong even if its arithmetic is right. Never present never-used/granted (1437 of
      5494) as the posture: it reads the unobservable grants as if they were clean.

  (c) A "since then" paragraph: the figure is as of 2026-09-10. The live role graph read 283 IAM_ROLE
      nodes at 2026-10-09 03:31 UTC (a different instrument, which counts service-linked roles too), so
      the population has MOVED. State that; do NOT recompute against AWS -- a fresh run is a different
      cell (IAM-u-2) this round.
```

## DEPENDENCIES

None. The input bundle is committed. IAM-u-2 (a fresh run) runs beside you and you do not wait for it.

## BOUNDS

```
NO CLOUD CALL. This cell reads one committed JSON file. No aws, no comp-iam-usage run.
C-NO-ACCESSDENIED: nothing is narrowed, detached or applied; the posture number recommends nothing.
C-TWO-REMEDIES: permissions axis only. Do not touch GOVERNANCE_DISPOSITION.md or any owner field.
READ, NEVER WRITE: every other worker's deliverables directory (~1 .. ~9, ~11, ~12) is read-only to you.
G-21: no alert, alarm, monitor, schedule or notification of any kind.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam-usage    instrument pins unchanged since the round-3 run (5c7f03ba37 / 8670fc5025), so the
                  bundle you roll up was produced by the code that is at HEAD today.
round-1 POSTURE   deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md is a ONE-ROLE posture
                  (opal-data-refresh-lambda-role). Read it for vocabulary; it is NOT an estate figure and
                  your document must not cite its number as one.
comp-find aws     283 IAM_ROLE nodes, graph vintage 2026-10-09 03:31:25 UTC (DECLARED=262,
                  LIVE-no-DECLARED=18, MULTI_STATE_MANAGED=3). Used only for (c).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~10/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-u-1.posture-number-rollup-of-the-219-role-census.md
</paths>

Read surfaces (not granted for writing): the round-3 bundle and report in `deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/`,
the round-1 posture in `~1/`, the PRD at `org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md`.
Your surprise row id is `NFRA_IAMROLES202609-Z-W10-S<k>`, `"fabric": "site-z"`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-u-1"><invocation>python org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~10/posture-rollup.py org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/permission-cold-raw-bundle.json</invocation><expect>output carries the line `TOTALS roles=219 granted=5494 used=421 never-used=1437 unobservable=3636` and the line `TOTALS-EXCL-CODEBUILD roles=218 granted=2576 used=418 never-used=695 unobservable=1463`, recomputed from the committed bundle with no cloud call; a missing script (rc=2, "No such file") means the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-u-1"><invocation>grep -c -E '^POSTURE: .*denominator.*as of 2026-09-10.*service-linked' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~10/POSTURE_NUMBER_ESTATE.md</invocation><expect>a count of 1 or greater -- the headline carries its figure, its denominator, its vintage and the service-linked qualifier on ONE line, so the number cannot be quoted onward without them; a "No such file" error means the deliverable is missing</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-u-1"><invocation>grep -c -E '^POSTURE-EXCL-CODEBUILD: ' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~10/POSTURE_NUMBER_ESTATE.md</invocation><expect>a count of 1 or greater -- the figure is also given without the one role that carries 2918 of 5494 grants</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-u-1" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming
  3.0.0_SA_CVO~Z): asked "are we following least privilege?", does the document ANSWER with a number, what it
  is out of and as of when -- and does that answer keep the unobservable two-thirds in view, so a reader
  cannot take it as a cleaner estate than was measured?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>4</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-u-1</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 4) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-3 slug @36e167a2ea -> `ROUND_ANALYSIS.round3.md` @f8571787db section 7 (R4-A) -> L5 round-4 decomp -> this issuance.
**Chain:** an independent chain of one. **Class:** worker-light -- a rollup script plus one document, well under 100 product lines.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule`, BUDGET REACHED at 220 s, 1 of 6 carriers, denominator C1=23 (7 gates armed), C2=32 PARTIAL (0 of 32 scanned); PARTIAL_OR_BLIND, not read as clean. G-21 binds as CLAUDE.md law.
comp-iam: RUN -- `bash .tools/comp-iam stats` from the main checkout: 214 TF roles / 196 services / 1154 operations / denominator 338 gaps; this cell does not read it.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (instrument pins unchanged; population moved 219 -> 283 graph nodes).
</preflight>

**Preflight disposition:** the cell reads one committed file and makes no cloud call; the battery figures are carried for the "since then" paragraph only. Check dry-run at the base `54c2fd91b6`: AC1 base: FAIL as expected (script absent); AC2 base: FAIL as expected (file absent); AC3 base: FAIL as expected (file absent).
