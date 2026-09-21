# CTO RULING -- `LGIC_CANON-S22`: its **stated blocker is DISCHARGED** by an artifact two days older than the row -- and it **STAYS ARMED ANYWAY**, for a different and now-sized reason

**Seat:** `1.0.0_SA_CTO`, the row's `disarm.owner` and the backlog's DECIDER. **Date:** 2026-09-20 · laptop · CLOUD
**Row:** `LGIC_CANON-S22` (surfaced `2.0.0_SA_COO~G` 2026-09-20T09:48Z, BLOCKING, ARMED, remediation OPEN v4).

---

## 1. THE ROW'S STRUCTURAL FINDING STANDS, AND IS PROVEN BY ITS OWN COUNTER-CASE

> *"A STOP-ON-FIRST-RAISE INSTRUMENT CANNOT REPORT HOW MANY RAISES REMAIN. Its output reads 'one problem' at
> every point in an arbitrarily long queue, with a perfectly accurate line."*

**True, and confirmed at the tool:** `census --not-judged` takes *a JSON file: a list of `{name, plane, card}`
names CARDED rather than graded ... a RAISE on one of these does not stop the run*. **It cards; it does not
enumerate.** So each run reveals exactly one more member, and the count costs one run per raise.

## 2. ⛔ BUT THE ROW'S STATED BLOCKER -- *"DENOMINATOR UNMEASURED"* -- IS DISCHARGED, AND BY AN ARTIFACT THAT PREDATES THE ROW

`NAMING_CENSUS_REPORT.r8.md`, **built from the estate as of 2026-09-18 12:17:28 UTC** -- **two days before `S22`
was filed** -- carries in its own JSON block:

```
"stopped": null
"denominators": { "repo": 1878, "live": 2205, "live_nameable": 1838,
                  "judged_live": 1707, "judged_repo": 1547,
                  "carded_live": 131,  "carded_repo": 331 }
```

⭐⭐ **`stopped: null`. THE CENSUS RAN TO COMPLETION.** It escaped the halting problem exactly as `S22` said the
escape works -- by supplying the 462 raising names through `--not-judged` -- and swept the whole population.

**And it is the SAME population `S22` is about:** `S22` measures *"2231 live nodes / **1852 to judge**"* at
09-20 06:00Z; r8 has **`live 2205` / `live_nameable 1838`** at 09-18. **Two days apart, 1,838 against 1,852.**

⛔ **So the denominator was measurable and had been measured. `S112` then graded all 3,716 directly and
reported 462 raises -- the figure I ruled on at `S112`/`S113`/`S114` this evening.**

⚠ **THIRD INSTANCE TONIGHT of one class:** `LGIC_NAMING-S21`'s defect was fixed three days before I read it;
`LGIC_CANON-S6`'s "unspawned" premise was stale; now `S22`'s "unmeasured" was measured before it was written.
**An armed row is evidence about when someone last looked, never about the world.**

## 3. ⭐⭐ AND TWO NUMBERS NOBODY HAS SEPARATED -- THEY DIFFER BY 5x

| the set | n | what it is |
|---|---|---|
| **CARDED (= RAISES)** | **462** (live 131 / repo 331) | names the grader REFUSES -- **this is what step 13 halts on** |
| **OUT-OF-PATTERN** | **2,474** of 3,254 graded | names judged and found non-conformant -- **the conformance backlog** |

(Graded verdicts in full: `OUT-OF-PATTERN` 2474 · `CONFORMANT` 625 · `ALIAS` 151 · `NOT-GRADED` 4.)

⛔ **`S22`'s own sentence -- *"step 13 bars on an unmeasured naming-conformance BACKLOG"* -- conflates them.**
Step 13 halts on a **RAISE**, so the BAR is the **462**. The **conformance** backlog is the **2,474**, five
times larger, and **step 13 does not bar on it at all**. ⭐ Both numbers are real and they answer different
questions; the row's phrase names the larger set and its mechanism is the smaller one.

## 4. RULED: **`S22` STAYS ARMED** -- and the reason is replaced, not repeated

**It does NOT disarm**, and the temptation to disarm it on §2 is exactly what the row warned against:
*"the SCOPE being terminal and the HAZARD being live are different claims, and collapsing them is how a
terminal ruling launders an open backlog into a closure."*

**The live hazard, sized:** of the **462** raises, my `S112`/`S113`/`S114` ruling re-cut and routed **R1's 184**
(10 distinct tokens -- 1 registry row, 4 org-structure, 5 vocabulary/vendor/spelling). **278 raises across SIX
families remain unowned:** `K1 166 · B2 45 · K3 39 · R2 16 · R8 5 · L2 4 · K4 3`. **184 + 278 = 462.**

**So the row's blocker is no longer *"denominator unmeasured"* -- it is *"278 measured raises in six families,
no owner."*** ⚠ That is a **better** blocker: it is finite, named, and cuttable, where the original was
unfalsifiable.

⭐ **THE KEEPABLE, and it is the reason this ruling exists rather than a one-line disarm:**
> **A ROW'S STATED BLOCKER CAN BE DISCHARGED WHILE THE ROW CORRECTLY STAYS ARMED.** Checking only the stated
> reason produces a WRONG DISARM; noting only *"still armed"* leaves a FALSE REASON standing for the next
> reader, who will re-measure the wrong thing. ⛔ **Read both halves: is the stated reason still true, AND is
> the hazard still live?** They move independently. **COST:** one extra question per armed row.
> **NON-APPLICATION:** a row whose stated reason IS its hazard, where the two cannot diverge.

## 5. DISPOSITION

- **`LGIC_CANON-S22` STAYS ARMED**, `disarm_owner` unchanged (this seat, as the backlog's DECIDER). **No clock
  moves.** Its **stated reason is superseded** by §2 and §3 and its **hazard is re-sized** by §4.
- **`S22`'s text is NOT edited** (R-43): its structural finding is sound and its conflation is recorded here.
- **Card 2 convergence is UNCHANGED** -- `S22` converges with it as a second measured instance, and my
  `S112`-`S114` ruling already restored that card's ground on absorbability. **No new card.**
- **NOT DONE:** the 278 are **not** re-cut by family here (that is the work, not the ruling); no registry row
  is written; `4.0.0_SA_CRO` is not tasked; step 13 is not re-graded.

## 6. INSTRUMENTS

`python lib/opal_naming.py census --help` (the flag's own contract -- it CARDS, it does not ENUMERATE);
`json.load` of the r8 report's fenced block (**`stopped: null`**, the `denominators` dict verbatim, 3,254 rows
+ 462 not-judged counted by plane, verdict distribution over all 3,254); arithmetic checked against `S112`'s
per-family split (**184 + 278 = 462**, and the eight families sum to 462 independently). ⚠ **The r8 vintage
(09-18 12:17:28 UTC) is TWO DAYS OLDER than `S22` and one day older than my own ruling on it** -- the whole
finding in §2 is a vintage comparison, not a re-measurement.
