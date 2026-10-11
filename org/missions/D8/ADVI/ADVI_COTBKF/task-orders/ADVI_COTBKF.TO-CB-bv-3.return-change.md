# TO ADVI_COTBKF.TO-CB-bv-3.return-change -- round 74 CB-bv-3: the first return number: for the validated funds, the account-days whose daily return changes on the unadjusted close, in three bands; built on a copy

<to_id>ADVI_COTBKF.TO-CB-bv-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~129</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>74</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bv-3` (`decompositions/ADVI_COTBKF_DECOMP.round74.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bv-2

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT built on a COPY. Nothing is served, applied or written to any bucket. You change no product code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_74_20261011.md` sections 1, 2 (items 2 and 3) and 3 item 3; this round's record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~128/VALIDATED_UNADJUSTED.json` and its `.csv` (the funds VALIDATED
UNADJUSTED: the only funds this cell touches; if the record is absent, that is the refusal clause); how the served table was
reproduced at its pin: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~104/R28_VS_R29_AT_PIN.json` and `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json`
(the split store pinned at 2026-10-09T11:52:52Z, 32 partitions; the chain `commonwealth_daily_valuation.py` then
`commonwealth_sweep_regrade.py` then `commonwealth_fwd3_serve.py --build`, with `--split-store-as-of` and `--yahoo-cache`, under the
SERVED rule version `method_r28`); the as-traded basis in `data/assets/scripts/silver/commonwealth_daily_valuation.py`
(`as_traded_store`, the basis-census file it reads, the classes it substitutes).

**The ruling.** "The three reaches are not added, compared or quoted as a size. The next number shown is a return number": "for the
validated funds only, the account-days whose daily return changes when the validated unadjusted close replaces the price now used, by
size of change (under 1 basis point, 1 to 10, over 10), counts only. Built on a copy; nothing served."

**Your item.**

1. **The baseline reproduces the served table first.** Build the chain locally at the served pin under `method_r28`, into your own
   scratch, and show its daily returns equal the served copy (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet`): rows, measured rows,
   and the count of account-days whose return differs (expect 0 beyond a stated floating tolerance). If the baseline does not
   reproduce, STOP: that is the refusal clause, and nothing after it means anything.
2. **The variant changes ONE thing:** for the validated funds, and for no other security, the price used is the cached unadjusted
   close for that day. Do it WITHOUT editing product code: the as-traded basis already substitutes the cached close for tickers its
   census file classes as adjusted, so the variant is the same chain run against a COPY of that census file, in your scratch, in
   which only the validated funds' class is changed. Say exactly which rows of the copy changed and diff the copy against the
   original. If the chain cannot be pointed at a copy without a code change, STOP and say which constant binds it: that is the
   refusal clause, and a row.
3. **Confirm the variant moved only what it should:** the securities whose close differs between baseline and variant are exactly
   the validated funds (count; any other is listed); on those, the days re-derived or dropped by the basis's own rules (it drops
   days it cannot bracket), counted.
4. **The return number.** Over account-days measured in BOTH builds: how many returns change, by size of the absolute change: under
   1 basis point, 1 to 10, over 10 (a basis point is 0.0001 of return; state the floor below which a difference is floating-point
   residue and is not counted as a change). The largest change, as a number of basis points with its date and no account. Also:
   account-days measured in one build and blank in the other, each way, with the blank reason counted; account-months and
   account-years whose grade changes.
5. **Where the changes sit:** by fund (ticker, account-days changed), by year, and on or off a distribution date of the fund.
   Counts only. No account id, no account's return, value or flow.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json` and a short `.md`; a `.csv` by fund (columns: cusip, ticker, account_days_changed, under_1bp, bp_1_to_10,
   over_10bp; CUSIPs only in the column named exactly `cusip`). Top-level keys, exactly: `pin`, `baseline` (`{"reproduces": true|false,
   "rows", "measured", "differing"}`), `variant` (`{"census_rows_changed", "securities_moved", "other_securities_moved"}`),
   `validated_funds`, `account_days_compared`, `changed` (`{"total", "under_1bp", "bp_1_to_10", "over_10bp", "residue_floor"}`),
   `measured_to_blank`, `blank_to_measured`, `grades_changed`, `largest_change_bp`, `by_year`, `on_distribution_date`, `headline`,
   `not_established`.

