# AMGT_RESAPP task order -- `AMGT-rk-15` -- FWD-18's ONE CHART -- a named series with no numeric points renders nothing and passes every field check

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~23</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~23`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN A, a queue of FIVE orders (`AMGT-rk-1`, `AMGT-rk-8`, `AMGT-rk-12`, `AMGT-rk-15`, `AMGT-rk-16`). Chain A holds EVERY portal edit of the round, so the portal has ONE writer.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~23;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-15` (row `W18-S12`; `FWD-18`; ADDENDUM 4 s.2 (raised as open call U1 by `2.0.0_SA_COO~Z` at the L5 subtraction))

**THE MEASURED STATE.** `FWD-18`'s ACCEPT promises *"one chart, chosen for that company, of the thing it lives or
dies on"*. Measured: the thesis driver chart is **ABSENT 5 of 5** and `thesis_driver` is a **NAMED SERIES WITH NO NUMERIC
POINTS**; segments are carried as prose.

⛔ **THE SHAPE OF THE DEFECT IS THE SAME AS A CONTROL THAT CANNOT ACT.** A named series with no points **satisfies "the field is
populated" and renders nothing.** Every field-presence check passes; the chart is still blank.

**RULED:** the filings analyzer emits the driver as a **NUMERIC SERIES with its points and their units**, not only a name; the
Thesis tab **draws that one chart**; **ABSENT-explicit with a classed reason** where the filing carries no series.

⛔ **THE CRITERION ASSERTS A NONZERO POINT COUNT ON A REAL NAME, NEVER THE PRESENCE OF THE FIELD.** That distinction is the whole
cell.

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. Raised by `2.0.0_SA_COO~Z` in the v1.4 s.20a subtraction over the PRD's outcomes against the served plane -- `W18-S12` occurs ONCE in the whole analysis and ZERO times in any cell -- and RULED by `1.0.0_SA_CTO~Z` at ADDENDUM 4 s.2.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
portal/src/App.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~23/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
lib/research/filings/
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-15.the-one-chart-as-a-numeric-series.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant; this block governs WRITES. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~23 <0.9.0_WK_AMGT_RESAPP~23@opal.agent>" -F <msgfile> -- <paths>`
  (the message file written by a NON-SHELL writer, never a printf or heredoc). Never push, merge, rebase, `checkout --`, `stash`
  or `clean`.


**ISSUER AMENDMENT 1 (2026-09-16 ~07:0xZ, `2.0.0_SA_COO~Z`, issuer).** This block did NOT name THIS ORDER'S OWN
FILE when the round was issued, so the order's final step -- flipping `<status>` to `complete` -- was a write
OUTSIDE the grant and was therefore NOT EXECUTABLE. Found by `0.9.0_WK_AMGT_RESAPP~28` on `AMGT-rk-10`, which did
exactly the right thing: it made the edit locally to confirm the gap, **REVERTED IT BYTE-FOR-BYTE**, and filed row
`AMGT_RESAPP-Z-W28-S1` rather than overriding its own `<paths>`. Measured across the round: **16 of 16 round-12
orders carried the defect and 0 of 13 round-11 orders did** -- the issuer's generator dropped a line the precedent
it was built from already had. The own-file entry is ADDED above. **NOTHING ELSE IN THE GRANT MOVES:** no new
surface, no widened directory, no change to any criterion, bound or cell text.


