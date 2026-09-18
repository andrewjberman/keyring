# TO NFRA_OPLGTW.TO-OG-r-2 -- on-host capacity and existing-workflow regression on the candidate

<to_id>NFRA_OPLGTW.TO-OG-r-2</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>superseded -- CLOSED for round 1 by 2.0.0_SA_COO~O at 2026-09-18T23:5xZ, EXECUTED AND DRAINED (@0279872d7a), never re-handed. The cell RAN: 6 of 8 mechanical criteria PASS by output, proof-of-spec VALID rc=0 (re-run by the issuer from the shared tree, a different checkout), CAPACITY.json records the on-host measurements and AC8's capacity verdict INSUFFICIENT with its `for_prd_revision_if_insufficient` block. TWO FAILS REMAIN AND NEITHER IS REPAIRABLE IN THIS ROUND: OGR2-AC4 (export at contract scale peaked 270581760 against the 268435456 job cap, LIMIT_EXCEEDED) is answered by R-OG-22, which rejects moving either number until the CTO resolves whether 250000 rows / 50 MiB is a CONSUMER REQUIREMENT or an aspiration -- a question about a consumer, not about this cell, and the revision is the CTO's at L4 and is NOT cut; OGR2-AC2 is a disclosed FAIL under R-OG-24 (the bar is "never exceeds"; the maximal job peaked 282021888) and joins AC4 as the second input to that same revision. Spec is frozen mid-round and this order's own bound forbids flipping complete with a mechanical FAIL, so holding it open would deadlock round 1's L10 on another seat's L4 question (LD-0521: the refuser counts open orders PER PROJECT). NOTHING IS RE-GRADED BY THIS CLOSE and no cap moves: the FAILs stand as measured, rows W2-S10, S48, S49 and S51 stay for 3.0.0_SA_CVO at L9, and the cell RE-CUTS in round 2 against the revised contract, carrying the cap_respected instrument repair (draft cell R2-b, @94b0c19f27). Was: pending.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-r-2` | **outcome_ref:** FWD-5, FWD-7, FWD-8 | **depends_on:** `OG-r-1`, `OG-i-4` | **slot:** ~2, queue position 3

---

## WORKER FACE

### THE CELL

`OG-r-2` -- **on-host capacity and the existing-workflow regression**, measured on the candidate: the t4g.small host
(`OG-i-4`) running the released build (`OG-r-1`). Write the benchmark harness at
`infra/aws/ec2/opal-gateway/tests/acceptance/onhost_bench.py`, run it on the host through SSM, and record.

The PRD, verbatim: *"Benchmark the actual candidate before enablement. Admission must reserve the measured existing
Gateway peak RSS plus 25 percent and 128 MiB operating headroom before starting a child, even below the global job cap;
insufficient headroom returns BUSY. A14 compares a declared identical existing-user workload before/after: no failures and
no more than 20 percent p95 latency regression, with workload, sample counts and measured window recorded. If the target
cannot satisfy the caps, return measured evidence for a PRD revision rather than activating with weakened guarantees."*
And: *"The Gateway's smaller deadline/response limits stay within Claude's published runtime limits"*; *"The SPEC's
18:43:46Z evidence records a 60-second ALB idle timeout: keep the 30-second query and export preparation deadlines and
avoid idle streaming gaps."*

Contract limits you measure against: `job_memory_bytes` 268435456, `query_deadline_seconds` 30, `export_deadline_seconds`
30, `export_rows` 250000, `export_utf8_bytes` 52428800, `per_principal_jobs` 1, `global_jobs` 2, `queue_size` 0;
`capacity.admission_existing_peak_rss_multiplier` 1.25, `admission_os_reserve_bytes` 134217728,
`existing_workflow_p95_regression_max_fraction` 0.2.

**How the benchmark runs.** In process on the host, with synthetic principal contexts and the synthetic fixtures from
`infra/aws/ec2/opal-gateway/tests/acceptance/fixtures/` (`OG-v-1`), calling the engine and export functions directly.
No bearer token is minted and no Schwab tool is enabled for any real principal. The existing-workflow before/after uses
`OG-p-1`'s workload, instrument and window rule (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`)
and `OG-i-4`'s re-baseline on the new host
(`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/pilot-host-resize.result.md`).

**Read:** the PRD's "C4", "C5" and "Operator journey, audit and release"; the contract's `limits` and `capacity`; the
engine (`infra/aws/ec2/opal-gateway/app/integrations/schwab/engine.py`) and export (`.../schwab/export.py`) at HEAD.

