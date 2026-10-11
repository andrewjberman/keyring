# TO ADVI_COTBKF.TO-CB-bl-3.flagged-days -- round 64 CB-bl-3: the 24 emptied-account days with a return above 1 percent, explained by class

<to_id>ADVI_COTBKF.TO-CB-bl-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~92</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>64</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bl-3` (`decompositions/ADVI_COTBKF_DECOMP.round64.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE: counts, shares, security identifiers (CUSIP, symbol), asset kinds, dates, file-and-line citations and reason codes only** in your record, report, commit messages and rows. Never an account id, never an account's position size, value, flow or return tied to an account. Aggregate before you print. A RATIO of two of an account's numbers (for example outflow divided by prior value) may be reported to two decimal
places; the numbers themselves may not.

**This is a MEASUREMENT. Read row ADVI_COTBKF-D2-S101 in the channel and `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_64_20261011.md` section 3 (row D2-S101) and section 4 item 3
first.**

**Why.** 1,757 minted account-days are MEASURED with no holdings row: every one has `market_value_eod` 0 (the day an account is
emptied). On 24 of them the absolute return is above 1%, and on 3 above 100%. Those are the cells of the table that could be WRONG
and not blank.

**Your item.**

1. Rebuild the set: the measured rows (`return_basis` `TWR`) of the 3,325 minted day files under
   `C:/dev/ajb_workspace/.scratch/advi_cotbkf/ard_cottonwood_r47/date=<D>/data.parquet` that have no row in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet` for
   that account and day. It must read 1,757, and 24 of them must have `abs(total_return_daily) > 0.01`. If not, that is the refusal
   clause.
2. For each of the 24: the day's external flow, the prior day's value, and the ratio of the outflow to the prior value. Then say
   WHICH disagrees and why, from the data, as a CLASS:
   - read the prior day's holdings rows (how many positions, how many unpriced, whether the prior day was itself measured);
   - read the transactions of that account on the day and the two days either side in the silver transactions cache
     (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/`): transaction types, whether an in-kind transfer or a position transfer left without an amount, whether a
     flow is dated a day off the holdings change;
   - read how the return form treats that day in `data/assets/scripts/silver/commonwealth_daily_returns.py` (lines 1 to 30 and the
     function that assigns reasons near line 227) and `commonwealth_flows.py`.
3. Name the classes. For each: how many of the 24, how many of the 3 above 100%, the mechanism in one sentence with file and line,
   and whether it is a defect of the FORM when the day-end value is zero, a defect of the DATA (a flow or a transfer the custodian
   file states differently), or a true return.
4. Count how many of the OTHER 1,733 emptied-account days fall in each class's mechanism but stayed under 1% (so the class is sized,
   not just its visible part).
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~92/FLAGGED_DAYS.json` and a short `.md` beside it. Top-level keys, exactly: `emptied_measured_days`, `flagged`,
   `flagged_above_100pct`, `classes` (a list of `{"class", "flagged", "above_100pct", "other_emptied_days_same_mechanism", "kind"
   (FORM | DATA | TRUE | UNEXPLAINED), "mechanism", "file", "line"}`), `unexplained`, `evidence`, `not_established`.

### ACCEPTANCE

<criterion id="CB64bl3-AC1" cell_refs="CB-bl-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~92/FLAGGED_DAYS.json',encoding='utf-8'));c=d['classes'];print('FLAGGED-DAYS-RECORD emptied_measured_days=%d flagged=%d above_100pct=%d classes=%d class_sum=%d unexplained=%d'%(d['emptied_measured_days'],d['flagged'],d['flagged_above_100pct'],len(c),sum(x['flagged'] for x in c),d['unexplained']))"</invocation><expect>FLAGGED-DAYS-RECORD emptied_measured_days=1757 flagged=24 above_100pct=3</expect></criterion>
`CB64bl3-AC1` -- the set is rebuilt to the measured counts and every flagged day sits in a class (`class_sum` equals 24, with
`UNEXPLAINED` a legal class).

<criterion id="CB64bl3-AC2" cell_refs="CB-bl-3" judgment="true"/>
`CB64bl3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each class's mechanism follows from the cited lines
and counts; FORM, DATA and TRUE are told apart on evidence; an unexplained day is called unexplained.

<expected_criteria>CB64bl3-AC1,CB64bl3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** You READ local data under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` (the base checkout; never write
  there) and write scratch under your own worktree `.scratch/` only (never committed).
- **No gate override** of any kind and no `--force`. If a gate refuses a commit, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`. A commonwealth script you run carries
  `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round64.md</decomp_doc> (round 64), cell `CB-bl-3`.
<owned_cells>CB-bl-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB64bl3-AC1, CB64bl3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~92/ADVI_COTBKF.TO-CB-bl-3.flagged-days.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB64bl3-AC1,CB64bl3-AC2` BEFORE the flip. Mechanical: CB64bl3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the `FLAGGED-DAYS-RECORD` line; each class with its counts, kind and mechanism; the size of each mechanism among the other 1,733 days; the unexplained count; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the set is rebuilt to the measured counts before any class is named; UNEXPLAINED is a legal class; each mechanism is sized among the unflagged days too; BLIND: a cause that lives in the custodian's raw file and not in the silver transactions.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-64 analysis @5cc2574c67 (msg 4579), section 4 item 3; `3.0.0_SA_CVO` REMEDIATION_v36 @877c95fb20.
