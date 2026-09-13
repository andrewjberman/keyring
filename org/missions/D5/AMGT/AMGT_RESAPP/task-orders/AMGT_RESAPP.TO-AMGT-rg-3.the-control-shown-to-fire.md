# AMGT_RESAPP task order -- `AMGT-rg-3` -- THE CONTROL SHOWN TO FIRE -- a negative control nobody has ever made fail

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rg-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~14</issued_to>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**You are `0.9.0_WK_AMGT_RESAPP~14`.** Work ONLY in the worktree whose absolute path is given to you
in your spawn prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`
and `.tools/` exist; if either is absent, STOP with a BLOCKING row -- you are on the wrong base.

**YOU HOLD ONE ORDER.** It is small and it is entirely a measurement.

## 1. THE CELL, inlined in full -- `AMGT-rg-3` (row `AMGT_RESAPP-Z-W11-S5`, serving FWD-14)

**A NEGATIVE CONTROL THAT HAS NEVER BEEN SHOWN TO FAIL IS NOT YET A CONTROL.** Round 7's `rf-3` AC3
reads:

```
m = read_model_block('BABA_US_Equity')
print('POSITIVE=%d WRONG_SCOPE=%d' % (len(_figures(m,'fiscal_year_line_item')), len(_figures(m,'not_a_real_scope_NOPE_xyz'))))
             ->  POSITIVE=183 WRONG_SCOPE=0
