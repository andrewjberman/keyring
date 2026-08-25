# CLAUDE.md — Opal Capital Workspace

**First: read `org/XXX.md`** — startup protocol, MCP registration, task orders, session logging.
Rules below are law for every agent, every session. Format: **imperative + mechanism + pointer.**
The *why* and the incident history live at the pointer. Full annotated history: `git log -p CLAUDE.md`.

## Before the rules: how much to check

**Verification scales with the COST OF BEING WRONG. When the next check would not change what you
do, STOP.** The test itself is **Rule 28 (EVIDENCE LAW)** -- four questions and a table saying how
many to ask. Three clauses that are not obvious and were each measured:
- **It governs SUPPLEMENTARY controls, NEVER THE SUBSTANCE OF THE ACT.** Reading the artifact you
  are adjudicating IS the act, not a check on it.
- **SIZE BY THE CLAIM YOUR WORK FEEDS, not only the act in front of you** -- a cheap act can feed an
  expensive claim.
- **RE-DERIVE WITH A DIFFERENT INSTRUMENT, OR CITE THE PEER'S INVOCATION. NEVER RE-RUN THE SAME
  COMMAND.** A same-command re-run tests the peer's honesty, which is not this fabric's failure mode.
  **The rule is per-seat; the waste is fabric-wide** (four seats independently md5'd one unedited
  file in a session, each individually correct).

**Found something odd that is NOT your task? Do NOT halt and investigate.** One line to
`3.0.0_SA_CVO` (cc the issuer) and **keep working** -- CVO files, investigates, and only material
findings graduate to remediation. **Rabbit-holing on an off-scope anomaly is the failure this channel
exists to prevent.** An ARMED hazard (can cause harm while you look away) still disarms same-turn via
a named owner. `docs/doctrine/THE_SURPRISE_CHANNEL.md` -- board: `comp-surprise`.
## NEVER (one miss = an incident)

- **NEVER call a pipeline stale/broken/frozen until you have RESOLVED THE TRADING CALENDAR — count in
  TRADING DAYS, never wall-clock.** Every AUM/holdings/trading pipeline is **`T-1` unless it explicitly
  qualifies otherwise**, so Friday's data IS Monday's correct answer and a Monday "77h stale" reading is
  a healthy pipeline plus a weekend. Mechanism: `lib/trading_calendar.py` is the ONE frontier definition
  (`expected_last_trading_day` / `trading_days_behind`); a `comp-freshness` entry lacking
  `freshness_basis: trading-day-frontier` silently falls back to flat-hours and **will false-alarm every
  Monday — so the instrument's verdict is not a second opinion, it is the same error.** A false outage
  spends credibility and manufactures pressure to "fix" a working pipeline, which is how a guard gets
  removed. Why: `memory/feedback_trading_calendar_before_staleness_tminus1_default.md`.
- **NEVER** reference another firm's bucket from a pipeline tree (bd/cot/inf) — gate-blocked at commit + IAM Deny at runtime.
- **NEVER** move served output without never-widen sign-off (CTO+COO); a verified DELTA=0 deploy needs no hold.
- **NEVER** run bare `terraform apply` (use `safe-apply`), bare `git commit` (use `safe-commit.sh`), or
  `aws lambda update-function-code` (Terraform only). Gate: `.tools/hooks/never-rules-gate.sh` (PreToolUse).
  Audited override: `# never-override: <reason>`. Why: `docs/references/INCIDENTS_2026-07-13.md`.
- **AD-HOC GOLD RUNS ARE PERMITTED FOR QA. PRODUCTION PIPELINES MUST BE SCHEDULED.** An ad-hoc run is a
  legitimate QA instrument — fire one to test or reproduce. But **a pipeline whose only trigger is another
  pipeline's success has no schedule and is a defect**: it freezes silently when its upstream breaks.
  Event-driven is fine as an *accelerator*, never as the only trigger. **An ad-hoc run is never the
  production path and its artifacts are never production evidence.** Design: `docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md`.
- **NEVER BUILD AN ALERT, ALARM, SNS TOPIC, SES SEND, NOTIFICATION, FRESHNESS CHECKER OR MONITOR UNLESS
  ANDREW EXPLICITLY ASKS. Standing moratorium.** *"It is an anti-pattern, and a waste of time for all
  parties."* **WHAT TO DO INSTEAD, and it is the reason this is an anti-pattern rather than merely
  unwanted: a monitor on an unsettled route measures the wrong thing precisely, and must be rebuilt the
  moment the route changes. Canonical routes and schedules FIRST; monitoring only once the thing being
  monitored is settled.** A finding still lands as a gate or an owned blocking item — what is banned is
  reaching for notification machinery as the deliverable. Why: `docs/architecture/MDPF_DEBTCLEAN_PRD.md` §11–§12.
- **NEVER implement a gate on ANY work — no approval step, sign-off, co-sign, hold, or "X must approve
  before Y" — unless Andrew EXPLICITLY asks for that gate.** Not from process symmetry, precedent,
  prudence, a seat's charter, or an exec's routing habit. **The harm: an agent-manufactured approval step
  is INVISIBLE TO ANDREW — work he believes is moving sits held on an approver he does not know exists.**
  Pre-existing MECHANICAL enforcement stands (commit-gate, safe-commit/apply/deploy, owned-paths,
  never-rules-gate); what is banned is creating NEW approval gates. Proposing a gate candidate to
  Andrew/CTO is legal; implementing without his word is not.
