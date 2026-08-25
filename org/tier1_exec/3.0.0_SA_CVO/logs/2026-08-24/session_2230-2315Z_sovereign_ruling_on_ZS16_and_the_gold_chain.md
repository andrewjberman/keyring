# Andrew rules Z-S16 sovereignly, gold runs ad-hoc, and the chain nobody had stated — `3.0.0_SA_CVO~Z`

**archetype:** VALIDATE
**Seat:** `3.0.0_SA_CVO~Z` (site Z) · **This entry:** ~22:30Z → ~23:15Z
**Predecessors:** `session_1955-2110Z_...` @`5b4c6ba991` · `session_2110-2230Z_...` @`f3c1c1d368`

---

## Objective

Hold the channel through the post-fire window, and keep the CODE-vs-EXERCISED and
ad-hoc-vs-scheduled distinctions from blurring at the moment they became easiest to blur.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `jsonschema` (protocol s.8) | every append, 8 this window | VALID each time | Also swept my own rows for **ARMED with no recorded disarm** — found Z-S17, see §3. |
| `aws s3api list-objects-v2` | explicit token walk, twice | 4,070 keys / 5 pages · 137 rules, `NextToken` absent | Materialised then filtered client-side, per the banked pagination rule. A `--query` over a page would have answered both questions wrongly. |
| `safe-commit.sh` | 8 commits, `-F` msgfiles via Write | ALL CLEAN | — |
| `comp-closure` | **not run** | — | Off the directives item per Andrew ~21:4xZ; its findings travel the tooling route. |

**Gap found:** none in the comp-tools. Two of my own ad-hoc controls failed to fire (§4).

---

## Work Completed

### 1. Andrew ruled Z-S16 sovereignly, and wider than the spec reading
> *"all downloaded information from the providers platforms (trueshares and pathfinder) should have
> some kind of 'as of' field... that needs to be what is used for any date stamping on provenance.
> it is fine to track metadata of when we've updated data... but that is a very different figure...
> maintained from bronze ingestion onward"*

It settles the row: **the provider's as-of stamps provenance.** It also settles the half I had
deliberately not asserted — operation metadata is legitimate and is a *different* figure, so
`_ingested_at` was never the defect. **"From bronze ingestion onward" makes it a chain property.**

**And it has a clock:** invisible on the served surface today *only* because DIVZ/IDVZ are shells in
gold. **Tomorrow's 13:00Z fire is when the wrong as-of reaches a served artifact.**

**Then DE~Z scoped the remedy back down** by diffing the two platinum versions: 2,384 leaf fields,
**one** differs (`/generated_at`); `data_as_of` unchanged. **The serving layer already implements his
contract**, so the remedy is **bronze→silver only** — a real reduction in DS~Z's cell, arriving
before they cut it.

### 2. Gold ran — and I pinned which run
`opal-data-etfs/gold/` went **0 → 3 objects** at 22:56:44Z, `run_class: "adhoc"` in the manifest.
The scheduled `cron(0 13)` does not fire until 13:00Z tomorrow, so **this is AC3's exercise, not
AC7's evidence.** F6's *"gold/ = 0 objects"* is superseded. Recorded at landing time because
**downstream these artifacts are byte-identical to what the scheduled run will produce.**

### 3. Items minted, and one error of my own
- **Z-S24** — D4's placement is stale on `origin/SITEZ` while `origin/CLOUD` carries the superseding
  text, **and CLOUD's row cites its proof commit as living on SITEZ.** So **this staleness survives
  checking the record**, because the record is on the stale side.
- **Z-S25** — three keys share the leaf `positioning_data.json`. My framing measurement: **50 leaves
  in that bucket collide 3+ times**, so the collision is the *unremarkable* half; the hazard is the
  **age spread with live successors** (Rule 25's key-migrated signature).
- **Z-S26** — filed as a **NON-DEFECT**: gold's as-of needs **both** silver *and* `bbg/{date}/`, so
  **A5 is the precondition for gold advancing**, and an L1 failure produces an artifact **identical
  in shape to tonight's correct one.**
- ⛔ **Z-S17 — my own error.** I de-gated it on Andrew's word and **let a DE-GATE read as a DISARM.**
  Routing is not disarming. **A fused-axis error in the channel whose own protocol exists to separate
  those axes** — de-gating changed round-*gating*, not hazard *standing*. It sat ARMED and unwatched
  for over an hour. Found by sweeping my own rows for exactly that shape.

### 4. Adjudicated a live disagreement between two seats
CTO~Z reported platinum unmoved; DE~Z reported it wrote. **Both were right.** Measured:
`76,149 B → 76,149 B`, **ETag changed**, new manifest at 23:00:45Z — **after** CTO~Z's read.
**Nobody was wrong; the state moved between two correct observations.**

I reported the identical size as *why* they disagreed and treated it as a fortunate diagnostic.
**DE~Z asked why the sizes matched**: the only mutable field is a fixed-width timestamp. **A
size-based check does not occasionally miss such a write — it misses it every time, by
construction.** *"A coincidence you cannot explain is a finding you have not finished."*

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Filed Z-S26 as a **non-defect** | The guard is correct and well-designed. The value is the chain, not a fault. |
| Refused to conflate gold's `date=2026-08-21` with Z-S16 | One is a **partition-level calendar** selection (NEVER#1 working); the other a **row-level** substitution. Conflating them manufactures a Rule-17 finding out of a correct guard. DS~Z and MSTR~Z drew it first. |
| Recorded the ad-hoc gold run's provenance **at landing time** | Downstream the artifacts are byte-identical to the scheduled run's. In an hour nobody could tell from the bucket. |
| Stated Z-S17's standing against myself rather than letting the de-gate stand as handling | De-gating removes an item from the round's attention **without disarming it** — safe-and-invisible. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md` | 23 → 26 items; Z-S16 ruling + scoping; Z-S17 standing; Z-S12 reframe | Yes — `c6e49baf33` … `9a04b1ac5a` |

**Push state:** earlier work is on `origin/SITEZ`; this window's commits are **LOCAL** and ride the
next integration window.

---

## Blockers

**None at this seat.** Z-S16's remedy is DS~Z's cell, cut by COO~Z, on CTO~Z's ruling.

---

## Current State

**The pipeline works end to end at the silver tier and has a schedule at the gold tier** — but the
gold schedule has **never fired**, and that is AC7.

**Z-S16 is the only BLOCKING item open**, now sovereignly ruled, remedy scoped to bronze→silver, with
a deadline set by a fire nobody controls.

---

## Next Steps — TOMORROW, IN ORDER, AND THE ORDER IS THE POINT

1. **07:00 ET — Z-S5.** MSTR~Z's post-fire read of `RC_CONS` + the constituents manifest.
2. **~11:00Z — the L1 fire.** ⛔ **CHECK `bbg/2026-08-24/` LANDED. This is Z-S26 and it is the
   load-bearing check of the day:** if it did not land, gold steps back to 08-21 and the shells stay
   shells — **and the output looks identical to tonight's correct run.** *The thing to verify is not
   "did the shells fill" but "did the bbg partition land"; the shells are downstream of that.*
3. **13:00Z — TO-5 AC7**, the first **scheduled** gold fire. Read the invocation record, not a
   report. **This is also when Z-S16 reaches a served artifact** if the converter is unfixed.
4. **[`3.0.0_SA_CVO~Z`]** Round v1 cannot close while Z-S16 stands, and per the bar bound at Z-S18,
   not until exercised criteria close on measurement rather than on a declared-unmeasurable.
