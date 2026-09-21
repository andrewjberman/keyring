# TO NFRA_MCPINDEX.TO-MX-c-4 -- classification and registration compose from each integration's declaration

<to_id>NFRA_MCPINDEX.TO-MX-c-4</to_id>
<project>NFRA_MCPINDEX</project>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~1</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @b7dc80e2cc (ADMITTED) | **Decomp cell:** `MX-c-4` | **serves:** C2, V.4, A11, FWD-10 | **slot:** ~1, queue position 3 of 5

---

## WORKER FACE

### THE CELL

`MX-c-4` -- **classification and registration compose from each integration's declaration; a tool with no catalog entry or no classification is REFUSED at registration.** Status at the cut: OPEN.

**Writes:** exactly the `<paths>` block below (it is your grant), plus your deliverables folder `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/`. The cell's own writes line reads: `APP/destructive_ops.py`, `APP/data_entitlement.py` (tool-class composition only), `INT/base.py`, `INT/registry.py`, `TST/test_entitlement_admin.py` (the :332 pin only), `TST/test_tool_classification_composition.py` (new). Abbreviations used in the criteria: `GW` = `infra/aws/ec2/opal-gateway`; `APP` = `infra/aws/ec2/opal-gateway/app`; `INT` = `infra/aws/ec2/opal-gateway/app/integrations`; `TST` = `infra/aws/ec2/opal-gateway/tests`; `CAT` = `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`; `EMIT` = `workflows/atom_decomposition`; `TFGW` = `infra/aws/terraform/opal-gateway`; `STD` = `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md`.

**Read:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` (the specification; the ENDPOINT section and CONTRACTS C1-C8 bind); your cell's section of `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md` (s.3), its gates (s.6), its bounds (s.8) and the findings at s.1 and s.11 -- they carry the measured facts this cell rests on (the catalog's repository path; the emitter's code against its docstring; `dim_transaction`; the discharged entity-resolution gate; the builder-resolved catalog address). Print the bytes at any line you rely on (PRD VII.5); never grep for a quote.

Write `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/classification-composition.result.md` (each value with its instrument, UTC time and denominator). The probe for every mechanical criterion is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py`, which you write: it takes the criterion's short id (`AC1` .. `AC12`), runs or reads the evidence, prints its measurement with vintage and denominator, then exactly one line `VERDICT: PASS-MXC4-AC<n>` or `VERDICT: FAIL-MXC4-AC<n> <reason>`. A "(difference)" criterion runs its engaged and disengaged arms in the same probe run and prints what differed. A census criterion prints its denominator.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="MXC4-AC1" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC1</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC1(?![0-9])</expect></criterion>
`MXC4-AC1` -- `IntegrationSpec` (`INT/base.py`) carries a per-tool classification and a per-tool catalog-entry reference, and `validate_integration_spec` refuses a spec with either missing

<criterion id="MXC4-AC2" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC2</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC2(?![0-9])</expect></criterion>
`MXC4-AC2` -- `destructive_ops.classify(tool)` returns the declared class for an integration tool, read through the registered spec, and still returns `_UNKNOWN_TAG` (fail-closed) for any tool with no declaration

<criterion id="MXC4-AC3" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC3</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC3(?![0-9])</expect></criterion>
`MXC4-AC3` -- (difference) a planted integration whose one tool has no classification is refused at `register_enabled` and adds zero tools, while the same integration with the classification declared registers that tool, in one test module (FWD-10 PROOF, the refusal half)

<criterion id="MXC4-AC4" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC4</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC4(?![0-9])</expect></criterion>
`MXC4-AC4` -- (difference) a planted tool with a classification but no catalog-entry reference is refused at registration, while the same tool with the reference registers

<criterion id="MXC4-AC5" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC5</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC5(?![0-9])</expect></criterion>
`MXC4-AC5` -- `INT/registry.py` discovers integrations from their own directories, and the four existing ids (`ycharts`, `opal_portal`, `globgrph`, `schwab`) register exactly as before, names printed before and after

