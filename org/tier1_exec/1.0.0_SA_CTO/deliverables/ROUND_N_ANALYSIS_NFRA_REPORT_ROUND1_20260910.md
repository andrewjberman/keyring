# ROUND-N ANALYSIS -- `NFRA_REPORT` round 1

**Author:** `1.0.0_SA_CTO~Z` - **2026-09-10 ~00:5xZ** - **Limb:** L10, the CTO's answer to the CVO's slug
**Slug:** `3.0.0_SA_CVO~Z` msg 20689; `ADJUDICATION_v1.md` @`87f279b055`, extended @`bdc578c78c`
**Drain-end read:** `2.0.0_SA_COO~ZZ` msg 20680
**PRD:** `org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md` v0.6
**archetype:** VALIDATE

> **This document is what `2.0.0_SA_COO~ZZ` recuts round 2 from, in ONE issuance.** It is not a grade of
> the lane's work and not a re-derivation of the drain -- both of those are measured elsewhere and are
> cited, not re-taken.

---

## 1. THE CENTRAL FINDING: ROUND 1 BUILT ENGINES, AND NINE OF TWELVE BARS CANNOT BE MET BY AN ENGINE

Measured with the estate's own `FWD_DEF_RE` against the PRD's ENDPOINT section, 12 of 12 outcomes
parsed, and the tally **cross-checks against the endpoint deliverable's own independent claim of
"NINE of TWELVE are EXERCISED and THREE are APPLIED"**
(`ENDPOINT_GLOBAL_INFRA_REPORTING_20260909.md:304`) -- **both read 9 / 3, independently:**

| bar | count | outcomes |
|---|---|---|
| `APPLIED` -- true once the artifact is in place | **3** | `FWD-2`, `FWD-9`, `FWD-10` |
| `EXERCISED` -- has RUN, and the result was READ | **9** | `FWD-1`, `FWD-3`, `FWD-4`, `FWD-5`, `FWD-6`, `FWD-7`, `FWD-8`, `FWD-11`, `FWD-12` |

⛔ **SO ROUND 1 COULD NOT HAVE CLOSED THIS PROJECT NO MATTER HOW WELL IT EXECUTED, AND THAT IS THE
SINGLE MOST IMPORTANT SENTENCE IN THIS ANALYSIS.** Twelve cells built twelve engines. Nine bars ask
whether the report has RUN and someone has READ the answer. **A round that builds every engine
perfectly still leaves nine outcomes unrealized**, because the bar is about exercise, not existence.
Anyone reading "12 of 12 terminal, 12 VALID" as near-completion has read the wrong quantity.

⭐ **AND THAT IS THE BARS WORKING, NOT A PLANNING ERROR.** `EXERCISED` was chosen per-outcome at L2 and
confirmed by Andrew precisely so that a built-but-never-run report could not grade REALIZED. The
project's own commissioning complaint was a report that ran daily and said the same alarming thing
every time -- an artifact that exists and is not read. **The bars were set to make that outcome
ungradeable, and they are doing it.**

---

## 2. PER-OUTCOME DISPOSITION

**Grading rule used:** `REALIZED` only where the artifacts show the bar's own words satisfied.
Everything else is `NOT-REALIZED` with the reason, and **`NOT-REALIZED` is not a criticism** -- for
nine of these it is the expected state after a build round.

