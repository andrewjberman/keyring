# NFRA_COMPDRIFT P3(a)+(b) + NFRA_GRAPHUNI Phase-B compute prep (lane ~D)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Current State
COO~B GO'd P3 (023154Z) and the full dispatch is executed + ACCEPTED (024415Z). 3 commits this
window, all pushed to CLOUD (through 62063ee60). COMPDRIFT is now essentially COMPLETE (P1+P2+P3ab);
Phase-B compute producer is fold-ready + staged.

**P3(a) -- `f988cc667` (ACCEPTED, "textbook grounding doctrine").** GROUNDING REFUTED MY OWN EARLIER
FINDING: there was NO comp-heat bug. Ran comp-heat drift isolated -> valid JSON, rc0, 118 uncommitted
writes; comp-heat + its object_freshness engine use git + os.path.getmtime, ZERO `find`. The
"find: missing -mtime" I'd reported was a CAPTURE ARTIFACT of an earlier background diagnostic, not a
comp-heat defect (Rule-22: I'd grounded a symptom + inferred a mechanism; caught it by running the
engine isolated BEFORE touching anything). THE REAL DEFECT (mine): `drift_cli.py` `_bash()` forced
EVERY seam engine through `bash <file>`, but comp-heat + comp-freshness are `#!/usr/bin/env python3` --
`bash <pyfile>` mis-parses + HANGS (2min -> `_run` timeout rc124 -> false UNVERIFIABLE). FIX: added
`PYTHON_EXE` + `_interp(tool_path)` that dispatches by shebang (python tools -> python, bash tools ->
bash). Also fixed the comp-freshness INVOCATION (no-arg just prints help+exit2; the real full sweep is
`comp-freshness all`, single = `artifact <s3_prefix>`) + a 300s budget (heaviest --deep leg: live S3 x3
+ full DDB). VERIFIED end-to-end via a direct-adapter harness: comp-heat seam-1 -> UNCOMMITTED (118, real,
was UNVERIFIABLE-by-hang); comp-freshness -> STALE (exit1, real -- so the aea677899 exit-code parse-logic
was correct but had NEVER executed until this invocation fix).

**P3(b) -- `c58c59e0c` (ACCEPTED).** Per-seam BEHIND verdict-severity split. Added a `stale` verdict-class
(`BEHIND`/`VINTAGE-STALE` -> WARN, exit-CLEAN, ACTION=refresh) to `_classify`/`_record`/`ACTION`;
`adapter_comp_kuzu_provenance` now emits `SELF-HEALING` for its behind case (the marker oracle
auto-re-derives on next read -> self_heal/OK). So comp-kuzu BEHIND (self-healing) and code_heat BEHIND
(genuinely vintage-stale, needs manual re-derive) no longer BOTH fall through to clean/OK -- the WARN now
surfaces the drift that needs action while the self-healer stays quiet. VERIFIED: code_heat BEHIND->stale/WARN,
comp-kuzu SELF-HEALING->self_heal/OK, `rollup_exit([stale,self_heal])`=0 (CLEAN, surfaced-not-gated),
`[stale,break]`=1 (BREAK dominates), live comp-kuzu->current no-crash.

**P3(c) -- HELD on Trino** (COO~B), no action. **COMPDRIFT net:** parse-hardened 7/7 (prior window) +
invocation-fixed (shebang) + severity-nuanced = comp-drift --deep is trustworthy AND executable AND
actionable (COO~B: "production-grade state-verb tool").

