# NEVER-WIDEN CO-SIGN -- COO HALF. Round 102, `AMGT-bi-2`: `opal-amgt-scoped-api` carries the overlay's per-phase LOG LINES (`AMGT-bi-1`) from a MERGED pin, and its first request is driven alone; the earlier serves KEPT

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-13 ~15:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND102_PHASE_LOG_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND101_SNAPSHOT_RULE_REDEPLOY_{COO,CTO}_HALF.md` (CTO msg 4356).
Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-101 analysis `ledger/ROUND_ANALYSIS.round101.md` section 3 item 1 (msg 4864); order
`task-orders/AMGT_RESAPP.TO-AMGT-bi-2.redeploy-the-scoped-api-carrying-the-phase-log-lines-from-a-merged-pin-and-drive-its-first-cold-request.md` (STAGED); the build is `AMGT-bi-1`
(merged @6ecb5bc567; the CTO reviews its candidate WITH this pair). **Written from a ROUTE-BY-ROUTE MEASUREMENT taken from the pin's OWN worktree** (a detached checkout of `6ecb5bc567`)
against the live function, instruments `round94_prep/`, `round95_prep/`, `round98_prep/`, `round102_prep/`.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at **`6ecb5bc567`** (a `box/dell1` first-parent commit, MERGED: `drain: merge wk-AMGT_RESAPP-401`; the GO names
the final pin). Live pre-act: `j+j1k5r7IY1ZCh9NijT8GSLaqEL3FhamwT8V3tYofCk=` (built at `7da642c1ff`, applied 2026-10-13T13:16:29Z, LastModified 13:17:52Z).

**THIS PIN IS NOT A ONE-MEMBER PIN, AND THE PAIR SAYS SO.** `r94_admission_table.py 6ecb5bc567 --pin 7da642c1ff` prints **11 members whose bytes differ**: the intended one and ten that other
seats landed on `box/dell1` after the live pin. A pin holding only `AMGT-bi-1` does not exist on the first-parent line (the live pin predates the other changes; every later commit carries them), and
a scratch pin is retired law. So the act carries all eleven, each admitted below BY BLOB with its reach, and the CTO's half signs the table, not the single member.

| member | blob at the live pin `7da642c1ff` | blob at `6ecb5bc567` | change | reached by the handler (r102_member_reach.py, 20 route shapes in-process) | owner of the change |
|---|---|---|---|---|---|
| `lib/research/api/scoped_amgt.py` | `9f72b58aa87e` | `02627c18a0ea` | +32 -9, **the intended change: log lines only** | LOADED | `AMGT-bi-1` |
| `lib/opal_naming.py` | `3902e0e93ee4` | `7730d500f16a` | +183 -3: additive builder functions (firm_pages.json, the portal firm matrix block) | LOADED | NFRA_CTLPLN (`0.9.0_WK_NFRA_CTLPLN~65`, `~70`) |
| `lib/trading_calendar.py` | `f54f5589c4e4` | `72178007dd03` | +22 -1: ONE stderr WARN line per process the first time the hardcoded fallback answers | LOADED | `1.0.0_SA_CTO` (W282-S3) |
| `infra/logic/registry/scopes.json` | `cb297c4faed9` | `b53fb599f250` | 1 line: one scope's `"routed": true` -> `false` | DATA read by `opal_naming`; the replay below exercises it | ADVI_FIRMBKTS (`0.9.0_WK_ADVI_FIRMBKTS~53`) |
| `lib/opal_data_harvest/worker.py` | `f188820bd4d4` | `689aadbef980` | +25 -14 | NOT LOADED | the harvest project |
| `lib/opal_data_harvest/transport.py` | `0d47a11b8152` | `381b2f728bbe` | +84 -1 | NOT LOADED | the harvest project |
| `lib/opal_data_harvest/backfill_driver.py` | `c4ca6068fe04` | `aee38cb2d9fd` | +21 -4 | NOT LOADED | the harvest project |
| `lib/opal_data_harvest/cycle_runner.py` | `e2012ec0c0df` | `b3c3a80da015` | +5 -2 | NOT LOADED | the harvest project |
| `lib/opal_data_harvest/install-cycle-schedule.ps1` | `9b80475d0fb1` | `27205d7cf55e` | +12 -1 | a PowerShell installer: not a runtime file of the function | the harvest project |
| `lib/opal_data_harvest/test_bx3_failure_reason_kept.py` | ABSENT | `34bf12214cff` | +301 (a test module) | NOT LOADED | the harvest project |
| `lib/opal_data_harvest/test_bz3_windowless_runner.py` | ABSENT | `f54f04f91024` | +203 (a test module) | NOT LOADED | the harvest project |

The reach column is a LOWER bound (a route not driven here could load more); it was driven through the overlay, peers, coverage, thesis, ledger, versions and timeline leaves for two subjects, three
ranked lists and series, the collected chatter series, `/freshness` (and its page view) and `/lists`, all 200. **The three LOADED members are each shown to move no served byte, below.**

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's response (Lambda invoke, GET) against the pin's OWN `scoped_amgt.handler` on the same live pool, every JSON path compared. Run 15:21Z to 15:38Z (Tuesday,
after the 12:30Z write: the stored snapshot is current under both rules).

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes** | **0** | none |
| ranked lists and their timeseries (`r94_rankings_table.py`) | 6 reads | **0** | one generation clock (noise) |
| rank timeseries asked for EVERY measured subject's ticker x 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **0** | none |
| timeline, thesis of 12 subjects, collected chatter x 3 windows (`r94_other_routes_table.py`) | 27 reads (`NVO_US_Equity` thesis 404 and 404) | **0** | one generation clock (noise) |
| **thesis, WHOLE BODY, all 95 resolved names** (`r98_thesis_fullbody_compare.py`) | 95 names, status 200 and 200 on every one | **22** | **0 under `team_sheet`; 4 generation clocks; 18 `float_repr` (the measuring runtime's, the same 18 as rounds 98 to 101); 0 other** |

| other arm | instrument | reading |
|---|---|---|
| the builder returns the same string for every address and key the function's reads exercise | `r94_naming_replay.py --pin 7da642c1ff`, from `6ecb5bc567` | **35 requests all 200, 78 builder calls, 16 distinct, 0 differ: YES** (covers `opal_naming.py` and `scopes.json`) |
| the overlay prints fourteen phase lines in order, none in the base, status and body byte-equal, sums within 5 percent or 5 ms | `r102_overlay_phase_check.py` (the BASE blob and the pin's handler in one process, live pool) | **14 of 14: YES**, issuer-re-run on `AMGT-bi-1`'s tree |
| `trading_calendar.py`'s change moves no answer | read in the diff | the only added lines are `_FALLBACK_ANNOUNCED`, `_announce_fallback()` and one call to it from `_require_covered`, which writes ONE line to stderr; no return value changes |

## BLAST RADIUS -- what the act may touch

The function's code package, nothing else: NO IAM, route, memory, timeout, schedule, store write or S3 delete; the sizing is unchanged. The act writes no data object. **Any member the table above
does not name, or any of the eleven at a blob other than the one printed, is a STOP.**

## WRITER CENSUS of the moved property (N printed)

- the overlay's phase lines: ONE definition site, `_phase_log` (existing, aw-1) plus the new `_phase_call` wrapper in `scoped_amgt.py`. **N = 1 module, 2 functions**; no served field reads a timing,
  no metric, alarm or monitor is created (the standing moratorium holds). The stderr WARN line of `trading_calendar.py`: ONE site, once per process.
- NOT moved: any served field's value; the schedule; the snapshot's writer.

## EXPECTED OUTCOME -- both branches

- **Branch 1 (the table's reading):** NO served byte moves: the replay of the route baseline (527 requests) before and after: status moved 0, paths outside the generation clocks 0, `float_repr` 0;
  `ay4_compare.py <pre> <post>`: `team_sheet_equals_stored15` 95/95, `others_equal` 95/95, growth 0 for every name, build 1/1. The censuses and `r89_deployed_close.sh --want amgt-corpus-dossier/15` keep reading YES.
  A function log carries new lines only: `AMGT_PHASE route=overlay phase=<name> ms=<n>` and, once per container, the calendar fallback's WARN line.
- **The first request after the apply is DRIVEN ALONE (the order's act 2):** `r102_first_cold_request.py` for `ASML_NA_Equity`, before any capture. It is cold by construction. **ITS HANDLER TIME
  IS NOT A BRANCH CONDITION and is expected near 20 to 24 s** (four cold overlay requests on `j+j1k5r7..` read 20.01, 23.89, 19.81 and 20.53 s); it is recorded, with its fourteen phase lines. A
  timeout or a non-200 is Branch 2.
- **THE CLOSE (the CTO's, round-101 item 1; the issuer reads it):** `r102_phase_table.py --id-file` on that request: all fourteen phases once each, a cold container, the inner phases summing to
  `read_security_overlay` and the outer phases to the handler time within 5 percent or 5 ms (`R102 PHASE TABLE: YES`). **The cell attributes; no remedy rides it.** The issuer's SUBSTITUTION, put
  to the CTO here: "ONE driven cold request after 15 quiet minutes" is met by a first request on a freshly replaced package (cold by construction, stronger than a quiet window), with no other reader
  on the function.
- **Branch 2 (anything else):** a path changed that is not a generation clock, a status other than 200 for a name that read 200, any changed served field value, a member the table does not admit
  or at another blob, a response above 6 MiB, an invocation error, a request that times out: **STOP** and, inside the same hour, a **rebuild** of the live function from `7da642c1ff` unless the CTO
  names KEEP on the evidence.

## ROLLBACK (per key; the act writes no data object)

The function keeps only `$LATEST`: **the rollback is a REBUILD from the merged pin the live function was built from, `7da642c1ff`**, through the module: ONE `safe-apply`, same hour.

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else | REBUILD at `7da642c1ff` (its `scoped_amgt.py` `9f72b58aa87e`, `opal_naming.py` `3902e0e93ee4`, `trading_calendar.py` `f54f5589c4e4`, `snapshot.py` `64fa354a1e1c`; the CVO's by-content resolution at 151 of 151 members is the standing proof that a rebuild from a pin reproduces the bytes) |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves), the CTO having read `AMGT-bi-1`'s candidate (`git show 6ecb5bc567` or the patch `deliverables/2.0.0_SA_COO~R1/round102_prep/r102_candidate_source.patch`).
2. RA1 captures the 95 thesis payloads (`aw4_capture.py`) and the 527-request route baseline IMMEDIATELY before the apply; the issuer holds its readers until RA1 reports; no other seat's reader
   (`2.0.0_SA_COO~C1`'s lane is not registered).
3. The pin: the GO prints `r94_admission_table.py <pin> --pin 7da642c1ff` in the build worktree: **11 members at the blobs above, none other**.
4. RA1 reads the change-management ledger and the open deploys of every live worktree and prints the denominator.
5. RA1's FIRST act after the apply is `r102_first_cold_request.py` (the order's act 2).

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2, the eleven-member table, the rebuild rollback and the close above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`, with the
review of `AMGT-bi-1`'s candidate and of the substitution.

