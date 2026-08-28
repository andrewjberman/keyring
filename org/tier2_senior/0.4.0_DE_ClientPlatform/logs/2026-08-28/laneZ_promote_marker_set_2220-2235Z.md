# 0.4.0_DE_ClientPlatform~Z -- 2026-08-28 22:20-22:35Z -- PROMOTE MARKER SET + TO-F1-DE CLOSE-OUT

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**DELTA LOG.** The substantive build window (21:30-22:20Z) is ALREADY logged in full at
`laneZ_d3d4_render_defects_2130-2230Z.md` @`d1a970af35` and is deliberately NOT re-narrated here --
two durable records of one window diverge from minute one. This covers only what happened after that
file was written.

---

## Commits

**None in this window.** Nothing was built; the window is one measurement, three routed messages and
a banked memory. Prior window's commits stand: `db3df0b2` (portal DEV) and `d1a970af35` (workspace
SITEZ), both still **LOCAL** -- push routed to `0.0.0_AB_MSTR~Z` at 22:11Z and not yet taken.

---

## OK: THE ONE PIECE OF REAL WORK -- 14211 s.3 WAS AN UNDISCHARGED ASK SITTING IN MY INBOX

`3.0.0_SA_CVO~Z` 14211 arrived 21:56Z and I saw the notification but never opened the file. Reading
it at the top of this window found a direct request to this seat: *"when your commits are final, one
durable user-visible string that only the new code has is all I need."* My commits were final and the
ask was undischarged.

**THE ANSWER IS THAT NO SUCH STRING EXISTS, AND THAT IS A PROPERTY OF THE CHANGE.** D-4 DELETES a
component and D-3 REWIRES colour resolution; neither adds user-visible text. Measured with
`git grep -c` at both vintages rather than picking a plausible one:

```
  OLD=4dde6df344 (origin/DEV)   NEW=db3df0b2   scope src/
    "#8b5cf6"            OLD 6 files  NEW 7    PRESENT IN OLD -> false pass
    "#94a3b8"            OLD 4        NEW 5    PRESENT IN OLD
    "Opal Fixed Income"  OLD 1        NEW 2    PRESENT IN OLD (the comment quoting Andrew)
    "Fixed Income"       OLD 42       NEW 43   PRESENT IN OLD
    "memberColor"        OLD 0        NEW 1    NEW, but a local IDENTIFIER -- minification renames it
  CONTROLS: POSITIVE "Asset Category Views" NEW=1 . NEGATIVE bogus token NEW=0
```

>> **`#8b5cf6` is the candidate a reasonable seat would have reached for -- it is the fix's headline
   value -- and it sits in SIX old files.** A marker chosen from it would have passed on the
   UNPROMOTED bundle. This is why the ask was answered by measurement and not by nomination. <<

**What I gave instead:** the only clean `1 -> 0` string as the DISCRIMINATOR (`A fee-split breakdown
is not available for this view.`), plus a MANDATORY positive control from the same component
(`This block carries no L1 breakdown for this node.`). An absence with no positive control proves
nothing -- 14211's own doctrine, applied to my own marker.

## WARN: THE TRAP I FOUND IN MY OWN COMMIT

```
  "Fee split unavailable"  OLD 1 file  NEW 1 file   <- STILL IN NEW SOURCE
  db3df0b2:src/components/CategoryViewTree.tsx:290:
    * `PredicateUnavailable` stood here and rendered an amber "Fee split unavailable" box.
```

**The panel's HEADING survives in the block comment that records its own deletion.** A source-level
grep for it returns a hit and reads as *"D-4 did not land"* -- a false FAIL on a correct commit.
`1.0.0_SA_CTO~Z` 14282 s.1 hit this and handled it correctly by reading rather than counting; it is
now pinned in writing so the next reader does not re-derive it.
⚠ **The two planes disagree and the plane must be named:** minification strips comments, so at the
BUNDLE level both strings vanish and either marker works; at the SOURCE level only the body copy
discriminates.

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `git grep -c` | `-F <tok> {4dde6df344,db3df0b2} -- src`, 10 tokens x 2 vintages + 2 controls | PASS -- 5 candidates disqualified, 1 discriminator + 1 control identified, trap located |

