# NFRA_MCPINDEX task order -- `MX-u-1` -- read from the gateway source what each client adapter accepts as the `platform` argument of the five client_* tools, and write it as one data file

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round27-GATEWAY.md</decomp_doc>
<owned_cells>MX-u-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-u-1.platform-labels</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~94</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted mutants inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-u-1` (round 27, workstream GATEWAY; PRD v0.19 FWD-24/FWD-25; CTO round-26 analysis, round-27 list item 2)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The five client tools of the gateway (`client_resolve_account`, `client_get_holdings`, `client_get_allocation`, `client_get_fees`, `client_get_transactions`) take an optional `platform` argument. The tool descriptions do not say what a valid value is. In round 26 a runner passed vendor names (blackdiamond, schwab, orion, eclipse) and was refused `platform_not_source_label`; the CTO ruled those refusals are not tool faults until a run uses the labels the tools accept. Your job is to READ THE SOURCE and state, per tool and per adapter, what `platform` accepts. The issuer then reads the accepted values from the data, re-runs the Schwab and Eclipse chains and writes the rule into the per-employee sheets.

**What to build.** `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~94/platform_labels.json`: 35 items (5 tools x 7 adapters).

### What the source holds (read it yourself; these anchors are where to start, the file is the evidence)

Everything is under `infra/aws/ec2/opal-gateway/app/` (read-only surfaces; the path grant of section 3 does not name them because you only READ them).

- Dispatch. `tools.py:28` imports the seven adapter modules; `tools.py:1626` registers each with `client_core.register_adapter` (`client_core.py:93`). The five tool wrappers are `tools.py:1632` (resolve), `:1638` (holdings), `:1644` (transactions), `:1653` (allocation), `:1659` (fees); the work is in `client_core.py`: `client_resolve_account` at `:552` (it asks EVERY adapter that holds the firm, passes `platform` to each, merges the candidates and records each adapter's refusal), `client_get_holdings` `:598`, `client_get_transactions` `:602`, `client_get_allocation` `:617`, `client_get_fees` `:621` (these route by the vendor prefix of the account reference through `_route` and `_adapter`, `client_core.py:476-484`, `:543-546`).
- The seven adapter files, each `client_adapter_<adapter>.py`, each with the five functions `resolve_account`, `get_holdings`, `get_allocation`, `get_fees`, `get_transactions` taking `platform`:
  - `client_adapter_schwab.py` (adapter `schwab`, firm bound at `:87`): `_check_platform` at `:96-101`; the refusal table at `:42-57`; the docstring at `:11-12`.
  - `client_adapter_smartx.py` (`smartx`, `:72`): `PLATFORM_LABEL` at `:35`, `_check_platform` at `:83-85`.
  - `client_adapter_bd49f.py` (`bd49f`, `:141`): `_platform` at `:159-164`, `PLATFORM_LABEL` at `:44`.
  - `client_adapter_bdcottonwood.py` (`bdcottonwood`, `:83`): `_labels` at `:178-187`, `_check_platform` at `:190-192`, the extra refusals at `:283` and `:448`, the transactions and fees read at `:331-352`.
  - `client_adapter_commonwealth.py` (`commonwealth`, `:81`): `PLATFORM_LABEL` at `:29`, `_platform` at `:94-96`.
  - `client_adapter_orion.py` (`orion`, `:55`): `_account_rows` at `:174-190`, `_tx_rows` at `:193-217`, `resolve_account` at `:222-231`; raises of `platform_not_source_label` at `:186`, `:206`, `:231`.
  - `client_adapter_eclipse.py` (`eclipse`, `:56`): `resolve_account` at `:146-156`; the other four functions at `:199-220`.
- Every raise of `platform_not_source_label`: `client_adapter_orion.py:186,206,231`; `client_adapter_bdcottonwood.py:192,283,448`; `client_adapter_schwab.py:100`; `client_adapter_commonwealth.py:96`; `client_adapter_eclipse.py:156`; `client_adapter_smartx.py:85`; `client_adapter_bd49f.py:164`.
- The three canonical firms are `49financial`, `cottonwood`, `inflection`. Each adapter binds the ONE firm it serves in `bind_firms()` (the `FIRMS = (lookup("<firm>")["key"],)` line named above).

### The contract (verbatim from the decomposition; it is the whole specification)

**U1 PLATFORM LABELS** `platform_labels.json`, schema `gateway_platform_labels/1`: `{"schema","items":[{"tool","adapter","firm","accepts_platform":true|false,"platform_meaning":str,"label_source":{"table":str,"column":str}|null,"omit_means":str,"refusals":[{"code":str,"when":str}],"cite":"<path>:<line>","evidence":[str,...]}]}`. One item for each pair (tool, adapter) over the five `client_*` tools (`client_resolve_account`, `client_get_holdings`, `client_get_allocation`, `client_get_fees`, `client_get_transactions`) and every client adapter file `client_adapter_*.py` that handles a `platform` argument (read `client_core.py` and `tools.py` for the dispatch to find which adapter answers which firm); items sorted by (tool, adapter). `platform_meaning` (at least eight ASCII words) states what a valid `platform` is for that adapter, read from the code (for example a custodian label read from a named column of the vendor's own table, or "no platform label: the argument is ignored or refused"); `label_source` names the table and column the accepted values come from when the code reads them from data, else null; `omit_means` (at least eight ASCII words) states what the adapter does when `platform` is omitted; `refusals` lists the refusal codes the adapter raises about `platform` with the condition in at least five words; `cite` and every `evidence` entry are `<path>:<line>` of a file that exists with at least one `evidence` entry that is a different line from `cite`. No account number, name or data value appears anywhere in the file.

What the check adds to that text (so you are not surprised):
- `adapter` is the file name without `client_adapter_` and `.py` (`bd49f`, `bdcottonwood`, `commonwealth`, `eclipse`, `orion`, `schwab`, `smartx`). The check derives the 35 pairs itself by scanning the seven files for a `platform` parameter in each of the five functions; a missing, extra, repeated or unsorted pair is refused. Sorting is by (`tool`, `adapter`), both as plain strings.
- `firm` is the canonical firm key the adapter binds (`49financial`, `cottonwood` or `inflection`), read by the check from the adapter's `FIRMS = (lookup("..."))` line.
- `accepts_platform` is true when a non-null platform value can pass without a platform refusal for that tool (including an adapter that never reads the argument), false when every non-null value is refused. The check knows one answer from the source: the Schwab `_check_platform` has a single bare `return` (the None case), so every Schwab item must be false. A false item must list at least one refusal.
- `cite` is `infra/aws/ec2/opal-gateway/app/client_adapter_<adapter>.py:<line>` of THAT adapter's file (the line where that tool's function handles or ignores `platform`); `evidence` entries are `<path>:<line>` of existing files, at least one different from the cite. Every `refusals[].code` must appear as a quoted string in the cited adapter file; when `label_source` is not null, its `table` and `column` must appear in that file as written there (`fact_allocations`, `fact_transactions`, `fact_positions`, `Custodian`, `custodian`). Texts are plain ASCII; no digit run of seven or more in any string (the check treats it as account data).

### Inputs you read (you do NOT edit them)

- the gateway source named above, under `infra/aws/ec2/opal-gateway/app/`.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/evidence/PER_VENDOR_RUN_20261021.json` and `ROUND26_REPORT.md`: the refusals the round-26 runner met (counts and codes only), for context.
- the CRO brief `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md` section 4 (which vendor table and column hold the account number and the custodian).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree may lack `infra/aws/ec2/opal-gateway/app`, `workflows/atom_decomposition` and `workflows/gateway_battery`; the issuer pre-adds them, and `git sparse-checkout add infra/aws/ec2/opal-gateway/app workflows/atom_decomposition workflows/gateway_battery` is the only sparse change you may make (do it first if a path above is missing).
1. Read, for each of the seven adapters, how the five functions treat `platform`: what value is accepted, what is compared (a constant, a lower-cased text, or a Custodian value from a partition's rows), what the function does when `platform` is None, and which refusal codes it raises about it (and which further codes follow from it, for example `account_not_resolved` when the account has no rows under the label). Read `client_core.py` for how resolve fans out to all adapters of the firm. Where an adapter never reads `platform` in a function (it raises another refusal first), say so: `accepts_platform` true, the meaning naming the refusal that comes first.
2. Write the file with the Write tool (JSON, `indent=1`, ASCII), 35 items sorted by (tool, adapter), then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u1_check.py` for exactly what each arm grades.
3. Then spot-check yourself: open five items at random and re-read the cited line; if one does not show what the text says, fix it. The issuer reads the file at the drain and compares it with the live data.

## 2. BOUNDS

1. You change only the files the path grant of section 3 names. Do NOT edit the issuer's checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter, any file under `infra/` or `app/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no gateway call, no grant, no deploy, no push. You READ the adapter source; you read no data.
2. ASCII only in the data file. You write one data file and no code. No account number, no client name, no data value, no last-four anywhere.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit). If the naming gate prints NAMING ERROR for a folder missing from the sparse cone and the commit still lands, say so in a surprise row (id form below); do not refile a row another worker of the round already filed.
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u1.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u1_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~94/platform_labels.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~94/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-u-1.platform-labels.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W94-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-u-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u1.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~94/platform_labels.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (35 (tool, adapter) pairs derived from the 7 client adapter files); the schema; exactly the derived pairs, each once, sorted by (tool, adapter), with the firm each adapter binds and well-typed fields (accepts_platform a boolean, label_source null or a table and column, refusals a list of code and when, text fields and evidence present); the planted negatives (a wrong schema, a pair dropped, a pair twice, a foreign tool, a foreign adapter, items out of order, a wrong firm, accepts_platform as a string, a label_source without a column) are each refused for the planted defect -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-u-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u1.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~94/platform_labels.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every item's cite is a line of its own adapter file and its evidence holds a different line, every cite and evidence entry resolves to an existing file and line, platform_meaning and omit_means have at least eight ASCII words, every refusal code is a quoted string of the cited adapter file with a condition of at least five words, a label_source names a table and column found in that file, no string carries a digit run of seven or more, a false accepts_platform lists a refusal, and every Schwab item is false; the planted negatives (a cite in another adapter file, a cite past the end of the file, evidence equal to the cite only, evidence naming a missing file, a three-word meaning, a non-ASCII omit text, a refusal code the file never raises, a three-word refusal condition, a digit run of eight, a false accepts_platform with no refusal, Schwab marked as accepting) are each refused for the planted defect -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~94/NFRA_MCPINDEX.TO-MX-u-1.platform-labels.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: for each of the seven adapters one line saying what `platform` accepts (counts and names only, no data); every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 27, workstream GATEWAY, worker ~94. Source: the CTO's round-26 analysis `ledger/ROUND_ANALYSIS.round26.md` (`1.0.0_SA_CTO~Z`, msg 36269) round-27 list item 2 (read from source the label set each client_* tool accepts, re-run Schwab and Eclipse with valid labels, put the labels in the sheets) and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round27-GATEWAY.md` (the contract R27.3 U1 is frozen at the cut; this order's section 1 adds only the clarifications the real source required: `adapter` = file stem, `firm` = the bound canonical key, the meaning of `accepts_platform`, the cite and evidence forms, the 35-item count). Base dry-runs 2026-10-21: `u1.AC1 base: FAIL as expected` and `u1.AC2 base: FAIL as expected` (the deliverable is absent; only the final deliverable arm fails, every control and planted-negative arm passes). Scratch reference file (not committed, built outside the repository from a real reading of the seven adapters): passes `u1.AC1` (12 of 12 arms) and `u1.AC2` (14 of 14 arms); three mutants of the reference itself (a pair dropped; Schwab marked as accepting; a label_source table the file lacks) each FAIL the criterion that owns the defect. WHAT THE SOURCE SAYS (the fork's reading, not enforced beyond the Schwab arm): Schwab accepts no platform at all (a contract label gets `platform_not_source_label`, anything else `platform_enum_open`); SmartX accepts only the constant `smartx`; Black Diamond 49F accepts `blackdiamond` or `black diamond` in any letter case; Commonwealth accepts only `commonwealth` (lower-cased compare); Black Diamond Cottonwood and Orion accept a Custodian/custodian value present in the partition read (tables `fact_allocations` or `fact_transactions` for Cottonwood; `fact_positions` or `fact_transactions` for Orion); Eclipse reads a platform only in resolve (the custodian of the Orion `fact_positions` rows) and ignores it in the other four functions. This explains the round-26 refusals: the runner passed vendor names where the adapters want a source label, or a constant, or nothing. The check proves shape and grounding in the adapter files, not that a prose judgment is right, which the issuer reads at the drain against the live data.

<status>issued</status>
<round>27</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
