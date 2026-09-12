# AMGT_RESAPP task order -- `AMGT-rf-1` -- THE CROSS, AT THE PRODUCER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rf-1</owned_cells>
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

## 1. THE CELL, inlined in full -- `AMGT-rf-1` (rows W10-S2, serving FWD-15)

**THE CROSS, AT THE PRODUCER.** The lead panel's surface is specified as **Trending/Breakout x
Price/Chatter** -- a CROSS of two INDEPENDENT controls giving FOUR ranking products, not two labels for
two axes. L9 measured what actually happens: `resolve_axis` falls back on **FOUR OF FOUR** calls with
`movement_basis` ABSENT, because **no producer has ever written a `TRENDING_*` or `BREAKOUT_*`
partition**. Only the SUBJECT half (CHATTER, PRICE) exists on the producer plane.

**Make the PRODUCER supply the movement dimension**, so that the four requested combinations are four
real ranking products rather than two partitions wearing four names. Carry `requested` vs `served`
identities visibly on every payload, and **never invent a rank in the browser** -- deriving the
movement dimension on the read side is re-deriving a ranking, which this cell is forbidden to do.

⛔ **THE TWO BRANCHES THE SLUG OFFERS ARE NOT BOTH YOURS.** Row `Z-W10-S2`'s remedy reads *"Make the
existing producer/surface contract supply and validate the movement dimension, **or** obtain an
explicit specification correction before claiming four distinct ranking products."* **THE ISSUER HAS
CHOSEN THE FIRST BRANCH** (decomp s.15e item 2): the four-way cross is what L9 DEMANDED of the previous
attempt and it serves FWD-15, so correcting the specification to a two-way surface would NARROW a
ratified outcome. **You do not get to choose the narrowing either.** If the producer repair proves
infeasible, file a row stating exactly which mechanism blocks it and stop on that clause.

**A STATIC MEMBERSHIP EDIT IN A TEST IS NOT PRODUCER AVAILABILITY.** L9 named this explicitly: patching
`PRODUCER_LANDED_AXES` in a test *"demonstrates code selection, not producer availability"*. The
producers are `lib/research/metrics/chatter_axis.py` and
`integrations/bloomberg/research/price_axis_pull.py`, both writing `opal-harvest-security-metrics`.

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

## 2a. TWO THINGS THAT WILL LOOK LIKE BLOCKERS AND ARE NOT

- **The price-axis producer lives under `integrations/bloomberg/`.** That does NOT authorize a
  Bloomberg call. Read `integrations/bloomberg/READ_HERE.md` FIRST if you touch anything there. You are
  changing the PARTITION SHAPE a producer writes, not performing a live pull, and the harvester box is
  not up.
- **The chatter axis is a SCHEDULED producer** (`infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf`,
  `cron(0 10 * * ? *)` UTC). An ad-hoc QA run is PERMITTED and is how you test; the scheduled fire stays
  the acceptance. If your change can deploy, NEVER-2 obliges you to open a ledger entry in
  `org/critical_paths/change_management/` at the start and close it at completion, and the
  `org/critical_paths/.open_deploys/<slug>.json` sentinel must be COMMITTED -- a merely staged sentinel
  is deleted by a forced worktree teardown. Both paths are in your grant for exactly this reason.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/__init__.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
