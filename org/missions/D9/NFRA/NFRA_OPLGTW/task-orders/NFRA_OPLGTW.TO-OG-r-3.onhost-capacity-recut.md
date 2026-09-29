# NFRA_OPLGTW task order -- `OG-r-3` -- ROUND 2 (E6): on-host capacity re-cut -- the repaired memory grader, the streaming export at contract scale, and AC4 on the ruled windows

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-r-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~11</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time on-host benchmark; no cron, alarm, monitor or cadence is created.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM operation, policy, principal or role is added; the benchmark runs in process on the host under the existing instance role, and the CloudWatch/ELBv2/SSM reads use the operator's existing access.
comp-adversary: DECLARED-NOT-APPLICABLE -- the grader repair is ruled (R2-b @94b0c19f27, R-OG-24) and the windows are ruled (R-OG-23A/B; Q5 @5676f4a48a).
EGRESS CLASS, declared: Opal's own AWS plus the PyPI download for the venv below -- development egress permitted to this project's COO and its workers (Andrew-direct ~21:2xZ, record @7bfa5811c6).
</preflight>

## 1. THE CELL -- `OG-r-3` (decomposition addendum R2-E, item E6; re-cut of round 1's `OG-r-2`)

**Re-run round 1's on-host capacity benchmark against the unchanged contract, with three changes.** Outcomes served:
FWD-4, FWD-5, FWD-7. Contract `org/standards/NFRA_OPLGTW_CONTRACT.json` UNCHANGED (ruling R-4).

The harness exists: `infra/aws/ec2/opal-gateway/tests/acceptance/onhost_bench.py` (540 lines at drafting), written by
`OG-r-2`. So do its round-1 outputs:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/CAPACITY.json`,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/onhost-capacity.result.md` and the probe
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r2.py`. Read all three first. The earlier
result is context. It is NOT acceptance.

**Change 1 -- the memory grader reads the measurement on every path (repair R2-b; row `NFRA_OPLGTW-S48`, ruling
R-OG-24).** `onhost_bench.py:418-421`, at the bytes:

```
def _cap_respected(js):
    if js["ok"]:
        return js["peak_child_rss_bytes"] <= CONTRACT_JOB_MEMORY_BYTES
    return js["code"] in ("BUSY", "LIMIT_EXCEEDED")
```

A job that ended `LIMIT_EXCEEDED` is graded "respected" without its RSS being read. In round 1 the maximal job peaked at
282,021,888 bytes, against a cap of 268,435,456, and was graded True. Ruling R-OG-24: the bar is **"never exceeds"**.
`cap_respected` reads `peak_child_rss_bytes` on EVERY terminal path. A refusal is not compliance. Before you quote any
`cap_respected` verdict, census its consumers in `onhost_bench.py` and in your probe, and print the count. (At drafting,
`onhost_bench.py` read it at :432, :435, :439, :469, :485 and :491.)

**Change 2 -- the export arm goes through the real, streaming path.** Round 1 could not export end to end.
`onhost_bench.py:366-371` records the reason: the engine's export branch never returned `rows`, so
`SchwabService.export_query` failed (row `NFRA_OPLGTW-Z-S8`). The harness therefore called `run_export` and `write_csv`
separately. `OG-x-2` fixed the path and `OG-x-3` served it. Your export arm now calls the served code: `export_query` via
`export.generate_csv`, in process on the host, with synthetic principals and the synthetic fixtures. Run it at contract
scale: a fixture that matches 250,000 rows, with a CSV at or under 52,428,800 bytes. Run it again at one tenth of that.
Record both peaks.

**Change 3 -- AC4 is graded on the ruled windows (rows `NFRA_OPLGTW-W2-S10` and `NFRA_OPLGTW-S49`; rulings R-OG-23,
R-OG-23A, R-OG-23B, in `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md`; ruling Q5 @5676f4a48a).**
- The literal "zero failures" bar STANDS.
- The BASELINE window is the contiguous `2026-09-11T00:00:00Z .. 2026-09-18T00:00:00Z` (seven day-buckets).
- Q5 adds ONE post-release window of equal length ending at the cut: `2026-09-21T00:00:00Z .. 2026-09-28T00:00:00Z`
  (seven day-buckets). Both windows are printed with their request counts.
- A named incident DISQUALIFIES any window that contains it. Nothing is excised from inside a window.
- A clean-window claim prints TWO numbers: the failure count, and the traffic denominator.
- Instrument: CloudWatch `GetMetricStatistics`, namespace `AWS/ApplicationELB`, period 86400. Dimensions
  `LoadBalancer=app/opal-gateway/89166a68f337e5a4` and `TargetGroup=targetgroup/opal-gateway-tg/00997fc81f087cb8`.
  Metrics: `HTTPCode_Target_5XX_Count` (Sum), `RequestCount` (Sum), `TargetResponseTime` (SampleCount, p95).
- The BEFORE p95 is `OG-p-1`'s: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`
  `OGP1-AC11`, 0.5535024102704742 s over 2026-09-02T19:15Z..2026-09-16T19:15Z.

