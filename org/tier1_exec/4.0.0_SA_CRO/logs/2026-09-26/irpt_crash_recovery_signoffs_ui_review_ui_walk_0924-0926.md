# IRPT 09-24 to 09-26: crash recovery, the PFOE and gateway fixes, 20 sign-off halves, the 50-finding UI review, and /ui-walk -- 4.0.0_SA_CRO

**archetype:** MIXED
**secondary_archetypes:** TRACE, VALIDATE, SCRIBE, IMPLEMENT
**Date:** 2026-09-24 to 2026-09-26 (window: after `a2841a953f`, the 09-24 04:49Z log, to 2026-09-26 22:3xZ)
**Task Order:** ad-hoc (Andrew-direct at the 4.0.0_SA_CRO terminal throughout)
**Status:** COMPLETE for every act asked. Standing obligations are under Next Steps.

---

## Objective

Recover the fabric after the 09-24 crash. Then carry Andrew's direct asks to closure:
- the IRPT return to the canonical flow;
- the DSGN_IRPTV1 UI-finish brief;
- Lauren Harmon's PFOE trade submission;
- the Teams gateway image gap;
- the Investor Reporting frontend traces and route structure;
- the S147 speed fork;
- the 50-finding UI review register;
- a dormant UI-walker service account with the /ui-walk skill.

Serve as the second half on every never-widen act routed to this seat.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find (via the native Grep/Glob tools) | code and record searches across portal/, infra/, org/ | PASS | Native Grep/Glob were the default. Two raw Bash greps were denied by the rail hook and re-run through the native tools. |
| graph / comp-surface | -- | SKIPPED | This seat made no cloud, infra or data change. The one world write (the ui-walker row in `opal-users-v2`) is a single table row, not a graph node. |

**What worked:** the rail denial rerouted two recursive greps correctly. Direct HAR parsing (python over the 350-entry walk HAR) answered every frontend question faster than a code census.
**What failed:** none of the comp tools failed. Two shell heredocs broke on quoting and were rewritten with the Write tool.
**Gap found:** no comp tool answers "which entities does this page's API call return, at what grain". That took HAR parsing.

---

## Work Completed

### 1. Pre-crash session commits, recorded here because that session never logged them (09-24 04:57Z-12:22Z)
From commit subjects only; this seat has no working context for them:
- `9cf6a63d6f` and `e1476853c9`: the B7 speed option B (boundary keep-warm).
- `d8abd7dc65`, `2ee8926519`, `c7126b5142`, `9a9138d4ab`, `b74eb87e67`: the /closer traces (Performance and Analysis, with addenda).
- DSGN_IRPTV1 PRD L4-R brief halves: v0.3 REFUSED `fc5378db02` / `7f58e337b0`; v0.4 SIGNED `7112a0a59b` / `159b019d9b`; v0.5 SIGNED `6d9077a944` / `cbd50ce98f`.

### 2. Crash recovery and the IRPT return (09-24)
- The crash recovery brief `6f8eefcfe7`, adopted by the CTO.
- The IRPT closer-to-canonical return brief, v1 to v2.1: `c3f04daf4d`, `f4704110cc`, `262cad6741`, `c45fb31429`. Andrew's five answers are recorded @`262cad6741`.

### 3. The DSGN_IRPTV1 UI-finish brief (09-24)
`20f90739bd`: 11 outcomes, calls C1-C3. It became PRD v0.8, and round 3 was issued from it.

### 4. The PFOE trade submission (09-25)
- **Autosave 500:** a missing autosave key plus no ListBucket gave AccessDenied, which became a 500. Routed to the CTO
  (`a6834b314b`), fixed by the CTO @`789dc46e5c`, verified here in the function log.
- **Trade Submission's new Vident path:** routed (`1c8bce6f79`), built by the CTO, released to PROD on Andrew's word.
- **Result:** read here by `get-item`: `TRADE-20260925-183318-731E1A` PENDING_APPROVAL (`c3b37bd549`). The blank
  identifiers were confirmed intentional by Andrew (`00dbc00cc6`).

### 5. The Teams gateway image gap (09-25 to 09-26)
- No new Graph entitlement is needed. Two code gaps were routed to the CTO (`fcd327ecdd`) and are live at gateway
  `0af72fb1d0`.
- The chat read was verified at top=25. The `read_chat_message_images` live test ran after Andrew's /mcp reconnect: 1
  of 1 image for each of 2 messages, 64,125 and 43,220 bytes (`64ea37320e`).

### 6. Never-widen second halves signed or refused by this seat (09-26)
- Walk principal (Opal-class) fe8e8d89 `909dd40acc`.
- Admin+Dev walk packet:
  - v1 REFUSED `f8fa80bddc` (the method-graded audit fired on a correct walk);
  - v3 `a157c45762`, v5 `80b1a711f3`, v7 `36b060964b`, v8 `243bf8a1e3`;
  - v9 `8840cf8762`, then K7 VOID `248d3d9057` (a wrong 0.06854 baseline);
  - v10 `bc1481a8be`.
- Export deploy B: v1 `f8fc5ff21d` (plus the three-firm arm), `2c716304dc` (arm narrowed), v2 `c1ad65cbcd`. R1 was
  re-read at full precision and the baseline corrected: `6fb82db891`, 183 of 183 shared points identical.
- Own-mask labels `c412578ede`.
- Reopen authz `219f9450da`.
- S147 fix M `4eacc1283f`.
- Window 5 `0571ef3cd2`.
- UIR-07 v2 and ETF tags `07525238da`.

