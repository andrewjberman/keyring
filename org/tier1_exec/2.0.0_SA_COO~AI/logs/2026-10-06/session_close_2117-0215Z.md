# Re-seat for two NFRA_OPALAI items: opal_ai CI green on DEV, R25.3 cut, built and drained as OA-f-14 -- 2.0.0_SA_COO~AI

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, IMPLEMENT, VALIDATE

**Window:** 2026-10-06 21:17Z -> 2026-10-07 02:15Z (site Z). First log of this seating.

## Objective

Seated by `0.0.0_AB_MSTR~Z` on Andrew's word (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_211xZ_NFRA_OPEN_CALLS_ALYSSA_NOT_NOW_COO_AI_IF_WORK_G2ND_ANY_TIME.md`
@9480178371), scoped by `1.0.0_SA_CTO~O` msg 30323 to two items, in order:
1. fix the opal_ai CI red (failure on DEV and PROD at e34ba403c3);
2. cut R25.3 (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round19.md:100`) as one cell.

Both are closed in lane. `1.0.0_SA_CTO~O` accepted both (message of 02:12Z) and asked for this log, a saved handoff and
IDLE. Nothing further is cut without a new word.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-which` | startup exercise | PASS | forwarder ran; 104 of 104 comp-tools resolve bare |
| `comp-find` | `R25\.3` over `org/missions` | PASS | 3 hits across 16270 files; found "carried to NFRA_OPALAI" in OPLGTW's decomposition and round-20 analysis |
| `.tools/prd-signoff.py status` | NFRA_OPALAI | PASS | v0.5 ADMITTED; ratified-text half current by ENDPOINT hash, text changed since signed (WARN at the gate) |
| `.tools/to-check.py --all --assignee` | this lane | PASS | 0 active task orders at seating |
| `comp-blast` / `comp-routes` / `comp-cache` | -- | NOT RUN | one cell, five named gateway files, no route, cache or infra edge added; the write surface was read directly instead |

**What worked:** `comp-find` located where R25.3 had been carried in one call, which settled which lane owns the cut.
**What failed:** a `comp-find ... | tail` pipe is refused by the rail (census into a receiver); use the tool's own flags.
**Gap found:** none new.

## Work Completed

### 1. Startup
`/watcher` (registered, Monitor armed and re-armed on every 30-minute expiry), `org/XXX.md` steps A-E. Two stale
messages acked (29144, 29168). Steps 2-4 (prior logs, `prompt.md`, org chart) were NOT read: the direction scoped the
seat to two items. The audit-archive invoker printed five integrity findings (four missing baselines, one non-append
edit in `org/mcp/agent-spawn-audit.log`); whether they have an owner was NOT checked.

### 2. Item 1 -- opal_ai CI
- Measured cause: the only failing check was ruff, 2 findings, both `EXE001` (shebang present, file not executable), on
  `opal/agent/teams_watch/teams-watch.py` and `opal/agent/tools/portal_lookup.py`.
- The directed fix (chmod +x) is unreachable through `safe-commit.sh` here: `core.fileMode=false`, so
  `git commit --only` reads the mode from HEAD and reports nothing to commit. Row `NFRA_OPALAI-Z-S58`.
- Fix landed instead: one shebang line removed from each file (every call site runs them as `python <file>`).
  opal_ai `de5ce25fa3`. `1.0.0_SA_CTO~O` accepted the mechanism (msg 30328).
- `0.0.0_AB_MSTR~Z` pushed DEV e34ba403c3 -> de5ce25fa3 on Andrew's word (msg 30452). CI run 37549439215 on that
  commit: success; py_compile, ruff (0 findings), ascii, device-path, pytest all PASS.

### 3. Item 2 -- R25.3 as cell OA-f-14
- Issued: decomposition ADDENDUM R2-A12, order
  `org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-f-14.scoped-consent-envelope.md`, checks
  `deliverables/2.0.0_SA_COO~AI/round2/checks/f14.AC1-AC3.sh`. Issuance e1ef365925, drained ea4f02487a.
  fanout: 1 of 1 chains.
- First build (worker `0.9.0_WK_NFRA_OPALAI~29`): a Graph scope map per tool, `identity_scope.consent_scopes`, both
  `/login` consent legs and the silent acquire narrowed for a scoped identity. Issuer re-grade 3 of 3.
- Issuer finding on its own step: the silent-acquire bound is keyed on the token OWNER while the map is keyed on
  TOOLS, so non-tool routes minting the concierge's token are narrowed without an entry. Row `NFRA_OPALAI-Z-S57`
  (ARMED against the release). `1.0.0_SA_CTO~O` ruled (a), msg 30365: keep the bound, map every non-tool caller.
- Amendment A1 (411fd64465): `CALLER_GRAPH_SCOPES`, the union rule, a seventh arm that counts every `get_token`
  call site outside `tools.py`. Built by worker ~29 (ee22aced29, proof ed194dbbda).
- Issuer re-grade, each check run by this seat: AC1 7 of 7, callers 10 (8 modules), 0 unmapped; AC2 36 passed /
  failed []; AC3 4 gateway files, 0 outside the order. Order flipped complete d76ea69096; row Z-S59 cites Z-S57.
- Held undrained through the fabric hold (msg 30383 -> RELEASE 30443) and until NFRA_OPLGTW OG-rl-9 was terminal
  (its amendment A1 makes the release set every live..CLOUD gateway difference). Drained af10f7d42b after
  `2.0.0_SA_COO~O` msg 30506: 8 files needed, 0 dropped, 0 foreign. AC1 and AC2 re-run on the shared tree: PASS.

## Decisions Made

- **Shebang removal instead of the mode bit** (item 1): the only route inside rule 14a; accepted by the CTO.
- **Step 4, the silent-acquire bound** (item 2): the issuer's decomposition judgment, later ruled inside R25.3.
- **Non-email identity binding unions the caller's scopes** (A1): a `<tid>/<oid>` value cannot be matched to an email
  from configuration; the ruling forbids a dead end. Recorded in the order's record face for the analysis.
- **No drain before OG-rl-9 terminal**: agreed with `2.0.0_SA_COO~O` (msg 30477).
- **Worker stopped at HOLD, respawned** after `0.0.0_AB_MSTR~Z` ruled branch commits outside the hold (msg 30397).

## Files Modified

See commit messages: opal_ai `de5ce25fa3`; workspace `e1ef365925`, `ea4f02487a`, `b6bcb7a749`, `411fd64465`,
`d76ea69096`, `af10f7d42b` (this seat); `1fb6300bcb`, `95028d4d69`, `ee22aced29`, `ed194dbbda` (worker ~29).

## Blockers

None BLOCKED. Nothing in this lane is waiting on this seat.

## Current State

- **opal_ai:** origin DEV = de5ce25fa3, CI success. Origin PROD = e34ba403c3, last run failure. PROD goes green only
  when de5ce25 is promoted, which is Andrew's word; no promote was asked or made.
- **OA-f-14 (+A1):** `complete`, on local CLOUD at af10f7d42b. Push state at 02:1xZ: LOCAL (ls-remote read: origin
  CLOUD ba32125d62). NOT deployed: the live gateway serves 7d65a28db0, and the four files
  `infra/aws/ec2/opal-gateway/app/graph_scope_map.py`, `app/identity_scope.py`, `app/token_broker.py`,
  `tests/test_scoped_consent_r253.py` are the live..CLOUD difference.
- **Behaviour at release:** the concierge `opalbloomberg@opalinvest.com` asks for 8 Graph scopes instead of 17, or 9
  (adds `Files.ReadWrite.All`) when `TAXSMA_WORKBOOK_IDENTITY` is a tid/oid value. Unscoped identities unchanged.
  Never exercised against a real Microsoft consent.
- **Rows:** Z-S57 ARMED against the release (build-side condition met, Z-S59); Z-S58 INERT; W29-S1 INERT (two
  `test_asker_scope.py` tests fail in a multi-file pytest run, at base too).
- **Not verified:** the worker's negative control on the census arm was reported, not re-run by this seat. The live
  values of `TAXSMA_WORKBOOK_IDENTITY`, `MS_INGEST_IDENTITY` and `OTP_MAILBOX` were not read.
- Worktrees `C:/tmp/coo-ai-r253` and `C:/tmp/oa-29` and their branches are removed. `C:/tmp/oa-dev`
  (opal_ai, branch `nfra-opalai-r2-dev` @de5ce25fa3) remains.
- No cron armed. One inbox Monitor, re-armed per expiry.

## Next Steps

1. `[2.0.0_SA_COO~O]` cut the release order for OA-f-14's four gateway files (request sent 02:10Z). Before GO it
   reads on the live host whether `OG_TAXSMA_WORKBOOK_IDENTITY`, `MS_INGEST_IDENTITY` and `OTP_MAILBOX` name a scoped
   identity (`1.0.0_SA_CTO~O` msg 30365 item 5), and carries the CTO, COO and CVO halves.
2. `[3.0.0_SA_CVO~O]` rows Z-S57, Z-S58, Z-S59 and W29-S1 at the next channel compile.
3. `[1.0.0_SA_CTO~O]` reads at the analysis: step 4 and the non-email union rule (order record face).
4. `[2.0.0_SA_COO~AI on its next seating]` nothing owed. The parked close run and OA-t-1 / OA-t-3 stay parked.
5. Unowned at this seat: the five audit-archive integrity findings printed at startup.
