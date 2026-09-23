# R closer status

Owner: `4.0.0_SA_CRO~Z`. September 23, 2026. **Active; MVP incomplete.**

Candidate worktree: `C:/tmp/amgt-r-20260923`, branch `closer/amgt-r-20260923`, base `db3267d079718ad47cc1ce338292d7e5f5640d55`. This worktree isolates R changes from other closers and the dirty shared checkout. [Authority](AUTHORITY.md) records the direct assignment and execution relay.

## Implemented and exercised

`lib/research/reports/inputs.py` supplies immutable input references, byte hashes and per-part method/input dependency stamps. It returns named stale reasons when input content, source key, availability, method bytes/version or part dependencies change. Invalidation reaches downstream recommendation/Posture parts, retaining unrelated parts. Explicit absence and failed reads differ; a repeated failure never becomes fresh. Dependency cycles, unknown parts, duplicate identifiers and malformed hashes refuse.

**PASS, offline exercise:** 15 unittest cases; Ruff check passes. These are synthetic controlled cases, not retained-data, provider, browser or deployed acceptance. [Evidence](EVIDENCE.json) records the exact source hashes and exercised results. The component has no production caller yet; its first intended consumer is the per-part report producer. It neither authorizes publication nor resolves whether an input is acceptable.

Exact-seat lane preflight allowed the new report module/test paths and this deliverable home. A negative control rejected `portal/src/pages/SecurityAnalysis/Report.tsx` as POD_DE_ANY. The validator did not reject the tested registry path, but that does **not** settle its explicitly undecided owner; R makes no registry change.

## Next work and dependencies

1. Independent H review of this component; CVO review of I5/I6 examples once the typed-claim decision is settled.
2. Consume C's I4 positive/absent/stale examples, retaining the actual five-member shape. Artifact semantic hashes and retained-byte hashes must remain distinct.
3. Complete report schema, producer, evidence gates and immutable history/store against the accepted contract; integrate S/H source examples. Review the figure/synthesis semantic fork in [INTERFACES.md](INTERFACES.md).
4. Prepare authorized serving/export changes; portal authoring and canonical registry publication need the named owners/grants.
5. Obtain readable model/input/fund-form rulings and a bounded per-use run before live synthesis. Complete deployed, browser, export and full-population proof afterwards.

Gaps R01-R04 and S04 remain open. No historical research measurements are silently refreshed by this implementation status.
