# AMGT_RESAPP task order -- `AMGT-rg-2` -- THE INCOMPLETE READ AT THE CHART -- two different worlds render byte-identical

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rg-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~13</issued_to>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**You are `0.9.0_WK_AMGT_RESAPP~13`.** This is the SECOND order of your queue; `rg-1` comes first.
Work ONLY in the worktree whose absolute path is given to you in your spawn prompt.

⛔ **THE PORTAL IDENTITY PROBE FROM `rg-1` APPLIES HERE TOO** -- `git -C portal rev-parse
--show-toplevel` must print the portal path, not the superproject root. An unmaterialized portal
answers from the superproject with a real hash and a real branch name and never fails (row
`AMGT_RESAPP-Z-W12-S1`).

## 1. THE CELL, inlined in full -- `AMGT-rg-2` (row `C-S98`, serving FWD-14)

**THE CHART RENDERS THE SAME PIXELS FOR "THERE IS NO DATA" AND "WE TRIED AND GAVE UP", AND ROUND 7
BUILT THE SIGNAL IT IGNORES.** `3.0.0_SA_CVO~Z` measured the real component at portal `83cc87f2`:

```
RankedChart( absent payload )          ->  static HTML  H
RankedChart( retry-exhausted payload ) ->  static HTML  H     BYTE-IDENTICAL
reads:   points, point_count
ignores: read_completeness, unresolved_point_count
both payloads describe zero landed days
```

Round 7's `rf-5` delivered exactly the distinction the page throws away: a bounded incomplete-read
signal with `read_completeness` and an unresolved denominator, four batch response shapes, and a
105-key mixed case returning all 105 points. **The backend now preserves it and the chart discards
it.**

**DELIVER: the chart CARRIES the incomplete read -- rendering it with its unresolved denominator, or
REFUSING with it -- so that `absent`, `partial` and `retry-exhausted` produce DISTINGUISHABLE output.**

⛔ **"DISTINGUISHABLE" IS THE WHOLE CRITERION AND IT IS MEASURED AS A BYTE COMPARISON.** Three
payloads, three outputs, no two identical. A version that renders a spinner for all three has not
moved this row.

⛔ **PRESERVE PRODUCER ORDERING.** The row says so. Do not re-sort or re-key the series to make a
render easier -- the producer's order is the contract, and `rg-1`'s lesson is that the consumer is
what bends.

## 2. WHERE THIS CAME FROM

**ROUND 8**, cut from `1.0.0_SA_CTO~Z`'s L10 round-7 analysis @`65e788455a`. Analysis s.5.1: **"The
consumer boundary is the round's centre of gravity, not another producer repair. `C-S99` and `C-S98`
are both *populated-consumer* defects. A cell that repairs the producer again cannot move either."**

⭐ **THE CLASS, stated once because your criteria inherit its shape:** *EVERY DEFECT ROUND 7 PRODUCED
IS A CHECK RUN ON THE NEAR SIDE OF A BOUNDARY AND CLAIMED FOR THE FAR SIDE.* The adapter's tests are
the near side. **Every mechanical criterion below runs the COMPONENT.**

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rg-2.the-incomplete-read-at-the-chart.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). File a row and stop on the clause rather
  than routing around it. `deliverables/0.9.0_WK_AMGT_RESAPP~13/` needs no entry.
- ⛔ **PORTAL FROZEN BOTH FABRICS: COMMIT YES / PROMOTE NO.** Commit inside `portal/` on your own
  portal branch; **no push, no fetch from origin, no merge to DEV or PROD.**
- ⛔⛔ **DO NOT COMMIT THE `portal` GITLINK IN THE SUPERPROJECT.** It stays at `e85f6eb84f`. Moving it
  forced a backout at `275530053c`, because the object is reachable from no portal remote ref and a
  superproject merge carries a bare object id without validating it.
- **EVERY INVOCATION IS BOUNDED AND THE TIMEOUT IS RECORDED AS THE OUTPUT.** Keep it that way.

