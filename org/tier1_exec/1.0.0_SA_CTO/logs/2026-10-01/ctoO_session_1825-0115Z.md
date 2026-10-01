# G-ACCT step 6 done, then the ~O queue cleared: R20 entries, MCPMSP v0.4 + round-1 analysis, OPLGTW v1.2, OG-t-2 CTO half -- 1.0.0_SA_CTO~O

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE, VALIDATE

**Date:** 2026-09-30 18:25Z -> 2026-10-01 01:15Z
**Task Order:** ad-hoc (HANDOFF_G-ACCT_STEP6_ELEVATED_20260930.md @709f29915f), then the ~O inbox
**Status:** COMPLETE (nothing at this seat waits on an act it can take)

---

## Objective

Execute the G-ACCT step-6 handoff: give Andrew a typeable Opal_Agent Claude window and get it signed in to
`opal-gateway-bbg` as Opal Bloomberg. Then, on Andrew's `/watcher` here, take the `1.0.0_SA_CTO~O` seat and clear its
queue.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| naming-gate (as library) | `load_legacy_reads()`, `authority_ok()` over NAMING_LEGACY_READS.json | PASS | 10 usable / 0 refused at HEAD; 8/8 authority; 2 negative controls refused |
| prd-signoff | `status NFRA_MCPMSP`, `status NFRA_OPLGTW` | PASS | proved v0.4 re-opened no half; v1.2 showed the CONTRACTS change, then the CVO re-sign |
| launch-gate.ps1 | via launch-v2 `-GateOnly`, and as the operator | PASS | GATE: PASS as Opal_Agent; REFUSE PROBE-READABLE ADMIN-GROUP as operator (negative control) |
| surprise-row-gate | via safe-commit on Z-S50 | PASS (after fix) | first refusal was mine: `surfaced_at` `22:1xZ` fails the schema regex |
| comp-find | (none run) | SKIPPED | targeted reads by known path; the rail denied one raw grep, so the native Grep tool was used |

**What worked:** using the gate's own functions to grade the R20 entries, instead of re-deriving the rule.
**What failed:** the `[WATCHER-EXPIRED]` re-arm line prints the inbox-watch path UNQUOTED, which breaks on this box's
`Opal Bloomberg` path (quoted by hand on each re-arm).
**Gap found:** the safe-commit `index.lock` and MERGE_HEAD refusals in the shared tree have no wait-and-retry. Each
needed a hand-built background loop.

---

## Work Completed

### 1. G-ACCT step 6 -- DONE (whoami = Opal Bloomberg)
- Five measured launch attempts (record: `C:\Users\Opal Bloomberg\.opal_runtime\G-ACCT_STEP6_RESULT_20260930.md`,
  operator-local):
  - `runas /trustlevel:0x20000` stays HIGH integrity.
  - `Start-Process -Credential` gives an untypeable window at HIGH and at MEDIUM, which falsifies the UIPI hypothesis.
  - `Process.Start` from a Medium (explorer-launched) shell gives a typeable window.
- The runtime's `concierge-gate.sh` needs jq on PATH. I copied the vendored jq 1.7.1 into
  `C:\Users\Opal_Agent\.local\bin` and appended that folder to Opal_Agent's user PATH.
- Operator launcher `C:\Users\Opal Bloomberg\.opal_runtime\launch-v2.ps1` (+ `.cmd`): Andrew tested it, and it is
  typeable.
- Both defects are filed as NFRA_OPALAI-Z-S50 @1f34e162cc.

### 2. Identity correction
- What I took for a "live non-elevated ~O" was this session's own watcher, plus an orphaned `agent-poller.py`
  (pid 21008) from my first registration.
- I deregistered with `kill_pollers` (1 killed), re-registered (pid 48588), and wrote the session serial file.

### 3. 27342 -- R20 entries (un-holds MX-t-10/t-13/r-7)
- e692000c06: an addendum to the authority record carrying ids NFRA-MCPINDEX-R20-01..08.
- 0d71a22887: 8 entries in `org/standards/NAMING_LEGACY_READS.json`, pin e692000c06, cutoff 2026-12-31 as a review
  point.

### 4. 27335 -- Schwab catalog row
- Ruled to the round-5 slug. MX-t-2 is superseded, and round 5 is frozen.

### 5. 27352 -- NFRA_MCPMSP
- PRD v0.4 @7ecc812be5: hop 0 struck; A1 PARKED.
- Round-1 L10 analysis @5e2ff94c28, amended @6924628218:
  - grades: 0 REALIZED / 2 HELD / 9 NOT_REALIZED;
  - round-2 list E1-E6;
  - R-2 ruled by the laptop gate owner (msg 103400).
- Rulings:
  - 27413: option (a). MCPMSP builds the internal reader role; MCPINDEX routes its two readers.
  - 27412: `MSP_CALLING_IDENTITIES` approved.

