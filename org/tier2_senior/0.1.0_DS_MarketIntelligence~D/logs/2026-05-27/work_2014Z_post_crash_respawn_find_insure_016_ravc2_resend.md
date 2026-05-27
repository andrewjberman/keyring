# Post-crash respawn + FIND_INSURE.016 RAVC2-Request resend — 0.1.0_DS_MarketIntelligence~D

**Trigger:** MSTR direct ~2010Z respawn per Andrew direct (PowerShell crash window swept ~D session away)
**Author:** 0.1.0_DS_MarketIntelligence~D
**Timestamp:** 2026-05-27T~20:14Z
**Wall:** ~5min orient + RAVC2-Request resend (single-action recovery cycle)

---

## §1 — Crash diagnosis

Prior session (FIND_INSURE.016 Phase 2B job-board survey worker) crashed between commit + RAVC2-Request MCP. Evidence:

- Last `~D` commit: `15778ecad` 2026-05-27T19:45:38Z = `survey(0.1.0_DS_MarketIntelligence~D): FIND_INSURE.016 Phase 2B job-board public-API survey v0.1`
- Last MCP from `0.1.0_DS_MarketIntelligence~D` to ws COO (inspected `org/mcp/inbox/2.0.0_SA_COO/read/`): GO-ACK at `20260527T193939Z` (19:39Z) — no RAVC2-Request entry from `~D` for FIND_INSURE.016
- Gap: ship landed 19:45Z, RAVC2-Request never fired, crash followed before send
- TO `org/tier2_senior/0.1.0_DS_MarketIntelligence/task_orders/FIND_INSURE.016.dsd-job-board-public-api-survey.md` still `<status>active</status>`

## §2 — Recovery cycle actions (this session)

1. `/watcher` Step 1-6: registered LIVE on opal-agent-comms broker (PID 34148); launched tracked inbox-watch task `bg3mjqz0m` (was VERDICT=NONE pre-launch, no kill needed); inbox empty both paths.
2. Read `session_pre_reboot_snapshot.md` (1455Z) — confirmed pre-crash standing posture was KEEP-EPHEMERAL pending CMASMP/POSITN close OR next dispatch; both completed cleanly by COO. So ~D was idle when FIND_INSURE.016 dispatch landed ~1931Z from COO.
3. Read FIND_INSURE.016 TO + confirmed shipped brief `docs/briefs/find-insure-phase2b-job-board-public-api-survey-v0.1.md` exists.
4. **Sent RAVC2-Request to ws COO** (the missing MCP): MCP `20260527T202403Z_0.1.0_DS_MarketIntelligence_D__RAVC2-Request__FIND_INSURE.016_Phase_2B.md`. CC trio per TO line 69: 1.0.0_SA_CTO + 0.1.0_DS_MarketIntelligence~C + 0.7.0_AE_CloudOps~B.
5. Armed `/work` cron `2033bf57` firing @ :03/:23/:43 every hour (session-only).

## §3 — FIND_INSURE.016 ship recap (re-stated for log-of-record)

`15778ecad` survey(~D): Phase 2B 6-board public-API survey v0.1 covering LinkedIn / Indeed / Glassdoor / ZipRecruiter / Monster / SimplyHired. 5-of-5 ACs self-attested PASS per TO. Wave-1 ship-priority recommendation = LinkedIn + Indeed (HAR-HIGH); aggregate cost estimate ~$10-12 per 99-IMO scan via Bα + Bβ mix; sister-coord §5 scopes 4 shared-utility parity points to DS~C's `lusha_client.py` (`79d202af0`).

## §4 — Standing posture post-cycle

- **KEEP-EPHEMERAL** pending ws COO RAVC2-Accept verdict on FIND_INSURE.016 v0.1 OR next dispatch
- `/work` cron `2033bf57` armed; next tick @ :23 or :43 local will run /work body (inline /watcher folds per LD-0082)
- No uncommitted ~D work in tree
- Watcher tracked task `bg3mjqz0m`; registration LIVE

## §5 — Lessons-learned candidate (not memory-banked; offered for pattern-recognition)

**Crash-window MCP gap** — the discipline "ship → RAVC2-Request as paired atomic" is real cultural-only; under PowerShell crash the gap manifests as commit-landed-but-RAVC2-never-sent. Recovery cost was ~5min once respawn fired. Detection cost = grep COO inbox for D-from-self entries against own commit log. If this happens frequently enough across the fabric, candidate for a structural fix (e.g., a post-commit hook that drafts a RAVC2-Request template to MCP outbox before allowing /work loop to advance). Not raising as memory now — single empirical; bank if it recurs.

---

ACK on /work cron arming; next tick proceeds normally.

— 0.1.0_DS_MarketIntelligence~D
2026-05-27T~20:14Z
