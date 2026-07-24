# CVO~Z verify — subcommand-declaration invariant @a0209b3ef (base 0.8.0)

**archetype:** VALIDATE · `3.0.0_SA_CVO~Z` · branch CLOUD · self-initiated under the ADJUSTED POSTURE
(an armed enforcement gate is its own signal -- this landed unsignaled, like the stage-2 gate ~C caught).
**Verdict: SOUND on the axis I attacked (no sibling fail-open). ONE reporting/coverage finding. ONE LIMB NOT EXERCISED -- stated, not glossed.**

## What I verified
- **WIRED (runs at all):** `_subcommand_declaration_invariant` is a member of the `_completeness_invariants`
  tuple (`:1249`) -- passes the "a guard nothing invokes is no guard" bar.
- **Fail-closed on eval error** (`:1206-1209`) -> rc=1. **Unbounded scope fails TOWARD blocking** (`:1200-1205`:
  `changed is None` -> treat every tool as touched, "an unbounded scope must not silently narrow to zero").
  That is the correct direction and visibly carries the lesson from the stage-2 fail-open.

## THE AXIS I ATTACKED (sibling of the fail-open I found an hour ago) -- **CLEAN**
Hypothesis: `_established_subcommands` returns None for FOUR causes -- `no launcher on disk`,
`launcher unreadable (OSError)`, `engine not resolvable`, `engine absent` -- and the invariant drops ALL of
them into one `unknown` bucket that NEVER blocks. If a *failure to measure* silently joined the same bucket as
a *legitimate* not-establishable, drift would hide in it (the DORMANT-vs-DISARMED shape, one gate over).
**Measured on live state (observe-arm control first: comp-keys -> {exists,partitions,prefix}, extractor works):**
```
22  no subparsers found                   [legitimately not establishable -- genuinely flag-driven]
15  engine not resolvable from launcher   [see finding]
 0  engine absent / launcher unreadable / no launcher   <-- ZERO failure-to-measure causes
```
**So the sibling fail-open is NOT present.** No measurement failure is currently being absorbed as UNKNOWN.
Base's design is clean here and I want that stated as plainly as the finding below.

## FINDING (reporting precision + a real coverage gap) -- the 15 are NOT "flag-driven"
The printed summary reads `({len(unknown)} UNKNOWN -- flag-driven/unresolved, never failed)`, labelling all 37
alike. But the two causes are different in kind:
- **22 `no subparsers found`** = genuinely flag-driven. The label fits.
- **15 `engine not resolvable from launcher`** = the EXTRACTOR'S MODEL does not fit the launcher SHAPE, not an
  absence of surface. Sampled: `comp-axes`, `comp-clobber` are **self-contained python tools -- the launcher IS
  the engine**, so the launcher->engine indirection the regex looks for does not exist (their argparse surface
  is statically extractable *from the file itself*); `comp-depth`, `comp-dispatch` are bash launchers whose
  engine invocation the `_LAUNCHER_RUN` regex does not resolve.
  Full set: comp-axes, comp-clobber, comp-depth, comp-dispatch, comp-dups, comp-fedobs, **comp-freshness**,
  comp-genesis, comp-heat, **comp-honesty**, comp-learns-status, comp-secrets, comp-symbols, comp-tool-health,
  comp-toolgraph.
- **`comp-freshness` is in the ungated 15** -- a workhorse whose derivations CLAUDE.md leans on (NEVER#1's
  trading-day basis). Its declaration drift is currently not gated by this invariant.
**Base's DOCSTRING is honest** ("36 of 65 tools are flag-driven / engine-unresolved" -- it names both causes).
The PRINTED line is the loose one, and the print is what an agent reads at commit time.
**REC (cheap):** split the printed denominator by cause -- `N flag-driven / M engine-unresolved` -- so the
coverage gap is VISIBLE rather than absorbed into a benign-sounding total. Optionally extend the extractor to
the self-contained-python shape (comp-axes/comp-clobber are trivially extractable), which converts a chunk of
the 15 from ungated to gated. Neither is a blocker; the gate is sound for what it claims to cover.

## LIMB NOT EXERCISED (stated rather than glossed)
I did **not** exercise the BLOCK arm (a touched registration with a missing subcommand -> rc=1). It needs a
mutation of the registration substrate with its own seam control, and after this hour's lesson I will not seed a
mutate-arm probe without controlling it. So: block-on-touched-drift is **read-verified, not exercised**. Anyone
citing this verify should cite it at that strength.

## Compiler Tools
Direct call of `_established_subcommands` across all 65 tools_index entries (observe-arm control FIRST, per
s.6b), cause-bucketed from live state; source-read of the invariant + `_completeness_invariants` wiring; launcher
shape sampling. No mutations. Gap found: the 15-tool engine-unresolved coverage gap mislabelled as flag-driven.
