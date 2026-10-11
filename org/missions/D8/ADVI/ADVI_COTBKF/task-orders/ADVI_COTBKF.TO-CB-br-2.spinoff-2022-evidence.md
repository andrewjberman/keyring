# TO ADVI_COTBKF.TO-CB-br-2.spinoff-2022-evidence -- round 70 CB-br-2: the 2022 spin-off for one security: the evidence record the addendum will be written against

<to_id>ADVI_COTBKF.TO-CB-br-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~112</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-br-2` (`decompositions/ADVI_COTBKF_DECOMP.round70.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code. No vendor is asked.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_70_20261011.md` section 2 item 3 and section 3 item 2; rows ADVI_COTBKF-D2-S118, D2-W103-S1 and D2-W103-S2 in the channel;
the round-68 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~103/SPINOFF_CLAIMS.json` (its
`other_candidate_prints`, the entry for CUSIP 00206R102) and the round-69 scan
`.../0.9.0_WK_ADVI_COTBKF~108/CLOSE_VS_TRADE_SCAN.json` and `.csv` (the row for ticker T).

**The ruling you serve.** The CTO's rule of round 68: a factor is applied if and only if it reproduces the price the security traded
at before the event. For one event (CUSIP 00206R102, event date 2022-04-11, factor 1.324 in the split-history store) two records say
the served closes sit at 0.757 of the traded price until the event. The CTO will write a PRD addendum AGAINST your record. So the
record must stand on its own: every number in it re-derived by you from the data, none copied from the two earlier records.

**Your item.**

1. **The pairs.** From the silver transactions cache `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet`: every buy or sell row (`by`, `sl`)
   of that CUSIP with a non-zero quantity and amount; per trade date the quantity-weighted traded price `abs(Amount) / abs(Quantity)`.
   The custodian's row must be shown to be the custodian's: name the cache's source object (what silver table it was read from and
   which delivered file that table holds; `data/assets/scripts/silver/commonwealth_*.py` and the PRD's manifest rows say).
2. **The closes.** The served build's close for that CUSIP on each trade date: `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet`
   (this is the build at the served instant, where the store's entry for this event is absent).
3. **The table, one row per comparable date** (a security's price on a date is not client data): date, traded price, served close,
   ratio close / traded, close times 1.324, ratio of that to the traded price, trades on the date. ALL dates, before and after the
   event: the claim is that the ratio is about 0.757 before and about 1.00 after, so the after-event dates are the negative arm and
   must be in the table. Write it as `SPINOFF_2022_PAIRS.csv` in your deliverables folder.
4. **The counts:** dates before the event, and of them within 0.5 percent and within 2 percent of the traded price WITHOUT the factor
   and WITH it; the same for dates on or after the event (where the factor must NOT be applied: show what applying it would do);
   median and worst ratio of each. The dates the two earlier records could not compare (trades before the served table starts): how
   many, and why.
5. **Where the factor comes from:** the store's entry (read it by its version id at an instant AFTER it landed, 2026-10-10, with the
   version-aware reader `load_store_splits(s3, cusips, as_of)` in `data/assets/scripts/silver/commonwealth_daily_valuation.py`; a
   read-only get): its date and ratio exactly as stored, and the object's version id.
6. **What applying it would change in the served table:** the dates whose close moves (all dates before the event on which an account
   holds the security: count them from `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet`), the priced holding account-days, and
   how many of those are MEASURED account-days in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet`. Round 67 found 28 returns and 2
   blank reasons move for the four events together: say how many of yours are this event's, from your own counts.
7. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~112/SPINOFF_2022_EVIDENCE.json`. Top-level keys, exactly: `cusip`, `ticker`, `event_date`, `factor` (`{"value", "store_date",
   "version_id", "as_of"}`), `custodian_source`, `pairs` (`{"before_event", "on_or_after_event", "not_comparable"}`),
   `without_factor_before` and `with_factor_before` (each `{"within_half_percent", "within_two_percent", "median_ratio",
   "worst_ratio"}`), `without_factor_after`, `with_factor_after`, `reads` (`APPLY` | `DO_NOT_APPLY` | `UNDECIDED`, by the rule
   quoted above and nothing else), `reach` (`{"dates", "priced_holding_account_days", "measured_account_days"}`), `not_established`.

### ACCEPTANCE

<criterion id="CB70br2-AC1" cell_refs="CB-br-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~112/SPINOFF_2022_EVIDENCE.json',encoding='utf-8'));p=d['pairs'];a=d['without_factor_before'];b=d['with_factor_before'];c=d['without_factor_after'];print('SPINOFF-2022-EVIDENCE cusip=%s event=%s factor=%s pairs_before=%d pairs_after=%d without_before_2pct=%d with_before_2pct=%d without_after_2pct=%d reads=%s measured_account_days=%d'%(d['cusip'],d['event_date'],d['factor']['value'],p['before_event'],p['on_or_after_event'],a['within_two_percent'],b['within_two_percent'],c['within_two_percent'],d['reads'],d['reach']['measured_account_days']))"</invocation><expect>SPINOFF-2022-EVIDENCE cusip=00206R102 event=2022-04-11</expect></criterion>
`CB70br2-AC1` -- the record names the event, carries the pair counts on both sides of it and the reading the rule gives. The CTO
reads the counts; the addendum is written against them.

<criterion id="CB70br2-AC2" cell_refs="CB-br-2" judgment="true"/>
`CB70br2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: every number is this cell's own derivation; the
after-event dates are in the table as the negative arm; the traded price is shown to come from the custodian's delivered rows; the
reading follows from the rule as worded and from nothing else; the reach is counted on the served table.

<expected_criteria>CB70br2-AC1,CB70br2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** One read-only versioned get of the split store's entry for this CUSIP
  is allowed; everything else is local.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write or delete.** No push. No `--refresh`. No vendor call.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids and reason codes only. A build log line carrying `read_account=` is never echoed.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W112-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round70.md</decomp_doc> (round 70), cell `CB-br-2`.
<owned_cells>CB-br-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB70br2-AC1, CB70br2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~112/ADVI_COTBKF.TO-CB-br-2.spinoff-2022-evidence.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB70br2-AC1,CB70br2-AC2` BEFORE the flip. Mechanical: CB70br2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the custodian source of the trade rows; the pair counts before and after the event and the dates that could not be compared; the four comparisons (without and with the factor, before and after) with counts within tolerance, medians and worst ratios; the store entry's date, ratio and version id; the reading the rule gives; the reach; the `SPINOFF-2022-EVIDENCE` line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement.
comp-iam: DECLARED-NOT-APPLICABLE one read-only versioned get on a store this build already reads; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- every number is re-derived here, none copied from the two earlier records; the after-event dates are the negative arm and must be in the table; the reading is bound to the rule as worded; BLIND: the traded price includes whatever the custodian put in the amount (fees, on a few percent of single dates in earlier controls).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-70 analysis @991f749df1 (msg 5340), section 3 item 2; PRD ADDENDUM v0.7 @72d624cd26; `3.0.0_SA_CVO` REMEDIATION_v40 @90e1a7cbda.