Each deletion of a walk principal was read gone here: users 0 of 79, with a positive control of 1.

### 7. Frontend traces and route structure (09-26)
- /closer trace x3 plus the proposal `889160ce2c` (from the 350-entry PROD walk HAR). It was adopted as PRD v0.9
  ROUTE STRUCTURE.
- The label correction `713a49f7b8`: labels repeat within a client, 1 distinct of 2 and 1 of 3. PRD v0.12 re-pinned C25
  to it.

### 8. The S147 design-fork card `aa16886778`
B is allowed only as PLATINUM rebuilt from gold (past twr_daily partitions carry 4 versions). C is not taken (R11). The
CTO adopted it as R9. The timings later showed the engine read is 4.0 of 26.7 s, so B is held and fix M shipped.

### 9. Andrew's UI review register (09-26)
- `fd463341e3`: 49 findings, a brief and the coverage check.
- UIR-50 (ETF Classifier precedence) `4a17009de0`, corrected `83124e6de2`.
- PRD v0.14 @`c236788365` reads 50 of 50 on the check.

### 10. /ui-walk and the dormant UI walker service account (09-26), Andrew-direct "just build it"
- `447daa112d`: `opal-users-v2` `USER#usr_opal_ui_walker`, disabled at rest, armed and disarmed per walk.
- Exercised 3 times live on localhost:5174. Each disarm read a refused login (HTTP 401).
- The walks reproduced UIR-02: the tab strip's button covers the open search listbox. They also measured UIR-07 in
  Global mode as #17 of 17.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| The UI walker account is DORMANT at rest (disabled, no usable hash, no SSM parameter), not a standing login | Superadmin reach exists only during a walk. That is safer than the MFA-bound test login whose password sits in git. |
| Refused the admin+Dev v1 packet | Its "0 non-GET" audit fires on the page's own POST resolve and POST selections, so it could not tell a correct walk from a wrong one. |
| Signed export B only with a three-firm human-read arm | D1 changed members that human reads hit, and the packet read one firm against a recalled value. |
| Voided v9's K7 | The 0.06854 baseline was K6's 09-24 point, not its YTD, so a correct read would have rolled back a working deploy. |
| The UIR-07 condition: the Global-mode arm | Andrew reported the case in Global. The packet's arm was single-firm. |
| The ETF condition: a ticker-to-CUSIP identity census before B2 | The CASH ticker named both Pathward stock and a synthetic cash row. |

---

## Files Modified

See the commit messages: 53 of this seat's commits in the window, 39 of 53 on `origin/CLOUD` `7f2e82d758` (fetch +
merge-base read at 22:3xZ). Rows needing extra context:

| File | Change | Committed |
|------|--------|-----------|
| `.claude/skills/ui-walk/{SKILL.md,ui_walker_account.py,walk.mjs}` | The new skill, the account tool and the walker | Yes -- `447daa112d` |
| `docs/briefs/irpt-ui-review-{brief,findings}-20260926.*`, `irpt-ui-review-coverage-check.py` | The 50-finding register, the brief and the check (now `--register`) | Yes -- `fd463341e3`, `4a17009de0`, `83124e6de2`, `447daa112d` |
| `org/tier1_exec/4.0.0_SA_CRO/handoffs/2026-09-26_1857Z.md` | The seat handoff | Yes -- `717466680b`, `64ea37320e` |
| `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` | Row IRPT_BCKEND-S145 (a 49F client at $0.00 READY) | Yes -- `bc1f221579` |
| `opal-users-v2` `USER#usr_opal_ui_walker` (AWS) | Provisioned disabled, 21:5xZ | n/a (world); status read disabled after every walk |

---

## Blockers

None at this seat. Every owed item waits on another seat's packet (Next Steps).

---

## Current State

This seat owes second halves on:
- (a) the R4 scheduled Holdings publication enable (2.0.0_SA_COO~M, Monday 2026-09-28 re-run). Hold it to the pinned
  per-class diff, the INF name digit/email census, and the classification-table re-read;
- (b) the ETF Part B B2 writes, after the ticker-to-CUSIP census it asked for;
- (c) COO~M's COT cash-line fix;
- (d) any new walk window.

The standing account `opal-ui-walker@opal.test` reads `status=disabled`, SSM ABSENT
(`python .claude/skills/ui-walk/ui_walker_account.py status`). Walk outputs are in the gitignored
`tmp/ui-walk/20260926T2*`.

DSGN_IRPTV1 PRD v0.14 @`c236788365` carries all 50 UIR ids, the ROUTE STRUCTURE (C25 @`713a49f7b8`), and FWD-19 to
FWD-23. The handoff file `org/tier1_exec/4.0.0_SA_CRO/handoffs/2026-09-26_1857Z.md` holds each owed half's conditions.

---

## Next Steps

1. **Sign or refuse the R4 enable half** on arrival [2.0.0_SA_COO~M], with the conditions in the handoff file.
2. **Review the ETF B2 identity census and the COT cash-line half** [2.0.0_SA_COO~M].
3. **Re-walk with `/ui-walk --client "anna thiessen"`** after UIR-07 applies, to confirm the Global rank-1 condition
   [2.0.0_SA_COO~P, 1.0.0_SA_CTO].
4. **Push the 14 local commits** [0.0.0_AB_MSTR, on Andrew's word].
