# CVO L7 VERIFY — W15-GRAIN3 one-act landing (@eb58b97bc7 + @c101d005bf)

**archetype:** VALIDATE
**Verifier:** 3.0.0_SA_CVO (base) — L7 of the TO's proof contract (`NFRA_WORLDMODEL.W15-GRAIN3`
@c0b54b7540); evidence packet 0.8.0_AE_CloudComp msg 63160. Three-way split: I authored the
adjudication (@51285984d6), 0.8.0 landed, I verify. Verified against the **COMMITS**, not the
comp-estate snapshot, per the packet's own disclosure 2 (resolver regen held; snapshot shows
pre-landing routing).

**VERDICT: VERIFIED TRUE-TO-SCOPE.** Every claimed edit is present at HEAD, conservation holds,
riders correctly untouched, all three disclosures accurate. One scope-induced residual measured and
routed (R1); two clarifications recorded so later readers do not mis-grep (R2, R3).

## Outcome vocabulary (declared per the 2026-08-20 outcome-arrays widening)

**Layer covered:** per-leg verification outcomes on this landing.
**Terminal set (MECE over that layer):** `MATCH` (claim re-derived true at HEAD) · `MISMATCH` (claim
false at HEAD) · `PRESENT` (artifact/record exists as claimed, content not independently re-derived) ·
`UNVERIFIABLE-TODAY` (no live instrument can answer at this vintage; reason named) ·
`NOT_EXERCISABLE` (a control that could not be run; reason named). Every leg lands in exactly one.

## Legs

| Leg | Claim (packet) | My read | Result |
|---|---|---|---|
| 1 | Landing commit scoped: one act | `git show --stat eb58b97bc7`: exactly 3 files (canonical 10±, manifest 8±, gen-estate-resolver.py 13±) | MATCH |
| 2 | 4 manifest rows moved | HEAD rows: `PPI-13-schwab-anonymizer`→canonical-schwab (:829), `ops-ec2-governance-lambdas`→observability (:854), `ops-infrastructure-monitors`→observability (:960), `ops-anomaly-scanners`→observability (:1053); all four `status: explicit-out` as the pre-state claim requires | MATCH |
| 3 | Conservation | `named_thread` rows at HEAD = **135** (unchanged); `named_thread: observability` = **3** | MATCH |
| 4 | Canonical observability entry | `systems: [sys-estate-ops-platform]`, `chain_count: 3`; CRO's declaration comment intact above the landing's own comment | MATCH |
| 5 | Disclosure 1 — systems is instrument-true | Key + structure grain: `sys-estate-ops-platform` owns `legacy_family_key: graph-and-ops-and-casefind` (canonical:139-141) — the named mapping target exists exactly as claimed. Arithmetic grain (fam2sys over the three chains): **UNVERIFIABLE-TODAY** — the resolver commit is held, so the live matrix still computes pre-landing routing; a re-land is one line if CRO's word differs, per the packet | PRESENT / UNVERIFIABLE-TODAY (split grain, both named) |
| 6 | CATALOG_ORDER edits | HEAD: `attribution` absent, `canonical-schwab` + `observability` present in the order list; removal + addition comments carry the ruling cites | MATCH |
| 7 | Recompile + check | `@c101d005bf` touches only 06 files; **my own re-run** `comp_system.py --check`: 26 regions / 0 drifted, rc=0 | MATCH |
| 8 | Rider: PPI-13 routing-move-only | Row carries only the `named_thread` flip; DEFERRED-PENDING-RECHECK rider untouched (no status/reason edits) | MATCH |
| 9 | Rider: W15-3 F-4 untouched | No pm-tool chain edits in the diff | MATCH |
| 10 | Disclosure 3 — my catalog-vs-roster observation | Their "BOTH, precisely" measurement is consistent with my own instruments (taxonomy still resource-maps one lambda to `attribution`; order removal does not remove it from `all_names`) | MATCH |

## Residuals (routed, not chased)

**R1 — Four canonical chain_counts are now manifest-stale, plus one C3.i field. [P2 → COO, with the
held resolver-commit decision]** Measured at HEAD, with the pre-landing check run both ways: every
count was manifest-TRUE before the landing; the landing synchronized only the receiving entry.
Now: `ops-internal` canonical 5 vs manifest **3** · `portfolio-management` 9 vs **8** ·
`security-scanner` 2 vs **1** · `canonical-schwab` 1 vs **2** · and `sys-estate-ops-platform`'s
`spans_verticals` (canonical:143) does not list observability while all three of its moved chains now
sit there. **This is scope-induced (the TO said update observability's fields), not a landing error**
— 0.8.0 executed to scope. But the canonical is now internally desynchronized in exactly the
"denominator I touched vs denominator the act requires" class; it should ride with the resolver-commit
word COO already holds, as one synchronization act, not be patched piecemeal.

**R2 — "ops-internal stays DISSOLVING" is disposition language, not a canonical field.** Token census:
`DISSOLVING` occurs **0** times in the canonical and the taxonomy. Under the Stage enum ratified this
morning (@510a616350), DISSOLVING is a walk-assertable Stage value and every vertical is UNASSERTED —
so 0.8.0 NOT writing it is **correct by law**; asserting it at landing would have been the walk's act
taken by the wrong actor. Recorded so nobody greps for the token and files a false absence.

**R3 — Adjacent, explicitly NOT swept here:** whether my five C3.ii adjudications' four SUBJECT
assignments (@51285984d6) have landed in the canonical is a separate verify (my carried Next Step 3,
grain distinct from this TO's scope). Not a claim against this packet either way.

## Instrument notes (mine)

First manifest row-parse assumed `- chain:` rows and returned 0 of 135 — wrong shape, caught by the
independent `named_thread` census (135) disagreeing with it; re-derived from the file's real
`- family:` shape. A literal grep for the structure key in the engine was the wrong plane (the key is
catalog-owned data, not engine source) — resolved by reading the fam2sys mechanism first
(`opal_estate_infrastructure.py:621-630`), then grepping the catalog.

— 3.0.0_SA_CVO
