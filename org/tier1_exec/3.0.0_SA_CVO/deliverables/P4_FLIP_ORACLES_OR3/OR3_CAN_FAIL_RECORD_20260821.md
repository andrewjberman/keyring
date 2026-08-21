# OR-3 CAN-FAIL RECORD -- the CVO half of P4_FLIP_ORACLES_49F

**Author:** 3.0.0_SA_CVO · 2026-08-21 ~16:15Z · **archetype:** VALIDATE
**TO:** OPAL_ADVIPOINTERS.P4-ORACLES-49F, criterion OR-3: *"each oracle exercised once against a
state where it MUST fail (the legacy serve or a mutated fixture) -- pass-on-both rows are
rewritten, shown."* DE half (OR-1/OR-2) consumed at @d8808b489e; DE's three deltas
(natural-404 retired · three-state route rule · d12 identical-ETag) are ADOPTED into this pass --
delta (2)'s three-state rule is the correct design and my 112411Z framing is superseded by it.

## Verdict up front

**Every oracle leg exercisable today DISCRIMINATES -- zero pass-on-both rows, zero rewrites
needed.** The legs that cannot be exercised today are named with the state that unblocks each,
never recorded as passed-by-silence.

## 1. L3 VALUE-ANCHOR -- CAN-FAIL EXERCISED, 15/15 EMIT rows (runnable today, run today)

Method: pass-side = live twin ETag+size vs the frozen manifest anchor (s3api head, my own reads);
must-fail = the same anchor test applied to the row's declared must-fail state.

| rows | must-fail class | result |
|---|---|---|
| 6, 7, 9, 10, 14, 16 (real-delta FLIP) | LEGACY-SERVE | pass-side OK on all 6 live twins; anchor test **FAILS-AS-REQUIRED** against the legacy serve on all 6 (legacy ETag != anchor; anchored values differ per the pins) |
| 8, 11 (S3-only FLIP) | LEGACY-SERVE (content address) | pass-side OK; **FAILS-AS-REQUIRED** on the legacy object both rows |
| 12, 13 (DELTA=0 pair) | MUTATED FIXTURE, **one each, never shared** | own byte-flipped mutant per row (method: single-byte XOR at offset 100 of the local build copy; reproducible); anchor test **FAILS-AS-REQUIRED** on each mutant independently. The identical live ETags (`ab37740d...`, 7,260,521 B both) are the measured reason sharing is forbidden -- adopted. |
| 1, 2, 3, 15, 17 (HELD/STRUCTURAL, inverted) | twin-request-appearing | S3 half exercised: twin-absent invariant **HOLDS 5/5** (same-listing discrimination), and the **state-substitution control FIRES** (the absence instrument applied to a published key detects it) -- the instrument discriminates present-vs-absent, so a never-widen breach (a held twin appearing) WILL fail the row. |

Bucket-scope law: every absence verdict above ran against `opal-data-portal-v2` with the published
keys as the same-call positive control.

## 2. L1 ROUTE -- EXERCISABLE-AT-ROUTE-LANDING (stated, not silently passed)

The must-fail (nonexistent-key positive control, own isolated invocation) **cannot discriminate
today**: at S-UNROUTED every request 4xxs, so a bogus-key non-200 is indistinguishable from a real
key's non-200 -- the control would "fail" on everything, which is an instrument that cannot pass,
the mirror image of one that cannot fail, and equally not a control. It becomes discriminating the
moment the AE route act lands (real key -> 200, bogus key -> non-200). **Run it then, per row, as
its own invocation, before any flip commit cites a cert.** The three-state rule's S3-first
discipline was exercised today: all 10 flip twins PRESENT + route unbuilt = S-UNROUTED measured,
not inferred.

## 3. L2 SHAPE + L4 LOUD -- EXERCISABLE-AT-FLIP; fixtures PRE-BUILT so flip-day is mechanical

Both legs exercise `adviKeyRepoint` behavior that is unreachable while `ADVI_ROUTE_LIVE = false`
(`:216` short-circuits before any twin attempt). Flipping that constant is DE's flip-day act on
DE's lane; a temporary cross-lane working-tree flip at this seat is the shared-worktree sweep
hazard and was deliberately not taken. **Therefore:**
- **L2 must-fail fixtures are PRE-BUILT, one per portal-read flip key (8), at
  `fixtures/mutant_{key}.json`** -- each a well-formed body carrying NONE of that key's
  `hasAnyKey` probe keys (the gate's own definition of shape-invalid), in ui-smoke `--fixtures`
  format, one per key per the d12-pair rule. Expected on exercise: the LOUD
  `[P4-REPOINT-49F] SHAPE MISMATCH` marker + `fallback-shape-mismatch` recorded. A row whose
  mutant does not produce that exact marker is rewritten -- DE's own bar, adopted verbatim.
- **L4's exercise IS its must-fail** (--fail 503 -> the quiet marker or the row is rewritten);
  nothing to pre-build.
- **Run alongside DE's per-key exercise pass at the flip, before any flip commit cites its
  cert** -- same window, my read of the markers, not DE's self-report (49F-CERT-INPUT-INDEPENDENT
  extends to this table).

## 4. Answers to DE's two design challenges

1. **Held-row inverted oracles: ENDORSED, and row 15 is ratified as a MANDATORY member of every
   flip-day pass.** A table that only tests intended change cannot see over-flipping; row 15 is
   the only detector for the :369 template collapse, a breach that travels through a shared code
   path. (The registry-as-data in the module makes it unreachable *by that module*; row 15 is the
   independent check that stays true if the module is edited -- keep both.)
2. **S3-only rows 8/11 COUNT toward OR-1 coverage.** OR-1 is a *carried* denominator (the frozen
   list), not an *exercised* one, and their L1/L2/L4 N/A-BY-CONSTRUCTION entries are plane
   statements with a measured basis (0 hits / 414 files; 1 comment) -- stated, never skipped, per
   COO's own ratification of the scoping (64841 (iv)). Their L3 legs are exercised (section 1).
   The read-side question ("does a NON-portal consumer read ownership_map") stays open on its own
   plane and is not this table's to answer.

## 5. Residue, named

- L1 controls + L2/L4 exercises: run at route-landing / at-flip respectively (owners: me, in DE's
  window). Until then OR-3 is COMPLETE-FOR-THE-RUNNABLE-POPULATION with the remainder
  state-blocked by external acts, each named.
- The held-4's post-backfill re-pin (separate act) carries its two pre-declared provenance rows
  (a07 vintage, accrual_materiality) -- unrelated to this table but recorded wherever the flip-day
  reader might otherwise conflate the two passes.

-- 3.0.0_SA_CVO
