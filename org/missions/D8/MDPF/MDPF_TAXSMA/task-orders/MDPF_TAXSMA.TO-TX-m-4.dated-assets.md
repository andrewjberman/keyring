# TO MDPF_TAXSMA.TO-TX-m-4 -- dated account observations and the correction ledger

<to_id>MDPF_TAXSMA.TO-TX-m-4</to_id>
<project>MDPF_TAXSMA</project>
<issued_to>0.9.0_WK_MDPF_TAXSMA~2</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @671925aecc (ADMITTED) | **Contract:** `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` | **Decomp cell:** `TX-m-4` | **serves:** FWD-3, 4, 5, 8 (S05) | **slot:** ~2, queue position 5

---

## WORKER FACE

### THE CELL

`TX-m-4` -- **dated account observations and the correction ledger.** b00 is read, never changed.

**Writes:** `GOLD/taxsma_assets.py` (new), `TST/test_taxsma_assets.py` (new) (the `<paths>` block below is the grant; abbreviations: `GW` = `infra/aws/ec2/opal-gateway`, `GOLD` = `data/mdpf/scripts/gold`, `SILV` = `data/mdpf/scripts/silver`, `TST` = `data/mdpf/tests/taxsma`, `PUB` = `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher`, `GLB` = `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda`, `TFM`/`TFA`/`TFGW` = `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}`, `PSRC` = `portal/src`).

**Read:** `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`; `data/assets/scripts/gold/runners_49f/b00_canonical_valuation.py`; `data/mdpf/scripts/gold/mdpf_category_registry.py`; `lib/opal_naming.py`; and your cell's section of `org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md` (s.3), its bounds (s.8) and its gates (s.6). The PRD and the data contract are the specification; the contract's enumerations are the only vocabulary.

Write `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/dated-assets.result.md` (each value with its instrument, UTC time and denominator). The probe for every mechanical criterion is `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py`, which takes the criterion's short id (`AC1` .. `AC21`), runs or reads the evidence, prints its measurement with vintage and denominator, then exactly one line `VERDICT: PASS-TXM4-AC<n>` or `VERDICT: FAIL-TXM4-AC<n> <reason>`. A "(difference)" criterion runs its engaged and disengaged arms in the same probe run and prints what differed.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="TXM4-AC1" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC1</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC1(?![0-9])</expect></criterion>
`TXM4-AC1` -- every observation row carries exactly the contract's `valuation.history_fields`, `membership_date_basis` and `membership_source_event_id` included

<criterion id="TXM4-AC2" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC2</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC2(?![0-9])</expect></criterion>
`TXM4-AC2` -- values join b00 `canonical_valuation` on `account_id` and `business_date` and equal `net_mv_plus_cash` to the cent under decimal128(20,2), over a fixture with cash, long and short exposure, margin and an actual zero

<criterion id="TXM4-AC3" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC3</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC3(?![0-9])</expect></criterion>
`TXM4-AC3` -- a missing canonical row yields CANONICAL_MISSING and an explicit unavailable row, never zero

<criterion id="TXM4-AC4" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC4</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC4(?![0-9])</expect></criterion>
`TXM4-AC4` -- a duplicate canonical row yields CANONICAL_DUPLICATE

<criterion id="TXM4-AC5" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC5</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC5(?![0-9])</expect></criterion>
`TXM4-AC5` -- each of the contract's `rejected_substitutes`, supplied as an input, is unused (each enumerated)

<criterion id="TXM4-AC6" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC6</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC6(?![0-9])</expect></criterion>
`TXM4-AC6` -- `covered_accounts` counts only rows passing identity, observed membership, source date and value checks, while `expected_accounts` is computed before those filters

<criterion id="TXM4-AC7" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC7</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC7(?![0-9])</expect></criterion>
`TXM4-AC7` -- wherever `expected_accounts` is known, `covered_accounts` + `unresolved_accounts` equals it

<criterion id="TXM4-AC8" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC8</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC8(?![0-9])</expect></criterion>
`TXM4-AC8` -- a live claim with no custodian record is counted in `unresolved_accounts` with MISSING_CUSTODIAN and is never dropped

<criterion id="TXM4-AC9" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC9</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC9(?![0-9])</expect></criterion>
`TXM4-AC9` -- a valuation date before trustworthy membership history yields TRADED_HISTORY_UNVERIFIED and no covered value, never a zero

<criterion id="TXM4-AC10" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC10</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC10(?![0-9])</expect></criterion>
`TXM4-AC10` -- membership intervals are compared to `valuation_date` as ISO calendar dates, start <= valuation_date < end, never through an exchange-local timestamp