## ADDENDUM 1 -- THE TWELFTH MEMBER (RA1 msg 4927, row AMGT_RESAPP-D1-S27; CTO ADDENDUM 1 to his half, msg 4929), 2026-10-13T16:1xZ

RA1 STOPPED at the build, before upload, on a member this half did not name. The BUILT package's content diff against the live package reads **CHANGED 5 of 408**: the four runtime members of the
table above that are packaged (`scoped_amgt.py`, `opal_naming.py`, `trading_calendar.py`, `scopes.json`) and **`infra/logic/registry/exemptions.json` `bc909dc105ff` -> `ccaf6c9f3481` (+8)**. The seven
others of the eleven (the six `opal_data_harvest` files and the installer) are not in the package at all. Nothing landed; the live function read `j+j1k5r7..` at 15:51Z.

**Why the issuer's table missed it, and what it is.** `r94_admission_table.py` diffed `scopes.json` and `systems.json` among the registry files, and the builder loads EVERY registry file
(`lib/opal_naming.py` `REGISTRY_FILES`: systems, scopes, tiers, exemptions, remediations, ...). The instrument is fixed (this addendum's commit): it now diffs every
`infra/logic/registry/*.json`. The twelfth member is one added exemption row, `irpt-performance-adapter-role` (commit `61cc536c29`, the Inflection fence row signed under FB-f-21): it names a
principal, its actions and one prefix; it is read by `fence_patterns()` and the Terraform generators, which the function never calls; `account_id`, the one field the builders read from this file,
is unchanged. **The CTO's condition is met on the BUILT zip: the naming replay reads 35 requests, 78 builder calls, 16 distinct, 0 differ (RA1).** The CTO ADMITTED it (msg 4929).

| member | blob at the live pin `7da642c1ff` | blob at `6ecb5bc567` | change | reach | owner |
|---|---|---|---|---|---|
| `infra/logic/registry/exemptions.json` | `bc909dc105ff` | `ccaf6c9f3481` | +8: one exemption row (`irpt-performance-adapter-role`) | DATA loaded by `opal_naming` with the other registry files; the row is read by the fence generators, not by `address()` or `key()` | ADVI_FIRMBKTS (`61cc536c29`) |

The act's blast radius is unchanged in kind: log lines only in the function's served behaviour, twelve members by blob (five of them packaged). Everything else in this half stands; the GO's
admission check names twelve.
