# TO MDPF_TAXSMA.TO-TX-m-1 -- business status and effective-membership history from Silver

<to_id>MDPF_TAXSMA.TO-TX-m-1</to_id>
<project>MDPF_TAXSMA</project>
<issued_to>0.9.0_WK_MDPF_TAXSMA~2</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @671925aecc (ADMITTED) | **Contract:** `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` | **Decomp cell:** `TX-m-1` | **serves:** FWD-1, 3 (S03) | **slot:** ~2, queue position 3

---

## WORKER FACE

### THE CELL

`TX-m-1` -- **business status and effective-membership history from Silver.** Synthetic fixtures only.

**Writes:** `GOLD/taxsma_membership.py` (new), `TST/test_taxsma_membership.py` (new) (the `<paths>` block below is the grant; abbreviations: `GW` = `infra/aws/ec2/opal-gateway`, `GOLD` = `data/mdpf/scripts/gold`, `SILV` = `data/mdpf/scripts/silver`, `TST` = `data/mdpf/tests/taxsma`, `PUB` = `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher`, `GLB` = `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda`, `TFM`/`TFA`/`TFGW` = `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}`, `PSRC` = `portal/src`).

**Read:** `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`; `lib/opal_naming.py`; and your cell's section of `org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md` (s.3), its bounds (s.8) and its gates (s.6). The PRD and the data contract are the specification; the contract's enumerations are the only vocabulary.

Write `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/membership.result.md` (each value with its instrument, UTC time and denominator). The probe for every mechanical criterion is `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py`, which takes the criterion's short id (`AC1` .. `AC23`), runs or reads the evidence, prints its measurement with vintage and denominator, then exactly one line `VERDICT: PASS-TXM1-AC<n>` or `VERDICT: FAIL-TXM1-AC<n> <reason>`. A "(difference)" criterion runs its engaged and disengaged arms in the same probe run and prints what differed.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="TXM1-AC1" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC1</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC1(?![0-9])</expect></criterion>
`TXM1-AC1` -- the module reads only the S19 Silver parquet and its metadata; a harness with the Bronze object deleted still classifies

<criterion id="TXM1-AC2" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC2</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC2(?![0-9])</expect></criterion>
`TXM1-AC2` -- a full-sheet fixture (traded, funded-but-untraded, prospect, blank, total, conflicting) places each row in exactly one `business_status`, with a count per population printed

<criterion id="TXM1-AC3" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC3</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC3(?![0-9])</expect></criterion>
`TXM1-AC3` -- Traded is parsed by trim and casefold into YES, NO or blank, and every other value is INVALID (each enumerated in the fixture)

<criterion id="TXM1-AC4" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC4</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC4(?![0-9])</expect></criterion>
`TXM1-AC4` -- (difference) flipping only Traded from No to Yes on one row raises `business_active_accounts` by one, while changing only Ready or a funded balance on the same row leaves it unchanged

<criterion id="TXM1-AC5" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC5</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC5(?![0-9])</expect></criterion>
`TXM1-AC5` -- `business_active_accounts` counts distinct validated full keys with Traded=YES, and the module reads no custodian, master, BD enrollment or value source (call-site census)

<criterion id="TXM1-AC6" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC6</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC6(?![0-9])</expect></criterion>
`TXM1-AC6` -- two rows carrying one full key count once in `business_active_accounts`, and both rows carry CONFLICT

<criterion id="TXM1-AC7" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC7</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC7(?![0-9])</expect></criterion>
`TXM1-AC7` -- a YES row without a valid full identity stays CONFLICT with its YES claim retained, never PROSPECT

<criterion id="TXM1-AC8" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC8</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC8(?![0-9])</expect></criterion>
`TXM1-AC8` -- an invalid identity on a YES claim, an unknown Traded on an identified account and a nonempty unrecognized row each make `business_active_accounts` null with a reason, never a smaller number (each arm enumerated)

<criterion id="TXM1-AC9" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC9</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC9(?![0-9])</expect></criterion>
`TXM1-AC9` -- a source or Traded-schema failure makes the current count null with last-good freshness, never an empty census

<criterion id="TXM1-AC10" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC10</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC10(?![0-9])</expect></criterion>
`TXM1-AC10` -- a YES first observed at UTC time T opens an OBSERVE_TRADED interval inclusive from date(T), with `membership_date_basis` FIRST_OBSERVED_UTC and the S03 service actor

<criterion id="TXM1-AC11" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC11</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC11(?![0-9])</expect></criterion>
`TXM1-AC11` -- (difference) an explicit NO observed on date D closes the interval exclusively on D, while a missing, invalid or disappeared row on D leaves it open

<criterion id="TXM1-AC12" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC12</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC12(?![0-9])</expect></criterion>
`TXM1-AC12` -- a NO-to-YES change opens a new interval and keeps the earlier one

