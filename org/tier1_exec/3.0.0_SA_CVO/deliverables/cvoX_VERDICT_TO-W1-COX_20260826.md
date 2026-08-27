# CVO~X proof-of-spec verdict — NFRA_SUBSTRATECARDING.TO-W1-COX · **PASS**

**Verifier:** 3.0.0_SA_CVO~X · **Verified:** 2026-08-26 ~19:4xZ · **Lane:** 0.7.0_AE_CloudOps~X (73287)
**Artifacts:** C3i.json + comp_similar.json + instance @35c9a9b7ed (worktree ≡ commit, measured at my
seat). Push state LOCAL as the lane measured (fired positive control cited); rides integration.

## Battery (my own invocations)

| check | result |
|---|---|
| proof-of-spec-check with COX-AC1..AC7 | **VALID rc=0** · alignment ENFORCE · 7/7 · 16/16 · 16/16 · vintage resolves |
| v1 schema over both cards | **0 errors, 2 of 2** |
| basis+evidence+owner | **14/14 rows complete; 0 absent rows** — UNSOUND/QUALIFIED verdicts coherent under AC-F3 |
| AC4 — **NEGATIVELY SATISFIED, the strong form** | `determinism: deterministic` established by the two-arm control, read in the card's own evidence at my seat: same-input byte-identical (2,477 bytes twice) AND different-subject (`opal-mcp-audit`) DIFFERS. Trigger {inferential,hybrid} unmet → null `inference_detail` CORRECT. `invocations_per_run = 0` is the pricing answer, not an evasion |
| wave as_of | byte-identical ×2, on-anchor, on-pin (carded_utc 19:09:51Z, lane batch read) |
| back-dating | CLEAN — 1 anchor occurrence per card, the as_of field |
| coverage denominators | non-null both cards |
| Rulings 1+2 | currency-in-evidence present; explicit semantic-axis UNMEASURED in verdict.why on both cards, with what was NOT examined named (SIM_TWIN=0.60 intent, domain set currency, composer definitions) |
| Andrew-direct 1907Z application | **C3i `authority_role: evidence` — the correct call, taken by the owning lane** as routed; the ABSENCE of a stable C3 layer carried as the finding, not softened |
| COX-AC6 | committed set = 3 files, all lane deliverables; 7 carded generator/source files untouched (lane's git-status read; commit content verified at my seat) |

**Verdicts accepted: C3.i UNSOUND (5 blocking defects, 2 honestly UNOWNED) ·
comp-similar QUALIFIED.**

## Noted with approval, on the record

- **The 1.031 signature re-attribution** is model verification conduct: the suspicion's SHAPE
  reproduced (8 THIN rows at byte-identical sim=1.0 sorted above discriminating results) while its
  MECHANISM was re-attributed (templated thin summaries scored deterministically, not a
  non-deterministic process) — and QUALIFIED-not-UNSOUND is justified by the exercised blind-row
  control protecting the load-bearing --supersede path. Sound prior, corrected mechanism, both kept.
- **The sha1-key two-axes finding** (docstring "STABLE by construction" true on reproducibility,
  false on survives-ordinary-change — 5 arms, one variable) and the **exact-arithmetic open question
  stated as OPEN not as a finding** (4 static = 4 live is consistency, not provenance) are exactly
  the discipline the rubric asks for.
- **Third census-trap layer surfaced:** comp-keys --all on a wide prefix returns "CAPPED at 5000" —
  the lane narrowed until a complete denominator printed before any absence claim. Added to the
  rubric's absence-row check.
- The lane's tail-eats-rc self-catch and the independent additionalProperties rediscovery (with
  priority correctly ceded to 0.8.0_AE_CloudComp~X) are both in the instance, as they should be.

## Verifier disclosure

My first spot-check of the AC4 two-arm control returned a false "arm missing" — my own regex
(`byte.?identical`) failed to match the evidence's "byte-compared -> IDENTICAL" phrasing. Caught by
reading the artifact before concluding; the corrected read confirms both arms. Recorded because a
verifier's instrument error that survives becomes a false REWORK — the exact class this wave has
been catching all day.

— 3.0.0_SA_CVO
