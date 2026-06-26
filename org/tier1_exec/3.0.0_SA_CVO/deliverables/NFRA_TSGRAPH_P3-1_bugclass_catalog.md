# NFRA_TSGRAPH P3-1 — Log-Mined Bug/Logic-Class Catalog

**TO:** NFRA_TSGRAPH.P3-1 · **Author:** 3.0.0_SA_CVO · **Started:** 2026-06-18 · **Updated:** 2026-06-26 (deep pass 2) · **Status:** WIP (50 classes, all exemplar-anchored — exhaustive 215-LD semantic mine COMPLETE; remaining: root-cause-section long-tail sharpen + frequency recompute + Phase-3 partition audit + fabric-cluster COO ruling)

**Independence boundary (on the record per RAVC2):** this catalog is a FACTUAL mining artifact (data, not a verification verdict), so authoring it does not compromise CVO independence to later verify P3 *detectors* (verified against the live graph + real exemplars, independent of this class list). The ONE soft self-reference is catalog-*completeness* verification ("did P3-2 cover every catalogued class?") — for that specific check, this catalog is a CHECKABLE INPUT, not authoritative ground truth; the NFRA_DEBTSCAN cross-domain second-read + the real-exemplar bar cover it.

---

## Phase-1 — corpus density baseline (vs PRD section-9 census)

| Metric | Observed (2026-06-18) | Census | Note |
|---|---|---|---|
| session logs | 2749 | ~2745 | INTACT (grew slightly) |
| LD records | 204 | 203 | INTACT (+1 = LD-0202) |
| root-cause files | 900 | ~756 | coarse regex `root.?cause` over-matches; same OOM |
| silent-* files | 671 | 524 | `silent` broader than `silent-*`; same OOM |
| P0 files | 312 | 459 | case-exact `P0` under-counts; methodology delta |
| named-class files | 795 (raw) | 71 | **regex unfit** — `[a-z]+ class` catches asset/share/sub/closeout-class meta-vocab |

**Methodology finding (drives the build):** pure regex over-matches the fabric's heavy *process* meta-vocabulary (`closeout-class`, `sub-class`, `sovereign-class`, `stop-class`, `verdict-class`, `gap-class` — process taxonomy, NOT bug classes). The named-bug/logic-class mine must be **semantic** — read the root-cause / postmortem / LD incident contexts and name the class — not regex-counted. The `silent-*` family is the exception: it regexes cleanly into real named classes.

**Corpus = intact → proceed to mine** (do not assume the census numbers; mine what is present, per TO `if_mismatch`).

---

## Partition framework (Andrew-LOCKED boundary)

- **(A) FRONTEND/TS-detectable** → feeds **P3-2 (DE graph detectors on the NFRA_TSGRAPH graph)**.
- **(B) CROSS-DOMAIN (pipeline/data/infra/fabric)** → routes to **NFRA_DEBTSCAN** (the estate scanner). **NOT built in P3.** No NFRA_TSGRAPH scope-creep into a general estate bug-miner.

