# CVO PROPOSAL — the directive-retirement mechanism (Andrew commission via MSTR briefing, LD-0433)

**archetype:** DIAGNOSE + VALIDATE (analysis + proposal; NOT a build)
**Author:** 3.0.0_SA_CVO · 2026-08-20 ~1925Z · answers
`BRIEFING_20260820_CVO_DIRECTIVE_RETIREMENT_MECHANISM.md` (@59c555589d). Routes back through
MSTR; Andrew rules; the build lands per its Rule-24 record + owner gates.

## 0. Anatomy verified — and ONE CORRECTION to the briefing, load-bearing for the design

Verified at my seat this hour: the tripwire header verbatim ✅; the three-file sub-group contract ✅;
`comp_missions.py` emit/compile as the house pattern ✅; zero code parsers of DIRECTIVES.yaml ✅
(readers are agents + law, per the briefing).

**THE CORRECTION: `org/tier0/missions.yaml` contains NO directives section — the DIRECTIVES.yaml
rows are not machine-compiled from anything today.** The header says it plainly: *"MSTR base
writes these rows (register owner)"*; the item list's source is a CTO deliverable (S10/S11), and
stance cells are event-refreshed by hand on sovereign word. The tripwire governs the rows'
CONTENT FORM (no paths/globs/attach; members are references) — it is a discipline the hand-written
rows must satisfy, not a statement that a compiler produces them. **So "equivalently compiled"
cannot mean "copy an existing directives compiler" — none exists. It must mean: the retirement
mechanism is at least as machine-disciplined as the register's own pattern — a HUMAN-ASSERTED FACT
plus a MACHINE-EXECUTED VIEW, with a recomputability check that rejects hand-drawing.** That is
exactly the register's constitutional split (the machine cannot write a stance; the machine alone
writes the derived artifacts), applied to retirement.

## 1. THE MECHANISM (proposed)

**Three parts: a fact, a move, a check.**

### 1a. The FACT — a presence-based retirement record, human-written, no enum minted

The register owner (MSTR) writes one block on the directive's row in `DIRECTIVES.yaml`:

```yaml
retired:
  at: "2026-08-20"
  by: 0.0.0_AB_MSTR
  authority: 'Andrew-direct <verbatim or record path> + terminal evidence <citation, e.g. the
    site-Z acceptance record @393211922e + PROD v2.1.164 serving>'
```

- **Writer:** the register owner only (the same hand that writes stance cells — no new writer class).
- **The fact is human/sovereign-asserted with citation** — anatomy point 4 honored exactly: the
  machine never decides a directive is complete; it only reacts to the record.
- **PRESENCE IS THE FACT.** No `status:` enum value is minted anywhere — the Rule-24 question
  "which tokens?" is answered by needing none. (See §2 for the formal record.)

### 1b. The MOVE — machine-executed, never hand-drawn

A compiler leg in the house pattern (`comp-missions retire` inside `.tools/comp_missions.py`, or a
sibling; the build owner decides the exact seam):

- Scans `DIRECTIVES.yaml` for rows carrying `retired:` → **CUTS each from the live view and
  APPENDS it to `org/missions/DIRECTIVES_RETIRED.yaml`**, byte-preserving the row + its stance
  cells, stamping `retired_vintage:` (the row's stance `as_of` values at cut time) and the
  build-artifact banner.
- **The retired view is 100% machine-written** — its banner states it, and hand edits are rejected
  by the check (1c). Andrew's "never hand drawn if we can avoid it": the FACT must be hand-written
  (constitutionally), the FILE never is.
- The live view header gains one line pointing at the retired sibling (the reading protocol's
  breadcrumb).

### 1c. The CHECK — the tripwire, made mechanical for retirement

`comp-missions directives-check` (runs in the post-commit refresh hook beside the existing emit):

- **Partition invariant:** no directive id appears in both views; every retired row carries a
  complete `retired:` record (at/by/authority all present — a bare flag is rejected).
- **Conservation:** live + retired = the ever-minted id set (nothing silently deleted — the
  label-not-delete precedent at corpus grain).
- **Form tripwire** on BOTH views: no paths/globs/attach; members reference-only (the existing
  discipline, now checked instead of trusted).
- **Freeze invariant:** a retired row's stance cells NEVER change after the cut (byte-compare vs
  the record's own stamp). See §4.

## 2. THE RULE-24 RECORD (the schema act, four postulates + token hygiene)

The act: adding the `retired:` record field to the directive-row schema + minting the sibling view.

- **(i) MECE:** presence/absence of a complete record is binary and exhaustive — every directive
  is exactly one of live/retired. No partial states exist (an incomplete record is a check
  FAILURE, not a third state).
- **(ii) Same grain:** the field sits at directive grain on directive rows; the sibling file is
  the same grain partitioned by the same field. One grain throughout.
- **(iii) Intent coherence:** one intent — recording that the directive's work is complete. It
  deliberately does NOT encode health, device, or lifecycle-of-a-vertical (those live on their own
  axes).
- **(iv) Stability frame:** one remedy (the compiler leg) moves every value; a state change is one
  human record + one mechanical emit, identical for every row.
- **Token hygiene / Lifecycle_Stage reuse ASSESSED AND REJECTED, with the discriminator:** the
  freshly ratified Stage enum is C3.ii VERTICAL grain — WHERE A VERTICAL SITS IN ITS LIFE. A
  directive completing is PLACEMENT grain — WHETHER A PLACED WORK ITEM IS DONE. Reusing DISSOLVED/
  WINDING_DOWN here would put two grains on one axis (Rule 24(ii)) and import container-lifecycle
  semantics into a work-completion fact. No reuse; and because the design is presence-based, **no
  new token is minted either** — the census obligation reduces to the field name `retired`
  (word-boundary census over the register files is a stated build-time duty).

## 3. LD-0428 SEMANTICS (what retirement does to the boundary reads)

A retired SITEZ row is no longer that fabric's work: the boundary question "what does this device
work?" is answered by the LIVE view, which the row has left — **the reading protocol is satisfied
by construction, not by every reader remembering to check a status column** (this is the decisive
argument for Andrew's sibling-file sketch over a status-axis-in-place: agents consult placements
by reading DIRECTIVES.yaml; a file that contains only live work cannot be misread). The
shared-REGISTRY half survives in the sibling: history preserved, citations intact, nothing erased.

## 4. TTL / STABILITY

A retired row's stances FREEZE — the closed-period-immutable pattern (the estate's dormancy law,
second exception kind): no TTL aging on a closed judgment, no `STALE-DECLARED` labeling, and a
post-retirement stance edit is a CHECK FAILURE (a refresh of a frozen record would be the defect).
The `retired_vintage` stamp makes the freeze verifiable, not aspirational.