**The probe** for every mechanical criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py`,
which reads the recorded benchmark output (`CAPACITY.json` in your deliverables), prints the measurement with vintage and
denominator, then exactly one line `VERDICT: PASS-OGR2-AC<n>` or `VERDICT: FAIL-OGR2-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGR2-AC1" cell_refs="OG-r-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGR2-AC1(?![0-9])</expect></criterion>
`OGR2-AC1` -- the benchmark runs on the candidate host (after `OG-i-4`) against the released build, with synthetic principal contexts in process and no bearer token minted.

<criterion id="OGR2-AC2" cell_refs="OG-r-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGR2-AC2(?![0-9])</expect></criterion>
`OGR2-AC2` -- the maximal and concurrent Unicode query fixtures each stay within 256 MiB resident memory per job.

<criterion id="OGR2-AC3" cell_refs="OG-r-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGR2-AC3(?![0-9])</expect></criterion>
`OGR2-AC3` -- the maximal and concurrent Unicode query fixtures each finish within 30 seconds or return BUSY or LIMIT_EXCEEDED as designed.

<criterion id="OGR2-AC4" cell_refs="OG-r-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGR2-AC4(?![0-9])</expect></criterion>
`OGR2-AC4` -- a 50 MiB CSV fixture is generated within the export deadline and its temporary files are gone afterwards.

<criterion id="OGR2-AC5" cell_refs="OG-r-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGR2-AC5(?![0-9])</expect></criterion>
`OGR2-AC5` -- the existing peak RSS on the new host and the admission reserve computed from it are recorded.

<criterion id="OGR2-AC6" cell_refs="OG-r-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGR2-AC6(?![0-9])</expect></criterion>
`OGR2-AC6` -- (difference) the existing-workflow p95 after, against `OG-p-1`'s before, regresses by no more than 20 percent with zero failures, workload, sample counts and windows printed.

<criterion id="OGR2-AC7" cell_refs="OG-r-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGR2-AC7(?![0-9])</expect></criterion>
`OGR2-AC7` -- the ALB `idle_timeout` is read immediately before the test, with ARN and UTC time, and exceeds the 30-second preparation deadline.

<criterion id="OGR2-AC8" cell_refs="OG-r-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGR2-AC8(?![0-9])</expect></criterion>
`OGR2-AC8` -- the record carries a capacity verdict, SUFFICIENT or INSUFFICIENT, and an INSUFFICIENT one carries its measurements for a PRD revision.

<criterion id="OGR2-J1" cell_refs="OG-r-2" judgment="true"/>
`OGR2-J1` -- graded at L9 by 3.0.0_SA_CVO: the benchmark's workload is representative of the pilot's declared use. RECORD; NO VERDICT.

<expected_criteria>OGR2-AC1, OGR2-AC2, OGR2-AC3, OGR2-AC4, OGR2-AC5, OGR2-AC6, OGR2-AC7, OGR2-AC8, OGR2-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **The benchmark changes nothing it did not bring.** It copies the harness and synthetic fixtures to a scratch directory on the host, runs, and removes them; it does not restart the service, change configuration, enable the integration or write to the state store beyond isolated `RUNTIME#bench-og-r2-*` keys. A step that would need more is a BLOCKING row.
- **No real data.** Synthetic fixtures only; no Schwab object is read in this cell.
- **No egress off Opal infrastructure.** No call to Claude, Anthropic, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** An INSUFFICIENT capacity is a measured result, not a failure to repair: record it (AC8), never lower a limit or raise a cap to pass. A criterion you cannot satisfy as written is refused and reported with its measurement. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W2-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/tests/acceptance/onhost_bench.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-r-2`, round 1 (section 3, S9).
<owned_cells>OG-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGR2-AC1` .. `OGR2-AC8`, `OGR2-J1` (9). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/NFRA_OPLGTW.TO-OG-r-2.onhost-capacity.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGR2-AC1,OGR2-AC2,OGR2-AC3,OGR2-AC4,OGR2-AC5,OGR2-AC6,OGR2-AC7,OGR2-AC8,OGR2-J1`
BEFORE the `complete` flip. Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a
`status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.** Result file
`onhost-capacity.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. This cell waits on OG-i-4, which is HELD on G-A; nothing else holds it.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell adds no IAM operation, policy, principal or role; it runs an in-process harness on the host under the existing instance role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~2, queue position 3, handed after `OG-r-1` and `OG-i-4` merge. Round 1 of NFRA_OPLGTW, issued by
`2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