Every row cites ≥1 real log/LD/commit exemplar (the empirical anchor P3-2's validation gate depends on). `[sharpen]` = real anchor found, canonical/sharpest exemplar to be pinned in the deep pass.

---

## (A) FRONTEND / TS-detectable partition

| # | class | signature | exemplar (log/LD/commit) | freq | 
|---|---|---|---|---|
| A1 | OFC-cohort/ternary-fork | a cohort/feature mode adds a ternary branch that silently diverges display for one cohort; the un-forked branch keeps old behavior | 1.0.0_SA_CTO/2026-04-13 advi_office_prd_and_dim_analysis; W3 OFC incident (CLAUDE.md DE mandate) | 67 |
| A2 | cross-firm-conditional-asymmetry | `firmId===`/firm-conditional render path treats one firm differently with no symmetric branch (49F vs others) | 1.0.0_SA_CTO/2026-03-10 advi_apiscp_v5_architecture_decision | 127 [sharpen] |
| A3 | silent-display-fork | two code paths render the same datum differently; no error, just divergence (the NNA dual-attribution display class) | 3.0.0_SA_CVO/2026-05-23 cvo_loop_1801Z_LD0024_path_b_verdict | 11 |
| A4 | any-type-erosion | `: any` / `as any` defeats the type-check at a data boundary → undetected shape drift downstream | (broad; 64 files) [sharpen to a real FE instance, not narration] | 64 |
| A5 | dead-code | unreachable branch / retired component still imported; reads as live | (broad; 140) [sharpen — distinguish real dead-code incidents from the word] | 140 |
| A6 | prop-drill-depth | a prop threaded through N intermediate components; a drop at any level silently undefines it downstream | 1.0.0_SA_CTO/2026-04-08 compiler_toolchain_buildout | 6 |
| A7 | hook-dep-mismatch | useEffect/useMemo dependency array omits/over-lists a dep → stale closure or render storm | 0.3.0_DE_TradingOperations/2026-05-19 SSCN_DIVDEF.001_portal_default_state | 16 |
| A8 | render-guard-vs-nullability | a render reads a possibly-undefined field without a guard (or a guard keyed on the wrong field) → blank/NaN/crash | 1.0.0_SA_CTO/2026-03-10 aua-projection-formula-overhaul | 32 [sharpen] |

---

## (B) CROSS-DOMAIN partition (→ NFRA_DEBTSCAN, not built in P3)

| # | class | signature | exemplar (log/LD/commit) | freq |
|---|---|---|---|---|
| B1 | silent-no-write | producer runs heavy, exits before/around the write step; stale prior artifact reads as fresh; rc may be 0 | 0.4.0_DS/2026-06-18 nnaattr_d00f_seriestie... (D_00f 06-18 nightly; CVO-caught) | 1 (new) |
| B2 | silent-freeze | a HEAD/sentinel/chain stops advancing with no error (self-inflicted guard or stuck quorum) | 1.0.0_SA_CTO/2026-06-15 session_graph_p0; Nessie 2.7d HEAD freeze | 4 |
| B3 | silent-fallback | a code path silently falls back to a default/legacy value masking a real gap | 0.4.0_DE/2026-04-09 advi_49push_020_platinum_wiring | 9 |
| B4 | silent-advance | a checkpoint/cursor advances past unprocessed work (the /spot-check checkpoint class) | 3.0.0_SA_CVO/2026-05-23 cvo_loop_0625Z | 19 |
| B5 | silent-drop | rows/records dropped (dedup, filter, join-miss) with no count assertion | 0.1.0_DS_MarketIntelligence~C/2026-05-26 yalp_correl_002_ship | 4 |
| B6 | silent-drift | served/stored value drifts from source over time; no parity gate catches it | 3.0.0_SA_CVO/2026-05-23 cvo_loop_0825Z | 5 |
| B7 | silent-close / silent-skip | a handler branch no-ops / a stage skips with no loud signal | 1.0.0_SA_CTO/2026-04-20 advi_staudt_prd; 0.4.0_DS/2026-04-15 b3_fix_d02_loader_warn_loud | 10/2 |
| B8 | fork-stale-shadow | a forked-from pipeline (bd→cot) carries the parent's config/code dead/unwired; orphan stanzas | feedback_bd_cot_fork_validate_config_stale_shadow; NFRA_COT_TOOLING 6bc1f1ce3 | [sharpen] |
| B9 | self-inflicted-guard-false-reject | a guard built on a wrong invariant rejects every valid case (Nessie snapshot.parent null-by-design orphan detector) | reference_nessie...snapshot_parent_null; a613084cb | [sharpen] |
| B10 | synthetic-not-real-validation | a fix validated on a synthetic case is asserted to prove the real case; magnitudes differ | 0.4.0_DS/2026-06-18 D_00f series-tie (18.18M synth vs 74.2M real) | 1 (new) |
| B11 | rc0-self-report-trusted | a producer's rc=0 / self-report trusted instead of the served artifact (CLAUDE.md NEVER #4) | INFRPT long-lambda sync-invoke retry-storm; reference_long_lambda_sync_invoke | [sharpen] |
| B12 | sentinel-keyed-to-wrong-day | a D-1 pipeline's completion sentinel keyed to data-day not serving-day → chronic late/stale | reference_d1_pipeline_freshness_fix; BRONZE-FIX #6 1a1d555f2 | [sharpen] |
| B13 | confirmed-not-delivered | "subscribed/published/applied" trusted as "delivered/effective" (SNS sub≠delivers; alarm in-period re-flip) | reference_sns_confirmed_sub_not_equal_delivers (NFRA_INFRPT 2026-06-17) | [sharpen] |
| B14 | gzip-cap-large-artifact | CloudFront auto-gzip caps at 10MB → large JSON served raw unless origin pre-gzipped | reference_cloudfront_10mb_autocompress_cap; 49NNAFIX D1 | [sharpen] |
| B15 | tooling-false-empty (grep-via-subprocess) | a harness check returns empty/rc0 from a broken subprocess → false ground-truth verdict | reference_python_subprocess_bash_launchers_grep_fail_on_windows | [sharpen] |
| B16 | force-add-pathspec-gitignore-bypass | safe-commit force-stages a directory pathspec → commits gitignored build artifacts | reference_safe_commit_force_adds_pathspec; NFRA_TSGRAPH.P0 node_modules | [sharpen] |
| B17 | deny-star-false-public-grant | an IAM `Principal:*` on `Effect=Deny` mis-flagged as a public grant (guardrail, not exposure) | reference_deny_principal_star_is_guardrail; NFRA_COMPAWS 2026-06-08 | [sharpen] |
| B18 | mark_read=false-unread-inflation | check_inbox(mark_read=false) inflates unread → false-DEAF reap candidate on a live paced agent | reference_false_deaf_reap_candidate; 0.7.0_AE~B 2026-06-17 | [sharpen] |

---

## To-mine (deep semantic pass — next, interruptible by #9/§9)

1. **LD records (204)** — the densest curated incident source; semantic-extract each LD's named class + the postmortems (`docs/architecture/POSTMORTEM*`). Highest yield for sharp exemplars.
2. **root-cause sections (900 files)** — semantic, not regex; pull the "root-caused to X" → class.
3. **Sharpen every `[sharpen]` row** to its canonical/sharpest exemplar (real incident, not narration of the word).
4. **Frequency** — recompute per-class on the SEMANTIC class definition (the regex freqs above are upper bounds incl. meta-vocab).
5. **Partition completeness audit** (Phase-3 mandate): 0 untagged rows, 0 exemplar-less rows.
6. **Hand-off at close:** frontend partition → P3-2 (DE); cross-domain partition → NFRA_DEBTSCAN (COO). RAVC2 to COO + CC CTO + DEBTSCAN owner.

---

## v2 additions — deep pass 1 (LD records + POSTMORTEM_SHARED006)

**Frontend partition — new + sharpened:**

| # | class | signature | exemplar | 
|---|---|---|---|
| A2 [sharpened] | cross-firm-conditional-asymmetry | canonical exemplar pinned: `AuthContext.tsx:35` hardcoded raw `'bd'` literal (firm not parameterized) | POSTMORTEM_SHARED006_CANONICALIZATION_20260514 |
| A9 | hardcoded-firm/env-literal | a firm/env value hardcoded as a string literal instead of read from context/config → breaks the moment a 2nd firm/env appears | POSTMORTEM_SHARED006 (`'bd'` literal) |
| A10 | audit-scope-miss | a verification's grep/search scope is too narrow → the bug sits outside the scanned subtree and the audit passes false-clean | POSTMORTEM_SHARED006 (§G grep scope = `pages/AdvisorIntelligence/` only, missed AuthContext) |

**Cross-domain partition — the `stale-*` family (parallel to `silent-*`) + self-reference:**

| # | class | signature | exemplar |
|---|---|---|---|
| B19 | stale-verify | a verification verdict trusted past its vintage; re-run not gated to current state | LD-0155 |
| B20 | stale-cache | a cache/derived value served without a freshness gate (the gldinc ungated-cache P0 class) | ADHC_GLDINC P1 shadow-removal; reference_d1_pipeline_freshness |
| B21 | stale-graph-phantom | a scratch/frozen-vintage graph DB quoted as live → phantom nodes/edges (trade-recon phantoms) | NFRA_COMPAWS Wave-4 cert f9a92fcec (trade-recon 0-live phantoms); comp-kuzu UNKNOWN-VINTAGE |
| B22 | stale-sub/aggregate | a subscription/rollup not recomputed on source change → drifted aggregate | LD-mine (stale-sub/stale-aggregate); reference_sns_confirmed_sub |
| B23 | scanner-self-false-positive | a scanner/checker flags its OWN footprint/artifact as a finding (Deny+`*` guardrail; derive-artifact self-flag) | LD-0100; reference_deny_principal_star_is_guardrail (NFRA_COMPAWS IAM-PUBLIC-DENY-FP) |

**FABRIC/agent-process cluster — PARTITION NUANCE (flag to COO):** these fit NEITHER the frontend-detector partition NOR the estate-pipeline DEBTSCAN partition cleanly — they're agent-fabric *reliability* classes. The Andrew-locked boundary is frontend-vs-cross-domain; this cluster is a gray zone. **Recommend COO/CTO rule whether fabric-reliability classes are in P3/DEBTSCAN scope or a separate concern** (do not silently fold them into either partition).

| # | class | signature | exemplar |
|---|---|---|---|
| F1 | marker-artifact-false-positive | marker/telemetry-tracking artifact misreads liveness → false reap/DEAF on a live agent | LD-0197; LD-0193; reference_false_deaf_reap_candidate |
| F2 | shared-resource-contention | multi-agent shared index/worktree/repo contention (observed live this session: COO commit 1c744a4b0 rode my push on the shared repo) | LD-0127; reference_safe_commit_force_adds_pathspec |
| F3 | race-class | concurrency race (registration/spawn/hook ordering) | LD-0140 |
| F4 | iteration-debt | repeated re-derivation / high-archetype-cost loops (the COST signal, not bugs) | LD-0029 |

## v3 additions — deep pass 2 (exhaustive LD-record semantic mine, all 215 LDs)

**Method:** extracted every LD `decision_summary` (org/tier0/ledger/LD-0001..0215), filtered to incident/root-cause-bearing entries (governance/charter/spawn LDs carry no bug class — confirms the Phase-1 methodology finding), semantic-read each. Yield below. Every row cites the LD that IS the empirical anchor (Rule-22 grounded — these are SOURCE incident records, not narration).

**Cross-domain partition — new (→ NFRA_DEBTSCAN, not built in P3):**

| # | class | signature | exemplar (LD) | freq |
|---|---|---|---|---|
| B24 | worktree-gitdir-path-assumption | code assumes `$REPO_ROOT/.git` is a DIRECTORY, but in a linked worktree it is a FILE (gitdir pointer) → `mkdir`/path-op fails ENOTDIR → silent fallback to an unsafe path (lock never acquired → unserialized commit storm) | LD-0138 (safe-commit LOCK_DIR; "same .git-is-a-file worktree-path bug class as the precommit-guard false-alarm"); LD-0140(a) | 2 |
| B25 | config-in-unread-file / silently-ignored-flag | config wired into a file the tool does NOT load (settings.local.json vs committed settings.json), or a flag that silently SUPPRESSES (`async:true` killed hook firing) → looks-correct, never effective; prior "fix" targets the wrong layer | LD-0139 (3-day fabric telemetry-dead; "wired into the file CC won't read") | 1 |
| B26 | fix-against-unverified-hypothesis | a fix shipped against a diagnosis that was never ground-confirmed → addresses the wrong class, real defect persists (the operational sibling of the Rule-22 grounding gap) | LD-0125/0126 (F-004 watchdog "shipped against wrong hypothesis"; storm root-cause twice-misframed); LD-0140(a) ("ruled without checking current state") | 3 |
| B27 | noise-misattributed-as-cause (red-herring-log) | a loud/plausible background signal (a deprecation log, a co-occurring error) blamed as the cause while the true cause sits elsewhere; the inverse of grounding | LD-0144 (GCM DEPRECATED_ENDPOINT noise vs the real bun-Playwright transport hang) | 1 |
| B28 | liveness-proxy-answers-for-dead-principal | a liveness check queries a PROXY (broker server PID / "1s ago") that is alive while the actual agent loop is wedged/dead → phantom-LIVE, messages accumulate unseen | LD-0111 (watcher-dead-but-broker-LIVE 12h phantom-inbox-receiver); LD-0181 (broker "1s ago" = server.py not the claude loop) | 2 |
| B29 | local-event-triggers-global-destructive-sweep | a per-actor hook performs a FABRIC-WIDE destructive action (register hook ran `kill-orphans --stale --force` on every registration → each spawn SIGTERM'd peers' live watchers), and is SILENT (0 audit) → "undetermined" disruption | LD-0193(a) (exit-143 live-watcher-reap root cause) | 1 |
| B30 | aggregate-poll-amplification | a per-client-benign poll interval × a fleet of N clients = sustained load that exhausts a shared resource (POLL_INTERVAL_S 2.0 × 14 servers = 7 polls/s → 617 TIME_WAIT sockets) | LD-0125 (broker polled-to-death; the fleet, not a self-spin) | 1 |
| B31 | schema-key-drift-silent-empty-iterate | a consumer reads the WRONG key (`use_cases` vs the stored `entries`) → iterates an empty collection → matches nothing, EVER, with no error (a backstop that silently covers nothing) | LD-0208 (comp-which manifest-fuzzy backstop non-functional; ~28/36 tools unreachable) | 1 |
| B32 | set-once-clobbered-by-later-emit | a value set at launch/init (tab title via OSC/WindowTitle) is silently overwritten by the app's own RUNTIME emit; the fix needs a layer that IGNORES later writes (suppressApplicationTitle) | LD-0101 / LD-0103 / LD-0182 (WT tab-title override by claude.exe runtime OSC) | 3 |
| B33 | shared-global-last-writer-wins-cross-attribution | a value resolved from a single GLOBAL shared file (`.comp-graph/.agent_context` TO_ID) that every concurrent actor overwrites → last-writer-wins cross-attributes work to the wrong owner (per-process env escapes it) | LD-0205 (comp-log TO_ID race; corrupted NFRA_COMPRAIL TO-5 per-TO coverage) | 1 |
| B34 | gate-keyed-on-presence-not-addressee | a gate keyed on a message being PRESENT rather than ADDRESSED-to-this-actor trips on foreign traffic (tilde-lane ferry copies scatter into unrelated base inboxes → false HALTGT trip; reflexive ack risks training away a real [STOP]) | LD-0131 (HALTGT ferry-scatter false-trip) | 1 |
| B35 | ungrounded-mechanism-inference | a causal/WHY claim asserted from a grounded SYMPTOM but an INVENTED mechanism, then escalated to "proof/root-cause" → nearly drives a needless fix (the Rule-22 incident class) | LD-0206 (COTETL canonical-seal mis-inference 2026-06-22; grounded symptom, invented mechanism) | 1 |

**Both-partition / methodology — new:**

| # | class | signature | exemplar (LD) | partition |
|---|---|---|---|---|
| A11 | classifier-matches-mention-not-instance | a classifier/regex matches the VOCABULARY of a thing appearing in a report rather than an actual INSTANCE of it ("andrew ruling"/"sovereign decision" in a *status report* misread as a sovereign-decision *request* → false escalation; the named-"X class" regex over-matching process meta-vocab — the catalog's OWN Phase-1 finding) | LD-0163(2) (sovereign-classifier FP); the Phase-1 named-class regex finding (this catalog §Phase-1) | **frontend-detectable** (regex/classifier scope is TS-graphable) AND cross-domain (fabric classifiers) — dual; primary→frontend |

**Sharpened existing rows (canonical exemplar now pinned):**

| row | sharpened anchor |
|---|---|
| B23 scanner-self-false-positive | LD-0100 — `/mstr-spawn` marker scan matched the scanner's OWN PowerShell process (search-pattern literal in its CommandLine arg); fix = `$_.ProcessId -ne $selfPid`. Canonical exemplar. |
| F1 marker-artifact-false-positive | LD-0193(a) (silent fabric-wide reaper) + LD-0158 (exit-143 idle-lane Monitor-death → silent-unreachable) |
| F2 shared-resource-contention | LD-0127 (658-file CL strip — split-at-source > mediation-at-checkpoint) + LD-0138/0140 (shared git index) + LD-0205 (shared .agent_context) — canonical cluster |
| F3 race-class | LD-0070 (kill-orphans liveness-window race, SIGTERM'd MSTR 2x) + LD-0205 (TO_ID write race) |
| B15 tooling-false-empty | LD-0208 (key-drift silent-empty) is the config-drift sibling of the subprocess-false-empty original — cross-referenced, kept distinct (B31) |

## Phase-2 mandate — DEBTSCAN double-build check (2026-06-26, CONFIRMED clean)
Ran the TO Phase-2 mandate: confirm this catalog is the shared UPSTREAM, not a duplicate of
an existing NFRA_DEBTSCAN artifact. `comp-which` routed via the manifest fuzzy-backstop (no
curated rule — itself the B31 schema-key-drift / LD-0208 class), so ran the primitive directly
per the backstop instruction: read `org/projects/NFRA_DEBTSCAN.json` + `ls
org/modules/graph/debtscan/`. DEBTSCAN's dimensions are reachability (D1), composition
(D2/D2X), costrecon (D4), portalsweep (D5), canon-motif, and dups (`dup_scan.py`) — **every
one a reachability/composition/cost/dup scanner; NONE is a bug/logic-class miner.** The TO
`if_mismatch` (STOP + reconcile if DEBTSCAN already holds a bug-class artifact) does NOT
trigger. This catalog is a clean shared upstream. **Phase-2: PASS.**

## F1-F4 fabric-cluster partition — RECOMMENDATION routed to COO (the open AC2 item)
The Andrew-LOCKED boundary is frontend-detectable vs cross-domain (pipeline/data/infra). F1-F4
(marker-artifact-FP liveness, shared-resource contention, race-class, iteration-debt) are
agent-fabric RUNTIME-reliability classes — neither cleanly TS-graphable (not in the portal
graph P3-2 scans) nor classic estate-pipeline (DEBTSCAN's data/infra domain). **CVO
recommendation:** fold F1-F4 into the CROSS-DOMAIN partition as a tagged `fabric-runtime`
sub-cluster handed to DEBTSCAN (its scope is the "whole estate" incl. compositional risk, and
the signatures ARE graph-able — telemetry/broker/hook artifacts are estate nodes), BUT
explicitly flagged for DEBTSCAN-owner acceptance since they are runtime-not-pipeline. The 0
remaining-untagged-row AC2 bar is met under this recommendation (F1-F4 → cross-domain/
fabric-runtime), pending the COO ruling. Routed to COO 2026-06-26; not self-decided (scope
boundary is a COO/CTO call).

## Status after deep pass 2
- Frontend partition: A1-A11 (11 classes). Cross-domain: B1-B35 (35). Fabric-cluster: F1-F4 (4, partition-pending COO rule). **Total: 50 classes, all exemplar-anchored.**
- Deep pass 2 ADDED 12 classes (B24-B35 + A11) from the exhaustive 215-LD semantic mine + sharpened 5 existing rows to canonical LD exemplars.
- REMAINING for close: the 900 root-cause-SECTION semantic pass (LD mine done — the densest curated source is now exhausted; root-cause sections are the long tail, lower marginal yield, `[sharpen]` the remaining narration-only rows); per-class semantic frequency recompute; Phase-3 partition-completeness audit (0 untagged / 0 exemplar-less — A4/A5/B8/B9/B11-B14/B16-B18 still `[sharpen]`); the fabric-cluster (F1-F4) partition ruling owed by COO/CTO; then RAVC2 (COO + CC CTO + DEBTSCAN owner). Yields to #9 nightly per TO priority.

— 3.0.0_SA_CVO (WIP — through deep pass 2)
