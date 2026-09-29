# TO IRPT_BCKEND.TO-IB-m21-213 -- UIC-16 at 49F: Schwab account-type and registration full names in the labels

<to_id>IRPT_BCKEND.TO-IB-m21-213</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~72</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-213`
(`decompositions/IRPT_BCKEND_DECOMP_R21_M.md`) | **outcome_ref:** FWD-5 (Holdings labels) | **depends_on:** IB-mr-203
drained (same file family)

---

## WORKER FACE

### THE CELL

`IB-mr-213` -- UIC-16 (the account type in full) is live for INF (CLOUD bcf7a6adde: `holdings_snapshot.py`
`account_mask` and `directory_runner.py` `masked_discriminator` keep the source's full type). 49F kept Schwab's codes
until a code list existed. The CTO committed one from Andrew's source:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/SCHWAB_ACCOUNT_CODES_BRIDGEFT_READ_20260929.json` (@41ef4ef498; source
https://docs.bridgeft.com/docs/source-account-and-registration-types, read 2026-09-29 04:1xZ; 27 `acct_type` and 101
`acct_regis` codes). In `dim_balance` 2026-09-25 the table names all 9 `acct_type` codes and 34 of 35 `acct_regis`
codes in use; RI401 (1 account) and blank (2 accounts) are absent (CTO 102567, 102582).

**Build:**
1. Load the table as DATA: copy it byte-for-byte into
   `data/assets/scripts/gold/investor_reporting/schwab_account_codes.json` (the build must not read another seat's
   deliverables folder at run time), keeping its `source_url` and `read_at`. Never fetch the URL.
2. 49F's ACCOUNT `display.label` (via `account_mask`, as the INF rule does) and the directory's `masked_discriminator`
   use the full names from that file. A code the file lacks prints as "unrecognised (<code>)" -- never guessed, never
   the raw code alone. Read commit bcf7a6adde (`git show`) for the INF shape and follow it; if `directory_runner.py`
   is generated, regenerate it with its generator (name it) rather than hand-editing.
3. The new data file joins the Holdings closure: add it to `_IRPT_HOLDINGS_CLOSURE` in `.tools/safe_deploy_core.py`
   (read-trace it the way amendment 1 of TO-IB-m19-2 did). Do not re-mint.
4. Tests: `data/assets/scripts/gold/investor_reporting/tests/test_schwab_codes.py` -- a known code maps to its full
   name, RI401 and blank print as unrecognised, and the loader refuses a table with no `source_url`.
5. Real local 49F build (no upload): write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R21_UIC16_49F_SUMMARY_20260929.json` as
   `{"table_source": "<the CTO path above>", "source_url", "accounts", "labelled_full_name", "unrecognised":
   {"<code>": <accounts>}, "guessed": 0}`.
6. **Every reader (round-19 analysis section 2 -- this changes a served figure):** write the half
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_UIC16_49F_20260929.md`
   (`## The act`, `## Blast radius` with the local candidate diff, `Rollback per key`) and census in it EVERY reader of
   49F's `display.label` and `masked_discriminator` (the portal Holdings card and account picker, directory search,
   exports, any cache), each with the check that will prove it on the served page at the re-mint.

### AMENDMENT 1 (2026-09-29 07:2xZ, issuer 2.0.0_SA_COO~M) -- READ THIS FIRST; it overrides step 2 and AC2 above

