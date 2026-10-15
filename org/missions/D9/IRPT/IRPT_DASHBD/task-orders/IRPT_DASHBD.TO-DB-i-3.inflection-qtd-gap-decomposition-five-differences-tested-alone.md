# TO IRPT_DASHBD.TO-DB-i-3 -- the Inflection QTD GAP DECOMPOSITION on a sample of about 12 households across the gap bins: five named differences between the Opal derivation and Orion's client factor (gross against net of fees, trade against settlement date, flow timing inside a day, income accrual, the cash sweep) each tested ALONE against the round-109 baseline, and the explained share of each household's gap per variant; a private table, counts, bp and shares only in the repo; nothing written to AWS

<to_id>IRPT_DASHBD.TO-DB-i-3</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~303</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>115</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_115_20261015.md` section 3 cell 1 (msg 7956) | **Rows:** IRPT_DASHBD-D2-W303-S<k> | **Decomp cell:** `DB-i-3` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 2) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-303`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~303/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes, bp and shares only in the repo, a row or your report; an account number, a household or client id, a name or a figure (a return, a value, a flow) is never recorded; a household is named only by the sha256 (hex, utf-8) of its id. Your private folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~303/` (create it).

**Why.** Opal derives Inflection's account returns from Orion positions and transactions, and aggregated per household the quarter-to-date (QTD) result sits 25 bp or more from Orion's own client return for 184 of 287 comparable households (round 114, record `deliverables/0.9.0_WK_IRPT_DASHBD~301/BASIS_VARIANTS_R114.json`; 9 households sit at 100 bp or more). Excluding the cash lines did not close it. The CTO will not set a tolerance, or let the account pages show derived figures, until the gap is explained. This cell tests five named differences, ONE AT A TIME, on a small sample, and reports how much of each household's gap each difference explains. It rules nothing.

**The sample (a rule, so the checker can recompute it).** From round 114's private variant file `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~301/QTD_BASIS_VARIANTS.parquet` (columns `household_sha256`, `variant`, `gap_bp`, `reason`), take the rows with `variant` = `all` and a non-null `gap_bp` (the absolute gap in bp). The sample is EVERY household with `gap_bp` of 100 or more, plus, for EACH of the other three bins (under 5; 5 to under 25; 25 to under 100), the one household whose `household_sha256` sorts lowest (plain string order). That is 12 households.

**The inputs (all existing and private or granted; READ them, do not rebuild them).**
- Your template is the tracked script `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~301/tieout_basis_variants.py` (READ it; copy what you need into your own script; do not edit it). It reproduces round 109's QTD gap for the basis `all`: the cached account values, the account dimension, the household sums, `daily_returns` / `window_return` from the module, Orion's figure as `factor(as-of) / factor(2026-09-30) - 1`, and the control against round 109. YOUR BASELINE is exactly that computation (`base`), but you keep the SIGNED gap: `signed_gap_bp = (derived - orion) * 10000`.
- The private cache `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~174/work/positions_daily_cache.parquet` (columns `acc`, `date`, `n_rows`, `v_all`, `nan_rows`, `n_cash`, `n_inactive_nonzero`, `v_cash`, `v_active`), the account dimension `.../0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet`, and round 109's `.../0.9.0_WK_IRPT_DASHBD~174/TIEOUT_GAPS.parquet` (control only).
- The module `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_return_daily.py` (READ-ONLY; import it). Its `TYPE_CLASS` places every transaction type: `EXTERNAL_IN` / `EXTERNAL_OUT` (flows), `INTERNAL`, `INCOME` (Dividend to Cash, Interest Paid in Cash, Interest Paid), `IN_VALUE` (Management Fee, Trading Expense, ADR Fee, Administrative Fee, Administrative Fee Adjustment, Wire Fee, Fee Credit, the tax types, the gains to cash) and `CORPORATE_ACTION`. `flows_of(frame, accounts)` builds the external flows by `transDate`.
- The reader `InflectionSilverReader` (`.../inflection_account_dim.py`, GET-only, refuses any path outside `s3://opal-data-assets/orion/inflection/` and `.../eclipse/inflection/`). Read the NEWEST partition only of `.../orion/inflection/silver/fact_transactions/` and `.../fact_performance/`. The transactions frame columns include `accountId`, `transactionDescription`, `transAmount`, `transDate`, `status`; READ its full column list (state it in `basis_words`) to find any settlement-date, ex-date, record-date, pay-date or accrual column the variants below need.

