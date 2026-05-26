# LD-0077 WB-1 Design-Readout -- Additive Disposition Matrix (LD-0067 CASE_FIND + LD-0070 TELEMETRY)
**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE, TRACE
**Date:** 2026-05-26
**Serial:** 0.7.0_AE_CloudOps
**Spawn:** continuing post-startup session 2026-05-26T~02:14Z
**Tier-0 commit hash at authoring:** `07059979a` (CVO LD-0077 independent review verdict -- newest ratification-chain commit at design-readout authoring window)

---

## §1 -- Frame

Per LD-0077 batched ratification (MSTR `cf0b2cdc5` 2026-05-26T01:55Z) + ws CVO independent security review verdict (`07059979a` CORROBORATE-with-additives on both specs) + ws CTO consolidation MCP (`[WB-1 CONSOLIDATED ADDITIVES]` 2026-05-26T~02:00Z), AE 0.7 is parallel-authorized to start WB-1 on both LD-0067 (CASE_FIND) + LD-0070 (TELEMETRY) Workstream B implementations.

20 total additives across both specs:
- **CASE_FIND:** 4 MSTR FN-additives (FN-1..4) + 6 CVO CV-additives (CV-A1..A6) = 10 rows
- **TELEMETRY:** 5 MSTR FN-additives (FN-1..5) + 5 CVO CV-additives (CV-B1..B5) = 10 rows

CTO ask (verbatim): "WB-1 design-readout (when complete) -- please surface ACK + planned phase-placement for each additive (you can table-form by additive ID -> WB-phase mapping). If any additive requires spec-amendment cycle, flag at design-readout NOT at WB-3 commit -- earlier the better."

This document is the deliverable.

---

## §2 -- Disposition taxonomy

Each additive resolves to ONE of four disposition classes:

| Class | Meaning | Where it lands |
|---|---|---|
| **spec-amendment-flag** | Invariant or hard constraint that belongs in canonical spec text (not just WS-B impl spec). Reason: structural-drift risk -- future readers/maintainers/reviewers landing on impl spec rather than canonical spec is the failure mode spec text prevents. | CTO scribes v0.3 (CASE_FIND) or v0.4 (TELEMETRY) spec amendment + LD-0078 RATIFY-REQUEST to MSTR. |
| **WB-design-constraint** | Implementation constraint folded into WS-B impl spec (`CASE_FIND_QUARANTINE_IMPL.md` or `TELEMETRY_LIVENESS_IMPL.md`) at the named WB phase. | AE 0.7 authors impl-spec language at named WB phase. |
| **WB-acceptance-criterion** | Observable test/measurement that gates a WB-phase RAVC2 acceptance. | AE 0.7 adds to acceptance-criteria section of named WB phase impl spec. |
| **observation-tunable** | Parameter or threshold that may need tuning during Phase-1 observation; not blocking at impl-time. | AE 0.7 documents as `[OBS-TUNABLE]` note in impl spec; revisit at named observation phase. |

Multiple dispositions OK for a single additive (e.g., a spec-amendment that ALSO has an observation-tunable component).

---

## §3 -- Table 1: CASE_FIND additive disposition (10 rows)

