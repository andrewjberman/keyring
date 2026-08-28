# PRE-DEPLOY SERVED BASELINE — `category-views`, 4 scopes — captured before ACT 1

**Captured:** 2026-08-28T17:12:55Z by `3.0.0_SA_CVO~Z`, from the SERVED edge
(`GET https://opalinvest.dev/api/general/mdpf/{scope}/category-views.json`, authenticated).
**Producer vintage carried by the bytes:** `as_of 2026-08-27`, `written_at 2026-08-28T13:50:49–51Z`.

```
category-views.49financial.json   4339 B   sha256 163ea1d53e10cf829a604115fa4c305c…
category-views.cottonwood.json    5116 B   sha256 48764d7074b9ebfa5b32f481d4ee0e3c…
category-views.inflection.json    4331 B   sha256 eed9147b574175aa7e23f0cb444be7ad…
category-views.global.json        4442 B   sha256 1d07a154eec501a940496fb4b801041c…
```

---

## WHY THIS EXISTS — and why it had to be taken NOW

Andrew approved the D1_CATVIEWS ship at ~17:0xZ **on stated incomplete information**: the sweep that
discharged the four known blockers was declared NON-EXHAUSTIVE by its own author, and the pin advance
`bf74d031c1 → 70a0828226` carries **1,381 lines across 6 modules** that nobody has reviewed
(`1.0.0_SA_CTO~Z` 13511/13512; figure independently re-derived at this seat — 6 files, 1,310
insertions + 71 deletions).

`1.0.0_SA_CTO~Z`'s ACT 1 acceptance predicate (13514) is sound and this does **not** replace it. But
that predicate checks the fields we **predicted** would move — 49financial's `SMA.aum`, `Client.aum`,
the `absent_reason` — with cottonwood/inflection as an UNMOVED control. **The residual Andrew accepted
is precisely the possibility of a field nobody predicted.** A field-list check cannot see that; only a
whole-object diff can.

⛔ **AND A WHOLE-OBJECT DIFF IS IMPOSSIBLE WITHOUT A PRE-DEPLOY SNAPSHOT.** The producer rewrites these
objects on every fire. The moment ACT 1 lands and the next scheduled fire runs, the "before" ceases to
exist anywhere. **The capture window closes at the deploy, which is why this was taken before it and
not asked for after.** This is instrumentation, not a gate: nothing here blocks ACT 1.

---

## THE RECIPE — run this AFTER the first scheduled fire that follows the ACT 1 deploy

```bash
# 1. re-fetch the same four scopes, same route, into a DIFFERENT directory
#    PATH HAZARD, MEASURED ON THIS BOX 2026-08-28: MSYS /tmp and the literal /tmp that native
#    Windows python resolves to C:\tmp are DIFFERENT DIRECTORIES, and C:\tmp already holds
#    same-named, same-shaped category-views files left by other actors -- so a wrong read does
#    not fail, it SILENTLY CORROBORATES. Use an absolute scratchpad path. (13485 s.5.)
AFTER=<absolute-scratchpad-path>

# 2. WHOLE-OBJECT diff, every leaf, per scope -- not a field list
python - <<'PY'
import json, sys
BEFORE = "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoZ_D1_PREDEPLOY_BASELINE_20260828"
AFTER  = "<absolute-scratchpad-path>"
def leaves(o, p=""):
    if isinstance(o, dict):
        for k, v in o.items(): yield from leaves(v, f"{p}/{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from leaves(v, f"{p}[{i}]")
    else: yield p, o
for s in ["49financial", "cottonwood", "inflection", "global"]:
    b = dict(leaves(json.load(open(f"{BEFORE}/category-views.{s}.json"))))
    a = dict(leaves(json.load(open(f"{AFTER}/category-views.{s}.json"))))
    moved = {k for k in b.keys() & a.keys() if b[k] != a[k]}
    print(f"== {s}: {len(moved)} field(s) MOVED, {len(a.keys()-b.keys())} ADDED, {len(b.keys()-a.keys())} REMOVED")
    for k in sorted(moved):    print(f"   MOVED   {k}: {b[k]!r} -> {a[k]!r}")
    for k in sorted(a.keys()-b.keys()): print(f"   ADDED   {k} = {a[k]!r}")
    for k in sorted(b.keys()-a.keys()): print(f"   REMOVED {k} (was {b[k]!r})")
PY
```

⚠ **`_provenance.written_at` WILL move on every scope — that is the fire, not a change.** Expect it and
do not report it as drift.

## WHAT THE DIFF SHOULD SHOW — and what a surprise looks like

**EXPECTED (the approved fixes), per `1.0.0_SA_CTO~Z` 13514:**
```
49financial  nodes/SMA/aum          0.00           -> 22,794,766.25
49financial  nodes/Client/aum       290,426,813.47 -> 267,632,047.22   (delta EXACTLY -22,794,766.25)
49financial  nodes/SMA/absent_reason  the "A TRUE ZERO" sentence -> GONE
all scopes   nodes/Models/... L2 member `aum` values populate where they were null
```
**POSITIVE CONTROL — cottonwood and inflection should show NOTHING but `written_at`.** If either moves
a money field, that is drift from the 1,381 un-reviewed lines and it is the thing this baseline exists
to catch.
**ANY `ADDED` / `REMOVED` key on ANY scope is a schema change nobody predicted.** Report it; do not
rationalise it.

## ⛔ THE SENTENCE THAT MUST NOT BE WRITTEN AFTER THIS PASSES

**"The artifact is now correct."**

After a fully successful ship, `global.Client` is **STILL short by $359,773,356.74**. The gap is
*exactly* cottonwood + inflection, so 49financial cancels identically **for any value of it** — the ship
moves that gap by **0.00**, confirmed independently at three seats (`2.0.0_SA_COO~Z` 13501,
`1.0.0_SA_CTO~Z` 13514, and arithmetically at this seat). A verification that reads clean on
49financial and stops there will produce exactly that false sentence, **because the scope it checked is
the scope that got fixed.**

Expect `global` to show a `Client.aum` move only as the pass-through of 49financial's change; the
**understatement itself is untouched**, and `global` will still carry a `scope_note` reading *"The
global scope carries NO category-views object — absent, not empty"* while being that object.

---

**Owner:** `3.0.0_SA_CVO~Z`. Not a gate, not a queue item, and nothing is owed to this seat to run it —
any seat closing the ACT 1 ledger entry may use it.

— `3.0.0_SA_CVO~Z`
