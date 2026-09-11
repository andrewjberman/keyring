# AMGT_RESAPP.TO-AMGT-re-1 -- THE SURFACE, RECUT: four shape gaps L9 named, on top of the panel and tabs that already exist

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-re-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~10</issued_to>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

## THE CELL, INLINED IN FULL (round 6/v0.7, row S16, FWD-15)

```
AMGT-re-1. THE SURFACE, RECUT. A previous attempt (AMGT-rd-8) built the shell and was ADJUDICATED FAIL
on two criteria. YOU ARE NOT STARTING FROM AN EMPTY PAGE and you are NOT rebuilding what exists.

WHAT ALREADY EXISTS AND IS KEPT -- the adjudicator's own words: "the persistent panel, three tabs and
header Print location are present". That work is 20 files / 2,067 insertions on branch
`wk-amgt_resapp-5-8-portal` in the portal repo. START FROM THAT BRANCH.

THE FOUR SHAPE GAPS, quoted from the FAIL grade, are the cell:

 (1) CROSSED CONTROLS, NOT A ONE-TO-ONE MAPPING. "Trending/Breakout are mapped one-to-one to
     Chatter/Price instead of crossed controls." The panel is Trending/Breakout X Price/Chatter --
     TWO INDEPENDENT CONTROLS producing FOUR combinations, not two names for two axes.

 (2) THE READ ADAPTERS. "required /api/scoped/amgt adapters are not delivered." Follow the
     established auth-gated `/api/scoped/*` pattern with the auth-validator-edge viewer-request; do
     not mint a new unauthenticated path.

 (3) STARRED FILTERS, IT DOES NOT RE-ORDER. "The StarredList iterates stored starred order, contrary
     to the report's producer-order filter claim." The starred set is a FILTER over the producer's
     ranked order; the ranking stays the producer's.

 (4) THE CHART IS OVER TIME. "RankedChart is ticker-indexed and has no time-series implementation
     despite the stated automatic second-day behavior." The Chart view plots a ticker's rank ACROSS
     axis_date, and it starts working on day two by itself because AMGT-rd-5 writes a new axis_date
     daily. You will have ONE day of data; the implementation must be correct anyway, and a single
     point is the honest render of one day.

IT READS PRE-COMPUTED ROWS AND NEVER RE-DERIVES A RANKING AT RENDER TIME (C-SERVER-SIDE-RANKING).
The rankings come from `opal-harvest-security-metrics` -- base key axis_date (HASH) / ticker (RANGE),
GSI `axis-rank-index` on axis_date (HASH) / rank_sort (RANGE), PAY_PER_REQUEST, 42 rows live.
MEASURED ON THE LIVE PLANE 2026-09-11 ~20:5xZ, with describe-table on the OLD name returning
ResourceNotFoundException as the control. Prefer the env knob HARVEST_METRICS_TABLE with that value
as the fallback default. The ranked read is Query(IndexName='axis-rank-index',
KeyConditionExpression=axis_date = :ad, ScanIndexForward=True) -- rows come back already sorted, no
client-side sort. The per-ticker point read is GetItem(axis_date, ticker) on the base table.

THREE SHAPE DECISIONS ARE ANDREW'S AND ARE NOT YOURS TO REOPEN:
  - PRINT IS A HEADER EXPORT ACTION, not a tab.
  - THE MODEL TAB IS CUT, its figures REHOMED into Thesis and the Security overlay.
  - THE LEAD PANEL IS PERSISTENT -- it stays while the tabs change beneath it.

WHAT TO PRODUCE, under portal/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~10/:
  (a) the four gaps above, closed on top of the existing branch;
  (b) A RENDER CHECK THAT EXERCISES THE REAL ROUTE AND THE REAL PRINT ACTION. The previous attempt
      rendered fixture components and a PrintTriggerButtonReplica, and the adjudicator's verdict was
      that it "cannot establish live ranking reads or renderer wiring". A replica of the button is
      not the button. READ the render -- do not merely capture it -- against the silver-canvas colour
      law; light text or ghost-white buttons outside a dark Panel are the recurring defect a grep
      cannot see;
  (c) a short deliverable naming, for each of the four gaps, the file and the change that closes it.
```

## DEPENDENCIES

**NONE UNMET.** `AMGT-rd-5` (chatter rows), `AMGT-rd-6` (price rows) and `AMGT-rd-7` (starred state) are
all `complete` and drained; their outputs are what this cell reads. This cell is the whole of round 6.

## BOUNDS

```
BLOCK NOTHING PORTAL MOVES -- NO PROD AND NO DEV PROMOTE -- UNTIL ANDREW NAMES IT. Andrew-direct
  2026-09-11 ~15:0xZ, verbatim: "nobody does any portal promotes until i say so is the takeaway here."
  COMMIT your work; do NOT promote, do NOT push the portal submodule, do NOT merge to DEV or PROD.
BLOCK START FROM BRANCH `wk-amgt_resapp-5-8-portal` IN THE PORTAL REPO and commit onto your OWN portal
  branch. Do NOT commit onto DEV or PROD. Do NOT rebuild the panel, the tabs or the Print header that
  already exist there.
BLOCK NEVER RE-DERIVE A RANKING AT RENDER TIME. Read pre-computed rows. No client-side sort of an
  unranked set, no score computed on load, no scan-then-rank.
BLOCK THE THREE SHAPE DECISIONS ARE ANDREW'S. Do not restore the Model tab; do not make Print a tab;
  do not make the Lead Panel non-persistent.
BLOCK NEVER write device-specific logic into the portal -- DERIVE, don't hardcode.
BLOCK NO cell may claim an EXERCISED outcome REALIZED on the strength of its own artifact. This cell
  makes FWD-15 REACHABLE; a PERSON must still have used it. Grade the DONE WHEN state line, never the
  ACCEPT paragraph. Do not mark FWD-15 REALIZED.
BLOCK NO MONITOR, NO ALARM, NO SNS, NO FRESHNESS CHECKER. Standing moratorium.
BLOCK NO non-ASCII in code, logs or AWS.
BLOCK DO NOT TOUCH infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf. It carries a known
  unresolvable resource reference and two literal ARNs for a deleted table (row C-S49). It is a
  SEPARATE surface with a separate owner and it does not gate this cell.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
THE npx DECOY, measured by the previous worker and reproduced A/B against a sibling checkout (row
    AMGT_RESAPP-Z-W2-S8): the literal `npx tsc` resolves to an UNRELATED npm-registry package in this
    worktree. EVERY criterion below therefore uses `npx --package typescript tsc`. If you see a tsc
    that behaves strangely, this is why -- disambiguate, do not silently swap.
THE ALWAYS-PASSES INSTRUMENT, which is why AC2 and AC3 exist (rows Z-S23 / Z-S24): portal's ROOT
    tsconfig.json is `"files": []` plus `references` only, and plain `--noEmit` does NOT follow project
    references, so it typechecks ZERO FILES and cannot fail. The previous attempt's AC2 was that exact
    invocation. `-b --force` is what actually builds the referenced projects.
comp-routes behaviors: the auth-gated `/api/scoped/*` pattern with the auth-validator-edge
    viewer-request is the precedent the new adapters follow.
comp-blast: APPLICABLE. Run it at Phase 1 on every shared component you touch.
comp-cache: the AMGT/research key namespace was CLEAN at the round-5 cut and the previous attempt
    registered 6 `amgt-lead` keys with 0 type mismatches. Keep it clean.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
portal/src/
lib/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-re-1.lead-panel-recut.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~10/`. A path missing from that block is a path
you are REFUSED on. Refuse a criterion you cannot satisfy as written, report it, file a surprise ROW
(`AMGT_RESAPP-Z-W10-S<k>`) and STOP on that criterion. MINT THE ROW ID FROM A RE-READ of the channel
file, never from recall.
NOTE: `portal/` is its own git repo with its OWN object store. Address it explicitly (`git -C portal ...`)
and return to the workspace root when the task ends -- a lingering portal CWD silently substitutes the
WRONG repo's history into evidence pulls, with no error. Check `git rev-parse -q --verify MERGE_HEAD` in
the WORKSPACE root before each commit there and wait if a merge is open.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-re-1"><invocation>cd portal &amp;&amp; timeout 110 npx --package typescript tsc -b --force --pretty false 2>&amp;1 | tail -5</invocation><expect>zero TypeScript error lines from a FULL referenced-project build. Any `error TS` line is NOT met. ⛔ AND A CLEAN RESULT HERE IS NOT EVIDENCE ON ITS OWN: AC2 and AC3 are the controls that prove this instrument can see anything at all, and AC1 without them is exactly the green the previous attempt produced over an ungraded build</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-re-1"><invocation>cd portal &amp;&amp; timeout 110 npx --package typescript tsc -b --force --listFiles --pretty false 2>&amp;1 | grep -c -E "^[A-Za-z]:|^/"</invocation><expect>a printed integer STRICTLY GREATER THAN ZERO -- the number of source files the compiler actually examined. ⛔ ZERO IS THE EXACT DEFECT THAT MADE THE PREVIOUS ATTEMPT'S CHECK UNFAILABLE and is NOT met. An empty output, a non-numeric line, or a count that does not include this cell's own `src/pages/SecurityAnalysis/` files is NOT met either</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-re-1"><invocation>cd portal &amp;&amp; printf "\nconst __re1_mutant: number = \"not a number\";\n" &gt;&gt; src/pages/SecurityAnalysis/types.ts &amp;&amp; timeout 110 npx --package typescript tsc -b --force --pretty false 2>&amp;1 | grep -c "TS2322"; git checkout -- src/pages/SecurityAnalysis/types.ts</invocation><expect>a count of ONE OR MORE -- the deliberately injected type error IS CAUGHT by the same instrument AC1 uses. ⛔ A COUNT OF ZERO MEANS THE INSTRUMENT IS BLIND IN THE BROKEN WORLD, which is precisely how the previous attempt failed, and is NOT met. The final `git checkout --` MUST restore the file; a criterion that leaves the mutant in the tree is NOT met regardless of its count</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-re-1"><invocation>timeout 110 comp-find "Replica|PlaceholderOnly|__fixtureOnly" portal/src/pages/SecurityAnalysis --limit 20 2>&amp;1 | tail -12</invocation><expect>a printed denominator of files scanned, and ZERO hits -- the render check exercises the REAL route and the REAL Print action, not a stand-in. ⛔ A `Replica` component in the evidence path is the previous attempt's exact defect ("renders fixture components and a PrintTriggerButtonReplica rather than the actual route/action") and is NOT met. A denominator of 0 files scanned is OUT-OF-CORPUS, not a zero, and is NOT met either</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-re-1"><invocation>timeout 110 comp-cache collisions 2>&amp;1 | tail -12</invocation><expect>a printed denominator of portal files scanned, and NO collision among the AMGT/research query keys. Pre-existing collisions on other surfaces (market-performance, model-portfolio, partner-analytics, positioning) are expected and are NOT this cell's. A new key colliding is NOT met; a denominator of 0 files scanned is OUT-OF-CORPUS and is NOT met either</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-re-1" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical): the surface compiles under a FULL referenced-project build.
- **AC2** (mechanical, VACUITY CONTROL): the compiler examined a non-zero number of files. This is the
  criterion the previous attempt lacked, and its absence is why a green meant nothing.
- **AC3** (mechanical, MUTANT CONTROL): the instrument FAILS IN THE BROKEN WORLD. An injected `TS2322`
  must be caught and then reverted.
- **AC4** (mechanical): the evidence surface is the real route and the real action, not a replica.
- **AC5** (mechanical, auto-rule 2): the new query keys do not collide.
- **AC6** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with `status_reason`
  naming `3.0.0_SA_CVO~Z`): are the FOUR named gaps actually closed -- Trending/Breakout CROSSED rather
  than mapped one-to-one, the `/api/scoped/amgt` adapters delivered on the auth-gated pattern, Starred
  FILTERING the producer's order rather than iterating its own, and RankedChart a real time series over
  `axis_date` -- on top of a persistent Lead Panel, three tabs, Print as a header export, and the Model
  tab's figures actually rehomed? And does the page READ pre-computed rankings rather than re-deriving
  any ranking at render time?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>6</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<supersedes>AMGT-rd-8 -- adjudicated FAIL on AMGTrd8-AC4 and AMGTrd8-AC2 by 3.0.0_SA_CVO~Z in ADJUDICATION_v5.md. Transition authorized by 1.0.0_SA_CTO~Z msg 21677 as the round's L10 owner: an adjudicated FAIL is a CONCLUDED ATTEMPT WITH A NEGATIVE VERDICT, so L9 releases the recut and rd-8 does not wait for the slug.</supersedes>

<preflight>
ALL THREE RUN 2026-09-11 ~22:2xZ. None declared-not-applicable; each disposition carries its own
denominator and its own stated blindness rather than a summary that reads clean.

comp-schedule: RUN -- 5 of 5 carriers scanned; REACHED-DENOMINATORS C1=23, C2=7, C3=12, C4=20, C5=334; BLIND ON C4 (SCOPE-GUARD, SEMI-DECIDABLE, 0 of 20 gates answered) and C5 (PROJECT-BLOCKING, NOT-DECIDABLE, 0 of 334 answered), both answer-state PARTIAL_OR_BLIND by the tool's own voice.
  WHAT IT MEANS FOR THIS CELL: this cell DECLARES NO SCHEDULE and touches none. The project's one
  scheduled producer is `AMGT-rd-5`'s chatter axis (`cron(0 10 * * ? *)` UTC) whose terraform is
  EXPLICITLY outside this cell's `<paths>` and is named in a BLOCK bound. The two blind carriers are
  recorded because a decidable-on-3-of-5 result is not a clean scan, and this order does not pretend
  otherwise.

comp-iam: RUN -- 835 call(s) verdicted across 96 mapped role(s): 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD, 11 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE; totals 12 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 31 service(s); BLIND on 266 call(s) in 26 role-UNMAPPED service(s), NOT resource-checked.
  NEITHER flagged row is on this cell's surface -- they are `etfs-reports-reporter` (s3:PutObject on
  an ETFS platinum key) and `opal-assets-mdpf-portal-publisher` (s3:GetObject on
  `opal-data-portal-v2`).
  TWO HOLES THE TOOL PRINTS ABOUT ITSELF, REPEATED HERE RATHER THAN SWALLOWED: the 266 unmapped calls
  are "an honest hole, not a pass", and the 51 GRANTED-BROAD rows are "EXCLUDED, NOT CLEARED -- a
  wildcard grant cannot be falsified by a resource check". So this is NOT a claim that the read path
  is IAM-clean; it is a claim that nothing this cell introduces appears in the flagged set.
  AND THE READ PATH THIS CELL BUILDS IS NOT IN THAT CENSUS AT ALL: the `/api/scoped/amgt` adapters do
  not exist until this cell writes them, so their IAM cannot be verdicted here. Re-run after they
  land. That is a real gap, not a formality.

comp-adversary: RUN -- composed against THIS order (`--no-packet`); complement sources 4 run / 0 deferred-with-reason / 5 declared-excluded; the DECOMPOSITION neighborhood RESOLVED so 36 directory sibling(s) were DEMOTED to a declared exclusion carrying their count; BLIND on the five v1-unwired sources it names (toolgraph independence, comp-axes snapshot rows, comp-blast/comp-trace expansion, comp-pulse warnings, comp-cochange diversity).
  Its freshness read returned `verdict: BEHIND` on a pinned source. This cell does not consume that
  source; it is written down because a BEHIND verdict noticed and not recorded is the same as one
  never run.
</preflight>

### PREFLIGHT (record face)

- **L4-R GATE, BOTH LIMBS, RE-MEASURED AT THE MOMENT OF CUTTING** -- not carried from an earlier tick.
  (a) `prd-signoff.py status AMGT_RESAPP` -> **ADMITTED**, v0.5 @`932d83eb17`, ratified-text SIGNED
  current, brief SIGNED current. (b) `prd/signoff/4.0.0_SA_CRO~Z.json`'s `half_hash`
  `7c533738184fd9fa7668123d...` **EQUALS** the brief half's current hash computed from the PRD bytes via
  `prd_signoff_lib.half_hashes`, compared rather than hardcoded. The stale old-format BASE record
  (`4.0.0_SA_CRO.json`, no `half`, no `half_hash`) is still on disk and is OUT-VOTED, not fixed.
- **CELL ID** `AMGT-re-1` validated against `CELL_ID_RE` before use, with `AMGT-rd-8` as the positive
  control.
- **SLOT** `~10` is fresh: slots `~1`..`~9` are all in use under `deliverables/`, enumerated not assumed.
- **COVERAGE, BY SUBTRACTION:** round 6's declared cell set is `{AMGT-re-1}` = ONE; orders staged
  covering it = ONE; UNCOVERED = zero; EXTRA = zero.
- **THE TWO INSTRUMENT DEFECTS ARE FIXED IN THE CRITERIA, NOT DELEGATED TO THE WORKER.** AC2 and AC3
  did not exist in `rd-8`; they exist because `1.0.0_SA_CTO~Z` made the recut conditional on a bar that
  FAILS IN THE BROKEN WORLD, and because every round-5 cell that PASSED already carried such a clause
  while the one that failed carried none (rows `Z-S23`, `Z-S24`).
- **NOT IN THIS CELL AND DELIBERATELY SO:** the `C-S49` scheduler IAM/resource defect (separate surface,
  REC'd to `4.0.0_SA_CRO~Z`), and the `Z-S16` portal-base coupling (a bound on the eventual PROMOTE, not
  on the cell; Andrew owns the un-park).