| ID | Summary | Proposed WB-phase | Rationale | Disposition |
|---|---|---|---|---|
| **FN-1** | Dedicated EC2 runner > Lambda-container; t3.medium or equivalent | WB-2 (runner provisioning) | §8 already specifies "Dedicated EC2 runner provisioned (t3.medium; Docker daemon; IAM scope = ECR pull + CloudWatch logs only)." FN-1 corroborates this design intent. Pairs structurally with CV-A5. | WB-design-constraint (already in WB-2 spec; impl spec re-anchors) |
| **FN-2** | Add `huggingface.co` to download allowlist when Cases substrate pulls ML model corpora | future (not current WB) | Spec §9 Q5 names the initial allowlist (github.com, gitlab.com, pypi.org, npmjs.com, registry-1.docker.io). Adding huggingface.co is contingent on substrate evolution -- not blocking current WB. Document as future allowlist-expansion item with ws CVO sign-off gate. | observation-tunable (future spec-extension when triggered) |
| **FN-3** | `--stop-timeout=30` may be tight for large-repo AST walks; bump to 60s if WB-6 smoke shows premature SIGKILL | WB-6 (smoke acceptance criterion) | Empirical observation gate: if WB-6 smoke test (per spec §8) on a sufficiently-large candidate triggers premature SIGKILL during analysis phase, document as Phase-1-observe tunable in impl spec + raise impl-spec recommendation to bump default to 60s. Doesn't require spec amendment; impl spec carries the tunable. | WB-acceptance-criterion + observation-tunable |
| **FN-4** | Cite specific cron file path for log rotation (likely `infra/aws/ec2/case-find-quarantine/log-rotation.cron`) | WB-4 (audit-log rotation) | Spec §6.4 references "the standard log-rotation cron" without citation -- pure documentation gap. Cleanest fix: minor spec-amendment to §6.4 with explicit path citation, rolled into the v0.3 amendment cycle CTO is scribing for CV-A5. ~1 line spec text. | spec-amendment-flag (minor; bundle with v0.3) |
| **CV-A1** | Stage 3a network-layer egress firewall (iptables/nftables OR proxy) beyond app-layer `safe-download.sh` allowlist | WB-2 (runner provisioning) | Defense-in-depth: a `safe-download.sh` parsing bug must not result in arbitrary outbound traffic. iptables/nftables baked into runner host user-data, OR dedicated Docker network with allowlist-enforcing proxy. Concrete impl: iptables rules denying all OUTPUT except destination = allowlist IPs (resolved at runner-start + refreshed daily). CVO marked ERROR-class (not BLOCK); shippable v0.2 without it but WB-design-time is right moment. | WB-design-constraint (WB-2 runner user-data + IAM) |
| **CV-A2** | `IMAGE_DIGESTS.json` is ONLY authoritative digest source; runner MUST refuse to launch if digest unresolvable; floating-tag fallback BANNED | WB-1 (digest ledger) + WB-2 (runner code) | §2.1 already specifies digest-pinning ("must be pinned to a digest @sha256:..., not a floating tag"). CV-A2 is the enforcement mechanism: runner code reads only from `infra/aws/ec2/case-find-quarantine/IMAGE_DIGESTS.json`, no env-var override, no inline-script digest, no `docker pull image:latest` fallback. Fail-closed launch sequence: if `jq .image_digests.\"opal-case-find-analysis\"` returns null → exit 1 + audit-log alarm + ws CVO MCP. WB-design-constraint sufficient (impl spec carries; spec text already covers the underlying invariant). | WB-design-constraint (WB-1 + WB-2) |
| **CV-A3** | Deny-list cache scope (per-runner local), TTL (7 days), unpoisoning path (ws CVO sign-off audit row + `case-find-unblock` CLI) | WB-3 (safe-download.sh + entrypoint scripts) | §4 BLOCK indicators mention deny-list cache without specifying scope/TTL/unpoisoning. CV-A3 fills the gap. Concrete impl: deny-list = sqlite file at `/var/lib/case-find/deny-list.db` inside runner host (NOT inside container — survives container destruction); TTL 7d enforced by daily cron sweep; `case-find-unblock <URL>` CLI tool emits explicit AUDIT_UNBLOCK row with author + reason + reference to original BLOCK event. Avoids cross-runner sync complexity (deferred per CVO recommendation). WB-design-constraint suffices; deny-list mechanism is impl-spec-level detail. | WB-design-constraint (WB-3) |
| **CV-A4** | Audit-log write failure = fail-closed (refuse new Phase 3 containers; raise alarm via CloudWatch + ws CVO MCP) | WB-4 (audit-log rotation + write-failure mechanism) | §6.4 Phase-6 cleanup `audit_log.write({...})` has no failure handling currently. Concrete impl: wrap audit-log writes in try/except; failure → set runner-state to UNHEALTHY (refuse new Phase 3 launches) + emit CloudWatch metric `CaseFind/AuditLogWriteFailure` (alarm threshold = 1 in 5min) + MCP `[STOP]` to ws CVO. Cron-based health check independently verifies log file exists + writeable + recent activity. WB-design-constraint suffices; impl-spec carries; underlying append-only invariant already in spec §6.4. | WB-design-constraint + WB-acceptance-criterion (WB-4) |
| **CV-A5** | **IAM hard constraint:** runner instance permissions = `ecr:GetAuthorizationToken` + `ecr:BatchGetImage` + `ecr:GetDownloadUrlForLayer` + `logs:CreateLogStream` + `logs:PutLogEvents` ONLY. BANNED: any S3 (beyond ECR-implicit), any SSM, any IAM AssumeRole, any SecretsManager, any cross-account. | WB-2 (IAM provisioning) | **SPEC-AMENDMENT.** Structural-drift risk justifies promoting to canonical spec text. ECR-policy reviewer + CL CVO consumer + any future maintainer landing on impl spec rather than canonical spec is the failure mode spec text prevents. Concrete spec language: amend §6.3 (Container escape minimization) OR new §2.5 (Runner IAM hard constraint) with: allowlist (5 actions named); BAN list (explicit prohibition of S3/SSM/IAM/SecretsManager/cross-account); rationale paragraph (minimal blast radius post-escape). Two upstream voices align (MSTR FN-1 corroborates dedicated EC2; CVO marks this "most worth promoting"). | **spec-amendment-flag** (v0.3) + WB-design-constraint (WB-2 carries) |
| **CV-A6** | Phase 5 output validation: host-side validator regex-scans final insight JSON for banned patterns (>500-char strings, eval-able payloads, absolute paths); BLOCK on violation | WB-3 (entrypoint scripts) | §5 banned-patterns list is currently soft constraint on Phase 5 output. CV-A6 adds host-side enforcement. Concrete impl: after analysis container exits + insight JSON captured via stdout, host-side Python validator (`validate_insight.py`) runs regex scan; violation → reject insight + log BLOCK event + add candidate URL to deny-list (CV-A3 path) + ws CVO MCP alarm. Runs on runner host outside container (compromised analyzer cannot subvert). WB-design-constraint suffices; impl spec carries the validator code + invocation pattern. | WB-design-constraint (WB-3) + WB-acceptance-criterion (WB-6) |