- **NEVER convert Andrew's instruction to ONE agent into a gate or stop on ANY OTHER agent — his word
  binds the ADDRESSED seat, verbatim scope, nothing wider.** Relaying is mandatory; ADJUDICATING SCOPE is
  prohibited in BOTH directions — neither narrowing a sovereign word nor widening it. If wider scope seems
  plausible, ASK — never hold on the inference. Record:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260804_1827Z_NO_INFERRED_GATES_NO_SHADOW_PIPELINES.md`.
- **NEVER stand up a shadow / shadow-fork / "build-alongside" pipeline, duplicate output path, or STANDING
  PARITY COMPARATOR — BUILD IT CORRECTLY THE FIRST TIME AND PORT OVER.** (Andrew-direct, COMPLETE VETO:
  *"these things never ever get decommissioned and they become debt and fuck us up forever… The comparator
  is also a HORRIBLE idea because it just muddies the water even further."*) **The mechanism of harm: an
  extra path outlives its test purpose as permanent debt, and a standing comparator adds a SECOND
  instrument to adjudicate instead of clarifying the first.** The sanctioned method: build-time correctness
  (tests, exercised tie-outs, an ad-hoc QA read — run-and-read, nothing standing), then a DIRECT port on the
  production schedule with same-window rollback. Do NOT manufacture a replacement verification gate around
  the port. A consolidation (one canonical builder replacing N) is fine; the veto hits the standing
  second-channel delivery mechanism. Why: `memory/feedback_no_shadow_channels_veto_build_correctly_and_port.md`.
- **NEVER** trust a producer's self-report or rc=0 — verify against the SERVED artifact / live state.
- **NEVER** leave a confirmed deploy half-landed — a begun deploy FINISHES in-session (every prefix, leg,
  activation step) or rolls back + escalates loud to COO. Mechanism: deploy-completion ledger entry in
  `org/critical_paths/change_management/` opened at deploy-start, closed at completion; unclosed at session
  end = COO alarm.
- **NEVER rebase** — not `git rebase`, not `git pull --rebase` — on any shared branch (CLOUD/DEV/PROD/main).
  It rewrites multi-agent history and a non-conflicting result is luck, not correctness. Rejected push =
  `git pull` (merge) then re-push. Gate: `.tools/hooks/never-rules-gate.sh` closes all four cells incl.
  PowerShell and a bare `git pull` under `pull.rebase=true`. Audited override: `# never-override: <reason>`.
  **A silent non-conflicting rebase is indistinguishable from an honest merge — the gate is the only detector.**
  A scratch-branch rebase is your own business.
- **NEVER write device-specific logic into `ajb_workspace` or `portal` — DERIVE, DO NOT HARDCODE.** The repos
  are DEVICE-AGNOSTIC BY DEFAULT; device-specific code must be "very finely scoped and rare."
  **VIOLATIONS:** a hardcoded user path · a baked drive prefix (`/c/` vs `/cygdrive/c/`) · a hardcoded
  workspace root · device-keyed branching outside an identity resolver · behavior that silently no-ops on
  the other machine. **CORRECT PATTERN:** workspace root → `git rev-parse --show-toplevel`; drive prefix →
  `test -d /cygdrive/c && echo /cygdrive/c || echo /c`; `ajb.ps1` → `OPAL_WS_ROOT` + derived-root fallback.
  A claim is a coordination signal, never device ownership. **The narrow legitimate exception, made testable:
  is being device-specific this code's PURPOSE, or an accident of where it was written?** Only the first
  qualifies. ⛔ **DIRECTION RATIFIED — REMEDIATION IS NOT AUTHORIZED BY THIS LINE**: a non-conforming file is
  surface-it, not chase-it. Record: `org/tier0/ledger/LD-0405.md`.

## Deployment Rules

1. **Terraform is the only Lambda deploy mechanism.** No console, no `deploy.sh`, no direct code pushes.
2. **Commit before apply.** code → TF → source map → commit → plan → apply → 0-diff → tag → push `--follow-tags`.
3. **Dependencies go in Lambda Layers.** No `pip install -t .` into source dirs; inline vendoring needs approval.
4. **Update the source map** — every Lambda has an entry in `infra/aws/lambda/ci/lambda-source-map.json`.
   ⚠ **The map PAIRS a Lambda with its repo dir; it does NOT compare deployed bytes to built-from bytes.**
   Code currency is Rule 22a's CODE layer and is the assignee's read, not this map's.
5. **Size Lambda resources deliberately** — never leave `yang-lambda` defaults (256MB/30s) on data-processing Lambdas.
6. **Tag after deploy:** `git tag -a {pipeline}-v{X.Y.Z}` + push `--follow-tags` after every 0-diff apply.
7. **EC2 deploys go through `safe-ec2-deploy.sh`** — never run service-specific deploy scripts directly.
8. **`EC2_MANIFEST.json` is the source of truth** — every EC2 service registered; CI/CD depends on it.
9. **Terraform manages EC2 infrastructure, not code** — code deploys via `safe-ec2-deploy.sh` / SSM.
10. **Never push code directly into EC2 Docker images** — fix locally, deploy through the normal cycle.
11. **Verify parity before EC2 work:** `./infra/aws/ec2/verify-ec2.sh`.
12. **S3 is the artifact store for ALL EC2 code** — never write code on a VM, never inline Python in SSM.
    Local → S3 → EC2 pulls → execute, even for ad-hoc diagnostics. `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`.
13. **DS owns the full commit→QA-deploy cycle** for `data/*/scripts/{gold,silver,bronze}/*.py` incl. `aws s3 cp`;
    DT/AE = infra, PROD triggers, multi-pipeline only. Enforced by `.tools/safe-deploy.sh` (pre-push hook;
    bypass audited). Bucket map = `safe_deploy_core.py` PIPELINE_MAP (bd/inf/cot/mdpf). SHARED repo homes
    (`data/assets/scripts/{gold,silver}`) deploy under the S3-membership guard: key-exists=update enforced,
    404=loud skip, first-mints explicit. **cot is a COMPLETELY separate firm pipeline from bd — never
    mirror/sync** (gate + IAM enforced). Why: `docs/architecture/ADHC_DSFLOW.md`.
14. **Every `.py` edit passes `.tools/commit-gate.sh` before commit** (py_compile + ds-precommit-check
    AST/silver-ids + ruff py39, pin 0.15.11). Universal, all agents, all lanes.
14a. **Commit via `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -F <msgfile> -- <paths>`
    — do NOT pre-`git add`** (the wrapper stages your pathspec inside its lock). **`-F` not `-m`** for any
    non-trivial message (see Git §F-010: a `-m` body is shell-evaluated before git sees it, so a backtick
    or `$(` in it EXECUTES). **`--force` BYPASSES ONLY THE CONTAMINATION / SENSITIVE-FILE CHECKS — IT DOES
    NOT BYPASS A GATE FAILURE OR AN OWNED-PATHS REFUSAL** (`safe-commit.sh:547`). For a lane refusal the
    sanctioned escape is `GIT_COMMIT_AUTHOR_OVERRIDE=<LANE>` — audited, and **SINGULAR: one lane per commit**,
    so a change spanning N lanes is N audited commits, never one `--force`. Why:
    `memory/feedback_commit_only_flag.md`, `docs/architecture/ADHC_OWNPTH.md`.
