# DSGN_REBRND — DECOMPOSITION (L5)

```json
{
 "project": "DSGN_REBRND",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@8ad762f7bf",
 "prd_half_hashes": {"ratified-text": "SIGNED 3.0.0_SA_CVO", "brief": "SIGNED 2.0.0_SA_COO~D"},
 "author": "2.0.0_SA_COO~D",
 "cells": 15,
 "chains": 3,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~D` (L5 is the COO's; no seat certifies this before L6).
**Input:** the PRD's SURFACE MANIFEST at `8ad762f7bf`, ADMITTED — both halves SIGNED.
**Frozen at the cut.** It does not version during the round. A cell that looks wrong mid-round is a
**surprise row, never an edit** (`org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/`).

**The four binding rulings** reach every cell from the PRD preamble: light canvas `#F4F6FA` with
`#0A1733` as deliberate inverted bands · the charts keep their colour · nothing third-party is
vendored · **no cell writes to `DEV` or `CLOUD`; all work lands on `feature/d13-visual-elevation`.**

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

⛔ Written as *the printed denominator MINUS what is excluded*, never as a forward list.

```
  SURFACE MANIFEST rows at 8ad762f7bf ............................ 14   (denominator, parsed)
  minus rows marked "excluded" .................................... -1   (row 14: opalinvest.com,
                                                                          any competitor site, the
                                                                          backend API, deck_generation
                                                                          outputs, route/auth code)
  minus rows whose kind is "read" ................................. -1   (row 12)
  minus rows whose kind is "execute locally" ...................... -1   (row 13, the pinned skills)
  ------------------------------------------------------------------
  WRITE SURFACES IN SCOPE ......................................... 11
```

**The unscoped control (Rule 24's domain falsifier).** A subtraction over the wrong domain reads as
measured and is blinder than recall, so the domain itself was falsified before use: an unscoped
token sweep for AWS-surface terms over the **whole** PRD (not just the manifest) returned **0** —
`lambda`, `terraform`, `.tf`, `iam`, `s3`, `cloudfront`, `ecs`, `sns`, `ses`, `dynamodb`, `glue`.
The domain holds nothing the manifest does not hold. This is also the measured basis for
`comp-iam`'s disposition in §6.

**Status vocabulary** — four values, and **NOT-EVALUATED is one of them** so that non-evaluation
cannot be encoded as a verdict:

| value | meaning |
|---|---|
| `MEASURED` | evidence is in hand at the cut, with its instrument named |
| `DECLARED` | the PRD or brief asserts it; **not independently measured here** |
| `NOT-EVALUATED` | not looked at. Not a pass, not a fail. |
| `N/A` | the field does not apply to this surface |

---

## 2. THE RECTANGLE — 11 write surfaces × 5 fields

| # | write surface | current state | target state | collision set | evidence at cut | cell |
|---|---|---|---|---|---|---|
| 1 | `portal/design/brands/opal-capital.json` → generated `themes/opal-capital.css` | `MEASURED` — correct architecture, wrong values (brief IV.4); live via `main.tsx:7` | one writer of every token value; measured website values | none (sole writer) | `MEASURED` | RB-s-1 |
| 2 | `portal/src/index.css` (`:16`,`:40-43`,`:52`,`:69`,`:111-115`,`:132`,`:142`,`:166`,`:171`) | `MEASURED` — 9 cited lines byte-verified at portal `787015e8` | consumes tokens, redefines none | **HIGH** — 6 PRD cells | `MEASURED` | RB-s-1,2,3,5,6 |
| 3 | `portal/src/main.tsx` | `MEASURED` — theme import at `:7` | unchanged unless the generator moves | low | `MEASURED` | RB-s-1 |
| 4 | `portal/public/fonts/` | `N/A` — does not exist | Lato woff2 400/700 + OFL text beside them | none | `MEASURED` (licence text read) | RB-s-2 |
| 5 | `portal/src/ui/components/panels/` + the control components | `DECLARED` — the PRD names them the landing site; **this seat has not censused them** | one container level; one control vocabulary; four states | **HIGH** — 6 PRD cells | `NOT-EVALUATED` | RB-s-3,4,5,9,10 |
| 6 | `portal/package.json` | `MEASURED` — 4 chart libs, 2 icon sets, 2 animation libs | one of each; retired packages removed | low | `MEASURED` | RB-s-11 |
| 7 | `portal/tailwind.config.js` | `MEASURED` — dead under Tailwind v4; `primary-500` in 0 files | deleted | none | `MEASURED` | RB-s-1 |
| 8 | `portal/CLAUDE.md` "Color law" | `MEASURED` — carries the superseded silver-canvas law | rewritten in place onto the light canvas | none | `MEASURED` | RB-s-8 |
| 9 | `design/brand/COLOR_ARCHETYPES.md`; `design/systems/portal/DESIGN_SYSTEM.md`; `design/process/UI_VERIFICATION.md` | `DECLARED` — L2 read them and calls the 2026-07-15 archetype superseded; **this seat has read neither file's body** | rewritten in place, never a second archetype beside the old | none | `NOT-EVALUATED` | RB-s-8 |
| 10 | `portal/DESIGN.md` | `MEASURED` — draft exists on `feature/d13-visual-elevation` @ portal `10236236`; **absent on CLOUD/DEV** | the ratified contract; the draft is input, never authority | none | `MEASURED` | RB-s-7 |
| 11 | `design/brand/portal-routes.json`; `design/brand/portal-surface-inventory.json`; the FWD-9 pack | `N/A` — none exist | minted with printed denominators | none | `MEASURED` (absence) | RB-s-12,13,14,15 |

**Two `NOT-EVALUATED` rows are load-bearing and are stated, not smoothed.** Surfaces 5 and 9 were
never opened by this seat — the PRD names them and L2 read them, but **a PRD's assertion is
`DECLARED`, not `MEASURED`**, and the rectangle says so. Both are census obligations inside their
cells, not assumptions the cells may rest on.

---

## 3. THE CELLS — 15

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1 (`PREFIX-<axis>-<digits>`); axis `s` =
surface.

| cell | what it is | PRD candidate | serves | writes |
|---|---|---|---|---|
| `RB-s-1` | the token spine: ONE writer, the measured values, **and the two disjoint colour families** | **R1 + R8 merged** | FWD-1, 6, 7 | surfaces 1, 2, 3, 7 |
| `RB-s-2` | typography: Lato self-hosted, tabular numerals, the `font-mono` census to zero | R2 | FWD-2, 1 | 2, 4 |
| `RB-s-3` | canvas and surfaces: light canvas, navy as ink, bands enumerated, nesting collapsed, native controls styled | R3 | FWD-1, 10 | 2, 5 |
| `RB-s-4` | ordered scales: one hue, ramped light→dark | R4 | FWD-3 | 5 |
| `RB-s-5` | accent rationing and ONE control vocabulary | R5 | FWD-4 | 2, 5 |
| `RB-s-6` | focus: visible everywhere, the website's ring | R6 | FWD-5 | 2 |
| `RB-s-7` | **the contract**: `portal/DESIGN.md` authored and ratified | **R7 split, part 1** | FWD-6, 1 | 10 |
| `RB-s-8` | **the archetype rewrites + the review loop's clause-cite step** | **R7 split, part 2** | FWD-6 | 8, 9 |
| `RB-s-9` | density: the work fills the screen; a designed end state | R10 | FWD-10 | 5 |
| `RB-s-10` | empty / loading / error / no-permission: four designed states | R11 | FWD-11 | 5 |
| `RB-s-11` | one rendering system: charting, icons, animation consolidated | R9 | FWD-8 | 6, 5 |
| `RB-s-12` | **the affected-surface inventory** (route × state, denominator printed) | **R14 split, part 1** | FWD-1,4,5,10,11 | 11 |
| `RB-s-13` | **render + keyboard coverage over that inventory** | **R14 split, part 2** | FWD-1,4,5,10,11 | 11 |
| `RB-s-14` | the boundary exercise: measured parity, `design/brand/portal-routes.json` | R12 | FWD-1 | 11 |
| `RB-s-15` | Andrew's side-by-side pack | R13 | FWD-9 | 11 |

**Coverage of the PRD's candidate set: 14 of 14.** R1→RB-s-1 · R2→RB-s-2 · R3→RB-s-3 · R4→RB-s-4 ·
R5→RB-s-5 · R6→RB-s-6 · **R7→RB-s-7 + RB-s-8** · **R8→RB-s-1** · R9→RB-s-11 · R10→RB-s-9 ·
R11→RB-s-10 · R12→RB-s-14 · R13→RB-s-15 · **R14→RB-s-12 + RB-s-13**. Zero candidates dropped.

### Why the three re-cuts

- **R1 + R8 merged → `RB-s-1`.** Both PRODUCE `DesignTokens` into the same JSON. Two cells writing
  one sole-writer file is the write collision this project exists to remove; merging them is
  Rule 24(iv) state coherence — one remedy moves both, so they are one cell.
- **R7 split → `RB-s-7` + `RB-s-8`.** R7 both AUTHORS a new contract and REWRITES four incumbent law
  files in place. Different grain (Rule 24(ii)) and different risk: authoring is additive, the
  rewrite supersedes standing law that other projects read. They must be separately gradeable.
- **R14 split → `RB-s-12` + `RB-s-13`.** The inventory is an enumeration with a denominator and can
  be minted before any visual change exists; the coverage renders cannot. Keeping them as one cell
  would make an independent measurement wait on the whole spine.

---

## 4. PLACEMENT AXIS

**Every cell executes on LAPTOP.** D13 is placed LAPTOP (Andrew-direct 2026-09-11, *"it will be
laptop fabric"*); the portal submodule and the workspace design repository are both laptop-side; no
cell names a site-Z surface. **No cell is owned by a seat** — every cell is served by a worker at L7
(`0.9.0_WK_DSGN_REBRND~<n>`).

**Branch placement is uniform and binding:** `feature/d13-visual-elevation` in BOTH repos. Workers
branch their worktrees from it; the drain lands on it and nowhere else.

---

## 5. DEPENDENCY EDGES AND CHAINS

Edges are keyed to **observed completion**, not to intent: `A → B` means B's acceptance cannot be
evaluated until A's artifact exists.

```
  RB-s-1 ──┬──> RB-s-2
           ├──> RB-s-3 ──> RB-s-9
           ├──> RB-s-4
           ├──> RB-s-5
           ├──> RB-s-6
           └──> RB-s-7 ──┬──> RB-s-8
                         ├──> RB-s-9
                         └──> RB-s-10
  RB-s-12 ──> RB-s-13
  RB-s-11  (no inbound edge)
  {RB-s-2,3,4,5,6,9,10,13} ──> RB-s-14 ──> RB-s-15
```

⛔ **THE EDGES THAT MATTER HERE ARE WRITE COLLISIONS, NOT LOGICAL DEPENDENCIES, AND THAT IS THE
NON-OBVIOUS PART OF THIS CUT.** `RB-s-2, 3, 5, 6` are logically independent of one another — but
**five cells write `portal/src/index.css`** and **five write the panel primitives**. Two workers
editing one file in two worktrees produce a guaranteed merge conflict, not a race. So the collision
set, not the dependency arrow, decides the queue.

**CHAINS (connected components of the undirected edge set): M = 3.**

| chain | cells | write surfaces | disjoint from the others? |
|---|---|---|---|
| **A — the spine** | RB-s-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15 | 1,2,3,4,5,7,8,9,10,11 | — |
| **B — consolidation** | RB-s-11 | 6 (`package.json`) + a named 6-file migration set | **partially**: it touches component files chain A restyles |
| **C — the inventory** | RB-s-12, 13 | 11 (`portal-surface-inventory.json`) | **yes** for RB-s-12; RB-s-13's renders need A |

⚠ **B AND C ARE NOT CLEANLY DISJOINT AND THIS DECOMP SAYS SO RATHER THAN CLAIMING M=3 AND MOVING
ON.** B's 6 migrated files are components chain A may also restyle; C's second cell renders A's
output. The honest reading: **B is parallel-safe on `package.json` and its named file set, C's first
cell is parallel-safe outright, and both must drain BEFORE chain A's verification cells
(`RB-s-13`, `RB-s-14`, `RB-s-15`)** or those cells measure a tree that is still moving.

**Fan-out this decomposition supports:** `N = 3 of M = 3 chains, cap 8` — the L6 issuance states and
defends the final line; N is bounded above by M, so three is the ceiling, not a target.

---

## 6. BATTERY DISPOSITION

Mandatory core, each with a denominator, a blindness statement, or a reason for non-application.

### `comp-adversary` — **RUN**

`comp-adversary compose org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md`, read-vintage
HEAD `@fbfe03afe8` at 2026-09-11T08:50:36Z, rc=0.

| source | denominator | result |
|---|---|---|
| cited-commit verification | 3 attempted | **3 verified, 0 unverifiable** |
| cited-path vintage | 19 attempted | 16 stable, **3 flagged GONE** |
| uncited neighborhood | **2630** siblings | cap declared, not silent (25 shown) |
| unparsed hex runs | 4 | `10236236`, `20260911`, `787015e8`, `d4b20a28ba` |

**All three GONE flags resolved at the cut — none is a live defect, and one is an instrument
defect:**

1. `docs/architecture/D13_DESIGN_PRD.md` — **genuinely absent.** Known; it is the register's own
   dangling reference (L2 finding 4) and belongs to `0.0.0_AB_MSTR`. Not this project's.
2. `portal/DESIGN.md` — **absent at read-vintage and that is CORRECT.** It lives on
   `feature/d13-visual-elevation` at portal `10236236`; verified present there by `git cat-file -e`.
   The PRD states this; the tool reads CLOUD and cannot see a feature branch.
3. `portal/DESIGN_SYSTEM.md` — ⛔ **FALSE GONE, AND IT IS THE TOOL'S DEFECT.** The PRD cites
   `design/systems/portal/DESIGN_SYSTEM.md`, which **exists** (34,039 bytes). `comp-adversary`'s
   path parser split the nested path at the repeated `portal/` segment and then reported the
   truncation as missing. **A validator trusting the flag would have chased a file that was never
   gone.** Surfaced here; a fix is not this project's surface.

**Blindness, stated because the tool states it itself:** source 3 reports
`T11: decomposition neighborhood NOT RESOLVED (artifact carries no <decomp_ref>) -- filesystem
adjacency stands as the neighborhood`. So its 2630-sibling complement is **directory adjacency, not
the dependency chain** the spine asks a lens to walk. It cannot see this cell set's real
neighborhood, and it does not claim to. Re-running it against a task order (which carries
`<decomp_ref>`) at L7 would resolve T11; this cut does not rely on that.

### `comp-schedule` — **RUN, and it is APPLICABLE (the non-obvious call)**

`comp-schedule` is the GATE LEDGER: *"a promise to check something later."* The reflex is to call it
N/A on a frontend project. **That is wrong here — this project creates three such promises**, and a
gate that outlives its reason with no visibility is the exact failure Andrew named when he asked for
the tool. Registered at the cut:

| gate | owner | the condition that clears it |
|---|---|---|
| **FWD-9's grade half** | Andrew | his word after the `RB-s-15` side-by-side. Not a scheduled event; an act only he can take. |
| **The brief's Appendix A prose defect** | `2.0.0_SA_COO~D` | "20 bear on an outcome; 3 are cleanup" contradicts its own table (21/2). Deliberately not fixed mid-sign-off; clears at the next legitimate re-pin of the brief. |
| **`comp-adversary`'s false-GONE path parser** | not this project | clears when the tool's path splitter is fixed. Recorded so the next reader does not re-derive it. |

### `comp-iam` — **DECLARED-NOT-APPLICABLE**

`comp-iam` cross-references source-code operations against Terraform policies. **Reason, measured
rather than assumed:** an AWS-surface token sweep returned **0 hits over the SURFACE MANIFEST** and
**0 over the whole PRD** (`lambda`, `terraform`, `.tf`, `iam`, `s3`, `cloudfront`, `ecs`, `sns`,
`ses`, `dynamodb`, `glue`). The PRD states outright that *"nothing here is deployed by this
document."* No cell writes an AWS surface, so the lens has an empty input — and **a checker handed
an empty set returns a vacuous pass that reads as clean**, which is why this is recorded as
NOT-APPLICABLE with its denominator rather than RUN-and-green.

⚠ **The bound on that reason:** it covers the CELLS. The portal itself ships to AWS through CI, so
if a later round promotes this branch to `DEV`, **that promotion is an act with an IAM surface and
is not covered here.** The PRD already excludes promotion from its scope; this is the same boundary
seen from the battery.

### Beyond the core

`comp-which`, `comp-find`, `comp-read` are used inside cells as instruments, not as battery lenses.
No lens of the admitted catalogue is claimed beyond the three above; the two `NOT-EVALUATED` rows in
§2 are the honest statement of what no lens covered at this cut.

---

## 7. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** The domain is §1's subtraction — 14 manifest rows minus 3
non-write kinds = 11 write surfaces, with an unscoped falsifier run over the whole PRD (0 AWS
tokens) to prove the domain was not narrowed in the direction that mattered. Every one of the 11
surfaces appears in §2's rectangle and is claimed by at least one cell; no cell claims a surface
outside it. **Exhaustive:** yes, against that denominator. **Mutually exclusive:** yes for *ownership*
of a surface's target state; explicitly **NOT** for *touch* — surfaces 2 and 5 are written by five
cells each, which §5 handles as a collision set rather than pretending to exclusivity it does not
have.

**(ii) SAME GRAIN.** Every cell is *one visual concern across a named write-surface set, gradeable
by rendering or by a census with a denominator.* The two re-cuts in §3 exist to restore this grain
where the PRD's candidates mixed it (R7 mixed authoring with superseding standing law; R14 mixed an
enumeration with a render campaign).

**(iii) INTENT COHERENCE.** One axis: **the portal's visual layer.** Not behaviour, not data, not
information architecture, not routes or auth. Every excluded item in the PRD's NOT COMMISSIONED list
stays excluded; no cell widens.

**(iv) STATE COHERENCE — what each remedy does NOT move.** Stated because a remedy silently assumed
to move a value it does not is how a cell passes and the product stays broken:

- `RB-s-1` moves token VALUES. It does **not** move any consumer that hardcodes a colour outside the
  token chain — those are `RB-s-3`/`RB-s-5`'s census, not RB-s-1's.
- `RB-s-2` moves the typeface and numeral rendering. It does **not** move column *layout*; its bar
  is "alignment no worse than before", not "alignment improved".
- `RB-s-7` moves the CONTRACT. It does **not** move a single pixel — a green RB-s-7 with every other
  cell red is a document nobody obeys, which is why FWD-6's bar is a build-from-contract page and a
  rejection-by-clause, not the file's existence.
- `RB-s-8` moves standing law that **other projects read** (`IRPT_FNTEND` is a named consumer). It
  does **not** move their code; they inherit through the token files on their own schedule.
- `RB-s-11` moves which libraries render. It does **not** move what any chart SHOWS — a chart that
  cannot migrate without changing its content is a surprise row, never a quiet exception.
- `RB-s-12` moves the denominator of what is known to be affected. It does **not** move any surface,
  and a large inventory is not evidence of a large change.

---

## 8. THE FOUR L5 OBLIGATIONS THIS LANE CARRIED IN

Recorded in the brief-half review (`laneD_L4R_BRIEF_HALF_REVIEW_DSGN_REBRND_v0.2.md@7533130e28`) and
discharged at L6, not here:

1. **Compound acceptance clauses split one per criterion.** The PRD's drafts conjoin up to seven
   clauses (R3), and v0.2 made R3/R5/R6/R10 longer. `to-pipeline-gate.py` refuses two
   `<invocation>` or two `<expect>` in one criterion **mechanically**, so this is enforced at the
   cut, not trusted.
2. **The two human-act clauses re-cut.** `RB-s-14`'s walked person and `RB-s-7`'s
   "author's agreement" each become an on-demand act a worker CAN take, plus a
   `judgment="true"` criterion with **no verdict**, graded by `3.0.0_SA_CVO` at L9.
3. **FWD-9's grade half stays Andrew's.** `RB-s-15` cuts the pack-exists half as the on-demand act;
   the grade is his and is registered as a gate in §6.
4. **No cell assumes the competitor capture.** It is egress and needs his per-use word.

⛔ **AND ONE BOUND ON THE COVERAGE GATE, WORTH KNOWING BEFORE THE ISSUANCE.** `to-pipeline-gate.py`
grades `<owned_cells>` union against this cell set **at `DECOMP`**; at `EXECUTING` — a recut —
coverage is **NOTED, NOT GRADED**. The first issuance is mechanically protected against a dropped
cell; a recut is not, and that read stays this lane's.

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. **Surfaces 5 and 9 are `NOT-EVALUATED`.** The panel primitives and the three `design/` law files
   were never opened by this seat. Their cells carry the census; nothing here rests on their shape.
2. **The chain count is a judgement about write collisions, not a measurement.** M=3 is derived from
   the edge set this document declares. A different, defensible cut could read M=1 (everything
   converges on the token spine) or M=5 (splitting the collision sets harder). The reasoning is in
   §5 so it can be argued with rather than inherited.
3. **No cell has been exercised.** Every "target state" is a specification, not an observation.
4. **`RB-s-13`, `RB-s-14` and `RB-s-15` measure a moving tree until B and C drain.** §5 states the
   ordering constraint; nothing mechanical enforces it, and that is this lane's read at the drain.
5. **No effort or duration estimate appears here**, deliberately.
