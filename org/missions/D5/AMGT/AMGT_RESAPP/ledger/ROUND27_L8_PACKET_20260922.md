# AMGT_RESAPP round 27 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `5726f647e1`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-22 ~13:3xZ.

**DRAIN-END, complete:** 2 of 2 terminal, 0 open.
- Issued as one slug @`40f01c2b08`, on the CTO's ruling msg 24216 (on msg 24215).
- Round 27 is NOT bound by Andrew's backfill gate (msg 24217); neither cell is a backfill.
- Both cells are code or read-only: no pair, no word, no live write.

## 1. Round state, final

| cell | drain | second instrument (this seat's own) |
|---|---|---|
| rk-106 B4 roster/domain diagnosis (READ-ONLY) | `e7c45ca8b5` | The two load-bearing citations were re-read at the worker's HEAD: `battery.py:1182` hard-sets `"officer_section": None` on the company-site route, and `enrich.py:166-174` `verified_domain_for` returns `verified_site.host`. The branch diff touches ONLY the deliverables, the channel row and the order (0 code files). The worker's census: 21 of 21 prefixes, 1,780 objects before and after, 0 changed. |
| rk-105 filing_attempt SKIP-HELD / CHANGED-HELD | `5726f647e1` | Diff read in full. The outcome projection excludes `retrieved_at`, `seconds`, `tests` and every `reason`. SKIP-HELD returns a receipt and skips the read-back. A changed outcome raises `FilingAttemptChangedError` (a `HarvestStoreError` subclass, so the 4 other writer call sites keep their raise). `battery.main` catches ONLY that subclass around a name's pool write, prints `CHANGED-HELD`, continues, and returns 2 with a summary. A run with no changed outcome prints as before. Suites in the worktree: harvest 79 (72 + 7), filings 100, management 95/13. **MERGED TREE: harvest 79, filings 100.** |

## 2. For the grade -- named, none hidden

1. **rk-105 was AMENDED mid-flight (ISSUER AMENDMENT 1, CTO msg 24221), before any build.**
   - The CTO rejected this seat's REC to keep the raise, and ruled CHANGED-HELD with a non-zero exit at run end.
   - The amendment was written into the worker's own worktree copy of the order (committed WITH its work, so no shared-tree conflict) and relayed to the worker as a ruling.
   - Changes: item 1 gains the subclass; item 3 gains the catch, the summary and exit 2; one test was added; AC1 went from 6 to 7 and AC2 from H0 + 6 to H0 + 7.
   - It is a MODIFICATION, so the gate does not grade it (a human discipline, per Rule 27).
   - The worker confirmed the amended text by `git diff` against the base before building.
2. **rk-105 AC0 drift:** `writer_call_sites` read 5, where the order's prose said 6. The literal script excludes the harvest mover's own definition-module call; this is recorded, not failed, per AC0's own rule. The worker's report also printed AC0's harvest line as "79"; this seat's re-run and AC2 both read 79 AFTER the build, and the base is 72 (8 test files at the base, 9 at HEAD).
3. **rk-106's rows:** W106-S1 (the cell text named "the model block" as an S3 object that does not exist as such; answered via the crosswalk record instead, and the answer is unaffected).

## 3. Andrew's keying rule (msg 24223) -- the check this seat owes

"No cell may bake in a NEW dependency on the ticker-derived security_key form beyond what exists today."
- **rk-105:** no new dependency. It keys the existing write-once object by the existing `security_key` partition and adds no new key or lookup.
- **rk-106's recommendation**, NOT built: Lusha's domain falls back to `verified_domain_for(source_object)`, which reads `verified_site.host` from the filing object. The domain itself is issuer-verified, not ticker-derived. The source object it reads is still LOOKED UP by the existing `security_key`. That is existing coupling, not new, but it is FLAGGED here so the key design (composite FIGI, msg 24227) can re-key it.

## 4. What rk-106 found -- the inputs to a later round, none cut (the backfill is gated on Andrew's three preconditions)

- 6861's officers are served today from the Bloomberg `COMPANY_EXEC_OFFICERS` fallback (1 officer), not from its filing.
- The filing roster is empty because the company-site route never extracts an officer section (`battery.py:1182`).
- The only verified domain candidate is `verified_site.host` = `www.keyence.co.jp`, found by subtraction over 6 objects, 19 URL occurrences and 5 hosts.
- Candidate cells for the next round:
  - (1) Lusha's `domain_for` falls back to `verified_domain_for`;
  - (2) should company-site wins attempt officer-section extraction?
  - (3) the RESOLVED marker reader cell (already agreed, with a pair).

## 5. What this seat asks of L9/L10

Grade the 2 terminal cells. Neither carries a judgment criterion.
