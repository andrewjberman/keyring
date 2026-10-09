# TO NFRA_TRNSPT.TO-TR-h16 -- H6: household optional for svc-commentary (row D2-S7, as ~V2 shipped)

<to_id>NFRA_TRNSPT.TO-TR-h16</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-h-16` (`decompositions/NFRA_TRNSPT_DECOMP_R16.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-h-16` (CTO msg 2205; row NFRA_TRNSPT-D2-S7): "household is optional for svc-commentary only, deployed in F10-d-1 v2". Real IRPT reports carry
no household (~P2 msg 1849), but `data/transcripts/scripts/commentary/ticket_client.py` still requires it: `_REQUIRED_ANSWERS = ("advisor", "firm",
"household", "report_type", "add_commentary")` (:13), the body reads `ctx["household"]` (:25) and the title is "Draft commentary -- %s (%s)" %
(household, report_type) (:32); `stub_post` checks `_REQUIRED_ANSWERS` (:96).

**Build -- to ~V2's contract v0.2 @20784c5462 (`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md`
section 8, "what shipped"; ~V2 msg 2214), which supersedes the issuer's interim rule:**
1. `ticket_client.py`: `household` is OPTIONAL for svc-commentary -- when the ticket context has none (missing, None or empty), OMIT the
   `household` key from `answers` (no placeholder); when one is present it may be sent as before. The TITLE is ALWAYS "Draft commentary --
   <firm> (<report_type>)" and is NEVER built from household (v0.2 section 8: "never put client identity in the title"; at most 300 characters).
   `stub_post` accepts a body without `answers.household`, rejects a title over 300 characters, and still refuses every other missing required
   value. Nothing else changes.
2. `data/transcripts/scripts/tests/test_commentary_ticket_client.py`: add `test_household_optional_for_svc_commentary` (no household -> the body has
   no household key, the title is "Draft commentary -- <firm> (<report_type>)", the stub returns 201 and `action: done`); update ONLY existing
   assertions that expected the household in the title; keep every other test green.
3. Read the token from the secret named in v0.2 (`opal/ticketing/svc-commentary`, its `.token`) only through the injected `token_reader` -- no
   secret read in this cell.

### ACCEPTANCE

<criterion id="TR16-h16-AC1" cell_refs="TR-h-16"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R16_CHECKS/r16_checks.py h16</invocation><expect>R16-H16-OK</expect></criterion>
`TR16-h16-AC1` -- the household-optional test passes by name and the ticket-client suite is green.

<expected_criteria>TR16-h16-AC1</expected_criteria>

Dry-run at the base (box/dell2 20784c5462): `R16-H16-FAIL missing test_household_optional_for_svc_commentary` -- FAIL as expected. Keep every
`test_commentary_*.py` green.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** No AWS, HTTP or gateway call; fakes only.
- **Refusal clause.** If making household optional breaks a test outside these paths, stop and file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next
  unused across every document under `surprise-channel/`).

<paths>
data/transcripts/scripts/commentary/ticket_client.py
data/transcripts/scripts/tests/test_commentary_ticket_client.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R16.md</decomp_doc> (round 16), cell `TR-h-16`.
<owned_cells>TR-h-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR16-h16-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-h16.household-optional.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR16-h16-AC1` BEFORE the flip. Commit code first, then pin each artifact to a commit
that contains it.
</proof_of_spec>

**REPORT:** the body and title with and without household, the test name, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a client change.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 2 sources read (ticket_client.py :12-32, :88-112; ~V2's shipped behavior per CTO msg 2205); BLIND to the live API (H5 deployed, svc-commentary token not yet minted). Traps: dropping household when one IS present, loosening another required field; the face fixes both.
lane: the ticket client, its test, the investigation file.
</preflight>

Source: CTO msg 2205; row NFRA_TRNSPT-D2-S7; decomposition round 16 cell TR-h-16 and issuer ruling 1.