The first build (0.9.0_WK_IRPT_BCKEND~66, drained @57d87e9f0f) fed Schwab's `acct_type` into both labels. The CTO
REFUSED its half (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_REFUSED_HOLDINGS_UIC16_49F_20260929.md`,
@05b9abe572): `acct_type` is the PRODUCT code (`IRA` spans six registrations -- Contributory, Roth, Rollover, SEP,
SIMPLE, Inherited; `S1` "Schwab One" spans Individual, Joint, Designated Beneficiary, Living Trust, Custodial), so the
page would read "Individual Retirement" for a Roth. UIC-16 needs the REGISTRATION type: `acct_regis`.

Starting from CLOUD (which carries the first build: `schwab_account_codes.py/.json`, the two call sites, the closure
lines, `tests/test_schwab_codes.py`):
1. Both call sites -- `holdings_49f.build_49f_actual`'s `account_masks` step and `directory_runner.build_49f`'s
   `acct_row` `account_type` -- take `dim_balance`'s `acct_regis` column through the table's `acct_regis` map (never
   the `acct_type` map). Give `schwab_account_codes` an explicit registration lookup so the map used is named at the
   call site. A row with no `acct_regis` column or a blank value prints "unrecognised (<code>)" as before.
2. Tests: add a case proving a registration code (e.g. a Roth one) maps to its registration name and that the
   `acct_type` map is not what the label reads. RI401 and blank stay unrecognised.
3. Rewrite `R21_UIC16_49F_SUMMARY_20260929.json` from a real local build on 2026-09-25 with a new key
   `"field": "acct_regis"`; the CTO expects 7,545 of 7,548 named, `unrecognised` {"RI401": 1, "": 2}. Replace
   `measured.acct_type_value_counts` with `acct_regis_value_counts` and new sample labels.
4. Update the half in place: `## The act` and the counts say registration type; strike the product-code examples. Keep
   the readers census, rollback and release order. Leave the `## COO half` and `## CTO half` sections as they are.
AC1 and AC3 are unchanged; AC2 now runs `R21_CHECKS/r21_uic16_49f_regis.py`, which refuses a summary without
`"field": "acct_regis"`. Flip `<status>` back to `complete` only after all three pass.

### ACCEPTANCE

<criterion id="IBM21-213-AC1" cell_refs="IB-mr-213"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_schwab_codes.py -q -p no:cacheprovider</invocation><expect>a summary line with N passed and no failed or error</expect></criterion>
`IBM21-213-AC1` -- the built behaviour, including unrecognised codes and the loader's refusal.

<criterion id="IBM21-213-AC2" cell_refs="IB-mr-213"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R21_CHECKS/r21_uic16_49f_regis.py</invocation><expect>SCHWAB-REGIS-NAMED followed by the labelled and total account counts</expect></criterion>
`IBM21-213-AC2` -- a real local 49F build names every account the table covers, guesses none.

<criterion id="IBM21-213-AC3" cell_refs="IB-mr-213"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_UIC16_49F_20260929.md</invocation><expect>HALF-READY NEVER_WIDEN_HALF_REQUEST_HOLDINGS_UIC16_49F_20260929.md</expect></criterion>
`IBM21-213-AC3` -- the half, with its all-readers census, is written for the issuer to sign and send.

<expected_criteria>IBM21-213-AC1,IBM21-213-AC2,IBM21-213-AC3</expected_criteria>

Dry-run at the base 2026-09-29 04:4xZ: AC1 "no tests ran", AC2 NOT-NAMED (summary absent), AC3 NOT-READY -- FAIL as
expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** No upload, no mint, no served write, no URL fetch. `holdings_snapshot.py` and
  `directory_runner.py` are members of the directory bundle (MSTR skips it at push).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W72-S<k>`), and do not weaken the test to pass.

<paths>
data/assets/scripts/gold/investor_reporting/
.tools/safe_deploy_core.py
docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R21_UIC16_49F_SUMMARY_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_UIC16_49F_20260929.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R21_M.md</decomp_doc> (round 21, workstream ~M), cell `IB-mr-213`.
<owned_cells>IB-mr-213</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM21-213-AC1, IBM21-213-AC2, IBM21-213-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~72/IRPT_BCKEND.TO-IB-m21-213.uic16-49f-schwab-full-names.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM21-213-AC1,IBM21-213-AC2,IBM21-213-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the label rule and where it lives, the data file and closure change, the summary
counts, the readers census, the pytest lines, the half's path, commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the served move rides the round-20 halves' re-mint.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change.
comp-adversary: RUN -- 1 commit read (bcf7a6adde: directory_runner.py 4 lines, holdings_snapshot.py 13, one test) and 1 table read (27 acct_type / 101 acct_regis codes, @41ef4ef498); BLIND: 49F's label code path and the readers of display.label were not traced at the cut (step 6 censuses them).
lane: the <paths> block IS the grant; ~M owns the gold holdings snapshot.
</preflight>

Source: CTO 102567 and 102582; CTO round-19 analysis (@d797a87872) section 6 item 2.