<criterion id="MXC4-AC6" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC6</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC6(?![0-9])</expect></criterion>
`MXC4-AC6` -- every one of the 49 existing tool names resolves through `destructive_ops.classify` and `data_entitlement` to the class it had before the change, compared by name, denominator 49, zero differences

<criterion id="MXC4-AC7" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC7</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC7(?![0-9])</expect></criterion>
`MXC4-AC7` -- `read_teams_attachment` is classified, and it is no longer denied by the fail-closed branch; the classification it receives is stated with its reason (`J` below)

<criterion id="MXC4-AC8" cell_refs="MX-c-4" judgment="true"/>
`MXC4-AC8` -- JUDGMENT (graded by 3.0.0_SA_CVO at L9; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL) -- `read_teams_attachment`'s classification is correct for a tool that reads the content of a Teams attachment by URL, and it neither widens what any tier can reach nor reads as a write

<criterion id="MXC4-AC9" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC9</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC9(?![0-9])</expect></criterion>
`MXC4-AC9` -- the pinned count at `TST/test_entitlement_admin.py:332` becomes a derived count that asserts, by name, every registered tool against its integration's own pinned list, and it still fails when a tool is registered without being pinned (difference: one planted unpinned tool fails it; removing the plant passes)

<criterion id="MXC4-AC10" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC10</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC10(?![0-9])</expect></criterion>
`MXC4-AC10` -- the Gateway suite's collected, passed and failed counts are printed before and after the edit, and no test that passed before fails after

<criterion id="MXC4-AC11" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC11</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC11(?![0-9])</expect></criterion>
`MXC4-AC11` -- C2's bar, EXERCISED (CTO 98944): for every registered tool, denominator printed, a lookup by name through `destructive_ops.classify` returns its declared class and a lookup by name through `data_entitlement` returns its tool class, and the tool's catalog-entry reference resolves to an entry in `CAT` -- zero tools fail any of the three

<criterion id="MXC4-AC12" cell_refs="MX-c-4"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/probes/mx_c_4.py AC12</invocation><expect>(?m)^VERDICT: PASS-MXC4-AC12(?![0-9])</expect></criterion>
`MXC4-AC12` -- (difference) a planted tool reachable by the composed registration path but resolving through neither registry is REFUSED at registration, while the same tool with both declarations registers (a composed path that could ship it FAILS C2)

