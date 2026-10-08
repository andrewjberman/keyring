# COMP_USAGE -- is each comp-tool used? (census, 2026-10-08 ~22:0xZ)

Fork of 4.0.0_SA_CRO for Andrew-direct ~21:3xZ (record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_213xZ_COMP_TOOLS_AUDIT_DELETE_UNUSED_REVIEW_COMP_WHICH_ROUTER.md). READ-ONLY. Laptop. Windows: 7d = since 2026-10-01 ~22:0xZ, 30d = since 2026-09-08 ~22:0xZ.

## Population
- `.tools/comp-*` on disk: 105 entries = 99 distinct tools after folding `.py`/`.sh` twins (comp-deadgrant, comp-denytest, comp-firmsep-sweep, comp-surprise, comp-tagauthz, comp-whoread).
- Registry (org/modules/graph/TOOL_MASTER.yaml): 100 tools. Union: **100**. Registry-only: pipescript (no comp- file; the pipescript engine). Disk-only: none.
- Registry status: only comp-aws is `deprecated`; every other tool reads `active`.

## Sources (denominators and spans)

| Source | What one row is | Rows | Span (UTC) | Blind spot |
|---|---|---|---|---|
| `org/mcp/comp-tool-runs.jsonl` (laptop, gitignored) | one comp-tool run logged by `comp_log_auto.py` (serial, tool, rc), ANY caller: agent, hook, gate, another tool | 57582 | 2026-07-14T02:37 .. 2026-10-08T21:58 | laptop only; only tools whose wrapper calls comp_log_auto; caller kind not recorded |
| Claude Code transcripts (`~/.claude/projects/C--...-ajb-workspace/**/*.jsonl`, mtime within 30d) | a Bash/PowerShell tool_use whose command word is a comp-tool (AGENT-TYPED) | 435 files; 4134 commands carrying `comp-` text | 2026-09-09T12:30 .. 2026-10-08T21:59 | laptop only; no Codex seats; a form the parser misses (a tool inside a subshell string) is uncounted |
| `org/mcp/comp-which-rail.log` (laptop) | a rail decision: RUN-* (a comp-find/read/grep/glob run), ROUTE/ROUTE-POSTERIOR (comp-which routed a question TO a tool) | 114309 | 2026-06-22T12:56 .. 2026-10-08T21:59 | ROUTE-POSTERIOR includes routing-harness probes (comp-which-routing-test.py), so route counts overstate real asks |
| site Z rail log (archive `org/audit/archive/sitez/2026-10-08T170308Z/org_mcp_comp-which-rail.log`) | the same, site Z | 60328 | 2026-07-29T01:48 .. 2026-10-08T17:01 | the only cross-box usage source found; no dell1/dell2 archive exists; no site Z runs log is archived |
| Code callers (hooks, skills, CI, gates, in-use .tools) | a file that INVOKES the tool (shell command word, `.tools/<tool>`, or a quoted name in .py) | -- | HEAD | catalogs, registries, docs and the tool's own engine module excluded |

tool_activity (S3 parquet) was not read: it is laptop-only, 3-hourly and overwrites its keys, so it adds nothing the two laptop sources lack.

## Classes (denominator 100)

- **ACTIVE 24** -- run in the last 7 days (agent-typed or a logged run)
- **OCCASIONAL 27** -- run in the last 30 days, not the last 7
- **WIRED-ONLY 7** -- no run in 30 days, but a hook, skill, gate, CI job or in-use tool invokes it
- **DORMANT 41** -- no run in 30 days in any source, and nothing in use invokes it
- **DEPRECATED 1** -- the registry's own status

## Per tool

ag = agent-typed (transcripts); run = logged runs, any caller; rail = rail RUN-* lines (laptop + site Z); route = times comp-which routed a question TO it (30d, incl. harness probes); fail = nonzero rc / runs (30d).

