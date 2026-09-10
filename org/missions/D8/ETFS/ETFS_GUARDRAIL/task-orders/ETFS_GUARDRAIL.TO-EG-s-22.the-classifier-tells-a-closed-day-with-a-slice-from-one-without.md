# TO ETFS_GUARDRAIL.TO-EG-s-22 -- THE CLASSIFIER MUST TELL A CLOSED DAY CARRYING A SLICE FROM A CLOSED DAY CARRYING NOTHING: FWD-4's own instrument returns class A and `continue`s BEFORE it ever looks at whether a slice exists, so the one property this project exists to protect is invisible to the code that checks it

<to_id>ETFS_GUARDRAIL.TO-EG-s-22</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- 0.9.0_WK_ETFS_GUARDRAIL~1, against the face with its criterion tags @`12f16b46f5`. S22-AC1 PASSES BY OUTPUT: `ARMS 7 of 7 PASS` then `EGS22-CLASSIFIER-DISCRIMINATES`, rc=0. S22-AC2 RECORDED as judgment and NOT self-graded, for `3.0.0_SA_CVO` at L9. proof-of-spec-check rc=0 VALID on the UNCHANGED instance (2/2 criteria carry a cell_ref, 1/1 cell reachable, 4 of 4 artifact rows resolving, 1 of 1 surprise resolving). THE DEFECT REPRODUCED FIRST, before any edit: against the pre-change classifier pinned at `c866edd324`, a closed day carrying a real 1209-byte slice (sha256 `09ca15d4...`, 4 PRICED rows, `source_as_of 2026-09-07`, fetched live) and a closed day carrying nothing returned the BYTE-IDENTICAL record with 0 keys naming the slice. THE SHAPE IS A FIELD, `slice_on_closed_day` (bool) on the class-A record, chosen on rule 24 (iii)/(iv) rather than on cost: the class axis answers whether a day is a hole and why, and whether an artifact turned up is an ORTHOGONAL fact about a different actor with a different remedy owner (PRD v0.6 row `S20`). `_CLASS_NAMES` is untouched, so no four-postulate record and no token census are owed and the arithmetic trap cannot fire -- PROVEN by arm (e) at 27 partner-day records across 3 of 3 partners with 0 counts moved and `trading_days`/`holes` identical on both sides. TWO PERMANENT REGRESSION ARMS added to the estate's own suite (8 -> 10 passed, 0 failed both sides); they are controls, not constants, because both assert `with_slice != without`, which arm (a) measured byte-identical on the old code. DEPLOYED != BUILT (10,157 B `23c30889...` vs 12,226 B `b2ab67fd...`, CRLF 0 in both), and the deployed bytes hash EQUAL to the pre-change blob -- the box is reading exactly the un-fixed classifier and the served verdict cannot discriminate until someone deploys these bytes; carried to `1.0.0_SA_CTO` for L10 placement with an owner. THIS CELL DEPLOYED NOTHING, touched no producer (row `S20` untouched: detection, not prevention), constructed 0 SES clients and invoked 0 Lambdas (arm (g), proven from the run), and wrote nothing to S3. Row `W1-S32` (the face's missing criterion tags) is DISARMED by the issuer at `12f16b46f5`; census by subtraction returned 22 of 23 faces already carrying theirs, blast radius one.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.6, row `S19` | **Decomp cell:** `EG-s-22` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.4, s.13) | **outcome_ref:** FWD-4

---

## THE CELL

`data/etfs/scripts/coverage/classifier.py` is the instrument FWD-4 names, and it cannot see FWD-4's violation.

Read the branch yourself before you change anything. At `classify_month`, the loop opens:

```
if not tcal.is_trading_day(d):
    result[date_str] = {"class": "A", "reason": "market closed (not a trading day)",
                         "probe": None}
    continue

if date_str in series:
    result[date_str] = {"class": "COVERED", "reason": "slice exists", "probe": None}
    continue
```

`classifier.py:122-125` @`c866edd324`, ahead of the presence check at `:128`. The function's own docstring
says *"only PRESENCE of a key matters here, not its contents"* -- and PRESENCE is the exact check the class-A
branch returns before reaching. A closed day carrying a slice and a closed day carrying nothing produce the
BYTE-IDENTICAL record: `{"class": "A", "reason": "market closed (not a trading day)", "probe": None}`.

That is not hypothetical. `daily/inflection/2026-09-07.json` holds **four PRICED rows on a US market holiday**,
`LastModified 2026-09-07T15:00:41Z`, `value-sha 41d1124f75c3` identical to 09-05, 09-06 and 09-08 and different
from 09-04 -- a carried-forward duplicate, which is precisely the "repaired into a number nobody measured" that
FWD-4 forbids. Every arm of the accept that grades FWD-4 read clean over it, because the accept enumerated two
partners of three and because the classifier's class A is silent about invention by construction.