<expected_criteria>MXC4-AC1, MXC4-AC2, MXC4-AC3, MXC4-AC4, MXC4-AC5, MXC4-AC6, MXC4-AC7, MXC4-AC8, MXC4-AC9, MXC4-AC10, MXC4-AC11, MXC4-AC12</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_MCPINDEX-W1-S<k>`, per the worker definition. Keep working after filing.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

**The decomposition's bounds, inlined verbatim (s.8):**

1. **No egress off Opal infrastructure.** No worker calls YCharts, Bloomberg, Microsoft Graph or any vendor. The one live
   YCharts call in `MX-v-4` is made only under Andrew's per-use word for that call (G-Y).
2. **No private data in the repository.** No client name, full account number, balance, token, cookie or credential
   enters code, fixtures, catalog entries, deliverables or logs; masked references and aggregate counts only.
3. **Addresses and names from the builders.** Every new S3 key is `address()` output and every new resource name is
   `name()` output (Rule 30). A builder refusal is a registry row, never a typed path.
4. **Deploy discipline.** A world-changing act opens its change-management entry and commits the OPEN sentinel before
   the act, then closes and commits the entry before the reads that grade it. Terraform through `safe-apply` only, never
   `-target`; the Gateway through `infra/aws/ec2/safe-ec2-deploy.sh` only.
5. **One Terraform state, one writer.** The `opal-gateway` root is applied by `MX-i-3` alone in this project, and never
   concurrently with NFRA_OPLGTW or MDPF_TAXSMA (G-S).
6. **No served output moves.** No cell writes a portal served key. `MX-r-1` releases dormant code and proves DELTA=0 on
   the tool surface; enabling is `MX-r-2` under G-A.
7. **No new monitor, alarm, SNS, email, watcher, schedule or standing comparator.** `MX-h-1` names any schedule a
   candidate would create, and choosing one is a finding, not a build.
8. **The Schwab integration is read, never edited.** No file under `infra/aws/ec2/opal-gateway/app/integrations/schwab/`
   changes in any cell. The engine is reached by import. The one Schwab change this project may make is a fence prefix
   for `dim_transaction`, generated by `MX-i-1` and applied by `MX-i-3`.
9. **The spec is frozen, and the face instructs refusal.** A criterion that cannot be satisfied as written is REFUSED and
   reported with its measurement, never repaired, widened or met by another route. Anything off-spec is a row.
10. **The catalog is generated, never hand-edited or hand-merged.** `DATA_CATALOG.yaml` changes only as the emitter's
    output; a merge conflict on it resolves by re-running the emitter at the drain.
11. **Every invocation terminates** (`timeout 120`, or the tool's own budget).
12. **Commits go through `.tools/safe-commit.sh` under the worker's serial; every `.py` edit passes
    `.tools/commit-gate.sh`.**
13. **Unknown deployment facts are measured, never presumed.** A cell asserts no deployed state it did not read back.
14. **No new dependency.** A missing instrument is a refusal, never an install.
15. **Tool names under C3.** No tool is registered under the research record's business-first names or the parked
    `DESIGN.md:44-45` names as they stand.
16. **Opal staff only.** No partner or client principal is admitted, granted or tested with (Andrew's standing
    2026-08-20 ruling).
17. **The Gateway suite baseline is `MX-p-1`'s printed count.** A cell adds no failure; a pre-existing failure is not
    its to fix (a row if its change touches it).

---

<paths>
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/integrations/base.py
infra/aws/ec2/opal-gateway/app/integrations/registry.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_tool_classification_composition.py
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc> @f506f63a8b, cell `MX-c-4`, round 1 (section 3).
<owned_cells>MX-c-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `MXC4-AC1` .. `MXC4-AC12` (12). Instance at
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/NFRA_MCPINDEX.TO-MX-c-4.classification-composition.proof_of_spec.json`
(phase `INVESTIGATION`, firm `NFRA`, spec_ref.group `OTHER`, spec_ref.doc the PRD @b7dc80e2cc, decomp_ref.doc the
decomposition @f506f63a8b, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> MXC4-AC1,MXC4-AC2,MXC4-AC3,MXC4-AC4,MXC4-AC5,MXC4-AC6,MXC4-AC7,MXC4-AC8,MXC4-AC9,MXC4-AC10,MXC4-AC11,MXC4-AC12`
BEFORE the `complete` flip. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a
row is FAIL withdraws your own grant. Judgment rows carry no verdict.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 1800, 5 of 5 carriers scanned (C1 138, C2 7, C3 12, C4 21, C5 334), 26 gates armed, 0 naming NFRA_MCPINDEX, the opal-gateway or the catalog; self-test PASS 6/6. This project registers G-S, G-A, G-B, G-Q, G-Y and notices N-1, N-2 (decomposition s.6).
comp-iam: RUN at L5 -- DESIRED plane; opal-gateway-role 14 statements (portal json/* and platinum/* already granted; silver only through assumed fenced roles; no firm-bucket grant); attach-census 31 policy blocks NOT ATTACHED and 6 deny statements unparsed (deny-blind, stated).
comp-adversary: RUN at L5 on the PRD v0.5 -- 7 of 7 cited commits verified; 7 cited paths attempted, 7 stable, 0 flagged; 1754 uncited siblings, 12 digested. Blindness stated: T11 unresolved (the PRD carries no <decomp_ref>), and path stability is not path correctness (s.1 falsifier 1).
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); the deliverables folder is granted by convention.
</preflight>

Seating: slot ~1, queue position 3 (MX-c-1 -> MX-c-2 -> MX-c-4 -> MX-g-1 -> MX-g-2). Round 1 of NFRA_MCPINDEX, issued by `2.0.0_SA_COO~M`, seated by `1.0.0_SA_CTO` on Andrew-direct 2026-09-21 ~00:5xZ (arming record @07b8a03ec3). Decomposition v2 @f506f63a8b (merge e4c6d91353), recut on 1.0.0_SA_CTO 98944 before issuance; v1 @020ab35a75 never issued.
