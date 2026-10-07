# IRPT_CUSTDY decomposition -- ROUND 4 (issuer 2.0.0_SA_COO~K2; drafted 2026-10-07 ~10:5xZ, dell2)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:** the round-3 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_CUSTDY_ROUND_3_20261007.md`
@ec25e39844 (`1.0.0_SA_CTO~DELL2` msg 382), section 3: E1-E3, one issuance. receiving-check: UNCHECKED (no checker for a round analysis;
read by this seat). PRD v0.3 @1aa8fb7a0c ADMITTED. Code at HEAD: rounds 1-3 under `data/assets/scripts/gold/irpt_custody/`.

**Rule 24.** Domain: the analysis's E1-E3, nothing else (the template waits on the portal kit; hop 5's served render on IRPT_BCKEND E-P9;
the estate-wide 1,961 is `~P2`'s census). Three cells, three write sets, one fixed field between E1 and E2.

## Measured constraints (dell2, ~10:5xZ)

1. **The SI anchor ruling (S8a), verbatim order:** rule 1, the custodian's own account inception date where the accounts file carries
   one; rule 2, otherwise the gold's first data date for the account, labelled exactly `since <date>, the first date Opal holds`, NEVER
   "since inception"; rule 3, an anchor before 2010-01-01 reports SI as not available with that reason (the calendar covers 2010-2027
   and raises outside it; HOLD A lifted for 2010-2027, msgs 317/322). This replaces round 2's `HELD_CALENDAR_FIX` floor at 2024.
2. **Round 3's real run** (row S8): 10 households, 14 accounts for the chosen advisor (`matthew_gooch`, as-of 2026-09-30); SI NO_DATA on
   all 14 (no anchor resolved); 4 granted accounts NOT_IN_DIRECTORY and therefore listed as uncovered, with no report.
3. **S8(b) ruling:** the directory supplies only names and households; FWD-1 reads accounts from the ownership map. A NOT_IN_DIRECTORY
   account still gets its report, named from the ownership map, and the advisor's NOT_IN_DIRECTORY count prints with its denominator.
4. **S7:** `tests/test_advisor_projection_refused.py::test_none_source_names_the_seam_line` fails at HEAD since IRPT_BCKEND @b43f82c155;
   the suite must read 0 failed on CLOUD.
5. The returns gold in `opal-data-49financial` reads from dell2 since ~10:44Z (msgs 358/367): every cell's real-data check runs here.

## THE ANCHOR FIELD (fixed here so E1 and E2 run in parallel)

Every account document that `client_report_figures.py` builds carries
`"si_anchor": {"date": "<YYYY-MM-DD>"|null, "rule": 1|2|3|null, "label": "<text>", "status": "OK|NOT_AVAILABLE|NO_ANCHOR"}`:
rule 1 -> label `since inception <date>`; rule 2 -> label `since <date>, the first date Opal holds`; rule 3 -> status `NOT_AVAILABLE`,
label `not available: data before 2010-01-01`; no anchor at all -> rule null, status `NO_ANCHOR`. E2 reads this field from the documents and
prints it; E2's tests stub it.

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CU-d-1` (E1) | the SI anchor in `client_report_figures.py`: resolve rule 1/2/3 per account, write `si_anchor`, compute SI from the anchor when its date is on or after 2010-01-01, label per the ruling; retire the 2024 floor | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | A, `0.9.0_WK_IRPT_CUSTDY~9` |
| `CU-d-2` (E2) | the advisor's directory gap in `hop3_real_run.py`: a NOT_IN_DIRECTORY account gets its report named from the ownership map; print the count with the advisor's denominator; print each account's `si_anchor` (date, rule) from the documents | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | B, `0.9.0_WK_IRPT_CUSTDY~10` |
| `CU-d-3` (E3) | the suite green: retire or re-point the S7 tracer test; a committed check script prints the suite's failed count | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | C, `0.9.0_WK_IRPT_CUSTDY~11` |

## Write sets (disjoint)

- **CU-d-1:** `client_report_figures.py`, `tests/test_client_report_figures.py`, `tests/test_client_report_held_si.py`, `tests/test_si_anchor.py` (new), `si_anchor_probe.py` (new: the real-data check, prints the anchors per rule for one advisor).
- **CU-d-2:** `hop3_real_run.py`, `tests/test_hop3_real_run.py`, `tests/test_hop3_directory_gap.py` (new), `check_directory_gap.py` (new: the real-data check, prints the advisor's gap).
- **CU-d-3:** `tests/test_advisor_projection_refused.py`, `none_source.py`, `tests/run_suite_check.py` (new).
- (all under `data/assets/scripts/gold/irpt_custody/`). Each: its deliverables folder and the investigation file.

**New check scripts, not new flags:** the L6 gate refuses an expect bar that an existing tool does not print at the cut (round 2's
refusal), so each cell's real-data check is its own new script importing the changed module.

**Ordering and fan-out:** `fanout: 3 of 3 chains, cap 8` -- the anchor field above is the only seam between A and B; C touches neither.

## The issuer's acts after the drain

1. The one real run: `hop3_real_run.py --advisor matthew_gooch --as-of 2026-09-30` on dell2 after all three merges; grade E1 (1)-(2) and
   E2 (1)-(2) from it (each account's anchor and rule; SI computed for rule 1/2 anchors on or after 2010; the NOT_IN_DIRECTORY count with
   its denominator and every account reported). The file holds client figures and is not committed; a row carries its summary.
2. `tests/run_suite_check.py` on CLOUD after the last merge: E3's criterion.