lib/research/metrics/
integrations/bloomberg/research/price_axis_pull.py
infra/aws/terraform/amgt-resapp/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rf-1.the-cross-at-the-producer.md
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
  <criterion id="AC1" cell_refs="AMGT-rf-1"><invocation>timeout 110 python -c "import sys; sys.path.insert(0,'.'); from lib.research.api import scoped_amgt as s; combos=[(m,x) for m in ('trending','breakout') for x in ('price','chatter')]; res=[s.resolve_axis(m,x) for m,x in combos]; served=sum(1 for r in res if r.get('served_axis')==r.get('requested_axis')); print('SERVED_EQ_REQUESTED=%d of %d' % (served,len(combos))); print('LANDED=%s' % sorted(s.PRODUCER_LANDED_AXES))"</invocation><expect>`SERVED_EQ_REQUESTED=4 of 4` -- all four requested combinations resolve to a partition that IS the one requested. ⛔ The measured defect is 4 of 4 FALLING BACK, so any number below 4 is NOT met. ⛔ AND THE PRINTED `LANDED` SET IS THE DISCRIMINATOR: it must contain four crossed values (a TRENDING_* and a BREAKOUT_* form), not the two subject-only values `CHATTER`/`PRICE`. A pass with `LANDED` still reading two values means the read side was taught to stop reporting the fallback rather than the producer being fixed, and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rf-1"><invocation>timeout 110 python -c "import sys; sys.path.insert(0,'.'); from lib.research.api import scoped_amgt as s; bad=[('sideways','chatter'),('trending','volume')]; n=0; [n:=n+1 for _ in ()]; out=[]
for m,x in bad:
    try: out.append((m,x,'ACCEPTED',s.resolve_axis(m,x)))
    except Exception as e: out.append((m,x,'REFUSED',type(e).__name__))
print('REFUSED=%d of %d' % (sum(1 for o in out if o[2]=='REFUSED'), len(bad)))
[print(o) for o in out]"</invocation><expect>`REFUSED=2 of 2` -- the NEGATIVE CONTROL. An unlanded movement (`sideways`) and an unlanded subject (`volume`) must still be REFUSED after the repair. ⛔ If the fix is "accept everything", both of these start passing and AC1 becomes unfailable -- that is the always-passes shape this round exists to eliminate, and `REFUSED` below 2 is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rf-1"><invocation>cp lib/research/api/scoped_amgt.py "$TMPDIR/rf1.pre" 2>/dev/null || cp lib/research/api/scoped_amgt.py /tmp/rf1.pre; printf "\nBROKEN_SENTINEL_RF1 = 1/0\n" &gt;&gt; lib/research/api/scoped_amgt.py; timeout 110 python -m pytest lib/research/api/tests/ -q 2&gt;&amp;1 | tail -3; cp /tmp/rf1.pre lib/research/api/scoped_amgt.py 2&gt;/dev/null || cp "$TMPDIR/rf1.pre" lib/research/api/scoped_amgt.py; cmp -s /tmp/rf1.pre lib/research/api/scoped_amgt.py &amp;&amp; echo RESTORED_BYTE_IDENTICAL || echo RESTORE_FAILED</invocation><expect>the pytest tail shows a FAILURE or COLLECTION ERROR (the deliberately broken sentinel IS caught by the same suite the other criteria rely on), AND the final line reads `RESTORED_BYTE_IDENTICAL`. ⛔ A green pytest run with the sentinel present means the suite cannot see this file at all and is NOT met. ⛔ AND THE RESTORE IS FROM A WORKING-TREE SNAPSHOT, NEVER `git checkout --`: round 6's criterion used the index and destroyed ~90 lines of a worker's uncommitted work while printing its expected number (row `Z-W10-S1`). `RESTORE_FAILED`, or an absent final line, is NOT met regardless of the test result</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rf-1"><invocation>timeout 110 comp-find "movement_basis|requested_axis|served_axis" lib/research portal/src/pages/SecurityAnalysis --limit 20</invocation><expect>a PRINTED DENOMINATOR of files scanned, and the resolution record present on BOTH the library and the surface side -- `requested` and `served` identities are carried visibly to the consumer, not silently collapsed. ⛔ A denominator of 0 files scanned is OUT-OF-CORPUS, NOT a zero, and is NOT met -- note `portal/` is a submodule and the panel lives at `c6728146`, so a census over an unchecked-out portal returns a false zero (decomp s.15e item 1)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rf-1" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR in your proof instance, not a paraphrase.**
A judgment criterion carries `judgment="true"`, no children and NO verdict from you: record it
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~Z`, which grades it at L9.
**`PASS` or `FAIL` on a judgment row is INVALID.**

## 5. WHEN YOU ARE DONE

Write your proof instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~11/AMGT_RESAPP.TO-AMGT-rf-1.the-cross-at-the-producer.proof_of_spec.json`,
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
