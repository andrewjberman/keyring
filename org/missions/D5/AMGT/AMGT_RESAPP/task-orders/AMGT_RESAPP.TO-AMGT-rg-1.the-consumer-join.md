# AMGT_RESAPP task order -- `AMGT-rg-1` -- THE CONSUMER JOIN -- the page reads 0 of 183 figures

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~13</issued_to>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**You are `0.9.0_WK_AMGT_RESAPP~13`.** Work ONLY in the worktree whose absolute path is given to you
in your spawn prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`
and `.tools/` exist; if either is absent, STOP with a BLOCKING row -- you are on the wrong base.

⛔ **AND YOUR SECOND ACT IS A PORTAL IDENTITY PROBE, because a previous worker was silently lied to
by one.** `git -C portal <cmd>` in an UNMATERIALIZED portal directory does not fail -- git walks UP
and answers **from the superproject**, with a real hash and a real branch name. Run:

```
git -C portal rev-parse --show-toplevel
```

It MUST print the portal path itself. If it prints the superproject root, portal is not materialized
and every `portal/` path below resolves to nothing -- STOP with a BLOCKING row. (Row
`AMGT_RESAPP-Z-W12-S1`. Your spawn has already materialized portal and printed this probe with both
controls; this is your own confirmation, not a substitute for it.)

⚠ **YOU HOLD A QUEUE OF TWO ORDERS AND THIS IS THE FIRST.** `rg-1` then `rg-2`. Both write
`portal/src/pages/SecurityAnalysis/`. They are ONE CHAIN and one worker's queue **not because they
share a file -- they do not -- but because A GITLINK HAS NO SUB-PATH GRAIN** (row
`AMGT_RESAPP-Z-S33`): two workers in one submodule are one contended object, and the second drain
would silently revert the first.

## 1. THE CELL, inlined in full -- `AMGT-rg-1` (row `C-S99`, serving FWD-14/FWD-15)

**THE PAGE CANNOT READ WHAT THE BACKEND NOW EMITS, AND THE JOIN IS NOT FLAKY -- IT IS ARITHMETIC.**
Round 7 repaired the producer: 196 figures resolve, 183 of them `fiscal_year_line_item`, ten fiscal
prices corrected with provenance, an unresolved control that REFUSES. Then `3.0.0_SA_CVO~Z` measured
the consumer at portal `83cc87f2` and found:

```
CONSUMER  checkFor:  figure.fiscal_year != null ? `fy${figure.fiscal_year}:${figure.mnemonic}`
                                                : `header:${figure.mnemonic}`
PRODUCER  emits:     fiscal_year_line_item:PX_LAST:2025
RESULT    header: agrees on both sides  ->  13 of 13 header checks JOIN
          nothing on the producer side ever emits fy<year>:  ->  0 of 183 fiscal checks join
          the unresolved-price control also matches 0 of 1