**ISSUER AMENDMENT 2 (2026-09-16 ~07:4xZ, `2.0.0_SA_COO~Z`, issuer) -- THE ROUTE SHAPE WAS WRONG AND THE
CRITERION COULD NOT PASS.** The invocation named a bare `rawPath` with no `/api/scoped/amgt` prefix and no
edge header, so the deployed router refused it **404 "not an /api/scoped/amgt route"** BEFORE ANY CELL LOGIC
RAN. Adding the prefix alone returns **401 "missing edge-injected X-Firm-Id"**. Measured at this cut, the
shape that actually reaches the route is **the prefix PLUS an `x-firm-id` header -> 200**. ⛔ **A criterion
that 404s before the logic runs cannot discriminate a working route from a broken one -- it is the mirror of
a criterion that cannot fail: THIS ONE COULD NOT PASS.** The property asserted is UNCHANGED; only the object
it is asserted against is corrected. Found by the issuer's dry run after `0.9.0_WK_AMGT_RESAPP~24` and `~26`
each refused their own as written and filed rows (`W24-*`, `W26-S3`).

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO. Andrew's "No portal promote necessary" removes the PROD promote from the
goal's definition of done; it does NOT license a promote and does NOT lift the freeze. **THE PORTAL DEV PUSH IS RESERVED** under
LD-0367/0368 and is NOT taken by any cell -- a shared branch moves only by `0.0.0_AB_MSTR~Z` on Andrew's word at the terminal.
**COLLECTION STAYS OFF:** three Windows tasks are DISABLED over a SEVEN-BODY article pool, and that is the measured consequence of
a RESERVED decision, not a defect to fix; no cell enables collection (@`9db2a36cdc`). **NO alarm, monitor, SNS/SES-send,
notification or freshness checker** -- standing moratorium; a wired queue is not a monitor. The ETF plane is READ-ONLY. Secrets
through `comp-secrets` only. **The one authorized Lusha enrich stays UNUSED** under the documented contract and contact data is
never stored. **No vendor call beyond what this order names**, and availability is never authorization. No non-ASCII in anything
you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired,
widened, or satisfied by a route this order did not name. **A count bar is read from the LIVE STORE AT THE CUT and PRINTS its
denominator** -- the honest denominators today are 7 article bodies over 3 names, 3 covered model-block keys of 89 coverage / 256
universe (plus NVDA, not covered), 5 filings/drafting pilot names, 33 peers objects with 10 carrying members, 2 posture keys.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W23-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it) and never
edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING** -- never halt to investigate.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

**ISSUER AMENDMENT 6 (2026-09-16 ~15:2xZ, 2.0.0_SA_COO~Z).** AC1 and AC3 are RE-CUT; AC2 is UNCHANGED. Nothing else in this order moves.
- **AC1** read `name`, `units`, `points` and `absent_reason` under `thesis_driver`. The served body carries the driver's
  `series` and `unit` there, and its `status` and `reason` in a sibling `thesis_driver_chart`. It now reads both carriers
  and prints which one carries the points. **A named series with 0 points is NOT met whatever the reason says**; the
  absent branch is only for a filing that names no series.
- **AC3 raised NameError before printing anything:** a bare double quote ended the shell string early. Fixed with chr.
Found by running the queued orders' criteria before any worker reached them (row `AMGT_RESAPP-Z-S121`).

**ISSUER AMENDMENT 8 (2026-09-16 ~15:5xZ, 2.0.0_SA_COO~Z).** AC1 is MOVED to `AMGT-rk-7` AC5 (it keeps `cell_refs="AMGT-rk-15"`), and the grant NARROWS: `lib/research/api/scoped_amgt.py` is removed. AC2 and AC3 are UNCHANGED.
- The chart is computed in the adapter and served by a deploy, and both are chain B's. Your halves: the filings analyzer emits the
  driver as a NUMERIC SERIES with points and units, or a classed absence (AC3), and the Thesis tab draws that chart (AC2). Row
  `AMGT_RESAPP-Z-S127`, under ruling row `AMGT_RESAPP-Z-S124`.