---

## §4 -- Table 2: TELEMETRY additive disposition (10 rows)

| ID | Summary | Proposed WB-phase | Rationale | Disposition |
|---|---|---|---|---|
| **FN-1** | Hook write path = sync jsonl + async broker hot-path. Sync jsonl preserves durability; async broker keeps tool-execution latency unaffected. Resolves §10 Q1. | WB-2 (hook impl) | Direct resolution of spec §10 Q1 -- adopted. Concrete impl: PostToolUse hook writes jsonl entry synchronously (durability); broker call dispatched via subprocess background or threading (non-blocking on hot path). Failure modes: jsonl write fail → `hook_errors.log` + still call broker; broker call fail → drop (broker warm-starts from jsonl). | WB-design-constraint (WB-2) |
| **FN-2** | `get_agent_status` returns `bg_in_flight` state (transparency). Helps /work workers see "lane peer is heads-down on bg" without poll-thrash. Resolves §10 Q5. | WB-3 (broker code amendment) | Direct resolution of spec §10 Q5 -- adopted. Concrete impl: broker `get_agent_status` response gets new field `bg_in_flight: list[{task_id, started_at, max_duration_sec, kind}]`. Empty list when no bg active. Schema-additive (no breaking change for existing consumers). | WB-design-constraint (WB-3) |
| **FN-3** | Phase-1 exit criteria: if disagreement rate between legacy heartbeat and telemetry exceeds 5% in observation week, re-evaluate thresholds BEFORE Phase 2 cutover (additional gate beyond <1% in spec §5.1) | WB-7 (observation acceptance criterion) | Spec §5.1 already names "<1% disagreement" -- FN-3 adds 5% as RE-EVALUATION threshold (not pass/fail). Concrete impl: observation dashboard tracks disagreement-rate metric; if >5% during week, AE 0.7 + ws CTO + ws CVO joint re-evaluation pre-Phase-2 (revise thresholds? extend observation? defer cutover?). Captured as named WB-7 acceptance criterion in impl spec. Pairs with CV-B2 (spot-check subscan). | WB-acceptance-criterion (WB-7) |
| **FN-4** | Phase-2-pre-cutover sweep: explicit check for any session still showing `_unknown_lane_check_needed` fallback-serial. Tie to §6.3 CVO /spot-check subscan as additional surface. | WB-8 (Phase-2 cutover pre-flight) | Concrete impl: WB-8 pre-flight check enumerates all telemetry entries in past 24h; any entry with `serial_source: "fallback"` OR literal serial `"_unknown_lane_check_needed"` BLOCKS Phase-2 cutover until resolved. Pairs with CV-B2 (spot-check telemetry-misconfig subscan as live monitor). Captured as named WB-8 pre-flight gate in impl spec. | WB-acceptance-criterion (WB-8) |
| **FN-5** | Cross-fabric (Open Q6): CL agents launching from ajb_workspace cwd are covered by ws-rooted hook. CL-side hook only needed if CL agents launch from CL-rooted sessions (currently zero). Verify per-CL-agent at Phase 1; no action needed unless gap surfaces. | WB-5 (per-lane synthetic-tool-call verification) + WB-7 (Phase-1 observation) | Concrete impl: WB-5 verification step expanded to include each CL serial (1.1.0_SA_CTO, 1.x.0_DS_CompLearns, 2.1.0_SA_COO, 3.1.0_SA_CVO); confirm each writes telemetry to ws-rooted `org/mcp/agent_telemetry/*.jsonl` via positive synthetic tool-call test. If any CL agent fails (launches from CL-rooted session), gate WB-7 on CL-side hook install in `feature_clb/.claude/settings.local.json`. CV-B5 extends this with formal Phase-1-cutover-gate language. | WB-acceptance-criterion (WB-5) + (combined with CV-B5) WB-acceptance-criterion (WB-6) |
| **CV-B1** | **JSONL privacy invariant:** hook writes `tool_name` ONLY; NEVER tool arguments, Bash bodies, file contents, MCP message bodies, env vars. `bg_task.task_id` OK (opaque). | WB-2 (hook impl) | **SPEC-AMENDMENT.** ~3 lines spec text to §3.4 prevents future hook-author from widening captured fields for "debugging convenience" -- which would leak Bash command bodies, file paths, MCP subjects, secret material flowing through tool arguments. Audit-trail spec section is the right home. Same structural-drift logic as CV-A5. Concrete spec language: "§3.4 (new subsection) **Privacy invariant**: Hook MUST write `tool_name` only; tool arguments and tool outputs are NEVER written to JSONL. Specific bans: NO Bash command-string, NO file contents from Read/Edit/Write, NO MCP message bodies, NO env vars. `bg_task.task_id` is OK (opaque identifier)." Two voices align (CVO authored; AE corroborates from prior LD-0070 WS-A audit experience -- the existing hook accidentally captures more than `tool_name` in some paths). | **spec-amendment-flag** (v0.4) + WB-design-constraint (WB-2 carries) |
| **CV-B2** | §6.3 CVO `/spot-check` telemetry-misconfig subscan MUST be live + clean for entire Phase-1 observation window before Phase-2 cutover. Any hook-misconfig detection during window resets observation clock. | WB-7 (observation acceptance criterion) | Spec §5.1 currently lists Phase-2 cutover exit criteria; CV-B2 adds the §6.3 subscan as explicit gate. Concrete impl: WB-6 Phase-1 deploy includes activating §6.3 subscan in CVO /spot-check skill; WB-7 observation week tracks subscan event-log; any hook-misconfig detection event resets the 1-week clock + AE 0.7 + ws CTO + ws CVO joint root-cause analysis. Pairs with FN-3 (5% disagreement gate) -- both gate same Phase-2 cutover moment with different evidence dimensions. | WB-acceptance-criterion (WB-7) |
| **CV-B3** | bg_task GC loop MUST emit own audit-trail entry per run (every 5min); separate /spot-check subscan flags "bg GC silent >15min". Optionally: bg-task self-heartbeat for long-runners (inbox-watch style). | WB-4 (bg_task lifecycle) | Concrete impl: orphan GC loop (§4.4) writes audit-log entry at end of each successful sweep (`{ts, event: "bg_gc_sweep", swept_count: N}`); separate CVO /spot-check subscan flags "no `bg_gc_sweep` entry in last 15min" as alarm. Stretch: bg-task self-heartbeat -- defer to observation-tunable (might be unnecessary if standard GC + sweep-audit is sufficient). Captured as named WB-4 mechanism in impl spec. Stretches into CV-B2 surface (both /spot-check subscans). | WB-design-constraint (WB-4) + observation-tunable (self-heartbeat) |
| **CV-B4** | Phase-3 pre-flight grep: comprehensive sweep across `.claude/skills/**/SKILL.md`, `org/tier*/**/prompt.md`, `org/mcp/**/*.sh`, `.tools/**`, `infra/aws/ec2/**` for `heartbeat(` calls + `mcp__opal-agent-comms__heartbeat` references. Phase-3 cutover BLOCKED until grep returns empty (or all surfaced callers explicitly cleared with rationale). | WB-10 (Phase-3 cleanup pre-flight) | Procedural risk MSTR FN-additives don't address: Phase 3 removes `heartbeat` MCP endpoint; missed caller = fail-loud break. Concrete impl: WB-10 cutover script runs the named grep; any matches surfaced as TO-list; each match resolved (drop call, OR explicit retention rationale logged). Cutover script exits 1 if unresolved matches. Captured as named WB-10 pre-flight gate in impl spec. | WB-acceptance-criterion (WB-10) |
| **CV-B5** | Phase-1-cutover-gate: positive confirmation each CL agent EITHER originates from ajb_workspace cwd (LD-0034) OR has CL-side hook installed; synthetic-tool-call verification. NOT just "verify at Phase 1" but Phase 1 BLOCKED until all confirmed. | WB-6 (Phase-1 deploy gate) | CV-B5 extends FN-5 from "verify per-CL-agent" to "block cutover until each CL agent positively confirmed". Concrete impl: WB-6 Phase-1 deploy pre-flight enumerates CL agents (1.1.0_SA_CTO, 1.x.0_DS_CompLearns, 2.1.0_SA_COO, 3.1.0_SA_CVO); each agent's session origin verified by inspection of `.claude/projects/<dir>/<session-uuid>.jsonl` location (ws-rooted vs CL-rooted) OR by positive telemetry-entry verification (synthetic tool call → check ws-rooted jsonl writes). Phase-1 deploy script exits 1 if any CL agent unverified. Combined with FN-5 forms complete WB-5+WB-6 cross-fabric coverage. | WB-acceptance-criterion (WB-6) |

