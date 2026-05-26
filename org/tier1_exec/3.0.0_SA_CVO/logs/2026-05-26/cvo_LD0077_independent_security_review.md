---
agent: 3.0.0_SA_CVO
role: ws CVO (workspace Chief Verifier Officer)
date: 2026-05-26
session_event: post-respawn (LD-0074 kill 00:48Z -> /mstr-spawn ~02:00Z per LD-0076 canonical first-use)
trigger: LD-0077 batched ratification (cf0b2cdc5) -- MSTR-DIRECT ask for ws CVO independent security review (constitutional gate per CASE_FIND §10 + TELEMETRY §11)
artifacts_reviewed:
  - docs/architecture/CASE_FIND_SECURITY_PROTOCOL.md @ HEAD (v0.2, 58fce543a content baseline + post-ratify state)
  - docs/architecture/TELEMETRY_LIVENESS_FRAMEWORK.md @ HEAD (v0.3, 566647bfd content baseline + post-ratify state)
  - org/tier0/ledger/LD-0077.md (MSTR ratification rationale + FN-additives)
verdict_taxonomy: CORROBORATE / COUNTER / CORROBORATE-with-additives / CORROBORATE-with-CONCERN (4-shape per banked memory)
self_validation_surface: NONE (CVO did not co-author either spec; clean independent posture)
---

# ws CVO Independent Security Review -- LD-0077

## Frame

Per LD-0077 (MSTR ratification 2026-05-26T01:55Z) the constitutional gate at §10/§11 of both specs calls for ws CVO **independent security review** before AE_CloudOps Workstream B implementation kickoff. MSTR notes AE 0.7 WB-1 authorized to start in parallel per LD-0077 Path A rationale -- this review runs in parallel, not as a gate-before-WB-1; my findings feed pre-WB-7 (CASE_FIND smoke test) + pre-Phase-2-cutover (TELEMETRY) as the downstream gates.

CL CVO has consumer-of-record review separately for /case-find per CASE_FIND §10 reviewer list -- that's parallel, not mine.

I read both specs at HEAD + the LD-0077 ledger. MSTR's FN-additives (CASE_FIND FN-1..4 + TELEMETRY FN-1..5) are baseline; my review starts from there, either corroborating + extending, or countering if a structural concern surfaces.

## Verdict Summary

| Spec | Verdict | New CVO additives | Concerns flagged |
|---|---|---|---|
| CASE_FIND_SECURITY_PROTOCOL.md v0.2 | **CORROBORATE-with-additives** | 6 (CV-A1..A6) | 0 |
| TELEMETRY_LIVENESS_FRAMEWORK.md v0.3 | **CORROBORATE-with-additives** | 5 (CV-B1..B5) | 0 |

No COUNTERs. No CORROBORATE-with-CONCERN escalations. Both specs are structurally sound; CVO additives extend orthogonal surface area to MSTR's FN-additives. All ratification, FN-additives, and Workstream B parallel authorization stand.

## Methodology

Project-level /verify-channel pattern applied -- per banked memory `feedback_self_correction_upstream_of_verify_channel`, this is a **design-gate** independent review (not a REPAIR-AMENDMENT scope), so the lens is: are the threat models comprehensive, are the controls structurally sufficient, are the failure modes named with compensating controls, and are the implementation hooks specific enough that Workstream B cannot mis-implement.

Boundary test for CVO additives vs MSTR FN-additives: MSTR additives are **inside the design surface** (allowlist expansion, tuning, pointer citations). My CVO additives target **adjacent security surface MSTR didn't cite** (egress controls beyond app-layer allowlist, image-digest source-of-truth, telemetry as sensitive resource, etc.). Orthogonal-not-redundant.

---

## CASE_FIND_SECURITY_PROTOCOL.md v0.2 -- Detailed review

### Strengths (corroborating MSTR's RATIFY)

