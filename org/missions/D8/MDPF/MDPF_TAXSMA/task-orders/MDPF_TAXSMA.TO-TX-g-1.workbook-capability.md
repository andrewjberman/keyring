# TO MDPF_TAXSMA.TO-TX-g-1 -- the `GET /ms/taxsma-workbook` capability module, its route registration and configuration keys, with unit tests

<to_id>MDPF_TAXSMA.TO-TX-g-1</to_id>
<project>MDPF_TAXSMA</project>
<issued_to>0.9.0_WK_MDPF_TAXSMA~1</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @671925aecc (ADMITTED) | **Contract:** `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` | **Decomp cell:** `TX-g-1` | **serves:** FWD-7 (S01) | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`TX-g-1` -- **the `GET /ms/taxsma-workbook` capability module, its route registration and configuration keys, with unit tests.** `GW/app/server.py` is being rewritten by NFRA_OPLGTW workers in parallel (it moved twice during this project's L5). Edit ONLY the route registration you need, as a small hunk; the COO merges it at the drain.

**Writes:** `GW/app/taxsma_workbook.py` (new), `GW/app/server.py` (route registration only), `GW/app/config.py` (the two configuration keys only), `GW/tests/test_taxsma_workbook.py` (new) (the `<paths>` block below is the grant; abbreviations: `GW` = `infra/aws/ec2/opal-gateway`, `GOLD` = `data/mdpf/scripts/gold`, `SILV` = `data/mdpf/scripts/silver`, `TST` = `data/mdpf/tests/taxsma`, `PUB` = `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher`, `GLB` = `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda`, `TFM`/`TFA`/`TFGW` = `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}`, `PSRC` = `portal/src`).

**One entries-only edit outside your module.** `infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py` asserts at :542 that its hand-written `ROUTE_CLASS` dict (:487) names every route `app.server` serves (NFRA_OPLGTW `OG-a-2`, on CLOUD since @7459929520). Add exactly ONE `ROUTE_CLASS` entry for `/ms/taxsma-workbook`, carrying its REAL guard class as your code enforces it (the file's `capability` class: a capability route answers 401 to an access token), and change nothing else in that file. That module imports `moto` (:35), which this box lacks, so it is NOT-EVALUATED here (row MDPF_TAXSMA-S2); the entry keeps it green where it runs. Row MDPF_TAXSMA-S3 records why this path is in your grant.

**Read:** `infra/aws/ec2/opal-gateway/app/ms_ingest.py`; `infra/aws/ec2/opal-gateway/app/token_broker.py`; `infra/aws/ec2/opal-gateway/app/audit.py`; `infra/aws/ec2/opal-gateway/app/server.py`; `infra/aws/ec2/opal-gateway/app/config.py`; `infra/aws/ec2/opal-gateway/app/identity.py`; `infra/aws/ec2/opal-gateway/tests/conftest.py`; `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`; `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`; and your cell's section of `org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md` (s.3), its bounds (s.8) and its gates (s.6). The PRD and the data contract are the specification; the contract's enumerations are the only vocabulary.

Write `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/workbook-capability.result.md` (each value with its instrument, UTC time and denominator). The probe for every mechanical criterion is `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py`, which takes the criterion's short id (`AC1` .. `AC23`), runs or reads the evidence, prints its measurement with vintage and denominator, then exactly one line `VERDICT: PASS-TXG1-AC<n>` or `VERDICT: FAIL-TXG1-AC<n> <reason>`. A "(difference)" criterion runs its engaged and disengaged arms in the same probe run and prints what differed.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="TXG1-AC1" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC1</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC1(?![0-9])</expect></criterion>
`TXG1-AC1` -- a GET with the configured capability bearer against a synthetic Graph worksheet returns exactly the contract's `capability.response_fields`

<criterion id="TXG1-AC2" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC2</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC2(?![0-9])</expect></criterion>
`TXG1-AC2` -- every returned row carries exactly the seven `projected_columns` plus the three `row_metadata` fields

<criterion id="TXG1-AC3" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC3</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC3(?![0-9])</expect></criterion>
`TXG1-AC3` -- (difference) the same request with the bearer absent, wrong, or valid only for another route returns UNAUTHORIZED_CAPABILITY, while the correct bearer on the same test client returns 200

<criterion id="TXG1-AC4" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC4</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC4(?![0-9])</expect></criterion>
`TXG1-AC4` -- a non-GET method on the route is refused

<criterion id="TXG1-AC5" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC5</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC5(?![0-9])</expect></criterion>
`TXG1-AC5` -- a caller-supplied site, item, sheet, range, URL, identity or query parameter is refused and never forwarded to Graph (each selector enumerated)

<criterion id="TXG1-AC6" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC6</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC6(?![0-9])</expect></criterion>
`TXG1-AC6` -- the capability bearer is refused on every other Gateway route in the same test client

<criterion id="TXG1-AC7" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC7</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC7(?![0-9])</expect></criterion>
`TXG1-AC7` -- with `TAXSMA_WORKBOOK_IDENTITY` unset, the route returns AUTH_REQUIRED and makes no Graph call

<criterion id="TXG1-AC8" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC8</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC8(?![0-9])</expect></criterion>
`TXG1-AC8` -- (difference) with the same email and otherwise identical valid inputs, a principal whose tid alone differs from the configured pair yields AUTH_REQUIRED with zero token fetches and zero Graph requests, while the configured pair returns 200

<criterion id="TXG1-AC9" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC9</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC9(?![0-9])</expect></criterion>
`TXG1-AC9` -- (difference) with the same email and otherwise identical valid inputs, a principal whose oid alone differs from the configured pair yields AUTH_REQUIRED with zero token fetches and zero Graph requests, while the configured pair returns 200

<criterion id="TXG1-AC10" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC10</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC10(?![0-9])</expect></criterion>
`TXG1-AC10` -- a missing, unvalidated or caller-supplied tid/oid pair yields AUTH_REQUIRED before any token fetch

<criterion id="TXG1-AC11" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC11</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC11(?![0-9])</expect></criterion>
`TXG1-AC11` -- a generic MCP, ms-ingest or OTP credential presented to the route yields UNAUTHORIZED_CAPABILITY

<criterion id="TXG1-AC12" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC12</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC12(?![0-9])</expect></criterion>
`TXG1-AC12` -- a request to `/ms/taxsma-workbook` passes the route's own guard before any generic `/ms/*` handler runs (call-order assertion in the test client)

<criterion id="TXG1-AC13" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC13</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC13(?![0-9])</expect></criterion>
`TXG1-AC13` -- the audit record carries the principal's tid/oid reference, with the email as display metadata only

<criterion id="TXG1-AC14" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC14</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC14(?![0-9])</expect></criterion>
`TXG1-AC14` -- a NeedsLogin or revoked result from the token broker yields AUTH_REQUIRED, never an empty 200

<criterion id="TXG1-AC15" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC15</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC15(?![0-9])</expect></criterion>
`TXG1-AC15` -- a synthetic Graph permission denial on the item maps to one contract error code, recorded in the audit record as distinct from a Gateway guard refusal

<criterion id="TXG1-AC16" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC16</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC16(?![0-9])</expect></criterion>
`TXG1-AC16` -- an ETag change between the before and after reads beyond `etag_change_retries` yields SOURCE_CHANGED

<criterion id="TXG1-AC17" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC17</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC17(?![0-9])</expect></criterion>
`TXG1-AC17` -- a used range over `max_used_rows_including_header` yields SOURCE_TOO_LARGE with the observed extent, never a truncated `complete: true`

<criterion id="TXG1-AC18" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC18</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC18(?![0-9])</expect></criterion>
`TXG1-AC18` -- a duplicate or ambiguous expected header yields SOURCE_SCHEMA_INVALID

<criterion id="TXG1-AC19" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC19</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC19(?![0-9])</expect></criterion>
`TXG1-AC19` -- a nonempty unrecognized row is returned with `row_kind` UNRECOGNIZED, never dropped

<criterion id="TXG1-AC20" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC20</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC20(?![0-9])</expect></criterion>
`TXG1-AC20` -- across every test case, no response or audit record contains a prohibited field (Name, Advisor Contact, AUM (Mn), Divest Securities, Instruction, Comment, or any token), each enumerated

<criterion id="TXG1-AC21" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC21</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC21(?![0-9])</expect></criterion>
`TXG1-AC21` -- every call writes one audit record carrying exactly `capability.audit_fields` and none of `capability.audit_exclusions`

<criterion id="TXG1-AC22" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC22</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC22(?![0-9])</expect></criterion>
`TXG1-AC22` -- the Gateway test modules that collected and passed before the edit still do, count printed before and after (the two `moto`-dependent modules named as NOT-EVALUATED on this box)

<criterion id="TXG1-AC23" cell_refs="TX-g-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py AC23</invocation><expect>(?m)^VERDICT: PASS-TXG1-AC23(?![0-9])</expect></criterion>
`TXG1-AC23` -- the tests add no dependency (no `moto`; the token broker and Graph are stubbed)

<expected_criteria>TXG1-AC1, TXG1-AC2, TXG1-AC3, TXG1-AC4, TXG1-AC5, TXG1-AC6, TXG1-AC7, TXG1-AC8, TXG1-AC9, TXG1-AC10, TXG1-AC11, TXG1-AC12, TXG1-AC13, TXG1-AC14, TXG1-AC15, TXG1-AC16, TXG1-AC17, TXG1-AC18, TXG1-AC19, TXG1-AC20, TXG1-AC21, TXG1-AC22, TXG1-AC23</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
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
- **Surprises** go to `org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `MDPF_TAXSMA-W1-S<k>`, per the worker definition. Keep working after filing.

<paths>
infra/aws/ec2/opal-gateway/app/taxsma_workbook.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/tests/test_taxsma_workbook.py
infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py
org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md</decomp_doc> @7f65001ab3, cell `TX-g-1`, round 1 (section 3).
<owned_cells>TX-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `TXG1-AC1` .. `TXG1-AC23` (23). Instance at
`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~1/MDPF_TAXSMA.TO-TX-g-1.workbook-capability.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `MDPF`, spec_ref.group `OTHER`, spec_ref.doc the PRD @671925aecc, decomp_ref.doc the
decomposition @7f65001ab3, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> TXG1-AC1,TXG1-AC2,TXG1-AC3,TXG1-AC4,TXG1-AC5,TXG1-AC6,TXG1-AC7,TXG1-AC8,TXG1-AC9,TXG1-AC10,TXG1-AC11,TXG1-AC12,TXG1-AC13,TXG1-AC14,TXG1-AC15,TXG1-AC16,TXG1-AC17,TXG1-AC18,TXG1-AC19,TXG1-AC20,TXG1-AC21,TXG1-AC22,TXG1-AC23`
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

Seating: slot ~1, queue position 1. Round 1 of MDPF_TAXSMA, issued by `2.0.0_SA_COO~T`, seated by `0.0.0_AB_MSTR` (msg 97080,
LD-0569) on Andrew's seat order ~12:5xZ 2026-09-15. Decomposition @7f65001ab3.
Amended before spawn by `2.0.0_SA_COO~T`: one entries-only path (`tests/test_principal_cutover.py`, a single ROUTE_CLASS line) added to <paths> on 2.0.0_SA_COO~O's 97236; row MDPF_TAXSMA-S3. No criterion changed.
