# Session Log — 0.4.0_DE_ClientPlatform — 2026-07-23 0355–0435Z — 3F-BF2 + P3a PROD check + guard wiring
**Archetype:** build+verify at Andrew-tempo ("right now immediately")

## Arc
1. **3F-BF2 built + ACCEPTED** (portal DEV 7394a58f): paired-read accessor (pairedProvenanceRead.ts,
   schema = CRO @708661904 §1a, shape 4-way aligned with DS pre-hardening — his emit == my read,
   derivation mine at per-firm grain, fail-safes confirmed); direct-read-failing guard
   (provenance-read-guard.mjs) MUTANT-PROVEN; all 7 raw-read sites migrated (global branch included);
   Interpolated band derived entirely from point_class (shrink-proven via the v1/v2 exercise — v1's
   incomplete-channel fixture accidentally exercised the missing-entry fail-safe end-to-end, caught by
   READING the render). Canonical republish render-verified (Long Term canonical blue, 3 ETags md5-MATCH,
   zero code change — data-driven paths absorbed the re-key).
2. **P3a dropped-signal loop closed by COO**: promote had LANDED 0152Z (PROD 5ef8bc63 / portal-v2.1.142 /
   CI 29972762013 SUCCESS); DT's signal to me dropped. **PROD verification run in full** (evidence
   @ee3d6db85): deployed ModelPortfolios chunk carries 4/4 distinctive f8ace4f8 literals (code identity);
   cottonwood internal+claims render ground truth on the REAL opalinvest.dev bundle ($458M/$124.4M/294/
   291-funded/median $207,443, Long Term canonical blue); inflection ($202M/713) + 49financial
   ($1.64B/7,041) regressions FULLY POPULATED live — residual (b) closed; global unauthenticated state
   unchanged. Honest limit: transport-injected ETag-verified served bytes for the data legs (stub session
   cannot pass edge auth); credentialed click-through = Andrew's own live session / demo-tenant candidate.
3. **Guard wired at BOTH layers per CTO 042253Z, WIRING mutant-proven**: pre-push (canonical
   .tools/portal-hooks/pre-push @7015a0a45) REFUSED a real push of a planted violation file:line-named;
   clean push accepted (90d2fbc5, 1807b12a). CI backstop step in portal ci.yml before typecheck.
   Candor: probe commit used bare `git commit --no-verify` on the deleted scratch branch (mutant vehicle,
   never merged, disclosed to CTO); CI limb not live-exercised (would require landing a violation to
   prove violations can't land — offered CTO a sanctioned draft-PR ref if wanted).

## Compiler Tools
| Run | Observed | Verdict |
|---|---|---|
| comp-surface-check check x2 (by hand + in safe-commit) | SEV1 headline/benchmark flagged both commits | READ; SURFACE_ACK audited both (accessor migration preserves values, provenance attached) |
| comp-transform schema-check ModelPortfolios --feature interpolated | not run as named — the component-level instrument was DEGRADED earlier tonight (types-resolution WARN); contract grounded instead on CRO @708661904 + DS's cited emit block + the served artifact bytes | SUBSTITUTED with stronger grounding, stated |
| provenance-read-guard (mine) | clean=0; planted mutant=1 naming file:line; hook-level: real push REFUSED; clean push accepted | PASS, mutant-proven at BOTH the test and the wiring |
| bunx tsc -b x3 | 2 real type errors caught (cohort_class null, meta shape) then clean | PASS after fixes |
| /frontend-dev renders x9 read | band exercise v1/v2, canonical served, 5 PROD legs | PASS; v1 caught the incomplete-channel fixture defect by render-reading |
| aws s3 cp + md5 vs DS ETags | 3/3 MATCH (canonical trio), earlier trio 3/3 | PASS — byte-identity grounded |

## Standing
- ARMED: BF2 acceptance render on DS's real served point_class[] (BF1); qt5 real data may shrink the band.
- AT CTO: whether to live-exercise the CI limb on a sanctioned ref; demo-credential instrumenting call.
- Instrument gaps open: comp-transform on this component; comp-validate config for G8 producer (DS).
