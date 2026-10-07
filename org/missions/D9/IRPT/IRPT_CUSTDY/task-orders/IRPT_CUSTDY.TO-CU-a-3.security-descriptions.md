# TO IRPT_CUSTDY.TO-CU-a-3 -- round 1 CU-a-3: the securities -- every holding described from Opal's own classification, or marked as not described

<to_id>IRPT_CUSTDY.TO-CU-a-3</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~3</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-a-3` (`decompositions/IRPT_CUSTDY_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none (the decomposition fixes your interface)

---

## WORKER FACE

### THE CELL

`CU-a-3`, hop 4 of the round-1 thread. FWD-6: "every holding in a client report takes its class, sector and history from Opal's own
securities record, never from Black Diamond's labels; a holding Opal cannot describe is shown as such." Round 1 does this for one
advisor's holdings. You build the DESCRIBER and prove it on fixtures and on the real classification table (a repo file, no AWS).

**What exists (READ, never edit):** `infra/aws/lambda/v2_portal/_shared/etf_classification.py` -- the one classification table's reader
(MDPF_SECCLASS): `get_asset_class(ticker, default)`, `get_sector(ticker, default)`, `get_sub_asset_class(ticker, default)`,
`classify_holdings(holdings_df, ticker_column)`, `validate_tickers(tickers)`, `get_stats()`. Read it to learn what `default` returns for
an unknown ticker and how it loads its table. Import it; never copy its table.

**Your interface (fixed by the decomposition; two other consumers call it):** module
`data/assets/scripts/gold/irpt_custody/security_descriptions.py` exposes
`describe(holdings: list[dict]) -> list[dict]` -- each input dict (keys at least `symbol`, `cusip`) returned with four keys added:
`class`, `sector`, `described` (bool), `description_source` (`"MDPF_SECCLASS"` when the table describes it, `"NONE"` when it does not).
A holding the table does not know gets `class: null`, `sector: null`, `described: false`, `description_source: "NONE"` -- never a guessed
class, never a Black Diamond label. Input order is kept; input keys are never changed.

**Build:**
1. `describe()` as above, plus a CLI: `--symbols <comma list>` prints one line per symbol and then `DESCRIBED total=<n> described=<d>
   undescribed=<u>`; `--self-test`. Device-free.
2. `--self-test`: run `describe()` on a fixture of at least five holdings -- three tickers the real table knows (pick them by reading the
   table), one unknown ticker, one holding with no symbol -- and print, as the LAST line, `SECURITY-DESCRIBE-SELFTEST known_ok=<True|False>
   unknown_marked=<True|False> order_kept=<True|False>`.
3. Tests `data/assets/scripts/gold/irpt_custody/tests/test_security_descriptions.py` (pytest; insert the module's directory into
   `sys.path`; no `__init__.py`): a known ticker gets the table's class and sector; an unknown one is `described: false` with nulls; input
   order and keys preserved; an empty list returns an empty list.

### ACCEPTANCE

<criterion id="CU3-AC1" cell_refs="CU-a-3"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_security_descriptions.py</invocation><expect>passed</expect></criterion>
`CU3-AC1` -- the describer's behaviour: known, unknown, order, empty.

<criterion id="CU3-AC2" cell_refs="CU-a-3"><invocation>python data/assets/scripts/gold/irpt_custody/security_descriptions.py --self-test</invocation><expect>SECURITY-DESCRIBE-SELFTEST known_ok=True unknown_marked=True order_kept=True</expect></criterion>
`CU3-AC2` -- the seam against its REAL neighbour: the real classification table read through the real reader, with the unknown-ticker
difference control.

<expected_criteria>CU3-AC1,CU3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call.** No write anywhere outside a temp dir.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W3-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/security_descriptions.py
data/assets/scripts/gold/irpt_custody/tests/test_security_descriptions.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.md</decomp_doc> (round 1), cell `CU-a-3`.
<owned_cells>CU-a-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU3-AC1, CU3-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~3/IRPT_CUSTDY.TO-CU-a-3.security-descriptions.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU3-AC1,CU3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the self-test output, the three known tickers you used, the reader's behaviour for an unknown ticker, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a library function; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the cell makes no AWS call at all (repo files and local fixtures only).
comp-adversary: RUN -- no firm data (a ticker describer); read-only; BLIND: MDPF_SECHIST history (round 1 takes class and sector only; history is ENRICHMENT 3).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @c2bc15f427 section 2 hop 4, S05, FWD-6; decomposition contract (the one code interface).
