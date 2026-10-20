# TO NFRA_SCHWABBF.TO-BF-k3 -- the Schwab bronze key function on the PER-MASTER rule: firm form for 0840 and Cottonwood, today's key for 0824 and 0833

<to_id>NFRA_SCHWABBF.TO-BF-k3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-k-3` (`decompositions/NFRA_SCHWABBF_DECOMP_R3.md`) |
**outcome_ref:** FWD-1, FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-k-3`, PRD v0.7 C-KEYFORM. Andrew-direct ~16:3xZ, verbatim: "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out." and ~14:3xZ: "abiding by the path structure that already exists in that bucket ... schwab vendor and 49 firm for the 0840 and cottonwood firm for the various master accounts".
v0.7 text: "**The firm form applies per master:** the key function holds the set of firm-form masters (08403355 and the four Cottonwood masters) and returns today's key, byte-for-byte, for any other master, so 0824 and 0833 are written and read exactly as before. One master is never stored in two forms."

**What exists (read, then change only the two key-function files and the test).** Round 2 (merged `ef38445985`) rewrote both files so that ALL SEVEN masters, including 08242234 and 08335338, take the firm form. That is wrong now, and it is a live hazard: `data/black_diamond/scripts/bronze/_monolith_bronze.py` is mapped by the deploy gate to `s3://opal-data-bd/code/`, where the live bd converters resolve master 08242234 for the purpose `model_portfolios`; deployed as it stands they would list the firm folder and refuse "not moved". Rework both files to the per-master rule.
- Pre-round bytes of both files (the master-form functions you must keep for 0824 and 0833): `git show 5f1ad506a4:data/black_diamond/scripts/bronze/_monolith_bronze.py` and `git show 5f1ad506a4:data/canonical/schwab/silver/_canonical_silver_lib.py`. The current firm-form block is the BRONZE KEY FORM block in both files (byte-equal today).
- The builder `lib/opal_naming.py address()`; registry `infra/logic/registry/scopes.json`. Measured: `address('schwab','49financial','bronze','acc','date=2023-10-17')` is `s3://opal-data-assets/schwab/49financial/bronze/acc/date=2023-10-17`; `address('schwab','cottonwood','bronze','acc','date=2026-10-16')` is `s3://opal-data-assets/schwab/cottonwood/bronze/acc/date=2026-10-16`.

**The per-master contract (other cells build against it; keep every round-2 name working, add the new ones).** Every function returns a KEY (no bucket).
1. `FIRM_FORM_MASTERS`: literal map `{"08403355": "49financial", "08719286": "cottonwood", "08134043": "cottonwood", "08165601": "cottonwood", "08480305": "cottonwood"}` in BOTH files (byte-equal block). `is_firm_form(master) -> bool` (membership). `firm_of(master)` returns the firm for those five and RAISES `KeyError` for any other master (including 08242234 and 08335338: they have NO firm form).
2. `bronze_partition_prefix(master, feed, date_compact)`: firm-form master -> `schwab/{firm}/bronze/{feed.lower()}/date={YYYY-MM-DD}`; any OTHER master -> TODAY's partition `schwab/{master}/bronze/{feed.lower()}/{date_compact}`. `date_compact` must be 8 digits and a real calendar date, else RAISE, for both.
3. `bronze_key_for_file(master, feed, date_compact, filename)`: `bronze_partition_prefix(...) + "/" + filename`; the filename MUST start with `{master}.`, else RAISE.
4. `monolith_bronze_key(feed, date_compact, master)`: same signature; for 0824 and 0833 it returns EXACTLY what the pre-round function returned (`schwab/{master}/bronze/{feed.lower()}/{date_compact}/{master}.CRS{date_compact}.{FEED}.zip`).
5. `parse_bronze_key(key)`: the firm form only (as round 2), and RAISES unless the master is a firm-form master and the path's firm equals `firm_of(master)`. `parse_legacy_bronze_key(key)`: the old master form, unchanged from round 2.
6. The listers (`list_bronze_dates` in the bd-tree file, `latest_bronze_date` in the silver file) keep names, signatures and return type (compact `YYYYMMDD`, sorted). For a FIRM-FORM master: the round-2 master-filtering behavior (list `schwab/{firm}/bronze/{feed}/`, keep names starting `{master}.`, take dates from `date=`; old-form-only RAISES "not moved" with the count; both forms: the firm form wins). For ANY OTHER master: the pre-round lister, byte-for-byte behavior, reading `schwab/{master}/bronze/{feed}/` for 8-digit partition tokens.
7. Both files' docstrings keep the supersession note of round 2 and add: the firm form applies only to the masters in `FIRM_FORM_MASTERS` (PRD v0.7 C-KEYFORM; Andrew-direct ~16:3xZ); 0824 and 0833 are unchanged.

