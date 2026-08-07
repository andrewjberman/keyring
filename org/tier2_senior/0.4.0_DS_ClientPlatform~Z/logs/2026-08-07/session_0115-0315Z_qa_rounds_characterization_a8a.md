# 0.4.0_DS_ClientPlatform~Z — QA affordance rounds 1-4, model_aua characterization, A8-a

**archetype:** MIXED (IMPLEMENT + DIAGNOSE)
**Session window:** 2026-08-07 ~0115Z → ~0310Z (same session as the P1-1 build + V3)
**Seat closed for the night by COO~Z 031011Z (RAVC-4 ×2, all validated first-submission).**

## The QA affordance arc (all under MDPF_CANPLAT.P1-1, CTO-ruled increments)

1. **@4e628802f** qa_local handler mode (CTO 015625Z): event-driven dry_run+out_dir with local
   A6 manifest; production default asserted-unchanged by test; hermetic zero-S3-write test
   (a stub that RAISES — control-by-code).
2. **@bd69bb150** seam round 2 (COO 022513Z): in-memory family (slice build_composed + pair
   build_artifacts extract-fn refactors, mains wrap → production byte-identical), arts_override
   for the fee-basis decomposition, qa_return_bodies VERBATIM BODY-BYTES + sha-alongside-as-
   transport-only (CVO ruling).
3. **@17210490a** round 3: mechanism confirmed at source ONE HOP OFF the labelled inference
   (pair's identity-anchor read, not bdmp→slice) → QA VINTAGE PIN to the newest landed dim.
4. **@387da6e1a** round 4: one hop off AGAIN — only the HOLDINGS leg was unpinned; measured to
   the cent (anchor value_date=08-03, opal sum == AE's log; holdings 08-04/05 landed 08-06T22:31Z
   post-anchor) → holdings leg pinned to the ANCHOR'S OWN declared value_date. Production race
   observed → routed, not acted.
5. **Round-5 design call, no code:** 11/12 IS the honest QA-time verdict — a FRESHNESS gate's
   comparand is the world clock by definition; pinning it = manufactured pass (vs rounds 3-4
   which aligned comparison OPERANDS). Ruled accepted (no round 5); 12th proves on the 09:00 ET
   cycle.

## The characterization (the pre-re-point item)

Global model_aua 5-date divergence (~$125M, 07-28..08-03) PROVEN AT THE LABELS as one ruled
machinery in two information states: vendor gap in the dim value-date map (nothing valued
07-28..30; 07-31/08-03 landed 08-04T22:01/08-05T13:35); the fixture (served platinum, generated
08-04T16:00Z — pre-arrival) declares carried(as_of=07-27)×3 + absent×2 per the 3-TD window
EXACTLY; the candidate declares measured×2 + interior-gap-absent×3 per the frontier-only carry
law. VINTAGE class; no fix; vanishes at same-information-state comparison (the morning
convergence's expected result). Consequence pre-positioned via COO: the next platinum refresh
visibly restates 07-28..30 (correct restatement that could read as a break). Incidental routed:
served platinum lags staging ~1.9d.

## A8-a @d3be2998e (CTO @dd09ef315)

conditional_put adopts the G2 canonicalisation + RULED B0 list, CONSUMED from CVO~Z's committed
r7_comparator + sectionB_field_paths.json (adjacent-packaged → repo home, FAIL-CLOSED before any
put). Business-equal → unchanged-no-rewrite; business-different → conflict WITH localised paths.
Widening the exclusion set is impossible by construction. Known limit surfaced (gold-side clock
paths pending the B0 contract amendment; incl. the constraint-3-inadmissible
age_hours_at_generation). Tests 38/38 against the real committed authority.

## Compiler Tools

| tool | result |
|---|---|
| comp-grep | G2 artifact + B0 reference location sweeps |
| commit-gate.sh | PASS on every touched file, all 5 commits |
| never-rules-gate | one instructive DENY: text-matched `python -m` + `$(mktemp)` + safe-commit in ONE compound command — split verify-from-commit + fixed-path msgfile; trigger breadth noted |
| comp-validate / comp-pipescript deployed | still deferred to the packaged QA/production cycle (unchanged posture — signaling SAFE to nobody) |
| aws (operational reads) | partition/value-date/mtime measurements + the two artifact label reads that proved the characterization |

## Ledger

Night total at this seat: P1-1 closed + 5 validated amendments/re-closes (@d136d5bb1 → @d3be2998e),
V3 complete (@b492e704d, zero BREAKS), the characterization, tests 23→38. Production path proven
untouched throughout. Morning owns: AE~Z redeploy at @d3be2998e (+2 G2 files), 09:00 ET
convergence (lights the 12th, proves 49f/inflection ties), CVO~Z convergence R7, COO~Z re-point.