**What worked:** running BOTH control arms (positive `Asset Category Views` = 1, negative bogus token
= 0) so the engine is shown able to return one AND zero before any count is quoted.
**What failed:** nothing this window.
**Gap found / instrument note:** `comp-find` was NOT used here and the reason is structural, not
convenience -- **it searches the WORKTREE and cannot read a non-checked-out commit**, so it cannot
answer a two-vintage question at all. Rule 21's default routes search to comp-find; this is the
wrong-instrument case, and the deviation is stated in the routed message (14380 s.4) rather than left
for a reader to notice.

---

## Blockers

**None at this seat.** Two items are outstanding and BOTH sit with other serials -- neither is
assumption-BLOCKED, both are routed with an evidence-cited ask:

- [`2.0.0_SA_COO~Z`] The `CATV-TOF1-AC5` headline-figure word (msg 14271/14343). Rec (A), conditional
  on the held-node residual (their own 13544 s.4) being sound. One word flips AC5 to PASS.
- [`1.0.0_SA_CTO~Z`] Surprise S1 go/no-go (msg 14343 s.3): `IDVZ` + `PFDE` both resolve to `#f43f5e`
  in the SAME card, and the SMA reland is what makes it visible. I offered to land it in ~10 min and
  flagged that pinning ETF TICKERS into the MODEL colour map is the same semantic act that needed
  Andrew's word for `Fixed Income` -- so it wants their read, not my guess.

---

## Current State (written for zero prior context)

`D1_CATVIEWS.TO-F1-DE` is CLOSED at this seat. AC3 (canonical L2 colour via `getModelColor`) and AC4
(fee panel deleted from the DOM) are **PASS**, both read on a rendered page; AC3 independently scored
PASS by `3.0.0_SA_CVO~Z` (14283 s.1). AC1 is **N/A** (struck by the issuer on this lane's 60/60
measurement that D-1 is data-side), AC2 **UNCOMPUTABLE** until the reland, AC5 **UNCOMPUTABLE**
pending the routed word. Proof-of-spec instance at
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/D1_CATVIEWS.TO-F1-DE_PROOF_OF_SPEC.json` --
`proof-of-spec-check` **VALID, 0 violations**, coverage 5/5, alignment closed both directions.

Build: `portal` DEV @`db3df0b2` (two files: `src/components/CategoryViewTree.tsx`,
`src/lib/modelPortfolioColors.ts`). Records: workspace SITEZ @`d1a970af35`. **Both LOCAL** --
`origin/DEV` reads `4dde6df344`, `origin/SITEZ` reads `ea97a5e6dc` with my commit **4 deep** behind
three other seats' unpushed work.

`1.0.0_SA_CTO~Z` 14282 declared Andrew's gate (*"yes reland once all fixes are in"*) DISCHARGED on
this commit. Chain: push -> reland -> floor -> publisher -> promote -> verify. This lane's part is
done; steps 2-4 belong to `0.7.0_AE_CloudOps~Z` and `0.4.0_DT_ClientPlatform~Z`.

Memory banked this window: `dormant-guard-output-reads-as-the-convention` -- an unarmed filter emits
BYTE-IDENTICAL output to the fallback it will later override, which is how two senior seats wrote an
acceptance criterion around the wrong mechanism.

---

## Next Steps

- [`0.0.0_AB_MSTR~Z`] Both push legs. Portal is 1 commit; SITEZ is 4 and only the top one is mine.
- [`2.0.0_SA_COO~Z`] The AC5 word.
- [`1.0.0_SA_CTO~Z`] S1 go/no-go.
- [`0.4.0_DT_ClientPlatform~Z`] At promote: entry-chunk hash off `Ce258d2k` **AND** Last-Modified
  after the promote, both not either (14211 s.2); then the marker pair from 14380 s.2 on the served
  bundle, discriminator AND control together.
- [this seat, OFFERED AND UNCLAIMED] The post-promote visual render with a REAL bearer -- `AC3`'s
  rung, not the served-bytes rung. Mint-then-render is ONE act (TTL 900s) with a bogus-bearer 401
  control arm; a default-stub render is the FAILURE state. Fixture path and read-the-screenshot loop
  already exercised this session.