### THE MUTATION-CONTROL RULE

⛔ **A MUTATION CONTROL SNAPSHOTS THE WORKING TREE, NEVER THE INDEX.** `git checkout -- <path>`
restores from the index and once destroyed ~90 lines of a worker's uncommitted work while printing the
expected number (row `AMGT_RESAPP-Z-W10-S1`). Snapshot to scratch, restore from THAT, prove byte
identity with `cmp`.

## 4. PROOF OF SPEC -- one clause per criterion

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rg-2"><invocation>cd portal &amp;&amp; timeout 110 npx vitest run src/pages/SecurityAnalysis --reporter=basic 2&gt;&amp;1 | tail -20</invocation><expect>a test you ADD that renders the REAL `RankedChart` against THREE payloads -- `absent`, `partial`, `retry-exhausted` -- and asserts the three rendered outputs are PAIRWISE DISTINCT, with the three lengths or hashes PRINTED. STOP: any two identical is the measured defect and is NOT met. STOP: AND A SPINNER FOR ALL THREE IS NOT MET EITHER -- distinctness must come from the completeness signal, so at least the `retry-exhausted` case must name its unresolved denominator in the output</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rg-2"><invocation>cd portal &amp;&amp; timeout 110 npx --package typescript tsc -b --force --listFiles --pretty false 2&gt;&amp;1 | grep -c -E "^[A-Za-z]:|^/"</invocation><expect>a printed integer STRICTLY GREATER THAN 1000 and no `error TS` lines. STOP: a small number or 0 is the VACUITY defect round 6 shipped -- a references-only root examined ZERO files and could not fail -- and is NOT met. Record the tail verbatim beside the count</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rg-2"><invocation>cd portal &amp;&amp; timeout 110 grep -c -E "read_completeness|unresolved_point_count" src/pages/SecurityAnalysis/*.tsx src/pages/SecurityAnalysis/**/*.tsx 2&gt;/dev/null | awk -F: '{s+=$2} END {print "COMPLETENESS_REFS=" s}'</invocation><expect>`COMPLETENESS_REFS` STRICTLY GREATER THAN ZERO -- the component now READS the fields it ignored. STOP: 0 is the exact measured defect (`it reads points and point_count but never read_completeness or unresolved_point_count`) and is NOT met. This criterion is DELIBERATELY NOT SUFFICIENT and you should say so in your instance: a reference is not a rendering, and AC1 is what proves the behaviour. Record both readings</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rg-2"><invocation>cd portal &amp;&amp; ls src/pages/SecurityAnalysis/RankedChart.tsx &gt; /dev/null 2&gt;&amp;1 &amp;&amp; cp src/pages/SecurityAnalysis/RankedChart.tsx /tmp/rg2.pre &amp;&amp; printf "\nexport const BROKEN_SENTINEL_RG2: number = \"x\";\n" &gt;&gt; src/pages/SecurityAnalysis/RankedChart.tsx; timeout 110 npx --package typescript tsc -b --force --pretty false 2&gt;&amp;1 | grep -c "error TS"; cp /tmp/rg2.pre src/pages/SecurityAnalysis/RankedChart.tsx; cmp -s /tmp/rg2.pre src/pages/SecurityAnalysis/RankedChart.tsx &amp;&amp; echo RESTORED_BYTE_IDENTICAL || echo RESTORE_FAILED</invocation><expect>the error count STRICTLY GREATER THAN ZERO while the sentinel is present, AND the final line `RESTORED_BYTE_IDENTICAL`. STOP: a ZERO count means AC2's build is BLIND to this file, which would make AC2 unfailable for the very component this cell repairs -- that is the round-6 defect exactly, and is NOT met. If the component lives at a different path, use THAT path and record the substitution verbatim. The restore is from a WORKING-TREE snapshot, never `git checkout --`</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rg-2" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** A judgment criterion
carries `judgment="true"`, no children and NO verdict from you: record `UNVERIFIABLE-BY-INSTRUMENT`
with a `status_reason` naming `3.0.0_SA_CVO~Z`. **`PASS`/`FAIL` on a judgment row is INVALID.**

