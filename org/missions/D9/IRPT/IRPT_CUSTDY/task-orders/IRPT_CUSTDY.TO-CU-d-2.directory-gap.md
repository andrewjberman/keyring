# TO IRPT_CUSTDY.TO-CU-d-2 -- round 4 CU-d-2 (E2): the chosen advisor's directory gap -- every account reported, named from the ownership map, the gap counted

<to_id>IRPT_CUSTDY.TO-CU-d-2</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~10</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-d-2` (`decompositions/IRPT_CUSTDY_DECOMP.round4.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (the decomposition fixes the `si_anchor` field you read)

---

## WORKER FACE

### THE CELL

`CU-d-2`, item E2 of the CTO's round-3 analysis: the chosen advisor's directory gap. `data/assets/scripts/gold/irpt_custody/hop3_real_run.py`
builds one advisor's client-report documents (through `client_report_figures.py`) and writes them to ONE file. On real data (advisor
`matthew_gooch`, as-of 2026-09-30) it reported 10 households, 14 accounts, and listed 4 granted accounts as uncovered with reason
`NOT_IN_DIRECTORY` -- those 4 got no report.

**The ruling (CTO):** FWD-1 reads accounts from the ownership map; the directory supplies only names and households. So an account that is
NOT_IN_DIRECTORY still gets its report, with its name (and household) taken from the ownership map, and the count of the advisor's
NOT_IN_DIRECTORY accounts is printed with the advisor's denominator.

**What exists (READ):** `hop3_real_run.py` (your edit target), `advisor_client_list.py` (`book_of`, the ownership map's advisor entries:
`accounts`, `relationships`), the ownership map via `opal_naming.legacy_address('blackdiamond-platinum-49financial-ownership-map')`
(never type the key), `client_report_figures.py` (read only -- another cell is changing it in parallel).

**The field you print (fixed by the decomposition; another cell writes it):** each account document will carry
`"si_anchor": {"date", "rule": 1|2|3|null, "label", "status": "OK|NOT_AVAILABLE|NO_ANCHOR"}`. Print it when present; when absent (today's
code) print `si_anchor=ABSENT` -- never fail on its absence. Your tests stub it.

**Build:**
1. In `hop3_real_run.py`: a granted account that is NOT_IN_DIRECTORY is no longer dropped. Build its document like any other, with the
   household and name taken from the ownership map's relationship for that account (or the account's own masked id as its household when
   the map has none, said so in a `name_source` field: `DIRECTORY | OWNERSHIP_MAP | ACCOUNT_ONLY`). Only an account with no Schwab data at
   the as-of stays uncovered, with its reason.
2. The summary line keeps its fields and adds `not_in_directory=<n> of=<advisor's granted accounts>`. One line per account prints its masked
   id, `name_source`, and `si_anchor` (date, rule) or `si_anchor=ABSENT`.
3. A NEW script `data/assets/scripts/gold/irpt_custody/check_directory_gap.py --advisor <slug> --as-of <d>` that runs the wrapper in-process
   to a temp file and prints `DIRECTORY-GAP advisor=<slug> granted=<n> not_in_directory=<n> reported=<n> all_reported=<True|False>`
   (`all_reported`: every granted account with Schwab data at the as-of has a document). The temp file is deleted; nothing is committed.
4. Tests in a NEW file `data/assets/scripts/gold/irpt_custody/tests/test_hop3_directory_gap.py` (fixtures, stubbed readers, no AWS): a
   NOT_IN_DIRECTORY account gets a document with `name_source=OWNERSHIP_MAP`; the count and denominator print; an absent `si_anchor` prints
   `ABSENT` without failing; masking holds. Round 3's `test_hop3_real_run.py` must still pass (edit only where the change requires).

### ACCEPTANCE

<criterion id="CU11-AC1" cell_refs="CU-d-2"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_hop3_directory_gap.py</invocation><expect>passed</expect></criterion>
`CU11-AC1` -- the gap rule on fixtures: reported with its name source, counted with its denominator, the anchor printed or ABSENT.

<criterion id="CU11-AC2" cell_refs="CU-d-2"><invocation>python data/assets/scripts/gold/irpt_custody/check_directory_gap.py --advisor matthew_gooch --as-of 2026-09-30</invocation><expect>all_reported=True</expect></criterion>
`CU11-AC2` -- the seam against its REAL neighbour: the chosen advisor on real data on dell2. The counts are reported, not graded.

<expected_criteria>CU11-AC1,CU11-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS: read only.** No write; never `--apply`. **Never commit a real-run output file** (it holds client figures).
- **Never print or write a full account number.** Never edit `client_report_figures.py` or another cell's or project's file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W10-S<k>`; `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do
  not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/hop3_real_run.py
data/assets/scripts/gold/irpt_custody/check_directory_gap.py
data/assets/scripts/gold/irpt_custody/tests/test_hop3_directory_gap.py
data/assets/scripts/gold/irpt_custody/tests/test_hop3_real_run.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round4.md</decomp_doc> (round 4), cell `CU-d-2`.
<owned_cells>CU-d-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU11-AC1, CU11-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~10/IRPT_CUSTDY.TO-CU-d-2.directory-gap.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU11-AC1,CU11-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the real `DIRECTORY-GAP` line, how many documents moved from uncovered to reported, the test list, rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a run by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads opal-data-assets, opal-data-bd and opal-data-49financial with the dell2 box profile.
comp-adversary: RUN -- cross-firm (49financial only); read-only; no real-run file committed; BLIND: whether the ownership map carries a relationship (name) for every NOT_IN_DIRECTORY account.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-3 analysis @ec25e39844 section 2 S8(b) and section 3 E2; row S8; decomposition round 4 constraints 2-3 and the anchor field.
