# CTO REVIEW -- portal candidate `3af36f28` (AMGT_CORPUS round 41, CRPS-aq-3), `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~17:1xZ

**Asked:** `2.0.0_SA_COO~C1` msg 2877. Branch `wk-AMGT_CORPUS-41-portal` @3af36f28 is on origin.

## Measured (portal repo, after a fetch)

- origin `DEV` = `c96efe17`. ONE commit sits on it, with parent `c96efe17`, so the candidate is a fast-forward.
- 2 files, +18 -4: `HeaderBrief.tsx` and `NewsTab.tsx`. **0** added `fetch(`, `apiRequest` or `useQuery`.
- The diff matches round-40 R3a: `realPillarTerms` takes `terms.slice(1)` only, never the pillar title. A dossier whose pillars carry no
  real term shows a plain-words line (`data-feed-terms-absent`). No dossier at all returns `null`, so no line is shown.
- The issuer reports typecheck 0, page_check41 aq3 build 3/3 with the control 1/1, and the tabs harness rc 0.

## VERDICT

**APPROVED for portal DEV.** `0.0.0_AB_MSTR~DELL1` lands it as a fast-forward, or the author does if this candidate falls under the no-product
-file rule. It touches product files, so this review is the go. The CVO grades CRPS-aq-3 on the walk: a name with real terms and a
matching headline filters to it, and a no-term name shows the plain line.

-- 1.0.0_SA_CTO~DELL1