```

That output is real and its POSITIVE arm is genuinely non-vacuous -- 183 of the block's 196 figures
matched, so the input is loaded and the matcher is selective. **But nobody has ever run it against a
matcher that SHOULD make the wrong-scope arm non-zero.** `2.0.0_SA_COO~ZZZ` disarmed the row on that
reasoning at `Z-S46`'s predecessor `Z-S40`; **`3.0.0_SA_CVO~Z` REJECTED that closure at L9** --
*"the specifically required loosened-matcher mutant was not run"* -- and the row's own condition says
so in terms. **The CVO is right and this cell exists to pay a one-command debt.**

**DELIVER: the control, SHOWN TO FIRE.** Deliberately loosen the scope matcher so it matches
everything, run the IDENTICAL AC3 invocation, and record that `WRONG_SCOPE` goes NON-ZERO. Then
restore and prove byte identity.

⛔ **AND THE MUTATION MUST BE THE RIGHT ONE. A SCOPE-TOKEN MUTATION AND AN IMPORT SENTINEL ARE
DIFFERENT CONTROLS** -- the row says exactly that. Breaking the import proves the file is loaded;
only loosening the MATCHER proves this criterion can fail. Do not substitute the cheaper one.

⭐ **WHY THIS IS WORTH A CELL RATHER THAN A NOTE:** round 7's whole lesson, in the L10 analysis's
words, is that **every defect it produced was a check run on the near side of a boundary and claimed
for the far side.** This is that at the criterion altitude: a control claimed to discriminate,
exercised only in the world where it agrees.

## 2. WHERE THIS CAME FROM

**ROUND 8**, cut from `1.0.0_SA_CTO~Z`'s L10 round-7 analysis @`65e788455a`, s.5.4: *"`W11-S5`'s owed
mutant is a one-command debt, and the CVO named it precisely. It belongs in the recut or in a
same-tick disarm, not in a third round of adjudication."* It is in the recut.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/checkface/scopes.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rg-3.the-control-shown-to-fire.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). File a row and stop rather than routing
  around it. `deliverables/0.9.0_WK_AMGT_RESAPP~14/` needs no entry -- the tree convention grants it.
- ⛔ **THE PERMANENT STATE OF THOSE TWO MODULES AT THE END OF YOUR RUN IS BYTE-IDENTICAL TO THE
  START.** The mutation is transient and exists only inside AC1's own invocation. **You are not
  repairing anything here** -- if you find yourself wanting to change behaviour, that is a row, not
  this cell.
- **NO AWS ACT, NO DEPLOY, NO PORTAL ACT.** This cell touches neither. Portal stays FROZEN, and do not
  commit the `portal` gitlink -- it stays at `e85f6eb84f`.

### THE MUTATION-CONTROL RULE, AND IT IS THE WHOLE OF THIS CELL

⛔ **A MUTATION CONTROL SNAPSHOTS THE WORKING TREE, NEVER THE INDEX.** `git checkout -- <path>`
restores from the **index** and has destroyed ~90 lines of a worker's uncommitted edits while printing
the expected result (row `AMGT_RESAPP-Z-W10-S1`). **Copy to a scratch snapshot, restore from THAT,
prove byte identity with `cmp`.** A restore that cannot prove byte identity means the criterion is NOT
met however good its count looks. On this cell that rule is not a guard around the work -- it IS the
work.

## 4. PROOF OF SPEC -- one clause per criterion

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rg-3"><invocation>cp lib/research/checkface/scopes.py /tmp/rg3.pre; timeout 110 python -c "import io,re; p='lib/research/checkface/scopes.py'; t=io.open(p,encoding='utf-8').read(); import sys; sys.exit(0 if 'def ' in t else 3)"; timeout 110 python - &lt;&lt;'PY'
import sys; sys.path.insert(0,'.')
from lib.research.api import scoped_amgt as s
m = s.read_model_block('BABA_US_Equity')
orig = s._figures
def loosened(block, scope):
    return list((block or {}).get('figures') or []) if block else []
s._figures = loosened
print('LOOSENED POSITIVE=%d WRONG_SCOPE=%d' % (len(s._figures(m,'fiscal_year_line_item') or []), len(s._figures(m,'not_a_real_scope_NOPE_xyz') or [])))
s._figures = orig
print('RESTORED POSITIVE=%d WRONG_SCOPE=%d' % (len(s._figures(m,'fiscal_year_line_item') or []), len(s._figures(m,'not_a_real_scope_NOPE_xyz') or [])))
PY
cmp -s /tmp/rg3.pre lib/research/checkface/scopes.py &amp;&amp; echo RESTORED_BYTE_IDENTICAL || echo RESTORE_FAILED</invocation><expect>FOUR numbers and the restore line. Under the LOOSENED matcher `WRONG_SCOPE` must be STRICTLY GREATER THAN ZERO -- that is the control FIRING and it is the entire debt this cell pays. Under the RESTORED matcher it must be back to `0` with `POSITIVE` back to its real count. STOP: `WRONG_SCOPE=0` while loosened means the mutation did not reach the matcher the criterion uses, and is NOT met -- try again against the function AC3 actually calls rather than a namesake. STOP: `RESTORE_FAILED` is NOT met. If an in-process monkeypatch cannot reach it, mutate the SOURCE instead, from a working-tree snapshot, and record which route you took verbatim</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rg-3"><invocation>timeout 110 python -c "import sys; sys.path.insert(0,'.'); from lib.research.api import scoped_amgt as s; m=s.read_model_block('BABA_US_Equity'); print('POSITIVE=%d WRONG_SCOPE=%d DENOM=%d' % (len(s._figures(m,'fiscal_year_line_item') or []), len(s._figures(m,'not_a_real_scope_NOPE_xyz') or []), len((m or {}).get('figures') or [])))"</invocation><expect>`POSITIVE=183 WRONG_SCOPE=0 DENOM=196` -- the unmutated world, unchanged by your run, with the DENOMINATOR printed beside both arms so `183 != 196` shows the matcher is selective on the real artifact. STOP: any drift in these three numbers means your restore was incomplete and is NOT met, whatever AC1 printed</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rg-3"><invocation>timeout 110 python -m pytest lib/research/api/tests/ -q 2&gt;&amp;1 | tail -4</invocation><expect>the suite passes with its count PRINTED, against the RESTORED modules. This is the second, independent check that nothing you did persisted: AC2 reads the numbers, this reads the behaviour. STOP: a failure here after a clean AC2 means the mutation escaped into a file the direct read does not cover, and is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rg-3"><invocation>timeout 110 git status --porcelain -- lib/research/api/scoped_amgt.py lib/research/checkface/scopes.py | wc -l</invocation><expect>`0` -- the two modules are byte-identical to their committed state at the end of your run, measured by git rather than by your own snapshot. STOP: ANY non-zero is NOT met, and it is the one outcome this cell exists to make impossible: a control that proves itself by leaving the world changed has not proved anything. This is deliberately a DIFFERENT instrument from AC1's `cmp` -- one compares to a scratch copy you made, this compares to the repository</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rg-3" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** A judgment criterion
carries `judgment="true"`, no children and NO verdict from you: record `UNVERIFIABLE-BY-INSTRUMENT`
with a `status_reason` naming `3.0.0_SA_CVO~Z`. **`PASS`/`FAIL` on a judgment row is INVALID.**

**AND SAY PLAINLY IN YOUR INSTANCE WHAT THIS CELL DOES AND DOES NOT SETTLE:** it settles that rf-3's
AC3 CAN fail. It does not re-grade rf-3, does not change any round-7 disposition, and does not itself
disarm `Z-W11-S5` -- that disarm is `2.0.0_SA_COO~ZZZ`'s act on your evidence, and the CVO may read it
differently again.

## 5. WHEN YOU ARE DONE

Instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~14/AMGT_RESAPP.TO-AMGT-rg-3.the-control-shown-to-fire.proof_of_spec.json`,
graded by **your worktree's own** `.tools/proof-of-spec-check.py` from inside that worktree; flip
`<status>` to `complete`; commit with `--only -- <paths>`. Report once in your final message. **If a
criterion cannot be met, leave the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>8</round>
<slot>~14</slot>
<fabric>site-z</fabric>
<dep_stage>ROUND_CLOSE</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-7 analysis @`65e788455a`, s.5.4: "`W11-S5`'s owed mutant is a one-command debt ... It belongs in the recut or in a same-tick disarm, not in a third round of adjudication." The CVO's rejection of `Z-S40`'s closure is executed here as a ruling, not re-litigated. Cell set and subtraction: decomp s.16a over the NINE OPEN remedy rows of `REMEDIATION_v7.md` @`00e0813b9d`. Fan-out: decomp s.16c.</authority>

