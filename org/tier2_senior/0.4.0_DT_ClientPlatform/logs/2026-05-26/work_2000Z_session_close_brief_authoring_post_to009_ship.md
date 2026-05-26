# Session-close addendum — post-TO-009 ship brief authoring + ADVI_DEMOV1 project-CLOSED chain

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE
**date:** 2026-05-26
**worker:** 0.4.0_DT_ClientPlatform
**work-cycle:** 7-8 (post-TO-009 ship; brief v2 + DS~D handoff + KEEP-ACTIVE standby)
**Anchor:** companion to `work_1738Z_advi_demov1_009_portal_dev_prod_ship.md` (TO-009 ship log committed `9a0ea83fb`)
**Wall:** ~2.5h spawn-to-current (spawn ~15:54Z → final brief commit `74457d4e7` ~19:30Z → standby thereafter)

---

## Current state (session-close snapshot)

**KEEP-ACTIVE standby** post-TO-009 ship + ADVI_DEMOV1 project-CLOSED. Two follow-on waits:
1. **Wave-2 portal-tree-DEV-rule structural enforcement PRD** (~2-4h DT wall when ws CTO ships next session per capacity-flag) — my Phase 4 = 1st canonical Rule 19 conformant flow = empirical anchor for that PRD scoping
2. **ADVI_DEMOV1.010 follow-on PROD promotion** when DE 0.4 ships the F3 frontend patch (Black Diamond → Lone Pine Analytics label) — my judgment on fold-into-next-portal-tag vs standalone push

---

## What happened post-TO-009 ship (~17:38Z → ~19:30Z)

### Phase 2.5 — UAT-findings brief v1 → v2 (Andrew clarifications absorbed)

After TO-009 close commit `9a0ea83fb` landed, Andrew surfaced two corrections to my v1 brief (`ad37838b1`):

1. **"why would i need to log in as another user? it should be visible to all opal users like all other partners are"** — UAT-path correction. My v1 framing parroted PRD §6.1 wording about `demo@demo.test` Cognito login. Code audit (`AdvisorIntelligence/index.tsx:25,48`) confirmed `'demo'` is in `ALL_PARTNER_FIRMS` with internal-staff gating; Andrew's normal opal-capital account should see "Demo" in the dropdown.

2. **"NO COGNITO USAGE on Opal. We have NEVER used Cognito. We use dynamodb user table."** — architectural-fact correction. PRD §1 + §6.1 use Cognito language loosely; reality is `opalinvest-auth-handler` Lambda + `opal-users-v2` DynamoDB table. Banked new permanent memory `project_opal_auth_dynamodb_never_cognito` so this doesn't recur.

3. **"is the dev environment is stuck on PROD and not displaying DEV"** — strand-pattern diagnosis. Confirmed: main `portal/` tree pre-stranded on PROD `0be05530` from 0.3.0_DT's 2026-05-22 SSCN_TOOLBAR promotion (`feedback_portal_prod_promotion_strands_main_tree` 3rd-fire). Launched Vite dev server from existing DEV worktree `.runtmp/portal-dev-verify` on `:5175`. Andrew UAT then PASSed Smoke-A.

4. **Andrew UAT result + 3 backend findings + sovereign disposition:** *"all of that is backend issue, we can proceed with our frontend task orders and work on this subject unhindered."* Frontend UAT scope = PASS. F1 + F2 + F3 surfaced.

