# CTO placement -- the holdings-surfaces check, placed into MDPF_SECCLASS's next round

Author `1.0.0_SA_CTO`, clock read 20:56Z 2026-10-05 (4:56 PM Eastern). On `4.0.0_SA_CRO` msg 105381.

**Inputs**
- Andrew's word, at the `4.0.0_SA_CRO` terminal:
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_204xZ_HOLDINGS_SURFACES_ONLY_CANONICAL_ETFCLASSIFIER_TABLE.md`.
  "I want to make sure that we are consistently using ONLY the canonical ETFClassifier table. I do not want holdings being
  displayed from any other table or going through any other process. rivalfunds is an internal product and not related."
- The check: `docs/briefs/holdings-surfaces-canonical-classifier-check-20261005.md` @35859eb97d (`4.0.0_SA_CRO`; its measurements,
  not re-read by this seat).

**Scope of this note.** His word to the CRO ordered a check. This note orders no work and stops no seat. It records where each
finding already has a home in MDPF_SECCLASS's ratified outcomes, for this seat's next round analysis of that project.

| Finding (check section) | Home in MDPF_SECCLASS PRD v0.4 | Placement |
|---|---|---|
| 2.1 Investor Reporting Holdings tab: `bd-securities` fallback and three guess layers behind the canonical table (ruling 103169's declared exception) | FWD-4 (no second definition), FWD-5 (the old copy gone), FWD-11 (the AI classifier fills what nothing else places) | The fallback comes out AFTER the table holds the securities it labels today (the check counts about 496, 476 and 770 by firm, overlapping). FWD-11 is what makes that reachable. Removal is a served move per firm under C-SERVED. Ruling 103169's exception ends with that removal, not before |
| 2.1 served basis `TABLE` does not say which table answered | FWD-6's "a reader can tell" | Moot once the fallback is gone; until then it is a row for `2.0.0_SA_COO~M` |
| 2.3 and 2.5 two hardcoded portal lists (`Positioning/constants/etf-categories.ts`, `Attribution/constants/etf-categories.ts`) and `getSubAssetClass`'s fallback branch; `portal/src/lib/tickerRegistry.ts` | FWD-4: "every place in the code that assigns a class to a security outside the one shared list" | In scope of FWD-4's check. Whether the check's denominator reaches `portal/src` is read at the next round analysis; if it does not, the check is widened first |
| 2.2 Positioning ETFs mode: class and sub-class from Bloomberg's sector | FWD-6 names it as a DECLARED exception, ratified | CONTRADICTED by "ONLY". This seat does not retire a ratified outcome's exception on a word given to another seat for a check: one call to Andrew |
| 3. five classification paths not traced to a page | FWD-4 | A trace cell each, next round |

**Not decided here:** the geography list in the positioning Lambda (the table has no geography field), and the Black Diamond
library's identity step for a blank ticker (the class still comes from the table).

-- 1.0.0_SA_CTO
