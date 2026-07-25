# CVO~Z session log — 2026-07-25, Lane-A verdict + OPT1 ruling + the path-convention CLASS finding

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`

---

## 1 · Lane-A (`0.8.0_AE_CloudComp~A`) @`6fbc02911d` — verified; map s6 CONFIRMED resolved

**Denominator:** 21 sidecar rows reconcile to the claimed 18 exactly — 18 DISTINCT tools + 2 positive-control
rows + 1 supplementary subcommand row. Primary tally re-derived: MATCH 8 / MISMATCH 6 / MATCH-but-flagged 1
/ UNKNOWN 3 = 18.

**The 24-residual closure — the highest-stakes claim — HOLDS.** Pulled 3 of the 6 teardown commits myself
rather than reading the report's summary: `9781bbb266` (confirms the COMBINED bd teardown — both
freshness-probe and served-vintage-alarm in one commit, exactly as claimed), `dd7d2da955` (11 destroy, CTO
GO 211316Z), `e836f4c89a` (22 destroy, CTO GO 225710Z). All verbatim, all `0.7.0_AE_CloudOps`, 2026-07-17.
Verified the other citation TYPE too: `infra/aws/terraform/data-refresh/main.tf:34-36` really is
`module "data_refresh_api"` / `function_name = "opal-data-refresh-api"`. Counts close: 12+6+6=24, 0
unresolved.

**The closure DEFUSES the sixth through-line instance rather than confirming it.** "9 undeployed guard
dirs" read as 9 silent non-deployments; in fact 6 were deployed then **deliberately** torn down under
explicit CTO GO in an Andrew-directed clean-house, each self-describing as git-recoverable, with
never-deployed correctly distinguished by the ABSENCE of a teardown commit. `9781bbb266` even strips a
"phantom cluster … config-declared/never-applied" — that clean-house was itself removing through-line-class
debris. **EPISTEMIC LIMIT recorded because the adjacency is tempting:** the 07-17 teardowns removed
freshness/absence guards and we are today finding an absent-input blind spot. **I have NOT established any
relationship** — different planes (CloudWatch/Lambda guards vs comp-tool CLI exit codes). Noted only so
nobody later "discovers" it as a hidden link.

**comp-dups re-derived — and it is NOT on the disclosure scale at all.** My own invalid value ->
`TRUE_RC=0`, stderr carried only an unrelated SOVEREIGN HOLD line, stdout ran the **complete unfiltered
scan** (60 lines, 15 real TF label collisions) with zero acknowledgment the filter was invalid. The 3-point
disclosure scale measures how well a tool discloses an EMPTY result; **comp-dups returns a FULL, real,
authoritative result set answering a DIFFERENT QUESTION than the one asked.** Recommended a separate axis
(FILTER-IGNORED / SCOPE-COERCED) — a reader who asked for class X and saw 15 collisions will reasonably
believe those are class-X collisions. ~A concurred.

**comp-lambdamap re-derived:** `TRUE_RC=1` with a named, citation-bearing DRIFT report → genuinely LOUD, not
a subcommand artifact (answering ~A's own question). **Incidental live finding, routed out:** 6 real current
drifts — 3 WRONG_SOURCE_DIR (seeking-alpha) + 3 MISSING_ENTRY (`find-insure-crawl-job-posting-{board}`,
`m365-ms-ingest-liveness`, `opal-49f-value-parity`), the latter being live **Deployment Rule 4** violations.
Routed to CTO~Z for 0.7.0/DT; outside my lane and outside TOOLUNIFY scope.

**Finding against the deliverable (since fixed):** all 21 rows had `stdout_excerpt`/`stderr_excerpt` null
while the schema carried the fields and the delivery message asserted they were populated —
"verifiable from the record" vs "re-runnable" is a real difference. ~A fixed it (21/21 now populated,
verified) and root-caused it properly, which fed straight into §3.

## 2 · NFRA_GRAPHUNI OPT1 — refutation accepted; I refuted my OWN mechanism

**SET-IDENTITY REFUTED (11/28).** ~D's member-level run refuted my count reconciliation, stated as a
refutation rather than softened. **The hold was worth its cost:** had we wired on 192+112+2=306, we would
have landed a still-under-covering graph wearing a green count. Count- and member-equivalence came apart
exactly where I flagged they might, and only the member test could show it. Sharp case 5 vs expected 216
(worse than the marker-head's 13); function-level 39/39 exact for the third time.

**I formed a mechanism for ~D's open `find_node` residual, tested it, and KILLED IT.** `trace_graph.py:271-275`
is a case-insensitive SUBSTRING match on id-or-label, so I hypothesised seed-set inflation — a script-level
query also matching every function child, making "216" a multi-seed union whose size varies with node
population/id form, which would have made the sharp case an artifact and my endorsement of the
set-difference wrong. **Measured instead of asserted:**
```
fixture   gold:D_01.partner_analytics -> 43 matching nodes
producer  gold:D_01.partner_analytics -> 43 matching nodes
```
Identical — and identical for the very reason I expected to break it: `gold:D_01.partner_analytics` IS a
substring of `pipeline:bd:gold:D_01.partner_analytics`, so id-namespace prefixing does NOT defeat the match.
**Hypothesis refuted.** What it buys: nodes and seeds are provably equivalent, so the 216→5 collapse
**cannot be nodes or seeds — it is edges.** ~D's residual is NARROWED, not closed; I eliminated only my own
candidate and said so in those words.

**RULING:** endorsed CTO~Z's member-level set-difference shape — **the objection I would have raised is the
one I just retired.** Two additions: (a) partition missing members by the EDGE CLASS they ride on (since
nodes/seeds are equal, the distribution directly discriminates READS-adjacency vs transitive depth vs
another family); (b) run the FUNCTION-level case as a CONTROL in the same pass — 39/39 on three independent
paths makes it the trustworthy comparator, so function-clean + script-deficit would be conclusive while
function-grain gaps would indict the method. Ingestion stays hard-gated.

Also accepted CTO~Z's self-correction that ~D's run does NOT discriminate Kuzu contention (never touches the
Kuzu substrate) — I had accepted that sequencing without checking the substrate claim, so I was a step
behind them there.

## 3 · CLASS FINDING — three coexisting path conventions, 4 instances, 3 silent

~A's root cause was the fourth instance of one class today. **Verified with my own positive control:**
```
python3 -> C:\...\Python312\python3.exe   (platform: win32 -- NATIVE Windows Python)
os.path.exists('/cygdrive/c/.../CLAUDE.md') -> False
os.path.exists('C:/.../CLAUDE.md')          -> True
```
| # | Instance | Form used | Failure |
|---|---|---|---|
| 1 | my inbox Monitor script path | `/c/...` | exit 127 — **LOUD** (the only one) |
| 2 | stitch post-commit hook | `/c/...` | stderr, but hook `exit 0`s → **SILENT**; producer dead 17 days |
| 3 | harness wrapper cwd file | `/c/...` | appends failure → corrupts every Bash exit code, **SILENT** |
| 4 | ~A's sidecar builder | `/cygdrive/c/...` → native Python | `os.path.exists` False → 42 null fields, **SILENT** |

**Three of four silent, each returning a plausible falsy value (exit 0, a False, a null) rather than an
error** — the census's own through-line, sitting at the ENVIRONMENT layer beneath every lane's instruments.
Instances 3 and 4 corrupted census evidence directly. **The direction FLIPS at #4** (bash can't read `/c/`;
native Python can't read `/cygdrive/c/`), which is why four agents each read their own instance as a local
quirk and nobody generalised until the flip forced "how many conventions ARE there."

**One-line rule that closes all four: any path crossing a tool boundary on this host uses the native
`C:/...` form, obtained from `git rev-parse --show-toplevel`.** Both bash and native Python consume it.
That is why CTO~Z's `fbc91c6e28` fix was robust rather than merely working — it sidesteps the mount table
instead of picking a convention and hoping.

## 4 · Kuzu discriminator RESOLVED — contention, not degradation

Base lane's serial re-run verified on my own run: own `ps` substrate check empty (quiet), own timed
`comp-kuzu` with my own nonexistent type -> **TRUE_RC=1, 3s** against the original 60s AND 240s double
timeout (base measured 2.74s). ~80x delta, contention explains it fully; no degradation thread needed. The
4 deferred rows come out of deferral: 3 resolve to verdicts, comp-canon-motif correctly
NOT-A-FAIR-TEST-THIS-RUN (intended STALE mutation didn't manifest — they declined the convenient verdict).
Base also reported own-batch-only counts and deferred the cross-lane total, **one message after the
mitigation was adopted, unprompted.**

**THE ANALYTICAL POINT FOR SYNTHESIS — the register's `failure_mode` is wrong in BOTH directions.**
Under-declared: 8 declared-LOUD → observed quieter (ABSENT axis). Over-declared: reverse-polarity
declared-FAIL-OPEN → observed LOUD, accumulating across lanes (base: comp-kuzu/-inc/cluster/pipescript;
B: comp-pydeps/residue/imgread; A: comp-lambdamap). **Bidirectionality is a different finding, not a bigger
one, and it changes the remedy: a column wrong in ONE direction can be systematically corrected; a column
wrong in BOTH has no bias to correct — it is NOISE, so no global fix exists and each row is only as good as
its individual verification.** Recommended this sit ABOVE either direction's instance count in the
synthesis, because counts invite "which way is it biased" and the answer is neither.

## 5 · Queue (disclosed, not assumed)

REC1C_E, base's remaining MATCH rows, and REC1C_B remain **unverified**. Production is over (B was the last
batch), so the queue is bounded. CTO~Z ruled: no second verifier, compressions endorsed (full re-derivation
on every MISMATCH + every count claim; MATCHes ~1-in-4; static-source-citation rows read not re-run), drain
at honest pace.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `git log -1` × 3 teardown commits + `sed` on `main.tf` | PASS | map s6 load-bearing citations verified verbatim, not from the report's summary |
| Python (own parsers) × 3 sidecars | PASS | lane-A 21→18 denominator, OPT1 counts, base re-run block |
| `comp-dups` / `comp-lambdamap` (own probes) | PASS — 2 findings | silent scope-coercion confirmed; 6 live source-map drifts surfaced incidentally |
| Python over fixture + producer node ids | **PASS — refuted my own hypothesis** | 43 = 43 seeds; killed the seed-inflation mechanism, narrowing ~D's residual to edges |
| `python3 -c os.path.exists` (both path forms) | PASS — class characterised | native-Windows-Python mechanism confirmed by positive control |
| `ps` + timed `comp-kuzu` (own run) | PASS | TRUE_RC=1 at 3s vs prior 240s timeout — contention discriminator resolved |

**Own errors recorded this pass:** (1) hypothesised seed-set inflation for the `find_node` residual and
refuted it by my own measurement; (2) accepted CTO~Z's Kuzu-discriminator sequencing without checking the
substrate claim, and they corrected themselves before I did.
