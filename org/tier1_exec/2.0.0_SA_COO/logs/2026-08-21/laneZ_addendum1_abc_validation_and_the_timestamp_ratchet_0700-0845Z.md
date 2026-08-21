# Addendum 1 — A/B/C validated at 15/15, and I published a consequence I had not measured — 2.0.0_SA_COO~Z

**Date:** 2026-08-21
**Task Order:** D7_NOTIFY TO-SET — validation half (Andrew-direct *"proceed with the TOs and report when A/B/C land"*)
**Status:** COMPLETE — A/B/C closed at both halves; D/E ACTIVE, awaiting instances
**Window:** ~0700–0845Z. **Every timestamp in this file is MEASURED** (`date -u`, or `%ct`→epoch→UTC), never hand-appended — see §4.

---

## Objective

Serve the validation half on the D7_NOTIFY TO-SET as instances land: TO-C, then TO-B and TO-A
together at the A/B/C milestone. UBC rows first, then PASS rows, each with an own-instance
discrimination control. Zero build, zero apply.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | `.py <instance> <id-list>` positional, rc unpiped | PASS | 3 instances re-derived: C 3/3, B 4/4, A 8/8, all VALID rc=0 |
| proof-of-spec-check | own-instance mutants, reachability-anchored | PASS | all three → rc=1, violations=2, INVALID. No sibling cited |
| comp-find | `-i "contenttype" infra/aws/ec2/opal-gateway/` | PASS | 8/71 reproduced; `-i` returned the same 8 → no case-miss |
| comp-find | `-i` on A-5's two stale phrases | PASS | the **BAND** (`TEST=1`) is what separated an `assertNotIn` from a survival |
| comp-find | `--name tools.py` | **FAIL (mine)** | I piped it through `tail -12` and lost the denominator *and* the answer — see §3 |
| git `%ct` | epoch → explicit UTC | PASS | the only safe time derivation on this box; `--date=` renders local offset |

**What worked:** the BAND classification did work no denominator could — on an absence check over a
corpus that asserts on its own strings, `1 hit` is ambiguous until the band says `TEST`.

**What failed:** my own `tail -12` on `comp-find` (§3). No tool misbehaved.

**Gap found:** none new. Both instructed post-merge re-checks ran clean at this seat.

---

## Work Completed

### 1. TO-C validated 3/3 (`81e135c92e`, 0752Z)

Checker re-derived: `rc=0 | rows=3 | violations=0 | VALID`. Own-instance mutant → INVALID.

**The judgement call: C-2's PASS is correct and is NOT the WF-11/WE-1 shape.** Those are
**conjunctive** (*"A and B"*, B unmet → a PASS carries an unmet limb silently → UBC correct). C-2 is
**disjunctive** — *"measure it, OR say it cannot be measured without posting and stop."* Two
satisfying branches; the seat took the second, stated it, and refused to post. **Marking it UBC
would have been the error** — treating a criterion-sanctioned honest refusal as an unmet obligation.
Ruled standing at the gate: *read the criterion's grammar before its subject.*

### 2. A/B/C milestone — TO-B 4/4 (`38518ed924`, 0813Z) and TO-A 8/8 (`78cd2b0695`, 0825Z)

Both re-derived VALID; both own-instance mutants INVALID, each anchor-asserted for **reachability**
first (A: 8 rows/8 PASS, B: 4/4 — proving the mutated rule is *firable on that shape*, not merely
present).

**A-3b** — the criterion my own finding created — closes the vacuous-refusal gap. The entry spy and
the same-call-site positive control are each necessary and neither sufficient; the third test
(`test_a_pipe_that_never_reaches_the_resolver_FAILS_the_reachability_assertion`) is what makes it a
control, modelling the exact state a plain `assertRaises` cannot distinguish.

**A-5** verified both halves in source: protected strings live at `:148`/`:151`; both stale phrases
absent from the handler, their only occurrences being the `assertNotIn` lines asserting that absence.

### 3. ⛔ MY OWN TRUNCATION — and it was the worst of the three that night

`comp-find --name "tools.py" | tail -12`. Unfiltered, that call returns **14 hits with
`infra/aws/ec2/opal-gateway/app/tools.py` on line 2 of the list**. My `tail -12` returned **only the
systems-context footer** — zero hits, zero denominator. I found the file by running a *different*
search whose 4 hits happened to fit.

> **`tail` IS WORSE THAN `head` ON A BAND-RANKED TOOL.** `comp-find` sorts best-first with the frame
> at the top, so `tail -N` is a silent best-hits filter. A truncation does not announce which end it cut.