**The cell (`DB-i-3`).** For each sampled household compute the QTD `signed_gap_bp` under these NINE variants, each differing from `base` in exactly ONE way (the flows, axis, window, household sums and Orion's figure are `base`'s unless the variant says otherwise):
1. `base`: round 114's `all` method (value `v_all`, flows by `transDate` as `flows_of` builds them, end-of-day flow `r = (V_t - F_t) / V_(t-1) - 1`, fees and taxes left inside V as booked, income counted on receipt through the cash line).
2. `identity`: recompute `base` through a second code path with NO change. It must equal `base` to within 0.01 bp for every household (the difference control: a variant that changes nothing must change nothing).
3. `gross_fees` (difference: gross against net of fees): treat each fee transaction (types `Management Fee`, `Trading Expense`, `ADR Fee`, `Administrative Fee`, `Administrative Fee Adjustment`, `Wire Fee`) as an external OUTFLOW of its absolute amount on its `transDate` (so the fee no longer lowers the return), and `Fee Credit` as an external INFLOW of its absolute amount. Taxes stay in V.
4. `settle_timing` (trade against settlement date): the external flows dated by the transaction's SETTLEMENT date instead of `transDate`, if the frame carries a settlement-date column. If it carries none, the status is NOT_TESTABLE and every household's gap for this variant is null with the reason "the transactions frame carries no settlement date".
5. `flow_start_of_day` (how a flow inside a day is treated): the flow assumed to arrive at the START of the day, `r_t = V_t / (V_(t-1) + F_t) - 1`.
6. `flow_midday` (same difference, second form): the flow assumed at mid-day, `r_t = (V_t - F_t) / (V_(t-1) + 0.5 * F_t) - 1`.
7. `income_accrual` (income accrual): income counted when it ACCRUES rather than when it is received, using the frame's ex-date, record-date or pay-date column if one exists (the income types are the `INCOME` class). If no such date column exists the status is NOT_TESTABLE (null gaps, reason in words); never invent an accrual date.
8. `ex_cash_value` (the cash sweep, first form): the value is `v_all - v_cash` (cash lines out of V), flows unchanged.
9. `ex_cash_no_flows` (the cash sweep, second form): the value is `v_all - v_cash` AND the external flows and income are left out entirely (they sit in cash until invested), i.e. a return on the invested securities only.

A household whose gap cannot be computed under a variant is null with a plain-words `reason`, never filled. A variant is `TESTED` if at least one sampled household has a gap under it, else `NOT_TESTABLE`.

**The explained share.** For a TESTED variant `v` and household `h`: `share = (base_gap - v_gap) / base_gap` using the SIGNED gaps (`1.0` means the variant closes the gap; `0` leaves it; a negative share means it widens it; a share above 1 overshoots). Null when either gap is null or `|base_gap|` is under 0.01 bp. Do NOT clip. The five differences and their variants: `gross_vs_net_of_fees` = [`gross_fees`]; `trade_vs_settlement_date` = [`settle_timing`]; `flow_timing_in_a_day` = [`flow_start_of_day`, `flow_midday`]; `income_accrual` = [`income_accrual`]; `cash_sweep` = [`ex_cash_value`, `ex_cash_no_flows`].

