# ADVI_COTBKF round 66 -- L9 grade of CB66bn1-AC2 (method_r28 against method_r29)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T12:20:43Z. Row ADVI_COTBKF-D2-S115.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_66_DRAIN_END_20261011.md @eb8de12cd9 (msg 4896)`. This seat diffed the worker's two run tables against each other and against the served local table itself.
Counts and dates only; no account id, no client figure.

| limb of CB66bn1-AC2 | verdict | this seat's evidence |
|---|---|---|
| the two runs differ in the rule only | **MET** | Re-derived: 2 account-days differ between the two runs, 0 rows on one side only. The record's input equalities (split-store lines, 2,124,908 price rows) are the worker's and were not re-run |
| the control was run before the comparison | **MET** | The control ran first and failed as written; the comparison ran after the amendment. An early r29 start was killed and not used |
| every changed day is traced to a withholding or called unexplained | **MET on the worker's trace** | Both changed days are classed as withholding days. This seat did not read the transactions |
| the list of changed dates is the set a re-mint would replace, no wider and no narrower | **NOT MET** | Re-derived: against the served table, today's r29 run changes **32 account-days on 30 dates**, not 2 on 2. A re-mint from today's inputs replaces 30 day files |

**Verdict: CB66bn1-AC2 NOT MET, on the fourth limb alone.**

## Why the fourth limb fails

The list of 2 dates is the rule's effect with the inputs held equal. That part is right, and this seat reproduced it. But a re-mint
does not hold the inputs equal to the served run: the split store has grown since, and that alone moves 30 account-days on 29 dates.
A day file is replaced whole, so what counts is the date. One date, 2020-11-13, is in both sets: the rule moves one account that day
and the store moves another.

So the set a re-mint would replace depends on the pin:
- at a pin that reproduces the served store, it is the 2 dates;
- at today's store, it is 30 dates.

The record says it is not at a named pin. Until round 67 names the pin and the comparison is re-run there, the list is narrower than
what a re-mint would replace. The issuer flagged this itself; the grade follows from it.

## What stands

The rule's own effect is small and now measured twice: 2 account-days of 1,691,729, no month verdict moved.

The larger finding of the round is the control's failure: the served table cannot be rebuilt today. That is row D2-W97-S1, and it
matters beyond this rule. Any re-mint, for any reason, will also carry the store's drift unless the store is pinned.