1. **6-phase pattern + key invariant** ("at no point does external code execute against the host") is the correct architectural anchor. Phase 4 NO-EXEC rule banning `pip install` / `npm install` / `python <file>` / `node <file>` / `make` / `eval`/`exec` of decoded payloads catches the well-known supply-chain attack vectors (setup.py-network, npm-lifecycle-script, obfuscated-payload-eval).
2. **§2.2 mandatory Docker flags** form a defensible envelope -- `--network=none --read-only --cap-drop=ALL --security-opt=no-new-privileges --pids-limit --memory --cpus --user=nobody --rm --label`. The mandatory framing (not a recommendation) is correct.
3. **§3.3.1 two-stage container** elegantly resolves the download-with-no-egress paradox via named volume (NOT host bind mount) preserving §2.3 zero-host-mount invariant.
4. **§4 12-class indicator taxonomy** with severity ladder BLOCK→deny-list-cache is practical defensive ops; the indicator classes cover the known patterns I would have expected.
5. **§5 Case-Insight extraction** "NO RAW CODE" + 500-char-cap + no-eval-able + no-absolute-path is defense-in-depth -- the insight artifacts themselves cannot become attack vectors.
6. **§6.3 6-layer container-escape defense** + dedicated EC2 recommendation correctly assumes a Docker zero-day will eventually happen and prepares for blast-radius minimization.
7. **§7 CLAUDE.md framing as ADDS-not-overrides** correctly preserves existing security rules (1-18) -- this is the right composition pattern, not a replacement.

### CVO additives (CV-A1..A6) -- ORTHOGONAL to MSTR FN-1..4

**CV-A1 -- Stage 3a network-layer egress control (defense beyond application-layer allowlist).**

§3.3.1 Stage 3a runs `--network=bridge` with `--dns=8.8.8.8 --dns=1.1.1.1` (public resolvers, bypassing any host-level DNS filtering). URL allowlist enforcement lives **entirely in `safe-download.sh`** (application layer). If that script has a parsing bug (URL-parser-differential, redirect-following without re-allowlisting, unicode-host-name homograph, percent-encoding bypass), arbitrary egress becomes possible during the download window.

**Recommend:** require Stage 3a to operate under a **network-layer egress firewall** -- either (a) `iptables`/`nftables` rules baked into the runner host that allow only specific egress destinations, OR (b) a dedicated Docker network whose only route is through an HTTP/HTTPS proxy that enforces the allowlist independently. Belt-and-suspenders -- a `safe-download.sh` bug should NOT result in arbitrary outbound traffic. Feeds into AE 0.7 WB-2 runner provisioning.

**Severity:** ERROR-class (not BLOCK). Spec is shippable v0.2 with `safe-download.sh`-only enforcement, but Workstream B should add network-layer enforcement before WB-7 smoke test if feasible; otherwise document as Phase-1-observe tunable with explicit re-evaluation gate.

**CV-A2 -- Image-digest source-of-truth + fail-closed launch.**

§2.1 requires `@sha256:` digest pinning. §2.4 mandates weekly rebuild for CVE patches. WB-1 (per LD-0077 FN-additive context) references `infra/aws/ec2/case-find-quarantine/IMAGE_DIGESTS.json` as the digest ledger. But the spec does NOT explicitly state:

(a) `IMAGE_DIGESTS.json` is the ONLY authoritative source of digests for the runner (no fallback to floating tags, no "latest" pull, no inline digest in a script that can drift from the ledger);
(b) the runner code MUST refuse to launch a container if it cannot resolve a digest from the ledger (fail-closed -- if digest unknown, do not run, raise alarm to ws CVO + AE 0.7).

Without this, a future maintainer can add a fallback path "well, just pull the latest if the ledger is missing" -- which silently undoes the digest-pinning security property.

**Recommend:** add to §2.4 (or new §2.5) the hard rule: "Runner MUST refuse to launch when image digest cannot be resolved from canonical ledger; floating-tag fallback is BANNED." This pairs with MSTR FN-4 (cron-rotation pointer citation) on the rotation side -- the digest LEDGER is the static source-of-truth; the rotation CRON updates the ledger atomically.

**CV-A3 -- Deny-list cache scope, TTL, and unpoisoning path.**

§4 BLOCK indicators add the candidate URL to a "deny-list cache." The spec does NOT specify:

(a) Scope: per-runner-local? cross-runner cluster-wide? cross-fabric (ws + CL)?
(b) TTL: 24h? permanent until manual unblock?
(c) Unpoisoning path: false-positives WILL happen (e.g., legitimate package with obfuscated minified-JS triggers OBFUSCATED_PAYLOAD); who can remove a URL from deny-list, under what authority?

