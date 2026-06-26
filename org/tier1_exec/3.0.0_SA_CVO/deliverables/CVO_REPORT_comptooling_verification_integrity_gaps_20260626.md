# CVO Report to CTO — comp-tooling verification-integrity gaps (session-grounded + the 0.5.0 comp-iam defect)

**From:** 3.0.0_SA_CVO · **To:** 1.0.0_SA_CTO (comp-tooling owner) · **CC:** 2.0.0_SA_COO · **Date:** 2026-06-26
**Origin:** Andrew-direct ("assess what comp tooling would help... identify failure points"), wrapping the 2026-06-26 CVO session experience + 0.5.0_AE's comp-iam FALSE-MISSING report (`docs/briefs/comp-iam-false-missing-tf-resource-collision-20260626.md`, `e4866f07f`).

---

## The unifying theme (the CVO lens)

Every gap below is one failure shape: **a gate/verify tool that returns GREEN (or an authoritative-looking verdict) above its actual grounding.** That is the single most dangerous defect class for a verification fabric — a tool that *manufactures false confidence in a gate* is worse than no tool, because the discipline ("verify before deploy / before close") leans on it. Two directions:
- **FALSE-GREEN** — certifies a thing that isn't true (comp-iam mis-attribution; a detection layer that greens on an incomplete surface).
- **FALSE-CLEAR** — reads fresh/clean off a PROXY while the SYMPTOM is stale (comp-freshness on mtime vs `data_as_of`).

The cross-cutting fix is a **grounding contract**: every gate-tool verdict must (a) ground on the SYMPTOM not a proxy, and (b) carry an explicit *grounding-mode + vintage* signal (like `comp-kuzu`'s marker-oracle header) so a DESIRED-only or stale verdict can never be mistaken for live truth.

---

## P0 — comp-iam FALSE-GREEN / FALSE-MISSING (TF resource-name collision) [0.5.0's finding, amplified + extended]

**Mechanism (0.5.0, source-grounded + repro):** `extract_iam.py` `role_tf_to_name` keys roles by the BARE tf resource label, last-writer-wins, NOT namespaced by file/module. Two roots declaring `aws_iam_role "orchestrator"` → the later-scanned wins the key → the loser's inline statements `.extend()` onto the winner. Harms: (1) **FALSE-MISSING** on the loser (0 statements → a correct+applied grant reads "missing" — it misdirected the 06-26 astn outage diagnosis); (2) **FALSE-GREEN mis-attribution** on the winner (reads GRANTED for perms it doesn't hold — a gate certifying a permission that isn't there).

**My independent extension (comp-grep over `infra/aws/terraform`, 121 role decls):** the collision set is **WIDER than the 2 reported** — **5 duplicate bare labels**: `orchestrator`, `scheduler` (the astn pair 0.5.0 named), **plus `lambda_role`, `market_rsi_role`, `sfn_role`**. The last two are generic names likely duplicated across many roots → the mis-attribution blast radius is broader than the astn pair. CTO should assess each of the 5: do the colliding roles carry *divergent* inline policies (→ real FALSE-GREEN), or identical (→ benign)?

**Knowledge-parity gap (worth a doctrine note):** CLAUDE.md's comp-tool table credits `comp-iam` with "a TF-vs-live reconcile that catches a declared-but-unapplied control." But per 0.5.0's source-grounding, **`comp-iam service`/`gaps` NEVER read live AWS — they parse Terraform (DESIRED) only.** Agents (and the doc) have been treating a DESIRED-state parser as a live oracle. Either the reconcile capability lives in a *different* subcommand (the `comp-iam reconcile`/census I saw referenced — which is itself stale, see P2) or the doc overstates the tool. This needs reconciling, because "catches a declared-but-unapplied control" is precisely a live-vs-desired claim the parser can't make.

**Fix = CTO lane** (namespace the key by module; resolve role refs module-locally; collision guard that *errors* on a dup bare label; regression test). 0.5.0 offered to build it.

**Interim governance posture — I BLESS it (CVO):** until the fix lands, **any IAM-gated verification/cert grounds on LIVE `get-role-policy`, NOT comp-iam's DESIRED verdict.** Treat `comp-iam service/gaps` as DESIRED-state advisory, never a GRANTED/MISSING certification. (This session's cot firm-sep verdicts already satisfied this by accident-of-rigor — see self-check below.)

## P0 — comp-freshness is content-blind (mtime/`generated_at`, not `data_as_of`)

**What bit:** the cot served AUA (`s3://opal-data-cot/gold/artifacts/timeseries_chart.json`) had `generated_at=2026-06-26T13:46Z` but `data_as_of="2026-06-22"` — a gold re-run rewrote the file (fresh mtime) while the content stayed frozen, because the served artifact derives from holdings (separately frozen). 0.6.0 over-called the un-freeze off the mtime; the fabric nearly closed a freeze as resolved. When I reached for the tool, `comp-freshness script D_00b` returned **`NO_FRESHNESS_CONFIG — UNCHECKED, NOT a freshness pass`**, and its model is object-age class regardless.
**Recommend:** `comp-freshness content <served-artifact>` — parse the artifact's `data_as_of`/`as_of` field, compare to expected serving date, independent of mtime. Fabric-wide class (every served artifact derived from a pipeline). Would have caught this in one call.

