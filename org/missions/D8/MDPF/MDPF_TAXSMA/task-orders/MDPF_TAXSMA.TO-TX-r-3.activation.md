# TO MDPF_TAXSMA.TO-TX-r-3 -- activation: the measured first capability read under the named identity, bearer value, prelude on, rollout switch on, live authorized readback

<to_id>MDPF_TAXSMA.TO-TX-r-3</to_id>
<project>MDPF_TAXSMA</project>
<issued_to>0.9.0_WK_MDPF_TAXSMA~6</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @671925aecc (ADMITTED) | **Contract:** `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` | **Decomp cell:** `TX-r-3` | **serves:** FWD-1, 7 (S16) | **slot:** ~6, queue position 4 | **HELD on:** G-W,G-P (decomposition s.6); the COO spawns this order only when the gate's record exists

---

## WORKER FACE

### THE CELL

`TX-r-3` -- **activation: the measured first capability read under the named identity, bearer value, prelude on, rollout switch on, live authorized readback.** Held on G-W and G-P; the COO spawns this only when both records exist. G-A is answered (opalbloomberg@opalinvest.com); workbook access is believed but UNMEASURED, and your controlled read is its first measurement. A refused read is a reported result: never widen a guard, substitute an identity or grant access.

**Writes:** the protected `TAXSMA_WORKBOOK_IDENTITY` activation record; the change-management entry and sentinel (the `<paths>` block below is the grant; abbreviations: `GW` = `infra/aws/ec2/opal-gateway`, `GOLD` = `data/mdpf/scripts/gold`, `SILV` = `data/mdpf/scripts/silver`, `TST` = `data/mdpf/tests/taxsma`, `PUB` = `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher`, `GLB` = `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda`, `TFM`/`TFA`/`TFGW` = `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}`, `PSRC` = `portal/src`).

**Read:** `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_180xZ_TAXSMA_WORKBOOK_IDENTITY_OPALBLOOMBERG_AND_ACTIVE_FIELD_MEMBERSHIP.md`; `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_183xZ_TAXSMA_ACCESS_BELIEVED_AND_TRADED_COLUMN_IS_MEMBERSHIP_KEY.md`; `org/missions/D8/MDPF/MDPF_TAXSMA/prd/IDENTITY_ACCESS_PROOF_97190.json`; `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`; and your cell's section of `org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md` (s.3), its bounds (s.8) and its gates (s.6). The PRD and the data contract are the specification; the contract's enumerations are the only vocabulary.

