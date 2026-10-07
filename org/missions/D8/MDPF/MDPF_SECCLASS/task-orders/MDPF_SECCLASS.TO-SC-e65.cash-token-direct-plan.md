# TO MDPF_SECCLASS.TO-SC-e65 -- round 11 SC-e-65: C-CASH-TOKEN: the scheduled producer's direct plan places a whole-token CASH security as cash/Cash

<to_id>MDPF_SECCLASS.TO-SC-e65</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~47</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-65` (`decompositions/MDPF_SECCLASS_DECOMP_R11.md`) |
**outcome_ref:** FWD-7, FWD-13, FWD-17 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-65`. Andrew-direct (via 2.0.0_SA_COO~M2, ~14:1xZ 2026-10-07), on the "Classification not found" tickers of the 10-05 Cottonwood
build (BDCASHIN, FCASH, CQP and five more), verbatim: "most of those items literally have "Cash" as a token within, which would be the
"Cash" asset class. The others could likely be websearched."

PRD v0.15 C-CASH-TOKEN (1.0.0_SA_CTO~DELL1 msg 327): "a whole-token CASH in a ticker or name places the security in the TABLE as
cash/Cash by the direct plan, with classified_by naming the rule. A test pins BDCASHIN or FCASH in and CASHMERE out."

**Your base is the held branch `q/dell1/secclass-r9-held-34/r2` (cbbda93539).** It carries SC-e-44 and SC-e-63 in the same module.

**Where the direct plan is:** in `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`,
`plan_rows(held_securities, *, vocab, existing_tickers, ...)`. It takes `(ticker, name)` pairs and calls
`classify_asset_class(ticker, ...)` for each. A key with no direct match is listed unresolved. Each planned row carries
`classified_by = "scheduled"` (`CLASSIFIED_BY`) and an `input` field naming its source.

**Build:**
1. Before the other direct sources, a held security whose ticker or name carries `CASH` as a whole token is planned
   `asset_class` `cash`, `sub_asset_class` `Cash`. Its `input` names the rule (`cash_token`).
   - **The token rule, which you define and state in the docstring:** in a name, "cash" as a whole word, case-insensitive. In a
     ticker, `CASH` bounded by the ticker's start or end or by a known word split (BDCASHIN = BD + CASH + IN, FCASH = F + CASH). It
     must keep CASHMERE (a word that starts with CASH) out.
   - **Real names:** read the real names of the Cottonwood tickers from the build the CVO read (search the repo for BDCASHIN; the
     laptop CVO read @09e0d7c89c is on CLOUD if present). Make the rule hold for them.
2. **classified_by:** "classified_by naming the rule". Read `org/standards/MDPF_SECCLASS_CONTRACT.json`'s `classified_by` field.
   - If its values are a closed list without a value for this rule, keep `classified_by = "scheduled"` and name the rule in `input`.
     That is the issuer's ruling for this cell. Say so in your report and file an OBSERVATION row; do not edit the contract.
   - If the contract admits a value for it, use that value.
3. Add `infra/aws/lambda/v2_portal/_shared/tests/test_cash_token.py`. It pins BDCASHIN and FCASH to cash/Cash with `input` naming
   the rule, CASHMERE out (not cash/Cash), and a name-only case (a ticker with no CASH whose name has the word "Cash").
4. Do not change any other source's precedence. An existing row is never planned, as today.

### ACCEPTANCE

<criterion id="SC11-e65-AC1" cell_refs="SC-e-65"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e65_cash_token.py</invocation><expect>SC-E65 ok=True</expect></criterion>
`SC11-e65-AC1` -- plan_rows plans BDCASHIN ("BD Cash In") and FCASH ("Fidelity Cash") as cash/Cash. CASHMERE ("Cashmere Valley Bank")
is not cash/Cash, which is the difference control. The check reads the tree it is run from.

<criterion id="SC11-e65-AC2" cell_refs="SC-e-65"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC11-e65-AC2` -- the `_shared` suite passes with the new test. The control at the base is 185 passed.

<expected_criteria>SC11-e65-AC1,SC11-e65-AC2</expected_criteria>

Dry-run at the base (cbbda93539, 2026-10-07): SC11-e65-AC1 FAIL as expected (`BDCASHIN=None FCASH=None CASHMERE=None unresolved=3`); SC11-e65-AC2 PASS as expected (control, 185 passed).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54). No web search: the research of the other tickers is the issuer's act.
- No table write, no deploy, no upload. This is a shipped `_shared` member, so your branch rides the held-34 line. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W47-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py
infra/aws/lambda/v2_portal/_shared/tests/test_cash_token.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R11.md</decomp_doc> (round 11), cell `SC-e-65`.
<owned_cells>SC-e-65</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC11-e65-AC1, SC11-e65-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~47/MDPF_SECCLASS.TO-SC-e65.cash-token-direct-plan.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC11-e65-AC1,SC11-e65-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the token rule as written, the classified_by reading, the real Cottonwood names and how each grades, AC1/AC2 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the module change schedules nothing; it rides the e44/e63 deploy under its pair.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes.
comp-adversary: RUN -- CASHMERE-shaped false positives (AC1's control arm); a rule that outranks a stronger direct source (step 4); BLIND: the live planned set (the deploy's producer-live run).
lane: the <paths> block IS the grant; base is the held-34 line by issuer ruling in DECOMP_R11.
</preflight>

Source: round-10 analysis @a856d1525f section 2.3, section 3 item 6; PRD v0.15 C-CASH-TOKEN @54e82922e4; DECOMP_R11.