| FWD | bar | round-1 cell | disposition | why |
|---|---|---|---|---|
| `FWD-1` | EXERCISED | RP-s-2/3/4 | **NOT-REALIZED** | The verdict rule, row structure and schedule are built. **No trading morning has run**, and the bar additionally requires at least one morning whose verdict was "nothing needs you". |
| `FWD-2` | APPLIED | RP-s-1 | **REALIZED (pending L9's residual)** | `STATE_MODEL.md` carries the vocabulary; `RPs1-AC5` graded PASS by the CVO, and the confusion the bar fears is **BARRED, not discouraged** -- s.2 forbids an Axis-2 value on any non-CHECKED row. See §4(a) for the one residual. |
| `FWD-3` | EXERCISED | RP-s-2 | **NOT-REALIZED** | Per-row delta is built. The bar wants a reader who **used it** to tell a new problem from a standing one; there has been no second edition to diff against. |
| `FWD-4` | EXERCISED | **NONE** | **NOT-REALIZED -- UNCOVERED** | No round-1 cell served it. Row `NFRA_REPORT-Z-S1`; the PRD addendum at v0.5 split `S1` and created **`S13`**. **This is round 2's first item.** |
| `FWD-5` | EXERCISED | RP-s-6 | **REALIZED** | The bar: *"at least one alert that would reach nobody has been identified from the report, before any incident tested it."* `RP-s-6` identified **`opal-infrastructure-alerts` -- the report's own escalation channel -- as reaching nobody today**, via the SNS SMS sandbox, before any incident. **The bar is met in its own terms.** |
| `FWD-6` | EXERCISED | RP-s-7 | **REALIZED** | The bar wants one stale thing correctly called retired and one correctly called broken, **on evidence rather than age**. `RP-s-7` performed a real consumer walk to a client-facing terminus over ten candidates, resolved 5 ALIVE, and **treated every unresolved candidate as NOT deprecated** -- refusing the age heuristic is the bar's substance. |
| `FWD-7` | EXERCISED | RP-s-8 | **NOT-REALIZED** | The retirement register is built. The bar requires something **actually retired** and the next edition to have **stopped raising it** -- two editions and a real retirement, neither of which exists. |
| `FWD-8` | EXERCISED | RP-s-9 | **NOT-REALIZED, and PARTLY BLOCKED** | SEGMENT grain is live; **BOX grain is not deliverable** -- and not because of `RP-s-5`. See §5: resource-level Cost Explorer is opt-in DISABLED at the payer account. Andrew's. |
| `FWD-9` | APPLIED | RP-s-5 | **REALIZED, with a corrected denominator** | `RPs5-AC6` PASS; separation is real (instance_type byte-unchanged 27/27; machine_type 16, lifecycle 9, both = 0) and the grouping is correctly **RESTRAINED**. ⚠ Two measured corrections against the instance's own numbers -- see §3. |
| `FWD-10` | APPLIED | RP-s-10 | **REALIZED** | Coverage/denominator discipline is in place. ⚠ Its integrity now depends on §3's duplicate-id finding, which is exactly the class this outcome exists to prevent. |
| `FWD-11` | EXERCISED | RP-s-11 | **REALIZED** | The bar is the standing check no existing instrument performs. It **ran and returned findings on its first real pass** -- three served surfaces matching zero of 51 alarms, positive-controlled, including a live portal-consumed trade workflow. Read and acted on. |
| `FWD-12` | EXERCISED | RP-s-12 | **NOT-REALIZED** | `RPs12-AC3` PASS on the strip test, so the C-AI guardrail holds. But the bar wants the **named connections CHECKED and correct** on a real anomaly, and no anomaly has been produced by a running report. See §4(b) for a grain residual. |

**TALLY: SIX of twelve REALIZED** -- `FWD-2`, `FWD-5`, `FWD-6`, `FWD-9`, `FWD-10`, `FWD-11`. **Six
NOT-REALIZED** -- `FWD-1`, `FWD-3`, `FWD-4`, `FWD-7`, `FWD-8`, `FWD-12`. The two sets are disjoint and
sum to 12, which is the check that makes the headline quotable.

---

## 3. THREE MEASURED CORRECTIONS TO NUMBERS THE ROUND PRODUCED -- and they all cut the same way

The CVO's re-derivations found three arithmetic overstatements. **None changes a disposition. All three
overstate coverage, which is the direction that matters for a project whose whole premise is `FWD-10`.**

1. **The EC2 manifest carries a DUPLICATE instance id.** 27 entries, 26 with an id, **25 distinct**
   (`i-0800437d1dbb0b5cc` twice). **Any coverage figure derived from its row count overstates by one.**
   Round 2 must not compute a denominator off the row count.
2. **`RP-s-5`'s instance claims "27 of 27 rows carry an explicit machine_type XOR lifecycle value";
   the direct count is 25 of 27.** The two that carry neither are precisely the rows the cell
   **correctly declined to guess** -- so the act was right and the coverage sentence overstates by two.
3. **`C-S4` of the CVO's own adjudication was FALSE** and is superseded at `C-S5`: it said no JUDGMENT
   criterion was routed, when three were. Disclosed by that seat against itself.

⛔ **THE SHARED MECHANISM, AND IT IS THIS ROUND'S SIGNATURE FAILURE ACROSS THREE DIFFERENT SEATS: A
MATCHER THAT CANNOT MATCH RETURNS AN EMPTY RESULT THAT READS EXACTLY LIKE A TRUE ZERO.** The CVO's
first probe looked for `kind`/`type`/`criterion_type` when the field is `method`, and got an empty
distribution. This seat's own bar census in preparing THIS analysis demanded two spaces after an
outcome id and silently dropped `FWD-10`, `FWD-11`, `FWD-12` -- **three of twelve, and the parse looked
successful.** It was caught only because the tally failed a cross-check against a figure written down
independently. **The remedy that worked both times was a CROSS-CHECK AGAINST AN INDEPENDENTLY-RECORDED
NUMBER, not a more careful read.** Round 2's criteria should carry one wherever they count.

---

## 4. TWO RESIDUALS THAT ARE THE PRD'S, NOT A CELL'S -- amendments DIRECTED

Both come from the CVO's grades and both are L4 items, so they are settled here rather than routed:

**(a) The third axis renders ONLY when not `applied`, so ABSENCE CARRIES MEANING** -- and a blank is
indistinguishable from a field the renderer failed to populate. `STATE_MODEL.md` s.5's rule and s.7's
specimen **disagree about what a fully-applied row looks like** (the specimen prints a literal marker;
the rule prints nothing).
⛔ **RULED: absence may not carry meaning on this axis.** This is `FWD-2`'s own principle one axis
over -- *not being able to see something must never look like seeing something*, and a blank that
means "applied" is indistinguishable from a blank that means "the renderer broke". **A fully-applied
row renders an explicit value.** s.7's specimen is the correct behaviour and s.5's rule is the defect.
Round 2 amends the rule, not the specimen.

**(b) `C-AI` does not state the GRAIN at which "a generated part is never the sole carrier of a fact"
must hold.** `RPs12-AC3` passed at the REPORT grain; the constraint does not say whether it means the
report or the deliverable.
⛔ **RULED: the REPORT grain.** `C-AI` exists so that stripping every generated sentence leaves a
report that is still true and still checkable -- the reader's artifact is the report, and a deliverable
is an intermediate nobody reads at the morning read. **The bar is the report.** Recorded so a future
grader does not re-litigate it at a stricter grain and fail a cell that met the intended one.

---

## 5. WHAT ROUND 2 MUST COVER -- the input to ONE issuance

1. **`S13` / `FWD-4`** -- the attribution axis and its mandatory rendered `UNGROUPED` value. **The only
   structurally uncovered outcome.** ⚠ Its member NAMES are an open call at Andrew (Gateway / Graph /
   both); `UNGROUPED` is what makes the cell cuttable without that answer.
2. **THE RUN ITSELF.** Nine bars are `EXERCISED` and six remain unmet purely for want of real
   editions. **Round 2's centre of gravity is getting the report to run on trading mornings and
   getting its output read** -- not building more engines. `FWD-1`, `FWD-3`, `FWD-7` and `FWD-12` all
   reduce to this.
3. **The two amendments in §4**, as spec changes to `S1`/`S12`'s cells.
4. **The denominator hygiene in §3** -- no coverage figure off the manifest's row count.
5. ⛔ **NOT IN SCOPE: `FWD-8`'s BOX grain.** Blocked on a billing setting, not on `RP-s-5`. §6.

**SEQUENCING NOTE, offered and not mandated -- the decomp's contract is `2.0.0_SA_COO~ZZ`'s:** the
`(row, outcome)` one-cell rule that lane accepted removes the partial-cut hazard, and this round
supplies a second input to it -- **the fan-out is computed at the moment the graph looks maximally
serial.** That lane measured it: `2 of 2 chains` was correct at issuance and stopped being correct the
moment `RP-s-1` landed and four chains opened while slot `~2` idled, and the freeze on `<issued_to>`
meant it could not be rebalanced. **The freeze is correct and should not change** -- it is what makes a
worker face trustworthy. The available remedy is at the CUT: a round whose first cell unblocks several
others can be issued with the post-unblock width in mind rather than the pre-unblock one.

---

## 6. WHAT IS ANDREW'S, AND NOTHING WAITS ON HIM

- **Resource-level Cost Explorer is opt-in DISABLED at the payer account**, and cost-allocation tags
  are coarse -- null on 9 of 27 rows with a casing drift. **This is why `FWD-8`'s box grain is not
  deliverable, and the reason is NOT the compute manifest as `D3` assumed.** Enabling it is a billing
  decision. Row `Z-S4`, disarmed INERT by the COO lane.
- **`FWD-4`'s third property name** -- Gateway, Graph, or both. Carried; `UNGROUPED` unblocks round 2.
- **The `trade-submission-api` disposition** -- declare the gateway in Terraform, consolidate the two
  front doors, or authorize monitoring. From `FWD-11`'s first real pass.

---

## 7. WHAT THIS ANALYSIS DOES NOT CERTIFY

It does **not** re-derive 12-of-12 terminal, 12 VALID instances, 12 drains or 0 worktrees -- that is
`2.0.0_SA_COO~ZZ`'s measurement, **cited and not re-taken**. It does **not** re-grade the 31
command-method criteria, which are the executor's to self-report and the checker's to read at L8. It
does **not** read the nine deliverables the CVO also did not read. **It grades OUTCOMES against BARS
from the artifacts named above, and that is its whole scope.**

**The round is CLOSED at L10 for round 1. Six of twelve outcomes REALIZED. Round 2 is
`2.0.0_SA_COO~ZZ`'s in ONE issuance, off this document.**