| tool | ag 7d | ag 30d | run 7d | run 30d | rail 30d | route 30d | fail 30d | callers 30d | last run | wired by | class |
|---|---|---|---|---|---|---|---|---|---|---|---|
| comp-read | 2 | 804 | 37 | 4890 | 5774 | 1871 | 67/4890 | 53 | 2026-10-08 | skill:SKILL.md,SKILL.md; hook:pipescript-suite-check.sh; tool:comp-adversary,comp-find | ACTIVE |
| comp-pulse | 0 | 2 | 2700 | 10245 | 0 | 185 | 4925/10245 | 130 | 2026-10-08 | - | ACTIVE |
| comp-find | 50 | 1713 | 213 | 2668 | 5348 | 1436 | 41/2668 | 70 | 2026-10-08 | skill:SKILL.md; hook:pipescript-suite-check.sh | ACTIVE |
| comp-which | 39 | 183 | 88 | 4863 | 515 | 0 | 2027/4863 | 54 | 2026-10-08 | skill:SKILL.md,SKILL.md; gate:commit_gate_runner.py; tool:comp-routable-check | ACTIVE |
| comp-iam | 7 | 129 | 29 | 154 | 0 | 706 | 26/154 | 20 | 2026-10-08 | skill:SKILL.md,SKILL.md; tool:comp-secrets | ACTIVE |
| comp-surprise | 2 | 56 | 14 | 159 | 0 | 0 | 11/159 | 15 | 2026-10-07 | skill:SKILL.md,SKILL.md | ACTIVE |
| comp-kuzu | 9 | 41 | 37 | 94 | 0 | 400 | 8/94 | 12 | 2026-10-08 | skill:SKILL.md,SKILL.md; tool:comp-estate,comp-find | ACTIVE |
| comp-pipescript | 0 | 12 | 44 | 121 | 0 | 265 | 50/121 | 18 | 2026-10-08 | skill:SKILL.md,SKILL.md; hook:deploy-pipescript-check-post-commit.sh,pipescript-suite-check.sh; tool:comp-heat | ACTIVE |
| comp-routes | 2 | 22 | 8 | 72 | 0 | 213 | 0/72 | 14 | 2026-10-08 | skill:SKILL.md,SKILL.md | ACTIVE |
| comp-adversary | 0 | 35 | 3 | 41 | 0 | 0 | 0/41 | 14 | 2026-10-07 | skill:SKILL.md | ACTIVE |
| comp-system | 7 | 27 | 19 | 48 | 0 | 172 | 21/48 | 13 | 2026-10-08 | gate:safe-commit.sh | ACTIVE |
| comp-blast | 1 | 13 | 10 | 48 | 0 | 93 | 22/48 | 19 | 2026-10-08 | skill:SKILL.md,SKILL.md | ACTIVE |
| comp-lambdamap | 0 | 1 | 25 | 49 | 0 | 539 | 10/49 | 12 | 2026-10-08 | - | ACTIVE |
| comp-estate | 0 | 7 | 6 | 33 | 0 | 658 | 19/33 | 15 | 2026-10-08 | skill:SKILL.md,SKILL.md | ACTIVE |
| comp-diff | 0 | 0 | 3 | 32 | 0 | 111 | 2/32 | 11 | 2026-10-08 | - | ACTIVE |
| comp-trigger | 0 | 12 | 1 | 11 | 0 | 23 | 2/11 | 7 | 2026-10-08 | - | ACTIVE |
| comp-which-routing-test | 3 | 11 | 0 | 0 | 0 | 0 | - | 3 | 2026-10-08 | tool:comp-routable-check | ACTIVE |
| comp-tagauthz | 1 | 8 | 0 | 0 | 0 | 64 | - | 4 | 2026-10-08 | gate:safe-apply.sh | ACTIVE |
| comp-coverage-check | 2 | 6 | 0 | 0 | 0 | 0 | - | 2 | 2026-10-08 | gate:safe-commit.sh | ACTIVE |
| comp-activity | 3 | 3 | 2 | 2 | 0 | 39 | 0/2 | 1 | 2026-10-08 | - | ACTIVE |
| comp-trace | 0 | 0 | 1 | 5 | 0 | 24 | 2/5 | 5 | 2026-10-08 | - | ACTIVE |
| comp-graph | 1 | 1 | 2 | 2 | 0 | 35 | 0/2 | 1 | 2026-10-08 | skill:SKILL.md | ACTIVE |
| comp-xref | 0 | 0 | 1 | 3 | 0 | 35 | 1/3 | 3 | 2026-10-08 | - | ACTIVE |
| comp-routable-check | 2 | 2 | 0 | 0 | 0 | 0 | - | 1 | 2026-10-08 | - | ACTIVE |
| comp-schedule | 0 | 25 | 0 | 0 | 0 | 30 | - | 11 | 2026-09-24 | skill:SKILL.md,SKILL.md | OCCASIONAL |
| comp-keys | 0 | 2 | 0 | 20 | 0 | 69 | 4/20 | 4 | 2026-10-01 | - | OCCASIONAL |
| comp-manifest-check | 0 | 10 | 0 | 6 | 0 | 203 | 3/6 | 2 | 2026-09-18 | gate:commit_gate_runner.py; ci:drift-producer-push.yml | OCCASIONAL |
| comp-transform | 0 | 3 | 0 | 11 | 0 | 196 | 8/11 | 5 | 2026-09-28 | skill:SKILL.md,SKILL.md | OCCASIONAL |
| comp-iam-usage | 0 | 1 | 0 | 10 | 0 | 119 | 0/10 | 3 | 2026-09-24 | - | OCCASIONAL |
| comp-pydeps | 0 | 0 | 0 | 10 | 0 | 69 | 3/10 | 3 | 2026-09-23 | - | OCCASIONAL |
| comp-cluster | 0 | 5 | 0 | 4 | 0 | 179 | 2/4 | 2 | 2026-09-21 | - | OCCASIONAL |
| comp-secrets | 0 | 8 | 0 | 0 | 0 | 73 | - | 2 | 2026-09-22 | gate:commit_gate_lib.sh | OCCASIONAL |
| comp-dataflow | 0 | 1 | 0 | 5 | 0 | 74 | 0/5 | 4 | 2026-09-23 | - | OCCASIONAL |
| comp-heat | 0 | 6 | 0 | 0 | 0 | 26 | - | 2 | 2026-10-01 | - | OCCASIONAL |
| comp-state | 0 | 6 | 0 | 0 | 0 | 87 | - | 3 | 2026-10-01 | skill:SKILL.md; hook:closeout-comp-state-post-commit.sh; tool:comp-adversary | OCCASIONAL |
| comp-directives | 0 | 4 | 0 | 1 | 0 | 31 | 0/1 | 3 | 2026-10-01 | skill:SKILL.md | OCCASIONAL |
| comp-freshness | 0 | 5 | 0 | 0 | 0 | 303 | - | 4 | 2026-10-01 | - | OCCASIONAL |
| comp-platinum | 0 | 1 | 0 | 4 | 0 | 91 | 0/4 | 2 | 2026-09-18 | skill:SKILL.md,SKILL.md | OCCASIONAL |
| comp-cache | 0 | 1 | 0 | 3 | 0 | 39 | 0/3 | 3 | 2026-09-15 | - | OCCASIONAL |
| comp-closure | 0 | 2 | 0 | 2 | 0 | 85 | 0/2 | 1 | 2026-10-01 | - | OCCASIONAL |
| comp-xray | 0 | 0 | 0 | 4 | 0 | 128 | 0/4 | 1 | 2026-10-01 | - | OCCASIONAL |
| comp-legacywriter | 0 | 1 | 0 | 2 | 0 | 38 | 0/2 | 1 | 2026-09-18 | skill:SKILL.md | OCCASIONAL |
| comp-registry | 0 | 0 | 0 | 3 | 0 | 33 | 1/3 | 1 | 2026-09-22 | skill:SKILL.md | OCCASIONAL |
| comp-similar | 0 | 3 | 0 | 0 | 0 | 103 | - | 2 | 2026-09-09 | - | OCCASIONAL |
| comp-build | 0 | 0 | 0 | 2 | 0 | 13 | 0/2 | 1 | 2026-09-15 | - | OCCASIONAL |
| comp-validate | 0 | 0 | 0 | 2 | 0 | 28 | 1/2 | 2 | 2026-09-29 | skill:SKILL.md,SKILL.md | OCCASIONAL |
| comp-atomcheck | 0 | 0 | 0 | 1 | 0 | 50 | 0/1 | 1 | 2026-09-14 | - | OCCASIONAL |
| comp-describe | 0 | 1 | 0 | 0 | 0 | 33 | - | 1 | 2026-09-09 | - | OCCASIONAL |
| comp-ledger-agreement | 0 | 1 | 0 | 0 | 0 | 0 | - | 1 | 2026-09-09 | - | OCCASIONAL |
| comp-symbols | 0 | 1 | 0 | 0 | 0 | 1625 | - | 1 | 2026-09-10 | - | OCCASIONAL |
| comp-types | 0 | 0 | 0 | 1 | 0 | 28 | 0/1 | 1 | 2026-09-23 | - | OCCASIONAL |
| comp-constants | 0 | 0 | 0 | 0 | 0 | 40 | - | 0 | 2026-08-05 | gate:commit_gate_runner.py (engine import: comp_constants_cli) | WIRED-ONLY |
| comp-glob | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | tool:comp-routable-check | WIRED-ONLY |
| comp-grep | 0 | 0 | 0 | 0 | 0 | 23 | - | 0 | never logged | tool:comp-routable-check | WIRED-ONLY |
| comp-missions | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | hook:missions-refresh-post-commit.sh | WIRED-ONLY |
| comp-pii | 0 | 0 | 0 | 0 | 0 | 37 | - | 0 | 2026-07-25 | skill:SKILL.md | WIRED-ONLY |
| comp-shell | 0 | 0 | 0 | 0 | 0 | 37 | - | 0 | never logged | gate:commit_gate_runner.py (engine import: shell_cli) | WIRED-ONLY |
| pipescript | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | 2026-07-29 | gate:commit_gate_runner.py | WIRED-ONLY |
| comp-arity | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-assets | 0 | 0 | 0 | 0 | 0 | 77 | - | 0 | 2026-09-04 | - | DORMANT |
| comp-axes | 0 | 0 | 0 | 0 | 0 | 66 | - | 0 | never logged | - | DORMANT |
| comp-canon-motif | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-chainrun | 0 | 0 | 0 | 0 | 0 | 35 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-claimlink | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-clobber | 0 | 0 | 0 | 0 | 0 | 224 | - | 0 | never logged | - | DORMANT |
| comp-cochange | 0 | 0 | 0 | 0 | 0 | 26 | - | 0 | 2026-08-26 | - | DORMANT |
| comp-coverage | 0 | 0 | 0 | 0 | 0 | 34 | - | 0 | 2026-09-04 | - | DORMANT |
| comp-deadgrant | 0 | 0 | 0 | 0 | 0 | 11 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-debris | 0 | 0 | 0 | 0 | 0 | 12 | - | 0 | 2026-09-04 | - | DORMANT |
| comp-denytest | 0 | 0 | 0 | 0 | 0 | 42 | - | 0 | 2026-09-03 | - | DORMANT |
| comp-depth | 0 | 0 | 0 | 0 | 0 | 15 | - | 0 | never logged | - | DORMANT |
| comp-dispatch | 0 | 0 | 0 | 0 | 0 | 71 | - | 0 | never logged | - | DORMANT |
| comp-drift | 0 | 0 | 0 | 0 | 0 | 38 | - | 0 | 2026-09-02 | - | DORMANT |
| comp-dups | 0 | 0 | 0 | 0 | 0 | 35 | - | 0 | never logged | - | DORMANT |
| comp-fedobs | 0 | 0 | 0 | 0 | 0 | 36 | - | 0 | never logged | - | DORMANT |
| comp-firmsep-sweep | 0 | 0 | 0 | 0 | 0 | 32 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-genesis | 0 | 0 | 0 | 0 | 0 | 33 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-gitdrill | 0 | 0 | 0 | 0 | 0 | 24 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-honesty | 0 | 0 | 0 | 0 | 0 | 56 | - | 0 | never logged | - | DORMANT |
| comp-icedrill | 0 | 0 | 0 | 0 | 0 | 16 | - | 0 | 2026-08-26 | - | DORMANT |
| comp-imgread | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-incrparity | 0 | 0 | 0 | 0 | 0 | 10 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-kit-striplist-gate | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-learns-score | 0 | 0 | 0 | 0 | 0 | 64 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-learns-status | 0 | 0 | 0 | 0 | 0 | 44 | - | 0 | never logged | - | DORMANT |
| comp-lease | 0 | 0 | 0 | 0 | 0 | 222 | - | 0 | 2026-09-04 | - | DORMANT |
| comp-ontolint | 0 | 0 | 0 | 0 | 0 | 10 | - | 0 | 2026-08-26 | - | DORMANT |
| comp-parity | 0 | 0 | 0 | 0 | 0 | 37 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-passcraft | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-perf | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-residue | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-stitch-refresh | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-to | 0 | 0 | 0 | 0 | 0 | 72 | - | 0 | never logged | - | DORMANT |
| comp-tool-health | 0 | 0 | 0 | 0 | 0 | 34 | - | 0 | never logged | - | DORMANT |
| comp-tool-health-gate | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-toolgraph | 0 | 0 | 0 | 0 | 0 | 22 | - | 0 | never logged | - | DORMANT |
| comp-tooltip | 0 | 0 | 0 | 0 | 0 | 20 | - | 0 | 2026-07-25 | - | DORMANT |
| comp-v5-composite-test | 0 | 0 | 0 | 0 | 0 | 0 | - | 0 | never logged | - | DORMANT |
| comp-whoread | 0 | 0 | 0 | 0 | 0 | 32 | - | 0 | never logged | - | DORMANT |
| comp-aws | 0 | 18 | 0 | 7 | 0 | 7 | 0/7 | 6 | 2026-09-22 | - | DEPRECATED |

