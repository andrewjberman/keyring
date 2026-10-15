# L4-R review -- MDPF_CANON PRD v2.22, ratified-text half (ENDPOINT + CONTRACTS)

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-15 ~14:5xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 6036 and 6038 (both acked).
**Graded:** `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @ff1e47f079 (v2.22, half hash 3763f83bcc87) against v2.21 @3826492d9c,
which this seat signed (`L4R_REVIEW_MDPF_CANON_v2.21_RATIFIED_TEXT_20261014.md`).

## Verdict: SIGN

## The change (the whole diff v2.21 -> v2.22: 14 insertions, 2 deletions)

1. Header `prd_version` v2.21 -> v2.22.
2. **ENDPOINT, FWD-9 head**: "Firm scopes are unchanged by (a)-(d)" gains "except that at a firm scope the Client chips draw on the as-of
   date only, and the dated category-views history route has no required reader until the Cottonwood Trend addendum."
3. The v2.22 addendum at the foot, outside ENDPOINT and CONTRACTS. It answers this seat's CN-j-1 AC4 NOT MET (C-S83, ADJUDICATION_v15).

## The four checks

| Check | Result |
|---|---|
| ENDPOINT against its pins | The sentence states what the served page already does at a firm scope (`clientChipAt`, portal PROD `src/lib/trendGrouping.ts:97-109`: a chip draws on the as-of date only). Andrew approved that view: the bytes at `ANDREW_DIRECT_20261014_201xZ_PORTFOLIOS_SMOKE_TREND_FULL_HISTORY_COTTONWOOD_SPEC.md` @caf5dc7d73 lines 10-11 read "49 Financial View: No comments, everything is good to go here. Third for the Inflection view: No need to touch these", and he sent Cottonwood to a CRO spec. At Global the chips were already retired by (a)-(e). No FWD's DONE WHEN or ACCEPT moves, and FWD-3 is untouched. |
| Every operative constraint present | Yes. (a)-(e) and the Global rule table are unchanged. The history leaf stays served and covered by its pair (CONTRACTS row and surface-manifest row unchanged), so retiring the reader serves less and widens nothing. |
| No annotation, history or seat name inside the section | No seat name or citation was added. "Until the Cottonwood Trend addendum" is a forward condition, not history; it names the act that re-opens the question. |
| CONTRACTS agrees with the counterpart PRD | No CONTRACTS line changed between the two pins. |

## Nit (not a ground to refuse; fix at the next ENDPOINT edit)

FWD-9 DONE WHEN (1), at `MDPF_CANON_PRD.md`@ff1e47f079 lines 258-264, still reads "The Client chips read the dated category-views objects
through a READ-ONLY served history route ... The grade is read with that route live." The head's exception now governs the firm scopes,
and the chips are retired at Global, so this sentence has nothing left to govern. It reads the same way the v2.19-v2.21 Global overrides
read against the older DONE WHEN text, which this seat signed on the head's precedence. A grader should follow the head. Reconcile the
sentence at the next edit, so the next grade does not have to rule between two texts.

-- 3.0.0_SA_CVO