5. **F1 multiplier inversion (~17:42Z):** *"just incorporate some function to multiply all the numbers by 3"* — v1 said × 2/3 (per Andrew's earlier "cut down by 2/3" framing); v2 says × 3 (3.0× scale-up, makes demo headline larger than 49F).

6. **F2 spec refinement:** generate fake account strings `OPAL######` pattern. Andrew asked me to identify the Fee Summary data source — found at `FeeSummaryPanel.tsx:488` reading `.fee_summary.by_account[].account_id` from `s3://opal-data-demo/platinum/clients/{client_id}/summary.json`. Likely R1 JSON-path-aware-gap in `fake_identities.py` PII map.

7. **AE owner reroute:** v1 routed F1+F2 to `0.6.0_AE_PartnerETL`. Andrew asked which AE actually built the demo pipeline. Git-log audit of `data/demo/scripts/transform/` returned **`0.7.0_AE_CloudOps`** (infra/EC2/IAM via TO-001/.005/.007) + **`0.4.0_DS_ClientPlatform~C/~D`** (transform-code via TO-002/.004/.006). v1 routing was wrong; v2 corrected.

Brief v2 committed `595d2511f` on CLOUD. Routed to ws COO (FYI-CC to 0.6.0_AE for stand-down). AE 0.6.0 self-corrected next inbox cycle ("Disregarding the prior 'standing by' -- not waiting on a COO dispatch for me. Returning to standard standby.").

### Phase 4-coda — TO-009 close + project-CLOSED chain

- TO-009 close commit `9a0ea83fb` (TO status flip + ship_evidence + session log)
- ws COO RAVC2-ACCEPT Phase 4 absorbed all 5 ACs SAT
- ADVI_DEMOV1 project CLOSED 3-of-3 atomic `767c113ab` (JSON status complete + REGISTRY Active→Completed + PRD Status COMPLETE via CTO ANY_CTO lane)
- ws COO ACK absorbed brief v2 corrections fully (`~19:05Z`); routing re-dispatch to 0.7.0_AE_CloudOps + DS~C/~D queued
- F3 → ADVI_DEMOV1.010 GO'd to DE 0.4 same /drive #102 cycle (small 3-line patch + optional Cognito→DynamoDB wording fold-in)
- ADVI_DEMOV1 is 5th project CLOSED today (YALP_MKTOVR + ADHC_LEDGEH + ADHC_CDNCOHT + ADHC_COMPIL_V5 + ADVI_DEMOV1)
- My Phase 4 banked as 1st canonical CLAUDE.md Rule 19 conformant flow (shipped `c08f4287f` same day; ephemeral-worktree cherry-pick + main-tree-DEV-restore in same operation)

### Phase 4.5 — DS~D spawn-with-direction handoff (Andrew direct ask)

Andrew asked me to gauge whether DS~C/~D allocation was best use vs YALP work, then write a brief for DS~D he could ferry. Cost-benefit analysis returned:

- **F2 (account-# pseudonymization)** = strong case for DS~D spawn — extends ~D's own Path B + `seal_real_names()` infrastructure (TO-006); ~1-2h DS wall vs ~3-5h AE-solo with regression risk
- **F1 (numbers × 3 multiplier)** = weaker case; single-chokepoint multiplier AE 0.7 can write solo (snapshot-clean precedent `3cffa512b`)
- **YALP non-competition** — YALP is `0.1.0_DS_MarketIntelligence` lanes; DS 0.4.0 is ClientPlatform pod; different pods don't compete for capacity
- **Concurrency cap** 10/16 → +1 spawn → 11/16; cap not a constraint
- **Recommendation:** spawn only ~D (not both ~C and ~D); ~D more aligned with F2 specifically

Authored brief at `docs/briefs/advi-demov1-ds-tilded-spawn-direction-20260526.md` (commit `74457d4e7` on CLOUD). Brief contents:
- TL;DR + roles/responsibilities matrix (lane boundaries: DS owns `fake_identities.py` + `demo_transform.py` substance + `pii_leak_scan.py`; AE owns EC2/IAM/SSM dispatch; DT owns portal push; DE owns frontend)
- Project state context (9-TO chain shipped; CLOSED 767c113ab; F2 carry-open per LD-0030)
- F2 scope (Andrew verbatim + data-source trace + diagnosis + 5-step target spec)
- AC1-AC6 (machine-checkable)
- Investigation step (4 `jq` commands)
- Out-of-scope guardrails (don't touch F1/F3/EC2/IAM/portal)
- 5-channel coordination interfaces table
- Discipline carry-forward (Rule 14/14a/15, owned-paths, no-Cognito memory, spawn-with-direction template)
- 11-step startup sequence
- Full reference chain with commit SHAs (their own TO-006 + DS~C TO-002/.004 + AE 0.7 TO-007 + my TO-009 + COO close + my brief v2)

Brief ready for Andrew to ferry via `.tools\spawn-agent.ps1 0.4.0_DS_ClientPlatform~D` + first-message MCP citing the path.

---

## Inbox / MCP traffic this session-segment

| Time | From | Class | Action |
|---|---|---|---|
| ~17:38Z | (self) | Final RAVC2-Request | Sent to ws COO with all 5 ACs SAT + brief v2 corrections |
| ~18:30Z | ws COO | SENIOR_DISPATCH | ACK Phase 2 UAT + GO Phase 3+4 unhindered (based on v1 brief; v2 corrections in flight) |
| ~18:35Z | AE 0.6.0 | PEER_ASK | 2026-05-07 log loop-close + ACK FYI-CC; standing by for COO dispatch on F1/F2 (v1 framing) |
| ~18:36Z | (self) | FYI-LOOP-CLOSE | To AE 0.6.0 — routing-correction loop-close |
| ~18:40Z | AE 0.6.0 | UNBLOCK_RECEIVED (proxy) | Self-corrected from v2 brief; dropped standing-by posture |
| ~19:00Z | ws COO | SENIOR_DISPATCH | RAVC2-ACCEPT Phase 4 + ADVI_DEMOV1 CLOSED COMPLETE 3-of-3 atomic `767c113ab`; F3 TO-010 GO'd; F1+F2 reroute to AE 0.7 confirmed |
| ~19:05Z | ws COO | SENIOR_DISPATCH | ACK RAVC2-Request + brief v2 absorbed fully; Andrew clarifications + memory candidates banked |
| ~19:30Z | (self) | Handoff brief | Wrote + committed `74457d4e7` for DS~D ferrying |
| ~19:40Z+ | — | (no traffic) | Standby cycles |

---

## Compiler Tools (this session-segment)

| Tool | When | Outcome |
|---|---|---|
| `git log --all --author='0.4.0_DS_ClientPlatform~D'` | Pre-handoff-brief; cite-source recent surface for ~D | Confirmed ~D recent: TO-006 Phase 1-3 + Phase 2.1; last commit `7e9969a5d` 2026-05-24 |
| `git log --all --author='0.4.0_DS_ClientPlatform~C'` | Pre-handoff-brief; cite-source recent surface for ~C | Confirmed ~C recent: TO-004 13-attempt arc; last `469df551f` 2026-05-24 |
| `git log -- data/demo/scripts/transform/fake_identities.py` | Confirm ~D's last touch on F2's primary surface | ~D last touch was `7e9969a5d` (Phase 2.1); F2 extends from ~D's own work |
| `grep -nE '^- \*\*R[125]' docs/architecture/ADVI_DEMOV1.md` | Cite-source R1/R2/R5 in brief | Confirmed R1 (JSON-path-aware engine) + R2 (PII map reference) + R5 (mandatory leak scanner) intact |

No `comp-*` tools fired this session-segment (administrative-scribe + git-log forensics scope; no Lambda IAM / data-pipeline / portal schema-check changes).

---

## Memory state at session-close

**Banked this session (permanent):**
- `project_opal_auth_dynamodb_never_cognito` — written today after Andrew correction; load-bearing for any future agent reading ADVI_DEMOV1 PRD §1/§6.1 wording rot

**Surfaced this session (existing memories observed firing in practice):**
- `feedback_portal_prod_promotion_strands_main_tree` — 3rd-fire confirmed (per COO RAVC2-ACCEPT-PARTIAL); strand-impact-dimension expanded beyond next-promotion-blocking to UAT-blocking
- `feedback_track_inflight_to_by_artifact_not_sla` — Phase 1 audit-of-state resolved DE 0.4's "shipped via 6e6f013a8" framing into accurate "committed-locally-not-pushed" reality
- `feedback_git_fetch_before_deriving_deploy_head` — Phase 4 tag-baseline ground-truth (don't trust commit-message tag refs like the v2.1.98 fiction)
- `feedback_spawn_with_direction_fast_orient_pattern` — my own DT 0.4 spawn this session (~5min P1 ship; fast-lane regime); template used in DS~D handoff brief

**R&D candidates banked (for next /mstr-review or comp-tools brief):**
1. **bookkeeping-vs-ship-gap class** — TO status flip via separate commit without remote-push leaves downstream consumers reading wrong ground-truth (DE 0.4 TO-008 flip `6e6f013a8` vs portal-DEV-not-pushed reality)
2. **AC-wording-vs-deploy-model semantic gap** — PRDs/TOs reference "DEV CloudFront" when portal has single-CF; comp-routes / comp-platinum extension candidate
3. **strand-pattern impact-dimension expansion** — strand blocks UAT (not just next-promotion); structural-enforcement PRD next-session should capture multi-dimensional impact

---

## Closing posture

KEEP-ACTIVE standby. Two follow-on activation conditions:

1. **DE 0.4 ships F3 patch** (Black Diamond → Lone Pine label, 3-line frontend) → I do small PROD-promote (fold into next portal-tag bump OR standalone push per my judgment)
2. **DS~D spawned + F2 shipped → AE 0.7 EC2 re-dispatch + R5 PASS** → no DT work needed for that chain unless backend regression discovered

3. **Wave-2 portal-tree-DEV-rule structural enforcement PRD** (next session) → ~2-4h DT wall when ws CTO ships PRD; my Phase 4 ephemeral-worktree flow is the empirical anchor

/work cron continues at 20m cadence. Watcher tracked. Heartbeat current.

— 0.4.0_DT_ClientPlatform / archetype SCRIBE+COORDINATE
**work-cycle:7-8 (session-close addendum to work_1738Z TO-009 ship log)**
