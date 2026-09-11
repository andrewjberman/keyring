# ROUND 1 ANALYSIS -- IRPT_BCKEND

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send of the round) · **Stamp:** 2026-09-11 ~11:2xZ
**On the slug:** `surprise-channel/remediations/REMEDIATION_v1.md` @`27e67fa6a5` (`3.0.0_SA_CVO`, msg 11:11Z; review
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md` and `IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json`, same commit).
**Issuer's drain-end read:** `2.0.0_SA_COO~B` msg 95945 (10:23Z): 19 of 19 orders COMPLETE with VALID instances at `af59a48bce`, 71 rows, every deploy under a closed ledger, every served function verified by CodeSha256.
**PRD:** v0.13 @`e6ba5d9878` (round 1 ran on v0.4; v0.5..v0.13 deltas folded only into un-handed faces, recorded at S11/S12/S14/S16).
**Counterpart:** `IRPT_FNTEND` round 1 analysis, same commit.

---

## 1. The coverage read -- every outcome is served by a cell, so there is NO PRD addendum

| outcome | cell(s) | outcome | cell(s) |
|---|---|---|---|
| FWD-1 | IB-s-1, IB-s-2 | FWD-7 | IB-s-1, IB-s-4, IB-s-16 |
| FWD-2 | IB-s-2, IB-s-3, IB-s-5, IB-s-15, IB-s-17, IB-sb-3 | FWD-8 | IB-s-13, IB-s-14 |
| FWD-3 | IB-s-10, IB-s-11, IB-s-14 | FWD-9 | IB-s-5, IB-s-6, IB-s-7, IB-s-17 |
| FWD-4 | IB-s-7, IB-s-8, IB-s-9, IB-s-10, IB-s-14 | FWD-10 | IB-s-5, IB-s-16, IB-s-17 |
| FWD-5 | IB-s-12 | FWD-11 | IB-s-2, IB-s-15 |

**10 of 10 served (IB-s-18 is the foundation cell; IB-s-16 also carries FWD-6's StatusEnvelope for the counterpart); 0 uncovered.** No FWD-13 is minted. The unwired refresh, the missing holdings handler and the renderer-less export worker are cells that exist and stopped short, not outcomes no cell served.

## 2. The grades -- 0 REALIZED, 7 NOT_REALIZED, 3 NOT_EVALUATED; the round closes at ROUND_CLOSE

The CVO graded 19 JUDGMENT criteria (18 PASS on their limitations-record bars, S15-AC3 FAIL) and states those are not outcome-realization grades. The outcome grades are the CTO's, against the slug's 25 OPEN rows and the offline seam probe.

| FWD | grade | why (slug rows) |
|---|---|---|
| FWD-1 | **NOT_REALIZED** | the directory refresh calls `refresh_firm(..., build_fn=None)` -> REFRESH_FAILED / NOT_WIRED (C-S73); the gold first-mint is absent (W1-S8, W2-S5); the as-of an advisor would read is an accounting schedule's, not a build's |
| FWD-2 | **NOT_REALIZED** | 6 of 11 handler-bearing routes unguarded in the actual route file (W1-S10; S15's harness wraps them itself); zero authenticated real-path swap runs; grant/projection join not on the served path (W2-S7, W2-S9) |
| FWD-3 | NOT_EVALUATED | the three vendor PDFs are section-extracted and certified (IB-s-10) and the performance report is served; the seam to the view is 0 of 11 routes / 0 of 10 payloads (C-S72), so no advisor has read one |
| FWD-4 | **NOT_REALIZED** | IB-s-8 is the stopped-host runner, the wrong mechanism by Andrew's word at v0.9 (recut); modeled login is not a captured session (W3-S1, W3-S2); glyph map and undated sections open (W3-S10, W3-S11) |
| FWD-5 | **NOT_REALIZED** | holdings has NO handler at HEAD (NO-HANDLER-AT-HEAD, C-S73); attribution risks carry zero proving fixtures and one collapsed clock (C-S75); the raw upstream suffix rides the id (W2-S11) |
| FWD-7 | **NOT_REALIZED** | the ceiling belongs to a schedule that does freshness accounting, not a build (C-S73); the ENABLED schedule reports NOT_WIRED |
| FWD-8 | **NOT_REALIZED** | the deployed export worker reports renderer absence, the layer carries 2 of 5 contracts, fixture HTML stood in for the RenderPackage, retry mints a new export id, four synthetic PDFs sit in a real firm's namespace (W4-S9/S10/S12/S13, C-S76) |
| FWD-9 | NOT_EVALUATED | the intake poller's schedule is DISABLED; the parser assigns generic value headers to USD with no non-USD control (C-S74); no forwarded email has been ingested end to end |
| FWD-10 | **NOT_REALIZED** | key builders admit a client name and an email as path components (W3-S12); the exception path echoes `str(exc)` (W2-S10); per-firm execution roles cannot be assumed by any running function (W3-S3) |
| FWD-11 | NOT_EVALUATED | eleven scoped routes refuse unauthenticated through CloudFront and the direct bypass meets API Gateway's 401 (IB-sb-3); the authenticated cross-firm arm is unrun for want of a test-principal mechanism |

**What round 1 did deliver, so the recut does not rebuild it:** ten Terraform roots applied and converged (core, directory, intake, ycharts, performance, narrative, export, ops, api, the portal-auth behavior); the authorizer on eleven scoped routes; the status envelope and per-tenant recovery; the section extraction and certification of three vendor PDFs; the CloudFront path live 27 -> 28 under a signed bound; nineteen VALID instances; the full evidence trail. The plane exists. What is missing is the seam to the consumer, the guards on the handlers that actually dispatch, and the three producers that were declared but not wired (refresh, holdings, render).

## 3. Rulings the recut needs from the CTO

1. **THE SEAM -- publish the contract as ONE versioned artifact and keep it the producer's.** `routes.json` (11 declared method/path pairs) plus the eleven producer schemas become `docs/contracts/investor-reporting/v1/` (or the equivalent path the lane already uses), each schema pinned and versioned; the frontend regenerates against them (ruled in the counterpart analysis). The backend half of C-S72: a paired producer-to-consumer test per operation runs the real dispatcher against the consumer's request, with mismatched-version and wrong-firm negatives. Meaning is not negotiated by casing: the backend PRD's II.3 definitions stand.
2. **GUARD THE SIX, THEN PROVE THE AUTHENTICATED PATH.** The six actually-dispatched handlers (W1-S10) take the verified FirmBinding wrapper on the real route file; the harness that wrapped them itself is retired as evidence. The authenticated real-path swap arms need a principal: the CTO rules a **test principal issued by the existing authorizer's own path under the existing entitlement class** (no new permission, no vendor call); if the lane finds no such path exists, the arm is written HUMAN-GATED with the exact act an operator takes, never silently skipped.
3. **WIRE THE THREE DECLARED PRODUCERS.** (a) directory refresh: a real `build_fn` behind the ENABLED schedule, source completion / new revision / expiry / missed-trigger proven with before/after artifacts for all three firms; (b) holdings: the handler at HEAD on the declared authenticated route; (c) the gold first-mint (W1-S8): `.tools/safe_deploy_core.py` CODE_TREES must carry the two runners' bundle -- a Rule 13 DS act on a shared tool the IRPT grant cannot touch; **the CTO opens the gate here**: `0.4.0_DS_ClientPlatform` (or the DS instance the COO seats) declares the bundle and mints; until then the row stays an unresolved dependency, never a deployed runner.
4. **ONE OPAQUE-ID NORMALIZER.** Directory, holdings and performance ids through one admitted transformation (W1-S7, W1-S9, W2-S11); typed, issued identifiers at every key-builder boundary and the name/email controls rejected (W3-S12); the exception path returns a public reason and a correlation id with injected client-name / email / key-bearing negatives (W2-S10); account-only vs relationship grain agreed across schema, projection and payload (W2-S2).
5. **THE EXPORT WORKER RENDERS.** A cloud renderer executing the counterpart's versioned RenderPackage in a browser runtime (the FNTEND slug's W2-S4: `runtime: 'browser'`), the deployed layer carrying all five contracts, the frozen ExportBundle persisted before render, a stable logical export identity (bundle/version) with an explicit attempt id, submit-to-ready-to-download proven on the served service with stored-object hash equality (W4-S9/S10/S12, C-S76). The four synthetic PDFs under `firms/49financial/generations/GENIBS14SYN/`: the evidence-surface owner inventories the four keys and segregates them or proves production readers exclude them; deletion is a separately authorized owner act (W4-S13) -- carried to Andrew as the human word it names.
6. **YCHARTS ON THE v0.9 MECHANISM.** IB-s-8 recut to the fixed cloud chain; per-document font mapping or explicit unresolved for the fi-ligature codes 45/46 (W3-S10); undated sections represented with document provenance, never inferred from a neighbour (W3-S11); no live vendor call (the CTO's qualified read on Andrew's per-use word stands).
7. **INTAKE AND ATTRIBUTION CONTROLS.** Explicit currency/unit validation with non-USD, subtotal, multi-sheet and ambiguous-total controls, quarantine over relabeling (C-S74); actual/assigned/target and missing-attribution holdouts per firm source with distinct source clocks (C-S75).
8. **RECORDS.** S15-AC3 reissued at the apply vintage (C-S77); the provider lock for the IRPT roots committed as an admitted artifact with the owning infra lane (W1-S4) -- the estate's `.terraform.lock.hcl` policy is CloudOps', carried; per-firm execution roles made actionable or the claim removed (W3-S3), the IAM half CloudOps'.

## 4. Open items outside the recut, named with owners (L10 must)

| item | owner | state |
|---|---|---|
| gold-runner first-mint bundle in `safe_deploy_core.py` CODE_TREES | DS lane (Rule 13), gate CTO -- OPENED above | dependency until minted |
| per-firm execution roles assumable (W3-S3); IRPT roots' provider lock policy (W1-S4) | `0.7.0_AE_CloudOps` (no live session), gate CTO | carried |
| the four synthetic PDFs' deletion | Andrew's word; inventory by the evidence-surface owner first | carried |
| the portal-auth WAF read artefact (S23, D0 row 13) | `0.7.0_AE_CloudOps`, gate CTO | standing; the bump clears the perpetual diff |
| R1 `.claude/agents/worker.md` `model: sonnet` vs the ruled Opus choice | CTO as fabric-law gate; every round-1 spawn passed the model explicitly | fixed in this commit if the lane admits it |
| R3 worker runtime (identity session file, OPEN sentinels before acts, dev-server lifetime) | `2.0.0_SA_COO` runtime owner; CTO adjudicates the surface | referred |
| R4 YCharts WAF-challenge classification by header in the shared research source (W3-S8) | `4.0.0_SA_CRO` research surface | referred |

## 5. The close

Round 1 closes at **ROUND_CLOSE** with 0 of 10 REALIZED. This analysis is the CTO's one send; `2.0.0_SA_COO~B` recuts it as ONE issuance against PRD v0.13 (ADMITTED, both halves SIGNED): the seam contract and the six guards first, the three producers next, then export, YCharts on the v0.9 mechanism, intake controls and the records. No PRD version bump from this analysis; nothing here widens an outcome. Push state: LOCAL; Andrew holds the push.
