# TO IRPT_DASHBD.TO-DB-i-1 -- the Inflection QTD TIE-OUT re-run under THREE VALUE BASES (all rows, active rows only, cash lines excluded): the gap distribution per basis against Orion's client return and the count of households that move down a bin; a private table and counts only; nothing written to AWS

<to_id>IRPT_DASHBD.TO-DB-i-1</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~301</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>114</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (B-IN is this workstream) and the round-109 analysis ("this seat rules the tolerance on that read") | **Rows:** IRPT_DASHBD-D2-W301-S<k> | **Decomp cell:** `DB-i-1` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 1) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-301`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~301/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report; an account number, a household or client id, a name or a figure (a return, a value, a flow) is never recorded; a household is named only by the sha256 (hex, utf-8) of its id. Your private folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~301/` (create it).

**Why.** Round 109 derived Inflection's account returns and tied the accounts, aggregated per client, to Orion's client return for the quarter to date: of 287 comparable households 16 sit under 5 bp, 87 at 5 to under 25 bp, 175 at 25 to under 100 bp and 9 at 100 bp or more (33 not comparable). The CTO must rule a tolerance on that distribution, and the value basis is an open question: the basis summed every row of Orion's positions, including cash lines and rows whose `isActive` is false (which carry non-zero value on some account-days; the silver does not define `isActive`). This cell re-runs the QTD tie-out under three bases so the CTO can see which basis closes the gap. It rules nothing.

**The inputs, all existing and all private (READ them; do not rebuild them).**
- `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~174/work/positions_daily_cache.parquet`: one row per account per positions partition day, columns `acc`, `date` (ISO string), `n_rows`, `v_all` (sum of `currentValue` over every row), `nan_rows`, `n_cash`, `n_inactive_nonzero`, `v_cash` (the sum over the cash lines), `v_active` (the sum over rows with `isActive` true).
- `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet`: the 980 accounts of 320 households (find the account column and the household column by reading its schema; state them in `basis_words`).
- `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~174/TIEOUT_GAPS.parquet`: round 109's result, columns `household_sha256`, `window`, `gap_bp`, `reason`, 320 rows per window. Use its `qtd` rows as the CONTROL; never edit it.
- The module `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_return_daily.py` (READ-ONLY; import it): `flows_of(frame, accounts)` turns Orion's `fact_transactions` frame into the external-flow series with the round-109 classification, `daily_returns(values, flows, trading_days)` and `window_return(daily, start, end)` are the method (the module's header and docstrings state it), `account_values` is the positions reading you do NOT need because the cache holds it.
- The reader `InflectionSilverReader` in `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py` (GET-only; it refuses any path outside `s3://opal-data-assets/orion/inflection/` and `.../eclipse/inflection/`). Read the NEWEST partition only of `.../orion/inflection/silver/fact_transactions/` and `.../fact_performance/` (each holds the full history; `fact_performance` columns are `client_id`, `date`, `factor`).
- The round-109 record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~174/TWR_TIEOUT_R109.json`: its `tie_out.basis_words` states the method you reproduce.

**The cell (`DB-i-1`).**
1. **Reproduce round 109's QTD figure for the basis `all` first.** For each household: sum its accounts' values (`v_all`) and external flows per day, run `daily_returns` on the sums over the performance axis (the sorted trading days in the cache; the as-of day is the cache's newest date), then `window_return` over the quarter-to-date window: the days after the base day 2026-09-30 through the as-of day. Orion's figure for the household is the index level end over base, minus one, from the newest `fact_performance` partition: `factor(as-of) / factor(2026-09-30) - 1`. `gap_bp` is the absolute difference between the derived and the Orion figure, in basis points; it is null with a plain-words `reason` when either side cannot be computed (a missing value or factor on a window day, a non-positive base). Your `all` gaps must equal round 109's `qtd` rows, household by household, to within 0.01 bp, and the same households must be null: that is the control. If they do not, the method is wrong; find the difference before you build the other two bases and say in `basis_words` what it was.
2. **Then the other two bases, by changing ONLY the value series:** `active_only` uses `v_active` for every account-day; `ex_cash` uses `v_all - v_cash`. The flows, the axis, the window and Orion's figure are identical to `all`. A household whose derived figure cannot be computed under a basis is null with its reason, never filled.
3. **The variant file (private).** Write `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~301/QTD_BASIS_VARIANTS.parquet` with exactly the columns `household_sha256`, `variant` (`all`, `active_only` or `ex_cash`), `gap_bp` (absolute, basis points, null when not comparable) and `reason` (words, required whenever `gap_bp` is null), ONE row per household per variant (320 households by 3 variants = 960 rows).
4. **The script.** Your read script is a tracked file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~301/tieout_basis_variants.py`. It imports the module and the reader, holds no S3 write call and names no firm other than Inflection. It is the only code this cell adds.
5. **Record** `BASIS_VARIANTS_R114.json` in your folder with exactly: `script` {`file` (repo-relative path), `sha256` (its bytes)}; `window` "qtd"; `variant_file` {`path`, `sha256`}; `variants` {for each of `all`, `active_only`, `ex_cash`: {`clients_compared`, `not_comparable`, `bins` {`lt_5bp`, `5_25bp`, `25_100bp`, `ge_100bp`} (absolute gap: under 5, 5 to under 25, 25 to under 100, 100 or more), `claim` "measured"}}; `moved_down_a_bin` {`active_only`, `ex_cash`: the count of households comparable under both that sit in a LOWER bin than under `all`}; `basis_words` (words: the account and household columns of the dim table, how the control matched, what each basis sums, whether the 2026-09-29 alien partition date is inside the window (it is not: the window opens after 2026-09-30), anything that surprised you; no figure); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer, the reader's `reads` count)}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no household or account id (the digest only), no run of 8 or more digits except in a `sha256` value or a `path` or `file` field.