**ISSUER AMENDMENT 16 (2026-09-16 ~20:1xZ, 2.0.0_SA_COO~Z, issuer) -- AC2's TWO PAGE BARS ALREADY PASSED, AND THE ONE THAT MATTERED COULD NOT TELL THE POINTS FROM THE
NAME. A NEW AC4 GRADES THE POINTS ON THE SERVED BODY, AND THE `BA_US_Equity` RE-RUN LANDS HERE.**
- **THE DEFECT.** AC2 barred `driver-chart-refs` and `points-consumed` each at least 1. Measured on chain A's own
  portal branch `wk-amgt_resapp-12-23-portal` @`2453a7b4`, BEFORE any work: **8 and 7.** The chart COMPONENT is
  already built and the page already reads the series by NAME. **And `points-consumed` summed `thesis_driver` with
  `driver.points`, where `driver.points` reads 0 and `thesis_driver` reads 7** -- so the bar could not distinguish
  a page that reads the POINTS from one that reads only the NAME, which is the exact distinction its own expect
  demanded (*"A chart component that reads only the series NAME is NOT met"*). Only `absent-reason-rendered`,
  at 0, discriminated.
- **THE REPAIR, in two halves.** AC2 keeps the ONE page bar that is real -- the classed reason must be RENDERED --
  and demotes the rest to `CONTEXT-*`. **The points half moves to where it is actually true: the SERVED BODY.**
- **AC4 IS NEW AND IT IS THE CELL IN ONE READING.** Measured at this amendment on the deployed adapter,
  `GET /security/BA_US_Equity/thesis` 200: `thesis_driver_chart.driver_series` and `.driver_unit` **ALREADY SERVE**
  (the BCA deliveries series, in aircraft per year), `points_count` **0**, `chart_status` **ABSENT**, and
  `chart_reason` says the driver's series **is not one of the model block's 19 fiscal series by exact mnemonic or
  definition.** The name and the unit are there; the numbers are not. That is FWD-18 exactly.
- **AND THE `BA_US_Equity` PILOT RE-RUN IS PLACED HERE, NOT ON `AMGT-rk-18`.** Row `AMGT_RESAPP-Z-S127` asked which
  order carries it; **ANDREW-DIRECT 2026-09-16 ~19:2xZ ("Yes on all four, execute them.") authorizes it**, and the
  answer follows from AC4: the served points cannot change until BA's filings document is regenerated **under THIS
  cell's own producer change**. Running it from `AMGT-rk-18` would spend the vendor call and produce the OLD shape,
  so that order is explicitly told not to. **ONE name, ONE re-run, no cadence.**
- **AC3 IS UNTOUCHED AND WAS DRY-RUN WHOLE AT THIS AMENDMENT, rc=0, discriminating:** `filings-modules 6`,
  `points-emitted 0`, `units-emitted 0`, `absent-reason-emitted 0` -- all three bars fail today, which is the
  correct pre-state for the producer half.
- **NOTHING ELSE MOVES:** no grant path, no bound, no cell text. The grant already carries
  `lib/research/filings/`, and the re-run's world write is `filings/v1/BA_US_Equity/`, which needs no repo grant.

**ISSUER AMENDMENT 19 (2026-09-17 ~04:5xZ, 2.0.0_SA_COO~Z, issuer) -- SECTION 6'S CHECKER INVOCATION STILL NAMED `AC2,AC3`, ORPHANED WHEN AMENDMENT 16 ADDED AC4.**
`.tools/proof-of-spec-check.py`'s `coverage_check` flags an instance row NOT in the given expected-id list as an
UNEXPECTED ADDITION, not a silent pass -- so running the checker with the pre-amendment list against an instance that
correctly carries AC4 would have produced a coverage violation for a criterion that is not only legitimate but the
cell's own reading (`AC4 IS THE CELL IN ONE READING`). Section 6 now names `AC2,AC3,AC4`. No criterion, grant, bound
or cell text moves.

