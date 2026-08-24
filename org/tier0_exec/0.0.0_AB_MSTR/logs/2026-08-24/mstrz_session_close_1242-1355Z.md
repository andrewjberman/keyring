# MSTR~Z session close -- launch, parity assessment, and the Bloomberg constituent hunt (1242-1355Z)

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE

Seat: `0.0.0_AB_MSTR~Z`, site Z. Session began 2026-08-24T12:42Z (fresh; predecessor died in the
08-21 wind-down). Closing per Andrew-direct fabric-wide close-out, bridged 13:42:28Z
(`68ab4492-0197-4404-b0e7-b90543eb843c`). **No prior log this session -- window is the whole session.**

> **READ THIS LOG'S CLAIMS AS DATED.** Per the bridge's own instruction, every state claim below
> carries the CHECK that re-derives it. Values were true at the stated time and are not asserted now.

## 1. Launch (all three mandated steps + XXX.md)

`/watcher` task `btntyq2g5` · `/agentbus` task `b2de49ebb` (sitez inbound) · `/integrate` ASSESS-ONLY.
**Zero crons** -- correct per XXX.md Step 1b-F: the `/govern` re-arm clause is STRUCK (discharged
2026-08-05, successors do not re-arm) and the semantic-evolution backstop is MSTR-**base**, not `~Z`.

XXX.md: A.1 serial file written · A.2 audit invoker (finding, section 4) · A.3 **98 of 102**
comp-tools resolve bare AND a forwarder EXECUTED (unresolved: comp-closure, comp-directives,
comp-lease, comp-ledger-agreement.py) · B inbox empty · B.1 **0 TOs I execute** · D hook wired ·
E context set.

**MY OWN REGISTRATION WAS A LEFTOVER AND READ HEALTHY.** `get_agent_status` returned
`LIVE, last seen 78s ago, PID 38940` -- pid 38940 had NO process. `last_seen` was current because the
broker rewrites the whole file on ANY agent's heartbeat (BG registered 12:43:29Z). **Re-check:
compare the liveness pid against process truth, never the last_seen age.**

## 2. THE FINDING OF THE DAY -- Bloomberg DOES hold DIVZ/IDVZ constituents

Andrew-direct ~13:0xZ, VERBATIM: *"there is absolutely no way bloomberg does not track constituent
holdings for etfs"*. **He is right, and it is measured, not conceded.** Record committed
`a0d037464c`, pushed; report to CTO `d9906cce-b6a3-4ffb-a649-cd70d16adc2b`; CTO's own record landed
laptop-side `origin/CLOUD @abd4a35a3a`.

Holdings-DERIVED fields return fund-specific non-null data (ReferenceDataRequest, SPY in-request
control): count DIVZ=30/IDVZ=46; HB_INDUSTRY_SECTOR_ALLOCATION 10/14 rows; HB_GEO_CNTRY_ALLOC 3/20
rows; FUND_PCT_TOP_TEN_HOLD 48.75998/32.94046. **A sector allocation is a function OF the
constituents.**

**The 08-21 brief's MECHANISM was wrong; its measurements were fine.** It said the route is "a
different REQUEST TYPE, not a different name". Both halves falsified, each with a control:

- `INDX_MEMBERS` IS servable via ReferenceDataRequest -- INDU returned 30 members, SPX + INDX_MWEIGHT
  503 rows. Subcategory says NOT_APPLICABLE_TO_REF_DATA; **the message body says "Field not
  applicable to SECURITY"**. Reciprocal control: the count field works on the ETFs and fails on INDU;
  INDX_MEMBERS does the exact inverse.
- `PortfolioDataRequest` returns INVALID_SECURITY **for SPY as well** -- it addresses own-PRTU
  portfolios, not third-party ETF tickers. A route that rejects SPY was never a route to any ETF.

**The wall is a BQL ENTITLEMENT.** `//blp/bqlsvc` OPENS; every query returns *"User not authorized to
use BQL."* **Service-level control:** `get(px_last)for(['IBM US Equity'])` -- no holdings, no Opal
funds -- refused identically. The brief's *"zero NOT_AUTHORIZED therefore not entitlement"* was TRUE
of the refdata field surface and FALSE of the estate.

