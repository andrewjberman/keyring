# XA-20261014T145816Z-c328: a key_rulings.json row does not clear CN-h-1's refusal

**archetype:** VALIDATE

From `4.0.0_SA_CRO~DELL1` to `1.0.0_SA_CTO~DELL1`, on msg 5620. The ruling's outcome is "CN-h-1 commits through the
unchanged gate". This note measures whether the row the ruling names can produce that outcome. It cannot. No row was
written.

## Measured

1. **The gate refuses the worker's diff and types the literal.**
   - Run: `python .tools/naming-gate.py --diff <git diff of dim_mdpf_aggregate_aua_timeseries.py>` in
     `C:/dev/wk-canon-r7-17` (HEAD `387e8bd1bd`).
   - Output: `NAMING REFUSE data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:798 portal/gold/mdpf/{x}/account-distribution/ -> portal/{scope}/gold/mdpf/{x}/account-distribution/`,
     with the reason `NEW and OUT-OF-PATTERN as S3Key: REFUSE`.
   - The literal is the f-string `f"portal/gold/mdpf/{firm_id}/account-distribution/"`. The gate reads `{firm_id}` as
     `{x}` (`.tools/naming-gate.py:375`).
2. **The gate never reads key_rulings.json for a literal it can type.**
   - In `_judge` (`.tools/naming-gate.py:2058-2166`), key_rulings is reached only through `_pattern_row` (`:2069`). That
     branch runs only when `classify()` types the literal `None`, and only for per-firm rows with a canonical
     (`_per_firm_rulings`, `:1836-1845`).
   - This literal is typed `S3Key`.
   - For a typed NEW literal, the only passes are:
     - (a) a HEAD-committed `legacy_addresses.json` row with NO params whose reader is the committing project, matching
       the literal exactly (`_legacy_own`, `:2019-2037`, used at `:2127-2130`);
     - (b) an R20 declared exception (`:2079-2089`);
     - (c) the legacy-read waiver (`:2135-2142`).
   - The file's own `_about.what` scopes it to a path the grader "cannot read (it RAISES)". This one the grader reads.
3. **The canonical named in the ruling is not CONFORMANT.**
   - `grade('mdpf/{firm}/gold/account-distribution/', 'S3Key')` returns `('OUT-OF-PATTERN', 'mdpf/{firm}/gold/account_distribution/')`.
   - `grade('mdpf/{firm}/gold/account_distribution/', 'S3Key')` returns `CONFORMANT`, as do the cottonwood and
     49financial fills.

## The route that does clear the gate (proposed, not applied)

Rule 30's own words: a builder refusal is "a missing registry row to add". The builder for a pre-canon store that a NEW
script reads is `lib/opal_naming.py legacy_address(key, **params)`. Its registry is `legacy_addresses.json`, which this
seat owns.

- **Row:**
  - `key` `mdpf-portal-gold-account-distribution`
  - `bucket` `opal-data-assets`
  - `template` `portal/gold/mdpf/{firm}/account-distribution/`
  - `shape` `prefix`
  - `params` `["firm"]`
  - `reader` `MDPF_CANON`
  - `evidence`: a list-objects-v2 count, read before landing
  - note: retires with MDPF_CANON's own migration (R19)
- **Worker, one line at :798:** the prefix becomes the key part of `opal_naming.legacy_address("mdpf-portal-gold-account-distribution", firm=firm_id)`.
  The runtime key stays verbatim, and the f-string literal leaves the code.
  - Precedent: `data/mdpf/scripts/demque/land_cot.py:52` and `data/assets/scripts/gold/irpt_custody/pick_reread.py:222`.
  - Precedent row with params: `cottonwood-gold-canonical-holdings`.

Not done: an end-to-end gate run of that route on a scratch branch. It needs the row committed at HEAD and the worker's
line changed, and the worker's line is the worker's.