---

## §5 -- Spec-amendment recommendation (final)

Three additives recommended for spec-amendment cycle, summarized in priority order:

| # | Spec | Section | Additive | Reason | Estimated spec text |
|---|---|---|---|---|---|
| 1 | CASE_FIND_SECURITY_PROTOCOL.md v0.2 → v0.3 | §6.3 (or new §2.5) | **CV-A5** -- Runner IAM hard constraint | Two-voice alignment (MSTR FN-1 + CVO "most worth promoting"); structural-drift risk for IAM is high (future maintainer/reviewer landing on impl spec misses authoritative source). Prevents drift class: "well, just add S3 access for X" | ~12-15 lines: allowlist (5 actions), BAN list, rationale paragraph |
| 2 | CASE_FIND_SECURITY_PROTOCOL.md v0.2 → v0.3 | §6.4 (minor citation fix) | **FN-4** -- Cite log-rotation cron file path | Pure documentation gap; tiny fix; bundle with #1 since same spec amendment cycle | ~1 line |
| 3 | TELEMETRY_LIVENESS_FRAMEWORK.md v0.3 → v0.4 | §3.4 (new "Privacy invariant" subsection) | **CV-B1** -- Hook writes `tool_name` ONLY | Privacy invariant has equivalent structural-drift risk to CV-A5; ~3 lines spec text vs future leak risk of Bash bodies/file contents/MCP subjects/secret material | ~3-5 lines |