**HISTORY: current-day only.** HistoricalDataRequest on DIVZ 06-01..08-22 with PX_LAST as in-request
control: PX_LAST 6 dates, TOTAL_NUMBER_OF_HOLDINGS_IN_PORT and FUND_PCT_TOP_TEN_HOLD **zero rows**.
**The TrueShares daily capture remains necessary and its daily loss remains permanent.**

Oracle verified at this seat, not accepted: DIVZ 29 / IDVZ 43 data rows in the 2026-07-31 CSVs. The
gap vs 30/46 is three weeks of drift plus a `SALXX` money-market CASH line in row 1 of both.
**A weight tie-out is structurally unavailable under a negative outcome** -- no list to tie out.
Nothing landed in S3; the `adhoc-constituent-hunt/` prefix stays empty. A3 NOT built (rider respected).

Probe scripts are scratchpad-only (session-local, not committed). To re-derive: blpapi 3.26.5.1 is
importable natively on this box; `//blp/apiflds` FieldSearchRequest enumerates the field dictionary,
which is how name-guessing became a census (search "holdings" = 2164 fields, 22 bulk, no FUND_HOLDINGS).

## 3. Cross-fabric parity -- ASSESSED, NOT MERGED

Measured 13:0xZ: base `842195572a`, CLOUD +72 / SITEZ +82, **overlap 2 of 121 union-touched = 1.65%**
(healthy band), `git merge-tree --write-tree` **rc=0 CLEAN**, merged tree `a49c2bc4d5`.
**Re-derive before acting: `git fetch origin && git merge-base origin/CLOUD origin/SITEZ`, then re-run
merge-tree -- these counts move with every push on either fabric, and CLOUD was advancing during the
close-out (d2706b2849 at 13:42Z -> b102c11bbe at 13:46Z).**

Both overlap files resolved, neither needs a law owner:

- `infra/aws/lambda/ci/lambda-source-map.json` -- BASE-side ranges DISJOINT (CLOUD @1522; SITEZ @3,
  @2715-2718) -> mechanical union.
- `org/surprise_channel/ETFS_POSITIONING/INVESTIGATION_v1.md` -- site Z pre-applied the ADD/ADD
  rename to `INVESTIGATION_v1.Z.md` @`cdb83273ab` per cross-fabric CTO ruling 65860. A merge keeps
  both files; that is intended, and it is why merge-tree is clean.

**DEPLOY EXPOSURE IS ASYMMETRIC AND A FRESH SEAT MUST NOT SKIP THIS.** Leg B (CLOUD merges SITEZ) =
0 files. Leg A (SITEZ merges CLOUD) ceiling 4, **true targets 1**: three `data/etfs/scripts/gold/*`
resolve to `None` (`etfs` has **0 occurrences** in `.tools/safe_deploy_core.py`, 1295 lines, positive
control `cot`=16), and `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` ->
`opal-data-mdpf/code/scripts/assets_gold/`, a SHARED home where the key EXISTS -> **update ENFORCED**.
**Verification primitive:** import `safe_deploy_core` and call `file_to_s3_target(path)`, positive-
controlled with a bd gold path. MERGE HELD -- not opened during the close-out. It parks clean.

## 4. OPEN FINDING -- the audit-archive tamper alarm is FALSE, and structurally so

XXX.md A.2 emits **18 findings incl. 8 NON-APPEND-EDIT** (the highest-severity class) at every
site-Z startup. **They are cross-device artifacts, not tampering.** `.gitignore:68` `*.log` makes the
live audit logs DEVICE-LOCAL while `org/audit/archive/` is TRACKED (`git ls-files` = 420) -- **the
baseline travels between machines and the logs do not.** No `archive/<device>/` exists, so
`audit-archive-invoker.py` `chain_root()` (:99-115) falls back to the flat root, which its own
docstring calls *"the laptop chain"*. **Measured: 0 of site Z's 190 log lines appear in the
baseline's 1664**, and the date ranges are disjoint. A truncated log would be a PREFIX of its
baseline; zero overlap is a different machine's log. `DEVICES.txt` already registers `sitez`; the
archive layout has not moved. The docstring's "transition-safe by construction" holds for MINTING
(`authorise_device()` refuses) but **NOT for DETECTION**.
**Owner `0.7.0_AE_CloudOps`, gate `1.0.0_SA_CTO` -- neither seated on site Z. NOT actioned (close-out).**
Re-derive: `python .tools/audit-archive-invoker.py`, then `comm -12` a live log against its baseline
copy under `org/audit/archive/<baseline-ts>/`.

