# COMPLEARN frozen-partition / `rolling_log` -- GROUNDED, and the framing INVERTS

**Owner:** 2.0.0_SA_COO (took the item 2026-08-21 ~0320Z; it had been described as "unowned at
Andrew/COO" in 0.8.0's 64227, surfaced originally by `1.0.0_SA_CTO~D` msg 59074).
**Status:** GROUNDED. **DISPOSITION: NOT A DEFECT TO REPAIR. STAGING ON COMPLEARN ITEM 1 RELEASED.**
**Vintage of every measurement below:** repo HEAD at time of read, 2026-08-21 ~0340Z.

This record exists because a ruling that must outlive a seat goes in a commit, not a mailbox
(1.0.0_SA_CTO Ruling 2, 64295). The mailbox carries only the pointer.

---

## 1. WHAT WAS CLAIMED, AND WHAT I MEASURED

The finding as it reached me: *"`rolling_log` feeds 2 of 5 emitter partitions and nobody has
written it since 2026-07-29."* Both halves are TRUE. The conclusion everyone was reaching for --
that this is neglect needing repair -- is FALSE.

| claim | verdict | measured at |
|---|---|---|
| 5 emitter partitions | CONFIRMED | `infra/aws/terraform/globgrph/tool_activity.tf:161-168` -- rail, rolling_log, rolling_log_summary, session_log, telemetry |
| `rolling_log` feeds 2 of them | CONFIRMED | `tool_activity.tf:18` -- "rolling_log + rolling_log_summary <- compiler-tools-log.md". ONE file feeds TWO partitions. |
| the file the emitter actually reads | `org/compiler-tools-log.md` | `infra/aws/globgrph/tool_activity_emit.py:74` -- `ROLLING_LOG = "org/compiler-tools-log.md"`. RESOLVED THROUGH THE BUILD INPUT, not by filename. |
| dead since 2026-07-29 | CONFIRMED | last commit `c79b4537ca` 2026-07-29T19:48:06-04:00 (= 23:48:06Z); filesystem mtime Jul 29 20:29. ~22.2 days at time of writing. |

**RETRIEVAL CONTROLS RUN, because an absence verdict without them is not a verdict:**
- Positive control: `org/compiler-tools-log.md` carries **1,403 commits all-time**, so the history
  read discriminates and the silence-since-07-29 is real.
- **The positive control CAUGHT MY OWN ERROR mid-measurement.** My first path extraction resolved a
  bare `compiler-tools-log.md`, and the all-time count came back **0** -- which is the signature of a
  BAD PATH, not a dead file. Had I only run the "since 07-29 = 0" query I would have reported a
  correct-sounding conclusion off a broken retrieval.
- Two-homes check: `portal/org/compiler-tools-log.md` also exists (231 B, Jul 17). It is **NOT** the
  emitter's target and is not a two-homes defect on the load-bearing path -- `:74` resolves the
  `org/` copy explicitly. Recorded so nobody re-opens it as one.

## 2. ⛔ THE CAUSE, AT SOURCE -- IT IS A SOVEREIGN RETIREMENT, NOT NEGLECT

`org/modules/graph/comp_log_auto.py:281-287`, the writer's own docstring:

> **MARKDOWN APPEND RETIRED 2026-07-29, ANDREW-DIRECT** (verbatim: *"we need to completely take out
> any doctrine or hook or anything that would say to write to that compiler-tools-log.md file, its
> just constant commit nonsense"*). SCOPE GUARD: this removed the WRITE, not the file --
> `org/compiler-tools-log.md` IS PRESERVED at its committed state and is still readable history.

So the freeze is **ORDERED, DELIBERATE, PERMANENT, AND CORRECTLY IMPLEMENTED.** The file was
preserved on purpose. Custody was verified *before* the cut (the JSONL sink already carried every
row at finer granularity -- 10,147 rows, 873 in the trailing 24h at cut time), so nothing was
single-copy at the moment of the cut. This is a well-executed retirement, not an abandonment.

**RULE 25 APPLIES AND ITS OWN WARNING IS THE POINT.** At ~22 days this is not dormant (90d bar), so
no dormancy verdict was ever available. More importantly Rule 25 warns that
dormant-because-ABANDONED and dormant-because-MIGRATED are byte-identical from age alone and take
OPPOSITE actions. **This is a third kind -- dormant-because-SOVEREIGNLY-RETIRED -- and it is
byte-identical to the other two from age alone as well.** Resuming writes here would not have been
a repair; it would have violated a standing Andrew instruction. *An age reading cannot tell you
which of the three you are looking at, and only the writer's source said so.*

## 3. THE ACTUAL LIVE DEFECT, WHICH IS NOT THE ONE ANYONE WAS LOOKING FOR

The freeze is fine. **Its CONSUMERS were never told.**

**(a) The emitter still harvests a file that will never grow again.**
`tool_activity_emit.py:491` still calls `parse_rolling_log(_abs(ROLLING_LOG))`, and Terraform still
registers both frozen partitions as live Glue partitions. The catalog therefore presents 5
partitions of which 2 are permanently frozen **and nothing in the catalog says so.** This is
CTO~D's framing, now with a measured mechanism underneath it:
**A FROZEN PARTITION INSIDE A CATALOG READS AS PRESENT, NOT AS ABSENT.**

**(b) The scorer's corpus has a silently-empty limb -- and this is the sharp one.**
`org/modules/graph/comp_learns_score.py`, `load_corpus()`:
```
rolling = []
try:
    rolling = tae.parse_rolling_log(os.path.join(_WS, tae.ROLLING_LOG))
except Exception:          # noqa: BLE001
    rolling = []
```
`load_corpus()` advertises `{rail, sessions, rolling, routing, source}`. The `rolling` limb is now
**permanently empty**, and the bare `except` makes three states BYTE-IDENTICAL to every downstream
reader:
  1. frozen by sovereign order (the truth, today),
  2. the parse raised (a real breakage),
  3. genuinely zero rows.
**An empty value that carries no reason, feeding a SCORER.** This is CLAUDE.md's own retrieval-control
class -- *never let a read whose EMPTINESS carries a verdict fail silently* -- and the `source` field
is the natural place to declare it, since that field exists precisely to say what the corpus is.

## 4. DISPOSITION

1. **NO REPAIR OF THE WRITE.** Resuming the markdown append contradicts a standing Andrew-direct.
   Anyone proposing it must take it to Andrew, not to this record.
2. **⛔ STAGING ON COMPLEARN ITEM 1 IS RELEASED.** Item 1 (6th emitter partition + delete the private
   read at `load_corpus`) was staged behind this adjudication per CTO~D's *"looked at before anything
   else in COMPLEARN."* **It has now been looked at. The sequencing is satisfied by GROUNDING it, not
   by fixing it** -- the frozen pair is a permanent, sovereign, non-moving floor, not a pending
   change that item 1 could land on top of and be invalidated by. 0.8.0_AE_CloudComp is unblocked.
3. **HANDED TO ITEM 1 RATHER THAN FILED SEPARATELY:** finding (b) lives in `load_corpus()` -- the exact
   function item 1 already opens. When that change lands, the dead `rolling` limb should be handled
   deliberately: either dropped with a stated reason, or its emptiness DECLARED (a typed
   "frozen-by-retirement" marker in `source`) rather than left as a silent `[]`. **Not a new gate and
   not a widening of item 1's scope** -- item 1's own acceptance already requires that the private read
   and the new partition move in ONE change; this just says what the honest handling of the limb is.
4. **(a) SURFACED TO CTO'S PLANE -- AND RULED THERE THE SAME HOUR. SEE §6.**
5. **NOT ESCALATED TO ANDREW TONIGHT.** He already ruled on this file once, and the ruling is being
   honored. Nothing here needs his word.

## 5. WHAT THIS COST AND WHY IT WAS WORTH TAKING

The item sat as "unowned at Andrew/COO" -- the shape that stops looking like something anyone must
do -- while silently staging a build at another seat. Grounding it took one source read of the
writer and four measurements. **The finding everyone had was true and its implied remedy was
backwards**, and the defect that was actually live (a scorer corpus with a silently-empty limb) was
not the one being discussed.

---

## 6. ADDENDUM (same session, ~0356Z) -- CTO RULED THE CATALOG QUESTION, AND FOUND A SHARPER ONE

`1.0.0_SA_CTO` ruled item (a) on their own plane within the hour (64391), re-deriving every figure
at their seat first -- 5 partitions, 1,403 commits all-time, 0 since 2026-07-29, last write
`c79b4537ca` 2026-07-29T23:48:06Z. **Their UTC rendering matches mine exactly**, which is a
non-trivial agreement on the night the `--date=` local-rendering law landed.

**RULING: ANNOTATE, DO NOT DE-REGISTER.** Three reasons, all of which I accept:
1. **De-registration is a deletion warrant and nothing grants one.** Those partitions address
   28,007 lines of real history. Rule 25 licenses stop-treating-as-live, never `rm` -- and this is
   the most protected dormancy kind of the three, because **Andrew retired the WRITE and
   deliberately PRESERVED the FILE.** De-registering would make history he chose to keep
   unqueryable *while appearing to honour him.*
2. **The defect is the catalog's SILENCE, not the partitions' EXISTENCE.** An annotated frozen
   partition is legible; an absent one is indistinguishable from one that never existed, and a
   later census would find 3 and be unable to tell retirement from never-built.
3. **The remedy must match the layer below.** I ruled the scorer's limb should carry a typed
   `frozen-by-retirement` marker rather than a silent `[]`. Same disease, same cure, two layers --
   if the catalog de-registers while the scorer annotates, the two records disagree about whether
   the thing exists at all.

**⛔ AND CTO FOUND A SECOND STALE REFERENCE THAT IS WORSE, IN THE OPPOSITE DIRECTION.**
`tool_activity.tf:22` still reads *"A CLOUD-MANAGED FRESHNESS ALARM (host-independent) watches this
parquet's staleness..."*. **That alarm was TORN DOWN** -- `tool_activity_freshness.tf` removed
@858554332d under the 2026-07-28 moratorium.

> The frozen partition is **a real thing the record fails to describe.**
> `:22` is **a described thing that is not real.**

The second is the more dangerous shape: a future engineer reading `:22` concludes staleness here is
watched and reasons accordingly. It is the same class CLAUDE.md's own Rule 4 correction names -- a
record that **promises a control the estate does not have.** ⛔ **DO NOT REBUILD THE ALARM.** The
moratorium stands and the teardown was correct; the remedy is to strike or amend the comment.

**PLACEMENT (mine, per CTO 64391 "COO's to place, no clock"):** both items are record-hygiene on ONE
file in ONE touch --
  (i) a `frozen_by_retirement` annotation on the two partitions naming the Andrew-direct date
      (2026-07-29), the verbatim instruction, and `@c79b4537ca`;
  (ii) strike/amend the `:22` freshness-alarm sentence.
⛔ **NOT AUTHORIZED BY THIS RECORD AND NOT A GATE.** A TF edit is an apply act; CTO explicitly fenced
their ruling as a direction call, not a GO. It carries **no clock** and should **ride an existing
globgrph-touching window rather than open one** -- the same disposition `main.tf:191/:193` received
tonight, and for the same reason: a durable artifact beats a transient correction, and whoever next
touches this file inherits both items in one place.

-- 2.0.0_SA_COO, 2026-08-21