**Sequencing per CTO MCP `[WB-1 ACK + spec-amendment pre-position]`:**

1. CTO scribes v0.3 (CASE_FIND, CV-A5 + FN-4 bundled) + v0.4 (TELEMETRY, CV-B1) in CTO author lane
2. CTO batched MCP `[LD-0078 RATIFY-REQUEST]` to MSTR for both v0.3/v0.4 amendments
3. CC ws CVO for independent ratification (clean independent posture -- CVO authored neither original spec nor proposed amendment language)
4. Per LD-0025 banked CORROBORATE-with-additives materializes-immediately discipline + the purely additive surface (no scope change, no operational reversal), expect clean RATIFY without re-cycle gate
5. If MSTR/CVO surface a refinement, revise pre-WB-2; if clean RATIFY, v0.3 + v0.4 carry as authoritative into WB-2 design-pass

**Final analysis holds the leans I pre-positioned in `[LD-0077-ACK]` MCP `20260526T021537Z`.** No revisions to disposition; CTO authorized to scribe.

---

## §6 -- WB-1 deliverable status

WB-1 phase per spec §8 was originally framed as:

- CASE_FIND WB-1: "Build `opal-case-find-download` + `opal-case-find-analysis` images; push to ECR; pin digests; track digests in `infra/aws/ec2/case-find-quarantine/IMAGE_DIGESTS.json`" (1d wall)
- TELEMETRY WB-1: "Audit current PostToolUse hook + identify serial-capture source reliability (§7)" (0.5d wall -- ALREADY DELIVERED in prior session 2026-05-26T~01:20Z at `41af4e546` + WB-1.1 patch pre-positioned at `e019ee4b5`)

