# 0.4.0_DT Session Log — frontend-dev Harness Replacement

**Agent:** 0.4.0_DT_ClientPlatform
**Date:** 2026-04-14 (ET)
**Task Orders:** none (infrastructure work prompted by peer DE request blocked on `/frontend-dev`)
**Briefing:** `docs/briefs/frontend-dev-harness-bugs.md`

---

## Trigger

DE 0.4.0_DE_ClientPlatform requested `/frontend-dev` rapid-toggle validation on portal commit `e200193` (ADVI_FNTEND.D7 warm-import fix). Attempting to invoke `/frontend-dev` revealed the command is not a registered slash command in any session. Investigation pivoted from "run the test" to "make the test runnable for all agents going forward."

Andrew directed: build the replacement, provision a dedicated harness account.

---

## Action Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Startup: check-inbox + comp-graph context | Clean; ctx set to `SERIAL=0.4.0_DT_ClientPlatform, TO_ID=(none)` |
| 2 | ACK COO STANDBY for ADVI_FNTEND wave | Delivered 20260414T212021Z |
| 3 | ACK DE D7 rapid-toggle request | Delivered 20260414T221244Z; FYI to COO |
| 4 | Push portal DEV (7 commits incl. e200193) | `8d48a2a..e200193` -> origin/DEV |
| 5 | Diagnose `/frontend-dev` invocation path | Plugin not in `installed_plugins.json` / `enabledPlugins`; required subagents don't exist; org/XXX.md bans Task tool — fundamental conflict |
| 6 | Design replacement: Skill + constitution-driven CLI | Avoids Task subagent dep; uses Skill tool available to all agents |
| 7 | Build `.tools/frontend-dev.py` + wrapper | Playwright runner with auth, rapid_cycle, assert_not_blank, ACTIONABLE_FIXES JSON emit |
| 8 | Write `.claude/skills/frontend-dev/SKILL.md` | Closed-loop protocol: run → parse → Edit fixes → re-run, max 5 iterations |
| 9 | Write `portal/.frontend-dev/testing/README.md` | Constitution schema + step action reference + authoring checklist |
| 10 | Write `portal/.frontend-dev/testing/distribution_tab_rapid_toggle.json` | First real constitution: 10x GEO/ADV/OFC + 10x Snapshot/Continuous |
| 11 | Update `org/XXX.md` visual-testing section | Replaces `/frontend-dev` plugin refs with Skill invocation |
| 12 | Update `~/.claude/plugins/frontend-dev/hooks/auto_visual_test.py` reminder | Now points at Skill |
| 13 | First harness run → fail at login (401) | Same failure mode as pre-existing `smoke-test.py` — cred issue, not harness bug |
| 14 | Inspect `opal-users-v2` DynamoDB schema + Andrew's PROFILE record | PK/SK=USER#<id>/PROFILE; bcrypt $2a$12 password; role=admin userType=Dev tier=internal firmId=opal-capital |
| 15 | Provision `michael@opalinvest.com` | `put-item` with bcrypt hash of `l85a1q1p06677!`, same attrs as Andrew (PK=USER#usr_7aa8bf335ca5) |
| 16 | Swap constitution creds to Michael | email/password updated |
| 17 | Run harness — login OK, nav failed | URL pushed to `/advisor-intelligence` bounced to `/market`; App.tsx:449 catch-all `*` route race with pushState |
| 18 | Switch constitution setup from `nav` action to `a[href='/advisor-intelligence']` click | React Router owns the NavLink click handler — deterministic |
| 19 | Re-run `rapid-cohort-toggle` | **PASS** — 30 toggles, 0 blanks, 0 console errors |
| 20 | Re-run `viewstyle-toggle` | **PASS** — 20 toggles, 0 blanks, 0 console errors |
| 21 | Write bug briefing `docs/briefs/frontend-dev-harness-bugs.md` | 4 defects documented, 5 action items, 2 pending Andrew decisions |

---

## Bugs Found (Detail in Briefing)

| ID | Bug | Severity | Status |
|----|-----|----------|--------|
| B1 | `/frontend-dev` plugin never registered (meta) | Blocking | Resolved — replaced with Skill+CLI |
| B2 | `button:has-text("ADV")` matches "ADVISORS" top tab | Blocking | Fixed — use role+name+exact |
| B3 | pushState `/advisor-intelligence` races catch-all `*` route, bounces to `/market` | Blocking for harness | Worked around via NavLink click; root cause open for portal routing owner |
| B4 | Legacy creds `andrew@opalinvest.com` / `SmokeTest2026!` return 401 | Blocking | Resolved — Michael harness account provisioned |

---

## Files Created / Modified

**Workspace (parent repo, branch CLOUD, uncommitted):**
- `.tools/frontend-dev.py` (NEW) — 470 lines, constitution-driven Playwright CLI
- `.tools/frontend-dev` (NEW) — bash wrapper
- `.claude/skills/frontend-dev/SKILL.md` (NEW) — closed-loop protocol
- `portal/.frontend-dev/testing/README.md` (NEW) — constitution schema + authoring guide
- `portal/.frontend-dev/testing/distribution_tab_rapid_toggle.json` (NEW) — first real constitution
- `org/XXX.md` — Visual Testing section rewritten
- `docs/briefs/frontend-dev-harness-bugs.md` (NEW) — engineering briefing
- `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-04-14/frontend_dev_harness_build.md` (this file)

**User-level (not in repo):**
- `~/.claude/plugins/frontend-dev/hooks/auto_visual_test.py` — reminder text points at Skill

**AWS (irreversible write):**
- `opal-users-v2` DynamoDB: new item `PK=USER#usr_7aa8bf335ca5, SK=PROFILE` (michael@opalinvest.com)

---

## Harness Verification Results

**Constitution:** `portal/.frontend-dev/testing/distribution_tab_rapid_toggle.json`

| Scenario | Toggles | Blanks | Console Errors | Screenshots | Status |
|----------|---------|--------|----------------|-------------|--------|
| `rapid-cohort-toggle` | 10 × 3 = 30 | 0 | 0 | 4 | **PASS** |
| `viewstyle-toggle` | 10 × 2 = 20 | 0 | 0 | 3 | **PASS** |

Artifacts: `.frontend-dev-results/20260414T230455Z/` and `.frontend-dev-results/20260414T230531Z/`

**ADVI_FNTEND.D7 warm-import fix (portal commit `e200193`): validated.** Zero blank-chart flashes across 50 rapid cohort/viewStyle toggle events on DistributionTab.

---

## Compiler Tools

| Phase | Tool | Command | Result | Note |
|-------|------|---------|--------|------|
| — | — | — | — | Harness build is not a pipeline change — no comp-pipescript / comp-transform runs applicable. Tooling lives under `.tools/` and `.claude/skills/`, outside the graph. |
| Before portal push | comp-transform schema-check | (deferred to next portal edit session) | N/A | No `portal/src/**` component touched in this session — the 7 pushed commits were authored by DE+RD in prior sessions and already passed schema-check at their commit time. |
| Before ADVI_FNTEND batch PROD push | — | — | — | Not applicable — this session did DEV push only. PROD GO still pending from COO per STANDBY directive. |

Structural note: the frontend-dev harness itself will cause future compiler-tools runs to increase, since any agent invoking the Skill will emit Playwright-driven evidence alongside the usual comp-transform + comp-blast runs at commit time.

---

## Current State

- DE D7 rapid-toggle request: validated PASS. DE can flip D7 to `complete`.
- Harness is built, tested end-to-end, and documented. Ready for all-agent use.
- Portal DEV at `e200193` (origin/DEV up to date). Portal PROD still at `a30c403` from earlier session (portal-v2.1.42). Pending DE W6 OFC L1 + RD ADV donut subtext items are on DEV but not merged to PROD — awaiting Andrew's PROD GO (separate from this session's work).
- Parent repo CLOUD has **uncommitted** changes: the 8 harness files listed above. Holding commit pending Andrew's credential-handling decision (see Open Decisions).