## Signals worth a second look

- **The 10 most used (30d, ag+run+rail):** comp-read (11468), comp-pulse (10247), comp-find (9729), comp-which (5561), comp-iam (283), comp-surprise (215), comp-kuzu (135), comp-pipescript (133), comp-routes (94), comp-adversary (76).
- **Mostly machine-driven (runs >= 50, agent-typed <= 5%):** comp-pulse (ag 2 / run 10245), comp-which (ag 183 / run 4863). Their use is a hook's or gate's, not a seat choosing them.
- **Routed to, never run (route 30d >= 20, no run in 30d):** comp-clobber (224), comp-lease (222), comp-assets (77), comp-to (72), comp-dispatch (71), comp-axes (66), comp-learns-score (64), comp-honesty (56), comp-learns-status (44), comp-denytest (42), comp-constants (40), comp-drift (38), comp-parity (37), comp-pii (37), comp-shell (37), comp-fedobs (36), comp-chainrun (35), comp-dups (35), comp-coverage (34), comp-tool-health (34), comp-genesis (33), comp-firmsep-sweep (32), comp-whoread (32), comp-cochange (26), comp-gitdrill (24), comp-grep (23), comp-toolgraph (22), comp-tooltip (20). Either the routes are harness probes, or comp-which recommends tools agents then do not run -- a question for the router review.
- **High nonzero-exit rate (>= 25%, runs >= 10):** comp-transform 8/11, comp-estate 19/33, comp-pulse 4925/10245, comp-blast 22/48, comp-system 21/48, comp-which 2027/4863, comp-pipescript 50/121, comp-pydeps 3/10. A nonzero rc is not always a failure (some tools exit nonzero on a finding); read each tool's output contract.

## Not read

- dell1, dell2 and site Z transcripts and runs logs: cross-box usage is the site Z rail log only. A tool used only on another box can read DORMANT here.
- Codex seats' usage (no Claude transcripts).
- Whether each tool still WORKS: no tool was executed by this census; fail rates are logged rc only.
- The routing harness's share of ROUTE-POSTERIOR lines was not separated out.
- Wiring is a text match for an invocation form: a dynamic call (a name built at run time) is missed, and a quoted name used as data can read as a caller.
