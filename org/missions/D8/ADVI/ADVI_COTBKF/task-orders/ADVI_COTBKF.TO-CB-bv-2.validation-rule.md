# TO ADVI_COTBKF.TO-CB-bv-2.validation-rule -- round 74 CB-bv-2: a fund series is validated unadjusted on the custodian's price, the row's own date or the trading day before: the rule written first, three counts over all 270

<to_id>ADVI_COTBKF.TO-CB-bv-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~128</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>74</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bv-2` (`decompositions/ADVI_COTBKF_DECOMP.round74.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code. Nothing is fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_74_20261011.md` section 2 item 2 and section 3 item 2; the round-73 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~123/THREE_DATE_READ.json` with its `.csv` (101 funds with both a
reinvestment row and a cached close; 42 validated under that round's rule, which took a fund's BEST single date).

**The ruling.** "The date convention belongs to the VALIDATION, not to the price. The price a fund is valued at on a day is its
unadjusted close for THAT day, whatever day the custodian dates a reinvestment." And the rule to write: "a fund series is VALIDATED
UNADJUSTED when its cached close matches the custodian's reinvestment price, on the row's own date or the trading day before, on a
stated share of its dates, with a stated minimum of dates. The count of validated, refuted and unreadable funds is printed with the
denominator."

**Your item.**

1. **THE RULE FIRST.** Before any count, write to a file in your scratch (with a clock timestamp) and copy into the record: equal
   (within 0.5 percent); a date MATCHES when the custodian's price equals the cached unadjusted close on the row's own date OR on
   the trading day before; `validated` = at least N dates compared and at least a share S of them matching (state N and S);
   `refuted` = at least N dates compared and at most a share R matching (state R: positive evidence that the cache is NOT the price
   the fund traded at); `unreadable` = everything else, with a reason code (no cached close; no reinvestment row; fewer than N dates
   compared; between R and S). State why N, S and R are what they are without reference to how many funds each choice validates.
2. **Run it over all 270 fund series** and print the three counts with the denominator (they sum to 270), and the reason codes of
   the unreadable. By group: the 197 left on the store, the 73 substituted, the nine.
3. **Against round 73**, fund by fund: its 42 validated under the best-single-date rule against yours. Every fund that changes
   reading, by ticker, with its counts.
4. **What the either-date rule could wrongly accept:** on how many compared dates do BOTH days match (so the test cannot tell), and
   on how many does the ADJUSTED close also match within 0.5 percent on either day (so a match is not evidence of being unadjusted)?
   Per validated fund, the count of dates on which the unadjusted close matches and the adjusted close does NOT: a fund validated on
   dates where the two closes are indistinguishable is not shown unadjusted, and is listed.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~128/VALIDATED_UNADJUSTED.json`, a `.csv` of all 270 (columns: cusip, ticker, group, dates_compared, dates_matching,
   dates_distinguishing, reading, reason, round_73_validated; CUSIPs only in the column named exactly `cusip`) and a short `.md`.
   Top-level keys, exactly: `rule` (`{"text", "written_at", "minimum_dates", "share_validated", "share_refuted"}`), `fund_series`
   (270), `validated`, `refuted`, `unreadable`, `unreadable_reasons`, `by_group`, `against_round_73` (`{"changes": [...]}`),
   `indistinguishable` (`{"dates_both_days_match", "dates_adjusted_also_matches", "validated_funds_not_distinguished": [...]}`),
   `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB74bv2-AC1" cell_refs="CB-bv-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~128/VALIDATED_UNADJUSTED.json',encoding='utf-8'));r=d['rule'];i=d['indistinguishable'];print('VALIDATION-RULE rule_written=%s minimum_dates=%s share_validated=%s share_refuted=%s fund_series=%d validated=%d refuted=%d unreadable=%d sum=%d changes_from_round_73=%d validated_not_distinguished=%d'%(bool(r['written_at']),r['minimum_dates'],r['share_validated'],r['share_refuted'],d['fund_series'],d['validated'],d['refuted'],d['unreadable'],d['validated']+d['refuted']+d['unreadable'],len(d['against_round_73']['changes']),len(i['validated_funds_not_distinguished'])))"</invocation><expect>VALIDATION-RULE rule_written=True</expect></criterion>
`CB74bv2-AC1` -- the rule was written first with its three numbers; every fund series carries one reading (`sum` equals 270); the
issuer reads the counts and how many validated funds the adjusted close cannot be told from.

<criterion id="CB74bv2-AC2" cell_refs="CB-bv-2" judgment="true"/>
`CB74bv2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the rule precedes the run and its numbers are not
chosen by their yield; `refuted` needs positive evidence; a fund validated only on dates where the adjusted close also matches is
listed and not counted as shown unadjusted; nothing was fetched.

<expected_criteria>CB74bv2-AC1,CB74bv2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call.
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
  `ADVI_COTBKF-D2-W128-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round74.md</decomp_doc> (round 74), cell `CB-bv-2`.
<owned_cells>CB-bv-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB74bv2-AC1, CB74bv2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~128/ADVI_COTBKF.TO-CB-bv-2.validation-rule.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB74bv2-AC1,CB74bv2-AC2` BEFORE the flip. Mechanical: CB74bv2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the rule as written before the run, with its timestamp and its three numbers and why each; validated, refuted and unreadable over 270 with the reason codes; by group; every fund whose reading changes from round 73, by ticker; the dates on which both days match and on which the adjusted close also matches; the validated funds not distinguished, by ticker; the headline; the `VALIDATION-RULE` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the rule's numbers are stated before the run and not chosen by their yield; an either-date match is wider than a one-date match, so the cell counts the dates where the adjusted close matches too and lists any fund validated only on such dates; refuted needs positive evidence; BLIND: a fund that paid nothing in the cache window has identical closes and cannot be shown unadjusted by this test.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-74 analysis @42390144c0 (msg 5758), section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v44 @edbfc928ca.
