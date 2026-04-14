# Compiler Tools Directive (comp-*)

**Read this ONCE, internalize it, never forget it.**

You have compiler tools that map the entire system — frontend, API, Lambda, S3, gold scripts, EventBridge, CloudFront — as a single directed graph. They are deterministic, fast (<2s), and always correct. There are also pre-deploy gates that verify correctness before artifacts reach S3.

## Your investigation protocol (in this order):

1. **FIRST:** Run `comp-trace` or `comp-blast` for ANY question about how things connect, what depends on what, or what a change affects.
2. **SECOND:** If comp-* doesn't answer your question, use Grep/Glob/Read directly.
3. **NEVER:** Spawn an Explore agent for dependency, data-path, or connection questions.

## The tools:

| Tool | When to use | Example |
|------|-------------|---------|
| `comp-trace X` | "How does X connect to the rest of the system?" | `comp-trace AdvisorsTab --direction up` |
| `comp-blast X` | "What breaks if I change X?" | `comp-blast build_employee_leaderboard` |
| `comp-diff` | "What's the system impact of my uncommitted changes?" | `comp-diff` |
| `comp-xref` | "What changed in the dependency graph?" | `comp-xref` |
| `comp-build` | "Rebuild the graph" (auto-caches, rarely needed) | `comp-build` |

## Mandatory before these actions:

- **Before modifying any source file:** `comp-blast <file>` to see downstream impact
- **Before investigating a bug:** `comp-trace <component or artifact>` to see the full data path
- **Before committing:** `comp-diff` to see what your changes affect
- **Before writing a task order:** `comp-blast` to identify affected agents/components

## CRITICAL: Query syntax (get this wrong and you get zero results)

Node IDs in the graph are **stem names**, NOT file paths. The `find_node()` method does
substring matching against graph node IDs like `gold:D_00.portal_aggregates`, NOT filesystem
paths like `data/black_diamond/scripts/gold/D_00.portal_aggregates.py`.

**Rules:**
- Drop the `.py` / `.tsx` / `.mjs` extension. Use `D_00` not `D_00.portal_aggregates.py`.
- Drop directory prefixes. Use `AdvisorsTab` not `portal/src/pages/.../AdvisorsTab.tsx`.
- For function-level queries, use the function name directly: `build_employee_leaderboard`.
- For S3 artifacts, use the artifact name: `employee_leaderboard`.

### comp-trace syntax

`comp-trace <query> [--direction up|down|both] [--all]`

- `--all` traces ALL matching nodes (script + function-level). Use this when a stem like
  `D_00` matches both the script node and its 8 builder functions.
- Without `--all`, multi-match queries ask you to pick.

Examples:
- `comp-trace D_00 --all` — traces script + all function nodes
- `comp-trace AdvisorsTab --direction both` — full chain for one component
- `comp-trace employee_leaderboard --direction up --all` — who produces this artifact

### comp-blast syntax

`comp-blast <query> [--function NAME] [--depth N]`

**IMPORTANT: comp-blast does NOT have --all.** And script-level nodes (like `D_00`, `C_06`)
have NO direct edges in the graph — they return "No downstream consumers." The edges live
on **function-level nodes** and **artifact nodes**.

So for blast, you MUST query at the function or artifact level:

| WRONG (empty results) | RIGHT |
|---|---|
| `comp-blast D_00` | `comp-blast build_employee_leaderboard` |
| `comp-blast C_06` | `comp-blast build_client_mix_timeseries` (function name) |
| `comp-blast D_00 --all` | `comp-blast employee_leaderboard` (artifact name) |
| `comp-blast D_03 --all` | `comp-blast firm_composition` (artifact name) |

To find function names for a script, run `comp-trace D_00 --all` first — it lists all
function nodes. Then blast the specific function you care about.

### General rules

| WRONG (zero results) | RIGHT |
|---|---|
| `comp-trace D_00.portal_aggregates.py` | `comp-trace D_00` or `comp-trace D_00.portal_aggregates` |
| `comp-trace portal/src/pages/.../AdvisorsTab.tsx` | `comp-trace AdvisorsTab` |
| Any query with `.py` / `.tsx` / `.mjs` extension | Drop the extension |
| Any query with directory path prefix | Drop the path, use stem only |

If you get "No nodes matching" — you used the wrong format. Drop the extension, drop the path.
If you get "No downstream consumers" on comp-blast — you queried a script-level node. Use a function or artifact name instead.

## comp-routes (serving layer — URL to S3 key)

`comp-routes` traces how data gets from S3 to the browser through the full serving stack:
CloudFront behaviors -> origins -> auth layers -> router rewrites -> S3 keys -> components.

| Command | What it does | Example |
|---------|-------------|---------|
| `comp-routes trace <COMPONENT>` | Every fetch a component makes, traced end-to-end | `comp-routes trace PartnerAnalytics` |
| `comp-routes trace <ENDPOINT>` | Full chain: URL -> CF -> auth -> router -> S3 key | `comp-routes trace getEmployeeLeaderboard` |
| `comp-routes auth-map` | Which paths have no auth / edge-only / double auth | `comp-routes auth-map` |
| `comp-routes behaviors` | All CloudFront behaviors | `comp-routes behaviors` |