## 5. OPEN FINDING -- BG is ALIVE but PRUNED from the broker

`org/mcp/liveness.json` held **ONE entry (mine)** at 13:4xZ and `get_live_agents` showed 1 -- while
`0.0.3_BG_BBGTerminal` was alive by process truth (pid 6248 python.exe; inbox-watch stream pid 429
under live parent 77). **A registration defect, not a liveness one.** Consequence: anything keying
off registration reads BG as absent. **Had I trusted the broker I would have skipped relaying a
sovereign close-out order to a live seat.** Relay went via `send_message` -> QUEUED; the file landed
and BG's watcher claimed it 13:44:54Z (3714 B). **Per Rule 22b that is the EMITTED clock -- the
watcher claimed it; only BG's own ACK proves the agent read it.**
Re-check: compare `liveness.json` entries against `ps -ef | grep inbox-watch`.

## 6. A SERIAL IS NOT A SEAT -- an attribution error, raised and resolved

Base MSTR credited me with three acts: holding the shared-infra fence rather than relaying their
lift, correcting "14 on 7" to 15 on 8, and correcting a "fabric-wide" freeze lift to CLOUD-wide.
**I could not verify any of them from this seat and declined to inherit them** (`c412cd4e`), flagging
them UNVERIFIED-AT-MY-SEAT rather than accepting.

**Base MSTR then resolved it exactly** (`c52fb431`, 13:45:46Z): all three acts are **real**, at
**this serial**, on **2026-08-21 (~20:52Z, ~21:15Z, ~21:19Z)** -- in the PREDECESSOR session, which
died in the wind-down. Their words: *"I CONFLATED A SERIAL WITH A SEAT... a fact that was true of an
agent-identity across a boundary where the agent had been replaced, and nothing in the credit
announced that it had aged."*

> **THE LESSON FOR A FRESH SEAT, and it is the same vintage class as a stale ref pin, only pointed at
> ATTRIBUTION instead of measurement: a serial persists across seats; the context does not. Inherited
> credit is an unverified claim, and it is the kind nobody audits because it FLATTERS rather than
> ALARMS.** When a peer attributes work to your serial that is not in your transcript, the honest
> answer is "not this seat," not silence.

Verifiable in THIS session's transcript: flagged base MSTR's cottonwood 13:20Z mark as apparently
passed (it had not been -- they measured the apply at 12:54:28Z on the applied plane, 26 min inside;
my flag was unnecessary but correctly raised); re-derived the ETFS collision independently; held the
merge on Rule 26 reasoning; ran the constituent hunt that falsified the not-an-entitlement
foreclosure; and **self-caught a FALSE PASS in my own BQL control script** that printed
`OK / data returned (0 chars)` for three refused queries -- an empty capture rendered as success.
Only the corrected run's numbers appear in section 2.

## 7. Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-find | `-i 'BAD_FLD'` | PASS | 10 hits / 27864 files; bands SURFACED=1 CONFIG=5 DOC=4 -- located the Friday brief in one call |
| comp-find | `--name blp_client.py` | PASS | 1 hit, HEAD band |
| comp-pipescript | `deployed build_cottonwood_mdpf_slice.py --pipeline mdpf` | PASS | STALE: local 5c48cd38 vs s3 172111b3; per-layer denominators printed |
| comp-pipescript | same, flagless first attempt | REFUSED rc=2 | Correct -- `--pipeline` required, NO GUESS made. The refusal is the feature |
| comp-which | `"how do I grep the repo"` | PASS | A.3 exercise -- the forwarder RAN, not merely resolved |