**Test (`data/canonical/schwab/tests/test_bronze_key_form.py`, rework of the round-2 file).** Load both files by path; stub `boto3` and the listings; import `lib.opal_naming`, read the registry:
- SET: `FIRM_FORM_MASTERS` is identical in both files; its masters are all in the registry; each maps to the firm whose registry row lists it; it contains 08403355 and the four Cottonwood masters; it does NOT contain 08242234 or 08335338.
- PARITY, firm masters: 5 masters x 17 feeds (acc rps trn tnn sec uln ult rld rlu rly rtu rty fam slm upn upt trn_nna) x 2 dates (2023-10-17, 2026-10-16): both files return the same string, equal to `address(...)` plus the vendor name.
- PARITY, 0824 and 0833: for 2 masters x 17 feeds x 2 dates both files return the PRE-ROUND string; compute the expected value from the literal formula in item 4, AND for one feed/date per master prove it equals the function body at `git show 5f1ad506a4:<path>` by exec-ing that old source (the pre-round function, loaded under a different module name).
- GUARDS: wrong-master filename RAISES; bad date RAISES; `firm_of('08242234')` RAISES.
- LISTERS: firm master with two masters' files in one stubbed folder returns its own dates only; old-form-only for a firm master RAISES with the count; a non-firm master lists its OLD prefix and returns the same dates the pre-round lister returns on the same stub (run both on one stub).
- CONVERTER SEAM (name contains `converter_seam`): load `data/assets/scripts/silver/schwab_conversion.py` by path with `data/assets/scripts/lib` first on `sys.path` and assert its `feed_from_key`, `date_from_key` and `scope_from_key` return feed, date and MASTER for a key built by `monolith_bronze_key` for BOTH a firm-form master and for 08335338.

### ACCEPTANCE

<criterion id="BF3-k3-AC1" cell_refs="BF-k-3"><invocation>python -m pytest data/canonical/schwab/tests/test_bronze_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-k3-AC1` -- the set, firm-master parity with the builder, 0824/0833 parity with the pre-round function, the guards and the listers. The bar is a pytest summary line that STARTS with the passed count.

<criterion id="BF3-k3-AC2" cell_refs="BF-k-3"><invocation>python -m pytest data/canonical/schwab/tests/test_bronze_key_form.py -q -p no:cacheprovider --color=no -k converter_seam</invocation><expect>^1 passed[ ,]</expect></criterion>
`BF3-k3-AC2` -- the seam probe against the REAL neighbor: the converter's own readers accept both key forms.

<expected_criteria>BF3-k3-AC1,BF3-k3-AC2</expected_criteria>

Dry-run at the base: the round-2 test file reads `550 passed` against the all-firm functions (a control that proves nothing about the per-master rule). Rewrite the test FIRST and run both criteria: the 0824/0833 parity arms must FAIL against the all-firm functions; only then change the two files. If they pass before you change anything, stop and file a row.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named is READ and never edited.
- **LOCAL.** No S3, no network, no deploy. The deploy of the bd-tree copy is the issuer's release act and waits on your merge.
- **The next order in your queue (`TO-BF-m3`) imports this contract.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass. Row ids are shared across rounds: read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W1-S<k>` and use the next.

<paths>
data/black_diamond/scripts/bronze/_monolith_bronze.py
data/canonical/schwab/silver/_canonical_silver_lib.py
data/canonical/schwab/tests/test_bronze_key_form.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R3.md</decomp_doc> (round 3), cell `BF-k-3`.
<owned_cells>BF-k-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF3-k3-AC1, BF3-k3-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-k3.key-function-per-master.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF3-k3-AC1,BF3-k3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the function names with signatures, the pytest summary line for each criterion, the one commit hash covering both mirrors, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- key function and tests.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell touches no IAM and no network; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 1 (the all-firm function would break the live bd converters if deployed) and 3 (one script serves three masters) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.7 C-KEYFORM; Andrew-direct ~16:3xZ via CTO msg 109927; decomposition round 3 cell BF-k-3; round-2 reference `ef38445985`.
