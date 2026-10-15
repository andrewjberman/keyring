# L4-R review -- MDPF_CANON PRD v2.23, ratified-text half (ENDPOINT + CONTRACTS)

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-15 ~19:1xZ. Delivered by 1.0.0_SA_CTO~DELL1 msg 6129 (acked).
**Graded:** `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @c81505610d (v2.23, half hash d388fe8bbfd3) against v2.22 @ff1e47f079,
which this seat signed (`L4R_REVIEW_MDPF_CANON_v2.22_RATIFIED_TEXT_20261015.md`).

## Verdict: SIGN, with one finding for the decomposition (below)

## The change (the whole diff v2.22 -> v2.23: 47 insertions, 4 deletions)

1. Header `prd_version` v2.22 -> v2.23.
2. **ENDPOINT, FWD-9 head (a):** a demo-tenant session draws exactly as an internal session; "every other session" narrows to "a claim
   with no firmId".
3. **ENDPOINT, FWD-9 head:** "until the Cottonwood Trend addendum" becomes "(v2.23)"; new **(f)** the Cottonwood Trend and **(g)** Muni.
4. The v2.23 addendum at the foot, outside ENDPOINT and CONTRACTS.

## The four checks

| Check | Result |
|---|---|
| ENDPOINT against its pins | **(a)** The record `ANDREW_DIRECT_20261015_162xZ_DEMO_GLOBAL_TREND_USES_VARIANT1_NEXT_PROMOTE.md` @c81505610d lines 12-15 read "just use the same code as global view" and "it should get added on to the next prod promote of the portal". **(g)** `ANDREW_DIRECT_20261015_152xZ_MUNI_IS_CUSTOM_MODELS_EVERYWHERE.md` line 5 reads "Muni is in Custom Models, yes"; `ANDREW_DIRECT_20261015_184xZ_HAPPYLAND_MUNI_IS_CUSTOM_MODEL_OPAL_MUNICIPAL_BONDS.md` @fee736b125 lines 8-9 read "a Custom Model, Opal Municipal Bonds; it's with Cottonwood. It should be included in the Agggregate "Custom Models" group in the global view." That record is not in c81505610d's tree; it was read at its cited pin. **(f)** The CRO spec @21caa664be lines 15, 60, 64-66 give the window start 2026-06-09, Total = `partner_custody_total`, Other AUM = total - `model_aua`, 12 carried model-leg dates and an exact partition; the head states exactly these, base only. |
| Every operative constraint present | Yes. (b)-(e), the partition clause and the Global rule table are unchanged. (f) keeps the interpolated marking before 2026-07-20 and the to-the-cent partition; (g) names only Muni and keeps "never Other AUM or non-model". |
| No annotation, history or seat name inside the section | Four version tags were added inside ENDPOINT: "(v2.23, Andrew 2026-10-15)" at line 199, and "(v2.23)" at lines 219 (twice) and 226. No seat name was added. The section already carried "(v2.18)" and Andrew-direct citations that this seat signed at v2.22, so this is the existing practice, not a new class. Nit: drop the tags at the next ENDPOINT edit; the addendum carries the history. |
| CONTRACTS agrees with the counterpart PRD | No CONTRACTS line changed between the two pins. |

## Finding for the decomposition (not a ground to refuse: the ENDPOINT text is right; the addendum's claim is wider than the code)

The addendum says (a) "disarms D1-S29 ... Variant 2 is not repaired, and it remains only for a claim with no firmId". On portal origin/PROD
33ad65eef3, `src/pages/ModelPortfolios.tsx` sets `effectiveFirmId` to `claims?.firmId ?? 'global'` for a non-internal session outside
`MDPF_GLOBAL_VIEW_FIRMS`, and `trendModeFor(internal)` gives that session Variant 2. So a non-internal claim with no firmId opens Global
on Variant 2, which overdraws the Total on the 9 carried dates (`ADJUDICATION_v17.md` D1-C-S90). ENDPOINT still requires that session's
groups to partition the Total. D1-S29 is disarmed for the demo tenant only. For the no-firmId class, round 11 needs one of three things:
a Variant 2 repair (drop `modelsBand` on dates at or after per-model detail begins), proof that no such claim can reach the page, or a
CTO ruling that the class is out of scope. Whether any live login carries no firmId was not measured here.

## Carried nit from v2.22

FWD-9 DONE WHEN (1) still describes the Client chips reading the dated category-views history route. v2.23 did not reconcile it; the head
still governs.

-- 3.0.0_SA_CVO
