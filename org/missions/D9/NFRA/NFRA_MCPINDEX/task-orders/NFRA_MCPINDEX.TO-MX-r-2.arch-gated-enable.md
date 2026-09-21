# TO NFRA_MCPINDEX.TO-MX-r-2 -- enable this project's integrations: `ENABLED_INTEGRATIONS` and IAM, arch-gated

<to_id>NFRA_MCPINDEX.TO-MX-r-2</to_id>
<project>NFRA_MCPINDEX</project>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~5</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending -- HELD on G-A (decomposition s.6); issued with the round, spawned only when the gate stands</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @b7dc80e2cc (ADMITTED) | **Decomp cell:** `MX-r-2` | **serves:** release; FWD-1..FWD-10 | **slot:** ~5, queue position 5 of 8

---

## WORKER FACE

### THE CELL

`MX-r-2` -- **enable this project's integrations: `ENABLED_INTEGRATIONS` and IAM, arch-gated.** Status at the cut: HELD (G-A).

**Writes:** exactly the `<paths>` block below (it is your grant), plus your deliverables folder `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/`. The cell's own writes line reads: the host `.env` through the deploy path; `org/critical_paths/`. Abbreviations used in the criteria: `GW` = `infra/aws/ec2/opal-gateway`; `APP` = `infra/aws/ec2/opal-gateway/app`; `INT` = `infra/aws/ec2/opal-gateway/app/integrations`; `TST` = `infra/aws/ec2/opal-gateway/tests`; `CAT` = `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`; `EMIT` = `workflows/atom_decomposition`; `TFGW` = `infra/aws/terraform/opal-gateway`; `STD` = `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md`.

**Read:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` (the specification; the ENDPOINT section and CONTRACTS C1-C8 bind); your cell's section of `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md` (s.3), its gates (s.6), its bounds (s.8) and the findings at s.1 and s.11 -- they carry the measured facts this cell rests on (the catalog's repository path; the emitter's code against its docstring; `dim_transaction`; the discharged entity-resolution gate; the builder-resolved catalog address). Print the bytes at any line you rely on (PRD VII.5); never grep for a quote.

**HELD:** this cell holds on G-A. It is issued with the round so the issuance covers every cell; you are spawned on it only when the gate stands. If you find the gate NOT standing when you start, that is a BLOCKING surprise row and a stop, never a workaround.

Write `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/arch-gated-enable.result.md` (each value with its instrument, UTC time and denominator). The probe for every mechanical criterion is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/probes/mx_r_2.py`, which you write: it takes the criterion's short id (`AC1` .. `AC6`), runs or reads the evidence, prints its measurement with vintage and denominator, then exactly one line `VERDICT: PASS-MXR2-AC<n>` or `VERDICT: FAIL-MXR2-AC<n> <reason>`. A "(difference)" criterion runs its engaged and disengaged arms in the same probe run and prints what differed. A census criterion prints its denominator.

**Gates that touch this cell (decomposition s.6, inlined):**

- **G-A** | the CTO's G1-G8 arch-gate signed per integration before its enable-deploy | `NFRA_INTEGRATIONS_STANDARD.md` s.5 step 5 and s.8.1 (standing law) | `1.0.0_SA_CTO`; `3.0.0_SA_CVO` live-certs G5-G7 after | `MX-r-2`

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="MXR2-AC1" cell_refs="MX-r-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/probes/mx_r_2.py AC1</invocation><expect>(?m)^VERDICT: PASS-MXR2-AC1(?![0-9])</expect></criterion>
`MXR2-AC1` -- the CTO's G1-G8 arch-gate (STD s.8.1) is signed for each integration this cell enables, cited by commit, before the enable

<criterion id="MXR2-AC2" cell_refs="MX-r-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/probes/mx_r_2.py AC2</invocation><expect>(?m)^VERDICT: PASS-MXR2-AC2(?![0-9])</expect></criterion>
`MXR2-AC2` -- each enabled integration's id is added to `ENABLED_INTEGRATIONS` through the deploy path, never a runtime flip on the host

<criterion id="MXR2-AC3" cell_refs="MX-r-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/probes/mx_r_2.py AC3</invocation><expect>(?m)^VERDICT: PASS-MXR2-AC3(?![0-9])</expect></criterion>
`MXR2-AC3` -- (difference) after the enable, a non-admitted principal lists zero tools of this project, while an admitted principal lists exactly their granted set

<criterion id="MXR2-AC4" cell_refs="MX-r-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/probes/mx_r_2.py AC4</invocation><expect>(?m)^VERDICT: PASS-MXR2-AC4(?![0-9])</expect></criterion>
`MXR2-AC4` -- a below-`min_tier` caller is denied with `min_tier_denied` and zero egress, on the deployed Gateway (STD G5)

<criterion id="MXR2-AC5" cell_refs="MX-r-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/probes/mx_r_2.py AC5</invocation><expect>(?m)^VERDICT: PASS-MXR2-AC5(?![0-9])</expect></criterion>
`MXR2-AC5` -- the audit lake carries one deny and one ok record for each enabled integration, tier-stamped (STD G6)

<criterion id="MXR2-AC6" cell_refs="MX-r-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/probes/mx_r_2.py AC6</invocation><expect>(?m)^VERDICT: PASS-MXR2-AC6(?![0-9])</expect></criterion>
`MXR2-AC6` -- the change-management entry and sentinel open before and close after, as in `MX-r-1`

<expected_criteria>MXR2-AC1, MXR2-AC2, MXR2-AC3, MXR2-AC4, MXR2-AC5, MXR2-AC6</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_MCPINDEX-W5-S<k>`, per the worker definition. Keep working after filing.
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
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-mx-r-2.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc> @f506f63a8b, cell `MX-r-2`, round 1 (section 3).
<owned_cells>MX-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `MXR2-AC1` .. `MXR2-AC6` (6). Instance at
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~5/NFRA_MCPINDEX.TO-MX-r-2.arch-gated-enable.proof_of_spec.json`
(phase `INVESTIGATION`, firm `NFRA`, spec_ref.group `OTHER`, spec_ref.doc the PRD @b7dc80e2cc, decomp_ref.doc the
decomposition @f506f63a8b, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> MXR2-AC1,MXR2-AC2,MXR2-AC3,MXR2-AC4,MXR2-AC5,MXR2-AC6`
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

Seating: slot ~5, queue position 5 (MX-p-1 -> MX-v-1 -> MX-v-2 -> MX-r-1 -> MX-r-2 -> MX-v-3 -> MX-v-4 -> MX-v-5). Round 1 of NFRA_MCPINDEX, issued by `2.0.0_SA_COO~M`, seated by `1.0.0_SA_CTO` on Andrew-direct 2026-09-21 ~00:5xZ (arming record @07b8a03ec3). Decomposition v2 @f506f63a8b (merge e4c6d91353), recut on 1.0.0_SA_CTO 98944 before issuance; v1 @020ab35a75 never issued.