```

⭐ **AND THE PRODUCER KNEW THE NAME HAD TWO FORMS.** `lib/research/checkface/scopes.py` exists
*specifically* to pin it -- its own docstring reads *"whose scope was `fiscal_year`; the producer
writes `fiscal_year_line_item`."* **A canonical name was established on one side of a boundary and
nothing carried it across.** That is this cell.

**DELIVER: the consumer join repaired to the CANONICAL figure identity shared with the check-face
producer.** Read the identity from the producer's own module rather than re-deriving it.

⛔ **DO NOT REWRITE CANONICAL ARTIFACT IDS TO SUIT THE CONSUMER.** The row says so in terms. The
producer's identity is the contract; the page is what is wrong.

⛔ **AND THE REFUSE PRESENTATION MUST SURVIVE.** The unresolved-price control currently joins 0 of 1
-- after the repair it must join AND still render as a REFUSAL, not as a value. A repair that makes
183 rows appear and quietly turns the refusal into a number has replaced one defect with a worse one.

## 2. WHERE THIS CAME FROM

This is **ROUND 8**, cut from `1.0.0_SA_CTO~Z`'s L10 round-7 analysis @`65e788455a`, which closes:
*"NO PRD ADDENDUM IS REQUIRED -- the coverage read is CLEAN ... the recut proceeds from it in ONE
issuance."* Round 7's six cells are all terminal and 43 of 43 orders on this project are terminal.

⭐ **THE ROUND'S OWN LESSON, which is why your criteria look the way they do.** The analysis names one
defect class at three altitudes: **EVERY DEFECT ROUND 7 PRODUCED IS A CHECK RUN ON THE NEAR SIDE OF A
BOUNDARY AND CLAIMED FOR THE FAR SIDE.** The producer's 107 passing tests are the near side; the page
reading 0 of 183 figures is the far side. **So a criterion here that exercises the adapter proves
nothing about this cell** -- every mechanical criterion below runs against the COMPONENT.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
lib/research/checkface/scopes.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rg-1.the-consumer-join.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** You are admitted to exactly those paths and nothing
  else (RULING 1). Do not route around a missing path; file a row and stop on that clause. Your
  `deliverables/0.9.0_WK_AMGT_RESAPP~13/` home needs no entry -- the tree convention grants it.
- `lib/research/checkface/scopes.py` is granted **READ-FIRST**: it is the producer's identity contract
  and you take the canonical form FROM it. Edit it only if the canonical identity itself is wrong, and
  say so in a row if you do.
- ⛔ **PORTAL IS FROZEN BOTH FABRICS: COMMIT YES / PROMOTE NO.** Commit inside `portal/` on your own
  portal branch. **DO NOT push portal, do not fetch its origin, do not merge to DEV or PROD.**
- ⛔⛔ **AND DO NOT COMMIT THE `portal` GITLINK IN THE SUPERPROJECT.** It stays at `e85f6eb84f`, which
  is what `origin/SITEZ` publishes. Moving it is what forced a backout at `275530053c`: the object
  would be reachable from NO portal remote ref, and a superproject merge carries a bare object id
  without validating it. Leave ` M portal` exactly where it is.
- **EVERY INVOCATION IS RUN UNDER A TIMEOUT AND THE TIMEOUT IS RECORDED AS THE OUTPUT.** Every
  invocation below is already bounded; keep it that way.

### THE MUTATION-CONTROL RULE, AND IT COST A PEER NINETY LINES

⛔ **A MUTATION CONTROL SNAPSHOTS THE WORKING TREE, NEVER THE INDEX.** `git checkout -- <path>`
restores from the **index** and has destroyed ~90 lines of a worker's uncommitted edits while printing
the expected result (row `AMGT_RESAPP-Z-W10-S1`). **Copy the file to a scratch snapshot, restore from
THAT, and prove byte identity with `cmp`.** A restore that cannot prove byte identity means the
criterion is NOT met however good its count looks.

## 4. PROOF OF SPEC -- one clause per criterion

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rg-1" judgment="true"/>
  <criterion id="AC2" cell_refs="AMGT-rg-1"><invocation>cd portal &amp;&amp; timeout 110 node src/pages/SecurityAnalysis/__harness__/join.harness.mjs 2&gt;&amp;1 | tail -30</invocation><expect>FOUR PRINTED LINES FROM ONE RUN of a harness THIS CELL WRITES at that exact path, driving the REAL check-face join over a fixture of REAL CAPTURED ADAPTER BYTES committed beside it: `REPAIRED fiscal 183/183`, `REPAIRED header 13/13`, and -- IN THE SAME RUN, NOT A SEPARATE ONE -- the NEGATIVE CONTROL arm re-driving the IDENTICAL harness against the PRE-REPAIR figure identity printing `PRE-REPAIR fiscal 0/183`. STOP: THE NEGATIVE CONTROL MUST FIRE OR NOTHING HERE IS MET -- a run that prints only the repaired numbers proves the harness agrees with itself, not that the join was broken and is now fixed. STOP: AND A COUNT WITHOUT ITS DENOMINATOR IS NOT MET -- print `joined/total` on every line, because a repair that joins 183 of 999, or one that shrinks the denominator to 183 so the ratio flatters, is a different bug wearing this one's face. The fixture may be REDUCED from the captured bytes but the TOTALS may not move: 183 fiscal and 13 header are the denominators this criterion grades against</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rg-1"><invocation>cd portal &amp;&amp; timeout 110 node src/pages/SecurityAnalysis/__harness__/join.harness.mjs --unresolved-control 2&gt;&amp;1 | tail -30</invocation><expect>the UNRESOLVED-PRICE row driven through the REPAIRED join, printing `UNRESOLVED joined 1/1` AND `UNRESOLVED renders REFUSAL` AND `raw value absent from render: true`, with the PRE-REPAIR arm printing `UNRESOLVED joined 0/1` in the same run as the firing negative control. STOP: a repair that makes 183 rows appear and turns the refusal into a number is NOT met -- it replaces one defect with a worse one, and the row says the REFUSE presentation must survive. STOP: `raw value absent from render` must be asserted against the RENDERED output by searching it for the raw figure, not inferred from the code path</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rg-1"><invocation>cp lib/research/checkface/scopes.py /tmp/rg1.pre; printf "\nBROKEN_SENTINEL_RG1 = 1/0\n" &gt;&gt; lib/research/checkface/scopes.py; timeout 110 python -c "import sys; sys.path.insert(0,'.'); import lib.research.checkface.scopes" 2&gt;&amp;1 | tail -3; cp /tmp/rg1.pre lib/research/checkface/scopes.py; cmp -s /tmp/rg1.pre lib/research/checkface/scopes.py &amp;&amp; echo RESTORED_BYTE_IDENTICAL || echo RESTORE_FAILED</invocation><expect>the import FAILS with a traceback while the sentinel is present, AND the final line reads `RESTORED_BYTE_IDENTICAL`. This is the control that the canonical identity you read is really the module you think it is: if a broken `scopes.py` imports cleanly, you are reading a different module and every number above is about the wrong object. The restore is from a WORKING-TREE snapshot, never `git checkout --`; `RESTORE_FAILED` is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rg-1" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR in your proof instance, not a paraphrase.**
A judgment criterion carries `judgment="true"`, no children and NO verdict from you: record it
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~Z`, which grades it at L9.
**`PASS` or `FAIL` on a judgment row is INVALID.**

