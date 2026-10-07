# TO ADVI_COTBKF.TO-CB-d-2 -- round 4 CB-d-2: FWD-9 for every account that ends before 2026-06-23, each line followed to its newest account

<to_id>ADVI_COTBKF.TO-CB-d-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~13</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-d-2` (`decompositions/ADVI_COTBKF_DECOMP.round4.md`) | **outcome_ref:** FWD-9 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-d-2`, FWD-9: "where a client's account was replaced by a new one inside Commonwealth, an analyst reads the client's history as one line
from the oldest account to the newest, and sees which account each row came from; a link that cannot be shown is listed with its reason,
never guessed." Round 3 (`data/assets/scripts/silver/commonwealth_account_links.py`, read it first) linked only the 459 accounts that ended
before 2018, so a line stopped wherever its next account was not itself an old account (row ADVI_COTBKF-W11-S2: of 148 non-old link targets,
46 stopped trading before 2026). CTO ruling 3: every account that ends before 2026-06-23 gets a row, so every line reaches its newest account
or says why it stops. You prove it on the real table into a LOCAL directory. You write NOTHING to S3: `--apply` is the issuer's act.

**The data, measured at the cut.** Silver transactions `address('commonwealth', <cottonwood scope via lookup>, 'silver', 'transactions',
'date=2026-06-23')` (1,416,497 rows, 1,533 accounts) and silver positions `address(..., 'silver', 'positions', 'date=2026-06-23')` (469 rows,
column `AccountNumber`, 83 accounts, all present in transactions). **An ENDED account = an account with no row in the 2026-06-23 positions
table: 1,450 of 1,533** (459 last traded before 2018, 759 before 2026).

**The rule (unchanged from round 3's APPLIED reading, which the CVO verified on 2,652 of 2,652 evidence items):** A links to B when A's
holdings just before its in-kind exit are received in kind by B (`li` / transfer-in rows on the same CUSIPs, quantities equal within 0.001,
within 10 trading days), covering at least 80% of those holdings by count, with no second candidate meeting the bar (`AMBIGUOUS`, both listed,
never linked). Now applied to all 1,450 ENDED accounts. Every ended account gets exactly one row: `LINKED` (B, score, evidence) or `NOT_LINKED`
with a reason from a closed set that now includes `LEFT_COMMONWEALTH` (the in-kind exit has no receiver inside this delivery -- the crosswalk,
FWD-8, owns where it went), plus round 3's ("no in-kind receiver", "below threshold <score>", "ambiguous", "closed to cash"). Each row's
`client_line` follows links forward until an account that is OPEN (in the positions table) or ends without a link; print
`newest_account` and whether it is open.

**Output:** `--out <dir>` writes `account_links.parquet` and `.csv`; `--apply` writes at `address('commonwealth', <scope>, 'silver',
'account_links', 'date=2026-06-23')` (unit-tested on a stub, never run by you). LAST line exactly:
`ACCOUNT-LINKS ended_accounts=<n> every_ended_account_listed=<True|False> linked=<l> not_linked=<u> ambiguous=<a> chains=<c> lines_reaching_open_account=<o>`.

**Tests** in `data/assets/scripts/silver/tests/test_commonwealth_account_links.py` -- keep round 3's; add tests whose names contain
`ended`: an account absent from positions is ENDED and gets a row whatever its last-trade year; an exit with no receiver is `LEFT_COMMONWEALTH`;
a chain of three ends at an open account and reports it open; an account in positions gets no row.

### ACCEPTANCE

<criterion id="CB4d2-AC1" cell_refs="CB-d-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_account_links.py -k ended</invocation><expect>passed</expect></criterion>
`CB4d2-AC1` -- the ended-account rule and the new reason on fixtures.

<criterion id="CB4d2-AC2" cell_refs="CB-d-2"><invocation>python data/assets/scripts/silver/commonwealth_account_links.py --out .scratch/advi_cotbkf/account_links_r4</invocation><expect>ACCOUNT-LINKS ended_accounts=1450 every_ended_account_listed=True</expect></criterion>
`CB4d2-AC2` -- the real table: all 1,450 ended accounts listed, each linked with evidence or not linked with a reason.

<criterion id="CB4d2-AC3" cell_refs="CB-d-2" judgment="true"/>
`CB4d2-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: one client line that round 3 cut short now reaches its newest account, right on its
printed evidence; a sample of the new LINKED rows holds.

<expected_criteria>CB4d2-AC1,CB4d2-AC2,CB4d2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Local output and caches under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`;** S3 READS only of this project's silver tables; never `opal-data-bd` or `opal-data-inf`.
- **Never guess a link.** Within 120 seconds for CB4d2-AC2 (cache under `.scratch/`, warmed once untimed, and say so).
- **Rule 13:** a DS-lane script; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W13-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_account_links.py
data/assets/scripts/silver/tests/test_commonwealth_account_links.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round4.md</decomp_doc> (round 4), cell `CB-d-2`.
<owned_cells>CB-d-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB4d2-AC1, CB4d2-AC2, CB4d2-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS or
FAIL). Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~13/ADVI_COTBKF.TO-CB-d-2.links-every-ended-account.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB4d2-AC1,CB4d2-AC2,CB4d2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `ACCOUNT-LINKS` line, the NOT_LINKED reasons with counts, two client lines that now reach further than round 3's, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time builder.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads this project's silver under the laptop profile.
comp-adversary: RUN -- no guessed link (ambiguity listed; judgment criterion for the CVO); the ENDED definition is measured (positions table), not a year cut; BLIND: households the CRM may carry (after C-RESTRICTED).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO analysis ruling 3 (msg 105940); row W11-S2; CVO grade CB3c4-AC3; decomposition round 4 (measured constraint 3).