Write `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/activation.result.md` (each value with its instrument, UTC time and denominator). The probe for every mechanical criterion is `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py`, which takes the criterion's short id (`AC1` .. `AC11`), runs or reads the evidence, prints its measurement with vintage and denominator, then exactly one line `VERDICT: PASS-TXR3-AC<n>` or `VERDICT: FAIL-TXR3-AC<n> <reason>`. A "(difference)" criterion runs its engaged and disengaged arms in the same probe run and prints what differed.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="TXR3-AC1" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC1</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC1(?![0-9])</expect></criterion>
`TXR3-AC1` -- the ledger entry cites the G-A record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_180xZ_TAXSMA_WORKBOOK_IDENTITY_OPALBLOOMBERG_AND_ACTIVE_FIELD_MEMBERSHIP.md` @f95470f384 by path@commit

<criterion id="TXR3-AC2" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC2</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC2(?![0-9])</expect></criterion>
`TXR3-AC2` -- `TAXSMA_WORKBOOK_IDENTITY` holds the Entra tid/oid principal of `opalbloomberg@opalinvest.com` in protected configuration, with the email as display metadata, and the approval reference is recorded in protected deploy evidence

<criterion id="TXR3-AC3" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC3</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC3(?![0-9])</expect></criterion>
`TXR3-AC3` -- the never-widen sign-off (CTO and COO) naming both served keys, their writer count and each key's rollback is cited before the rollout switch turns ON (G-W)

<criterion id="TXR3-AC4" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC4</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC4(?![0-9])</expect></criterion>
`TXR3-AC4` -- the compatible consumer is promoted under its applicable authorization before the switch turns ON (G-P), cited

<criterion id="TXR3-AC5" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC5</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC5(?![0-9])</expect></criterion>
`TXR3-AC5` -- the configured tid/oid pair is resolved from the validated Entra principal context and recorded before the controlled read, with an email match alone refused as binding

<criterion id="TXR3-AC6" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC6</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC6(?![0-9])</expect></criterion>
`TXR3-AC6` -- one controlled read through `GET /ms/taxsma-workbook` records the identity binding, the item and the result in protected evidence without rows or tokens

<criterion id="TXR3-AC7" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC7</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC7(?![0-9])</expect></criterion>
`TXR3-AC7` -- the capability is enabled only after that controlled read succeeds; a refused read leaves it disabled and is reported, with no scope or grant change

<criterion id="TXR3-AC8" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC8</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC8(?![0-9])</expect></criterion>
`TXR3-AC8` -- the served 49financial and Global documents, read through the authorized consumer route, carry the Tax leaf with its coverage and dates

<criterion id="TXR3-AC9" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC9</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC9(?![0-9])</expect></criterion>
`TXR3-AC9` -- an unauthorized route control is refused

<criterion id="TXR3-AC10" cell_refs="TX-r-3"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_r_3.py AC10</invocation><expect>(?m)^VERDICT: PASS-TXR3-AC10(?![0-9])</expect></criterion>
`TXR3-AC10` -- the rollback (capability disabled, switch OFF) is exercised once, and the served documents return to the pre-activation shape

<criterion id="TXR3-AC11" cell_refs="TX-r-3" judgment="true"/>
`TXR3-AC11` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9; record the output, give NO verdict -- an operator walkthrough explains one inclusion, one exclusion and one exception from the supporting records

<expected_criteria>TXR3-AC1, TXR3-AC2, TXR3-AC3, TXR3-AC4, TXR3-AC5, TXR3-AC6, TXR3-AC7, TXR3-AC8, TXR3-AC9, TXR3-AC10, TXR3-AC11</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from the COO's working branch at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **No egress off Opal infrastructure.** No call to Microsoft Graph, SharePoint, the live workbook, the live `/ms/taxsma-workbook` route with a real identity, Claude, an Anthropic endpoint or any vendor API. AWS account 313476888478 (us-east-1) is Opal infrastructure.
- **No private data in the repository.** No client name, full account number, balance, token, cookie or delegated credential enters code, fixtures, deliverables or logs. Masked labels and aggregate counts only.
- **Addresses and names from the builders.** Every new S3 key is `lib/opal_naming.py` `address()` output and every new resource name is `name()` output; a secret's path is one `grade(<path>, "SECRET")` returns CONFORMANT for. A builder refusal is a surprise row, never a hand-typed path.
- **Deploy discipline.** A world-changing act opens its change-management entry and commits the OPEN sentinel before the act, then closes and commits the entry before the reads that grade it. Terraform only through `.tools/safe-apply.sh`, never `-target`; the Gateway only through `infra/aws/ec2/safe-ec2-deploy.sh`; never `aws lambda update-function-code`.
- **One Terraform state, one writer.** Apply only the root your order names.
- **No served output moves.** No write to either served `category-views.json` key except as your order names.
- **No new monitor, alarm, SNS, email, watcher, schedule or standing comparator.**
- **No source mutation.** No workbook, BD roster or custodian write; no change to b00; no bucket-policy broadening or firm-fence exemption.
- **No new dependency.** `moto`, `msal`, `vitest`, `jsdom`, `happy-dom` and `@testing-library/react` are absent on this box. Use the standard library, installed packages (`py -3.12` has pandas, pyarrow, boto3, pyyaml, pytest, fastapi, httpx), stubs, `bun` and the installed `playwright` library. A missing instrument is a refusal.
- **D9 is out of scope.** No account opening, margin, money-manager or strategy change, trade, converter change or access grant.
- **Every invocation terminates** (`timeout 120`, or the tool's own budget); a timeout is the recorded output.
- **Commits** go through `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`. No portal DEV or PROD push and no workspace gitlink move.
- **Unknown deployment facts are measured, never presumed.** Assert no deployed state you did not read back.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is ONE surprise row, and you keep working.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Surprises** go to `org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `MDPF_TAXSMA-W6-S<k>`, per the worker definition. Keep working after filing.

<paths>
org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/mdpf_taxsma-tx-r-3.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md</decomp_doc> @7f65001ab3, cell `TX-r-3`, round 1 (section 3).
<owned_cells>TX-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `TXR3-AC1` .. `TXR3-AC11` (11). Instance at
`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/MDPF_TAXSMA.TO-TX-r-3.activation.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `MDPF`, spec_ref.group `OTHER`, spec_ref.doc the PRD @671925aecc, decomp_ref.doc the
decomposition @7f65001ab3, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> TXR3-AC1,TXR3-AC2,TXR3-AC3,TXR3-AC4,TXR3-AC5,TXR3-AC6,TXR3-AC7,TXR3-AC8,TXR3-AC9,TXR3-AC10,TXR3-AC11`
BEFORE the `complete` flip. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a
row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 1800, 5 of 5 carriers scanned (C1 345, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming MDPF_TAXSMA; self-test PASS 6/6. This project registers G-R, G-S, G-O, G-A, G-W, G-P and notices N-1, N-2 (decomposition s.6).
comp-iam: RUN at L5 -- DESIRED plane, 472 .tf files scanned; mdpf-gold-lambda-role 11 statements, none on opal-data-49financial; publisher role 7 operations, 6 UNRESOLVABLE-RESOURCE, 1 GRANTED-ACTION/UNGRANTED-RESOURCE; 26 policy blocks NOT ATTACHED and 2 deny statements unparsed (deny-blind).
comp-adversary: RUN at L5 on the PRD v0.5 -- 19 of 19 cited commits verified; 38 cited paths, 30 stable, 8 GONE, all 8 the PRD's own PROPOSED_NEW paths. Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); the deliverables folder is granted by convention.
</preflight>

Seating: slot ~6, queue position 4. Round 1 of MDPF_TAXSMA, issued by `2.0.0_SA_COO~T`, seated by `0.0.0_AB_MSTR` (msg 97080,
LD-0569) on Andrew's seat order ~12:5xZ 2026-09-15. Decomposition @7f65001ab3. HELD at issuance on G-W,G-P.