**Unchanged from OG-r-2, re-run and recorded:** the maximal and concurrent Unicode query fixtures, the deadlines, the
existing peak RSS on the host, the admission reserve (existing peak x 1.25 + 134,217,728), and the ALB `idle_timeout`
read. R-OG-24 point 5 asks for admission arithmetic priced against transient overshoot. Record the reserve twice:
once from the formula, once re-derived from the MEASURED peak child RSS of this run, printing both inputs. This cell
does NOT change admission code; a gap between the two is a finding row.

The PRD, verbatim (C5 capacity): *"Benchmark the actual candidate before enablement. Admission must reserve the measured
existing Gateway peak RSS plus 25 percent and 128 MiB operating headroom before starting a child, even below the global
job cap; insufficient headroom returns BUSY. A14 compares a declared identical existing-user workload before/after: no
failures and no more than 20 percent p95 latency regression, with workload, sample counts and measured window recorded.
If the target cannot satisfy the caps, return measured evidence for a PRD revision rather than activating with weakened
guarantees."*

Contract limits measured against: `job_memory_bytes` 268435456, `query_deadline_seconds` 30, `export_deadline_seconds`
30, `export_rows` 250000, `export_utf8_bytes` 52428800, `per_principal_jobs` 1, `global_jobs` 2, `queue_size` 0;
`capacity.admission_existing_peak_rss_multiplier` 1.25, `admission_os_reserve_bytes` 134217728,
`existing_workflow_p95_regression_max_fraction` 0.2.

**How the benchmark runs** (as in OG-r-2): through SSM on instance `i-07dccb1615503ac99`, in process, with synthetic
principal contexts and the synthetic fixtures from `infra/aws/ec2/opal-gateway/tests/acceptance/fixtures/`. No bearer
token is minted and no Schwab tool is enabled for any real principal.

**The probe** for every mechanical criterion except AC1 is
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/probes/og_r3.py`, which you write. It reads your
`CAPACITY.json`, prints the measurement with its vintage and denominator, then exactly one line: `VERDICT: PASS-OGR3-AC<n>`
or `VERDICT: FAIL-OGR3-AC<n> <reason>`.

## 2. BOUNDS

- **Grant.** Your write surface is the `<paths>` block below. `app/` is NOT granted: the gateway code is `OG-x-2`'s,
  and it is served by `OG-x-3`. A path you need that is not named is a BLOCKING surprise row -- never an override.
- **Worktree.** You work in the worktree named in your identity line (the same one as `OG-x-2`). Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **Interpreter.** `.venv-og` at your worktree root, as `OG-x-2` built it (if absent:
  `python -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt moto pytest`,
  permitted development egress under @7bfa5811c6). Never commit `.venv-og/` or `.scratch/`.
- **The benchmark changes nothing it did not bring.** It copies the harness and synthetic fixtures to a scratch
  directory on the host, runs, and removes them. It does not restart the service, change configuration, enable the
  integration, or write to the state store beyond isolated `RUNTIME#bench-og-r3-*` keys. A step that would need more
  is a BLOCKING row.
- **The benchmark runs the SERVED code.** Before it runs, confirm by md5 over SSM that the host's
  `/opt/opal-gateway/app/integrations/schwab/{engine,integration,export}.py` equal `EC2_MANIFEST.json`'s
  `deployed_commit` bytes, and that this commit is `OG-x-3`'s release or descends from it. If not, STOP: a BLOCKING row.
- **No real data.** Synthetic fixtures only. No Schwab object is read in this cell.
- **No egress off Opal infrastructure** beyond the venv download above: no call to Claude, Anthropic, an interactive
  Entra sign-in, or any vendor API. CloudWatch, ELBv2 and SSM reads are made through `.tools/aws`.
- **Contract numbers do not move** (ruling R-4). An INSUFFICIENT capacity is a measured result, not a failure to
  repair: record it (AC6). Never lower a limit or raise a cap to pass.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and
  reported with its measurement. Anything off-spec is one surprise row, and you keep working.