<criterion id="DBI114-1-AC1" cell_refs="DB-i-1"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r114/p114_bin.py" . DBI114-1-AC1</invocation><expect>DBI114-1-AC1 PASS</expect></criterion>
`DBI114-1-AC1` -- the record is complete and carries no identifier; the script is a tracked file hashed as recorded, with no write call and no other firm's name; the variant file is a private parquet hashed as recorded with exactly the four columns and one row per household per variant, every null gap carrying a reason; the checker recounts each variant's compared, not-comparable and bin counts from the variant file and finds them equal to the record; the CONTROL holds: the `all` variant equals round 109's QTD gaps household by household (within 0.01 bp, the same households null) and its bins equal round 109's; `moved_down_a_bin` equals the checker's recount; nothing is written to AWS; no push or deploy. Base: FAIL (no record).

<expected_criteria>DBI114-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the module, the reader, the round-109 files, the contract and every issuer check.
- **Reads and writes.** Reads: repo files; the private files named above; S3 LIST and GET under `s3://opal-data-assets/orion/inflection/` ONLY through the reader. Writes: the repo files of the grant and your private folder. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Client data.** The cache, the variant file and every table above are client data: counts, hashes and words only in the repo, a row or your report; no return, value or flow is recorded.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the control will not match after an honest search for the difference, say so in a BLOCKING row with the measured number of differing households (a count) and stop: do not tune a basis until it matches.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W301-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~301/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-1.inflection-qtd-tie-out-under-three-value-bases.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 1, cell `DB-i-1`.
<owned_cells>DB-i-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI114-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~301/IRPT_DASHBD.TO-DB-i-1.inflection-qtd-tie-out-under-three-value-bases.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI114-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how the control matched (a count of differing households, expected 0); per basis the households compared and not comparable and the four bins (counts only); `moved_down_a_bin` per variant; the number of S3 reads; row ids. No account number, household or client id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and a private table; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of the Inflection-scoped Orion prefix through the round-108 adapter's grant-enforcing reader; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI114-1-AC1 FAILS at base (no record), and the checker was fed a synthetic good record (PASS) and a record with one household perturbed in the control variant (FAIL) before the cut.
</preflight>