15. **Every gold/silver/bronze `.py` begins with `from __future__ import annotations`** (PEP-604 on py3.9 runners). Gate-enforced.
16. **Local-runtime bash uses only Git Bash 3.6.7 default-install utilities.** MISSING (guarded `command -v`
    fallback required): `pgrep pkill flock pidof setsid wget`. Canonical pattern: `org/mcp/inbox-watch.sh`.
    **`.tools/jq.exe` IS VENDORED AND TRACKED — resolve it first, `command -v jq` as guarded fallback, then
    FAIL CLOSED AND LOUD.** ⛔ **NEVER `2>/dev/null` a read whose EMPTINESS carries a verdict** — a missing
    binary then returns CLEAN EMPTY and renders a "quiet fabric" out of nothing. Ad-hoc JSON parsing prefers
    python; a shell gate that must parse JSON uses the vendored resolution. EC2-side scripts exempt.
    `docs/architecture/ADHC_BASHFIX.md`.
17. **Silver = dedup + dtype standardization ONLY. NEVER slim fields, NEVER fillna/dropna/business-row-filter,
    NEVER drop bronze columns** — anything needing judgment about field relevance or null meaning is
    gold-tier business logic. Legacy violators migrate to passthrough on next touch.
    `memory/feedback_silver_no_field_slimming.md`.
17a. **BRONZE IS RAW AND UNTOUCHED — whatever the source delivers, byte-for-byte. PARQUET IS A *SILVER*
    FORMAT.** A `.parquet` under `bronze/` is an architectural violation, not a format preference: it coerces
    schema/dtypes AT INGEST, so the raw feed is **not recoverable**. **Each layer has exactly one job; doing a
    later layer's job early is IRREVERSIBLE.** Gate: bucket-policy deny on `.parquet` under `bronze/` segments,
    LIVE on opal-data-assets; other trees remain open (CTO to route). >> **WHEN DEPLOYED CODE AND THE REPO
    DISAGREE, "which is RUNNING?" is the wrong question — "which is RIGHT?" is, and that is ARCHITECTURAL,
    which no measurement answers. "It is deployed and it works" is not an architecture.** <<
    `memory/feedback_bronze_is_raw_untouched_parquet_is_a_silver_conversion.md`.
17b. **THE CANONICAL MEDALLION FORM IS FOUR TIERS ACROSS TWO BUCKETS — AND PLATINUM IS THE SERVING TIER.**
    `bronze` raw vendor · `silver` parquet queryable · `gold` processed analytics — all under
    **`opal-data-assets`**; `platinum` serving — under **`opal-data-portal-v2/platinum/`**. **SERVING IS ITS
    OWN TIER: per-consumer projection, display naming and route-specific reshaping belong in platinum, NEVER
    in gold.** Product-gold home is `opal-data-assets/portal/gold/{product}/{scope}/`; **GOLD IS PARQUET**
    (`{table}/date={D}/`, mirroring silver — JSON leaves the gold tier); vendor trees keep bronze+silver;
    **every platinum publisher READS PARQUET and is the estate's ONLY JSON producer**, so one-producer-per-
    served-key holds by construction. ⛔ **DIRECTION RATIFIED — MIGRATION IS NOT AUTHORIZED BY THIS LINE.**
    The estate does not match it today; a non-conforming tree is NOT a violation and NOT a warrant to move
    anything. Moving a served key is NEVER#3. Records: `org/tier1_exec/1.0.0_SA_CTO/deliverables/`.
18. **`terraform apply` goes through `.tools/safe-apply.sh`** — HALTGT inbox checkpoint at the last reversible
    moment (routine pending msg → `HALT_ACK=1`; override audited via `HALT_OVERRIDE="reason"`). ⚠ **A HALTGT
    PASS IS NOT EVIDENCE YOU WERE NOT HALTED, and `[STOP]` does NOT reliably hard-block** — the checkpoint sees
    only unread files directly under `inbox/<serial>/`, so a live Monitor guarantees a silent empty-inbox
    `exit 0`, and a `~lane` agent is unhaltable regardless. **NOBODY CITES A HALTGT PASS.**
    `docs/architecture/ADHC_HALTGT.md`, `org/tier0/ledger/LD-0267.md`.
19. **Portal main worktree stays on `DEV`, always.** Promotes run in an ephemeral worktree (`/prod-deploy`
    skill, DT lane). Found it on PROD? `cd portal && git checkout DEV` before any portal work.
20. **Check the dependency graph BEFORE you change anything** — (a) ahead of ANY cloud/infra/data change;
    (b) before commit for ANY frontend change. Pick the tool from `org/modules/graph/graph-call-manifest.yaml`.
    **Default to QUERY, never rebuild to answer a traversal.** **Read the provenance header on every call** —
    `UNKNOWN VINTAGE` = freshness unverifiable; a scratch DB (`--db-path`) is a frozen vintage. Verify your OWN
    just-made change against live AWS/served artifacts, never the graph. **`comp-surface-check` IS RETIRED** —
    the MP/benchmark/ADVI surfaces now carry NO automated commit-time guard, stated here so it is not
    discovered later as a gap. `docs/architecture/NFRA_GRAPHS.md`.