<proof_of_spec>
  <criterion id="AC2" cell_refs="AMGT-rk-15"><invocation>cd portal && python -c "import io,glob,os; fs=sorted(glob.glob('src/pages/SecurityAnalysis/**/*.tsx', recursive=True)); B=dict((f, io.open(f,encoding='utf-8',errors='replace').read()) for f in fs); j=''.join(B.values()); ch=[f for f in fs if 'ThesisDriverChart' in os.path.basename(f)]; cj=''.join(B[f] for f in ch); print('components', len(fs)); print('chart-components', len(ch)); print('absent-reason-rendered', j.count('absent_reason')); print('CONTEXT-chart-points-refs', cj.count('.points')); print('CONTEXT-driver-chart-refs', j.count('ThesisDriverChart')); print('CONTEXT-series-name-refs', j.count('thesis_driver'))"</invocation><expect>components and chart-components printed as denominators, and absent-reason-rendered AT LEAST 1 -- the ONE bar on this clause. ISSUER AMENDMENT 16 demoted the other two: driver-chart-refs and points-consumed were barred at least 1 each and ALREADY READ 8 and 7 on chain A's own portal branch before any work, because the chart COMPONENT IS ALREADY BUILT and the page already reads the series by NAME. Worse, points-consumed summed thesis_driver with driver.points, and driver.points reads 0 while thesis_driver reads 7, so the bar could not tell a page that reads the POINTS from one that reads only the NAME -- which is the precise distinction its own expect demanded. Those counts are retained as CONTEXT-*, PRINTED and NOT BARS, measured at the amendment on wk-amgt_resapp-12-23-portal @2453a7b4: components 19, chart-components 1, absent-reason-rendered 0, CONTEXT-chart-points-refs 2, CONTEXT-driver-chart-refs 8, CONTEXT-series-name-refs 7. The points half is now graded where it is REAL, on the SERVED body, by AC4</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-15"><invocation>python -c "import io,glob; fs=sorted(glob.glob('lib/research/filings/*.py')); j=''.join(io.open(f,encoding='utf-8',errors='replace').read() for f in fs); q=lambda w: j.count(chr(34)+w+chr(34)) + j.count(chr(39)+w+chr(39)); print('filings-modules', len(fs)); print('points-emitted', q('points')); print('units-emitted', q('units')); print('absent-reason-emitted', j.count('absent_reason'))"</invocation><expect>points-emitted, units-emitted and absent-reason-emitted each at least 1 against a printed module denominator -- the PRODUCER emits the numeric series, its units and the classed absence. Repairing only the page while the producer still emits a bare name would move the chart for no name and is NOT met. ISSUER AMENDMENT 6 (2026-09-16 ~15:2xZ, 2.0.0_SA_COO~Z) repaired this invocation's QUOTING: a bare double quote inside the shell's double-quoted python -c string ended the string early, so Python received an undefined name and the criterion raised NameError before printing any bar. The quote characters are now built with chr. At this amendment: 6 modules, points 0, units 0, absent_reason 0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-15"><invocation>python -c "import boto3,json; c=boto3.client('lambda'); b=json.loads(c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':'/api/scoped/amgt/security/BA_US_Equity/thesis','headers':{'x-firm-id':'bd'},'requestContext':{'http':{'method':'GET'}}}).encode())['Payload'].read()); d=json.loads(b.get('body') or '{}'); ch=d.get('thesis_driver_chart') or {}; pts=ch.get('points') or []; print('status', b.get('statusCode')); print('driver_series', str(ch.get('driver_series'))[:80]); print('driver_unit', str(ch.get('driver_unit'))[:60]); print('points_count', len(pts)); print('chart_status', ch.get('status')); print('chart_reason', str(ch.get('reason'))[:120]); print('first_point', json.dumps(pts[0])[:120] if pts else 'NONE')"</invocation><expect>status 200 and points_count NONZERO for BA_US_Equity on the DEPLOYED adapter, with driver_series, driver_unit, chart_status, chart_reason and first_point all printed. THIS IS THE CELL'S OWN WARNING MADE MEASURABLE: the cell says the criterion ASSERTS A NONZERO POINT COUNT ON A REAL NAME, never the presence of the field, and only the served body can say that. Measured at the amendment: status 200, driver_series 'BCA commercial aircraft deliveries (with 737 monthly production rate)', driver_unit 'aircraft delivered per year (and per month)', points_count 0, chart_status ABSENT, chart_reason naming that the driver's series is not one of the model block's 19 fiscal series by exact mnemonic or definition. SO THE NAME AND THE UNIT ALREADY SERVE AND THE POINTS DO NOT, which is the whole cell in one reading. ISSUER AMENDMENT 16 ALSO PLACES THE `BA_US_Equity` PILOT RE-RUN HERE, per row AMGT_RESAPP-Z-S127 and ANDREW-DIRECT 2026-09-16 ~19:2xZ which authorizes it: this clause cannot pass until BA's filings document is regenerated UNDER YOUR OWN producer change, so the re-run is yours and AMGT-rk-18 is told not to take it. ONE name, ONE re-run, no cadence. A points_count still 0 with an unchanged chart_reason is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~23/AMGT_RESAPP.TO-AMGT-rk-15.the-one-chart-as-a-numeric-series.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>12</round>
<slot>~23</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- C-FILINGS-ANALYZER and FWD-18. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-15`, CHAIN A, a queue of FIVE orders (`AMGT-rk-1`, `AMGT-rk-8`, `AMGT-rk-12`, `AMGT-rk-15`, `AMGT-rk-16`). Chain A holds EVERY portal edit of the round, so the portal has ONE writer). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

<preflight>
ALL RUN 2026-09-16 05:2x-05:3xZ at this cut (decomposition v1.6 s.20g).
comp-schedule: RUN -- 5 of 5 carriers within budget (16.25 s of 90); REACHED-DENOMINATORS C1=23, C2=7, C3=12, C4=21, C5=334; GATES ARMED 0 for this scope; C3 = 12 standing NEVER clauses (no alarm, no monitor, no freshness checker -- binding on every cell of this round); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (stats + service) -- 214 roles, 190 services, 1114 operations, 321 permission gaps; 478 .tf across 3 trees; 407 policy blocks attached, 27 NOT ATTACHED, 13 standalone. THE INSTRUMENT IS BLIND WHERE AMGT-rk-2 NEEDS IT: `comp-iam service opal-amgt-scoped-api` returns 3 operations, ALL UNRESOLVED-RESOURCE, and NO S3 row at all; the tool's own banner says the operation list is a FLOOR and never a deletion warrant. The round's one IAM delta is AMGT-rk-2's derived/model_block/ READ, and its never-widen co-sign reads the Terraform DIRECTLY rather than resting on this tool's silence.
comp-adversary: RUN (compose on the decomposition) -- 59 commit pins attempted, 58 verified, 1 UNVERIFIABLE (@9aef3734, inherited from an earlier section, not minted by s.20); 11 repo paths, 10 stable, 1 flagged; 15 file:line cites; 14 tool mentions; 26 hex runs not parsed as pins (named); 596 of 608 uncited siblings NOT digested (budget), 0 non-text. The round's adversarial surfaces are unchanged from round 11: filing text, vendor responses and pool objects are DATA inside a model prompt, never instructions; Posture is marked machine and read by no trade consumer.
comp-routes: RUN (stats) -- 7 origins, 29 behaviors, 14 rewrites, 22 API GW routes, 163 frontend endpoints (66 with URLs), 24 component bindings, 66 resolved; 50 of 66 edge auth, 24 of 66 API-GW auth. NONE of the 24 component bindings is a SecurityAnalysis component -- an INDEPENDENT corroboration of G1 on a different instrument from 4.0.0_SA_CRO~Z's git read.
comp-cache: RUN (collisions) -- 646 of 646 portal source files, 120 of 120 useQuery call sites captured, 0 unparseable, 17 shared keys, 0 TYPE MISMATCH. No cell of this round inherits a cache-key collision.
comp-blast: DECLARED-NOT-APPLICABLE -- the round's one live move is AMGT-rk-2's adapter redeploy and its derived/model_block/ grant, covered by a fresh never-widen co-sign, which is the narrower and correct instrument.
BATTERY LIMIT, STATED: comp-iam and comp-routes are DESIRED-plane (parsed Terraform and committed source) and cannot tell a declared grant or behaviour from a deployed one. Every bar in this round that asserts a grant or a route is graded on a LIVE READ or an INVOKE, never on a battery figure.
</preflight>
