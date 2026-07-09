# Session log — 0.7.0_AE_CloudOps — 2026-07-09 (1832Z–2040Z)
**archetype:** MIXED
**secondary_archetypes:** VALIDATE, IMPLEMENT, DIAGNOSE, COORDINATE

## Window summary

Launched onto an NFRA-first brief whose three named surfaces were all stale records. Grounding them
produced a security re-attestation, four fabric gates, a live client-facing finding, and four of my own
mechanism claims retracted.

1. **SCTY_PREMCP /otp — already built, deployed, live-healthy.** Brief + COO both said "ungated and
   unstaffed, build it." Deployed `app/otp.py` sha256 **== repo HEAD** byte-identical (so `0ccee9134`'s
   "Staged, NOT yet deployed" note was stale); ALB prio-30 forwards `/otp/{fetch,health}` with no OIDC;
   both firm bearers injected; EXERCISED `lambda invoke m365-otp-liveness` -> `{"ok": true, "status=200"}`.
   Nothing to build (`e23a9b965`).
2. **NO-BYPASS gate re-attested at the PERIMETER (CTO ruling 190127Z).** `/teams/poll` answers **302, not
   401** — no non-default ALB rule matches it, so it falls to the default rule, the only one carrying
   `authenticate-oidc`. The prior "3 REST bypasses" enum (0.7.0's + 0.8.0's "independent corroboration")
   was performed at the APP layer and never touched the ALB: **app-layer-true, perimeter-layer-wrong.**
   Fail-safe direction, not a vulnerability. Real bearer-gated-not-OIDC set = **16 paths** (`bfbf89ba7`).
   CTO adopted verbatim: *"two independent agents agreeing does not fix a shared blind spot when both look
   at the same layer."*
3. **F1 bearer-isolation — my reasoning REFUTED by CVO, retracted (`7ca2016e4`).** I claimed a random
   opaque bearer rejected by `/mcp` implies the real one is, "strictly stronger." False: the two differ in
   exactly the property a guard could key on (allowlist membership), so the probe had **zero power** against
   accidental static-bearer acceptance. Closed at SOURCE instead — `otp.check_bearer` has exactly 2 call
   sites (`server.py:446,486`, both `/otp/*`), `ms_ingest.check_bearer` 1 (`:507`), `_bearer_email` is
   RS256-only with no static branch, and the only other `compare_digest` is `oauth_as.py:224` (PKCE).
   CVO CERTIFIED on the enumeration. CTO **unbanked** the pattern he had taken from me as doctrine.
4. **CTO gate bundle — 4/4 shipped.** mass-deletion attribution gate; project-consistency lint;
   alarm-latch sweep; suppressed-error lint + the `safe-commit.sh:271` fix (pre-land GO).
5. **bd 49F client-facing AUA freeze — found, bounded, then RESOLVED read-only.** Escalated to Andrew by COO.
6. **LD-0262 / shared-worktree S2** — restored `logs/`, then stood down when MSTR revealed the deletion was
   Andrew-deliberate. My "the restore never landed" was an **inferred mechanism and wrong**.

## Deployment sequence + verification (DEPLOY additions)

| item | action | verification (APPLIED / EXERCISED truth) |
|---|---|---|
| `/otp` delivery | none (already live) | SSM `sha256sum /opt/m365-mcp-gateway/app/otp.py` == local HEAD; `OTP_BEARER` word-count=2; liveness invoke `{"ok":true,"detail":"status=200"}` |
| mass-deletion gate | `.git/hooks/commit-msg` installed | `--mode` -> `effective mode: warn`, flips 2026-07-11T19:30:00Z; 10/10 exercised (6 fire, 4 silence) |
| `safe-commit.sh:271` | patched, CTO pre-land GO 202938Z | 4/4 exercised; **the patched wrapper committed itself** (`8d1dca813`) |
| `cmtque-worker-down` | exercise only, **no config change** | actions disabled -> forced OK -> **re-latched ALARM in ~120s** -> actions re-enabled. Zero drift (TF declares no `actions_enabled`). |
| leg-4 L4 | **NOT closed** | marker `warehouse/_branch_head.main.json`: `writer_id=incremental_updater`, `committed_at=16:13:16Z` (post-L3-apply), all 3 tables non-null `last_write_iso`. `proof_required` MET; target also needs `derive_runner` -> pends ~02:10Z nightly. Watcher armed (`brufqfd5t`), escalates on 6h timeout. |