<preflight>
ALL THREE RUN 2026-09-13 ~00:2xZ, fresh this tick. None declared-not-applicable; each disposition
carries its own denominator and its own stated blindness.

comp-schedule: RUN -- 5 of 5 carriers scanned within budget (9.969 s of 90 s); REACHED-DENOMINATORS
C1=23, C2=7, C3=12, C4=20, C5=334. C1 SENTINEL, C2 DEPLOY-LEDGER, C3 MORATORIA all DECIDABLE with
every gate POSITIVE_RESULT; BLIND on C4 SCOPE-GUARD (SEMI-DECIDABLE, 0 of 20) and C5
PROJECT-BLOCKING (NOT-DECIDABLE, 0 of 334), both PARTIAL_OR_BLIND by the tool's own voice, plus a
NEEDS-READ prose carrier of 128 more it refuses to count.
  WHAT IT MEANS FOR THIS CELL: nothing here is scheduled and this cell changes no behaviour at all --
  its permanent diff is zero by construction. The blind carriers are recorded because a
  decidable-on-3-of-5 result is not a clean scan.

comp-iam: RUN -- 838 call(s) across 97 mapped role(s): 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51
GRANTED-BROAD, 14 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE; totals 15 missing, 291 deny-present,
1 coverage-unknown, 2 resource-mismatch across 32 service(s); BLIND on 266 call(s) in 26 role-UNMAPPED
service(s), NOT resource-checked.
  THE DENOMINATOR MOVED AND THAT IS ROUND 7's DOING: 835 -> 838 calls, 96 -> 97 roles, after rf-2
  registered the adapter in `infra/aws/lambda/ci/lambda-source-map.json`; comp-iam discovers Lambda
  call sites only through that file, which is why re-running the tool could never have closed row
  `Z-S27` and registering the package did.
  NEITHER flagged row is on this cell's surface. The tool's two self-declared holes are repeated
  rather than swallowed: 266 unmapped calls are "an honest hole, not a pass"; 51 GRANTED-BROAD rows
  are "EXCLUDED, NOT CLEARED". THIS CELL TAKES NO AWS ACT.

comp-adversary: RUN -- composed against the round-8 DECOMPOSITION (`compose <artifact> --no-packet`);
complement sources 4 run / 0 deferred-with-reason / 4 declared-excluded; 230 uncited directory
siblings with the display CAP of 25 declared rather than silent. T11 DID NOT RESOLVE in the tool's own
voice -- the artifact carries no `<decomp_ref>` because it IS the decomposition, so filesystem
adjacency stood as a WEAKER neighborhood and that is recorded as such. Its freshness read returned
`verdict: BEHIND` on a pinned source no cell in this round consumes; recorded because a BEHIND verdict
noticed and not recorded is the same as one never run.
</preflight>
