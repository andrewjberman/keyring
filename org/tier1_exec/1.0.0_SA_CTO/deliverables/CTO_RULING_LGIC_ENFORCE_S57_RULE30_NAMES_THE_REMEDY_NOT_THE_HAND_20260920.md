# CTO RULING -- `LGIC_ENFORCE-S57`: Rule 30 names the REMEDY, not the HAND -- and the registry lane is ABSOLUTE for a SEAT, CONDITIONAL for a WORKER

**Seat:** `1.0.0_SA_CTO` (the row's `disarm_owner`) · **Date:** 2026-09-20 · **Device:** laptop · **Branch:** CLOUD
**Row:** `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md`, `LGIC_ENFORCE-S57`
(surfaced `2.0.0_SA_COO~G` 2026-09-16T16:07Z, class BLOCKING, `hazard_standing` ARMED)

---

## 0. THE QUESTION, TAKEN FROM THE ROW'S OWN BYTES

The row routes exactly one thing to this seat, in its `notes`, verbatim:

> `! THE ONE THING THAT WOULD CHANGE MY READ is if Rule 30's 'a builder REFUSAL is a missing
> registry row to add' is meant to grant the refused seat the row-add; on the bytes, it names
> the remedy and not the hand, and no lane entry carries it.`

⛔ **This seat carried a WIDER restatement of that ask into its own tick notes** -- *"OWED: either a
seat-facing route for `infra/logic/registry/**` or an explicit ruling that every such write rides a
worker grant."* **That sentence is not in the row.** It is ruled on here only because the row's real
question, once answered, reaches it; the authority is the row, not the restatement. (`MEMORY.md`:
*check a ruling against the ruling -- your own restatement is the most dangerous copy.*)

---

## 1. RULED: **NO.** Rule 30 does NOT grant the refused seat the row-add. `2.0.0_SA_COO~G` read it right.

`CLAUDE.md` Rule 30, at the bytes: *"a builder REFUSAL is a missing registry row to add
(`infra/logic/registry/`), **never a hand-typed workaround**"*.

1. **The sentence's own contrast is OBJECT-vs-OBJECT, not HAND-vs-HAND.** Its two terms are *a
   registry row* and *a hand-typed workaround* -- both are answers to WHAT THE REMEDY IS. Nothing in
   it selects a performer, and it names no serial. The reading that grants the refused seat the
   row-add has to supply the missing half itself.
2. **Supplying it would be an agent-made lane widening inferred from a law sentence.** `CLAUDE.md`
   §2: *"NEVER convert Andrew's word to ONE agent into a gate/stop on another -- verbatim scope;
   relay, never adjudicate wider OR narrower; if wider seems plausible, ASK."* Widening is the same
   defect as narrowing, and a grant read out of a silence is the widest possible reading.
3. **Rule 30's own purpose cuts against it.** The rule exists so that *"homes, tenancy and names come
   from the canon and its builders, never from a seat's judgment."* `PLATFORM_LOGIC_DOCS` keeps the
   registry out of the hands of the projects it grades -- and `LGIC_ENFORCE`, a project whose whole
   subject is grading names against that registry, is precisely such a project. A self-granting
   reading would collapse the separation exactly where it was built to hold.

**`2.0.0_SA_COO~G`'s split stands as cut:** the measure-and-record half inside the project, the
registry-write half routed to `4.0.0_SA_CRO`. No lane is widened here, and none is asked for.

---

## 2. MEASURED AT HEAD, AND IT IS THE HALF THE ROW DID NOT REACH: the constraint is **ABSOLUTE FOR A SEAT** and **CONDITIONAL FOR A WORKER**

### 2a. The lane, re-measured today on the files that ACTUALLY EXIST

`git ls-tree -r --name-only HEAD -- infra/logic/registry/` returns **SIX** files: `exemptions.json`,
`remediations.json`, `resources.json`, `scopes.json`, `systems.json`, `tiers.json`.

⚠ **`refused_keys.json`, named in S57's own evidence line, IS NOT AMONG THEM** -- `LGIC_ENFORCE-S58`
caught that and is right; refused keys live inside `systems.json`. **It does not touch this finding:**
a lane grant resolves BY PREFIX and never tests that the path exists, so the lane answer is the same
either way. It is recorded because S57's evidence reads as though the file were measured.

`.tools/owned-paths-validate.py --check-agent`, path piped explicitly on stdin (an EMPTY stdin admits
every serial), worktree clean against HEAD on `.owned-paths.yaml`, **6 files x 4 serials = 24 reads:**

| path (all six) | `1.0.0_SA_CTO` | `2.0.0_SA_COO~G` | `0.9.0_WK_LGIC_ENFORCE~1` | `4.0.0_SA_CRO` |
|---|---|---|---|---|
| `infra/logic/registry/*.json` | **REFUSED** | **REFUSED** | **REFUSED** | **PERMIT** |

Lane `PLATFORM_LOGIC_DOCS`, `permitted_agents` exactly `['4.0.0_SA_CRO', '4.0.0_SA_CRO~A',
'4.0.0_SA_CRO~B', '4.0.0_SA_CRO~C', '4.0.0_SA_CRO~D']`. **The CRO PERMIT is the positive control** --
the lane resolves and admits somebody, so this is a real grant boundary and not a broken read or a
blanket refusal. **S57's premise is CONFIRMED UNCHANGED at HEAD**, as `LGIC_ENFORCE-S70` confirmed it
on 09-18, now re-measured two days later on the real file set.

### 2b. Why a SEAT can never get there, at the source

`.tools/owned-paths-validate.py:330` consults the fifth clause, and `_owns_task_order_paths:218-220`:

```
218      m = _WORKER_SERIAL_RE.match(agent.strip())
219      if not m:
220          return False
```

`_WORKER_SERIAL_RE` (`:123`) is `^0\.9\.0_WK_(?P<code>[A-Z0-9_]+?)[~_](?P<n>[0-9]+)$`. **A non-worker
serial fails it and returns False before any grant is read.** Clauses 1-4 (exact match, tilde-strip,
`org/<tier>/<SERIAL>/(logs|task_orders)/**`, `deliverables/<SERIAL>/`) cannot reach `infra/logic/**`
either. ⛔ **So for a SEAT the lane enumeration is the ONLY door, and there is no route to build --
which disposes of the wider restatement in §0: a "seat-facing route" is not a thing this mechanism
can express.**

### 2c. Why a WORKER can, and it has been EXERCISED

`worker_grant`: `{serial_glob: '0.9.0_WK_*', source: 'task-order-paths'}`. A worker is admitted to
exactly the `<paths>` a **non-terminal** order under its own `<CODE>`, `issued_to` that serial, names
at HEAD. ⛔ **`_worker_orders(root, code)` (`:176-206`) never asks WHO ISSUED the order or what lane
the issuer holds.**

**Exercised, measured, not inferred:** `org/missions/D14/LGIC/LGIC_CANON/task-orders/
LGIC_CANON.TO-CN-o-5-r4.checklist-first-run.md` -- `issued_to 0.9.0_WK_LGIC_CANON~1`, `<paths>` names
**`infra/logic/10_ONBOARDING_CHECKLIST.md`**, a `PLATFORM_LOGIC_DOCS` path. `status: complete`.

⭐ **ALREADY ON THE RECORD, AND NOT THIS SEAT'S TO RE-FILE:** `LGIC_CANON-S21` states it in its own
words -- *"a SEATED WORKER reaches it through worker_grant on the order's `<paths>`, exactly as CN-o-5
did, and the CRO is the writer for any act taken outside a cell."* Its `disarm_owner` is
`2.0.0_SA_COO~G`. **NO NEW ROW IS FILED HERE.** A census of all 433 LGIC channel rows found 5 naming
the clause; this limb cites the carrier rather than minting a sixth. *(The check that produced this
was run BEFORE claiming novelty -- last tick this seat over-billed a finding as "sharper than the
caveat" and was falsified; "novel" is a claim with a denominator.)*

### 2d. Standing state today -- an EXPOSURE, not an INCIDENT

**718 tree task-order files at HEAD across 19 codes; 45 NON-TERMINAL; `0` of the 45 names ANY
`infra/logic` path.** No standing worker grant on the registry exists right now. CN-o-5-r4 is
`complete`, and a terminal order grants nothing -- **so the exercised-route reading and the zero agree
and each explains the other.** Rule 22's negative mirror: the route is REAL and has been TAKEN once,
historically, inside the lane's own subject-matter project; it is not open today. **Nothing is
re-opened.**

---

## 3. ⛔ THE CONSEQUENCE THE SPLIT NEEDS SAID PLAINLY: "ROUTE IT TO THE CRO" IS A DISCIPLINE AT THE CUT, NOT A GATE

A COO that names `infra/logic/registry/systems.json` in a worker cell's `<paths>` obtains **exactly
the write the lane refuses that COO itself.** The validator will permit it, correctly, because
Rule 27 says the order IS the grant.

**This is the same LAW-STRONGER-THAN-TOOL shape** `CLAUDE.md` already carries twice -- Rule 27's
parenthesis (*no lane enumerates a worker*) and Rule 14a's override (*singular is a human discipline,
not a mechanism*). It is named here so the discipline is CHOSEN rather than stumbled into.

⛔ **NOT PROPOSED, DELIBERATELY: no gate, no issuer-lane check, no approval step.** Building one would
be an agent-made gate (`CLAUDE.md` §2, Andrew-direct 2026-08-04) on a mechanism Andrew ratified as
designed (ADHC_OWNPTH.005, *"recs approved"* @`9ef9a40aae`). If a limb is ever wanted, it is his card.

---

## 4. DISPOSITION

- **`LGIC_ENFORCE-S57` -- the owed item is ANSWERED, so its disarm condition is MET, and this seat,
  its `disarm_owner`, DISARMS it.** The split it cut is ruled CORRECT.
- ⚠ **THE CLOCK MOVE IS `3.0.0_SA_CVO`'s TO WRITE (R-19).** Disarming is not disposing; this document
  disposes nothing and carries no `adjudicates`.
- **NOT DONE HERE, named so the silence is not read as a verdict:** `LGIC_ENFORCE-S56` is untouched
  (`S70` already restated it and its premise had moved); `LGIC_CANON-S21` is `2.0.0_SA_COO~G`'s row
  and is cited, not moved; `LGIC_ENFORCE-S58`'s nonexistent-path finding is confirmed in passing and
  its own disposition is not this seat's; **no lane is widened and none is asked for.**

## 5. INSTRUMENTS

`git ls-tree -r --name-only HEAD`; `.tools/owned-paths-validate.py --check-agent` x24 with the path
piped explicitly and `4.0.0_SA_CRO` as the positive control; source read of `check_agent:275-334`,
`_owns_task_order_paths:209-235`, `_worker_orders:176-206`, `_WORKER_SERIAL_RE:123`; the module's own
`_worker_orders` over all 19 codes (denominator 718 files / 45 non-terminal orders printed);
`git show HEAD:<order>` on CN-o-5-r4; a 433-row parse of all four LGIC surprise channels for prior
carriers of the worker-grant clause. **A first pass at the order census returned `0 codes` on a wrong
glob (`task_orders/` for `task-orders/`); it was re-run with a positive control, which is the only
reason the zero was not published.**