⛔ **NOTHING YOU PRODUCE MAY BE GRADED `REALIZED`** -- the portal evidence is reachable from 0 of the
portal remote's 9 heads while the recorded gitlink is `e85f6eb84f`. **EXERCISED, never REALIZED**,
until the gitlink lands under Andrew's freeze lift. Say so in your instance.

## 5. WHEN YOU ARE DONE

Instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~13/AMGT_RESAPP.TO-AMGT-rg-2.the-incomplete-read-at-the-chart.proof_of_spec.json`,
graded by **your worktree's own** checker from inside that worktree; flip `<status>` to `complete`;
commit with `--only -- <paths>`. **If a criterion cannot be met, leave the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>8</round>
<slot>~13</slot>
<fabric>site-z</fabric>
<dep_stage>ROUND_CLOSE</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-7 analysis @`65e788455a`, s.5.1: "The consumer boundary is the round's centre of gravity, not another producer repair." Cell set and subtraction: decomp s.16a over the NINE OPEN remedy rows of `REMEDIATION_v7.md` @`00e0813b9d`. Fan-out and why M is 2: decomp s.16c. Drain contract: s.16d.</authority>

<preflight>
ALL THREE RUN 2026-09-13 ~00:2xZ, fresh this tick. None declared-not-applicable; each disposition
carries its own denominator and its own stated blindness.

comp-schedule: RUN -- 5 of 5 carriers scanned within budget (9.969 s of 90 s); REACHED-DENOMINATORS
C1=23, C2=7, C3=12, C4=20, C5=334. C1/C2/C3 DECIDABLE with every gate POSITIVE_RESULT; BLIND on C4
(SEMI-DECIDABLE, 0 of 20 answered) and C5 (NOT-DECIDABLE, 0 of 334), both PARTIAL_OR_BLIND by the
tool's own voice, plus a NEEDS-READ prose carrier of 128 more it refuses to count.
  WHAT IT MEANS FOR THIS CELL: nothing this cell touches is scheduled; round 8 cuts no producer cell.
  The two blind carriers are recorded because a decidable-on-3-of-5 result is not a clean scan.

comp-iam: RUN -- 838 call(s) across 97 mapped role(s): 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51
GRANTED-BROAD, 14 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE; totals 15 missing, 291 deny-present,
1 coverage-unknown, 2 resource-mismatch across 32 service(s); BLIND on 266 call(s) in 26 role-UNMAPPED
service(s).
  THE DENOMINATOR MOVED AND THAT IS ROUND 7's DOING: 835 -> 838 calls, 96 -> 97 roles, because rf-2
  registered the adapter in the source map and comp-iam discovers Lambda call sites only through it.
  NEITHER flagged row is on this cell's surface. The tool's own two holes are repeated rather than
  swallowed: 266 unmapped calls are "an honest hole, not a pass"; 51 GRANTED-BROAD rows are "EXCLUDED,
  NOT CLEARED". THIS CELL TAKES NO AWS ACT, so the tool is context here and not a gate.

comp-adversary: RUN -- composed against the round-8 DECOMPOSITION (`compose <artifact> --no-packet`);
complement sources 4 run / 0 deferred / 4 declared-excluded; 230 uncited directory siblings with the
display CAP of 25 declared rather than silent. T11 DID NOT RESOLVE in the tool's own voice -- the
artifact carries no `<decomp_ref>` because it IS the decomposition, so filesystem adjacency stood as
a WEAKER neighborhood and that is recorded. Freshness returned `verdict: BEHIND` on a pinned source
no cell in this round consumes; written down because a BEHIND verdict noticed and not recorded is the
same as one never run.
</preflight>
