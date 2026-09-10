# NFRA_REPORT PRD ADDENDUM 01 -- FOLDED IN. THIS IS A POINTER, NOT A SPEC.

⛔ **DO NOT CUT AGAINST THIS FILE. DO NOT EDIT IT. IT IS NOT A CARRIER OF ANY OUTCOME.**

`FWD-13`, `FWD-14` and `FWD-15` now live in the PRD's own `ENDPOINT` section, which is the only
carrier:

```
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md   ->   ## ENDPOINT (step 2, /endpoint --forward)
```

---

## WHY THIS FILE IS A POINTER NOW -- THE DEFECT IT CAUSED, STATED PLAINLY

This addendum was authored 2026-09-10 ~14:1xZ by `1.0.0_SA_CTO~Z` and **issued to the COO as the
spec for round 4 without ever being folded into the PRD.** The rule for a PRD addendum is explicit:
**the PRD edit is the CTO's, same turn, and nothing routes onward until the `ENDPOINT` section
reflects the change.** That did not happen.

**What the round was therefore cut from:** 3 outcomes and 6 constraints.
**What the PRD actually held:** 12 outcomes and its full constraint set.

⛔ **THE CONSEQUENCE, MEASURED RATHER THAN ASSERTED.** `C-COST-15` -- Andrew's own verbatim cost
detector, *"if something moves say 15% or more from its trailing 30 day price"* -- is a NAMED
CONSTRAINT in the PRD and was **not in the room when round 4 was cut.** This PRD carries the string
`15%` three times; this addendum carried it **zero** times. The round shipped a renderer that
dropped the cost sections, and the reader's first sight of it was the live 9 AM email.

⚠ **AND A SECOND DEFECT THAT SCOPE ALONE DOES NOT EXPLAIN, recorded here because this file is where
it was written:** §2 of this addendum asserted that the join was *"one substitution"* onto *"the
same row shape the compute functions already accept"*, and told the cut to *"exploit it rather than
re-architect around it."* **That was an architecture claim made without testing it.** The specimen's
row shape holds a state and a change and has no cell for a dollar figure, a ranked list or free
text. Even with the whole PRD in the room, that sentence pushes toward the shape that lost the
content. **The decomposition asked whether the port preserved the shape; the question was whether
the shape could carry the report.**

⚠ **AND A THIRD, ALSO FROM THIS FILE:** §6 sequenced the work as *"deploy on the Terraform path,
then exercise"*, which put `C-NO-REGRESSION` -- written in this same document -- **after the
irreversible act.** The check that would have caught the loss could not run until the loss was live.

⭐ **THE ENGINEERING WAS GOOD AND THE SPECIFICATION IT WAS BUILT TO IS WHAT FAILED.** The port was
faithful, the section partition complete with every omission reasoned, and the deploy correct with
its ledger opened before and closed after. `2.0.0_SA_COO~ZZ`'s own log took the root cause as L5's;
it was L4's, and L4 is this seat's.

---

## THE ORIGINAL TEXT

Preserved in git history at `@20c986bc70` and superseded. It is **not reproduced here**, because
reproducing it would recreate the exact condition this correction exists to close: two durable
carriers of one obligation, drifting from the minute the second is written.
