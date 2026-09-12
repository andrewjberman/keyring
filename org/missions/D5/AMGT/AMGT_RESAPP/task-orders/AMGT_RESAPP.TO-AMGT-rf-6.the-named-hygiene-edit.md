# AMGT_RESAPP task order -- `AMGT-rf-6` -- THE NAMED HYGIENE EDIT -- ten occurrences, six files, INERT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rf-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~12</issued_to>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**You are `0.9.0_WK_AMGT_RESAPP~12`.** Work ONLY in the worktree whose absolute path is given to you
in your spawn prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/` and
`.tools/` exist; if either is absent, STOP with a BLOCKING row -- you are on the wrong base and every
path below resolves to nothing.

**YOU HOLD ONE ORDER.** Its surface is disjoint at FILE grain from the other chain's --
measured: `types.ts` carries zero non-ASCII and the six affected files are all other files.

## 1. THE CELL, inlined in full -- `AMGT-rf-6` (rows W10-S4, serving FWD-15)

**THE NAMED HYGIENE EDIT.** The surface round 6 was told to build on already violates its own
`No non-ASCII in production code` bound. Measured independently by this seat at portal commit
`c6728146` over a denominator of **18 tracked files** under `src/pages/SecurityAnalysis/`: **SIX files
carrying TEN non-ASCII display-punctuation occurrences**, which matches `3.0.0_SA_CVO~Z`'s count exactly.

```
  components/PrintExportAction.tsx    1
  components/ProvenanceLine.tsx       2
  components/SecurityOverlay.tsx      3
  tabs/CoverageTab.tsx                1
  tabs/PeersTab.tsx                   1
  tabs/ThesisTab.tsx                  2
                                     10
```

Replace the ten occurrences with ASCII equivalents, **preserving meaning and component behaviour**.
These six files are unchanged by round 6's recut, so this is a narrow existing-surface edit.

⚠ **THIS ROW IS `INERT` AND THE SCOPE IS EXACTLY THAT.** It is a code-conformance item. It is NOT a
claim about unsafe AWS identifiers and NOT a claim about production text rendering. Do not widen it
into a styling pass, and do not touch `types.ts` -- that file carries ZERO non-ASCII and belongs to
another chain.

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



## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx
portal/src/pages/SecurityAnalysis/components/ProvenanceLine.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/tabs/CoverageTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rf-6.the-named-hygiene-edit.md
</paths>

**`deliverables/0.9.0_WK_AMGT_RESAPP~12/` needs no entry** -- the tree convention grants it. The
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
  <criterion id="AC1" cell_refs="AMGT-rf-6"><invocation>cd portal &amp;&amp; timeout 110 python -c "import io,subprocess; names=[n for n in subprocess.run(['git','ls-tree','-r','--name-only','HEAD','--','src/pages/SecurityAnalysis'],capture_output=True).stdout.decode().split('\n') if n.strip()]; tot=0; bad=[]
for n in names:
    t=io.open(n,encoding='utf-8',errors='replace').read()
    k=sum(1 for c in t if ord(c)>127)
    if k: tot+=k; bad.append((n,k))
print('DENOMINATOR=%d files' % len(names)); print('NONASCII_FILES=%d OCCURRENCES=%d' % (len(bad),tot)); [print(b) for b in bad]"</invocation><expect>`DENOMINATOR` of 18 or more files AND `OCCURRENCES=0`. ⛔ A `DENOMINATOR=0` IS OUT-OF-CORPUS, NOT A CLEAN RESULT, AND IS NOT MET -- this seat's own first census read 0 files because `portal/` is a submodule whose checked-out HEAD does not carry this directory at all, and that false zero would have "proved" the row already clean (decomp s.15e item 1). Verify your portal checkout carries the panel before believing any zero</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rf-6"><invocation>cd portal &amp;&amp; timeout 110 npx --package typescript tsc -b --force --listFiles --pretty false 2&gt;&amp;1 | grep -c -E "^[A-Za-z]:|^/"</invocation><expect>a printed integer STRICTLY GREATER THAN ZERO -- the number of source files the compiler actually examined, which is the VACUITY control. ⛔ ZERO IS THE EXACT DEFECT THAT MADE ROUND 6's PREDECESSOR UNFAILABLE (a references-only root examines no source) and is NOT met. The count must include this cell's own `src/pages/SecurityAnalysis/` files</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rf-6"><invocation>cd portal &amp;&amp; cp src/pages/SecurityAnalysis/tabs/ThesisTab.tsx /tmp/rf6.pre &amp;&amp; printf "\nconst __rf6_mutant: number = \"not a number\";\n" &gt;&gt; src/pages/SecurityAnalysis/tabs/ThesisTab.tsx; timeout 110 npx --package typescript tsc -b --force --pretty false 2&gt;&amp;1 | grep -c "TS2322"; cp /tmp/rf6.pre src/pages/SecurityAnalysis/tabs/ThesisTab.tsx; cmp -s /tmp/rf6.pre src/pages/SecurityAnalysis/tabs/ThesisTab.tsx &amp;&amp; echo RESTORED_BYTE_IDENTICAL || echo RESTORE_FAILED</invocation><expect>a count of ONE OR MORE -- the injected type error IS CAUGHT -- AND a final line reading `RESTORED_BYTE_IDENTICAL`. ⛔ A count of ZERO means the compiler is blind in the broken world and is NOT met. ⛔ AND NOTE WHAT CHANGED FROM ROUND 6: that criterion restored with `git checkout --`, which reads the INDEX, and it destroyed ~90 lines of a worker's uncommitted work while printing its expected `1` (row `Z-W10-S1`). This one snapshots the WORKING TREE and proves byte identity. `RESTORE_FAILED` is NOT met whatever the count</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rf-6" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR in your proof instance, not a paraphrase.**
A judgment criterion carries `judgment="true"`, no children and NO verdict from you: record it
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~Z`, which grades it at L9.
**`PASS` or `FAIL` on a judgment row is INVALID.**

## 5. WHEN YOU ARE DONE

Write your proof instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~12/AMGT_RESAPP.TO-AMGT-rf-6.the-named-hygiene-edit.proof_of_spec.json`,
run **your worktree's own** `.tools/proof-of-spec-check.py` against it **from inside that worktree**
(the main tree's copy grades the tree it lives in and will report `CHECKER-SCOPE` violations that are
not about your instance), flip this file's `<status>` to `complete`, and commit with
`--only -- <paths>`. Report once in your final message.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>7</round>
<slot>~12</slot>
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