**THE BAR IS DISCRIMINATION, AND THE SHAPE IS YOURS.** The classifier must report a closed day CARRYING a slice
differently from a closed day carrying NOTHING. Whether you do that with a distinct class value or with a
populated field on the existing class-A record is your call as the assignee. What is not negotiable is that the
two cases become textually distinguishable in the returned record, and that nothing else moves.

⛔ **IF YOU CHOOSE A NEW CLASS VALUE, CLAUDE.md RULE 24 BINDS AND THE ARITHMETIC IS A TRAP.**
`_CLASS_NAMES = ("A", "COVERED", "B", "C", "D", "UNKNOWN")` and `summarize` computes
`trading_days = COVERED + B + C + D + UNKNOWN` and `holes = C + UNKNOWN + D` -- class A is a member of neither
sum. A new value that silently joins `_CLASS_NAMES` without a decision about BOTH sums changes every partner's
`trading_days` and possibly `holes`, and every downstream coverage line with it. A new value therefore arrives
with its four-postulate record (MECE over a declared domain, same grain, one axis and one intent, and which
values one remedy does NOT move) plus a word-boundary token census of the class names across the estate. **A
populated FIELD carries none of that cost and is the cheaper shape** -- said as information, not as a
prescription; if the field shape is worse for a reason you can state, take the class and pay rule 24.

---

## DELIVERABLE