⛔ **AND NOTHING YOU PRODUCE MAY BE GRADED `REALIZED`.** The portal evidence lives at an object
reachable from **0 of the portal remote's 9 heads** while the recorded gitlink is `e85f6eb84f`. Every
portal-dependent outcome of this round grades **EXERCISED**, never REALIZED, until the gitlink lands
-- which needs Andrew's freeze lift and is not this round's to assume. Say so in your instance.

## 5. WHEN YOU ARE DONE

Write your proof instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~13/AMGT_RESAPP.TO-AMGT-rg-1.the-consumer-join.proof_of_spec.json`,
run **your worktree's own** `.tools/proof-of-spec-check.py` against it **from inside that worktree**,
flip this file's `<status>` to `complete`, and commit with `--only -- <paths>`. Report once in your
final message. **If a criterion cannot be met, leave the order OPEN and file a row** -- that is what
the last worker did five times and every one of those rows was accepted.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>8</round>
<slot>~13</slot>
<fabric>site-z</fabric>
<dep_stage>ROUND_CLOSE</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-7 analysis @`65e788455a`: "NO PRD ADDENDUM IS REQUIRED ... the recut proceeds from it in ONE issuance." Cell set and its subtraction: decomp s.16a, over the NINE OPEN remedy rows of `REMEDIATION_v7.md` @`00e0813b9d`. Fan-out and why M is 2: decomp s.16c. Drain contract: s.16d.</authority>

<preflight>
ALL THREE RUN 2026-09-13 ~00:2xZ, fresh this tick. None declared-not-applicable; each disposition
carries its own denominator and its own stated blindness rather than a summary that reads clean.

comp-schedule: RUN -- 5 of 5 carriers scanned within budget (9.969 s of 90 s); REACHED-DENOMINATORS
C1=23, C2=7, C3=12, C4=20, C5=334. C1 SENTINEL, C2 DEPLOY-LEDGER and C3 MORATORIA all DECIDABLE with
every gate POSITIVE_RESULT; BLIND on C4 SCOPE-GUARD (SEMI-DECIDABLE, 0 of 20 gates answered) and C5
PROJECT-BLOCKING (NOT-DECIDABLE, 0 of 334), both answer-state PARTIAL_OR_BLIND by the tool's own
voice, plus a NEEDS-READ prose carrier of 128 more it refuses to count.
  WHAT IT MEANS FOR THIS CELL: nothing this cell touches is scheduled. The project's one scheduled
  producer is the chatter axis and round 8 cuts no producer cell. The two blind carriers are recorded
  because a decidable-on-3-of-5 result is not a clean scan and this order does not pretend otherwise.

comp-iam: RUN -- 838 call(s) verdicted across 97 mapped role(s): 629 UNRESOLVABLE-RESOURCE, 142
GRANTED, 51 GRANTED-BROAD, 14 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE; totals 15 missing, 291
deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 service(s); BLIND on 266 call(s) in 26
role-UNMAPPED service(s), NOT resource-checked.
  THE DENOMINATOR MOVED AND THAT IS ROUND 7's DOING: 835 -> 838 calls and 96 -> 97 roles, because
  rf-2 registered the adapter in `infra/aws/lambda/ci/lambda-source-map.json` and comp-iam discovers
  Lambda call sites only through it. Row `Z-S27` is closed at the source plane by that move.
  NEITHER flagged row is on this cell's surface -- they are `etfs-reports-reporter` and
  `opal-assets-mdpf-portal-publisher`. TWO HOLES THE TOOL PRINTS ABOUT ITSELF, REPEATED RATHER THAN
  SWALLOWED: the 266 unmapped calls are "an honest hole, not a pass", and the 51 GRANTED-BROAD rows
  are "EXCLUDED, NOT CLEARED -- a wildcard grant cannot be falsified by a resource check".
  AND THIS CELL TAKES NO AWS ACT AT ALL, so the tool is preflight context here and not a gate.

comp-adversary: RUN -- composed against the round-8 DECOMPOSITION (`compose <artifact> --no-packet`);
complement sources 4 run / 0 deferred-with-reason / 4 declared-excluded; 230 uncited directory
siblings with the display CAP of 25 declared rather than silent.
  T11 DID NOT RESOLVE and the tool says why in its own voice: the artifact carries no `<decomp_ref>`
  because it IS the decomposition, so filesystem adjacency stood as the neighborhood instead of the
  decomposition graph. That is a WEAKER neighborhood than a task order would get, and it is recorded
  as such. Its freshness read returned `verdict: BEHIND` on a pinned source; no cell in this round
  consumes that source, and it is written down because a BEHIND verdict noticed and not recorded is
  the same as one never run.
</preflight>

### AMENDMENT 2026-09-13T01:2xZ -- `2.0.0_SA_COO~ZZZ`, AC1 ROUTED AND AC2/AC3 RE-INSTRUMENTED

**THIS IS A DEFECT IN THE ORDER, NOT IN THE WORK.** `0.9.0_WK_AMGT_RESAPP~13` ran all three
invocations exactly as written and all three failed for the same reason: **the toolchain they name
cannot execute inside this cell's grant and this estate's egress rule.** Rows `Z-W13-S1` and
`Z-W13-S2` carry it. Measured independently by this seat before amending, with both controls:
`vitest` appears **0 times in `portal/package.json` and 0 times in `bun.lock`**, while `react` reads
1 and a never-used name reads 0 -- so the instrument discriminates and the absence is real.
`node_modules` holds **1 entry**, so `tsc -b` has nothing to build with and the only path to a green
is registry egress plus a write outside `<paths>`.

⛔ **AN ALWAYS-FAILS CRITERION IS EXACTLY AS BROKEN AS AN ALWAYS-PASSES ONE**, and `AC1`'s failure
mode was the sharper of the two: its `0` is **indistinguishable from the references-only vacuity
defect it was written to screen for.** A criterion that returns the defect's own signature when the
instrument never started cannot discriminate, and this seat cut it that way.

**WHAT CHANGED AND WHAT DID NOT.**

- **`AC1` is converted to a JUDGMENT criterion and routed to `3.0.0_SA_CVO~Z` at L9. It is NOT
  deleted.** The typecheck vacuity screen is genuinely UNSATISFIABLE here and **that coverage is
  LOST for this round -- stated, not hidden.** The CVO grades the absence and its reason; this seat
  does not grade it and does not get to call the gap closed.
- **`AC2` and `AC3` keep every bar they carried** -- `183/183` fiscal, `13/13` header, printed
  denominators on every line, and the unresolved-price row still rendering as a REFUSAL rather than
  a value. **Only the instrument moved**, from a test runner this project does not declare to plain
  `node` over a harness this cell writes inside its own granted path.
- **BOTH NOW REQUIRE A FIRING NEGATIVE CONTROL IN THE SAME RUN** -- the pre-repair identity must
  print `0/183` and `0/1`. That is strictly MORE discrimination than the originals had, which is the
  test this amendment must pass: **an amendment that lets a criterion discriminate is a repair; one
  that lowers a bar is laundering.** The evidence already reported may not be restated -- both
  criteria are re-run from scratch in a fresh process.

**`<paths>` IS UNCHANGED AND NEEDS NO WIDENING:** `portal/src/pages/SecurityAnalysis/` already
admits the harness and its fixture. **The portal freeze is unchanged -- COMMIT YES / PROMOTE NO --
and no artifact of this cell may grade a portal-dependent outcome REALIZED.**