- **Numbers** in this order are context, never acceptance values, except where a criterion states one.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/acceptance/onhost_bench.py
infra/aws/ec2/opal-gateway/tests/acceptance/test_onhost_bench_grader.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W11-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

Six mechanical criteria: this is a WORLD measurement re-cut, not a build order; its one build act (the grader repair)
is one criterion.

<proof_of_spec>
  <criterion id="OGR3-AC1" cell_refs="OG-r-3"><invocation>timeout 110 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/acceptance/test_onhost_bench_grader.py::test_ogr3_ac01 -q -s -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
  <criterion id="OGR3-AC2" cell_refs="OG-r-3"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/probes/og_r3.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGR3-AC2(?![0-9])</expect></criterion>
  <criterion id="OGR3-AC3" cell_refs="OG-r-3"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/probes/og_r3.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGR3-AC3(?![0-9])</expect></criterion>
  <criterion id="OGR3-AC4" cell_refs="OG-r-3"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/probes/og_r3.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGR3-AC4(?![0-9])</expect></criterion>
  <criterion id="OGR3-AC5" cell_refs="OG-r-3"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/probes/og_r3.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGR3-AC5(?![0-9])</expect></criterion>
  <criterion id="OGR3-AC6" cell_refs="OG-r-3"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/probes/og_r3.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGR3-AC6(?![0-9])</expect></criterion>
</proof_of_spec>

- `OGR3-AC1` (`test_ogr3_ac01`) -- `onhost_bench._cap_respected` grades `{ok: False, code: "LIMIT_EXCEEDED",
  peak_child_rss_bytes: 282021888}` False and `{ok: False, code: "LIMIT_EXCEEDED", peak_child_rss_bytes: 200000000}`
  True, and the test prints the census of `cap_respected` consumers with its denominator.
- `OGR3-AC2` -- every benchmarked job on the host, whatever its outcome, peaks at or below 268,435,456 bytes of child
  RSS: the maximal query, the concurrent queries, and both export sizes. Each peak is printed.
- `OGR3-AC3` -- on the host, a 250,000-row export through `export.generate_csv` writes its CSV within 30 seconds, and its
  export and job files are gone afterwards.
- `OGR3-AC4` -- over the baseline window 2026-09-11T00:00Z..2026-09-18T00:00Z, `HTTPCode_Target_5XX_Count` is zero with
  `RequestCount` non-zero in every one of the seven day-buckets (both series printed), and that window's
  `TargetResponseTime` p95 regresses no more than 20 percent against `OGP1-AC11`'s 0.5535024102704742 s. The probe ALSO
  prints the post-release window 2026-09-21T00:00Z..2026-09-28T00:00Z's per-day 5XX count, request count and p95 (Q5);
  AC4 FAILS if that second window is not printed with its request counts.
- `OGR3-AC5` -- the ALB `idle_timeout`, read immediately before the benchmark with its ARN and UTC time, exceeds the
  30-second preparation deadline.
- `OGR3-AC6` -- `CAPACITY.json` carries a capacity verdict, SUFFICIENT or INSUFFICIENT. An INSUFFICIENT verdict carries
  its measurements in a `for_prd_revision_if_insufficient` block.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/NFRA_OPLGTW.TO-OG-r-3.onhost-capacity-recut.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>` BEFORE the `complete` flip. Result file
`onhost-capacity-recut.result.md` beside it must carry:
- the `cap_respected` consumer census;
- both export peaks and their ratio;
- the two admission reserves with their inputs;
- both AC4 windows, each with its request counts.

Flip `complete` only when every criterion PASSES by output. If a criterion measures FAIL, record it, leave the order
`pending`, and report.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~11, queue position 3; handed only after `OG-x-3` has shipped (edge x-3 -> r-3).
- Rows carried and disarmed by this cell's close: `S48` (AC1 + AC2), `W2-S10` and `S49` (AC4). Round-1 FAILs answered:
  OGR2-AC4 (the export at contract scale, now AC3) and OGR2-AC2 (now AC2 with the repaired grader).
- Q5 folded: the 09-11..09-17 baseline stays graded per R-OG-23A/B; the post-release window of equal length ending at the
  cut (09-21..09-27, seven buckets ending 2026-09-28T00:00Z) is printed with its request counts. Round 1's `OGR2-J1` is
  not carried: the round's judgment criterion sits on E1.
- The declared class is WORLD: an on-host benchmark on the production instance.

<status>staged</status>
<round>3</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