**Phase-B compute PREP -- `62063ee60` (ACCEPTED, fold-ready).** Generated the `--full` compute producer
(`infra/aws/globgrph/extract_gold_compute.py --full`): 1347 nodes / 3555 edges (+112 read-only-input
READS_S3 vs Phase-A's 169-write set), **0 UNRESOLVED**. Added a source-grounded, reader-SCOPED
cross-firm-read override (`_READ_OVERRIDE = {("mdpf","gold/timeseries/client_performance.parquet"):"inf"}`)
-- grounded on `build_mdpf_inflection_history_from_spine.py` reading `s3://opal-data-INF/...`, per the
ratified one-key-one-node cross-firm-read rule; it resolves the 2 tri-firm mdpf ambiguities that were in
the Phase-A rollup (Phase-A now also 0-unresolved). Producer staged LOCAL (scratch), deliberately NOT
emitted to S3 -- a premature emit would DANGLE the read-edges against ~A-storage / portal-etfs-slice
targets not yet present. Emit + co-sign the {~D,~A,~B} convergence at the ONE coordinated ~B-fired
Phase-B derive.

## Compiler Tools
| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-heat drift (isolated + via adapter) | ground-truth the phantom "bug" + verify the shebang fix | PASS | refuted the find-mtime finding (works clean); post-fix adapter -> UNCOMMITTED (real, was UNVERIFIABLE-by-hang). |
| comp-freshness (adapter, `all`) | verify shebang+invocation fix end-to-end | PASS | -> STALE (exit1, real) -- proved the aea677899 logic now actually executes. |
| comp-kuzu (adapter) | live provenance post-P3b | PASS | -> current (HEAD==marker); the BEHIND->SELF-HEALING path unit-verified. |
| (source-ground) .tools/comp-heat, object_freshness.py, iam_cli.py, comp-freshness argparse | Rule-22 shebang + invocation + reconcile-vocab grounding | PASS | grounded every fix in source before editing; found the real python-vs-bash root cause. |
| python (extract_gold_compute --full/--stats) | generate + verify Phase-B producer | PASS | 1347n/3555e, +112 edges, 0-unresolved after the override. |

**What worked:** running the engine ISOLATED before fixing refuted a false finding (Rule-22) -- and the
real root cause (python-tool-via-bash hang) was more impactful than the phantom would have been (it fixed
comp-heat AND comp-freshness, and revealed the freshness parse-logic had never executed). Grounding each
invocation/vocab in source (not inference) is what surfaced the wrong-vocab + wrong-invocation defects.
**What failed:** nothing regressed; the earlier comp-heat "finding" was a mis-attribution, caught + retracted
inside the fleet before it reached the NFRA_HEATMAP owner (COO~B was the router, never forwarded).
**Gap found:** comp-freshness `all` is the heavy --deep leg (>120s live S3x3+DDB) -- given a 300s budget;
exceeds -> UNVERIFIABLE-by-timeout (honest, never-silent).

## MCP Traffic
~7 dispatches. Significant: COO~B correction-ACCEPTED (Rule-22 model) + GO P3(b); COO~B P3(a)+(b) ACCEPTED
+ Phase-B prep ACCEPTED + hold-is-correct + GRANTS_S3 sequencing confirmed; ~B GRANTS_S3 capability-edge
enhancement (queued, mine, CTO-arch-gated) -> my ACK. No open questions routed to me.

## Blockers
None assumption-BLOCKED. COO~B EXPLICITLY validated the hold as correct (not a coast-failure): all
addressable ~D work is DONE; the remainder is genuinely externally-gated -- Phase-B fire (~B respawn +
gate-lift, CVO in flight/imminent), P3c (Trino surface), GRANTS_S3 (CTO arch + post-Phase-B). Real gates,
each stated.

## Next Steps
1. **[3.0.0_SA_CVO~B / 2.0.0_SA_COO~B]** the N-party /seams gate-lift (CVO in flight) -> then ~B fires the
   ONE coordinated Phase-B derive.
2. **[0.8.0_AE_CloudComp~B]** on respawn + gate-lift: fire the Phase-B derive folding ~A-storage-PhaseB +
   ~D-compute-PhaseB (staged, fold-ready) + ~B ARN-fixed lambda edges. I priority-interrupt to emit my
   producer + co-sign convergence at that fire.
3. **[0.8.0_AE_CloudComp~D]** post-Phase-B: (a) open the GRANTS_S3 CTO arch-Q (node-key form + POLICY-vs-ROLE
   grain + the firm-separation invariant) when COO~B sequences it; (b) COMPDRIFT P3(c) seam-6 Trino closers
   when the heat-federation surface lands.
