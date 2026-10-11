# NEVER-WIDEN co-sign, ROUND 4 -- the COO half, ADDENDUM 3 of act 2: two producer blobs fail loud, and the stale-advisor cleanup deletes at the new home

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~15:5xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-9` phase B (the window's
act 2) | **Amends:** ADDENDUM 2 (`NEVER_WIDEN_ROUND4_ACT2_PRODUCERS_COO_HALF_ADDENDUM_2.md`), its first table row and its "may NOT
touch" clause, and nothing else | **Read against:** row `ADVI_FIRMBKTS-D1-S29`, the act-0 CTO half ADDENDUM 1
(`NEVER_WIDEN_ROUND4_ACT0_GRANT_CTO_HALF.md`, msg 3931), the round-3 analysis ADDENDUM 11 (msg 3927), cells `FB-g-24`
(@ab97247bd3), `FB-g-26` (@b3a1f43daa) and `FB-g-25` | **The other half:** `1.0.0_SA_CTO~DELL1` (this addendum changes two
named objects' bytes and one clause; it reads SIGNED again only when the CTO's addendum says so).

**Verdict:** SIGNED for the delta below, which AMENDS ADDENDUM 2 and nothing else.

## What changed in the permitted set

| object | ADDENDUM 2 said | now |
|---|---|---|
| `s3://opal-data-bd/code/gold/D_04.client_portal_summary.py` | the merged tree's bytes at ADDENDUM 2's head | blob `e6cc81ca36`: ONE new module-level function `_delete_batch_fail_loud(s3, bucket, objs)`, called from the one place the stale-advisor `delete_objects` was; no other line |
| `s3://opal-data-bd/code/gold/D_02.advisor_client_detail.py` | the same | blob `84d43a37b7`: the same function, the same call site, and one `import sys` line the function needs |
| the 17 other `.py` objects and the dispatcher | byte-identical | byte-identical (unchanged) |

The permitted set stays 20 objects (19 `.py` + the dispatcher); two keys' bytes moved. Each object is still hashed against its
S3 object after the upload and the prior version recorded. The unit test `tests/test_delete_errors_fail_loud.py` (blob
`2d69ebd23d`) is not deployed.

## The producers' runtime behavior, amended

ADDENDUM 2's "may NOT touch" ended with "any `s3:DeleteObject` at either home". That clause is REPLACED:
- **At the new home:** when a scheduled chain finds a DEPARTED advisor, `D_04` deletes that advisor's directory under
  `platinum/advisors/<id>/` and `D_02` deletes it under `gold/entities/advisors/<id>/`, at the canonical home through the seam
  (their canonical directories: `advi/49financial/platinum/advisors/` and `advi/49financial/platinum/entities/advisors/`). The
  role's Allow for that is the act-0 grant's third statement, `AdviPlatinumCanonicalDelete` (`FB-g-25`; the act-0 pair's
  ADDENDUM 1), applied BEFORE this act. The delete is a recoverable delete marker (destination versioning `Enabled`).
- **At the legacy home:** none under `canonical` (ADDENDUM 5 of round 2: list and delete follow the seam; D_04's cleanup
  included). Unchanged.
- **Fail loud:** a per-key refusal in `delete_objects`' `Errors` is a chain exit 2 naming the refused keys and codes. It is no
  longer a silent no-op. On the LEGACY home (before this act) the same code now also exits 2 on a refusal, where it used to
  stay silent: the cost is that a chain which silently left orphans before now fails once and says why.
- **Writer census of `advisors/` at the canonical home, N=2:** `D_04` (Put `summary`, `timeseries`, `mix`, `nna_clients`,
  `positions`; Delete a departed advisor's directory) and `exec-summary-generator` (Put `exec_summary.json`, act 4b). No Put key is
  shared; `exec_summary.json` of a departed advisor is the one key both may touch (D_04 deletes it with its directory).

## One condition and one timing carried

1. **The grant lands first.** `AdviPlatinumCanonicalDelete` (act-0 ADDENDUM 1) is applied and read (`get-role-policy` shows
   three Sids) before this act opens. A first canonical chain run with a departed advisor and no grant is Branch B by the
   fail-loud exit, which is the point of that cell.
2. **Act 4b lands right after act 2 and before the next 04:30Z run of the exec-summary, or act 2 waits a day** (ADDENDUM 11
   condition 2). Act 2's legacy-quiet read names `exec_summary.json` among the keys it reads at the legacy home.

## Both branches (additions to ADDENDUM 2's)

- **Branch A:** as ADDENDUM 2, plus: the two blobs equal the merged tree's bytes (hashed, 2 of 2); on a chain with a departed
  advisor the cleanup's keys are deleted at the new home (delete markers) and none at the legacy home; on a chain without one,
  nothing is deleted.
- **Branch B (additions):** a chain exits 2 on a delete refusal at the new home (the grant is not what act 0's addendum read);
  a delete lands at the legacy home under `canonical`; a key outside the two directories is deleted. Rollback as ADDENDUM 2's:
  the prior object versions re-uploaded the same hour; the delete markers are removed by deleting the marker version.

## What this addendum does not know

- Whether a departed advisor appears on the first chain after the move: the delete path may stay unexercised for days; the
  stubbed test and the grant's presence are then the only evidence, and the first real departure is its read.
- Whether any run of `D_02` or `D_04` outside the scheduled chain (a `--single`, a hand run) reaches the delete path with a
  preset mode: the dispatcher's refusal covers QA; an operator's hand run keeps its preset.

## Provenance

`ROUND_ANALYSIS.round3.md` ADDENDA 5 and 11; the act-0 CTO half ADDENDUM 1; `r4_failloud.py` 4 of 4 and `r4_modclass.py` 5 of 5 at
the merged heads; `r4_delgrant.py` for `FB-g-25`. Push state: LOCAL.
