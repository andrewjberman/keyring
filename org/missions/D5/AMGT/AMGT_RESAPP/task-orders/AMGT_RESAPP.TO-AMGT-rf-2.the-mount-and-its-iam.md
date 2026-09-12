# AMGT_RESAPP task order -- `AMGT-rf-2` -- THE MOUNT AND ITS IAM -- a `<paths>` repair, not a code one

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rf-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~11</issued_to>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**You are `0.9.0_WK_AMGT_RESAPP~11`.** Work ONLY in the worktree whose absolute path is given to you
in your spawn prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/` and
`.tools/` exist; if either is absent, STOP with a BLOCKING row -- you are on the wrong base and every
path below resolves to nothing.

⚠ **YOU HOLD A QUEUE OF FIVE ORDERS AND THIS IS ONE OF THEM.** `rf-1` through `rf-5` all write
`lib/research/api/scoped_amgt.py`, so they are ONE CHAIN and one worker's queue by construction -- two
workers on one file is a guaranteed conflict, not merely wasted parallelism. Do them **in the order
you are handed them**; `rf-4` in particular must follow `rf-3`, because the slug states that fixing
the scope filter alone *"would expose stale values"*.

## 1. THE CELL, inlined in full -- `AMGT-rf-2` (rows W10-S3, S27, serving FWD-15)

**THE MOUNT, AND ITS IAM. THIS IS A `<paths>` REPAIR, NOT A CODE ONE.** Eleven route declarations
and a handler already exist in `lib/research/api`. **Round 6's grant OMITTED the infrastructure mount**,
so the adapters are code that cannot be reached: L9 measured *"sixteen local fake-boundary tests pass;
a missing `X-Firm-Id` yields 401 and a body firm cannot replace the header. Those tests do not validate
an edge JWT, deployed origin isolation, handler package or served route."*

Deliver the mount: the API Gateway route, the Lambda declaration, the handler package, the trusted edge
boundary and the IAM. Follow the existing precedent -- `infra/aws/terraform/bd-pipeline/api-gateway.tf`
carries real `/api/scoped/*` `route_key` declarations on an existing API Gateway; that is the pattern,
not a new gateway.

⛔ **AND THIS CELL ALSO CARRIES ROW `Z-S27`, BECAUSE THE SLUG SAYS SO:** *"Coordinate with W10-S3; merely
adding a mount or repeating unchanged totals cannot close the coverage obligation."* `comp-iam` verdicts
CALLS against ROLES, and a library has no role -- so after the adapters landed, a full re-run returned
**byte-for-byte identical totals**, which reads as a clean re-check and is actually proof the instrument
never saw them. **The obligation is to make the adapter call sites and their role binding APPEAR IN THE
INSTRUMENT'S DENOMINATOR, then evaluate action AND resource grants against the actual package and
mount.** Carry an explicit OUT-OF-CORPUS / UNMAPPED marker when a thing genuinely cannot be verdicted.

## 2. WHERE THIS CAME FROM, so you can tell a repair from a rebuild

This is **ROUND 7**. Rounds 5 and 6 are CLOSED at L10 (`ROUND_ANALYSIS.round5.md` @`3c73d946e3`, which
also answers round 6). Round 6 was a single-cell recut of the lead panel (`AMGT-re-1`) and **its AC6
FAILED** at L9 -- the repaired criteria did their job by failing. This cell is one of six repairs cut
from the two slugs `3.0.0_SA_CVO~Z` delivered in commit `bd523222a1`.

⭐ **THE ROUND'S OWN LESSON, which is why your criteria look the way they do:** four projects' worth of
cells converged in one evening on ONE defect class -- **a criterion that cannot fail in the broken
world**. Round 6's predecessor shipped because `tsc --noEmit` against a references-only root examined
ZERO source files and a render check rendered a `PrintTriggerButtonReplica` instead of the route. Both
passed. Neither could fail. **So every mechanical criterion below carries a discriminator inside its
own `<expect>`** -- a negative control, a vacuity count, or a false-zero refusal -- and you should
treat a criterion that cannot fail as a defect worth a row even if it passes you.

## 2a. THE DEPLOY OBLIGATION IS REAL ON THIS CELL

This cell can produce a deploy. NEVER-2 obliges the actor to OPEN a ledger entry in
`org/critical_paths/change_management/` at the start and CLOSE it at completion, and to name in that
entry every task family that pulls any image tag it moves. **The
`org/critical_paths/.open_deploys/<slug>.json` sentinel must be COMMITTED, not merely staged** -- a
staged sentinel is destroyed by a forced worktree teardown, which is how a previous round lost its
ledger. Both paths are in your grant for exactly this reason.
**And the portal promotion freeze stands regardless of what you mount:** COMMIT YES / PROMOTE NO.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/__init__.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/amgt-resapp/
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rf-2.the-mount-and-its-iam.md
infra/aws/lambda/research/scoped_amgt_api/
infra/aws/lambda/ci/lambda-source-map.json
</paths>

**`deliverables/0.9.0_WK_AMGT_RESAPP~11/` needs no entry** -- the tree convention grants it. The
investigation channel IS listed because a row is possible and an unlisted channel is a wall.

### BOUNDS -- what you may NOT do, and these are refusals, not preferences

- **PORTAL IS FROZEN ON BOTH FABRICS, PROD AND DEV: COMMIT YES / PROMOTE NO** until Andrew names it.
  You may commit portal changes on your own portal branch. You may NOT push portal, merge to DEV or
  PROD, or take any act whose effect is a promotion.
- **NO VENDOR API CALL.** The vendor word is NARROW -- Seeking Alpha / FT / Bloomberg / WSJ, this
  project's harvesters only, and **effective only once the harvester box is up, which it is not**.
  Availability is not authorization. If a criterion seems to need a live vendor pull, it does not:
  file a row and stop on that clause.
- **NO CONTACT WITH ADAM MULLER** (C-NO-CONTACT), by any channel, for any reason.
- **YOU MAY NOT GRADE AN EXERCISED OUTCOME REALIZED ON YOUR OWN ARTIFACT.** Grade the DONE WHEN state
  line, never the ACCEPT paragraph.
- **YOU HAVE NO BROKER TOOL AND CANNOT ASK A QUESTION.** If this face is insufficient, that is a
  DEFECT IN THE ORDER: append ONE row to the investigation channel (`spec_asserts` + `world_is`) and
  keep working on what you can. Do not guess at intent.
- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** You are admitted to exactly those paths and nothing
  else (RULING 1). Do not route around a missing path; file a row and stop on that clause.
- **EVERY INVOCATION IS RUN UNDER A TIMEOUT AND THE TIMEOUT IS RECORDED AS THE OUTPUT.** An unbounded
  command does not fail loudly, it produces a criterion whose evidence is the word "timeout". Every
  invocation below is already bounded; keep it that way.

⛔ **AMENDMENT 1, `2.0.0_SA_COO~ZZZ`, 2026-09-12 ~22:2xZ -- TWO PATHS ADDED TO THE GRANT ABOVE, AND
THE DEFECT WAS THIS ORDER'S OWN.** You filed `AMGT_RESAPP-Z-W11-S2` (BLOCKING) reporting that AC1 is
unsatisfiable inside the grant: `comp-iam` discovers Lambda call sites ONLY through
`infra/aws/lambda/ci/lambda-source-map.json`, every handler package in the estate lives under
`infra/aws/lambda/`, and neither was granted -- so the handler package this cell's section 1 orders
you to deliver had nowhere legal to live. **You were right, you were right to stop on the clause
rather than route around it, and the omission is the issuing seat's.** ⭐ The order calls itself *"a
`<paths>` repair, not a code one"* because round 6's grant omitted the infrastructure mount; round
7's grant then omitted the handler package home. **THE REPAIR REPRODUCED ITS OWN DEFECT ONE DIRECTORY
OVER.**

**Added, and deliberately NARROW -- this cell's package home and the one registry file, never all of
`infra/aws/lambda/`:**
```
infra/aws/lambda/research/scoped_amgt_api/
infra/aws/lambda/ci/lambda-source-map.json
```
**WHAT IS UNCHANGED:** every criterion, the cell text, the deploy obligation in section 2a (both
ledger paths were already granted), and the portal freeze. AC2's band clause is NOT amended -- your
row `Z-W11-S3` is the correct handling and `3.0.0_SA_CVO~Z` grades it at L9; do not re-cut your
architecture to satisfy a band label. Nothing here asks you to re-run a criterion that already
passed.

### THE MUTATION-CONTROL RULE, AND IT COST A PEER NINETY LINES

⛔ **A MUTATION CONTROL SNAPSHOTS THE WORKING TREE, NEVER THE INDEX.** Round 6's injected-error
criterion ended in `git checkout -- <path>`, which restores from the **index** -- so it reverted a
worker's ~90 lines of uncommitted edits in that file **while printing the expected `1`**. The output
looked clean. That is row `AMGT_RESAPP-Z-W10-S1` and the correction is `1.0.0_SA_CTO~Z`'s round-5/6
analysis s.4 item 1.
**So every mutation criterion in this order copies the file to a scratch snapshot first, restores
from THAT snapshot, and proves byte identity with `cmp`.** If a restore step cannot prove byte
identity, the criterion is NOT met however good its count looks.

## 4. PROOF OF SPEC -- one clause per criterion

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rf-2"><invocation>timeout 110 comp-iam 2&gt;&amp;1 | grep -c -E "scoped_amgt|lib/research/api"</invocation><expect>a printed integer STRICTLY GREATER THAN ZERO -- the adapter's call sites now APPEAR in `comp-iam`'s own output, which is the exact thing row `Z-S27` says is missing. ⛔ ZERO IS THE MEASURED DEFECT and is NOT met. ⛔ AND UNCHANGED AGGREGATE TOTALS DO NOT SUBSTITUTE: before this cell the same tool returned 835 calls / 96 roles / 12 missing / 291 deny-present with `lib/` and `scoped_amgt` appearing 0 times against a POSITIVE CONTROL of 37 lines naming `infra/aws/lambda/`. A run that reproduces those totals and still shows 0 here is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rf-2"><invocation>timeout 110 comp-find "api/scoped/amgt" infra --limit 20</invocation><expect>a PRINTED DENOMINATOR of files scanned, and at least one `route_key`-bearing declaration in the CONFIG or DEF band under `infra/` -- the route is DECLARED in infrastructure, not only in library code. ⛔ Hits confined to the DOC or TEST band are NOT met: a route named only in prose or a fake is the exact shape that let sixteen tests pass against nothing mounted. A denominator of 0 files scanned is OUT-OF-CORPUS, not a zero, and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rf-2"><invocation>timeout 110 python -m pytest lib/research/api/tests/ -q 2&gt;&amp;1 | tail -4; echo "---"; timeout 60 comp-find "X-Firm-Id" lib/research/api --limit 10 2&gt;&amp;1 | grep -E "DENOMINATOR|hit"</invocation><expect>the suite passes AND the firm-header boundary is present with a printed denominator. ⛔ THIS CRITERION IS DELIBERATELY NOT SUFFICIENT AND YOU SHOULD SAY SO IN YOUR INSTANCE: sixteen passing fake-boundary tests are exactly what round 6 delivered, and L9 called them out because they *"do not validate an edge JWT, deployed origin isolation, handler package or served route"*. Record what these tests DO and DO NOT establish. The SERVED-plane exercise is AC5's judgment, not this instrument's</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rf-2"><invocation>cp lib/research/api/scoped_amgt.py /tmp/rf2.pre; printf "\nBROKEN_SENTINEL_RF2 = 1/0\n" &gt;&gt; lib/research/api/scoped_amgt.py; timeout 110 python -m pytest lib/research/api/tests/ -q 2&gt;&amp;1 | tail -3; cp /tmp/rf2.pre lib/research/api/scoped_amgt.py; cmp -s /tmp/rf2.pre lib/research/api/scoped_amgt.py &amp;&amp; echo RESTORED_BYTE_IDENTICAL || echo RESTORE_FAILED</invocation><expect>the pytest tail shows a FAILURE or COLLECTION ERROR, AND the final line reads `RESTORED_BYTE_IDENTICAL`. ⛔ A green run with the sentinel present means AC3's suite is blind to this file, which would make AC3 unfailable, and is NOT met. The restore is from a WORKING-TREE snapshot, never `git checkout --` (row `Z-W10-S1`); `RESTORE_FAILED` is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rf-2" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR in your proof instance, not a paraphrase.**
A judgment criterion carries `judgment="true"`, no children and NO verdict from you: record it
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~Z`, which grades it at L9.
**`PASS` or `FAIL` on a judgment row is INVALID.**

## 5. WHEN YOU ARE DONE

Write your proof instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~11/AMGT_RESAPP.TO-AMGT-rf-2.the-mount-and-its-iam.proof_of_spec.json`,
run **your worktree's own** `.tools/proof-of-spec-check.py` against it **from inside that worktree**
(the main tree's copy grades the tree it lives in and will report `CHECKER-SCOPE` violations that are
not about your instance), flip this file's `<status>` to `complete`, and commit with
`--only -- <paths>`. Report once in your final message.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>7</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<dep_stage>ROUND_CLOSE</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-5/6 analysis @`3c73d946e3` + @`ac9b2e7e46`, which closes: "Round 5 and round 6 are CLOSED at L10. The PROJECT is not closed. The recut is `2.0.0_SA_COO~ZZZ`'s in ONE issuance AND NOTHING GATES IT." Cell set and its subtraction: decomp s.15a. Fan-out and why M is 2: decomp s.15c.</authority>

<preflight>
ALL THREE RUN 2026-09-12 ~00:2xZ, fresh this tick. None declared-not-applicable; each disposition
carries its own denominator and its own stated blindness rather than a summary that reads clean.

comp-schedule: RUN -- 5 of 5 carriers scanned; REACHED-DENOMINATORS C1=23, C2=7, C3=12, C4=20, C5=334; C1/C2/C3 DECIDABLE with every gate POSITIVE_RESULT; BLIND ON C4 (SCOPE-GUARD, SEMI-DECIDABLE, 0 of 20 gates answered) and C5 (PROJECT-BLOCKING, NOT-DECIDABLE, 0 of 334 answered), both answer-state PARTIAL_OR_BLIND by the tool's own voice.
  WHAT IT MEANS FOR THIS ROUND: the project's one scheduled producer is the chatter axis
  (`infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf`, `cron(0 10 * * ? *)` UTC). `rf-1` and
  `rf-2` are the ONLY cells whose paths reach it, and both carry it explicitly rather than by
  accident. The two blind carriers are recorded because a decidable-on-3-of-5 result is not a clean
  scan and this order does not pretend otherwise. Several carriers' `last-verified` is DERIVED from
  the carrier's last EDIT, which the tool itself labels a WEAK proxy.

comp-iam: RUN -- 835 call(s) verdicted across 96 mapped role(s): 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD, 11 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE; totals 12 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 31 service(s); BLIND on 266 call(s) in 26 role-UNMAPPED service(s), NOT resource-checked; policy-source scan = 3 terraform trees / 472 .tf files.
  NEITHER flagged row is on this round's surface -- they are `etfs-reports-reporter` (s3:PutObject on
  an ETFS platinum key) and `opal-assets-mdpf-portal-publisher` (s3:GetObject on `opal-data-portal-v2`).
  TWO HOLES THE TOOL PRINTS ABOUT ITSELF, REPEATED RATHER THAN SWALLOWED: the 266 unmapped calls are
  "an honest hole, not a pass", and the 51 GRANTED-BROAD rows are "EXCLUDED, NOT CLEARED -- a wildcard
  grant cannot be falsified by a resource check".
  AND THE CENSUS STILL CANNOT SEE THIS PROJECT'S READ ADAPTER, which is row `Z-S27` and is `rf-2`'s
  to close: the totals came back BYTE-FOR-BYTE UNCHANGED after the adapters landed, and over the
  tool's own 992 output lines the strings `lib/` and `scoped_amgt` appear ZERO times against a
  POSITIVE CONTROL of 37 lines naming `infra/aws/lambda/`. An unchanged denominator after adding a
  consumer is proof the instrument never saw the consumer. `rf-2` does not close `Z-S27` by re-running
  this tool; it closes it by making the adapter call sites APPEAR in the denominator.

comp-adversary: RUN -- composed against the round-7 DECOMPOSITION (`compose <artifact> --no-packet`); complement sources 4 run / 0 deferred-with-reason / 4 declared-excluded; 229 uncited directory siblings with the display CAP of 25 declared rather than silent.
  T11 DID NOT RESOLVE and the tool says why in its own voice: the artifact carries no `<decomp_ref>`
  because it IS the decomposition, so filesystem adjacency stood as the neighborhood instead of the
  decomposition graph. That is a WEAKER neighborhood than a task order would get, and it is recorded
  as such.
  Its freshness read returned `verdict: BEHIND` on a pinned source. No cell in this round consumes
  that source; it is written down because a BEHIND verdict noticed and not recorded is the same as
  one never run.
</preflight>