### 6. 27410 -- NFRA_OPLGTW PRD v1.2 (the NFRA_TRNSPT orders)
- 725230b531 and the text fix c9fd271499: C7 plus workstream TRNSPT-DEPS, orders O1-O5.
- CVO finding F1 closed: there is no thread reach. Ratified half RE-SIGNED, `prd-signoff status` reads current.

### 7. 27434 -- OG-t-2 never-widen CTO half
- SIGNED @51df60aa1a with 3 conditions. The CVO second half is @045f6886d9; I relayed it to 2.0.0_SA_COO~O.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| R20 cutoff 2026-12-31 | X11/X12 are CONDITIONAL on events. The gate maps conditional to a date, and PERMANENT would misstate the row. |
| Hop 0 struck, A1 parked, no ENDPOINT edit | Andrew-direct ~17:45Z. Keeping ENDPOINT/CONTRACTS untouched kept the CVO half valid. |
| Headless content routes get new prefixes and bearers, never `/ms/*` | `/ms/*`'s contract is structure-only, and a leaked bearer should reach one prefix. |
| MCP stays inspect-only for attachments; PDF bytes only on the headless mail route | The byte need is a pipeline's (bronze), not an interactive caller's. |
| Opal Bloomberg write-capable tier read added to OG-t-2's verify | That pair had no second source, and step 11 did not exercise it. |
| `opalbloomberg@` is never an MSP calling identity | C8, harness indistinguishability, write-capable principal. Andrew then chose "Not yet" (G-MSPID). |

---

## Files Modified

See commit messages: e692000c06, 0d71a22887, 7ecc812be5, 5e2ff94c28, 1f34e162cc, 6924628218, 725230b531,
51df60aa1a, c9fd271499. Outside the repo (operator-local, never committed):
- `C:\Users\Opal Bloomberg\.opal_runtime\launch-v2.ps1`, `launch-v2.cmd`, `G-ACCT_STEP6_RESULT_20260930.md`
- Opal_Agent's `.local\bin\jq.exe`, and its user PATH

Andrew records committed this window:
- `ANDREW_DIRECT_20260930_225xZ_NFRA_MCPMSP_MSP_CALLING_IDENTITY_NOT_YET.md` @6924628218

Andrew's other words were captured in the operator-local result record ("go, also let me know when launcher version is
ready, i can test that anytime").

---

## Blockers

None at this seat. Open elsewhere, each with its owner:
- G-MSPID (Andrew)
- G-USER, G-IT-INF, G-ADVISOR, G-FIRM for MCPMSP A1 (Andrew)
- G-PUSH (0.0.0_AB_MSTR~Z on Andrew's word)
- the site-Z apply HOLD on opal-assets and mdpf-pipeline until the laptop push (0.0.0_AB_MSTR~Z msgs 27461/27465)

---

## Current State

Opal_Agent's Claude is signed in to `opal-gateway-bbg` as opalbloomberg@opalinvest.com, and the credentials file was
written 2026-09-30 15:03 ET. Launch it with `C:\Users\Opal Bloomberg\.opal_runtime\launch-v2.ps1`: it relaunches via
explorer at Medium, runs the gate as Opal_Agent over a pipe, then starts Claude with `Process.Start`. The repo launcher
`opal_ai/opal/runtime/launcher.ps1` still has defects 5 and 6 (row NFRA_OPALAI-Z-S50, issuer 2.0.0_SA_COO~AI).

All commits above are site-Z CLOUD LOCAL; origin/CLOUD read 85a765dbcd (ls-remote, 01:14Z). The project states:
- NFRA_MCPMSP is cutting round 2 under 2.0.0_SA_COO~MS, from ledger/ROUND_ANALYSIS.round1.md.
- NFRA_OPLGTW v1.2 is ADMITTED. OG-t-2 PHASE B holds both halves and runs off-hours.
- NFRA_MCPINDEX MX-t-10/t-13/r-7 are un-held.

---

## Next Steps

1. **[1.0.0_SA_CTO~O] Write the NFRA_MCPINDEX round-5 analysis on the CVO's slug.** It carries the Schwab catalog row
   (27335) and the routing of the portal_index/opal_discover readers through MCPMSP's internal role (27413).
2. **[2.0.0_SA_COO~O] Run OG-t-2 PHASE B off-hours under K1-K3 / conditions 1-3**, naming the Opal Bloomberg session
   (launch-v2) in the ledger. Then cut TRNSPT-DEPS O1-O5 against @c9fd271499.
3. **[2.0.0_SA_COO~AI] Cut the launcher fix from Z-S50** (Process.Start, a Medium parent, jq provisioning).
4. **[0.0.0_AB_MSTR~Z] Quote the inbox-watch path in the `[WATCHER-EXPIRED]` re-arm line.** It breaks on a path with a
   space.
5. **[Andrew] G-MSPID when ready.** Create G-USER, or name a non-person account.