## P1 — no detection-layer COVERAGE check (the A10 audit-scope-miss class)

**What bit:** I ACCEPTED-CVO'd the cot detection layer by verifying its 7 alarms *fire* — but not that the alarm *set covers the whole symptom surface*. Holdings/served-AUA was uncovered, so "alarms→OK" was a false all-clear. I checked mechanics, not completeness, and so did the CTO arch-accept.
**Recommend:** `comp-coverage <served-artifact>` (graph-native) — walk the served artifact's upstream lineage via the dependency graph and assert every freshness-relevant node has a watching alarm; print uncovered nodes. Would have printed "holdings: NO ALARM" at close-gate time. **DS graph-module lane** candidate (it's a graph traversal).

## P1 — no SM-secret freshness/mint tool (recurring firm-auth pattern)

**What bit:** verifying the cot reseed I rail-checked `describe-secret` for `LastChanged` + hand-rolled a box-side mint (`/datamining/auth/token` 200). `comp-freshness` is S3-only; `comp-iam` is policy-not-value-state. The BD durable-auth pattern (session cookies in SM, per-firm: 49f + cot + future) is now recurring and the reseed-verify is bespoke each time.
**Recommend:** `comp-freshness secret <id>` / `comp-secret` — `LastChanged` + optional liveness/mint probe for session-class secrets.

## P1 — no alert-path DELIVERY check (subscribed ≠ delivered, the B13 class)

**What bit:** to confirm the critical-surface rider actually reaches COO, I manually listed the SNS subs (confirmed SQS → `opal-critical-surface-alerts-coo`). The whole "fail-loud reaches COO" premise rests on this and is invisible to existing tools.
**Recommend:** `comp-routes alerts <topic>` — confirm alarm→SNS→SQS/email *delivers* (confirmed subs, not pending). Recurring for every critical-surface alarm.

## P2 — comp-iam census self-staleness

**What bit:** 0.6.0 noted comp-iam's reconcile census was stale (06-03) → fell back to live `get-role-policy`. A reconciler whose live-census is stale silently returns a stale reconcile.
**Recommend:** give the census the **marker-oracle freshness signal** `comp-kuzu` already has — flag `UNKNOWN VINTAGE`/`BEHIND`, never silently trust a stale census. (Ties to the P0 knowledge-parity gap — clarify what reads live vs desired.)

## P2 — fork-stale-shadow lint (the B8 class)

**What bit:** the cot box's `run-bd-auto-login.sh` carried a stale `APP_DIR=/opt/bd-49f-auto-login` — forked from 49f, never updated for cot. IAM firm-sep can't see a cross-firm *path literal* in a shell script; it just fails at runtime.
**Recommend:** a `comp-firmsep` lint that greps a firm's deploy artifacts for the *other* firm's path/bucket/secret literals.

## Reinforce (already chartered — NOT re-proposing): comp-which router (LD-0208)

`comp-which` dead-ended to the grep-dump backstop **twice** this session (the served-cot-AUA query; the DEBTSCAN-existence query). That's exactly LD-0208 (router covers ~8/36 tools). Flagging that it bit *live* AND that **Gate-1 now ENFORCES** (14:04Z) — a broken router behind an enforced gate funnels agents into grep-dumps, the precise risk LD-0208 named. Its priority went up today.

---

## CVO self-check — were THIS session's comp-iam verdicts compromised?

I rendered cot firm-sep verdicts (GREEN) to CTO off `comp-iam role` output. Independently grounded: my cot roles (`bd_cot_keepalive`, `bd_cot_freshness_probe`, `cot_exporter`) are **unique labels — not in the 5-key collision set** → no FALSE-MISSING/mis-attribution. And 0.6.0 cross-checked the same roles via live `get-role-policy` (Deny-bd intact, cot-only). **Two-source clean — the verdicts hold.** Note the lesson: the cross-check (comp-iam + live get-role-policy) is exactly the interim posture, and it's what makes me confident here — single-source comp-iam would not have been safe.

## Recommendation shape

Build all of the above is **CTO lane** (comp-tooling); the graph-native ones (`comp-coverage`) suit the **DS graph-module lane**. I recommend the builds, I do not author them (F5). Lead with the **two P0s** — the comp-iam collision (it can FALSE-GREEN a deploy gate *now*) and comp-freshness content-blindness (it nearly closed a freeze today). Both are the "GREEN above grounding" class; the grounding-contract pattern (symptom-not-proxy + explicit grounding/vintage signal) is the durable fix that generalizes past these specific tools.

## What you should have asked (unknown-unknowns)

**How many other comp-tools present a verdict more authoritative than their grounding — and which are wired into a GATE?** comp-iam (DESIRED-parsed, gates deploys) and comp-freshness (mtime-proxy, gates "is it fresh") are two we found by being bitten. The systematic question is a one-pass audit: for each comp-tool that emits a pass/fail/GREEN used in a gate, does its verdict ground on the symptom or a proxy, and does it advertise its grounding mode? The ones that gate something AND ground on a proxy AND don't advertise it are the latent FALSE-GREEN incidents waiting to happen. That audit is itself a high-value `comp-*` meta-check — and squarely the "Cases identify what new comp-tools agents need next" north-star.

— 3.0.0_SA_CVO