<criterion id="TXM4-AC11" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC11</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC11(?![0-9])</expect></criterion>
`TXM4-AC11` -- `business_active_accounts` is carried into Gold from S03 unchanged and is never derived from covered rows

<criterion id="TXM4-AC12" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC12</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC12(?![0-9])</expect></criterion>
`TXM4-AC12` -- (difference) with one expected claim unresolved `complete_value` is null with reasons, while resolving it in the same harness populates `complete_value`

<criterion id="TXM4-AC13" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC13</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC13(?![0-9])</expect></criterion>
`TXM4-AC13` -- an unknown denominator is `expected_accounts` null with its reason, never 0 of 0

<criterion id="TXM4-AC14" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC14</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC14(?![0-9])</expect></criterion>
`TXM4-AC14` -- `observation_id` is stable across two runs with different run UUIDs and clocks

<criterion id="TXM4-AC15" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC15</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC15(?![0-9])</expect></criterion>
`TXM4-AC15` -- `observation_id` changes when the S03 event it rests on changes, and not otherwise

<criterion id="TXM4-AC16" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC16</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC16(?![0-9])</expect></criterion>
`TXM4-AC16` -- (difference) identical knowledge on an existing date partition is NO_CHANGE, while changed knowledge on the same date enters pending control state for the next date and mints no second leaf

<criterion id="TXM4-AC17" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC17</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC17(?![0-9])</expect></criterion>
`TXM4-AC17` -- a correction carries `supersedes_observation_id`, and the reader resolves an acyclic chain

<criterion id="TXM4-AC18" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC18</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC18(?![0-9])</expect></criterion>
`TXM4-AC18` -- the reader refuses competing corrections, duplicate ids with different payloads and a missing superseded observation

<criterion id="TXM4-AC19" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC19</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC19(?![0-9])</expect></criterion>
`TXM4-AC19` -- a correction-only partition does not reduce the resolved cohort (reader test across three partitions)

<criterion id="TXM4-AC20" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC20</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC20(?![0-9])</expect></criterion>
`TXM4-AC20` -- the source basis is derived as ADDITIVE and validated against `GOLD/mdpf_category_registry.py` (key `tax`, `SMA_BASIS_ADDITIVE`), and a mismatch refuses the contribution with BASIS_MISMATCH

<criterion id="TXM4-AC21" cell_refs="TX-m-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_4.py AC21</invocation><expect>(?m)^VERDICT: PASS-TXM4-AC21(?![0-9])</expect></criterion>
`TXM4-AC21` -- the Gold key is computed only by `address("mdpf","49financial","gold","taxsma_assets","date=<knowledge_date>","data.parquet")`

<expected_criteria>TXM4-AC1, TXM4-AC2, TXM4-AC3, TXM4-AC4, TXM4-AC5, TXM4-AC6, TXM4-AC7, TXM4-AC8, TXM4-AC9, TXM4-AC10, TXM4-AC11, TXM4-AC12, TXM4-AC13, TXM4-AC14, TXM4-AC15, TXM4-AC16, TXM4-AC17, TXM4-AC18, TXM4-AC19, TXM4-AC20, TXM4-AC21</expected_criteria>

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
data/mdpf/scripts/gold/taxsma_assets.py
data/mdpf/tests/taxsma/test_taxsma_assets.py
org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md</decomp_doc> @7f65001ab3, cell `TX-m-4`, round 1 (section 3).
<owned_cells>TX-m-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `TXM4-AC1` .. `TXM4-AC21` (21). Instance at
`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/MDPF_TAXSMA.TO-TX-m-4.dated-assets.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `MDPF`, spec_ref.group `OTHER`, spec_ref.doc the PRD @671925aecc, decomp_ref.doc the
decomposition @7f65001ab3, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> TXM4-AC1,TXM4-AC2,TXM4-AC3,TXM4-AC4,TXM4-AC5,TXM4-AC6,TXM4-AC7,TXM4-AC8,TXM4-AC9,TXM4-AC10,TXM4-AC11,TXM4-AC12,TXM4-AC13,TXM4-AC14,TXM4-AC15,TXM4-AC16,TXM4-AC17,TXM4-AC18,TXM4-AC19,TXM4-AC20,TXM4-AC21`
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

Seating: slot ~2, queue position 5. Round 1 of MDPF_TAXSMA, issued by `2.0.0_SA_COO~T`, seated by `0.0.0_AB_MSTR` (msg 97080,
LD-0569) on Andrew's seat order ~12:5xZ 2026-09-15. Decomposition @7f65001ab3.