What worked: `comp-find`'s BAND classification separated the Friday brief (DOC) from its config
copies immediately; `comp-pipescript`'s flagless refusal prevented a wrong-tree read.
Gap found: none new at the tool layer. **The instrument that failed this session was my own scratch
probe, not a comp-tool** (section 6).

## 8. Blockers

**None at this seat.** Nothing half-landed, nothing staged, no merge open. The two open findings
(sections 4 and 5) are ROUTED-NOT-BLOCKING and their owners are unseated on this fabric.

## 9. Current State -- THE HANDOFF (zero prior context assumed)

- **Site Z is TWO seats: `0.0.0_AB_MSTR~Z` (me) and `0.0.3_BG_BBGTerminal`.** 26 active `~Z` TOs sit
  on DEAD seats (AE_CloudComp~Z 9, AE_OpalETL~Z 7, AE_CloudOps~Z 7, DS~Z 2). **Do not read any of
  them as live work.** Re-derive: `python .tools/to-check.py --all --assignee '~Z'`.
- **Site-Z directives: D6 / D7 / D9** (D8 CLOSED 08-20). Placement authority is the header of
  `org/missions/DIRECTIVES.yaml` (SITEZ = D6/D7/D8/D9; LAPTOP = D0-D5).
- **D6 state assessment MOVES TO THE PRD ROUND -- NOT STARTED, and it parks by staying unstarted.**
- **Z-S13 stays ARMED** with its named owner and durable channel record. Parking an armed item with
  a named owner is a safe position; disarming one mid-close is not.
- `origin/SITEZ` was **`a0d037464c`** at ~13:35Z (my push; safe-deploy confirmed 0 deploy-scope
  files). `origin/CLOUD` was **`b102c11bbe`** at 13:46Z and STILL MOVING as seats landed close-out
  commits. portal `origin/DEV` `d43b88c5`; portal `origin/PROD` `8a96c916` **UNWRITTEN**;
  v2.1.165 STAGED at `a239e4a9`, 0 remote branches, ledger KNOWN-HELD/SOVEREIGN-GATED.
  **ALL OF THESE ARE DATED PINS -- run `git ls-remote origin <branch>` before acting on any.**
- **The portal PROMOTE WORD IS ANDREW'S and had not arrived.** Base MSTR explicitly declined to read
  the fabric close-out order as releasing it: a general instruction does not answer a specific question.
- **The BQL entitlement is a SPEND CARD AT ANDREW, not a task.** Nobody should spec A3 against a
  surface that refuses the control query.
- Bloomberg DAPI was reachable at `127.0.0.1:8194` (`//blp/refdata`); services refdata / apiflds /
  bqlsvc / instruments / tasvc all OPEN, bqlsvc UNENTITLED. Re-check: `bloomberg_health`.
- mdpf 13:30Z fire (laptop): cottonwood HEALED on the deployed fix; the global leg still refuses on a
  cross-axis gate that was UNMASKED rather than caused -- unreachable behind the failing leg for four
  days. Laptop-owned; nothing for site Z.

## 10. Next Steps

1. **[Andrew]** BQL entitlement -- buy or not. Yes -> the constituents pull joins `etf_daily_pull.py`
   as CTO's A3. No -> TrueShares capture-forward is the only path and its daily-loss argument stands.
2. **[Andrew]** Whether site Z restarts seats at all. 26 TOs are stranded on dead ones; his 08-21
   word was "no new agents" and I did not overturn it on my own reading.
3. **[1.0.0_SA_CTO + Andrew]** The PRD-per-directive round. The D6 state assessment lands there.
4. **[0.7.0_AE_CloudOps / 1.0.0_SA_CTO]** The audit-archive device-chain defect (section 4) -- create
   `org/audit/archive/sitez/` or scope detection per device. Today it manufactures 8 false
   NON-APPEND-EDIT findings at every site-Z startup, in the estate's tamper-evidence base.
5. **[0.0.3_BG_BBGTerminal]** Re-register at next turn (section 5), and note the pruned entry in its
   own log so a fresh seat does not read it as a dead predecessor.
6. **[0.0.0_AB_MSTR]** The cross-fabric merge parks CLEAN; resume on either MSTR's word after the
   PRD round. Nothing about it decays.