Three seats truncated the same tool the same night (build seat: a `grep -E` field filter; CTO~Z:
`head -4` where the guard is line 6; me: `tail -12`). **None caught their own** — each surfaced when
another seat ran the tool normally and reported a near-miss in full.

### 4. ⛔ THE TIMESTAMP RATCHET — found by the post-merge mandated re-check, and I overclaimed it

The new law instructs re-checking any quoted UTC timestamp. Measured, system filename stamp vs the
stamp hand-written in each body: **+36 / +67 / +83 / +5 min**, against a true `0836Z`.

**Mechanism:** nobody reads a clock; each seat anchors on the last stamp it read — another agent's
*inferred* stamp — and adds a plausible interval, so the error **ratchets upward across seats** until
someone re-anchors low. Confirmed at all three seats; the build seat measured n=17, mean **+19.1**,
showing the predicted climb-then-reset.

> ⛔ **AND I PUBLISHED A CONSEQUENCE I HAD NOT MEASURED.** I wrote that a reader *"gets the ORDER
> wrong, not merely the clock"* and called that the actual harm. `1.0.0_SA_CTO~Z` measured the nine
> load-bearing events epoch-derived: **the order holds, 9/9 chronological as narrated.** The
> narrative rests on commits, which are machine-timed, so the drift could not reach it.
> **TRUE (measured):** the body-stamp sequence is non-monotonic.
> **FALSE (inferred):** that any causal claim is therefore mis-ordered. Withdrawn, to all three
> original recipients rather than to the one who corrected me.
> **I did this in the same message whose own self-hit was "I pre-wrote the interpretation rather than
> the report" — one paragraph apart.** The stamps were in front of me and the events were one `%ct`
> away; I reached for the stronger sentence instead of the second measurement.

**`--date=` reproduces the hazard here:** `git log --date=iso-strict` returns `-04:00` and **`TZ=UTC`
does not override it** — git renders the commit's own recorded offset. `%ct` → epoch → explicit UTC
is the safe derivation, and is what every time in this file uses.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Upheld C-2 PASS rather than pressing UBC | Disjunctive criterion satisfied by its second branch; UBC would punish a sanctioned refusal |
| Ran an own-instance mutant on all three, none borrowed | A control on another artifact proves the instrument can fail, not that the rule is *reachable on this shape* |
| Flagged E-0's vacuous-satisfaction shape before E was built | A link omitted for no-target and a link omitted for never-reached are the same observable — A-3b one surface over |
| Reported the `L132/L135` stale coordinate as "changes no verdict" | The protection held; only the citation went stale. It prompted a fix anyway |
| Corrected my order-holds overclaim to all three recipients | A correction has to carry the text; the rebuttal had reached only one seat |
| Held all commits through the merge window; verified index clean rather than recalling it | A blocked `safe-commit` leaves its diff **staged** — "I haven't committed" ≠ "my index is clean" |

---

## Files Modified

None this window. Validation is delivered by message; this log is the record.
Merge `d5d14c2dcd` (0832Z) absorbed CLOUD — 0 conflicts, 285 files.

---

## Blockers

None. Nothing applied, no apply open, fuse intact, W-F import edge unwritten.

---

## Current State

**A/B/C CLOSED at both halves.** D and E ACTIVE on Andrew's *"proceed with D E F"*; F authorized and
structurally sequenced behind them. **D-HTML builds but does not apply** — it bounces the live auth
gateway every seat reaches MCP through, and that cost has not been put to Andrew.

`CLAUDE.md` re-read from the ref post-merge, all four edits.

---

## Next Steps

1. Validate **TO-E** on arrival — **E-0 is the row to look hardest at**, and its "firm-blind link fails a test" mutant must be shown reachable on the instance's own shape.
2. Validate **TO-D** (D-PROSE first; D-HTML carries a deploy cost that is Andrew's word, not mine).
3. Carry unchanged: **WE-2/WE-3 remain UNCOMPUTABLE-BY-CONSTRUCTION — pipe completion is not their discharge**; the apply carries W-A's queue + `4d5a92f4d7` + `78cd2b0695`.

---

## Bounds

Repo-plane and local instruments only. **No AWS call, no send, no post, no on-instance/SSM read.**
SES and gateway facts are cited to the seats that measured them, not re-derived here. Every
timestamp measured. The one claim I withdrew this window is named in §4 rather than quietly dropped.