The changed `classifier.py`, and a battery under
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/` that proves the arms below by
output. Every `.py` edit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39). You commit the
`complete` flip yourself after the proof instance validates.

---

## BOUNDS

- ⛔ **DO NOT TOUCH THE PRODUCER.** `inflection`'s producer writing priced values onto closed days is PRD v0.6
  row `S20`, ruled OUTSIDE this project and leaving as a brief to `4.0.0_SA_CRO` to enter at L1 as its own
  project. Naming it in your record is right; changing it is out of lane and out of surface.
- ⛔ **THIS CELL DEPLOYS NOTHING.** No `aws s3 cp` to the artifact prefix, no Terraform, no Lambda update. The
  deploy is a separate act with a separate owner and arm (f) exists to MEASURE the gap rather than assume it.
- ⛔ **NO MAILER AND NO INVOKE.** You construct no SES client and you invoke no Lambda in any mode. This cell is
  clear of Andrew's standing constraint (*"make sure no test run hits aj's email, that is not appropriate"*,
  ~02:5xZ 2026-09-10) BY CONSTRUCTION, and arm (g) proves that rather than asserting it.
- **Read-only on S3.** You read served objects; you write none. If a read needs bytes you cannot fetch, the
  archived copy or a committed fixture built FROM those bytes is acceptable and must say which it is.
- The ZERO-vs-MISSING contract that `EG-s-4` protects is load-bearing for class B and must survive untouched.
- Found something off-task? Append a row to
  `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md` and KEEP WORKING.

---

## ACCEPTANCE

⛔ **AMENDMENT 2026-09-10 ~04:2xZ BY THE ISSUER on row `ETFS_GUARDRAIL-W1-S32`. THE FACE WAS CUT WITHOUT ITS `criterion` TAGS AND WITHOUT `expected_criteria`, AND THAT IS THE ISSUER'S DEFECT.** `.tools/proof-of-spec-check.py` reads `cell_refs` EXCLUSIVELY from a face's `criterion` tags (`:435`, "NOTHING HERE IS DERIVED") and the acceptance-row schema exposes no `cell_refs` field, so a prose-only acceptance section yields `0/0 criteria carry >=1 cell_ref` and the `complete` flip is UNREACHABLE no matter how good the work is. The assignee had this file in its `<paths>` grant and could have added the tags itself; **it refused, and it was right to** -- editing the issuance half so one's own proof validates would certify an alignment the cut never declared. The tags below are the ISSUER'S act and they are the ONLY thing this amendment changes: not one arm, not one word of the bar, and the invocation and token are transcribed from the battery the assignee ALREADY BUILT AND RAN GREEN, never re-specified. **CENSUS BY SUBTRACTION rather than recall, on the assignee's warning that sibling faces might share the defect (CLAUDE.md rule 24 (i) as sharpened tonight): 23 task-order faces in this project, 22 carrying BOTH tags, so exactly 1 is defective and it is this one.** `EG-s-19`, `EG-s-20` and `EG-s-21` each carry their tags and their flips are reachable. The L6 gate did not refuse this at issuance and that gap is carried to `1.0.0_SA_CTO` -- the gate checks that a newly-added face carries `<decomp_ref>` and a complete `<preflight>`, and does not check that it carries a gradable criterion at all.

<criterion id="S22-AC1" cell_refs="EG-s-22"><invocation>timeout 300 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs22_classifier_discriminates.py</invocation><expect>EGS22-CLASSIFIER-DISCRIMINATES</expect></criterion>
**`S22-AC1` -- PASSES BY OUTPUT.** One battery, run by the invocation named in the tag above, printing every
number beside its denominator and ending with the literal token `EGS22-CLASSIFIER-DISCRIMINATES` only when all
seven arms hold. Each arm is one clause.

**(a) THE DEFECT REPRODUCES FIRST, ON THE PRODUCER'S OWN BYTES.** Against the classifier AS IT STANDS BEFORE
your change, classify a closed day for a partner whose slice EXISTS, using `daily/inflection/2026-09-07.json`'s
real bytes (fetched, or a fixture built from them and declared as such with its sha256), and print the returned
record whole. Expect `{"class": "A", ...}` with nothing in it naming the slice. **If this arm does not
reproduce the defect, the premise of this cell is wrong: file a surprise row, print what you found, and stop --
do not proceed to change code on a premise the world just refused.**

**(b) THE DISCRIMINATOR.** After your change, the record returned for that same closed-day-WITH-slice case and
the record returned for a closed-day-with-NO-slice case are printed side by side and are TEXTUALLY UNEQUAL.
State the shape you chose in one sentence.

**(c) POSITIVE CONTROL -- A GENUINELY EMPTY CLOSED DAY STILL READS AS IT DID.** For a partner/date with no
slice on a non-trading day, taken from the artifact's own partner list with that list printed as the
denominator, the class is still `A` and the date still appears in no partner's `holes`.

**(d) THE ZERO-vs-MISSING CONTRACT IS UNDISTURBED.** Re-run the existing suite
`data/etfs/scripts/coverage/tests/test_classifier.py` by its own path and print its rc and its pass/fail counts.
Expect no regression against its pre-change result, which you also print.

**(e) NO ORDINARY DAY MOVES, AND THE ARITHMETIC IS PROVEN NOT ASSUMED.** Recompute the 2026-09 verdict over the
real served slices for EVERY partner the artifact lists, before and after your change, and print both full
count tables with the partner-day denominator. Every count is identical except where the closed-day-carrying-a-
slice case sits. Print `trading_days` and `holes` for each partner on both sides and state in words whether
either sum moved and why that is correct.

**(f) DEPLOYED-vs-BUILT, MEASURED.** Print the sha256 of the classifier bytes currently deployed at the box's
artifact prefix beside the sha256 of your committed bytes, and state `DEPLOYED == BUILT` or
`DEPLOYED != BUILT` in those literal words. **This cell does not deploy and the expected answer is
`DEPLOYED != BUILT`.** The arm exists because a project can pass every criterion while the artifact the estate
actually reads is unchanged -- so the gap is recorded as a number and handed on, never left as an assumption.

**(g) NO SEND AND NO INVOKE.** Print the evidence from your own run that no SES client was constructed and no
Lambda was invoked over the whole battery.

<criterion id="S22-AC2" cell_refs="EG-s-22" judgment="true"/>
**`S22-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** Your record states, for `3.0.0_SA_CVO` at L9: which
shape you chose and why; if a class value, its four-postulate record and its token census; what this change
does NOT repair, naming row `S20` and the producer explicitly; and the DEPLOYED-vs-BUILT number from arm (f)
with the sentence that the served verdict object cannot discriminate until someone deploys it. Do not grade
yourself PASS on this criterion -- it is graded at L9.

<expected_criteria>S22-AC1, S22-AC2</expected_criteria>

<paths>
data/etfs/scripts/coverage/classifier.py
data/etfs/scripts/coverage/tests/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-22.the-classifier-tells-a-closed-day-with-a-slice-from-one-without.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.4, cell `EG-s-22`.
<owned_cells>EG-s-22</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger of
any kind; it edits one library module and runs a local battery. The round-3 schedule read at `EG-s-19`'s cut
(2026-09-09 ~22:2xZ, 5 of 5 carriers, 25 gates armed, zero naming ETFS_GUARDRAIL or `opal-data-etfs`) is
unchanged and is stated here as context, not as this cell's disposition.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; no policy, role or trust document is
read or written, and the S3 reads run under the seat's existing credentials.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own
deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants.
`data/etfs/scripts/coverage/` is NOT a `{gold,silver,bronze}` path, so CLAUDE.md rule 13's DS commit lane does
not gate it; rule 14's `.tools/commit-gate.sh` does, on every `.py` edit, and binds here.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S22-AC1`, `S22-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-22.the-classifier-tells-a-closed-day-with-a-slice-from-one-without.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under
`deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S22-AC1,S22-AC2` BEFORE the
complete flip, which you commit yourself. Flip only when `S22-AC1` PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages --
anything you would ask is a surprise row.