Without unpoisoning + TTL, the deny-list can become a passive-DoS surface (legitimate packages permanently un-analyzable) OR a poisoning surface (attacker triggers a false-positive on a competitor's package).

**Recommend:**
- Scope: per-runner local (simpler; cross-runner sync deferred)
- TTL: 7 days default (after which, re-scan)
- Unpoisoning: requires ws CVO sign-off via audit-log entry referencing the original BLOCK event; manual `case-find-unblock <URL>` CLI tool that emits an explicit AUDIT_UNBLOCK row

**CV-A4 -- Audit log fail-closed semantics.**

§6.4 says `org/case-find-audit.log` is append-only "rotated by standard cron." §3.6 Phase-6 cleanup code `audit_log.write({...})` has no failure handling. The audit log is the ONLY record of what was analyzed + what was BLOCKED -- if writes silently fail (disk full, permission, file rotated mid-write), security-critical events vanish.

**Recommend:**
- Runner MUST detect audit-log write failure and **fail-closed**: refuse to start any new Phase 3 container if audit log is unwriteable; raise alarm via existing infra-alert mechanism (CloudWatch + ws CVO MCP)
- Phase 6 cleanup `audit_log.write()` wrapped in try/except where exceptions trigger the alarm path (NOT swallowed)
- Cron-based health check: log file exists + writeable + size growing during active periods + last-rotation-event sane

**CV-A5 -- Dedicated EC2 runner -- IAM blast-radius minimization (hard constraint, not recommendation).**

MSTR FN-1 corroborates dedicated EC2. WB-2 specifies IAM scope = "ECR pull + CloudWatch logs only" (LD-0077 ratification body). The spec body itself §6.3.6 frames the dedicated-runner as "consider running on a dedicated EC2 instance ... recommend dedicated runner." This is too soft.

**Recommend:** elevate to hard constraint in §2 or §6.3:
- Runner instance MUST NOT have IAM permissions beyond `ecr:GetAuthorizationToken` + `ecr:BatchGetImage` + `ecr:GetDownloadUrlForLayer` (read-only ECR pull) + `logs:CreateLogStream` + `logs:PutLogEvents` (CloudWatch logs)
- BANNED: any S3 read/write beyond ECR-backed S3 (which is implicit); any SSM permissions; any IAM AssumeRole; any cross-account permissions; any SecretsManager / SSM Parameter Store access
- Rationale: a successful Docker escape compromises only what the host can reach. Minimal IAM = minimal blast radius. Hard constraint blocks "well, just add S3 access for X" drift.

**CV-A6 -- Phase 5 "no raw code" enforced by host-side validator.**

§5 banned-patterns list ("any string > 500 chars from source corpus", "any eval-able string", "absolute paths") is currently expressed as a **soft constraint** on Phase 5 output. There is no mechanism specified to ENFORCE these constraints. A bug in the analyzer (or a clever payload that influences AST extraction output) could result in Phase 5 emitting raw code via `abstract_description` or `primitives_used` fields.

**Recommend:** add §5.x "Output validation":
- Phase 5 output MUST pass a **host-side validator** (runs outside the container) that scans the final insight JSON for the banned patterns (regex for >500-char strings; substring scan for `eval(`/`exec(`; absolute path detection)
- Validator failure = BLOCK-class event: insight rejected, BLOCK logged to audit, candidate added to deny-list, ws CVO MCP alarm
- Validator runs on host side (NOT in analyzer container) so a compromised analyzer cannot subvert it

### Open questions resolved or appropriately deferred

All 6 open questions in §9 are either addressed by MSTR FN-additives (Q1 dedicated EC2 = FN-1; Q5 allowlist = FN-2 + CV-A1 extends; Q6 NEEDS_HUMAN routing = clear) or appropriately deferred to AE 0.7 implementation judgment (Q2 toolchain pick; Q3 pattern taxonomy; Q4 triage thresholds tunable).

### Workstream B authorization posture

CVO concurs with LD-0077 authorization for AE 0.7 WB-1 to start in parallel. CVO additives CV-A1..A6 should be **folded into WB-1..WB-7 design-readout** as Workstream-B-specific constraints, NOT block WB-1 kickoff. Pre-WB-7 smoke test ratification gate is the appropriate moment for CVO + ws CTO + CL CVO to confirm all FN/CV-additives folded.

---

## TELEMETRY_LIVENESS_FRAMEWORK.md v0.3 -- Detailed review

### Frame note

This is fundamentally a **liveness/reliability framework**, not a security-only framework. But §10 Q7 raises the security angle ("the jsonl audit trail is a sensitive resource"). My security review focuses on the security surface; reliability/correctness of the dual-signal model + bg_task lifecycle + Phase 1/2/3 rollout is solid and I do not have substantive concerns there.

### Strengths (corroborating MSTR's RATIFY)

1. **Dual-signal model** (`LIVE` 120s work-threshold for dispatch / `SESSION_ALIVE` 600s any-kind-threshold for reaper) correctly de-conflates two semantic signals. Invariant `LIVE ⇒ SESSION_ALIVE` is correct.
2. **§1.3 consumer API** with `dispatch` defensive default = fail-safe (prefer false-negative over false-positive). Right call.
3. **§2 hot-path-vs-audit-trail decoupling** (in-memory tables + jsonl warm-start) handles broker restart resilience correctly.
4. **§3.2 tool-class → kind mapping** is comprehensive across the deferred-tool surface I can see.
5. **§4 bg_task lifecycle** with max_duration_sec defaults + §4.4 orphan GC handles the "long-running bg lies dispatch-LIVE" problem correctly.
6. **§5 Phase 1/2/3 rollout** with explicit exit criteria + dual-read safety belt during Phase 1 is measured progression.
7. **§7.2 session-id-keyed serial file** per AE 0.7 audit refinement is elegant -- per-session deterministic, tilde-lane-safe, broker-outage-decoupled.
8. **§8 LD-0063 bridge** semantically aligned (same 600s numeric value for SESSION_ALIVE) -- correct compatibility framing.

### CVO additives (CV-B1..B5) -- ORTHOGONAL to MSTR FN-1..5

**CV-B1 -- JSONL audit trail privacy invariant (per §10 Q7 -- stated as hard rule).**

§3.4 JSONL entry shape currently shows `"tool_name": "Edit"` -- not the tool arguments. This is correct, but the spec does NOT state it as an invariant. A future hook implementer reading §3 could reasonably add tool arguments to the JSONL for debugging convenience -- which would leak Bash command bodies, file paths read/written, MCP message subjects, and potentially secret material that flows through tool arguments.

**Recommend:** add §3.4 "Privacy invariant" subsection:
- Hook MUST write `tool_name` only; tool arguments + tool outputs are NEVER written to JSONL
- Specific bans: NO Bash command-string, NO file contents from Read/Edit/Write, NO MCP message bodies, NO env vars
- bg_task `task_id` is OK (opaque identifier, no payload)
- Rationale: JSONL is fabric-wide observability surface; treating it as sensitive-only narrows blast radius if access leaks

Q7 also suggests "same protection as `org/mcp/inbox/*` (filesystem perms + workspace-scope)." Filesystem perms is weak (all agent processes run under same Windows user, all can read each other's JSONL). The privacy invariant on what GETS WRITTEN matters more than file-perm protection in this environment.

**CV-B2 -- Phase-1 hook-misconfig detection as explicit exit-criterion (extends MSTR FN-4).**

MSTR FN-4 addresses fallback-serial sweep pre-Phase-2. CV-B2 extends: §6.3 already specifies a CVO `/spot-check` subscan ("any LIVE session per legacy heartbeat that has zero telemetry entries in the last 5min?"). The §5.1 Phase-1 exit criteria currently list "<1% disagreement" + "no hook-failure-induced false-STALE incidents" -- but does NOT explicitly require the §6.3 subscan to be running + passing as a Phase-2 cutover prerequisite.

**Recommend:** add to §5.1 exit criteria:
- "The §6.3 CVO /spot-check telemetry-misconfig subscan MUST be live + clean for the entire Phase-1 observation window before Phase-2 cutover. Any hook-misconfig detection event during the window resets the observation clock."
- Pairs with MSTR FN-3 (5% disagreement re-evaluation gate at Phase 1) -- both gate the same cutover moment with different evidence dimensions.

**CV-B3 -- bg_task GC as single point of liveness-truth.**

§4.4 orphan bg_task GC is the only mechanism that prevents a crashed session with an in-flight 24h SSM bg_task from appearing dispatch-LIVE for up to 24h. If the broker housekeeping loop crashes or stops firing (broker bug, restart-warm-start-skips-housekeeping-init, etc.), bg_in_flight entries become **liveness zombies** indefinitely.

**Recommend:**
- The bg_task GC loop MUST emit its own audit-trail entry on each successful run (every 5min); a separate /spot-check subscan flags "bg GC loop has not emitted in >15min" as alarm
- Consider: bg_task self-heartbeat. Long-running bg tasks (like `inbox-watch`) periodically ping the broker (every Nmin) -- if the bg task is dead, the heartbeat stops, and the broker can drop bg_in_flight earlier than max_duration_sec without waiting for GC.
- Minimum: spec should state the bg_task GC loop is a security-critical mechanism (not just a housekeeping nicety) and is independently monitored.

**CV-B4 -- Phase 3 pre-flight: comprehensive heartbeat-call sweep.**

Phase 3 cleanup removes the `heartbeat` MCP endpoint. The CVO `/spot-check` skill body, `/watcher` skill body, `/work` skill body, agent prompts, standing scripts, and miscellaneous Bash automations all currently call `heartbeat()`. Phase 2 makes `heartbeat()` a no-op (still callable, emits warning). Phase 3 removes it entirely -- callers fail-loud.

If even one consumer is missed, Phase 3 breaks it. This is a procedural risk MSTR's FN-additives don't address.

**Recommend:** add to §5.3 Phase 3 pre-flight checklist:
- Comprehensive grep across `.claude/skills/**/SKILL.md`, `org/tier*/**/prompt.md`, `org/mcp/**/*.sh`, `.tools/**`, and `infra/aws/ec2/**` for `heartbeat(` calls + `mcp__opal-agent-comms__heartbeat` references
- Each surfaced caller updated to drop the call OR explicit decision to leave it (it's a no-op in Phase 2; just emits a warning)
- Phase 3 cutover blocked until grep returns empty (or all surfaced callers explicitly cleared)

**CV-B5 -- Cross-fabric CL hook verification gate (extends MSTR FN-5).**

MSTR FN-5 corroborates per-agent CL verification. CV-B5 extends to procedure:
- Phase-1-cutover-gate: positive confirmation each CL agent's session originates from ajb_workspace cwd (LD-0034 unified inbox path) by inspection of `.claude/projects/<dir>/<session-uuid>.jsonl` location OR by confirmation of CL-side hook installation in `feature_clb/.claude/settings.local.json`
- NOT just "verify at Phase 1" but "Phase 1 cutover BLOCKED until all CL agents have positive confirmation either way"
- Confirmation method: synthetic tool call from each CL agent + verify telemetry entry appears in ws-rooted `org/mcp/agent_telemetry/{serial}.jsonl`

### Open questions resolved or appropriately deferred

All 7 open questions in §10 are either addressed by MSTR FN-additives (Q1 sync/async = FN-1; Q5 bg_task in get_agent_status = FN-2; Q6 cross-fabric = FN-5) or CVO additives (Q7 telemetry as sensitive surface = CV-B1), or appropriately deferred to AE 0.7 implementation judgment (Q2 bg_task defaults; Q3 broker invocation mechanism; Q4 fallback discounting).

### Workstream B authorization posture

CVO concurs with LD-0077 authorization for AE 0.7 WB-1 (TELEMETRY) to start in parallel. CVO additives CV-B1..B5 fold into WB-2/WB-3 design + WB-7 + WB-9 observation criteria. Pre-Phase-2 cutover ratification gate is the appropriate moment for CVO + AE 0.7 + ws CTO to confirm all FN/CV-additives folded.

---

## Self-validation surface (mitigation transparency per banked pattern)

Per `feedback_cvo_self_validation_mitigation_pattern.md`: ws CVO did NOT co-author either spec. Both specs were authored by 1.0.0_SA_CTO (ws CTO) in Workstream A. CVO's prior contribution was the `/verify-channel` skill itself (used as the lens for this review) -- which is the verification methodology, not the artifacts under review. Clean independent posture; no review-conflict mitigation needed.

LD-0077 ratification body was authored by 0.0.0_AB_MSTR -- CVO did NOT contribute to LD-0077 directly. Reading MSTR's FN-additives + corroborating/extending them is the canonical CVO independent-review pattern; not self-validation.

## Verdict footer

**CASE_FIND_SECURITY_PROTOCOL.md v0.2:** CORROBORATE-with-additives -- CV-A1 through CV-A6 fold into AE 0.7 Workstream B design-readout + pre-WB-7 smoke test ratification gate. All MSTR FN-additives (FN-1..4) stand. No COUNTERs.

**TELEMETRY_LIVENESS_FRAMEWORK.md v0.3:** CORROBORATE-with-additives -- CV-B1 through CV-B5 fold into AE 0.7 Workstream B design-readout + Phase-1 observation criteria + Phase-2 cutover gate + Phase-3 pre-flight checklist. All MSTR FN-additives (FN-1..5) stand. No COUNTERs.

**Workstream B authorization:** CVO concurs with LD-0077 parallel authorization. AE 0.7 may proceed with WB-1 (both LDs) immediately; CVO additives are constraints folded into Workstream B design, not pre-WB-1 gates. CVO will re-engage for pre-WB-7 (CASE_FIND smoke test) + pre-Phase-2-cutover (TELEMETRY) ratification.

**ws CVO standing:** post-respawn (per LD-0076 canonical first-use); registered LIVE on broker (PID 33692); inbox-watcher tracked (task `bawhbp2gi`); `/spot-check` will be armed at standard cadence following this review landing.

-- 3.0.0_SA_CVO (ws CVO)
2026-05-26
