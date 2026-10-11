# TO ADVI_COTBKF.TO-CB-c-4 -- round 3 CB-c-4: FWD-9 -- each pre-2018 Commonwealth account linked to the account that replaced it, by matched in-kind moves, or unlinked with the reason

<to_id>ADVI_COTBKF.TO-CB-c-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~11</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-c-4` (`decompositions/ADVI_COTBKF_DECOMP.round3.md`) | **outcome_ref:** FWD-9 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-c-4`, FWD-9: "where a client's account was replaced by a new one inside Commonwealth, an analyst reads the client's history as one line
from the oldest account to the newest, and sees which account each row came from; a link that cannot be shown is listed with its reason,
never guessed." This cell builds the LINKS (old account -> new account, with evidence). You prove it on the real table into a LOCAL
directory. You write NOTHING to S3: `--apply` is the issuer's act.

**The data, measured.** The silver transactions table `s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/date=2026-06-23/`
(read-only, default profile; parquet, `trade_year=<YYYY>/`): 1,416,497 rows, 1,533 accounts; columns `Advisor_ID`, `Account_Number`,
`Transaction_Type`, `Transaction_Description`, `Cusip`, `Symbol`, `Quantity`, `Amount`, `Trade_Date`, `source_line`, `source_record`, and more.
- **459 accounts** have their last trade before 2018-01-01 (407 of them started before 2016): the OLD accounts. Every one of the 311
  accounts trading in 2013 ends by 2017-12-29; the longest single-account history starts 2016-01. Old numbers are 11 digits (`acct#c9405219`);
  the 2016+ long-lived ones alphanumeric (`acct#0e4ff3a3`).
- The move shows in the types: `li` "Contribution to Asset" rows 2015 1,736 -> 2016 14,216 -> 2017 2,939; `trfi` "Position Transfer In"
  (and `TRFIR`, `trci`, `TRCISU`) and `trfo` "Position Transfer Out" (and `trco`) first appear in 2016.

**Link rule (exact, evidence printed):** an old account A links to a newer account B when A's holdings at its end (rebuilt from A's own
transactions up to its last trade) are moved in kind into B: B shows `li` / transfer-in rows on the same CUSIPs with quantities equal within
0.001, dated within 10 trading days of A's transfer-out rows or of A's last trade, covering at least 80% of A's end positions by count, with no
second candidate B' meeting the same bar (that case is `AMBIGUOUS`, both listed, never linked). Print per link: the matched CUSIPs, quantities,
dates and the score. Same `Advisor_ID` on both sides is evidence, not a requirement. Every OLD account gets exactly one row: `LINKED`
(new account, score, evidence) or `NOT_LINKED` (reason: "no in-kind receiver", "below threshold <score>", "ambiguous", "closed to cash").
A chain (A -> B -> C) is followed and printed as the client's line.

**Build `data/assets/scripts/silver/commonwealth_account_links.py`:** CLI `--out <local dir>`, `--apply` (writes at
`address('commonwealth', <scope>, 'silver', 'account_links', 'date=2026-06-23')`; unit-tested on a stub, never run by you); the scope through
`opal_naming.lookup`; device-free. Writes `account_links.parquet` and a `.csv`. LAST line exactly:
`ACCOUNT-LINKS old_accounts=<n> every_old_account_listed=<True|False> linked=<l> not_linked=<u> ambiguous=<a> chains=<c>`.

Tests `data/assets/scripts/silver/tests/test_commonwealth_account_links.py` (fixtures, no AWS): holdings rebuilt from buys/sells/transfers;
a clean in-kind move links; a partial move below the bar does not; two receivers give AMBIGUOUS; a chain of three accounts prints as one line;
every old account appears exactly once.

### ACCEPTANCE

<criterion id="CB3c4-AC1" cell_refs="CB-c-4"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_account_links.py</invocation><expect>passed</expect></criterion>
`CB3c4-AC1` -- the link rule on fixtures, including the ambiguity and below-threshold controls.

<criterion id="CB3c4-AC2" cell_refs="CB-c-4"><invocation>python data/assets/scripts/silver/commonwealth_account_links.py --out .scratch/advi_cotbkf/account_links</invocation><expect>ACCOUNT-LINKS old_accounts=459 every_old_account_listed=True</expect></criterion>
`CB3c4-AC2` -- the real table: all 459 old accounts listed, each linked with evidence or not linked with a reason.

<criterion id="CB3c4-AC3" cell_refs="CB-c-4" judgment="true"/>
`CB3c4-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: one client read as one line across an account change (FWD-9's DONE WHEN) is right
on its printed evidence, and a sample of LINKED rows holds.

<expected_criteria>CB3c4-AC1,CB3c4-AC2,CB3c4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Local output and caches under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`;** S3 READS only of the table above; never `opal-data-bd` or `opal-data-inf`.
- **Never guess a link.**
- **Within 120 seconds** for CB3c4-AC2 (column projection; cache under `.scratch/` and say so).
- **Rule 13:** a DS-lane script; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W11-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_account_links.py
data/assets/scripts/silver/tests/test_commonwealth_account_links.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round3.md</decomp_doc> (round 3), cell `CB-c-4`.
<owned_cells>CB-c-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB3c4-AC1, CB3c4-AC2, CB3c4-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS or
FAIL). Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~11/ADVI_COTBKF.TO-CB-c-4.account-links.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB3c4-AC1,CB3c4-AC2,CB3c4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `ACCOUNT-LINKS` line, three LINKED rows with their evidence, one chain printed as a client line, the NOT_LINKED reasons with
counts, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time builder.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads this project's silver under the laptop profile.
comp-adversary: RUN -- no guessed link (ambiguity listed, judgment criterion for the CVO); cross-firm (this project's table only); BLIND: links the CRM may carry (households; round 4 after C-RESTRICTED) -- this cell links on transactions alone and says so.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.4 @51a7c07278 FWD-9 (row S2); CTO msg 105855; decomposition round 3 (measured constraint 2).
