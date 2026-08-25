# ANDREW-DIRECT 2026-08-24 ~20:0xZ (the `1.0.0_SA_CTO~Z` terminal, site Z) -- `/loop [30m]`: run `/open-calls`, pitch the calls WITH RECS to CVO~Z to ADJUDICATE, then proceed; the site-Z fabric does ETFS_POSITIONING work and NOTHING ELSE this session

**Channel:** Andrew, directly at the `1.0.0_SA_CTO~Z` terminal, as a `/loop` invocation immediately after ruling C2-C5 ("all recs approved, proceed").
**Received by:** `1.0.0_SA_CTO~Z`. **Recorded + broadcast:** same turn (this file + MCP to `0.0.0_AB_MSTR~Z`, `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`).

## VERBATIM (the `/loop` args, exactly as typed)

> **`[30m] <Run /open-calls, pitching the calls with your recs to CVO to adjudicate, then proceed. This workflow and process applies exclusively to ETFS_POSITIONING work and that is the only work your fabric should be doing this session.>`**

## TWO FURTHER WORDS, SAME TERMINAL, MINUTES LATER -- VERBATIM

> **"Then make this loop a skill called /self-drive, where the user can write /self-drive to a single project or group of projects as a function of the directives.yaml. I.e., /self-drive laptop directives, or /self-drive sitez directives, or /self-drive D4."**

> **"The premise of the skill (and it should be built in) that the loop persists until the directive is done. Once complete, the loop turns off and the driver writes a log on the self-drive process or every 2 loops, whichever comes first."**

**What these settle:** the loop above is the FIRST INSTANCE of a general mechanism -- `/self-drive <scope>`, scope resolved from `org/missions/DIRECTIVES.yaml` (a directive code, a project code, or a placement group `laptop directives` / `sitez directives`); the loop PERSISTS UNTIL THE DIRECTIVE IS DONE (a completion condition read from the register, never a date), then TURNS ITSELF OFF; the driver WRITES A LOG on the self-drive process at completion OR every 2 ticks, whichever comes first. Built this session at `.claude/skills/self-drive/SKILL.md` (lane ANY); the loop armed above is re-pointed at `/self-drive D4` once the skill lands, so the running loop carries his completion + logging semantics.

## WHAT IT SETTLES -- three instructions in one line

1. **A SCOPED LOOP AUTHORIZATION at `1.0.0_SA_CTO~Z`: every 30 minutes, `/open-calls`.** Operator-initiated (his `/loop`), so it is the sanctioned exception to zero-crons-at-launch; **session-scoped by his own words ("this session")** -- the cron dies with the session and NO successor re-arms it without his fresh word. Cron `*/30 * * * *`, prompt = the text above verbatim.
2. **A PROCESS CHANGE for sovereign calls on this work: pitch them, WITH THIS SEAT'S RECS, to `3.0.0_SA_CVO~Z` to ADJUDICATE -- then PROCEED on CVO~Z's verdict.** For ETFS_POSITIONING work this session, a call that `/open-calls` would otherwise hold at Andrew goes to CVO~Z as the adjudicator (CVO independence: a CVO verdict is constitutionally independent; `org/XXX.md` authority hierarchy). *"Then proceed"* = execute on the verdict without a round trip to him. **What this does NOT change:** the record+broadcast law (his words still get recorded verbatim), Rule 27 (decomp before TOs; execute on spec), and the standing NEVERs -- CVO~Z adjudicates CALLS, it does not lift a NEVER (never-widen sign-off on a served key, vendor egress beyond his words, spend). Those remain his, and a card of that class is still surfaced to him -- stated here so CVO~Z is never handed a decision the law reserves.
3. **FABRIC SCOPE: the site-Z fabric does ETFS_POSITIONING work ONLY this session.** Reading, stated so it can be flagged if wrong: **"ETFS_POSITIONING work" = the D4 body of work -- `ETFS_POSITIONING` (round 1 delivered; promote held on two conditions) AND `ETFS_INGEST` (its ingestion/pipeline project, registered on his own "register the project" word and confirmed under C5 twenty minutes earlier).** Reading it as excluding `ETFS_INGEST` would exclude the project he just told COO~Z to decomp. Everything else on site Z (D6 / D7 / D9 legs, SYSPARITY, the estate report) is OFF this session; BG's daily vehicle stays in its HOLD (it is the ETF data's carrier, not new work).

## SCOPE -- surfaced, not adjudicated

- **"Your fabric"** = site Z (MSTR~Z runs it). This seat relays the scope to MSTR~Z as the fabric operator; it does not re-task other seats. If MSTR~Z reads "your fabric" narrower (CTO~Z's own lane only), that is theirs to say and his to settle.
- **The loop's tick body is `/open-calls` -> CVO~Z -> proceed.** It is not `/drive`; it dispatches nothing on a timer; a tick with zero calls prints the zero-line and stops.
- `org/XXX.md` Step 1b-F's CTO row says "Zero crons" -- **this is a session-scoped operator arm, which that row's standing rules already permit ("Loops are operator-initiated"); the row is the carrier for CROSS-SESSION re-arms, and there is none here.** Recorded in this file rather than the law file for that reason; MSTR~Z may add a struck-on-close clause if they judge the row should carry it.

## THE ACTS THIS TURN

| act | evidence |
|---|---|
| this record | commit hash in the session log |
| `CronCreate */30 * * * *` with the verbatim prompt, recurring, session-only | job id in the session log |
| broadcast to MSTR~Z / COO~Z / CVO~Z (scope + the adjudication role) | MCP receipts |
| first tick executed now: `/open-calls` at this lane | its output in the terminal |