## 5. FIRST EXERCISE — D8 (the acceptance test, per the briefing's sequencing)

1. **The fact:** MSTR writes D8's `retired:` record citing the sovereign confirmation ("they work
   perfectly"), the site-Z acceptance record @393211922e, and PROD v2.1.164 serving.
2. **The move:** the compiler leg runs — D8 leaves DIRECTIVES.yaml, lands in DIRECTIVES_RETIRED.yaml
   with frozen stances + vintage.
3. **Acceptance controls (each must be able to fail):**
   - POSITIVE: D8 present in the retired view with its complete record + citations.
   - NEGATIVE: D8 absent from the live view; a site-Z placement read no longer returns it.
   - TRIPWIRE: `directives-check` passes — partition, conservation, form, freeze all green.
   - **MUTANT:** a live directive WITHOUT a record (any of D0–D7/D9) must NOT move — run the
     compiler and byte-compare the live view minus the D8 cut; and a HAND-EDIT planted in the
     retired view must make the check FAIL (the never-hand-drawn guarantee, exercised not claimed).
4. **The verify:** I run the acceptance controls as the mechanism's cert (SoD: MSTR writes the
   fact, the build lane writes the compiler, I verify — nobody checks their own work).

## 6. BUILD ROUTING (per the briefing's owner map)

Compiler leg + check = an 0.8.0-class build row COO cuts, with the Rule-24 record (§2) riding the
TO and CTO's gate on the schema act (their tripwire is the load-bearing text). Register writes stay
MSTR's. Nothing here is mine to build; the D8 acceptance verify is mine to run.

**One explicitly-deferred option, named so it is a decision and not a drift:** promoting the
directive rows themselves into `org/tier0/missions.yaml` (making the LIVE view machine-compiled
too, closing the §0 correction fully) is a LARGER schema act on MSTR's source file — worthwhile,
severable, and not needed for D8. If Andrew wants it, it is its own Rule-24 act after this one.

— 3.0.0_SA_CVO

---

# AMENDMENT 1 — ANDREW-DIRECT (at the CVO seat, 2026-08-20 ~193xZ): MISSIONS IS DEPRECATED

**VERBATIM:** *"missions is deprecated, 'directives.yaml' has taken its place conceptually"*

**What this changes in the proposal above (each §, one line):**

- **§0 re-read:** the anatomy correction now lands harder than written — DIRECTIVES.yaml was never
  compiled from missions.yaml because it is not a derived view of missions at all: **it IS the
  register now.** The tripwire's "recomputable from missions.yaml alone" text aims at a deprecated
  source and should be re-worded at the build to "recomputable from the directives source of
  record alone" (same discipline, correct referent).
- **§1b re-anchored:** the compiler leg is **DIRECTIVES-NATIVE** (a `comp-directives` tool or the
  build owner's equivalent) — NOT an extension of `comp_missions.py`. Building new machinery into
  a deprecated substrate would mint debt on a corpse. **The PATTERN survives as a pattern**
  (build-artifact banner, post-commit refresh, mechanical recomputability check); the missions
  binary is not its required home.
- **§1a / §5 unchanged:** the FACT + MOVE + CHECK shape, the presence-based record, the freeze
  law, the D8 acceptance plan with both mutants — none of it depended on missions as source; the
  fact always lived on the directives.yaml row itself.
- **§6's deferred option is STRUCK:** promoting directive rows INTO missions.yaml is now
  wrong-direction by his word. The live view's own compile story, if wanted later, anchors on a
  directives-native source — a separate act, his call.
- **Path note, deliberately NOT inferred:** he said "conceptually." DIRECTIVES.yaml currently
  lives at `org/missions/DIRECTIVES.yaml`; whether the FILE relocates out of the deprecated
  directory is a build-time owner's choice (MSTR owns the register files) — flagged, not moved.
- **Surfaced, not adjudicated (scope stays his/owners'):** the deprecation implies a future
  disposition for the missions machinery itself (comp_missions.py, MISSIONS.md, the sub-group
  tree, the post-commit hook) — under the estate's own law that is surface-it-not-chase-it, and
  under this very proposal's mechanism the missions register would eventually be a candidate for
  exactly the kind of compiled retirement being proposed here.

— 3.0.0_SA_CVO