## Findings issued

| finding | grounding | disposition |
|---|---|---|
| `/teams/poll` OIDC-gated at perimeter, not bearer-gated | live `elbv2 describe-rules` | FILED; CTO amended the NO-BYPASS gate to a standing perimeter re-attestation |
| `github-token-6FYoJ6` is an **ARN suffix, not a secret name** | live `describe-secret` (real name `github-token`, exists); body must be JSON `{"token":...}` (`freshness_alarm:218-219`) | Andrew provisioning off it; a `create-secret` would have minted a decoy |
| leg-5-v2 parity alarms latched ~23h, detector blind since deploy | `describe-alarms` + λ logs (401) | raised PAT priority |
| **bd 49F `total.aua` FROZEN** at $1,837,159,865.68 across 8 writes / **3 advancing vintages** | S3 `list_object_versions` as a time series | COO re-derived independently -> **escalated to Andrew as ESTABLISHED** |
| 5 `bd-served-vintage-stale-*` alarms latched 67h — **watching vintage, not value** | `f38e59759` sweep | CVO took it; CTO source-confirmed mechanism (holdings `nzf=0.0000`, `cot_bronze_ingest.py:730-735` floor-reject) |
| `opal-infrastructure-alerts` has **one SMS subscriber, no durable limb** | `list-subscriptions-by-topic` | FILED |
| 2 CloudFront alarms `INSUFFICIENT_DATA` **186 days** | sweep | FILED |
| 18 projects terminal-status but still in REGISTRY Active (12 are NFRA) | `2bcb4b17e` | list -> COO; reconciles CTO's hand-count of 17 (delta = `MKOV_DLYCLD`, status `merged`) |

## Compiler Tools

| tool | use | result |
|---|---|---|
| `comp-which` | routed "where is the gateway source / teams-poll" | PARTIAL — near-tie (comp-routes/comp-cluster), **neither fits** (gateway is EC2+ALB, not CloudFront); fell through to on-rails `comp-glob`/`comp-grep` as designed |
| `comp-grep` / `comp-glob` | gateway `app/*.py`; `/otp` call-sites; `github-token-6FYoJ6` consumers; `stamp_marker`; `cmtque-worker-down` TF | PASS — the `freshness_alarm.tf` ARN hit is what decoded the suffix-vs-name confusion |
| `commit-gate.sh` | every `.py`/`.sh` edit (4 new tools, 2 gateway comment fixes) | PASS all |
| `safe-commit.sh` | 10 commits, all pathspec-scoped | PASS — and **surfaced its own `:271` bug** three times under MSTR's index contention |
| `comp-freshness` | bd platinum served freshness | PARTIAL — usage only; superseded by direct `list_object_versions` |

**What worked:** making invariants *printable* — `--mode` on the gate and `metric_shape()` in the sweep each
caught a bug I had reasoned past. **Gap found (routed to CTO, approved):** `comp-which` has **no route for
"what is the live ALB/perimeter shape of this host?"** `comp-routes` models CloudFront->origin; nothing models
ALB-listener-rule -> `authenticate-oidc`-vs-`forward`. The `/teams/poll` drift was found by a curl that happened
to return 302 — **and a curl that happens to work is not a control.**

## My own errors, corrected in-window (all four came from printing, never from thinking harder)

1. **"Strictly stronger" negative control** — refuted by CVO; retracted `7ca2016e4`; CTO unbanked it.
2. **Wrong `BLOCK_AFTER_EPOCH`** — shipped the gate LIVE-BLOCKING against CTO's WARN ramp for 7 min while it
   printed "WARN". Root cause: **I tested the override and never the default.** Fixed `61bf89ed1`; added a
   `--mode` self-check *because* the default was otherwise unassertable.
