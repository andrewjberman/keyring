# /self-drive D2 — tick 109

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` (:07/:37) · **UTC:** 2026-09-01 ~09:5xZ
**Ticks covered:** 106–109 · **Carrier:** `org/XXX.md` @`e706f59f62` · **Paired:** `/drive` @ `2.0.0_SA_COO` (`b8ac5fba`)

---

## Scope + completion

```
D2 -> 10 projects   device: laptop
COMPLETION: 2 of 10 carry the 'complete' token -> NOT DONE
register open_tos: 23  <- INSTRUMENT UNDER WITHDRAWAL, see §3
```

## The tick that mattered: an instrument was withdrawn, including mine

**`2.0.0_SA_COO` withdrew a METHOD, not two dispatches.** It quoted line 8 of a task-order face and
never opened line 87 **of the same file**, where its own ruling from three days earlier discharged
the criterion — then dispatched a seat to re-derive it. That seat spent three hops, a deployed-bytes
hash verification and an AST walk to independently reproduce a ruling with COO's own name on it.

**Every D2 open-count reported tonight — 22, 22, 23, 23, 23, 23 — came from a regex reading the
first line of a `<status>` block.** A status block is not the face. The discharge sat 79 lines below
and the instrument could not see it by construction.

### CTO ruling @91204

- **An open-count over task-order faces requires a full-face read.** Counts from a status-block grep
  are WITHDRAWN pending re-derivation. Not new law — rule 21 already names qualifiers and intra-file
  contradictions as *the things a grep of one file structurally cannot show*.
- **The general form:** a field at the top of a record is the author's summary; a correction appended
  below it is the record's actual state. An instrument reading the first reports the author's
  intention at authoring time — the one quantity nobody needs.
- ⛔ **My own completion test was placed inside that doubt before anyone raised it.** It read two
  fields per project JSON — the same shape. Bounded, not withdrawn.
- **NOT ordered:** a re-derivation of every count tonight. They feed a stop-condition at 2 of 10;
  re-derivation happens when a count becomes load-bearing.

## Driver act: I applied my own ruling to my own instrument (tick 108)

The completion test now also scans `phase`/`blocking` for correction markers.

```
49–50 correction markers across 6 of 10 member records
   ADVI_PERFRP 22 · ADVI_49F 11 · ADVI_INSURE 8 · OPAL_ADVIPOINTERS 6 · BDPARITY 2 · ROSTERCOLS 1
DISCRIMINATING RESULT: markers cluster ENTIRELY in ACTIVE projects.
   BOTH records reading 'complete' carry ZERO -> the stop-condition is NOT exposed to this class.
```

⭐ `3.0.0_SA_CVO`'s framing, worth keeping: **the difference between reporting an exposure and
reporting an exposure's reach.**

## Verdicts landed — ledger 26 → 30

| Tick | Call | Outcome |
|---|---|---|
| 106 | null stage waives an alignment gate | adopted, **sharpened** — the waiver is silent *in the verdict* and disclosed *in prose*, which is worse |
| 106 | done-bar 22 vs register 23 | adopted — a bar names a **set**, not a running count; does not move, does not go to Andrew; CVO required a discriminating test |
| 107 | object identity | **measured at source by this seat** — the publish path is a BYTE CARRY, not a serialisation; gap 1 closed, gap 2 (census vintage) named and left open rather than inferred |
| 108 | complete projects reading mid-pipeline | **CVO measured instead of routing** — 291 of 298 complete projects carry a null stage; **status is authoritative by elimination** and the stop-condition is correct |

⛔ **On 108 I asked the wrong question and it surfaced the right one.** I asked *"which convention is
it?"* There is none to recall — the field has **no defined close semantics** and those two records
are 2 of 7 in an inconsistent minority. The live question is whether the field should be declared
meaningless after close and read by nothing.

## Corrections against this seat, ticks 106–109

- **CVO:** routing both halves of the push finding as one architecture item risked **the immediate
  half inheriting an architecture timeline.**
- **CVO:** *"same instrument"* was the secondary question; *"same object"* was load-bearing, and I had
  asserted it inside a never-widen ruling.
- **`0.4.0_DE_ClientPlatform~D`:** corrected my claim about its own census — the three signed leaves
  rest on **pre-fix artifacts**, producer changed twice since.

## RESERVED cards still at Andrew

- D3's order relative to D8.
- Whether the flow-ingestion defect widens the ruled 22.

## Compiler Tools

`directives-check.py --json` · a python completion scan over 10 member JSONs **extended this tick**
with an intra-record correction-marker scan · direct source reads of `d_publisher_port.py`
(publish path) · `comp-find` for the emitter registry · `git ls-remote` for every push-state claim.
No `head` on any census.

**State:** `ARMED` · next tick on the cron.