Coverage: 5 origins, 23 behaviors, 16 API GW routes, 71 resolved endpoint routes.

**When to use:** Any question about how portal fetches reach their data. Audit methodology
Step 2 ("Trace the API Layer") should start with `comp-routes trace <component>`.

---

## comp-pipescript (gold script I/O — authoritative)

`comp-pipescript` is a separate tool for **gold layer script dependencies**. Unlike comp-trace
(regex heuristics), it AST-parses `lib/s3_layout.py` and `gold_dispatch.sh` directly.
Coverage: 23 scripts, 87 S3 keys, 113 read edges, 45 write edges.

| Command | What it does | Example |
|---------|-------------|---------|
| `comp-pipescript io <SCRIPT>` | Full I/O manifest. Also shows: COLUMN GAPS (columns accessed but missing from load list — silent failure root cause), S3-DYNAMIC reads (runtime CSV/parquet paths), PORTAL CONSUMERS (platinum keys → endpoints → portal components). Add `--no-portal` to skip routing table. | `comp-pipescript io D_00` |
| `comp-pipescript feeds <SCRIPT>` | Upstream dependencies — what scripts feed this one | `comp-pipescript feeds D_01` |
| `comp-pipescript consumers <SCRIPT>` | Downstream dependents — what scripts consume output | `comp-pipescript consumers C_07` |
| `comp-pipescript overlap <A> <B>` | Shared S3 artifacts between two scripts. **COO: run before writing cross-domain coordination blocks in TOs.** | `comp-pipescript overlap D_00 D_03` |
| `comp-pipescript deployed [SCRIPT]` | Compare local gold scripts against s3://opal-data-bd/code/gold/ ETags. **DS/AE: run before every gold run.** MATCH/STALE/MISSING_ON_S3. | `comp-pipescript deployed D_01` |
| `comp-pipescript postdeps [SCRIPT]` | Show declared post-step and precondition deps from gold_pipeline_deps.yaml. **DS/AE: run before any ad-hoc script run.** | `comp-pipescript postdeps build_canonical_prices_v2.py` |
| `comp-pipescript chain <NAME>` | Chain membership + execution order | `comp-pipescript chain downstream` |
| `comp-pipescript dag` | Full execution DAG with I/O | `comp-pipescript dag` |
| `comp-pipescript inject` | Inject pipeline edges into comp-trace graph cache | `comp-pipescript inject` |
| `comp-pipescript stats` | Graph statistics + warnings | `comp-pipescript stats` |

**When to use which:**
- Cross-layer questions (portal -> API -> Lambda -> S3 -> gold): use `comp-trace` / `comp-blast`
- Gold script I/O questions (what does D_00 read/write? what feeds C_08?): use `comp-pipescript`
- Before a gold run: use `comp-pipescript deployed` (code on S3?) + `comp-pipescript postdeps` (post-steps required?)
- Cross-domain TO decomposition: use `comp-pipescript overlap A B`

All commands support `--json` for machine-readable output.

---

## comp-validate (artifact correctness gate — MANDATORY before S3 upload)

`comp-validate` checks declared invariants against a local gold artifact before upload to S3.
This is the only tool that catches "no crash but wrong output" failures — zeros, missing keys,
incorrect sums — the class that caused 4 critical incidents in ADVI_49PUSH.

```
comp-validate D_04 --artifact /tmp/leaderboard.json   # run all checks, exit 1 on ERROR
comp-validate --list                                   # show all configured scripts/checks
comp-validate D_00 --list                              # show checks for one script
```

Config: `data/black_diamond/scripts/gold/gold_validate_config.yaml`

**DS mandate:** Run `comp-validate <script> --artifact <file>` before signaling AE on any
script that has a validate config. Do not upload or signal until all ERROR checks pass.

Exit codes: 0 = all ERROR checks pass | 1 = any ERROR fails (blocks upload)
WARN severity: advisory, does not block.

---

## comp-iam (IAM permission cross-reference)

`comp-iam` cross-references boto3/AWS CLI operations in Lambda/EC2 source against
Terraform IAM policies. Flags permission gaps before they cause silent failures.

```
comp-iam gaps                       # show all permission gaps (default)
comp-iam service bd-gold-trigger    # ops + grant status for one service
comp-iam role bd-exporter-ec2-role  # all granted actions for one role
comp-iam stats                      # summary counts
```

**DT/AE mandate:** Run `comp-iam gaps` after any iam.tf change. Run `comp-iam service <name>`
after adding any new boto3 call to a Lambda. The 2026-04-09 watchdog loop incident
(s3:DeleteObject missing from bd-exporter-ec2-role) is exactly what this tool detects.

Known v1 limitation: Lambda services need a `role` field in lambda-source-map.json for
per-Lambda gap detection. Gold EC2 scripts are fully covered.

---

All tools are bash commands. Run them via the Bash tool. They are at `.tools/` which is in your PATH.
