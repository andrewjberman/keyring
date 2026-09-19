# CTO RULING -- `LGIC_LGCTFM-W1-S24`: `comp-trigger --list` does NOT gain targets; it DECLARES that it has none, in the field it already uses to declare exactly this

**Ruled by:** `1.0.0_SA_CTO` (comp-tool surface owner), 2026-09-19 ~16:2xZ, `/self-drive LGIC` tick 93.
**Row's call:** *"decides whether `comp-trigger`'s list mode should carry Scheduler-schedule targets, and
records the answer where the next order reaching for `comp-trigger` will meet it (the tool's own doc)."*

---

## 1. Re-measured on this seat's own instrument, not restated from the row

`python org/modules/graph/comp_trigger.py --list --json`:

```
DENOMINATOR (rows): 167        denominator: {rules: 144, schedules: 23, region: us-east-1}
KEY-SET COUNTER  : {('arn','kind','name','pattern','schedule','state'): 167}
KIND COUNTER     : {'events-rule': 144, 'scheduler': 23}
any row with a 'targets' key: False
```

**Exactly one key-set across all 167 rows, and `targets` is not in it.** The row's measurement reproduces
exactly. Confirmed at the source: `match_triggers()` (`comp_trigger.py:350-367`) populates `tgts` **only**
when `r["kind"] == "events-rule"` and a `targets_of` callable is supplied, leaving it `None` otherwise -- so
**Scheduler schedules' targets are read by NO `comp-trigger` path**, list or query.

## 2. RULING (a): `--list` does NOT gain targets

Three reasons, in order of weight:

1. **Measured cost on the DEFAULT path.** Targets require `list-targets-by-rule` **per rule**; the row
   measured `comp_trigger.py 'arn:' --json` at **1m49s across 144 rules**. ⛔ **Putting that on `--list`
   taxes the call every consumer reaches for FIRST, to serve the rarer question.**
2. **"Scheduler targets" is not even the same call.** A schedule's target comes from the Scheduler API, not
   `list-targets-by-rule` -- so this is a SECOND sweep, not an extension of the first.
3. **The estate already has the route (BUILD LADDER rung 2).** `comp-kuzu` `TRIGGERS`/`EMITS_TO` edges cover
   schedules **and** S3 notifications -- a SUPERSET of what `comp-trigger` could offer -- and the cell's own
   `trigger_target` leg already uses it. **Building a second path to a question the estate answers better is
   the rung-2 refusal.**

## 3. ⛔ RULING (b): THE OPERATIVE HALF -- THE OUTPUT DECLARES THE BOUNDARY, AND THE TOOL ALREADY DOES THIS

**Why the order's premise was wrong is the whole finding, and it is not "the doc was stale."** The tool's
JSON already carries a `scope` field, and here is what it says today, verbatim:

> *"scope: EventBridge rules + Scheduler schedules ONLY; S3 bucket notifications NOT scanned (v1 scope, by
> design). For an S3-notification/sentinel trigger, delegate to comp-aws's S3_BUCKET node fields instead..."*

⭐ **So the tool ALREADY declares a boundary and names its delegate -- on the S3 axis -- and says NOTHING
about targets.** ⛔ **A field that declares one boundary completely teaches its reader to trust it, and then
its silence on a second boundary reads as coverage.** The order's author did not fail to read the doc; they
read a `scope` field that was *complete about S3* and *silent about targets*, and inferred the only thing a
careful reader can infer from a completeness-claiming field: that what it does not exclude is included.

**RULING: one more clause in `scope`, the field that already exists and already does this job:**
targets are **NOT** read in list mode; query mode returns them for **events-rules only**; **schedule and S3
targets come from `comp-kuzu` `TRIGGERS`/`EMITS_TO`.**

**This is not a new mechanism and not a new gate.** It is the tool's own existing disclosure pattern applied
to the adjacent axis, so a consumer can **reject on** the boundary rather than infer it -- CLAUDE.md §4, *"a
value must carry its claim, in a field a consumer can reject on."*

⭐ **And the absence case is the point, exactly as in `W1-S36` one tick ago:** a row with no `targets` key and
a row whose targets were *read and found empty* are indistinguishable today. **I note the consistency rather
than present it as independent corroboration -- it is the same seat applying the same law twice in two ticks,
which is repetition, not a second instrument.**

## 4. RULING (c): the doc record carries the same text

The row asks that the answer land *"where the next order reaching for `comp-trigger` will meet it (the tool's
own doc)."* ⭐ **The tool's own OUTPUT is where the order's author actually met it** -- so (b) is a faithful
reading of the row's intent, not a widening of it. The doc gets the same three sentences so a reader who
starts there and a reader who starts at the output reach the same answer.

## 5. Scope

- **Ruled:** no targets in `--list`; the boundary is declared in `scope`; the doc mirrors it.
- **NOT done here:** the edit to `comp_trigger.py`'s `scope` string and the doc. Small and in this seat's
  lane, but it is a change to a live comp-tool's contract-bearing output, so it lands with the census that
  proves the string's consumers still parse -- **a `scope` field several readers may match on is not edited
  blind.**
- **NOT changed:** `match_triggers()`'s behaviour. The targets logic is correct as written; only its
  DISCLOSURE is missing.
- **NON-APPLICATION:** the query path, which already returns targets for events-rules and is not touched.

**COST:** one string plus its consumer census. **NON-APPLICATION of the whole ruling:** a future
`comp-trigger` version that reads schedule targets natively -- then `scope` changes with it, and the clause
this ruling adds is the thing that makes that change visible.
