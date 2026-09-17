# TO NFRA_OPLGTW.TO-OG-i-5 -- the access-state table renamed to the builder's name, its records carried across under proof

<to_id>NFRA_OPLGTW.TO-OG-i-5</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.7 @79a1fd4a47 | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 -> v1.1 | **Decomp cell:** `OG-i-5` | **outcome_ref:** FWD-1, FWD-3, FWD-4, FWD-6, FWD-7 | **depends_on:** `OG-i-2` (the same Terraform state); precedes `OG-i-3` and `OG-r-1` | **slot:** ~1

---

## WORKER FACE

### THE CELL

`OG-i-5` -- **rename the live DynamoDB table `opal-gateway-access-state` to the name the naming builder emits, and carry
every record across under proof.** `OG-i-1` created the table on 2026-09-15 under a name the PRD typed. The naming
grammar (CLAUDE.md Rule 30, `lib/opal_naming.py`) makes every new resource name builder output. `1.0.0_SA_CTO` ruled the
table RENAMED in its own order and ledger entry, with no register departure (ruling R-OG-8, msg 97553, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md`, PRD v0.7 @79a1fd4a47 C1 and CONTRACTS).

The ruling, as its constraints:
- **The new name** is `name("gateway", None, "access-state", "table")`, measured by the ruling as
  `gateway-access-state-table` (CONFORMANT). Print it from the builder; never type it.
- **What the old table holds:** at the ruling's read, 7 items, 1,015 bytes, created 2026-09-15, ACTIVE. Re-measure it
  yourself; the number here is context, not an acceptance value.
- **Order of acts:** create the new table; copy every record; prove the counts equal and every item equal (the
  operator-audit namespace included); move the application's table reference and the Terraform declaration together;
  then remove the old table. The old table is retained until the copy is proven, and removed inside this order.
- **Move every reference together:**
  - `infra/aws/terraform/opal-gateway/schwab_access_state.tf` (the table resource, and the table ARN in the runtime
    grant and the operator policy);
  - `infra/aws/ec2/opal-gateway/app/access_state.py` (`TABLE_NAME`);
  - `infra/aws/ec2/opal-gateway/app/oauth_as.py` (its docstring names the table);
  - `org/standards/NFRA_OPLGTW_CONTRACT.json` (`state_store.table`), bumped to version 1.1.
  - `OG-i-3`, later in your queue, adds the three IAM names to the same v1.1.

**Two constraints added to the ruling (amended by `2.0.0_SA_COO~O` before re-hand, per `1.0.0_SA_CTO` msg 97556, which
adopts `3.0.0_SA_CVO`'s two notes as R-OG-8's own constraints).**
- **Writes QUIESCED through the copy and the cutover.** `app/oauth_as.py` writes this table live once deployed
  (one-use codes, refresh-generation rotation). A generation written between the copy and the cutover would be lost while
  both counts still agreed at their own instants.
  - So prove that NO writer touches the old table from the copy's start to the post-cutover re-check (AC12).
  - At the cut the live host runs a pre-project build (`OG-p-1` AC12 read 0 registered clients among the table's items).
    Read the deployed app on the host by SSM (read-only command text, printed) and show that it references neither
    table name.
  - Also show that the old table's per-item digests are unchanged between the copy's start and the post-cutover re-check.
  - If a live writer is found, that is a BLOCKING row and a stop. Stopping or pausing the Gateway service is not granted
    to this cell.
  - **The maintenance window, stated (msg 97556: "its length and the Gateway's behaviour during it (refuse with a retry
    hint, never a silent 500) are stated in the order and in the ledger entry").** The window runs from the copy's start
    to the post-cutover re-check (AC13), and is bounded at 60 minutes. Past that bound, stop, file a row, and roll back
    per the deploy discipline. The Gateway's behaviour during the window: the live host runs the pre-project build, which
    reads and writes neither table (AC12 proves it), so existing users see no change and there is nothing to refuse.
    - No build that writes the table is deployed until `OG-r-1`, after this order.
    - If AC12 finds that premise false, there is no window: stop at a BLOCKING row. A live writer would need its
      refuse-with-retry-hint behaviour built and deployed first, which this cell is not granted.
    - Write the window's start, end, length and this behaviour statement into the ledger entry's `copy` leg.
- **The old table is removed only AFTER the rollback window has closed; inside the window it is the rollback target and
  is not touched.** For this order the window closes when all of these are recorded PASS: the post-cutover count and
  item-by-item re-check (AC13), the reference move (AC7), the module runs (AC8) and the on-host exercise against the
  new table (AC9). Apply 2 starts only after that (AC10).

**How to sequence the two applies** (the mechanism is yours; the criteria constrain it):
- **Apply 1** declares the new table beside the old one and repoints the runtime grant and the operator policy to the
  new table's ARN. Nothing is destroyed.
- **The copy** runs under your operator identity, with conditional puts that never overwrite, from a consistent scan of
  the old table. Copy every item, probe records included.
- **Apply 2** removes the old table's declaration, and runs only after AC5 and AC6 are recorded PASS.
- Both applies run under ONE ledger entry with legs `create`, `copy`, `retire`.

**Read:** the PRD v0.7's "C1" and "C6" and its CONTRACTS enumeration line; the ruling record above;
`infra/aws/terraform/opal-gateway/schwab_access_state.tf`; `app/access_state.py`;
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/access-state-table.result.md` (OG-i-1's table,
grants and probe keys).

**The probe** for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py`,
taking the short id, printing its measurement with vintage and denominator, then exactly one line
`VERDICT: PASS-OGI5-AC<n>` or `VERDICT: FAIL-OGI5-AC<n> <reason>`. Save each plan as JSON (`terraform show -json`) in
your deliverables. AC9's on-host arm runs through SSM on `i-07dccb1615503ac99` with the instance's own role, using probe
keys `RUNTIME#probe-og-i5-<utc>` and `POLICY#probe-og-i5-<utc>`. Print each SendCommand's command text in your
evidence, and make it a read or that single probe write only (ruling R-OG-2).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGI5-AC1" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC1(?![0-9])</expect></criterion>
`OGI5-AC1` -- the new table name printed by `lib/opal_naming.py` `name("gateway", None, "access-state", "table")` equals `gateway-access-state-table`, and `grade()` on it reads conformant.

<criterion id="OGI5-AC2" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC2(?![0-9])</expect></criterion>
`OGI5-AC2` -- the ledger entry's OPEN sentinel is committed before apply 1 starts (the probe compares the sentinel's commit time with apply 1's recorded start).

<criterion id="OGI5-AC3" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC3(?![0-9])</expect></criterion>
`OGI5-AC3` -- apply 1's saved plan creates exactly the new table, updates only the runtime grant and the operator policy, and destroys nothing.

<criterion id="OGI5-AC4" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC4(?![0-9])</expect></criterion>
`OGI5-AC4` -- `describe-table` on the new table reads SSE enabled, point-in-time recovery enabled, PAY_PER_REQUEST billing, TTL on `expires_at` and the key schema `pk` (HASH) / `sk` (RANGE).

<criterion id="OGI5-AC5" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC5(?![0-9])</expect></criterion>
`OGI5-AC5` -- (discriminating) a consistent full scan of the old table and of the new table, taken after the copy and before apply 2, returns equal item counts, both printed; the result is recorded before apply 2 starts.

<criterion id="OGI5-AC6" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC6(?![0-9])</expect></criterion>
`OGI5-AC6` -- every item is equal on both sides by (`pk`, `sk`) and a sha256 of its canonical attribute map, with the per-namespace counts (`RUNTIME#`, `POLICY#`, and `operator_audit` records separately) printed; no key or value is committed, only digests and counts.

<criterion id="OGI5-AC7" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC7(?![0-9])</expect></criterion>
`OGI5-AC7` -- an unscoped `git grep -F opal-gateway-access-state` at your HEAD prints its denominator, and every hit outside the project's historical records (its deliverables, surprise channel, rulings, logs and change-management entries) is zero; `schwab_access_state.tf`, `app/access_state.py` and the contract JSON (version 1.1) name the new table.

<criterion id="OGI5-AC8" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC8(?![0-9])</expect></criterion>
`OGI5-AC8` -- `tests/test_access_state.py`, `tests/test_oauth_durable.py` and `tests/test_principal_cutover.py` each pass, one pytest process per module, their pass counts printed.

<criterion id="OGI5-AC9" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC9(?![0-9])</expect></criterion>
`OGI5-AC9` -- (difference) from the Gateway host, a runtime-principal write to a `POLICY#` probe key of the new table is AccessDenied, while the same write to a `RUNTIME#` probe key succeeds in the same harness (A13).

<criterion id="OGI5-AC10" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC10</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC10(?![0-9])</expect></criterion>
`OGI5-AC10` -- apply 2's saved plan destroys only the old table and changes nothing else, and its start time is later than the commit that records AC5, AC6, AC7, AC8, AC9, AC12 and AC13 PASS (the rollback window closed).

<criterion id="OGI5-AC12" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC12</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC12(?![0-9])</expect></criterion>
`OGI5-AC12` -- (quiescence) the deployed app on the Gateway host, read by SSM with its command text printed, references neither table name, and the old table's per-item digests taken at the copy's start equal those taken at the post-cutover re-check, the item count printed at both instants.

<criterion id="OGI5-AC13" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC13</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC13(?![0-9])</expect></criterion>
`OGI5-AC13` -- after the cutover (the reference-move commit and apply 1), the item count and the item-by-item digest check between the old and the new table are re-taken and equal, with the per-namespace counts printed, before apply 2 starts.

<criterion id="OGI5-AC11" cell_refs="OG-i-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py AC11</invocation><expect>(?m)^VERDICT: PASS-OGI5-AC11(?![0-9])</expect></criterion>
`OGI5-AC11` -- the ledger entry is closed and committed before the final reads, `describe-table` on the old name returns ResourceNotFound, and a fresh plan of the root reads 0 changes.

<expected_criteria>OGI5-AC1, OGI5-AC2, OGI5-AC3, OGI5-AC4, OGI5-AC5, OGI5-AC6, OGI5-AC7, OGI5-AC8, OGI5-AC9, OGI5-AC10, OGI5-AC11, OGI5-AC12, OGI5-AC13</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at hand-off (after `OG-i-2` merged). Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Record `pip freeze` in your result file. Never commit `.venv-og/` or `.scratch/`.
- **Deploy discipline (spine L7).** Open ONE entry with `py -3.12 .tools/deploy_ledger.py open --slug nfra-oplgtw-og-i-5-access-state-rename ...` with legs `create`, `copy`, `retire`, and COMMIT its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-i-5-access-state-rename.json` and its entry BEFORE apply 1. Close each leg with its proof and close the entry, and COMMIT that BEFORE AC11's reads. NEVER leave it half-landed:
  - if the copy cannot be proven, do not run apply 2;
  - revert the application and Terraform references to the old table in a commit, apply that, and leave both tables;
  - file an ARMED row naming yourself as disarm owner, and close the entry as rolled back.
- **Terraform.** Only through `.tools/safe-apply.sh`, never bare `terraform apply`, never `-target`. `.tools/terraform.exe` is provisioned into your worktree by the issuer; if absent, a BLOCKING row. The `opal-gateway` root is ONE state and only slot ~1 applies it.
- **Blast radius.** In the `opal-gateway` root and in AWS: the new table; the runtime grant's and the operator policy's table ARN; the copy's puts into the new table; and the old table's removal in apply 2. Nothing else. A plan showing any other change, or apply 1 showing any destroy, is a BLOCKING row and no apply.
- **The copy never overwrites.** Every put into the new table is conditional on the key being absent. A condition failure is a stop and a row, never a retry that overwrites.
- **No record for a real person is created, revised or read into evidence.** Only digests and counts leave the table.
- **The Gateway's running code is not deployed by this cell.** The live host keeps running its current build; `OG-r-1` deploys the integrated build later.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **No new monitor, alarm, SNS or notification path.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W1-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/terraform/opal-gateway/schwab_access_state.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/aws/ec2/opal-gateway/app/access_state.py
infra/aws/ec2/opal-gateway/app/oauth_as.py
org/standards/NFRA_OPLGTW_CONTRACT.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-i-5-access-state-rename.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 as amended 2026-09-16, cell `OG-i-5`, round 1 (section 3, S9).
<owned_cells>OG-i-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGI5-AC1` .. `OGI5-AC13` (13). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/NFRA_OPLGTW.TO-OG-i-5.access-state-rename.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @79a1fd4a47, decomp_ref.doc the
decomposition as amended, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGI5-AC1,OGI5-AC2,OGI5-AC3,OGI5-AC4,OGI5-AC5,OGI5-AC6,OGI5-AC7,OGI5-AC8,OGI5-AC9,OGI5-AC10,OGI5-AC11,OGI5-AC12,OGI5-AC13`
BEFORE the `complete` flip. Result file `access-state-rename.result.md` beside it, naming the new table ARN and both
tables' counts. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the cut 2026-09-16 ~19:4xZ -- --budget 240, 5 of 5 carriers scanned (C1 161, C2 6, C3 12, C4 21, C5 334), 25 gates armed, 0 lines naming NFRA_OPLGTW; 136 prose blocking fields are a reading list, not gates. Binding on this cell: the no-half-landed-deploy and safe-apply-only moratoria.
comp-iam: RUN at the cut -- comp-iam service opal-gateway, DESIRED plane only; 46 calls across 14 statements, 24 UNRESOLVABLE-RESOURCE, and dynamodb resources are not modeled (deny- and resource-blind for this table). This cell moves an existing grant's table ARN and adds no action; AC3, AC9 and AC10 read the APPLIED and EXERCISED planes the lens cannot see.
comp-adversary: RUN at the cut -- compose on the PRD at HEAD (v0.7): 4 of 4 cited commits VERIFIED; complement sources 5 run, 4 declared-excluded; pins are READ-VINTAGE only. The ratified-text half of v0.7 is OWED to 3.0.0_SA_CVO at the cut (1.0.0_SA_CTO msg 97553).
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); infra/aws/terraform/** and org/standards/** refuse a worker by lane and admit it only by this order's <paths>.
</preflight>

Added mid-round on 2026-09-16 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-8 (msg 97553, PRD v0.7 @79a1fd4a47),
with decomposition cell `OG-i-5` added in the same commit. Slot ~1, queue: `OG-i-5` -> `OG-i-3` -> `OG-i-4`. It precedes
`OG-r-1`, the first order that deploys a runtime consumer of the table. Amended 2026-09-16 ~20:0xZ, before any act (the
first hand-off's worker was stopped with its worktree clean), on `1.0.0_SA_CTO` msg 97556: quiescence and the
rollback-window ordering were added as cell text, AC12 and AC13 were added, and AC10 was re-anchored; no criterion was
removed. The issuer copies `.tools/terraform.exe` and the
halt-gate session serial file into the slot's worktree at spawn (row S18).
</content>