21. **comp-which / a comp-tool is the DEFAULT for every search + inspection; a raw search is the EXCEPTION.**
    Raw grep is text-local and connection-blind, so it MISSES coupled things. Reflex =
    `comp-which "<plain-English question>"` — it routes to the rich tool, else runs **`comp-find`** (search
    with each hit's dependency context, a DENOMINATOR line, and a BAND classification).
    ⛔ **`comp-find` IS CASE-SENSITIVE BY DEFAULT AND MATCHES SUBSTRINGS. Its denominator counts FILES
    SCANNED, never PATTERN COVERAGE.** On a ZERO result it guards you (it names `-i` itself). **The unguarded
    cases are the UNDERCOUNT and the OVERCOUNT — a partial case-miss returns a confident non-zero with no
    caveat, and a substring match inflates it (`egress` returned 19 hits, all `regression`).** This estate
    CAPITALISES its load-bearing words, so a case-sensitive census drops precisely the decision-carrying
    lines: measured `[Aa]udience` = 7 vs `-i` = 13, and every one of the six dropped was a ruling.
    **Run `comp-find -i` for any token census; anchor the token or read the hits before quoting a number.**
    Inline `**` emphasis breaks a phrase search at any case — search the shortest distinctive fragment.
    ⚠ `comp-find` counts LINES, not AST nodes. **GATED, not banned:** the LIVE hard-deny is
    raw-`aws`-INSPECTION + `infra/*.tf` grep unless the call carries `# rail-checked: <why>` (audited to
    `org/mcp/comp-which-rail.log`; a repeat override for one intent = a coverage gap → build the tool).
    Estate-scoped broad Bash `grep`/`find`/`rg` DENIES; non-estate broad-grep is a nudge. Native `Grep`/`Glob`
    = nudge-and-proceed; native `Read` + operational `aws` + pipe-greps = free. `/freeform` stands the rail
    down per-session. `docs/architecture/NFRA_COMPRAIL_PRD.md`.
22. **EVIDENCE LAW -- FOUR QUESTIONS, AND WHO EATS THE ERROR DECIDES HOW MANY YOU ASK.**
    (Rule 24 tests a SCHEMA; this tests a CLAIM. Doctrine + the failure catalogue:
    `docs/doctrine/CONTROLS_OVER_CARE.md`.)

    | If being wrong costs... | Ask |
    |---|---|
    | me, this turn -- I just redo it | nothing. Act. |
    | me later, or another seat | **THING + WHOLE** |
    | the record -- a commit, a message sent, a TO, a report | **+ LAYER** |
    | the world -- deploy, delete, grant, served key, a claim to Andrew | **+ NO** |

    **THING** -- the object I read IS the object I am claiming about, *at the vintage claimed*. A
    different bucket / tree / copy / moment does not error: it answers cleanly about something else.
    **WHOLE** -- my evidence spans the set I am claiming about. **Print the denominator.** A page is
    not a total; a part is not the whole; a residual you named is not one you measured.
    **LAYER** -- **DESIRED** (config, plan, source) != **APPLIED** (live state) != **EXERCISED** (it
    ran, and would have failed if the claim were false). **A description is never a state.**
    **NO** -- could this evidence have come out differently if the claim were false? If not, it is
    not evidence. Run the control that fails.

    ⛔ **THE ORDER IS THE MECHANISM. `NO` PASSES INSIDE A WRONG `THING`/`WHOLE`/`LAYER`** -- and then
    every instrument agrees with every other, because all of them are about the same wrong thing.
    **That is why careful agents still fail: they run `NO` hard and never ask the first three.**

    **"proof / provably / root cause / definitively / source-confirmed" are RESERVED WORDS** -- legal
    only on a claim that passed LAYER at EXERCISED. Cite grounding as `file:line @ <commit-ish>`:
    **a line citation without a vintage is not a citation.** A claim failing any postulate is
    `INFERRED` and NON-ACTIONABLE; the cert/dispatch owner withholds the GO.

22a. **INSTRUMENT TRAPS -- non-obvious failures of Rule 28 you cannot re-derive at the call site.**
    **CODE currency**: read the DEPLOYED artifact's bytes and diff against the source it is BUILT
    FROM, resolved through the BUILD INPUT (source-map / manifest), **NEVER by filename** -- a
    filename-resolved check reports drift where there is none AND reads clean where two copies have
    diverged. On EC2, **STAGED code is DESIRED and EXECUTING code is APPLIED** (first-boot-only pulls
    leave the staged object INERT), so applied truth is an on-instance read or the runner's exit-log
    -- **an expected log's ABSENCE is evidence too**. ⛔ A function whose running bytes are older than
    its built-from bytes **passes every rung**: plan 0-diff is true (TF does not manage code
    currency), `get-function-configuration` is true (it is about env), and it runs green on the old code.
    **IAM**: `comp-iam` models `(action)`, never `(action, resource)` -- a role holding `s3:GetObject`
    on ANY bucket reports `[GRANTED]` for every other. It also cannot see returned-buffer calls
    (`batch_writer`) or `generate_presigned_url`'s action-at-REDEMPTION. >> **AN UNDER-REPORTING IAM
    INSTRUMENT DOES NOT CAUSE AccessDenied -- IT CAUSES A FUTURE ENGINEER DOING LEAST-PRIVILEGE
    CLEANUP TO DELETE A NEEDED GRANT AS "UNUSED". SILENCE IS THE DEFECT. NEVER read a comp-iam
    operation list as a deletion warrant.** << Treat it as a FLOOR. For a NEW bucket/table/ARN verify
    live: `aws iam simulate-principal-policy --policy-source-arn <role> --action-names <a>
    --resource-arns <exact key>` -- which has **THREE false-deny modes**: 2+ `--resource-arns` flips
    held ones to `implicitDeny`; a conditioned statement with no `--context-entries` returns
    `implicitDeny` byte-identical to a real deny; and **it does not validate action names, so a TYPO
    is indistinguishable from a missing grant** (use `aws accessanalyzer validate-policy`).
    **ONE `--resource-arns` per call; run the positive control as a SEPARATE invocation** -- mode (1)
    silently disarms it.
    **DELIVERY**: three clocks, routinely conflated -- **SENT** (filename/mtime; `mv` preserves the
    sender's clock forever), **EMITTED** (a watcher claimed it, not that a consumer existed), **READ**
    (agent-side ACK -- the only sound oracle, and the one an orphan cannot forge). An orphaned watcher
    reads REACHABLE *because* the agent is deaf, so the verdict is **ANTI-CORRELATED** and passes the
    random-input control. **Producer-side signals are blind to consumer death; only a round trip
    crosses both.** A sovereign `[STOP]` needs an ACK-or-escalate loop.
    **RETRIEVAL**: a failed retrieval returns a VALUE -- `grep -c` counts zero in an error message.
    ⛔ `--query 'length(...)'` on a paginated `list-*` returns the PAGE count, and **`--no-paginate`
    is the hazard, not the remedy**: omit it, let the CLI paginate, count the materialised set.
    ⛔ `aws s3 ls` renders LOCAL time unmarked while `s3api` renders UTC; and `git log
    --date=format:'...Z'` **renders local and stamps a literal `Z`** -- use `%aI`/`--date=iso-strict`
    and **never type a `Z` into a format string.** A missing marker makes a reader ask; a false one
    makes them stop asking.

23. **Every SES send uses `Source`/`EMAIL_FROM` on the `opalinvest.dev` domain** — DKIM-signed + DMARC-aligned.
    `opalinvest.com` is address-verified only (DKIM NOT_STARTED, SPF excludes SES) — unauthenticated, so EOP
    quarantines it **nondeterministically**. ✋ **`opalcapital.com` — WE DO NOT OWN THIS DOMAIN.** Never send
    from it, never request a cert for it, never name it to a vendor as ours, never build on it. **IT IS NOT A
    VERIFICATION TODO — IT IS SOMEONE ELSE'S PROPERTY.** Gate: an OWNED-DOMAIN ALLOWLIST denying any new SES
    domain identity / ACM cert / DNS-bearing resource whose apex is not on it. >> **THE ESTATE HAS INSTRUMENTS
    FOR WHAT IS *DEPLOYED* AND ZERO FOR WHAT IS *OURS*. Grounding tells you what IS; it cannot tell you what is
    YOURS — a premise no instrument is pointed at is not a weak claim, it is an INVISIBLE one.** <<
    `memory/feedback_ses_sender_opalinvest_dev_standard.md`.
24. **TAXONOMY LAW — FOUR POSTULATES, prerequisites for ANY classification schema an agent authors:**
    **(i) MECE** — values mutually exclusive, collectively exhaustive, evaluated against the DECLARED LAYER the
    schema covers (name the layer, then hunt the uncovered member); **(ii) SAME GRAIN** — every value provably
    at one grain (never a file-level value beside a cohort-level value); **(iii) INTENT COHERENCE** — one axis
    serves ONE intent (mixing content-kind with handling-policy, or state with disposition, foundationally
    breaks the schema); **(iv) STATE COHERENCE — a stability frame:** name the state axis, then ask whether ONE
    remedy moves every value together. **If building the obvious instrument delivers some values and
    structurally cannot deliver others, YOU MUST NAME WHICH VALUES DO NOT MOVE.**
    **This binds EVERY SCHEMA-ENUMERATION ACT** — minting an axis, proposing or adding values to an existing
    axis, and **ADOPTING a schema authored elsewhere (adoption is an authoring act).** **OUTCOME ARRAYS,
    TYPED-RESULT SETS AND PREDICATES ARE SCHEMAS — they escape this gate precisely because they do not read as
    schemas.** A value-enum proposal arrives WITH its four-postulate record and a token-hygiene census
    (word-boundary occupancy over the canon files), or it is not a proposal. Remedy pattern for a violating
    axis: the two-field split (RCG charters v2). Working record: `rcg/rulings/RULINGS.jsonl` R-0006/R-0009.
25. **STALE >= 90 DAYS = DORMANT — not in use — unless it carries a DECLARED exception.** The default that
    TERMINATES the stale-but-reachable hold. 90d is structurally clear of the trading-calendar/T-1 class; only
    QUARTERLY cadence lands near the bar and must declare. **An exception DECLARES ITS KIND, because the two
    kinds take OPPOSITE remedies (Rule 24(iv)): LONG-TTL-LIVE** (e.g. capital market assumptions, 1yr — age
    measures against the declared TTL) **vs CLOSED-PERIOD-IMMUTABLE** (period-close snapshots, frozen forever
    and correctly — a refresh would be the DEFECT). ⛔ **DORMANT IS NOT A DELETION WARRANT** — it licenses
    stop-treating-as-live, never `rm`; moving served output stays NEVER#3. ⛔ **CHECK FOR A SUCCESSOR BEFORE
    CONCLUDING: dormant-because-ABANDONED and dormant-because-KEY-MIGRATED are byte-identical from age alone
    and take OPPOSITE actions.** Same-leaf-name live/dormant twins fail toward deleting the LIVE one.
    `memory/feedback_90_day_dormancy_default_with_declared_exceptions.md`.
26. **THE APPLY RUNS ON THE DEVICE THAT OWNS THE WORK. NEVER FERRY AN APPLY ACROSS FABRICS.** A seat that BUILT
    a change APPLIES it, on its own box, under the normal wrappers. **Why: the builder holds the context the
    applier needs, and a ferry is exactly the step that separates them** — a ferried apply had four disagreeing
    on-box sources and had to be re-framed mid-flight. Mechanism, present on both devices: `.tools/safe-apply.sh`
    · `infra/aws/ec2/safe-ec2-deploy.sh` (**NOT `.tools/`**) · `.tools/safe-deploy.sh` · `infra/aws/ec2/verify-ec2.sh`
    · deploy-completion ledger at `org/critical_paths/change_management/`. ⚠ **Terraform is NOT at one path on
    every device — resolve the binary, do not assume the baked path.** Every existing gate binds unchanged, and
    **owning the apply means owning NEVER#6's completion obligation, not escaping it.**
27. **EVERY new directive/project runs the DIRECTIVE EXECUTION PIPELINE: register → purpose-level PRD → COO
    atom-decomp of the operative surfaces BEFORE any TO exists (proof-of-spec derives from decomp cells,
    aligned BOTH directions with printed denominators) → EXECUTE ON SPEC → CVO's surprise channel.**
    **Mid-round the spec is FROZEN — an executing seat's only legal off-spec ACT is to SURFACE a surprise item**
    (one line by MCP to `3.0.0_SA_CVO`, cc the issuer); **CVO files it under `org/surprise_channel/**` — executing
    seats do not write that tree.** Surprise taxonomy is TWO ORTHOGONAL AXES: **class {OBSERVATION, BLOCKING} ×
    standing {ARMED, INERT}**. OBSERVATION never interrupts (one line, keep working); BLOCKING routes same-turn
    to the ISSUER for spec amendment; **any ARMED item disarms SAME-TURN via a NAMED disarm owner**, and
    **DISARMED ≠ REMEDIATED** (two states, two owners, two clocks). **SEATING: a Tier-2 seat instance is
    dispatched ONE PROJECT** — N concurrent projects = N `~lane` instances, one project each; the resource
    protected is the seat's CONTEXT. Protocol: `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md`.

## Agent Autonomy

**Do NOT ask permission** to read, write, build, test, commit, push to CLOUD/DEV, run scripts, or call
**Opal-owned** APIs (AWS, our own services) — pre-authorized; move fast, just execute. **This
pre-authorization EXCLUDES every egress off Opal-owned infrastructure.** **Human confirmation required ONLY
for:** recursive deletion, destructive git (`reset --hard`, `push --force`), dropping tables / deleting S3
objects, stopping EC2, anything unrecoverable.

- **NEVER call an external vendor API** (`ycharts_*`, or any non-Opal service) **without Andrew's explicit
  per-use word** — availability in the toolset is NOT authorization, and neither is a privacy sign-off nor a
  co-verified arg schema. An args allowlist is a privacy control on the audit LOG, never an egress control on
  the WIRE. Gate: `m365-mcp-gateway` tier check + audit lake (`s3://opal-mcp-audit`).
  `memory/feedback_availability_is_not_authorization_vendor_egress.md`.

**NEVER self-wind-down, NEVER default to "tonight."** Keep DRIVING every addressable task to completion NOW —
a session winds down ONLY when Andrew explicitly says so. Deferring to a scheduled-nightly is legal ONLY when
there is literally no other option (a hard external gate, stated plainly) — NEVER a default. "We'll monitor it
tonight" / passive idling = a coast-failure. `memory/feedback_no_passive_monitor_tonight_drive_now.md`.

## Compiler Tools (comp-*) — situation → command

All in `.tools/` (PATH). Catalog: `org/modules/graph/graph-call-manifest.yaml`; reference: `org/modules/graph/comp-tools.yaml`.

**Don't know which tool? `comp-which "<your question>"`** maps a natural-language question to the canonical
call. The tool count is GATE-MAINTAINED (`comp-manifest-check`), not prose-maintained — **do not freeze a digit
here.** A PreToolUse HUD hook nudges in-line when a `Grep`/`Glob`, a raw `aws` INSPECTION, an `infra/.tf` grep,
or a `useQuery`/`queryKey` search would answer a question a comp tool answers with higher context. Operational
aws (invoke/deploy/cp/verify/TF, DDB data-plane) + generic `s3 ls` are NOT nudged.

| Situation | Command | Note |
|---|---|---|
| Don't know which comp tool? | `comp-which "<question>"` | routes to the rich tool, else runs the on-rails primitive; never dead-ends |
| Need to grep/find the repo | `comp-find <pat> [path]` / `--name <glob>` | .gitignore+submodule-aware, logged, dependency context + DENOMINATOR + BAND. Use `-i` for any census |
| "What's in the news/advi/market pipeline?" | `comp-estate <name>` | FIRST CONTACT: named-thread traversal + ontology views (`--segments`/`--matrix`/`--layers`/`--definitions`). ⚠ Its `served:` field MIXES live-derived detail with snapshot prose and carries NO marker — **treat every topology or served-name claim as a PRIOR UNDER TEST and ground it on the live primitive.** Snapshot stale past 14d; `--refresh` before trusting a thread NAME |
| Editing a gold script | `comp-pipescript io [script] --pipeline <tree>` | COLUMN GAPS + portal consumers. `--pipeline` REQUIRED (flagless = rc=2, no guess) |
| Running a gold script | `comp-pipescript deployed [script]` | MATCH/STALE/MISSING; no-arg = all-trees firm-separated sweep |
| Ad-hoc (non-dispatch) run | `comp-pipescript postdeps [script] --firm <bd\|inf\|cot\|mdpf>` | required post-steps. **Flagless silently defaults to bd — name the firm** |
| Cross-layer graph question | `comp-kuzu "MATCH ..."` | canonical auto-refreshing DB; read the header |
| Gold run done, signaling AE | `comp-validate [script] --artifact <file>` | PASS/WAIVED = safe; `NO_CONFIG`/`ZERO_CHECKS` = UNVALIDATED, never signal SAFE |
| What breaks if I change X? | `comp-blast [fn/artifact]` | function name, not script name |
| Modifying a portal component | `comp-transform schema-check [Comp]` | MISSING = runtime undefined |
| 4xx / HTML-response debugging | `comp-routes behaviors` | CF error rules mask JSON errors |
| New boto3 call / iam.tf change | `comp-iam service [lambda]` / `comp-iam gaps` | **NECESSARY, NOT SUFFICIENT** — see Rule 22a |

⚠ **A firm-partitioned absence verdict MUST NAME THE TREE IT SEARCHED.** A 404 in the wrong bucket does not
error — it returns a clean, confident, well-formed ZERO. A cross-tree nonexistence claim requires enumerating
every tree or it is not a claim.

## Code Quality

**THE BUILD LADDER — every line of new code is a LAST resort. Run this gate IN ORDER before writing any.**
**(1) YAGNI** — does this need to exist at all? Unneeded code becomes debt the moment it lands and is never
decommissioned. **(2) The estate already has it — CODE *AND* INFRASTRUCTURE.** Code: `comp-which "<what you're
about to write>"` FIRST. Infrastructure: `comp-estate --layers` to locate the layer, then drill to the
recreatable pattern — an existing Lambda/trigger/bucket-grammar you didn't find is a duplicate you're about to
stand up. Terms/schemas: `comp-estate --definitions` prints the RATIFIED term registry; a vocabulary you
re-coin beside an existing ratified term is the same duplicate one layer up. **(3) The stdlib does it.**
**(4) A native platform feature covers it** (AWS/git/OS primitive). **(5) An already-installed dependency
solves it** (check the Lambda layer / lockfile before adding anything). **(6) It can be one line** — make it
one line. **(7) Only then: the MINIMUM code that works.** The failure this closes: an agent's instinct is to
BUILD, because a fresh build is the cheapest-feeling deliverable — the same mechanism as the alarm anti-pattern.

**No emojis (no non-ASCII) in production code, logs, or anything that runs on AWS** — breaks
CloudWatch/charmap, grep, CI stdout. Use `OK:`, `WARN:`, `ERROR:`, `SKIP:`, `BLOCKED:`.

## Detailed Documentation

- **Lambda / EC2 deploy protocols:** `docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md`,
  `docs/deployment/EC2_DEPLOYMENT_PROTOCOL.md`, `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`,
  `docs/deployment/TERRAFORM_PROTOCOL.md` (the one-document TF mechanism; law stays in this file),
  `docs/deployment/EC2_TELEMETRY_RIGHTSIZING_STANDARD.md`
- **Graph platform:** `docs/architecture/NFRA_GLOBGRPH_PRD.md`
- **Critical-surfaces watch + ledger:** `docs/architecture/NFRA_GRAPHS.md` §10 · `org/critical_paths/README.md`
- **Estate scanning:** `docs/briefs/nfra-debtscan-prd-request-20260612.md` · ledgers `org/modules/graph/debtscan/`
- **Agent Start Guide:** `org/XXX.md`
- **BLOOMBERG — ANY scenario** (terminal sign-in, `blpapi` session, empty fields / entitlement refusals, the
  daily `/terminal-upload` pull): **READ `integrations/bloomberg/READ_HERE.md` FIRST.** Three things not to
  re-derive: **sign-in is TWO-PHASE and BUDGETED** (fill is free and repeatable; submit spends one of two);
  **a refusal names the SURFACE, never the absence** — a clean zero on ONE surface says nothing about the
  surface next door; **the derived layer (count/sector/geo/top-ten) is CURRENT-DAY-ONLY**, so an uncaptured
  day is permanent. ⛔ Do NOT mint `data/bloomberg/` — `integrations/bloomberg/` is the ruled folder.

## Git

- Working branch: `CLOUD`. Portal submodule: `DEV`/`PROD`. Terraform binary: resolve it (`.tools/terraform.exe`
  on the laptop; on PATH at site Z — see Rule 26).
- `MSYS_NO_PATHCONV=1` ONLY for Terraform imports / ARN-path args, and for **`git show <ref>:<path>` whenever
  the REF contains a `/`** (`origin/CLOUD:.owned-paths.yaml` mangles; `HEAD:<anything>` passes). **Blanket the
  slashed-ref case; don't memorize the boundary.** **NEVER `2>/dev/null` a `git show <ref>:<path>`**: the mangle
  prints `fatal:` on stderr and returns CLEAN EMPTY stdout, rendering "file absent" out of a broken retrieval —
  run a positive control beside any ABSENT verdict. **NEVER for `git push`** (breaks the VALGATE hook)**, the aws
  launcher, or `safe-apply`.**
- **The `.tools` shims reach agent shells via `~/bin` FORWARDERS, NOT via profile PATH lines** — harness shells
  are non-interactive/non-login and source NO profile, so any PATH line in `~/.bashrc` never executes.
  START-OF-SESSION CHECK: `command -v comp-which` — on WARN run `bash .tools/provision-path-shims.sh` (idempotent)
  or use explicit `.tools/` prefixes. **AWS from Git Bash goes through the `.tools/aws` PATH shim** — it passes
  AWS namespace args literal and converts only real local paths; never bare `MSYS_NO_PATHCONV=1 aws`. Inspect
  with `AWS_SHIM_DEBUG=1`. **`.tools/aws.cmd` MUST be provisioned alongside it — BOTH FILES OR NEITHER:** a
  `powershell.exe` spawned FROM bash inherits bash's PATH and would resolve the extensionless shim as an
  Application and **HANG silently**, so a hung `aws s3 cp` REPORTS SUCCESS while S3 keeps the old artifact.
- **Python/PowerShell shelling to bash → import `.tools/git_bash_resolver.py` `git_bash()`; NEVER bare
  `bash`/`/bin/bash`** — a python-spawned bash Windows-resolves to the System32 WSL stub and fails LOUD or,
  worse, **SILENTLY reports success**. `shutil.which("bash")` does not reveal it. Use the ONE resolver.
- **Native Python spawning ANY MSYS binary** (`grep sed awk find sort tar curl timeout`) **→
  `.tools/msys_argv_guard.py` `msys_safe_run()`; NEVER a bare unix-tool name in a subprocess argv.** Two
  independent mechanisms, both load-bearing: **`shlex.quote`** closes glob de-escaping (an unquoted argv element
  carrying `\` + `* ? [ ( {` is silently de-escaped into a still-valid regex → rc=1/empty/no-stderr, *the wrong
  question asked correctly*) and bare-glob CWD expansion; **bash's MSYS PATH rewrite** closes CreateProcess
  searching System32 before PATH (`['find',…]` spawns the Windows tool while `shutil.which` reports GNU).
  Always-route is deliberate — callers must not pre-classify. **Oracle when suspecting argv corruption: echo the
  argument back; the downstream tool's verdict cannot distinguish intact from corrupted-but-matched-by-luck.**
- **Put the control on the RETRIEVAL, not the pattern. THE CLASS: an upstream stage silently redefines the
  domain the downstream stage measures over, the result is WELL-FORMED IN THE NEW DOMAIN, and the output DOES
  NOT CARRY ITS OWN FRAME** — nothing in `0`, `100`, or `218:` says what it is 0 OF. **Care cannot catch it;
  only printing the denominator beside the number can.**
  ⛔ **AWS: `--query 'length(...)'` on ANY paginated `list-*` returns the PAGE count** (measured: `list-rules`
  reported 100 when the truth was 142). ⛔ **`--no-paginate` IS THE HAZARD, NOT THE REMEDY — it returns page 1
  as a clean, complete-looking result.** **OMIT the flag, let the CLI auto-paginate, then count/filter the
  MATERIALISED set client-side.** An ABSENCE verdict from any `list-*` carries its denominator printed beside it.
  ⛔ **`aws s3 ls` renders LOCAL time with no marker while boto3/`s3api` render UTC** — pin the plane for any
  cross-source compare. ⛔ **And the remedy that invites — "so mark it UTC" — is itself a defect when
  hand-appended: `git log --date=format:'…Z'` RENDERS LOCAL AND STAMPS A LITERAL `Z`, off by the full offset
  while positively asserting UTC. A missing marker makes a reader ask; a FALSE marker makes them stop asking.**
  Use `%aI`/`%cI` or `--date=iso-strict`; **never type a `Z` into a format string.** The whole `--date=` family
  is suspect — `--date=short` also renders local, so a DATE-ONLY claim can silently cross midnight.
  ⛔ **TWO HALVES, DIFFERENT REMEDIES. ACCIDENTAL** — per-invocation; fixed by *how you call it*.
  **DESIGNED — permanent, because the instrument's domain is not the question you asked, and NO WAY OF CALLING
  IT DIFFERENTLY FIXES THAT. Its remedy is the opposite: KNOW THE INSTRUMENT'S DOMAIN AND CORROBORATE OUTSIDE
  IT.** ⛔ **THE PLANE FORM: a SERVED-layer absence is not a PRODUCT-layer absence; a CF-log census sees edge
  readers only. NO CONTROL INSIDE THE WRONG PLANE CAN CATCH A WRONG-PLANE ERROR** — positive control, printed
  denominator and 0 read failures all agree with each other because every one is about the same wrong plane.
  **Name the QUESTION'S plane before choosing the sweep's. AND AUTHORSHIP IS NOT EVIDENCE — when the claim is
  about another plane's state, the evidence comes FROM that plane EVEN WHEN YOU AUTHORED THE ARTIFACT.** *(A
  non-shell instance: an import guarded by `try/except` answers COMPLETION, never PRESENCE, so an
  "import-health check" passes with the package absent.)* The designed half is what Rules 22a/22b already
  police, unnamed — an instrument whose clean answer is STRONGEST exactly when the failure is TOTAL.
- **A commit message is an EXECUTION VECTOR — author EVERY non-trivial message via `git commit -F <file>`;
  `-m` is DEPRECATED for any body with special characters.** A double-quoted `-m "…"` is shell-evaluated
  *before* git or `safe-commit` sees it, so a backtick or `$(` in the body RUNS with your permissions and
  splices its stdout into the immutable record — **a lint cannot catch it (the substitution already
  happened)**. `-F` routes the body into a file the shell never parses. Only LOUD injections leave a scar;
  silent ones are holes, so **historical incidence is UNKNOWABLE — never quote a count as a total.**
  `org/tier0/ledger/LD-0276.md`.
- **NEVER compose a message reporting a COMPLETED ACT — a commit hash, a sweep count, a landed/pushed status —
  in the SAME tool call as the command that produces it. READ THE NUMBER, THEN WRITE THE SENTENCE.** The defect
  is an **ANNOUNCEMENT THAT OUTRAN ITS OWN ACT**: composed against the act's *intent*, shipped as a *report*,
  and **indistinguishable at the reader from one composed against real output** — so it passes every downstream
  check that trusts the report. ⛔ **SCOPE: this binds REPORTS OF COMPLETED ACTS, and does NOT bind a
  `safe-commit -F` message file**, which is authored before the act by necessity and executes ATOMICALLY with
  it. No mechanical detector exists, so this is an imperative, not a gate; compliance costs one round trip.
  **Sibling shape: an ENVELOPE that outran its CONTENT** — a `send_message` passing the wrong parameter name
  defaults the body to `""` and still returns a normal DELIVERED receipt. **An empty body and a substantive one
  are byte-identical at the recipient** — verify a substantive send by `wc -c` on the delivered file.
- **NEVER WRITE "YOU" OR "YOUR" ABOUT A SPECIFIC SEAT IN A MULTI-RECIPIENT MESSAGE — NAME THE SERIAL,
  AND CITE THE MSG-ID.** `to_agents` delivers ONE body to N inboxes, each header-stamped `To: <that
  recipient>`, so **a second person resolves PER READER**: "you were right" reads as addressed to
  every recipient, and "your 70784" makes each one look for a message they never sent. The correct
  form is `3.0.0_SA_CVO's 70924 found X`. **Cheap, and it fails in the direction nobody contests** —
  a seat handed credit for a peer's work has no reason to push back, so the false attribution is the
  one that survives. Costs: a serial instead of a pronoun. Does not apply to a single-recipient
  `to_agent` send, where "you" is unambiguous. Measured twice in one hour: a senior seat issued a
  wrong correction off one pronoun, and a peer had to refuse credit for a finding that was not theirs.
- **A REPORT OF A COMMIT STATES ITS PUSH STATE** — "landed LOCAL @hash, rides integration", or "on
  origin/<branch> @hash (ls-remote read)", never bare "landed". Under the integrator-only push gate a commit is
  invisible to every freshly-pulling or newly-spawned seat until pushed.

## Portal

- `portal/` — `bun install && bun run dev --port 5175`. Bun: resolve via the user profile, do not bake a path.

## Changing this file

**A rule = imperative (≤2 lines) + mechanism + pointer.** New rules ideally ship WITH a gate — **gates teach at
violation time; prose taxes every session, forever, in every agent's context.**

⛔ **A NEW VERIFICATION RULE MUST STATE WHAT IT COSTS AND WHEN IT DOES NOT APPLY. A rule with no
non-application clause is incomplete and does not land.** Every incident that reaches this file comes from
UNDER-verification, because over-verification costs time rather than correctness and nobody files a postmortem
for "we were slow" — so without this clause the file can only ratchet one way. **Context spent on a low-stakes
check is context unavailable for the high-stakes judgment later in the same session: that is a CORRECTNESS
cost, not a speed one.**

⛔ **A LAW EDIT HAS THREE DELIVERY SURFACES AND THE COMMIT IS ONLY ONE.** This file loads at session start and
is **never re-read mid-session**, so every seat that spawned before your edit carries the superseded text —
**and the asymmetry is invisible from inside a running seat.** So: **(1)** commit; **(2)** MCP-broadcast to
every live seat, same turn; **(3)** state the PUSH STATE in that broadcast — "landed LOCAL, rides integration",
never bare "landed" — and carry any law line a pending spawn depends on IN THAT SEAT'S SPAWN BRIEF until the
push is confirmed. The commit fixes the RECORD; only the broadcast fixes the FABRIC.

**WHERE THINGS GO — this file is LAW, not a notebook:**

| You have… | It goes in… |
|---|---|
| An **imperative** every agent must obey, + the **mechanism** they cannot obey it without | **CLAUDE.md** (here) |
| A **principle** that binds future behaviour | **`docs/doctrine/`** |
| **What happened** — an incident, measured numbers, who caught what | **`docs/references/`** |
| Startup / session mechanics | `org/XXX.md` |
| A decision and its rationale | `org/tier0/ledger/LD-NNNN.md` |

**Never cut a MECHANISM to save space** — a bare prohibition loses to the agent's own instruments. **But the
incident that taught it is not the rule.**

**INCIDENTS DO NOT LIVE IN GOVERNANCE DOCS.** An incident report is valid in an explicit incident/postmortem
doc when it is CONCRETE and a NOVEL basis. *"The main doctrine/controls/etc governance-style docs should not be
flooded with incident reports, at best they just reference an ID that goes to that incidence report/postmortem
doc."* **The editing test: a principle earns its place by being ACTIONABLE WITHOUT ITS INCIDENT.** If you cannot
state the mechanism without retelling what happened, the mechanism is not yet extracted — write the incident
record, extract the property, cite the record. **This binds CLAUDE.md, `docs/doctrine/`, `MEMORY.md` and every
governance surface.**