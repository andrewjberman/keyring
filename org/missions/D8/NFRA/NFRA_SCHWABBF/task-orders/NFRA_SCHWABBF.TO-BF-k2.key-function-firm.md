# TO NFRA_SCHWABBF.TO-BF-k2 -- thread hop 1: the one Schwab bronze key function in the FIRM form, both mirrors

<to_id>NFRA_SCHWABBF.TO-BF-k2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-k-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-4 | **depends_on:** `TO-BF-z2` (merged before your worktree is provisioned; the two key-function files are at their pre-round bytes)

---

## WORKER FACE

### THE CELL

`BF-k-2`, PRD contract C-KEYFORM at v0.5. Andrew-direct 2026-10-20 ~14:3xZ, verbatim: "abiding by the path structure that already exists in that bucket ... its just schwab vendor and 49 firm for the 0840 and cottonwood firm for the various master accounts".
FWD-4 ACCEPT: "Someone who only knows the naming builder finds any stored Schwab raw file on the first try, and never finds the same day stored two different ways."
A first version of this work was built on the MASTER form (`schwab/<master>/bronze/...`) and is superseded. It is recoverable for REFERENCE ONLY with `git show 293346aff1:data/canonical/schwab/silver/_canonical_silver_lib.py`, the same path for `_monolith_bronze.py`, and `git show 293346aff1:data/canonical/schwab/tests/test_bronze_key_form.py`; reuse its structure, parsers and test layout, change the grammar.

**What exists (read, then change only the two key-function files and the test).**
- `data/black_diamond/scripts/bronze/_monolith_bronze.py` and `data/canonical/schwab/silver/_canonical_silver_lib.py` each carry `monolith_bronze_key(feed, date_compact, master)` and the partition listers (`list_bronze_dates` in the first, `latest_bronze_date` in the second). The first is MIRRORED, not imported (it deploys standalone to `s3://opal-data-bd/code/`): any change to the key grammar lands in BOTH files in one commit, with byte-equal helpers.
- Pre-round grammar (what is stored today): `schwab/{master}/bronze/{feed}/{YYYYMMDD}/{master}.CRS{YYYYMMDD}.{FEED}.zip`.
- The builder `lib/opal_naming.py` `address()`. Measured 2026-10-20: `address('schwab','49financial','bronze','acc','date=2023-10-17')` is `s3://opal-data-assets/schwab/49financial/bronze/acc/date=2023-10-17`; `address('schwab','cottonwood','bronze','acc','date=2026-10-16')` is `s3://opal-data-assets/schwab/cottonwood/bronze/acc/date=2026-10-16`.
- The firm of a master is in `infra/logic/registry/scopes.json`: the scope row whose `masters` list names it. `49financial`: 08242234, 08335338, 08403355. `cottonwood`: 08719286, 08134043, 08165601, 08480305. The bd-tree mirror cannot import `lib`, so BOTH key-function files carry the same literal map `MASTER_FIRM`; the test proves it equals the registry.
- The silver converter (`data/assets/scripts/silver/schwab_conversion.py`) derives type and date from the FILE NAME. READ ONLY here (another cell changes it).

**The firm-form contract (the other cells of this round build against it; do not rename).** Every function returns a KEY (no bucket, no `s3://`).
1. `MASTER_FIRM`: the literal map above (seven masters). `firm_of(master) -> str` returns the firm; an unknown or malformed master RAISES `KeyError` (no default).
2. `bronze_partition_prefix(master, feed, date_compact) -> str` = `schwab/{firm_of(master)}/bronze/{feed.lower()}/date={YYYY-MM-DD}` (no trailing slash). `date_compact` must be 8 digits and a real calendar date, else RAISE.
3. `bronze_key_for_file(master, feed, date_compact, filename) -> str` = `bronze_partition_prefix(...) + "/" + filename`, the vendor name UNCHANGED (`{master}.CRS{YYYYMMDD}.{TYPE}.zip`, or `{master}.CS{MMDDYY}.{TYPE}.zip` for `fam` and `slm`). The filename MUST start with `{master}.`; otherwise RAISE (the vendor-master guard, in the key function).
4. `monolith_bronze_key(feed, date_compact, master) -> str`: same signature as today, now `bronze_key_for_file(master, feed, date_compact, f"{master}.CRS{date_compact}.{feed.upper()}.zip")`.
5. `parse_bronze_key(key) -> dict(firm, master, feed, date_compact, filename)`: the NEW form only. The master is the 8 digits before the first `.` of the file name; the firm in the path must equal `firm_of(master)`, else RAISE; anything not in the firm form (including the old master form) RAISES `ValueError`.
6. `parse_legacy_bronze_key(key) -> dict(master, feed, date_compact, filename)`: the OLD master form only, `schwab/{master}/bronze/{feed}/{YYYYMMDD}/{filename}`; anything else RAISES. The move tool uses it. The filename must start with the path's master.
7. The listers keep their names, signatures and return type (compact `YYYYMMDD` strings) and FILTER BY MASTER: list under `schwab/{firm}/bronze/{feed}/`, keep only keys whose file name starts with `{master}.`, take the date from the `date=YYYY-MM-DD` token and return it compact, sorted. Several masters share the folder, so a lister that skips this filter SUMS 0824 and 0833, which the purpose law in these files forbids.
   If no new-form key exists for that master but the OLD master prefix `schwab/{master}/bronze/{feed}/` holds keys, RAISE `ValueError` saying the old-form count and "not moved" (an empty answer there would read as "nothing landed"). While both forms coexist (copy done, old not yet deleted) the new form wins and old-form keys are ignored. Neither form: `list_bronze_dates` returns `[]`, `latest_bronze_date` raises as it does today.
