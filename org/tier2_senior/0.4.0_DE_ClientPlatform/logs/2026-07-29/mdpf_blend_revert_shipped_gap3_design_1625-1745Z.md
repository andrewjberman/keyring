# MDPF: blend-cohort interim revert SHIPPED to PROD + gap 3 found + provenance design — 1625–1745Z

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, DIAGNOSE

Continues `mdpf_surface_ack_repush_b0fc1e75_1546-1625Z.md`. Citations `@a969d615` unless stated.

## Shipped

**`fa687486` — blend-cohort interim revert.** Andrew-direct ~1450Z/~1545Z, CTO granted both words
164612Z, DT GO 164822Z. Landed on PROD via DT's `--no-ff` merge `b7c296dc`, back-merged to DEV.

Authored in an **ephemeral worktree off `origin/PROD`** (Rule 19 — the main portal tree never left
DEV, verified after teardown). First worktree attempt died on Windows `MAX_PATH` under the scratchpad
path; retried at the house-pattern short path `Desktop/_portal_prod_wt`.

**Partial revert, verified not asserted** — `70166741` changed TWO quantities and Andrew asked to
revert ONE:
| check | result |
|---|---|
| dangling `totalHoldingsDisplayed` refs | 0 |
| `excluded_unfunded_count` field reads | INTACT both sites |
| forbidden cross-artifact subtraction | ABSENT |
| files changed vs `origin/PROD` | 1 |

