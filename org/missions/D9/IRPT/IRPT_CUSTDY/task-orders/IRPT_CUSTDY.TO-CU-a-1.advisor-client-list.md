# TO IRPT_CUSTDY.TO-CU-a-1 -- round 1 CU-a-1: the advisor's client list, and the measured pick of the round's advisor

<to_id>IRPT_CUSTDY.TO-CU-a-1</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~1</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-a-1` (`decompositions/IRPT_CUSTDY_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (the decomposition fixes the one code interface you call)

---

## WORKER FACE

### THE CELL

`CU-a-1`, hop 1 of the round-1 thread, FWD-1: "One 49 Financial advisor's quarter-end client reports are produced by Opal from
Schwab's records." Hop 1 names the advisor and lists that advisor's accounts and households. You build the LIST and the PICK and prove
both on fixtures; the issuer runs them on real data after the drain. Read only: the tool writes nothing anywhere.

**What exists (READ, never edit):**
- `infra/logic/registry/scopes.json` -- the identity registry; 49 Financial's two Schwab masters are `08242234` and `08335338`; the firm
  is resolved by `lib/opal_naming.py` `lookup(<master>)['firm']` (never type a firm token: the commit-time naming gate refuses a firm
  token in any string outside the registry and the arguments of `lookup()`/`address()`/`name()`).
- `data/assets/scripts/gold/investor_reporting/directory_runner.py` -- IRPT_BCKEND's directory producer: `build_49f(data,
  business_date, directory_revision)` builds the directory entries (`_entry(firm_id, client_raw, rel_raw, account_rows, display_name,
  scope_kind, ...)`); `masked_discriminator(account_number, account_type)` is the house masking. Read it to find where the advisor
  (rep) and the household live in an entry. **If the directory carries no advisor field, that is a BLOCKING row (the PRD's S01 claim),
  not something you invent.**
- Schwab silver under `opal-data-assets/schwab/<master>/silver/` (producer `data/assets/scripts/silver/schwab_conversion.py`): read it to
  learn the positions table's name and partition shape for the coverage test below.
- The one code interface (the decomposition fixes it): `data/assets/scripts/gold/irpt_custody/security_descriptions.py` exposes
  `describe(holdings: list[dict]) -> list[dict]`, adding `class`, `sector`, `described`, `description_source` to each holding. Another
  worker builds it in parallel; **you import it lazily at run time and your tests inject a stub with that signature.**

**Build `data/assets/scripts/gold/irpt_custody/advisor_client_list.py`:**
1. CLI: `--advisor <id or name>`, `--pick`, `--as-of <YYYY-MM-DD>` (default `2026-09-30`), `--directory <local file or s3 key>` (default:
   the latest directory partition the producer writes, located the way `directory_runner.py` lands it), `--silver-root <local dir or s3
   prefix>`, `--self-test`. Device-free (no hardcoded drive or user path).
2. List mode (`--advisor`): every account and household of that advisor; print one line per household with its accounts, account numbers
   masked to the last 4 (`masked_discriminator`), then `CLIENT-LIST advisor=<a> households=<h> accounts=<n>`. An advisor with zero accounts
   prints `CLIENT-LIST advisor=<a> households=0 accounts=0` and exits 2.
3. Pick mode (`--pick`), the CTO's ruling exactly: over every 49 Financial advisor in the directory, keep those with 10 OR MORE households
   whose EVERY account has Schwab silver position rows at `--as-of`; pick the one with the FEWEST households; break a tie by the MOST
   distinct asset classes held (classes via `describe()`); a remaining tie by advisor id ascending. Print the census -- one line per
   advisor scanned: id, households, accounts, accounts covered at `--as-of`, eligible yes/no and why not -- then
   `ADVISOR-PICK scanned=<s> eligible=<e> pick=<id> households=<h> classes=<c>`. No eligible advisor prints `pick=NONE` and exits 2.
4. `--self-test`: build a fixture directory of at least four advisors (one under 10 households, one with an uncovered account, two
   eligible tied on households and split by classes) and a fixture silver root, with a stub `describe()`; run the list and the pick; print,
   as the LAST line, `ADVISOR-LIST-SELFTEST list_ok=<True|False> pick_ok=<True|False> tie_ok=<True|False>`.
5. Tests `data/assets/scripts/gold/irpt_custody/tests/test_advisor_client_list.py` (pytest, fixtures in `tmp_path`, insert the module's
   directory into `sys.path`; no `__init__.py`): the 10-household floor; an uncovered account excludes its advisor; fewest households wins;
   the class tie-break; masking keeps only the last 4; zero accounts exits 2.

### ACCEPTANCE

<criterion id="CU1-AC1" cell_refs="CU-a-1"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_advisor_client_list.py</invocation><expect>passed</expect></criterion>
`CU1-AC1` -- the list and the pick rule on fixtures: floor, coverage exclusion, fewest households, the tie-break, masking, the zero exit.

<criterion id="CU1-AC2" cell_refs="CU-a-1"><invocation>python data/assets/scripts/gold/irpt_custody/advisor_client_list.py --self-test</invocation><expect>ADVISOR-LIST-SELFTEST list_ok=True pick_ok=True tie_ok=True</expect></criterion>
`CU1-AC2` -- the seam through the real CLI on a fixture directory (the real pick is the issuer's act after the drain).

<expected_criteria>CU1-AC1,CU1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call** in your tests or self-test (fixtures only; the S3 read path is written and exercised by the issuer).
- **Read only:** the script writes nothing outside a temp dir. Never print a full account number.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W1-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/advisor_client_list.py
data/assets/scripts/gold/irpt_custody/tests/test_advisor_client_list.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit (`lib/opal_naming.py` included).

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.md</decomp_doc> (round 1), cell `CU-a-1`.
<owned_cells>CU-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU1-AC1, CU1-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~1/IRPT_CUSTDY.TO-CU-a-1.advisor-client-list.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU1-AC1,CU1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the self-test output, the CLI, the test list, where the directory carries the advisor and the household, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read tool run by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the issuer's real run reads with the dell2 box profile.
comp-adversary: RUN -- cross-firm (49financial scope only, resolved by lookup()); read-only; BLIND: whether the directory carries the advisor (the worker measures it; absent = BLOCKING row).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @c2bc15f427 section 2 hop 1, FWD-1, S01; decomposition constraint 7 (the CTO's pick ruling, msg 103).