3. **"Parity alarms latch on missing-data=breaching"** — FALSE. `freshness_alarm:159-166` publishes
   `Value=1e6` ("UNVERIFIABLE reads as maximally-stuck — fail LOUD"). The author's design is better than the
   accident I ascribed to it. My own sweep caught it -> produced rule **L4 PINNED**, which CTO folded into his
   latched-alarm ruling.
4. **"MSTR's restore never landed"** — grounded symptom (932 files missing), **invented mechanism**. The restore
   landed at 18:11Z; Andrew then ruled the purge deliberate and MSTR re-applied it. I read the intended
   post-cleanup state as a failed restore. Same Rule-22 error I spent the session naming in others.

Also: my first `served-value-freeze-check` rule was falsified by its **positive control** (it printed
`OK: varies` on the known-frozen artifact), and my first *negative* control was drawn from inside the incident,
so it could not fail. Both replaced.

## Blockers

None. `cmtque-worker-down` durable fix is **arch-gate-held with CTO** (option (b) `count = var.cmtque_enabled`
DESTROYS a critical-surface alarm; I do not destroy on my own authority). COO's notification-exercise bar is
**authorization-held** — completing it texts a live human phone. Neither is a blocker on leg-4.

## Current State (handoff — zero prior context)

- **leg-4 `freshguard-leg4-writer-wiring-finish`: OPEN, L4 pending.** `proof_required` already met by
  `incremental_updater` (marker 16:13:16Z, 3/3 tables non-null). Remaining: `derive_runner` stamps at the
  ~02:10Z nightly. Background watcher `brufqfd5t` fires on `writer_id == derive_runner`, escalates on 6h timeout.
  **EDGES P3 sequences after (Opt-2, one-image-ledger-at-a-time).**
- **bd 49F AUA frozen**, client-facing, escalated to Andrew. Tonight's 02:00Z bd run is the un-freeze attempt.
  Verify with `python .tools/served-value-freeze-check.py s3://opal-data-bd/platinum/firm/header_metrics.json
  --field total.aua --versions 9` — **a trailing constant run collapsing to 1 vintage IS the un-freeze landing.**
- **Gates live:** `.git/hooks/commit-msg` mass-deletion gate in **WARN** until 2026-07-11T19:30:00Z, then BLOCKS.
  Attribute with an `Authorized-Deletion: LD-####` trailer; bypass `FORCE_DELETE=1` (audited to
  `org/mass-deletion-audit.log`). **Standing: no bare `git commit`, no `git commit -a`** while the shared index carries deletions.
- **STOOD DOWN, untouched since:** `logs/`, `infra/aws/`, `.smart-lint-backup/` (MSTR owns). Fences honored:
  no CloudTrail data-event widening; `03_mappings/` untouched; no `git add -A`.
- **Commit messages: use `-F <file>`.** Backticks in a double-quoted `-m` are command substitution and execute
  with agent credentials — hit live this window.

## Next Steps

| # | item | gate |
|---|---|---|
| 1 | **[0.7.0_AE_CloudOps]** close leg-4 L4 + ledger on the `derive_runner` stamp | ~02:10Z nightly (watcher armed) |
| 2 | **[0.7.0_AE_CloudOps]** EDGES P3 materialize + deploy | after #1 (Opt-2) |
| 3 | **[1.0.0_SA_CTO]** arch-gate `cmtque_enabled` count-gate (destroys an alarm) | CTO GO |
| 4 | **[2.0.0_SA_COO]** authorize a test SMS, or a scratch-topic delivery exercise | COO/Andrew |
| 5 | **[2.0.0_SA_COO]** move 18 REGISTRY rows Active -> Completed (row half of the 2-step close) | COO lane |
| 6 | **[0.8.0_AE_CloudComp]** NFRA_GRAPHS AC2: wire the freshness contract on `comp-build` + `comp-aws derive` | accepted; CTO arch-gates the 4-state contract |
| 7 | **[1.0.0_SA_CTO / COO]** build `comp-routes perimeter` (reach, not rules) | CTO approved, needs lane |
| 8 | **[0.6.0 / DS]** bd `total.aua` producer: what input has been unchanged since 07-06T21:26Z | CTO source-confirmed the floor-reject; un-freeze rides 02:00Z |