8. Both files' docstrings say: this grammar supersedes `{master}/bronze/{type}/{YYYYMMDD}/` recorded in `docs/architecture/OPAL_ASSETS_CONSOLIDATION_PRD.md` (lines 36 and 477) and `docs/architecture/OPAL_ASSETS_PRD.md` (line 494), by Andrew-direct 2026-10-19 and 2026-10-20 and PRD v0.5 C-KEYFORM. Do NOT edit those documents.
Keep every existing public name working.

**Test (`data/canonical/schwab/tests/test_bronze_key_form.py`, rewrite of the round-1 file).** Load both key-function files by path; stub `boto3` and the S3 listings (no network); import `lib.opal_naming` and read `infra/logic/registry/scopes.json` from the repo root:
- REGISTRY: `MASTER_FIRM` in both files equals the registry's firm-to-masters rows for the seven masters.
- PARITY: for the 7 masters x 17 feeds (acc rps trn tnn sec uln ult rld rlu rly rtu rty fam slm upn upt trn_nna) x 2 dates (2023-10-17, 2026-10-16): both files return the same string and it equals `address('schwab', firm, 'bronze', feed, 'date=YYYY-MM-DD')` without `s3://opal-data-assets/`, plus `/` plus the vendor name.
- GUARDS: a filename whose prefix is another master RAISES; an unknown master RAISES; a bad date RAISES.
- ROUND TRIP and the two parsers' refusals (each refuses the other form); the CS-form name survives.
- LISTERS: a stubbed listing with 0824's and 0833's files for the same type and dates returns each master's own dates only (the sets differ in the stub); a listing with only old-form keys RAISES with the count; a mixed listing returns the new-form dates.
- CONVERTER SEAM (test name contains `converter_seam`): load `data/assets/scripts/silver/schwab_conversion.py` by path with `data/assets/scripts/lib` first on `sys.path` (it imports `stream_parquet`, tracked there) and assert its `feed_from_key` and `date_from_key` return the feed and the date for a firm-form key built by `monolith_bronze_key` -- the neighbor every copied object will wake up. (`scope_from_key` changes in another cell; do not assert it here.)

### ACCEPTANCE

<criterion id="BF2-k2-AC1" cell_refs="BF-k-2"><invocation>python -m pytest data/canonical/schwab/tests/test_bronze_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-k2-AC1` -- registry equality of the firm map, parity of both mirrors with the builder over 7 masters x 17 feeds x 2 dates, the guards, the parsers, and the master-filtering listers. The bar is a pytest summary line that STARTS with the passed count.

<criterion id="BF2-k2-AC2" cell_refs="BF-k-2"><invocation>python -m pytest data/canonical/schwab/tests/test_bronze_key_form.py -q -p no:cacheprovider --color=no -k converter_seam</invocation><expect>^1 passed[ ,]</expect></criterion>
`BF2-k2-AC2` -- the seam probe against the REAL neighbor: the converter's own readers accept a firm-form key.

<expected_criteria>BF2-k2-AC1,BF2-k2-AC2</expected_criteria>

Dry-run at the base 2026-10-20: at the issuance commit AC1 reads `243 passed` against the round-1 MASTER-form files. That is why `TO-BF-z2` merges first: from the restored pre-round bytes the round-1 test file errors on import (the restored library has no `parse_legacy_bronze_key`), so AC1 and AC2 FAIL as expected in your worktree. Run both criteria before you change anything and record what they print; if AC1 passes there, stop and file a row.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named is READ and never edited.
- **LOCAL.** No S3, no network, no deploy. The deploy of the bd-tree copy is the issuer's release act.
- **The next orders in your queue (`TO-BF-m2`, then `TO-BF-r2`) import this contract.** Keep the names and signatures exactly as written.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/bronze/_monolith_bronze.py
data/canonical/schwab/silver/_canonical_silver_lib.py
data/canonical/schwab/tests/test_bronze_key_form.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R2.md</decomp_doc> (round 2), cell `BF-k-2`.
<owned_cells>BF-k-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-k2-AC1, BF2-k2-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-k2.key-function-firm.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF2-k2-AC1,BF2-k2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the function names with signatures, the pytest summary line for each criterion, the one commit hash covering both mirrors, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- key function and tests.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell touches no IAM and no network; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 1 (shared partition, master filter) and 3 (converter reads segment 1) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 C-KEYFORM, C-NAMES; decomposition round 2 cell BF-k-2; round-1 reference `293346aff1`.
