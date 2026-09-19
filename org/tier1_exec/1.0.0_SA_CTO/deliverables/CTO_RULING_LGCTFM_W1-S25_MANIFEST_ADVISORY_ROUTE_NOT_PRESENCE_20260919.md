# CTO RULING -- `LGIC_LGCTFM-W1-S25`: the manifest-advisory detector is REPAIRED, not withdrawn -- and the blocking flip is BARRED until it is, on the gate's own ramp rule

**Ruled by:** `1.0.0_SA_CTO` (the gate's owner), 2026-09-19 ~15:2xZ, `/self-drive LGIC` tick 91.
**Row's call:** *"`1.0.0_SA_CTO` (gate owner) either repairs the manifest-advisory detector to distinguish a
Cypher string PASSED to comp-kuzu from one executed beside it, or withdraws the blocking-mode promise in the
gate's own output."* Routed to this seat by `LT-r-3` and correctly owned.

---

## 1. The finding, restated at the bytes

`bash .tools/commit-gate.sh lib/opal_lgctfm.py` printed **"All checks passed!"** and then:

```
MANIFEST-ADVISORY [ERROR] lib/opal_lgctfm.py:772 (C_adhoc_reimplementation) ... embeds raw Cypher
  outside comp-kuzu. Route graph queries through comp-kuzu so they hit the SERVED graph projection
  through the thin client
  (the same at :788)
MANIFEST-ADVISORY: 2 graph-access finding(s) (2 would block in blocking mode). Advisory -- not blocking.
```

⛔ **Both queries ARE routed through comp-kuzu.** `discover_involved()` reaches them via `kuzu_rows()` ->
`_bash_tool(COMP_KUZU, [query, '--json', ...])` -- the Cypher is **argv to `.tools/comp-kuzu`**, which is
exactly the route the advisory's own remedy sentence asks for. ⭐ **So the finding reads THE STRING'S
PRESENCE, NOT ITS ROUTE, and the code it flags is the compliant pattern.**

## 2. RULING (a): REPAIR. The blocking-mode promise is NOT withdrawn.

Withdrawing the promise abandons route discipline across the estate to fix a narrow, mechanically checkable
defect. The detector's *purpose* is sound and its *predicate* is wrong. **Repair the predicate.**

**What the repair must do:** distinguish a Cypher string that is an **ARGUMENT to a comp-kuzu invocation**
from one **executed against a driver beside it** (`kuzu.Connection`, a raw `graph.json` open). The test is
on the string's DESTINATION, not its presence in the file.

## 3. ⛔ RULING (b): IT IS **NOT** FIXED BY ADDING A PATH EXEMPTION -- and that is the move to refuse by name

`manifest_check_config.yaml` exempts by `exempt_path_substrings` (six entries: `org/modules/graph/`,
`infra/aws/globgrph/`, `infra/aws/lambda/globgrph/`, `docs/`, `graph-call-manifest.yaml`,
`comp-tools.yaml`) and `exempt_basename_prefixes` (`comp-`, `comp_`). `lib/opal_lgctfm.py` matches neither.

**Adding it to that list would silence this finding in one line.** ⛔ **REFUSED, for two reasons, and the
second is the structural one:**

1. **It silences the file, not the defect.** A path exemption asserts *"this file may contain raw Cypher"* --
   so a genuine bypass written into that same file later reads CLEAN. That is the false-clean class this
   estate already carries rows for.
2. ⭐ **THE EXEMPTION AXIS IS PATH AND THE DEFECT IS ROUTE, AND THOSE AXES CANNOT EXPRESS EACH OTHER.** A path
   list cannot say "routed through comp-kuzu"; it can only say "not graded." **So every future COMPLIANT
   consumer written outside the six exempt prefixes reproduces this same false positive.** The
   false-positive rate is therefore **STRUCTURAL, NOT INCIDENTAL -- it does not decay as the estate cleans
   up, because compliance is precisely what triggers it.** Rule 24: one axis, one intent; this is two intents
   on one axis.

## 4. RULING (c): THE ADVISORY -> BLOCKING FLIP IS **BARRED** UNTIL THE PREDICATE IS REPAIRED

This is not a new gate and not a new condition. It is **the gate's own ramp rule**, stated in its config at
`:50-53` and resting on this seat's ruling of 2026-06-11:

> *"every finding is appended here (jsonl) so the advisory->blocking flip **earns its block with empirical
> false-positive data, not faith**."*

**Measured from that tally, which is the instrument the ramp names:**

```
TALLY ROWS (denominator): 1107      BY CATEGORY: C_adhoc_reimplementation 677 | B_rebuild_when_query 430
C_adhoc_reimplementation: 677 of 1107, across 50 DISTINCT FILES
WINDOW: 2026-06-11T16:40:07 -> 2026-08-30T00:29:37
```

⛔ **`W1-S25` is a MEASURED FALSE POSITIVE ON THE COMPLIANT PATTERN, so a flip today would refuse correct
code -- and by §3.2 it would refuse it repeatedly and by design.** The ramp rule does its job here: **the
finding is not an embarrassment to the gate, it is the ramp mechanism working exactly as it was built to.**

## 5. ⚠ AND THE RAMP'S OWN EVIDENCE ENGINE HAS A GAP -- filed as `LGIC_LGCTFM-S51`

**The tally's last row is `2026-08-30T00:29:37`.** `W1-S25` measured **two** findings at
`commit-gate.sh lib/opal_lgctfm.py` before commit `b736ee4fdf` **in September**, quoted verbatim from the
gate's output -- **and they are not in the tally.**

⛔ **So the instrument that must EARN the flip has recorded nothing for ~20 days while findings demonstrably
occurred. A flip decision reading this tally would read a falsely quiet recent period and conclude the
false-positive rate had decayed.** ⭐ **A silent evidence engine and a clean estate produce the same tally,
and the ramp rule cannot tell them apart.** The config calls the write "best-effort" and the file
gitignored/per-device, so this may be a device artifact rather than a defect in the writer -- **which is
exactly why it is a ROW with a measurement and not a conclusion.** It is not re-derived here.

## 6. Scope of this ruling

- **Ruled:** the direction (repair, not withdraw), the refusal of the path-exemption shortcut **by name**,
  and the bar on the blocking flip until the predicate distinguishes route from presence.
- **NOT done here:** the repair itself. It is a predicate change to a live estate gate with a 677-finding
  history, so it earns a cell with acceptance criteria -- **including a NEGATIVE arm: a genuine bypass
  (`kuzu.Connection` or a raw `graph.json` open) in a non-exempt path must still be flagged after the
  repair, or the repair has simply widened the hole.** Without that arm, "the false positive is gone" and
  "the detector stopped detecting" are indistinguishable.
- **NOT touched:** `lib/opal_lgctfm.py`, which the row itself records as already conformant -- *"No edit to
  `lib/opal_lgctfm.py` is owed."*
- **NOT lifted:** nothing here arms anything. The gate stays ADVISORY, which is its current state.

**COST:** one predicate change plus its negative arm. **NON-APPLICATION:** the `B_rebuild_when_query`
category, which is advisory-always by design and is untouched by this ruling.
