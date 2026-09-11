# ROUND 1 ANALYSIS -- IRPT_FNTEND

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send of the round) · **Stamp:** 2026-09-11 ~11:2xZ
**On the slug:** `surprise-channel/remediations/REMEDIATION_v1.md` @`27e67fa6a5` (`3.0.0_SA_CVO`, msg 11:11Z; review
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md` and `IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json`, same commit).
**Issuer's completion report:** `2.0.0_SA_COO~F` msg 95938 (09:56Z): 11 of 11 orders terminal, drained in both repos (portal DEV `edab15b5`, workspace `2e50d2e129`), 41 rows.
**PRD:** v0.6 @`d1479bc5f0` (round 1 ran under the frozen v0.4 throughout; v0.5/v0.6 changed F5 and CONTRACTS after the cut).
**Counterpart:** `IRPT_BCKEND` round 1 analysis, same commit -- the seam finding below is ONE finding with two halves.

---

## 1. The coverage read -- every outcome is served by a cell, so there is NO PRD addendum

| outcome | cell(s) | outcome | cell(s) |
|---|---|---|---|
| FWD-1 | FE-s-1, FE-s-2, FE-s-3 | FWD-6 | FE-s-1, FE-s-3 (+ FE-s-7's lifecycle states) |
| FWD-3 | FE-s-4, FE-s-5 | FWD-8 | FE-s-4, FE-s-8, FE-s-9 |
| FWD-4 | FE-s-4, FE-s-6, FE-s-9 | FWD-11 | FE-s-2, FE-s-10 |
| FWD-5 | FE-s-7 | FWD-12 | FE-s-2, FE-s-4, FE-s-11 |

**8 of 8 served; 0 uncovered.** No FWD-13 is minted. The three things round 1 could not reach -- a partner firm reaching the route, the v0.5/v0.6 Generate composer, the mounted export flow -- are cells that exist and were not finished, not outcomes no cell served. This analysis is the answer; the ROUND-2 issuance is `2.0.0_SA_COO~F`'s.

## 2. The grades -- 0 REALIZED, 5 NOT_REALIZED, 3 NOT_EVALUATED; the round closes at ROUND_CLOSE

Every FNTEND bar is EXERCISED. The CVO graded ten JUDGMENT criteria on the images (1 PASS, 5 FAIL, 4 NOT_EVALUATED) and measured the seam offline; the grades below are the CTO's read of the outcomes against those.

| FWD | grade | why (slug rows / criteria) |
|---|---|---|
| FWD-1 | **NOT_REALIZED** | no partner-firm session can reach `/investor-reporting` -- all four allowlists omit it and a firm session lands on `/market` (W1-S10; F10-AC9); the client's 11 operations match 0 of 11 declared backend routes (C-S42) |
| FWD-3 | **NOT_REALIZED** | F5-AC8 FAIL: screen and print figures come from different fixtures, return units ambiguous, mobile columns clip |
| FWD-4 | **NOT_REALIZED** | FE-s-6 was built on v0.4's shape; the v0.5/v0.6 Generate composer (S10) is unbuilt; `AnalysisRequest.inputRevision` / `ReportSection.parity` semantics unagreed (W3-S2); F6-AC8 NOT_EVALUATED (no clean/correction pair) |
| FWD-5 | NOT_EVALUATED | F7-AC7: the target / missing-attribution comparison was never captured; the tab renders on fixtures |
| FWD-6 | NOT_EVALUATED | lifecycle states exist and the one-firm loop is repaired (W1-S12 disarmed), but no partner session and no agreed seam means the states were never exercised against a real backend response |
| FWD-8 | **NOT_REALIZED** | `AppliedBranding` and `ReceiptPanel` defined and UNMOUNTED (W1-S11); NarrativePacket semantics unagreed and the placeholder still renders (W2-S6); Lato absent from the package (W2-S3); F8-AC8 NOT_EVALUATED, F9-AC8 FAIL |
| FWD-11 | NOT_EVALUATED | the Global view is visible and firm attribution shown; the firm-advisor refusal half is unprovable while no firm can reach the route (F10-AC9) |
| FWD-12 | **NOT_REALIZED** | F11-AC9 FAIL: mobile clipping/overlap, missing typography, unused export components; F2-AC7 FAIL on the original captures (repaired in FE-s-3, credited as a repair, not as the bar) |

**What round 1 did deliver, so the recut does not rebuild it:** eleven orders with VALID instances; 322 passing tests across 48 files; the three-tab shell, header with the Model Portfolios dropdown, tabs, Holdings drilldowns, export modal and RenderPackage, Global view with a multi-firm catalogue; 65 components censused (27 reused, 38 new with reasons). The parts exist. The SEAM between the parts and the backend does not, and that is the whole of round 2.

## 3. Rulings the recut needs from the CTO (the decisions the slug said were the CTO's)

1. **THE SEAM -- the producer defines, the consumer conforms.** The FNTEND PRD's CONTRACTS section already says it: contracts are "consumed from the counterpart, whose PRD carries the field definitions ... this project never redefines a contract's meaning, units or dates." So: `infra/aws/terraform/investor-reporting/api/routes.json` is the authoritative method/path table, and the backend's producer schemas (its II.3 inventory, 11 of 11 positive controls passing) are the authoritative shapes. The frontend's eleven POST-to-slug operations and its ten failing consumer fixtures are the defect (C-S42). The recut cell: regenerate `portal/src/api/endpoints/investor-reporting.ts` and `LiveClient` against routes.json and the producer schemas, and replace isolated fixture agreement with ONE paired producer-to-consumer test per operation that crosses the real client into the real dispatcher (stale and wrong-scope negatives retained). No casing translator without economic meaning: where a field's MEANING differs, the backend PRD's definition wins and the frontend changes. The backend's half (publishing the contract as one versioned artifact) is ruled in the counterpart analysis.
2. **THE ROUTE MUST BE REACHABLE BY A PARTNER FIRM.** `portal/src/lib/firmAccess.ts` `FIRM_ALLOWED_PATHS` admits `/investor-reporting` for the three registry firms (49F, Cottonwood, Inflection). This is a portal-access file inside the portal tree; the CTO rules it IN SCOPE for a round-2 cell under FWD-1 / FWD-11 (the outcomes cannot be exercised without it), with the F10 proof re-cut: a firm session reaches IRPT, sees only its own scope, has no Global path; an unauthorized firm is still refused.
3. **DEV GOES GREEN FIRST.** The FIRST cell of the issuance clears the eight TypeScript errors in `__tests__/fe-s-11/` (S17) and every round-2 order carries `tsc -b --noEmit` exit 0 as a bar. No push of DEV before it lands (ruled 09:58Z).
4. **LATO IS A PACKAGING INPUT, NOT EGRESS.** The OFL 1.1 files already on this box (`.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/Lato-{Regular,Light,SemiBold}.ttf`, licence text at `docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt`) go into the render package with their hashes recorded; 600 stands in for 700 and the package says so; the 700 fetch stays a carried call for Andrew. No new source is fetched.
5. **THE GENERATE COMPOSER IS A RECUT CELL (F5 at v0.6, S10).** Client from the header, accounts as labels, immutable snapshot with as-of, 0-5 ordered opaque comparison keys, title, policy-limited overrides, displayed variant, per-click `request_id`; the `resolved` envelope never leaves the server; job states polled from the Opal job record.
6. **MOUNT THE EXPORT FLOW.** `AppliedBranding` + `ReceiptPanel` wired to the applied bundle / receipt state; no-assets, approved-assets, running, failed, ready/download states proven on the MOUNTED flow (W1-S11). NarrativePacket: the backend's field set is the meaning; absent history renders MISSING HISTORY (W2-S6).
7. **EVIDENCE RULES FOR ROUND 2 (S15/S16/S17 lessons, now face law for this project):** paired screen/preview/print from ONE frozen report; a unique-file manifest for every capture claim; every smoke criterion keys on a printed discriminator; every expect is a plain token; a fixture map names the WHOLE page's needs; the four NOT_EVALUATED surfaces (clean/correction Analysis; observed/target/missing-attribution Holdings; narrative-on and pre-history print) captured on the mounted views; mobile clipping fixed and captured at 390.

## 4. Open items outside the recut, named with owners (L10 must)

| item | owner | state |
|---|---|---|
| Lato 700 weight (egress) | Andrew's per-use word | CARRIED; 600 stands in |
| push portal DEV + workspace CLOUD | `0.0.0_AB_MSTR` on Andrew's word | CARRIED; after the first round-2 cell lands DEV green |
| R5 `ui-smoke.mjs` DID-NOT-LAND on query-string routes (W2-S5) | the portal smoke-tool owner; DSGN_REBRND R7/R14 touch the same instrument | referred, not an IRPT cell |
| R3 worker runtime (identity session file, OPEN sentinels, dev-server lifetime) | `2.0.0_SA_COO` runtime owner; CTO adjudicates the surface | referred |
| the recurring portal-auth WAF diff | `0.7.0_AE_CloudOps`, gate CTO (D0 row 13) | standing |

## 5. The close

Round 1 closes at **ROUND_CLOSE** with 0 of 8 REALIZED. The ROUND-2 ANALYSIS above is the CTO's one send; `2.0.0_SA_COO~F` recuts it as ONE issuance against PRD v0.6 (ADMITTED, both halves SIGNED), first cell the typecheck repair, then the seam, then the reachable route, then the composer and the mounted export, with the evidence rules on every face. No PRD version bumps from this analysis; nothing here widens an outcome. Push state: LOCAL; Andrew holds the push.
