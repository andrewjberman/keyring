# TO MDPF_TAXSMA.TO-TX-v-2 -- the local controlled journey harness, producer end

<to_id>MDPF_TAXSMA.TO-TX-v-2</to_id>
<project>MDPF_TAXSMA</project>
<issued_to>0.9.0_WK_MDPF_TAXSMA~5</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @671925aecc (ADMITTED) | **Contract:** `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` | **Decomp cell:** `TX-v-2` | **serves:** FWD-1 .. FWD-8 (S14) | **slot:** ~5, queue position 2

---

## WORKER FACE

### THE CELL

`TX-v-2` -- **the local controlled journey harness, producer end.** Local artifacts only; network calls blocked.

**Writes:** `TST/test_taxsma_journey.py` (new), `TST/fixtures/**` (new) (the `<paths>` block below is the grant; abbreviations: `GW` = `infra/aws/ec2/opal-gateway`, `GOLD` = `data/mdpf/scripts/gold`, `SILV` = `data/mdpf/scripts/silver`, `TST` = `data/mdpf/tests/taxsma`, `PUB` = `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher`, `GLB` = `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda`, `TFM`/`TFA`/`TFGW` = `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}`, `PSRC` = `portal/src`).

**Read:** `data/mdpf/tests/taxsma/expected_cases.json`; `data/mdpf/tests/taxsma/`; `data/mdpf/scripts/gold/`; `data/mdpf/scripts/silver/`; `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py`; `infra/aws/ec2/opal-gateway/app/taxsma_workbook.py`; and your cell's section of `org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md` (s.3), its bounds (s.8) and its gates (s.6). The PRD and the data contract are the specification; the contract's enumerations are the only vocabulary.

Write `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/journey-harness.result.md` (each value with its instrument, UTC time and denominator). The probe for every mechanical criterion is `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py`, which takes the criterion's short id (`AC1` .. `AC8`), runs or reads the evidence, prints its measurement with vintage and denominator, then exactly one line `VERDICT: PASS-TXV2-AC<n>` or `VERDICT: FAIL-TXV2-AC<n> <reason>`. A "(difference)" criterion runs its engaged and disengaged arms in the same probe run and prints what differed.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="TXV2-AC1" cell_refs="TX-v-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py AC1</invocation><expect>(?m)^VERDICT: PASS-TXV2-AC1(?![0-9])</expect></criterion>
`TXV2-AC1` -- the harness runs a synthetic Gateway through S02, S19, S03, S04, S05, S06, S07 and S08 against local artifacts only, with network calls blocked and the block asserted

<criterion id="TXV2-AC2" cell_refs="TX-v-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py AC2</invocation><expect>(?m)^VERDICT: PASS-TXV2-AC2(?![0-9])</expect></criterion>
`TXV2-AC2` -- before any overall verdict, the harness prints expected, executed, missing and extra case counts against `expected_cases.json`

<criterion id="TXV2-AC3" cell_refs="TX-v-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py AC3</invocation><expect>(?m)^VERDICT: PASS-TXV2-AC3(?![0-9])</expect></criterion>
`TXV2-AC3` -- every A01-A08 arm executes and its observed result matches the expected observable in `expected_cases.json` (per-arm table)

<criterion id="TXV2-AC4" cell_refs="TX-v-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py AC4</invocation><expect>(?m)^VERDICT: PASS-TXV2-AC4(?![0-9])</expect></criterion>
`TXV2-AC4` -- each control arm runs engaged and disengaged in the same harness run and records what differed

<criterion id="TXV2-AC5" cell_refs="TX-v-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py AC5</invocation><expect>(?m)^VERDICT: PASS-TXV2-AC5(?![0-9])</expect></criterion>
`TXV2-AC5` -- input, fixture and output SHA-256 are recorded for every arm with the commit the harness ran at

<criterion id="TXV2-AC6" cell_refs="TX-v-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py AC6</invocation><expect>(?m)^VERDICT: PASS-TXV2-AC6(?![0-9])</expect></criterion>
`TXV2-AC6` -- a scan of every output and captured log finds no synthetic full account key outside the protected fixture files

<criterion id="TXV2-AC7" cell_refs="TX-v-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py AC7</invocation><expect>(?m)^VERDICT: PASS-TXV2-AC7(?![0-9])</expect></criterion>
`TXV2-AC7` -- the A07 route controls (wrong identity, wrong route, wrong method, wrong bearer, other workbook, denied or revoked access) fail against the Gateway app test client, while the exact named-identity and exact-route control succeeds and is audited

<criterion id="TXV2-AC8" cell_refs="TX-v-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/probes/tx_v_2.py AC8</invocation><expect>(?m)^VERDICT: PASS-TXV2-AC8(?![0-9])</expect></criterion>
`TXV2-AC8` -- a Gateway guard refusal and a Graph permission denial are recorded as two distinct results

<expected_criteria>TXV2-AC1, TXV2-AC2, TXV2-AC3, TXV2-AC4, TXV2-AC5, TXV2-AC6, TXV2-AC7, TXV2-AC8</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
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
- **Surprises** go to `org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `MDPF_TAXSMA-W5-S<k>`, per the worker definition. Keep working after filing.

<paths>
data/mdpf/tests/taxsma/test_taxsma_journey.py
data/mdpf/tests/taxsma/fixtures/
org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md</decomp_doc> @7f65001ab3, cell `TX-v-2`, round 1 (section 3).
<owned_cells>TX-v-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `TXV2-AC1` .. `TXV2-AC8` (8). Instance at
`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~5/MDPF_TAXSMA.TO-TX-v-2.journey-harness.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `MDPF`, spec_ref.group `OTHER`, spec_ref.doc the PRD @671925aecc, decomp_ref.doc the
decomposition @7f65001ab3, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> TXV2-AC1,TXV2-AC2,TXV2-AC3,TXV2-AC4,TXV2-AC5,TXV2-AC6,TXV2-AC7,TXV2-AC8`
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

Seating: slot ~5, queue position 2. Round 1 of MDPF_TAXSMA, issued by `2.0.0_SA_COO~T`, seated by `0.0.0_AB_MSTR` (msg 97080,
LD-0569) on Andrew's seat order ~12:5xZ 2026-09-15. Decomposition @7f65001ab3.
