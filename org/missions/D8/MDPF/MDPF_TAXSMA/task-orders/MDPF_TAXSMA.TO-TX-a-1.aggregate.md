# TO MDPF_TAXSMA.TO-TX-a-1 -- the Tax contribution in the firm and Global aggregate series

<to_id>MDPF_TAXSMA.TO-TX-a-1</to_id>
<project>MDPF_TAXSMA</project>
<issued_to>0.9.0_WK_MDPF_TAXSMA~2</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @671925aecc (ADMITTED) | **Contract:** `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` | **Decomp cell:** `TX-a-1` | **serves:** FWD-6 (S06) | **slot:** ~2, queue position 6

---

## WORKER FACE

### THE CELL

`TX-a-1` -- **the Tax contribution in the firm and Global aggregate series.** Client and every other firm's figures must not move.

**Writes:** `GOLD/dim_mdpf_aggregate_aua_timeseries.py`, `TST/test_taxsma_aggregate.py` (new) (the `<paths>` block below is the grant; abbreviations: `GW` = `infra/aws/ec2/opal-gateway`, `GOLD` = `data/mdpf/scripts/gold`, `SILV` = `data/mdpf/scripts/silver`, `TST` = `data/mdpf/tests/taxsma`, `PUB` = `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher`, `GLB` = `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda`, `TFM`/`TFA`/`TFGW` = `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}`, `PSRC` = `portal/src`).

**Read:** `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`; `data/mdpf/scripts/gold/mdpf_category_registry.py`; `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`; and your cell's section of `org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md` (s.3), its bounds (s.8) and its gates (s.6). The PRD and the data contract are the specification; the contract's enumerations are the only vocabulary.

Write `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/aggregate.result.md` (each value with its instrument, UTC time and denominator). The probe for every mechanical criterion is `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py`, which takes the criterion's short id (`AC1` .. `AC10`), runs or reads the evidence, prints its measurement with vintage and denominator, then exactly one line `VERDICT: PASS-TXA1-AC<n>` or `VERDICT: FAIL-TXA1-AC<n> <reason>`. A "(difference)" criterion runs its engaged and disengaged arms in the same probe run and prints what differed.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="TXA1-AC1" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC1</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC1(?![0-9])</expect></criterion>
`TXA1-AC1` -- changed 49financial and Global series carry `aggregate_basis` INCLUDES_ADDITIVE, `base_excluding_tax_aua`, `tax_additive_aua` and `tax_coverage`, each aligned to `dates`

<criterion id="TXA1-AC2" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC2</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC2(?![0-9])</expect></criterion>
`TXA1-AC2` -- with a fixed synthetic baseline and known Tax cents, Tax is added exactly once at Tax, SMA, ALT Strategies and 49financial

<criterion id="TXA1-AC3" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC3</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC3(?![0-9])</expect></criterion>
`TXA1-AC3` -- Global's Tax equals the sum of firm Tax leaves, and Global's total adds Tax exactly once

<criterion id="TXA1-AC4" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC4</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC4(?![0-9])</expect></criterion>
`TXA1-AC4` -- Client and every other firm's series are byte-equal to the same inputs' run without the change

<criterion id="TXA1-AC5" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC5</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC5(?![0-9])</expect></criterion>
`TXA1-AC5` -- `source_basis` survives the Global fixed-key and reconstruction path for `tax`

<criterion id="TXA1-AC6" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC6</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC6(?![0-9])</expect></criterion>
`TXA1-AC6` -- (difference) a TAXSMA path missing the `aggregate_basis` declaration is a schema failure, while the declared path in the same harness succeeds

<criterion id="TXA1-AC7" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC7</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC7(?![0-9])</expect></criterion>
`TXA1-AC7` -- (difference) an overlapping full ID blocks the affected total, while the same fixture without the overlap completes

<criterion id="TXA1-AC8" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC8</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC8(?![0-9])</expect></criterion>
`TXA1-AC8` -- unknown or stale Tax makes the SMA, ALT Strategies, 49financial and dependent Global complete totals null with coverage, while unaffected firms keep their values

<criterion id="TXA1-AC9" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC9</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC9(?![0-9])</expect></criterion>
`TXA1-AC9` -- Tax coverage carries `business_active_accounts` and the dated expected, covered and unresolved counts as separate fields, each with its own date

<criterion id="TXA1-AC10" cell_refs="TX-a-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_a_1.py AC10</invocation><expect>(?m)^VERDICT: PASS-TXA1-AC10(?![0-9])</expect></criterion>
`TXA1-AC10` -- the same-vintage before and after arithmetic control is recorded with its input hashes

<expected_criteria>TXA1-AC1, TXA1-AC2, TXA1-AC3, TXA1-AC4, TXA1-AC5, TXA1-AC6, TXA1-AC7, TXA1-AC8, TXA1-AC9, TXA1-AC10</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
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
- **Surprises** go to `org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `MDPF_TAXSMA-W2-S<k>`, per the worker definition. Keep working after filing.

<paths>
data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
data/mdpf/tests/taxsma/test_taxsma_aggregate.py
org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md</decomp_doc> @7f65001ab3, cell `TX-a-1`, round 1 (section 3).
<owned_cells>TX-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `TXA1-AC1` .. `TXA1-AC10` (10). Instance at
`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/MDPF_TAXSMA.TO-TX-a-1.aggregate.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `MDPF`, spec_ref.group `OTHER`, spec_ref.doc the PRD @671925aecc, decomp_ref.doc the
decomposition @7f65001ab3, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> TXA1-AC1,TXA1-AC2,TXA1-AC3,TXA1-AC4,TXA1-AC5,TXA1-AC6,TXA1-AC7,TXA1-AC8,TXA1-AC9,TXA1-AC10`
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

Seating: slot ~2, queue position 6. Round 1 of MDPF_TAXSMA, issued by `2.0.0_SA_COO~T`, seated by `0.0.0_AB_MSTR` (msg 97080,
LD-0569) on Andrew's seat order ~12:5xZ 2026-09-15. Decomposition @7f65001ab3.
