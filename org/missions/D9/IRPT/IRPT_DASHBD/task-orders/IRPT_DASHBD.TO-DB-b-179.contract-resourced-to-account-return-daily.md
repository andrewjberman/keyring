# TO IRPT_DASHBD.TO-DB-b-179 -- re-source the performance report contract: every window figure the account return table can derive (beginning value, ending value, net additions, net gain, and the account returns, for quarter to date, year to date, last 12 months and since inception) now reads from account_return_daily, version 0.2.0 with the 0.1.0 bytes in its lineage; the gap table regenerated

<to_id>IRPT_DASHBD.TO-DB-b-179</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~145</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>95</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7289 (ruling on the issuer's finding that gold `account_activity_daily` holds four trading days) | **Rows:** IRPT_DASHBD-D2-W141-S3 | **Decomp cell:** `DB-b-179` (decomposition section 97, round 95) | **outcome_ref:** FWD-21 | **depends_on:** DB-b-174 (drained @0c27245bc9).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-145` (branch `wk-IRPT_DASHBD-145`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~145/`.

**Why.** The performance report contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (version 0.1.0, 117 members, bytes sha256 `53fce40546882c90b634decb91ec5176a54ddf3c3b4622270bfc5cc35f66991b`) sources every window figure of the two value summaries from gold `account_activity_daily`, which holds four trading days today, so no window can open. The CTO's ruling: every window figure that `account_return_daily` can derive comes from it; what only activity holds (the contributions-versus-withdrawals split and income) stays on activity or ABSENT until activity is backfilled (that is IRPT_BCKEND's, queued). The contract names ONE source per figure.
Read `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (its columns: `market_value_eod` the whole-account value at end of day, `external_flow` the net external flow, capital-in positive, with the skipped-day rule, `income_received`, `total_return_daily`, `day_quality`, `history_scope` and the rest; its `partition`, `grain` and `address`; read it in full) and the activity contract's `window_identity_tolerance`, and the current contract's `document` layout.

**The cell (`DB-b-179`).** A document change, no product code.
1. **Edit the contract** (an existing file; keep its path, its eight sections, its `document` layout and EVERY member id and section unchanged). Set `contract_version` to `0.2.0` and add `lineage`: a list holding `{"contract_version": "0.1.0", "sha256": "53fce40546882c90b634decb91ec5176a54ddf3c3b4622270bfc5cc35f66991b", "reason": "<one line: window figures re-sourced to the account return table>"}`. Re-point these 36 members, and only these, to `source` = `{"contract": "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json", "field": "<a column that really occurs there>", "fold": "<how the figure is folded from the daily rows, in words>"}`:
   - for BOTH value summaries, `pvs.<w>.<row>` (household: the sum over the household's accounts) and `avs.<w>.<row>` (one account), for `<w>` in `qtd`, `ytd`, `last_12_months`, `since_inception` and `<row>` in `beginning_value` (`market_value_eod` on the window's opening anchor day, the last trading day before the window; since inception: the first day the account has a value, then its value), `ending_value` (`market_value_eod` on the as-of day), `net_additions` (the sum of `external_flow` over the window's trading days), `net_gain` (ending value minus beginning value minus net additions: say in the fold that this is a gain BEFORE advisory fees and that the baseline's net gain includes fees; keep the fee-basis member's words);
   - `avs.<w>.return_cumulative` for the same four windows (the account's cumulative return: the compounding of `total_return_daily` over the window's trading days, with the contract's own guard and `day_quality` rules named in the fold). The household's `pvs.<w>.return_cumulative` STAYS ABSENT (returns do not add across accounts).
   Say in every fold how an account with fewer days than the window is handled (the baseline's "not held for the entire period" note) and how a day with no value is handled (that account's term, and the household sum that contains it, is absent in words).
   Do NOT change `act.*` (the activity summary keeps its activity source or ABSENT), `hold.*`, `trgl.*`, `glr.*`, the benchmark rows or anything else. Nothing in the file may name a vendor or a custodian. Run the existing checker for the sections and members first: `python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . DB94-1-AC1` must still print PASS after your edit.
2. **Regenerate the gap table** `GAP_TABLE.json` in YOUR folder, with the keys of the previous one (`contract_sha256` of the contract's NEW bytes; `totals` {`members`, `sourced`, `absent`}; `by_section` for the eight sections; `vendor_free` true; `baseline_cells_required`; `fwd20_map_folded`; `sibling_contracts_read`; `reads` {`vendor_calls` 0, `s3_reads` 0, `s3_writes` 0, `secret_reads` 0}; `served_values_changed` false; the previous gap table is `deliverables/0.9.0_WK_IRPT_DASHBD~140/GAP_TABLE.json`, read it) plus `resourced_members` (36) and `identity_by_window_sketch` (one or two sentences: how net gain, beginning value, ending value and net additions tie for a window).
3. **Report** the counts before and after (sourced and ABSENT, by section) and which of the 36 members you consider weakest (a fold that rests on an assumption), in words.

<criterion id="DB94-6-AC1" cell_refs="DB-b-179"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . DB94-6-AC1</invocation><expect>DB94-6-AC1 PASS</expect></criterion>
`DB94-6-AC1` -- the contract is above 0.1.0 with the 0.1.0 bytes in its lineage; the 36 window members source from the account return table with a fold; the activity summary keeps its own source; the regenerated gap table is bound to the new bytes and equals its totals; no vendor or custodian is named; no S3 access; no run of 8 or more digits. (DB94-1-AC1 keeps passing: the same 117 members, the same eight sections.) Base: FAIL.

<expected_criteria>DB94-6-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the activity, return and every other sibling contract.
- **No S3, no vendor call, no secret read, no deploy, no push, no portal.** Repo files only.
- **No client data.** Nothing in the contract or the gap table names a client, a household or an account.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W145-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content. ASCII only. Commit with `.tools/safe-commit.sh` as your definition says; run its gates in the background and wait for them.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~145/
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-179.contract-resourced-to-account-return-daily.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 97 (round 95), cell `DB-b-179`.
<owned_cells>DB-b-179</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB94-6-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~145/IRPT_DASHBD.TO-DB-b-179.contract-resourced-to-account-return-daily.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB94-6-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; DB94-1-AC1's last line; the sourced and ABSENT counts before and after, by section; the weakest folds; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a contract document edit and a counts-only gap table; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS access.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (contract at 0.1.0, no lineage) and its structure is checked by 71 synthetic arms dry-run.
lane: the <paths> block IS the grant.
</preflight>