### ACCEPTANCE

<criterion id="CB74bv3-AC1" cell_refs="CB-bv-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json',encoding='utf-8'));b=d['baseline'];v=d['variant'];c=d['changed'];print('RETURN-CHANGE baseline_reproduces=%s baseline_differing=%d validated_funds=%d securities_moved=%d other_securities_moved=%d account_days_compared=%d changed=%d under_1bp=%d bp_1_to_10=%d over_10bp=%d band_sum=%d measured_to_blank=%d blank_to_measured=%d'%(b['reproduces'],b['differing'],d['validated_funds'],v['securities_moved'],v['other_securities_moved'],d['account_days_compared'],c['total'],c['under_1bp'],c['bp_1_to_10'],c['over_10bp'],c['under_1bp']+c['bp_1_to_10']+c['over_10bp'],d['measured_to_blank'],d['blank_to_measured']))"</invocation><expect>RETURN-CHANGE baseline_reproduces=True baseline_differing=0</expect></criterion>
`CB74bv3-AC1` -- the baseline reproduces the served returns exactly, the variant moved the validated funds, and the changed
account-days are counted in three bands (`band_sum` equals `changed`). The issuer reads `other_securities_moved`.

<criterion id="CB74bv3-AC2" cell_refs="CB-bv-3" judgment="true"/>
`CB74bv3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the baseline is shown equal to the served table before
any variant number is read; the variant changes the validated funds' price and nothing else, by a copy and not a code edit; a
difference below the stated floor is not counted as a change; the number is stated as counts in bands for the validated funds only
and is not offered as the size of the whole defect; nothing was served.

<expected_criteria>CB74bv3-AC1,CB74bv3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no product code, test, config, manifest or registry.** The variant is a copied input file in your scratch.
- **AWS: READS ONLY**, and only the reads the valuation chain itself makes at the pin (the split store's versions; the price stores).
  No S3 write, no delete, no `--apply`, no `--remint`, no serve. Both builds write only under your scratch.
- No vendor call: the vendor cache is read as it sits on disk (`--yahoo-cache`), never refreshed.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W129-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round74.md</decomp_doc> (round 74), cell `CB-bv-3`.
<owned_cells>CB-bv-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB74bv3-AC1, CB74bv3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/ADVI_COTBKF.TO-CB-bv-3.return-change.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB74bv3-AC1,CB74bv3-AC2` BEFORE the flip. Mechanical: CB74bv3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the baseline against the served returns (rows, measured, differing); how the variant was made without a code edit and the diff of the copied census file; the securities moved and any other; the account-days compared and changed, in the three bands, with the residue floor; measured-to-blank and blank-to-measured with reasons; grades changed; the largest change in basis points; by fund, by year, on a distribution date; the headline; the `RETURN-CHANGE` line; a statement that nothing was served or written to a bucket; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE two local builds in a worktree scratch; nothing is served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: the cell makes only the read calls the valuation chain already makes at the pin, under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the baseline must equal the served returns exactly before any variant number is read, and the check's expected line says so; the variant is a copied input, never a code edit, and the cell stops if the chain cannot take a copy; the securities moved must be the validated funds and no other; a floating-point floor is stated; the number is for the validated funds only; BLIND: the basis's own re-derivation rules also act on a newly substituted fund, so a changed return is the price and those rules together.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-74 analysis @42390144c0 (msg 5758), section 3 item 3; `3.0.0_SA_CVO` REMEDIATION_v44 @edbfc928ca.
