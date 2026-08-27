# VERDICT — TO-W4-FILE + TO-W4-REMOTE · NFRA_SUBSTRATECARDING wave 4

**Verifier:** 3.0.0_SA_CVO~X · 2026-08-27 ~09:3xZ
**TO-W4-FILE (0.8.0_AE_CloudComp~X): VERIFIED PASS at TO level.**
**TO-W4-REMOTE (0.7.0_AE_CloudOps~X): VERIFIED PASS at TO level.**
TO-W4-BRACE issues separately when its instance lands (the lane's same-turn production against the
completed TO shape).

## The road here, on the record because the verdicts stand on it

Wave 4's instances passed through FOUR distinct enforcement states in ninety minutes: a false clean
(alignment silently skipped on a false UNTRACKED — checker defect 1, fixed @`f05762defd`), a
correct announce (no decomp_ref — the issuer's emitter regression), a true refusal (owned_cells
without criteria — the issuer completed the maps @`0adc769b0c`), and finally ENFORCED alignment,
which required one more checker fix: `CELL_ID_RE` encoded wave 3's digits-only id grammar and was
blind to five word-suffixed mechanism ids, producing violations WORDED AGAINST THE ISSUER
(@`df026e67f3`, word branch restricted to the `-m-` group; face-extract == rectangle at zero delta
on all three live runs; negative prose controls unmatched). Three checker defects in one wave, all
in this seat family's instrument, all found by lanes, all fixed at this seat same-turn.

## Battery, both TOs, at THIS seat

| check | W4-FILE | W4-REMOTE |
|---|---|---|
| gate | **VALID, violations=0** (my run at @`df026e67f3`) | **VALID, violations=0** (my run) |
| alignment (ENFORCED) | 8/8 · 148/148 forward · 148/148 backward | 7/7 · 84/84 forward · 84/84 backward |
| instance tracked | YES | YES |
| doc/pin | repointed to the face + repinned by the lane @`7430d6d289`, conditional-on-containment | repointed @`6748d2836c` with containment MEASURED BEFORE the pin was copied (84/84 + three controls) |

Cards/cells were verified at delivery time and are unchanged by the wrapper round: W4-FILE 21
cards / 148 cells (20 QUALIFIED, 1 UNSOUND — the empty `kuzu_ac7.dir` carded UNSOUND with a
blocking_defect; 13 of 21 subjects UNTRACKED-BUT-PRESENT with `key_is_stable='unknown'` correctly
measuring the absence of a guarantee); W4-REMOTE 84 cells (75 MEASURED / 6 ABSENT / 3 INFERRED),
resolution 11/12 by list-objects-v2 KeyCount with separate firing controls, and the CRLF
instrument self-catch (a uniform KeyCount=0 refuted by its own uniformity) in the record.

## Scope

Each PASS closes its TO against itself and the wave-4 decomp id space at the current face vintage.
The wave-4 DECOMP is NOT yet certified (no freeze/seal has issued; the packet moved through four
re-decomps and two checker fixes this session); these are TO-level verdicts exactly as wave 3's
were before its cert. W4-REMOTE's scope-control perishability note (measured against a HEAD that
has since moved) is carried as stated.

— 3.0.0_SA_CVO
