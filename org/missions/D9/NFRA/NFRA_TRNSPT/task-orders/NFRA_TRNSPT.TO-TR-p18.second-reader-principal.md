# TO NFRA_TRNSPT.TO-TR-p18 -- FWD-8: the second named reader's AWS principal, minted by name(), added to the transcripts key's readers

<to_id>NFRA_TRNSPT.TO-TR-p18</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-p-18` (`decompositions/NFRA_TRNSPT_DECOMP_R18.md`) | **outcome_ref:** FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-p-18` (CTO ADDENDUM 6 @7558d41da5): "the second named reader gets its AWS principal. Andrew named the readers; the principal is minted by name
through `name()`, under a pair." The named readers (Andrew-direct 2026-09-29) are two accounts: `andrew@opalinvest.com` and
`opalbloomberg@opalinvest.com`. Today `infra/aws/terraform/transcripts/main.tf:57-60` `var.reader_principal_arns` defaults to
`user/Andrew_Berman` only; the key policy's `NamedReadersUseTheKey` statement uses that list. Work in your worktree.

**Build:**
1. Mint the second reader's principal with `lib/opal_naming.py name()` (choose the scope and kind the builder admits for a human reader of the
   transcripts tier; record the builder call and its output in `data/transcripts/scripts/teams/NAMES.json` under a `second_reader` key, read by
   the tf, never typed). Declare it in `infra/aws/terraform/transcripts/main.tf` (or a new `infra/aws/terraform/transcripts/readers.tf`) as an
   IAM role that a person assumes, with NO policy other than what reading the transcripts tier needs: `s3:GetObject` / `s3:ListBucket` on
   `opal-data-transcripts` and the key use the key policy grants. Add its ARN to the named readers the key policy uses. Nothing else widens: the
   Dell users' grants, the commentary grant and every other statement stay byte-identical.
2. Who may assume it (the trust policy) is NOT decided in this cell: leave the trust principal to a variable with no default and say so; the
   issuer's pair names it with Andrew's routing.
3. `data/transcripts/scripts/tests/test_transcripts_second_reader.py` (new; parse the tf text, no AWS): `test_second_reader_from_builder` (the
   name the tf uses equals the NAMES.json builder output); `test_second_reader_in_named_readers` (its ARN reaches the key policy's named-reader
   list); `test_no_other_reader_widened` (the Dell-user and commentary statements are unchanged from the base).
4. If `terraform` resolves on your worktree, run `fmt -check` and `validate` after `init -backend=false`; else say "terraform not resolved".

### ACCEPTANCE

<criterion id="TR18-p18-AC1" cell_refs="TR-p-18"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R18_CHECKS/r18_checks.py p18</invocation><expect>R18-P18-OK</expect></criterion>
`TR18-p18-AC1` -- the three named tests pass.

<expected_criteria>TR18-p18-AC1</expected_criteria>

Dry-run at the base (box/dell2 c2d3f143d3): `R18-P18-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **WORLD by path floor, LOCAL in act.** No AWS call, plan or apply.
- **Refusal clause.** A builder refusal for the reader's name: add nothing typed; file a surprise row (`NFRA_TRNSPT-D2-W2-S<k>`, next unused across
  every document under `surprise-channel/`) and stop that piece.

<paths>
infra/aws/terraform/transcripts/main.tf
infra/aws/terraform/transcripts/readers.tf
data/transcripts/scripts/teams/NAMES.json
data/transcripts/scripts/tests/test_transcripts_second_reader.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R18.md</decomp_doc> (round 18), cell `TR-p-18`.
<owned_cells>TR-p-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR18-p18-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-p18.second-reader-principal.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR18-p18-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** the builder call and name, the declared resource and its policy, how its ARN reaches the key policy, the trust variable, the test
names, the check line, terraform fmt/validate or "not resolved", commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an identity declaration.
comp-iam: RUN -- 1 key policy read (main.tf: RootAdministersTheKeyAndCannotUseIt, NamedReadersUseTheKey, DellAgentUsersDecryptOnly, DellAgentUsersGenerateDataKey, two Deny statements); adds one reader to NamedReadersUseTheKey only; trust left to the pair.
comp-adversary: RUN -- sources: main.tf :1-60 and the key policy, Andrew's 2026-09-29 record, FWD-8's amended text, the existing IAM user Opal_Terminal (issuer read; not builder output, not mapped). Traps: adopting a typed name, widening another statement, deciding the trust in code; the face fixes each.
lane: the transcripts root's reader declaration, the teams NAMES.json, one test, the investigation file.
</preflight>

Source: CTO msg 2894 (ADDENDUM 6); decomposition round 18 cell TR-p-18 and issuer rulings 1-2.
