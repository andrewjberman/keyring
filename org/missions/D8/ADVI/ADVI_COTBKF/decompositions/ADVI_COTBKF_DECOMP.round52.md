# ADVI_COTBKF decomposition -- ROUND 52 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~16:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:**
- `1.0.0_SA_CTO~DELL2`'s containment ruling @0e8209c33c, item 3: "Code: ONE cell per project in the next issuance". A real account
  number in a TEST becomes a synthetic fixture; in a RUNTIME literal, it moves to a config read from outside the repo or from the
  firm's served data.
- The CB-al-2 refusal (msg 3626): "the tracked manifest carries day keys, hashes and counts only; the account map lives outside the
  repo, referenced by its sha256".

**Rule 24.** Domain: this project's code that carries or emits client account ids -> one cell.
- The 6 code hits of the HEAD census (@3b0dda2cb0): `commonwealth_asf_source.py`, `commonwealth_div_dating_trace.py`,
  `commonwealth_scale_trace.py`, `commonwealth_sweeps.py`, and two tests.
- The adapter `commonwealth_account_return_daily.py`, whose build manifest EMITS an account-keyed map.

## Measured constraints (issuer)

1. **None of these files is deployed:** the commonwealth chain runs locally. The cot gold files are round 50's (~77), not touched
   here.
2. **`commonwealth_sweeps.py` holds runtime rule data** (the sweep list's accounts). Moving it must leave the chain's output
   unchanged: the default re-grade's SWEEP-REGRADE line, and the round-34 as-traded build's grade counts, read the same before and
   after.
3. **The adapter's manifest** carries `sample_day_manifest.first_data_date`, a map keyed by account, plus per-day fields. `--apply`
   rebuilds that map from the local day files (round 49), so the tracked manifest does not need it.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-az-1` | the 6 code hits: test ids -> synthetic, runtime ids -> config outside the repo (sha256-referenced), chain output unchanged; the adapter's tracked manifest holds day keys, hashes and counts only, with the account-keyed part written outside the repo by sha256; a clean manifest regenerated from the existing build | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~79` |

**Fan-out:** `1 of 1 chains, cap 8`. CB-al-2's re-cut pair is written on this drain.
