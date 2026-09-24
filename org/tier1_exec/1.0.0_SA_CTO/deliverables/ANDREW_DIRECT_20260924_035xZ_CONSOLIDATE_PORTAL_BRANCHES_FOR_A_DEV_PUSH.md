# Andrew-direct 2026-09-24 ~03:5xZ at the 1.0.0_SA_CTO terminal -- consolidate the portal branches for a DEV push

Seat: 1.0.0_SA_CTO (Claude).

## VERBATIM

"Whoever is in charge of the dev build, make sure it is built with the most recent information/structure. I
dont know if all the different COOs are building on different branches or what, but somebody has got to
consolidate for a push to DEV"

## THE FACT

Portal work of this window sits on three branches with no assigned integrator (the CTO's gap):
- portal DEV head codex/local-live-data-20260923 @c1ac41ec (MSTR pushed 01:5xZ: P's reason-code render fix
  + two live-data commits);
- 2.0.0_SA_COO~M codex/irpt-m-ui: b0e2d9ad (model coverage counts a model descendant), 67158601 (drill
  affordance + child count, single-account first screen one level deeper, "Rebalancer strategy: <name>"
  label), parent e7e6eaea (overlay labels);
- 2.0.0_SA_COO~P p-reason-codes-20260924: 8e616985 (ClientSearch names a rejected per-firm browse).

## RULING IRPT-PORTAL-DEV-CONSOLIDATION-20260924 (CTO 100129)

1. 2.0.0_SA_COO~P (shared client surface owner) builds ONE candidate cut from c1ac41ec, merging M's pin and
   P's 8e616985 (never rebase; one merge commit per source; conflicts resolved per side with the owner named;
   no drive-by edits), runs install / tsc / eslint / the affected suites / a production build, and reports
   the head, merge commits, counts and a diff stat against c1ac41ec.
2. 2.0.0_SA_COO~M names the exact pin and freezes portal commits until the candidate lands.
3. 1.0.0_SA_CTO reviews the candidate and says GO.
4. 0.0.0_AB_MSTR pushes portal DEV to the GO'd candidate on THIS word (no further ask), ls-remote hash in the
   receipt, local checkout fast-forwarded, and tells Andrew what DEV now carries.
5. The backend functions deploy from P's publish worktree and are outside this act; the COT Holdings re-cut is
   a backend publication and does not gate the DEV push.

Bound: only committed and reviewed work rides the candidate. Push state LOCAL at write (origin/CLOUD
f96a0b9dd4 per MSTR 99987).
