# Session (cont.) — exit-143 watcher disruption rectified + comp-tool HUD shipped + catalog/registry hygiene
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE, SCRIBE

Continuation of the 2026-06-15 session (prior log: session_graph_p0_and_nfra_estate_arc.md a11f0f4f6, which ended at NFRA_PIPESCRIPT registration). This delta = the pipescript full-build rulings, the exit-143 fabric-disruption rectification, the catalog/registry hygiene, the comp-tool HUD (NFRA_TOOLHUD), and the NFRA_GCONTR seed registration. Per-thread detail is in the broker record + the cited commits.

## 1. NFRA_PIPESCRIPT — full-PRD build driven to close (my depth-rulings)
Andrew extended the /goal from a+b+c to full-PRD. My PRD-author calls drove the forks:
- P1b.2 routing-dispatch = read-only POINTER + catalog (NOT live sub-resolver invocation) -- the builder independently converged; adopted its "canonical call-string" refinement; F5 (read-only, never re-run expensive tools).
- P3.2 FE-reachability = DATA-primary (surface CVO ground-truth reachability_status), REJECT the live-portal grep -- decisive correctness call: bd-time-machine's provider EXISTS in code, so a live grep certifies the phantom as reachable; only ground-truth catches it.
- Cross-tool lane CONVENTION (two-rule): same-tool = decomposition-grant; cross-tool = author-by-anyone, review+commit-by-OWNER (DS edits AE's comp-pipescript -> AE ratifies). COO banked it.
COO closed the /goal (ead69f1e5, 2-step atomic): pipescript LIVE, 25 named threads, CVO 3-way gate-b + gate-c attestation.

## 2. exit-143 WATCHER DISRUPTION — analyzed + rectified + ledgered (Andrew-direct)
Andrew asked me to explore the recurring exit-143 Monitor deaths. Investigation (ground-truthed, not banked-conclusion): exit-143 = external SIGTERM; the dead-task tail delivered every message then "Terminated"; kill-agent ruled out (precise serial-match); the audit precedent (2026-05-30 watchers_reaped=1 on my serial) is real-but-distinct. MSTR (Andrew-direct) confirmed the TRUE trigger: a register_agent PostToolUse hook running `kill-orphans --stale --force` FABRIC-WIDE on EVERY registration -> reaps live-but-stale-reading watchers; SILENT (no audit). Rectification (Andrew refined to scope-to-serial-tilde-specific; "validate in design"):
- FIX A interim: removed the fabric-wide reap from the register hook (2f4b2b9e6).
- Real fix: `kill-orphans --serial <S>` EXACT tilde-match (~A reaps only ~A, never base/~B) + AUDIT every reap (was silent) + hook_register_orphan_cleanup.py (scoped, per-session V4 marker = no self-kill on re-register). Empirically tested V1/V2; caught + fixed a set-e/grep-no-match bug during testing (84b381c56). MSTR ledgered LD-0193, COO co-signed.
The watcher fix being a careful-not-fast shared-tooling change WITH testing is the through-line: a subtly-wrong reaper is what caused the incident.

## 3. CATALOG + REGISTRY hygiene (Andrew-direct)
- Registered pipescript in CLAUDE.md + graph-call-manifest (refreshed the stale 16->25 thread P1-only entry) + comp-tools.yaml. Consistency audit caught a REAL gap: comp-surface-check (D8 gate) was in CLAUDE.md + .tools/ but UNACCOUNTED in the manifest -> added to excluded_not_graph_use_cases (sibling of comp-manifest-check D6). All comp-*/pipescript now accounted (ff764cf80).

## 4. NFRA_TOOLHUD — comp-tool HUD, all 3 arms shipped (Andrew "agent HUD" question)
The catalog is the discoverability FLOOR; the HUD problem is salience-at-decision-time (agents blind-grep over the stronger repo-scoped tool). #1 (CTO): PreToolUse intercept hook (.tools/hooks/comp-tool-hud.sh) -- surfaces the comp call via additionalContext when an agent Grep/Globs a comp-answerable signature; advisory + anti-noise dedupe + logged; retuned to CVO's baseline (5 classes by bypass-volume + the negative filter = the non-noise key) + fixed a silent-dead-hook landmine CVO caught (IFS-tab-collapse on absent session_id). #2 (CTO): comp-which router -- natural-language question -> canonical call (the catalog made queryable); CVO's 6 mappings route correctly. #3 (CVO): the baseline (~15-20% of repo relationship-searches are comp-answerable; comp-pipescript+portal = ~80% of volume) + the reproducible before/after oracle (hud3_classify.py). Project NFRA_TOOLHUD registered.

## 5. NFRA_GCONTR seed registered (Andrew "make sure this is in there")
DS~A's period-contracts brief (48635a865) was committed but tracked by NO project -- registered NFRA_GCONTR (a129e9467): a graph_contracts table machine-encoding never-widen at the VALUE layer (the BMKAUD semantic-break class). CTO schema-ratify is the queued NEXT gate (mine), then AE Iceberg / CVO contracts / DS pipescript surface.

## Also ruled this window
B2 surface-check scope (portal surfaces scan vs the STITCH not the AWS-only derive) + stitch refresh flag; AE L4 derive-rebuild ack (graph caught up to current AWS state -- the P0's substantive recovery complete).

## Compiler Tools
| Tool | Run? | Result / why |
|---|---|---|
| comp-manifest-check list | YES | verified the graph-call-manifest LOADS cleanly after my pipescript + comp-surface-check edits (47 entries, canonical=47). |
| comp-which | YES (built + tested) | the new #2 router; routes all 6 CVO question-classes correctly + gold-id substitution. |
| catalog accounting audit (bash) | YES | every .tools/comp-* + pipescript accounted in the manifest (use-case OR explicit-exclusion); caught comp-surface-check unaccounted. |
| comp-tool-hud.sh | YES (built + tested) | the #1 intercept hook; advise/silent/dedupe/negative-filter/no-session_id all tested green. |
| pipescript | N (verified flags only) | not run for analysis this window; the catalog work registered + ground-truthed its shipped flags (--list output = 25 threads). |

## Open (mine)
NFRA_GCONTR CTO schema-ratification (next gate). YALP_YCUTVR PRD. OPLMCP IT-host (Andrew's send-now-vs-pin-host call). kill-agent found=0 live-liveness guard (queued, lower-pri, MSTR-assigned). Event-driven: AE globgrph ingest-filter/purge/re-enable RAVCs; CVO NFRA_TOOLHUD post-hook re-measure (the AFTER).