## Open Decisions (Pending Andrew)

1. **Credential storage** — Michael's password currently sits in plain text in `distribution_tab_rapid_toggle.json`. Committing that file puts credentials in git history. Options: env var, Secrets Manager lookup at CLI start, accept-and-commit (admin+Dev account, local-dev-only). Default: env var, but not changed without explicit ack.
2. **Michael's role scope** — provisioned admin+Dev for parity with Andrew. Tighter scope (viewer+Internal) would reduce blast radius if the harness is ever pointed at a non-local env. Not changing until we confirm every harness scenario works under a narrower scope.

## Next Steps

- [Andrew] Decide on credential handling (#1) and role scope (#2) above
- [0.4.0_DT] After Andrew's decision: swap creds if needed, then commit harness files on CLOUD with selective `--only` pathspec
- [0.4.0_DT] Signal DE: D7 validated PASS, flip to complete
- [0.4.0_DE] Next session: author a second constitution (AdvisorBookView drill, or any other component with a visual acceptance criterion) to prove the schema generalizes beyond one test
- [1.0.0_SA_CTO] Review B3 (pushState→catchall race in `App.tsx:449`) — low-priority portal routing question raised in the briefing
- [2.0.0_SA_COO] FYI — harness replacement is ready; agents should now invoke the Skill `frontend-dev`, not the dead plugin command. Consider a broadcast to all DE/DT/RD agents next session

---

— 0.4.0_DT_ClientPlatform