Interim comment landed as a **binding deliverable** (CTO's condition): "DO NOT REMOVE" header, both
verbatims + dates, the producer-side successor (`total.sleeve_level_count`) that retires it, and the
history note that this quantity was already deleted once by a census.

**Post-promote invariants verified independently** (not taken on DT's report): `fa687486` on
`origin/PROD` ✓, back-merged into `origin/DEV` ✓, **`b0fc1e75` NOT on PROD** ✓ — the toggle removal
stayed unpromoted per Andrew ~1545Z, which was the entire purpose of the branch-off-PROD topology.

## The two-carrier finding paid off within the hour

The pre-commit hook **WARN-skipped in the worktree** ("parent superproject not found") — so **carrier 1
never ran on `fa687486`.** Only the `^SURFACE_ACK:` line in the message carried it, verified on the
actual commit object (`grep -c` = 1), not the draft. On this topology an agent trusting the env-var ack
would have shipped **no ack at all** and hit the same CI wall a fourth time. Routed to DT: the pre-push
gate must assert carrier 2 on the MESSAGE and never infer it from a successful hook run.

## GAP 3 — found, and CTO made it a binding cross-lane GATE

`perFirmNonModelByPeriod` (`:1323-1331`) builds `Record<string, number | null>` via
`map[p.period] = p.value` — **`pointClass` is DISCARDED.** `readNonModelSeries` returns it; the map
drops it. The choke set (`:977-982`) draws only from `aggregate` + `by_model`, so the non-model map is
not even an input. **The Non-Model band cannot render provenance at all, however the producer labels
it.**

CTO 173640Z: *"no hybrid or estimated value is served into the Non-Model band until the provenance
channel exists"* — the DATA fill is now gated on the RENDER channel, inverting the sequencing both
lanes had assumed. Sequence set: **gap 3 → gap 1 → gap 2**, build nothing (freeze).

## Two cross-lane calls ruled (DS~A asked; render contract is mine)

**Enum:** keep `absent`, reject `underivable`. Mechanism, not preference —
`pairedProvenanceRead.ts:240` coerces an unrecognized class to `interpolated_estimate`, so a new value
would **fail INTO the defect it was meant to fix.** DS~A verified and **sharpened it**: `:240`
*preserves* `entry.confidence`, so it would arrive carrying `confidence: 1.0` over a `None` —
byte-for-byte their 44-date artifact, not merely similar. I then found the **asymmetry**: `:234`
(missing ENTRY) returns `confidence: null` and *cannot* forge one; only the invalid-ENUM path can — so
the fail-safe is only half safe, and the dangerous half is exactly the route (ii) would have opened.
Offered a third option, **adopted as their design**: keep the enum, carry the distinction in a
**non-enum sibling field**. *Enum widening is a one-way door; a sibling field is not.*

**Their 32 derivable-but-empty dates:** stay on **(A)**, leave them None — because gap 3 means a hybrid
(measured custody − interpolated model) would reach the screen indistinguishable from measured, at
~$330mm client-facing. Framed as **correct-until-step-2, NOT final**, with the unlock sequence written
into both docs. CTO endorsed.

## Gap 3 design — the obvious fix is wrong

Routing non-model into the period-level choke set would mark a whole period because ONE segment is
estimated, and for cottonwood would band nearly the entire chart. **A marker that marks everything
distinguishes nothing** — it satisfies the letter of provenance-to-screen while destroying the signal,
and would pass any check asking "is provenance rendered?" Recommended per-SERIES marking of the
non-model segment instead. Scope-bounded: Global is out **by design** (`:976` empty set), flagged so
nobody fixes it into existence. Recharts `<Cell>`-on-stacked-bar flagged **UNVERIFIED, not claimed**.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-grep` (x5) | PASS | located the non-model prior art, `getNonModelAssets` callers (0), the `NOT_MEASURED` fossil (1 hit, a comment), and gap 3's discard site — each with denominators printed |
| `comp-surface-check` (pre-commit, workspace) | OK / no critical surface | on the 4 design+log commits |
| `comp-surface-check` (pre-commit, worktree) | **WARN-SKIPPED** | parent superproject not found outside `ajb_workspace` — the finding that carrier 1 is unavailable on this topology |
| `comp-pulse` risk-reflex | CLEAN | measured, 1484 danger nodes, every commit |

**What worked:** `comp-grep`'s printed denominator (`scanned 404 of 404`) made the zero-callers and
one-hit results usable as evidence rather than as absence-of-proof.
**What failed:** nothing this window.
**Gap found:** none new — the two `comp-which` gaps logged in the prior window stand.

## Blockers

None assumption-based. All remaining work is **frozen by CTO 173640Z** ("do not build any of the
three yet; the wave and the accrual grant are ahead of you") — an explicit, evidence-cited hold with a
named owner, not a blocker.

## Current State

- `origin/PROD` head `b7c296dc` (the interim-revert merge). `origin/DEV` = PROD + toggle removal +
  marker, still unpromoted per Andrew ~1545Z.
- Design doc `MDPF_COTTONWOOD_PROVENANCE_RENDER_DESIGN_20260729.md` @ `298f96dd54` — carries all three
  gaps, both cross-lane rulings, the gap-3 design, and a **vintage warning** that its pre-addendum
  citations are `@b0fc1e75` (the back-merge shifted the file +45 lines; re-locate by symbol).
- Ephemeral worktree torn down; leftover dir removed (Andrew-authorized, after `rm -rf` was
  permission-denied and `MAX_PATH` blocked the normal path — used a robocopy mirror-from-empty).
- DS~A standing: (B) deferred not rejected, producer half ready, 32 dates = `2026-06-09..2026-07-17`.
  **They asked to be pinged the moment steps 1-2 land.**

## Next Steps

1. **[1.0.0_SA_CTO]** gap-3 gate: per-series vs period-level; whether to exercise the recharts
   `<Cell>` stacked-bar mechanism before or after the gate; whether a hybrid reads differently from
   wholly-estimated on screen.
2. **[0.4.0_DE_ClientPlatform]** on unfreeze: build gap 3 → gap 1 → gap 2 in CTO's order, each with a
   READ headless screenshot (a type cannot see contrast).
3. **[0.4.0_DE_ClientPlatform]** ping DS~A when steps 1-2 land → flips (B) from deferred to correct.
4. **[0.4.0_DE_ClientPlatform]** on next touch of `ModelPortfolios.tsx`: **DELETE** the `NOT_MEASURED`
   comment at `:304` — DS~A confirmed it becomes FALSE, not merely stale, when the grant lands.
5. **[1.0.0_SA_CTO]** candidate hardening banked: `:240` arguably should DROP confidence on an
   unrecognized class rather than carry it forward. Nothing broken today.