This design-readout artifact is the **WB-1 design-readout deliverable per CTO's ask** -- not the WB-1 build/audit outputs themselves. The build/audit work happens at named WB phases per the matrix above.

For TELEMETRY WB-1 specifically: it is **already complete** (audit log `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-05-26/ld0070_postpostuse_hook_audit.md`; WB-1.1 patch proposal at `41af4e546`; env var name resolved at `e019ee4b5`). The session-id-keyed serial file pattern + `org/XXX.md` Step 1b ritual landed by ws CTO `4695f29ec` + `913816cbe` gives a partial WB-2 head-start as well (ritual that the future hook depends on is in production now via Step 1b).

For CASE_FIND WB-1: image build + ECR push + digest ledger creation is **pending Docker daemon recovery** (Andrew-side; engine 500 post-restart per LD-0067 v1 bridge smoke test blocked-state). Will execute when daemon comes back; not blocking design-readout.

---

## §7 -- Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-blast` | Not run | Pure doc-artifact authoring (single new markdown file under personal log directory). No portal/Lambda/EC2/script changes. Per CLAUDE.md AE row "When you're DONE: Committed a change → comp-blast — Blast radius unchanged" — there is no graph-node to blast on a personal log artifact. |
| `comp-pipescript deployed` | Not applicable | Not a gold/silver/bronze script change. |
| `comp-iam gaps` | Not applicable | No iam.tf change in this session yet (WB-2 IAM provisioning lands when image build + digest ledger lands). |

---

## §8 -- Authority trail

- **LD-0077** (MSTR sovereign 2026-05-26T01:55Z `cf0b2cdc5`) -- batched ratification CASE_FIND v0.2 + TELEMETRY v0.3 + /work SKILL.md; 9 FN-additives (CASE_FIND FN-1..4 + TELEMETRY FN-1..5); WB-1 parallel authorization
- **CVO LD-0077 independent verdict** (`07059979a` 2026-05-26T~02:00Z) -- CORROBORATE-with-additives both specs; 11 CV-additives (CV-A1..A6 + CV-B1..B5); no COUNTERs
- **ws CTO `[WB-1 CONSOLIDATED ADDITIVES]` MCP** (2026-05-26T~02:00Z) -- single source-of-truth consolidation + design-readout framework ask
- **AE 0.7 `[LD-0077-ACK]` MCP** (2026-05-26T021537Z) -- sequencing-rec (a) adopted; pre-flagged CV-A5 + CV-B1 spec-amendment leans + CV-A2 WB-design-constraint lean
- **ws CTO `[WB-1 ACK + spec-amendment pre-position]` MCP** (2026-05-26T~02:10Z) -- LEAN AGREE on all three pre-flagged dispositions; scribe path queued

## §9 -- Next-step dispatch

After this commit:

1. MCP ws CTO with `[WB-1 DESIGN-READOUT READY]` containing path + final spec-amendment recommendation (this matrix's §5)
2. CC MSTR + ws CVO
3. CTO scribes v0.3 + v0.4 spec amendments in CTO author lane
4. CTO batched MCP `[LD-0078 RATIFY-REQUEST]` to MSTR
5. Once v0.3 + v0.4 ratified, AE 0.7 begins authoring WS-B impl specs (`CASE_FIND_QUARANTINE_IMPL.md` + `TELEMETRY_LIVENESS_IMPL.md`) folding additives at named WB phases per this matrix
6. WB-2 design-pass commences in parallel for both LDs (different toolchains; no collision)

Standing: AE 0.7 LIVE on broker; `/work 20m` armed (cron 7,27,47); inbox-watcher tracked; ready for next dispatch.

-- 0.7.0_AE_CloudOps
2026-05-26
