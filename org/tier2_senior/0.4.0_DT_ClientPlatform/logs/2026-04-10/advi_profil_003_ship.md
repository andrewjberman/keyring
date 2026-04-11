# 0.4.0_DT Log: ADVI_PROFIL.003 -- Frontend tax_exposure wiring ship pass
**Date:** 2026-04-10
**Agent:** 0.4.0_DT_ClientPlatform
**TO:** ADVI_PROFIL.003 (DS book tax_exposure, frontend-wiring bundle)
**Portal commit:** 40e62083f84d66524bbdef0958e4eb057f2f3d42 (portal DEV)
**Author attribution:** 0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>
**Committer:** Andrew Berman (machine user)

## Discovery shortcut

DS's brief `docs/briefs/de-brief-profil-003-tax-exposure-already-live.md`
revealed that the `tax_exposure` field has been in
`platinum/advisors/{id}/summary.json` since the initial D_04 commit.
No gold-script change required. `.003` was effectively already
half-shipped on the backend. Only the frontend needed to consume it.

Andrew authorized RD to bundle the frontend wiring directly with their
in-flight work rather than running a separate DE cycle ("OPTION A"
response to RD's question).

## Handoff from RD

RD handoff message 20260410T231211Z, ~90 seconds after my .005 ship
pass finished. Tight bundle:

```
 M src/pages/AdvisorIntelligence/AdvisorBookView.tsx   (+8/-1)
 M src/pages/AdvisorIntelligence/types.ts              (+9/0)
```

RD explicitly avoided adding `role_breakdown` to the type — that shape
(from D_00c Option 1 with fee_paying/no_fee sub-objects) is unverified
in RD's session and was deferred to a follow-up if the data is needed.
Conservative decision.

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| bun tsc -b | `bun run tsc -b` (portal) | exit 0 |
| comp-transform schema-check | `comp-transform schema-check AdvisorBookView` | PASS "All rendered fields match their response types." |
| comp-transform fields | `comp-transform fields AdvisorBookView` | l3Decomposition/l4Account/l4Composition rendered at root level — matches the .005 extract architecture |

eslint scoped to just the 2 touched files was already run by RD pre-handoff (0 errors) and I did not re-run the full directory eslint since the delta was so small and comp-transform schema-check covers the type coverage end of the audit.

## Scope purity

During staging I noticed `AdvisorIntelligence.tsx` also showed as
unstaged modified in the working tree. This was NOT in RD's .003
handoff and is almost certainly RD's in-progress .007 work (the
`isFirmAdmin = internal || isAdmin()` one-liner gate change). I staged
explicitly with `git add src/pages/AdvisorIntelligence/AdvisorBookView.tsx src/pages/AdvisorIntelligence/types.ts`
so the `AdvisorIntelligence.tsx` edit stayed unstaged and is preserved
for RD's eventual `.007` handoff. The `.003` commit is scope-pure.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read RD handoff 20260410T231211Z | 2-file bundle, +17/-1 LOC total |
| 2 | git status in portal submodule | working tree matches handoff + separate .007 WIP |
| 3 | bun tsc -b | exit 0 |
| 4 | comp-transform schema-check AdvisorBookView | PASS |
| 5 | git add (scope-pure, 2 files) | staged |
| 6 | git commit --author=0.4.2_RD_AdvisorIntelligence | SHA 40e6208, 2 files, +17/-1 |
| 7 | git push origin DEV | 36bf0fd..40e6208 DEV -> DEV |
| 8 | git log origin/DEV -3 verify | HEAD = 40e6208 with RD author |

## Verification

```
$ git log --format='%H %an %s' origin/DEV -3
40e62083f84d66524bbdef0958e4eb057f2f3d42 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL.003 -- wire tax_exposure into Book L2
36bf0fdd55a1b92cb0d7dc41d0b16a86fcaf5881 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL.005 -- L3/L4 client drilldown lift
65e411c5e5a2262d1f9487df0cc83b6629d94e89 0.4.0_DT_ClientPlatform 0.4.0_DT_ClientPlatform: ADVI_PROFIL.002 -- extend Claims with advisorId, remove cast
```

Commit count: 1
Author: 0.4.2_RD_AdvisorIntelligence (correct)
File delta: 2 files changed, 17 insertions, 1 deletion

## Runtime expected behavior

- Every advisor's Profile → Book L2 view now renders `TaxCostBasisPanel` populated with the real `tax_exposure` values from the platinum summary JSON
- Smoke target from DS brief: `alex_bright` should render Taxable $136.9M (55.6%) / Tax Deferred $97.5M (39.6%) / Tax Free $11.9M (4.8%) / Total ~$246M
- Chase and Travis should see their own 49fin tax posture on Profile → Book
- No regression on admin BooksTab drill path — that path was already consuming `AdvisorBookResponse.tax_exposure` via the same `TaxCostBasisPanel`, `.003` just brings the non-admin Profile→Book path to parity

## .003 TO status

Flipped to `complete`. DS's gold-script side was already live (confirmed
per brief), and the frontend wiring shipped via this commit, so the TO
is fully closed end-to-end. No additional DS work required on `.003`.

## Current State

- portal DEV: `40e6208` live, `.003` + `.005` + `.002` + `.001` stacked cleanly
- RD: continuing on `.007` (admin My Profile toggle)
- DS: committed `.004b` (advisor_ownership.json per the filename I ratified), proceeding; `.003` is closed
- AE: `.004a` LIVE as `portal-auth-v1.11.8` + `v1.11.9`, curl matrix validated
- DE: `.008` baseline visual pass in-flight
- Parent workspace submodule pointer: NOT bumped (4 portal DEV commits accumulated: .001 3e8cc3f, .002 65e411c, .005 36bf0fd, .003 40e6208)

## Next Steps

- [0.4.2_RD_AdvisorIntelligence] `.007` handoff next — broker me when working tree ready
- [0.4.0_DS_ClientPlatform] `.004b` deploy + gold run + verification per normal DS deploy cycle
- [0.4.0_DT_ClientPlatform] Camp inbox-watcher for `.007` handoff, `.004b` completion, `.008` baseline results, AE `.004c` trigger once `.004b` lands
- [Andrew] Submodule pointer bump pending — 4 portal DEV commits accumulated, worth doing when the deploy cadence is ready