<criterion id="TXM1-AC13" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC13</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC13(?![0-9])</expect></criterion>
`TXM1-AC13` -- an earlier Inception Date, Last Trade Date or `source_modified_at` never moves an interval's start (fixture with each set earlier)

<criterion id="TXM1-AC14" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC14</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC14(?![0-9])</expect></criterion>
`TXM1-AC14` -- an observation at 2026-09-16T00:30Z opens or closes its interval on 2026-09-16, the UTC date, never on the exchange-local 2026-09-15

<criterion id="TXM1-AC15" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC15</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC15(?![0-9])</expect></criterion>
`TXM1-AC15` -- (difference) a valuation date before the account's first observation is TRADED_HISTORY_UNVERIFIED, while the same date covered by a retained earlier complete NO observation reads inactive

<criterion id="TXM1-AC16" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC16</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC16(?![0-9])</expect></criterion>
`TXM1-AC16` -- replaying one logical snapshot twice with different run UUIDs creates no second event and moves no date (`source_event_id` stable)

<criterion id="TXM1-AC17" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC17</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC17(?![0-9])</expect></criterion>
`TXM1-AC17` -- an older unseen snapshot is retained with TRADED_EVENT_ORDER_CONFLICT and does not roll the current state back

<criterion id="TXM1-AC18" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC18</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC18(?![0-9])</expect></criterion>
`TXM1-AC18` -- two conflicting snapshots at one `observed_at` are refused

<criterion id="TXM1-AC19" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC19</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC19(?![0-9])</expect></criterion>
`TXM1-AC19` -- same-UTC-day transitions keep every event, and the latest accepted state governs that day

<criterion id="TXM1-AC20" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC20</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC20(?![0-9])</expect></criterion>
`TXM1-AC20` -- a CORRECT_IDENTITY, CONFIRM_TRANSFER or RESOLVE_STRATEGY record without a source YES leaves the account non-live

<criterion id="TXM1-AC21" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC21</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC21(?![0-9])</expect></criterion>
`TXM1-AC21` -- a legacy CONFIRM_EFFECTIVE_MEMBERSHIP record is read as historical evidence and activates nothing

<criterion id="TXM1-AC22" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC22</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC22(?![0-9])</expect></criterion>
`TXM1-AC22` -- the dispositions key is computed only by `address("mdpf","49financial","state","taxsma_membership","dispositions.json")`

<criterion id="TXM1-AC23" cell_refs="TX-m-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/probes/tx_m_1.py AC23</invocation><expect>(?m)^VERDICT: PASS-TXM1-AC23(?![0-9])</expect></criterion>
`TXM1-AC23` -- the module has no workbook, BD roster or trading write call site

<expected_criteria>TXM1-AC1, TXM1-AC2, TXM1-AC3, TXM1-AC4, TXM1-AC5, TXM1-AC6, TXM1-AC7, TXM1-AC8, TXM1-AC9, TXM1-AC10, TXM1-AC11, TXM1-AC12, TXM1-AC13, TXM1-AC14, TXM1-AC15, TXM1-AC16, TXM1-AC17, TXM1-AC18, TXM1-AC19, TXM1-AC20, TXM1-AC21, TXM1-AC22, TXM1-AC23</expected_criteria>

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
data/mdpf/scripts/gold/taxsma_membership.py
data/mdpf/tests/taxsma/test_taxsma_membership.py
org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md</decomp_doc> @7f65001ab3, cell `TX-m-1`, round 1 (section 3).
<owned_cells>TX-m-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `TXM1-AC1` .. `TXM1-AC23` (23). Instance at
`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~2/MDPF_TAXSMA.TO-TX-m-1.membership.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `MDPF`, spec_ref.group `OTHER`, spec_ref.doc the PRD @671925aecc, decomp_ref.doc the
decomposition @7f65001ab3, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> TXM1-AC1,TXM1-AC2,TXM1-AC3,TXM1-AC4,TXM1-AC5,TXM1-AC6,TXM1-AC7,TXM1-AC8,TXM1-AC9,TXM1-AC10,TXM1-AC11,TXM1-AC12,TXM1-AC13,TXM1-AC14,TXM1-AC15,TXM1-AC16,TXM1-AC17,TXM1-AC18,TXM1-AC19,TXM1-AC20,TXM1-AC21,TXM1-AC22,TXM1-AC23`
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

Seating: slot ~2, queue position 3. Round 1 of MDPF_TAXSMA, issued by `2.0.0_SA_COO~T`, seated by `0.0.0_AB_MSTR` (msg 97080,
LD-0569) on Andrew's seat order ~12:5xZ 2026-09-15. Decomposition @7f65001ab3.
