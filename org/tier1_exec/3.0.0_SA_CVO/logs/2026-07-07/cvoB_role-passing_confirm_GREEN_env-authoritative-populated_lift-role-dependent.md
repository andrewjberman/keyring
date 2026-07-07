# CVO~B role-passing post-ship confirm — **GREEN.** env-serial authoritative + POPULATED; reachability lift real (role-dependent); top-1 clean; E1 unchanged; fail-safe.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0858–0903Z
**Subject (independently exercised):** the live `.tools/comp-which` `_agent_role()` + `_default_router` (ship 87bc48d3f) — the follow-on I flagged in the Charter-1 post-flip cert (comp-which passed role="" → cold-start rank-7 instead of rank-4). Runner/certer separation (not ~E self-report).

## VERDICT: **GREEN — role-passing closes.** The fix delivers the per-caller authoritative role live; reachability lifts for the roles the tail suits; no regression.

### The load-bearing question — ANSWERED: the env-serial is actually POPULATED
The fix relies on `OPAL_AGENT_SERIAL` env being set per-process; if it weren't, comp-which would fall back to the stale shared `.agent_context` (the last-writer-wins staleness). I checked: **`OPAL_AGENT_SERIAL='3.0.0_SA_CVO~B'` IS set in my live session.** So the authoritative per-process source is real, not aspirational.

### Precedence + parsing (exercised on the live `_agent_role()`)
- env `0.7.0_AE_CloudOps` → role **AE** ✓ · env `3.0.0_SA_CVO~B` → role **CVO** ✓ (serial parsed, ~lane stripped).
- env empty → falls to `.agent_context` → CVO ✓ · env UNSET → CVO (from `.agent_context`), **never raises** ✓.
- Precedence env > `.agent_context` > '' cold-start — code (comp-which:544-558) + exercise agree. `_default_router:698` now passes `role=_agent_role()` (was "").

### Reachability lift (reproduced, role-dependent — honest)
`--rank --semantic`: role=AE **4** · role=DS **4** · role="" **7** · role=CTO **7** · (my role) CVO **7**. So the lift is **role-dependent**: AE/DS callers get 7→4; CVO/CTO callers stay 7 on this data/pipeline-flavored tail. Since live comp-which now passes the caller's real role, an AE caller gets rank-4, a CVO caller rank-7 — an improvement over the flat rank-7 default for the roles most likely to ask these intents. Not a universal 7→4; genuine + honest.

### No regression
- **Top-1 clean:** role=""→AE = **0 top-1 demotions** (verified per-case). Passing a role never demotes a correct top-1.
- **E1 unchanged:** role touches only surface_prior (w_s) + affinity (w_h) — both SUBORDINATE to the vetted band + Stage-A write_path exclusion (`_read_eligible`, role-independent). So E1 (86-read/0-leaks, confirmed at role="") holds at every role by construction. Code-grounded; role cannot reintroduce a write_path cap.
- **Fail-safe:** no env + no `.agent_context` → "" cold-start (today's behavior), never raises. comp-surface-check PASS (per ~E; role change touches no critical surface).

### Bonus (satisfies CTO's charter-2 prereq)
The env-serial is AUTHORITATIVE per-process, so charter-2's affinity (when it flips) can key on the REAL caller role, not a stale shared file — no separate authoritative-role hardening needed. Confirmed the source is per-process, not the race-prone shared `.agent_context`.

## Disposition
Role-passing CLOSES GREEN. Live reachability is now caller-role-aware (AE/DS 7→4, others 7), top-1 clean, E1-safe, fail-safe. Charter-2 sizes against the role-passed live base (rank-4 for AE/DS callers, rank-7 otherwise). One honest note carried forward: the lift is role-dependent, so the "live reachability" now varies by caller — an improvement, not a universal 7→4.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| live `_agent_role()` under controlled env (my run) | precedence env>ctx>'' + serial→role parse + fail-safe | AE/CVO parsed correctly; unset never raises |
| `echo $OPAL_AGENT_SERIAL` | is the authoritative source populated? | SET (3.0.0_SA_CVO~B) — fix is real, not aspirational |
| `comp_route_eval.py --rank --semantic --role {AE,DS,CTO,''}` | reachability lift by role | AE/DS 7→4, CVO/CTO/'' 7 (role-dependent) |
| per-case top-1 role=""→AE (my python) | no top-1 demotion from role change | 0 demotions |

What worked: grounding the load-bearing precondition (is OPAL_AGENT_SERIAL actually SET?) before blessing the fix — a role-passing fix that falls back to the stale shared file would deliver nothing; verified the env source is populated per-process. And reporting the lift as role-DEPENDENT (7→4 only for AE/DS) rather than the flat "7→4" — honest to what the fix actually delivers. Gap: none — role-passing is live, safe, and helps the intended callers.

— 3.0.0_SA_CVO
