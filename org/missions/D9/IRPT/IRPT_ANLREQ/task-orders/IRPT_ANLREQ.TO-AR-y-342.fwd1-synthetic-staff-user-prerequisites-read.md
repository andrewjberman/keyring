# TO IRPT_ANLREQ.TO-AR-y-342.fwd1-synthetic-staff-user-prerequisites-read -- the FWD-1 synthetic staff user's prerequisites read: whether the address form is admitted everywhere, what the ticket CREATE, upload door and analysis submit each need of the user, and the minting recipe; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-342</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~146</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ3</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-342` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~146`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-146` (branch `wk-IRPT_ANLREQ-146`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~146 <0.9.0_WK_IRPT_ANLREQ~146@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W146-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call, NO PUSH, no AWS call of any kind, no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-342`, inlined) -- a READ. The product tree is not edited.

*Context. The FWD-1 run files ONE Analysis Request in the Ticket Center as a synthetic Opal STAFF user whose address is `fwd1-staff-r41a@opal.invalid` (CTO msg 7767: the producer list gains exactly that address; it must be non-routable, unique to the run and never reused). The staff filer chooses the partner firm in the form (`AR-y-325`, merged and on portal DEV), and the same chosen firm must pass on all three hops: the ticket CREATE (`POST /api/scoped/tickets`), the upload door (`deps.ir.uploadAnalysisInput(upload, selectedTenant)`) and the analysis submit. Nobody has yet read, from source, what such a user must carry for every hop to accept it, nor whether the address form itself is admitted. The run order and the minting order depend on this record.*

Answer these four questions from SOURCE, each with `file:line` evidence read from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, the address.** Is an address of the form `fwd1-staff-r41a@opal.invalid` admitted as a signed-in INTERNAL (staff) principal everywhere the three hops read it? Search for any domain allow-list, suffix rule, regex or deny-list on the email or sub: the portal authorizer (`C:/dev/wk-irpt-anlreq-146/infra/aws/users/lambda/portal-authorizer/index.mjs`), the user store lookups (`opal-users-v2`, the email GSI, `infra/aws/users/`), the ticket service (`infra/aws/lambda/ticket_center/lambda_function.py`: `_actor`, `principal_class`, the INTERNAL class rules), and Investor Reporting (`_scope/served.py` `verified_internal_subject`, `_scope/interactive_access.py` `InteractiveAccess.current`, the OPAL_GLOBAL class test). For each place state `admits`, `refuses` or `not constrained`, with the line. A `.invalid` domain, a hyphen in the local part and digits must each be addressed.
2. **Q2, the ticket CREATE hop.** What must the synthetic user's record carry so `create_ticket` accepts an `analysis_request` for a partner firm chosen by a staff filer: `userType`, the class `principal_class` resolves, `allowedFirmIds` (and the exact form for the three firms `49financial`, `cottonwood`, `inflection`), the INTERNAL profile scope (`_in_profile_scope`), and any role or permission flag. Quote the functions `_firm_allowed`, `_in_profile_scope` and the CREATE row of the permission matrix (`MATRIX`) with lines. Also: what makes the Ticket Center page visible to this user in the portal (the internal-only rule: Andrew's ADDENDUM v0.6) so a person or the run can open it.
3. **Q3, the upload door and the analysis submit hops.** For a staff caller with `selected_tenant` = a partner firm: does the Investor Reporting upload door (the handler `uploadAnalysisInput` reaches; `intake/` and `_scope/`) check that firm against the caller's allowed firms, and what does it require of the caller's class (OPAL_GLOBAL or other)? The same for the analysis submit (`ycharts/generate/submission.py`, `acceptance.py`, `composition_admission.py`, `request_composition.py`): the owner the accepted record stores for a staff caller (`owner.principal_id`, `principal_class`, whether `home_firm_id` is allowed) and the check that the chosen firm equals the record's firm. State plainly whether one synthetic user record can pass all three hops for ONE chosen firm, or whether a hop needs an extra attribute.
4. **Q4, the minting recipe.** Read how the earlier sittings minted and removed synthetic users: `C:/dev/wk-irpt-anlreq-146/org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r30/sitting_r30.py` and the R29 sitting's scripts under `.../irpt_anlreq_r29/` (a name search inside those folders only). List the exact attributes a minted INTERNAL user row needs (key shape, table, `userType`, class, allowedFirmIds, email, GSI attributes, `exp`/TTL), how the portal token is obtained for it (a signed JWT with `sub`, `userType`: from which key slot; which tool), and how the row is removed and verified ABSENT. Do NOT mint anything, call anything or print a key or token. End with ONE line: `RECOMMEND: MINT_AS_DESCRIBED` or `RECOMMEND: CHANGE_ADDRESS <why>` or `RECOMMEND: NEEDS <what>`, and the one fact that decides it.


### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-146/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~146/r41/FWD1_PREREQ_READ.json` with keys: `base` (the sha your branch started from), `q1` {`rows` (a list of {`place`, `verdict` (`admits`|`refuses`|`not_constrained`), `evidence` {file, line, text}}), `domain_rule_exists` (true|false), `invalid_domain_ok` (`yes`|`no`|`unknown`)}, `q2` {`needs` {`userType`, `class`, `allowedFirmIds`, `profile_scope`, `other` (string)}, `functions` (list of {file, line, text}), `ticket_center_visibility` (string), `evidence` (list)}, `q3` {`door_checks_firm` (`yes`|`no`|`unknown`), `door_requires_class` (string), `submit_requires_class` (string), `owner_stored` (string), `firm_equality_check` (string), `one_record_passes_all_three` (`yes`|`no`|`unknown`), `extra_attribute` (string or null), `evidence` (list)}, `q4` {`row_attributes` (list of {name, value_or_form}), `table` (string), `token_method` (string), `removal_and_absent_check` (string), `evidence` (list), `recommend` (`MINT_AS_DESCRIBED`|`CHANGE_ADDRESS`|`NEEDS`), `deciding_fact` (string)}, and `not_read` (what you did not read: the live system, the deployed bytes). Then write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~146/shape_check.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~146/cite_check.py` named below. Every cited `{file, line, text}` is a path relative to the worktree root.

<criterion id="AR342-y-AC1" cell_refs="AR-y-342"><invocation>python C:/dev/wk-irpt-anlreq-146/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~146/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR342-y-AC1`: `shape_check.py` loads `r41/FWD1_PREREQ_READ.json` and prints `SHAPE-OK <keys>` only when every key above is present with an allowed value (`q1.invalid_domain_ok`, `q3.one_record_passes_all_three`, `q4.recommend` in their enums) and every answer block has at least one evidence item; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR342-y-AC2" cell_refs="AR-y-342"><invocation>python C:/dev/wk-irpt-anlreq-146/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~146/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR342-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It prints the denominator n.

<criterion id="AR342-y-AC3J" cell_refs="AR-y-342" judgment="true"/>
`AR342-y-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR342-y-AC1 AR342-y-AC2 AR342-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~146/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-342</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~146/IRPT_ANLREQ.TO-AR-y-342.fwd1-synthetic-staff-user-prerequisites-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-342`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR342-y-AC1,AR342-y-AC2,AR342-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape; the lens: an answer asserted without a read line, a 'not found' said without a search, a binding assumed set because a name exists, a recommendation that widens beyond the cell. The cell requires cited lines checked by script, a stated search for every absence, and a stated recommendation. NOT seen (blind): the live system and the deployed bytes; denominator: 4 questions, each answered with cited lines.
</preflight>

---

## RECORD FACE

- Cut as a dependency-free read while leg L waits on its applier (the usage limit of `0.7.0_AE_CloudOps~AQ2`). Workstream `ZZ3` of round 40. Risk LOCAL. Base: `AR342-y-AC1` and `AC2` FAIL as expected.
- Its output feeds the FWD-1 run order and the minting order; nothing is changed by this cell.