**The files.**
- The script: tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~303/gap_decomposition.py`. It imports the module and the reader, holds no S3 write call and names no firm other than Inflection. It is the only code this cell adds.
- The private table `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~303/GAP_DECOMPOSITION.parquet` with exactly the columns `household_sha256`, `variant`, `signed_gap_bp` (basis points, signed, null when not computable) and `reason` (words, required whenever the gap is null), ONE row per sampled household per variant (12 households by 9 variants = 108 rows).
- The record `GAP_DECOMPOSITION_R115.json` in your folder with exactly: `script` {`file` (repo-relative), `sha256`}; `window` "qtd"; `sample_size` (integer); `sample_households_sha256` (the sorted list of the sampled households' digests); `variant_file` {`path`, `sha256`}; `differences` (the map above, exactly); `variants` {for each of the SEVEN tested variants (not `base`, not `identity`): {`status` "TESTED" or "NOT_TESTABLE", `claim` ("measured" for a computed gap, "absent" for a NOT_TESTABLE variant), `words` (one or two sentences: what changed, and for NOT_TESTABLE why)}}; `explained_share` {for each of the seven tested variants: a map from each sampled household digest to its share (a number, or null)}; `households_with_a_single_difference_explaining_half` (the count of sampled households for which the largest share over the seven variants is 0.5 or more); `basis_words` (words: the transactions frame's column list, how the control and identity matched, which variants were NOT_TESTABLE and why, which differences explain the most and the least in words; no client value); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer, the reader's `reads` count)}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, bp, shares, paths, hashes and words only: no household or account id (the digest only), no run of 8 or more digits except in a `sha256` value or a `path`, `file` or `sample_households_sha256` field.

<criterion id="DBI115-1-AC1" cell_refs="DB-i-3"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r115/p115_gap.py" . DBI115-1-AC1</invocation><expect>DBI115-1-AC1 PASS</expect></criterion>
`DBI115-1-AC1` -- the record is complete and carries no identifier; the script is a tracked file hashed as recorded, with no write call and no other firm's name; the sample equals the checker's recompute from round 114's private variant file (every household at 100 bp or more plus the lowest-sha household of each other bin); the private table has exactly the four columns and one row per sampled household per variant, every null gap carrying a reason; the BASE absolute gap equals round 114's `all` gap for every sampled household (within 0.01 bp) and the IDENTITY variant equals BASE (within 0.01 bp); the differences map is exactly the five named; each tested variant's status agrees with its gaps (TESTED has at least one gap, NOT_TESTABLE has none); every explained share equals the checker's recompute from the signed gaps (null exactly where it is null) and the count of households with a single difference explaining half equals its recount; nothing is written to AWS; no push or deploy. Base: FAIL (no record).

<expected_criteria>DBI115-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the module, the reader, the template script, round 109 and 114's files, the contract and every issuer check.
- **Reads and writes.** Reads: repo files; the private files named above; S3 LIST and GET under `s3://opal-data-assets/orion/inflection/` ONLY through the reader. Writes: the repo files of the grant and your private folder. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Client data.** The cache, the transactions frame, the private table and every table above are client data: counts, hashes, bp and shares only in the repo, a row or your report; no return, value or flow is recorded.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If `base` will not match round 114's `all` gap for a sampled household after an honest search, say so in a BLOCKING row with the count of differing households and stop; if `identity` differs from `base`, the second code path is wrong: find the difference. Never tune a variant until it explains a gap, and never fill a null.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W303-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~303/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-3.inflection-qtd-gap-decomposition-five-differences-tested-alone.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 2, cell `DB-i-3`.
<owned_cells>DB-i-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI115-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~303/IRPT_DASHBD.TO-DB-i-3.inflection-qtd-gap-decomposition-five-differences-tested-alone.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI115-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how `base` and `identity` matched (counts of differing households, expected 0 and 0); the sample size and how many sit in each bin; per variant its status and, for TESTED ones, the count of sampled households it moves closer to Orion (share above 0) and the median share (a number, no household); `households_with_a_single_difference_explaining_half`; the transactions frame's column list; the number of S3 reads; row ids. No account number, household or client id, name or figure of a client.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and a private table; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of the Inflection-scoped Orion prefix through the round-108 adapter's grant-enforcing reader; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI115-1-AC1 FAILS at base (no record), and the checker was fed a synthetic good record (PASS) and one with the identity variant perturbed for one household (FAIL) before the cut.
</preflight>
