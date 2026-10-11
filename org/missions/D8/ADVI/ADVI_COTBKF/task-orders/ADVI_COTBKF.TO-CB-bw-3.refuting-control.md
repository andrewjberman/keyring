# TO ADVI_COTBKF.TO-CB-bw-3.refuting-control -- round 75 CB-bw-3: the refuting control: the validation rule, unchanged, run on the adjusted column of the 33 validated funds, expected refuted

<to_id>ADVI_COTBKF.TO-CB-bw-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~134</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bw-3` (`decompositions/ADVI_COTBKF_DECOMP.round75.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a CONTROL on a rule already written. You change no code and you do NOT change the rule. Nothing is fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_75_20261011.md` section 2 item 4 and section 3 item 3 ("0 refuted, and the refuting arm was never exercised. A validation
that has never said no has not been shown able to. One control before another fund is called validated: a series known to be
adjusted (one of the nineteen, read from its adjusted column) run through the same rule, expected REFUTED."); the round-74 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~128/VALIDATED_UNADJUSTED.json` and its `.csv` and `.md`: the rule AS WRITTEN (a date is compared when the cache has the row's own-date bar and the
previous bar; it matches when the custodian's reinvestment price equals, within 0.5 percent, the cached close on either day;
validated at 10 or more dates and 0.80 matching; refuted at 10 or more dates and 0.30 or fewer matching; else unreadable).

**Your item.**

1. **Reproduce the rule's own result first** on the unadjusted `Close`: 33 validated, 0 refuted, 237 unreadable over 270.
2. **The control:** the SAME rule, unchanged, with the cache's `Adj Close` column in place of `Close`, over the 33 validated funds
   (the nineteen left on the store, and the fourteen substituted). A series known to be adjusted should read `refuted`. Per fund:
   dates compared, dates matching, the reading. Counts: refuted, unreadable (between 0.30 and 0.80), validated.
3. **Say what it shows, whichever way it comes out.** If every fund is refuted, the arm works on this population. If some adjusted
   series read `unreadable` or `validated`, list them by ticker with their counts and say why from the data (an adjusted close
   equals the unadjusted one after the fund's last distribution in the window, so a fund's most recent dates always match): for
   each such fund, the share of its compared dates that fall after its last distribution, and the reading over the dates before it
   alone. Do NOT adjust the thresholds to make the control pass: report what a threshold would have to be, as a sensitivity.
4. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~134/REFUTING_CONTROL.json`, a `.csv` (columns: cusip, ticker, group, dates_compared, matching_close, matching_adj_close,
   reading_on_close, reading_on_adj_close; CUSIPs only in the column named exactly `cusip`) and a short `.md`. Top-level keys,
   exactly: `rule` (quoted from the round-74 record, with its numbers), `reproduced` (`{"validated", "refuted", "unreadable"}`),
   `control_funds` (33), `control_refuted`, `control_unreadable`, `control_validated`, `not_refuted` (a list, by ticker, with why),
   `arm_shown_able_to_refute` (true or false), `sensitivity`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB75bw3-AC1" cell_refs="CB-bw-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~134/REFUTING_CONTROL.json',encoding='utf-8'));r=d['reproduced'];print('REFUTING-CONTROL reproduced=%d/%d/%d control_funds=%d refuted=%d unreadable=%d validated=%d sum=%d not_refuted_listed=%d arm_shown_able_to_refute=%s'%(r['validated'],r['refuted'],r['unreadable'],d['control_funds'],d['control_refuted'],d['control_unreadable'],d['control_validated'],d['control_refuted']+d['control_unreadable']+d['control_validated'],len(d['not_refuted']),d['arm_shown_able_to_refute']))"</invocation><expect>REFUTING-CONTROL reproduced=33/0/237 control_funds=33</expect></criterion>
`CB75bw3-AC1` -- the rule's own result is reproduced, and the same rule run on the adjusted column gives each of the 33 funds one
reading (`sum` equals 33). The issuer reads how many were refuted and whether the arm is shown able to refute.

<expected_criteria>CB75bw3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry, and NOT the rule.** Everything is local; no network call.
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
  `ADVI_COTBKF-D2-W134-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round75.md</decomp_doc> (round 75), cell `CB-bw-3`.
<owned_cells>CB-bw-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB75bw3-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~134/ADVI_COTBKF.TO-CB-bw-3.refuting-control.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB75bw3-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the rule's own result as reproduced (33 / 0 / 237); the control over the 33 on the adjusted column: refuted, unreadable, validated; every fund not refuted, by ticker, with its counts and why; whether the arm is shown able to refute, said plainly; the sensitivity, marked as not the result; the `REFUTING-CONTROL` line; the account-id scan's DENOMINATOR line; a statement that the rule was not changed and nothing was fetched; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the rule is run as written, never tuned to pass; the rule's own result must be reproduced first; an adjusted series that is not refuted is listed with the reason read from the data, since an adjusted close equals the unadjusted one after a fund's last distribution; BLIND: a fund that paid nothing in the cache window, whose two columns are identical.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-75 analysis @cd481e59d2 (msg 5920), section 3 item 3; `3.0.0_SA_CVO` REMEDIATION_v45 @7dbb71c512.
