# Session log -- 0.4.0_DT_ClientPlatform~C -- the v2.1.165 promote REFUSED as superseded, and the completion gate that could not see 122 of its own ledgers

**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY (refused), REMEDIATE, COORDINATE

Window: 2026-08-26 ~15:40Z seating -> 16:5xZ. Fresh lane instance (`~C`); no prior log for this
session. Predecessor context inherited from this seat's 2026-08-24 logs, which proved load-bearing.

## Summary

Seated, armed, and within four minutes received a `[DRIVE] RELEASE` dispatch carrying a sovereign
approval to push a staged portal PROD promote. **I refused it on measurement.** The promote had been
overtaken 30 hours earlier by the other fabric; executing the instruction would have rewound
production by five releases. COO withdrew the instruction, ratified the refusal, and re-tasked me to
sweep its own dispatches for the same defect class. That sweep found a second, structural instance
inside the deploy-completion gate itself, which I censused and fixed.

**NO PRODUCTION WRITE OCCURRED. NOTHING WAS PUSHED. NOTHING WAS MASS-CLOSED.**

## Work done

### 1. Startup (org/XXX.md Step 1b)
- Serial `NOT REGISTERED` at load (fresh lane); registered PID 39344. Lane `~C` inbox dir did not
  exist and was created by the watcher at arm.
- **/watcher: no pre-existing process for my serial** (10 other seats had one) -- a genuine fresh
  arm, not the orphan case and not the context-clear false-positive. Monitor **bss251a0s** armed and
  CONFIRMED running by `TaskOutput` (the only probe that observes a *consumer*). Proven end-to-end
  minutes later when it delivered the COO dispatch.
- CronList: no scheduled jobs. Zero crons at launch, per the seating brief.
- Noted and did not touch: the BASE serial `0.4.0_DT_ClientPlatform` holds 10 unread messages
  (08-24/08-25) and has **no watcher process**. Per-tilde isolation makes them undeliverable to me
  and draining a foreign inbox is the orphan-thief act as an API call.

### 2. THE REFUSAL -- the whole point of the session
COO 72452 relayed Andrew's `"all recs approved"` and ordered the staged merge `a239e4a9` pushed.
My own 08-24 log had bound me to a condition: *pushable-as-verified only while origin/DEV ==
d43b88c5*. **First act was `ls-remote`, before anything else.** Measured at 15:4xZ:

| claim in the dispatch | measured truth |
|---|---|
| v2.1.165 awaits promotion | **portal-v2.1.165 EXISTS**, peels to `d9a98bcc`, author `0.2.0_DT_PortfolioAnalytics~Z`, 2026-08-25T01:47:35-04:00, 41 commits/43 files |
| origin/PROD == 8a96c916 | **73afaccd (v2.1.169)** -- PROD advanced through .166/.167/.168/.169 on 08-25, three Andrew-direct |
| origin/DEV == d43b88c5 | **4ac152f8** |
| push the staged merge | `a239e4a9` is an ancestor of **NEITHER** branch (`merge-base --is-ancestor` FALSE both; POSITIVE CONTROL `d9a98bcc -> 73afaccd` TRUE, so the negative discriminates). Parked as `parked/v2.1.165-etf-promote-held-20260824` |
| `adviKeyRepoint.ts` ABSENT from PROD -- the scope fact that *justified needing Andrew's word* | **PRESENT.** It shipped 30h earlier |

**The premise that made the question worth asking had already been falsified by the answer.**

### 3. The dormancy census COO ordered -- run, and its SUBJECT had moved
COO asked me to re-verify the 2-day-old census "at the cut ref before you push." There is no cut ref;
the machinery is LIVE ON PROD. So I ran it against **live `origin/PROD 73afaccd`**, using the file's
own prescribed extract-don't-match recipe (that recipe exists because this one line produced five
miscounts across two seats):

**15 brace-opened rows against the ruled denominator 15 -- held 14 / structural 1 / FLIP 0.**
`ADVI_ROUTE_LIVE = true`, but `adviRead` gates on `if (!ADVI_ROUTE_LIVE || entry.state !== 'flip')`,
so **every ADVI key serves legacy. DORMANT IN PRODUCTION, confirmed.**
- CONTROLS: the identical extraction returns 14 and 1 for states that DO exist -> FLIP 0 is a
  MEASURED zero, not a broken retrieval. Negative control on an impossible state = 0.
- SECOND INSTRUMENT (differs from the grep pipeline): a python parse of the registry block ->
  15 rows, `{held:14, structural:1}`, FLIP rows `[]`. Agrees.
- Same census on `origin/DEV 4ac152f8`: identical. **No flip staged upstream either.**

### 4. Ledger closed SUPERSEDED -- and I destroyed a record doing it, then restored it
`20260824T1241Z_...` -> **SUPERSEDED** (`_is_terminal_status` verified True; sentinel removed by
`close`, so prose and sentinel AGREE and DRIFT-A cannot fire). All six legs carry supersession
evidence and five lead with **NOT PERFORMED**. `SUPERSEDED` is an EXISTING token at
`deploy_ledger.py:139` -- no schema value minted.
⛔ **MY OWN DEFECT, CAUGHT BY READING THE DIFF I WAS ABOUT TO COMMIT:** `close-leg` calls
`_write_entry()`, which re-renders the .md from the sentinel JSON. The sentinel holds only
legs/log/status, so **the first `close-leg` silently deleted 139 lines of hand-authored record** --
the CTO scope ruling, the 100x near-miss, the local-state caution, the tool-refusal evidence.
Recovered from git HEAD and restored in full; verified each section present by name before commit.
I noticed only because `--stat` said `50 insertions, 139 deletions` on a file I thought I was adding
to. **If I had not read the stat I would have committed the deletion of the record that proved my
own refusal was correct.** Commit `244c525f51`.

### 5. THE SWEEP (COO re-task 72510) -- and a predicate I had to throw away twice
Population: 186 files -> **186 distinct Msg-IDs -> 71 distinct dispatches** (one body to N inboxes
inflates the file count). Two-axis filter (cites a RECORD artifact AND orders an act on deployed
state): **26 of 71**.
⚠ **My first pass flagged 139 of 186 as portal/cross-fabric-shaped. That was the common-noun trap** --
`portal` matches the bucket name `opal-data-portal-v2`, and `PROD`/`fabric` are native vocabulary
here. Discarded and re-cut. **A true count over the wrong population reads exactly like a right one.**
I hit the same trap a second time on the ledger sweep and discarded that column too.

**FINDING A:** COO's 15:37Z card carried FOUR recs under ONE sovereign word. **Two were
record-sourced and both died inside 25 minutes** -- mine by measurement, `freshguard` by COO's own
retraction. One was grounded at source (CVO 72456), one was Andrew-verbatim. **The card is the unit
that failed, not either call.** COO adopted: a card carrying multiple recs states its evidence basis
PER REC.

### 6. FINDING B -- the gate-bypass detector had its own gate-bypass
`_unindexed_open_ledgers` globbed ONE filename suffix, so its population was a naming convention:
**551 .md | 429 matched | 122 STRUCTURALLY INVISIBLE | 74 of those non-terminal | `check` reported 1.**
Seven differ from a covered ledger by **a single character** (`-deploy_completion.md`, hyphen where
the glob wants an underscore). Same lesson as Rule 22a's never-resolve-by-filename, measured inside
the completion gate itself.

⛔ **AND THE CENSUS CORRECTED MY OWN HEADLINE, WHICH COO HAD ALREADY ACTED ON.** 74 is a COVERAGE
number, not a DEFECT number, and I shipped it without that label. Of the 74: **51 are not deploy
ledgers at all** (44 are benchmark approval records), 15 have no leg manifest, 8 are deploy-shaped --
and 19 of the 74 carry closure evidence in grammars the predicate cannot parse. **True residual: 2
genuinely open**, one self-declaring `OPEN` and invisible for **65 days**, one with a single open
VERIFY leg (nothing half-landed). Led my report with the correction.

### 7. The fix (COO 72557 (b); CTO 72552 ruled mechanism-fix, no law text) -- `ec3639cad5`
Five changes, each STRUCTURAL rather than an enumerated spelling -- that discipline is the module's
own, whose comments record it being burned three times by readers that enumerated the spelling their
author had just seen: (1) strip leading non-alphanumerics so a status-emoji cannot defeat the token
check; (2) accept `**Opened/closed:**`; (3) glob `*.md` and filter by CONTENT via
`_is_deploy_ledger_shaped`; (4) a 4th status pattern for an UNTERMINATED bold span (ordered LAST so
1-3 keep first refusal); (5) `_LEDGER_TITLE_PAT`.
⛔ **I did NOT simply widen the glob, which was the obvious fix and is a trap:** ~188 non-ledger
records would then report as "open or malformed" -- trading a silent miss for a large false RED, the
over-reaping inversion. Result: **551 scanned | 483 ledger-shaped | 8 reported (was 1)**, and a
caller's note to COO that 5 of the 8 are noise until their records are fixed, so the `--red` bias is
a decision to make *before* arming, not after.

### 8. Open TO, status measured rather than read
`OPAL_ADVIPOINTERS.P4-PROMOTE-49F` (8d, PENDING) executes on DE's P4R-5 flip handoff. **FLIP is 0/15
on `origin/DEV` as of today** -- DE has not flipped, so there is nothing to promote. Correctly
pending, genuinely blocked upstream, NOT stalled work. Its own subject file records the 49F publisher
as a DISABLED Scheduler entry frozen since 2026-08-21.

## Deployment Sequence + Verification (DT role addition -- ACTUAL output)

| step | result |
|---|---|
| /prod-deploy | **NOT ENTERED.** Halted before Step 0 on the payload/ancestry measurement. |
| ls-remote origin DEV/PROD | DEV `4ac152f8`, PROD `73afaccd` -- the reads that killed the dispatch |
| ancestry | `a239e4a9` -> PROD FALSE, -> DEV FALSE; POSITIVE CONTROL `d9a98bcc` -> PROD TRUE |
| tag peel | `portal-v2.1.165^{}` = `d9a98bcc` != `a239e4a9` |
| Rule 19 | portal main tree on **DEV** throughout; worktree list = main tree only |
| local PROD | `73afaccd` == origin/PROD -- the 08-24 deliberate-local-state trap is DISCHARGED |
| PROD push | **NOT EXECUTED, AND CORRECTLY SO** |

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| to-check.py | `--all --assignee 0.4.0_DT_ClientPlatform` | PASS | `--all` load-bearing; 1 PENDING TO, blocked upstream |
| deploy_ledger.py | `close-leg` x6 / `close` / `check` | PARTIAL | close+check PASS; **`close-leg` destroyed hand-authored prose -- see §4** |
| git ls-remote / merge-base / rev-parse | portal refs + tags | PASS | the APPLIED plane; the whole verdict rests here, never on a local ref |

**What worked, and it is the only reason this session did not end in a production rewind:**
**re-reading `ls-remote` at the moment of the act rather than trusting a hash in a message** -- the
same habit my 08-24 predecessor logged as the thing to keep. It has now caught a stale pin in a
brief, a stale-verification window, and a sovereign-approved instruction to rewind production.
**A verification does not announce its own expiry, and neither does an approval.**

**What I got wrong:** (i) I told COO to stand MSTR down as push-holder with no basis -- I read my own
08-24 log back as a measurement two days later, the exact defect I was reporting, committed inside
the message reporting it. MSTR was never structurally in that push path. (ii) I shipped "74" as a
headline without labelling it a coverage number, and COO acted on it within four minutes. (iii) I
destroyed 139 lines of record with `close-leg` and caught it only from a `--stat` line.

## Blockers

**NONE for this seat.** The dispatch that would have been a blocker was withdrawn. The one open TO is
blocked on an upstream flip that measurably has not happened.
**QUEUED, NOT DELIVERED:** `2.0.0_SA_COO` and `3.0.0_SA_CVO` went offline before my completion report
(72599/72600 QUEUED; `1.0.0_SA_CTO` 72601 DELIVERED). The fix and census await COO's read.

## Current State (zero-prior-context handoff)

- **portal origin/PROD = `73afaccd` (v2.1.169)**; origin/DEV = `4ac152f8`. Portal main tree on DEV.
  **No promote is pending or staged.** `a239e4a9` is parked and must never be pushed.
- **ADVI on PROD: LIVE MACHINERY, DORMANT ROUTE** -- 15/15 rows, FLIP 0, two instruments. Andrew's
  2026-08-21 flip hold is unaffected and unbreached.
- **Ledger `20260824T1241Z_...` CLOSED SUPERSEDED** (`244c525f51`, LOCAL).
- **`deploy_ledger.py` FIXED** (`ec3639cad5`, LOCAL) -- gate now sees 483 ledger-shaped of 551 and
  reports 8. **Two genuinely-open ledgers surfaced for their owners and NOT touched by me:**
  `20260622T1630Z_cotetl_c00snapshot_servedaua_deploy.md` (self-declared OPEN, 65 days) and
  `20260804T0505Z_mdpf-emit1-...` (`0.2.0_DS_PortfolioAnalytics`; one open VERIFY leg -- the shape
  the HELD doctrine exists for, recommend a hold with a named re-read event).
- **BOTH COMMITS ARE LOCAL** and ride integration; `ls-remote` not read for them, so do not report
  them as on origin.
- Monitor `bss251a0s` live. Broker status current.

## Next steps

- [`2.0.0_SA_COO`] Read 72599: the 74->2 correction, the fix, and the `--red` bias decision BEFORE
  the next cycle (5 of 8 are record-grammar noise). The vocabulary question is yours: is `LANDED`
  terminal, does a leading qualifier count? I deliberately did not extend the token list.
- [`3.0.0_SA_CVO`] Verify `ec3639cad5` + `244c525f51`. The sharper target is my coverage-vs-defect
  mislabel, not the fix.
- [`0.2.0_DS_PortfolioAnalytics`] Your `mdpf-emit1` ledger, 22 days, one open acceptance leg.
- [owner of `cotetl_c00snapshot_servedaua`] Open 65 days, previously invisible.
- [this seat] `P4-PROMOTE-49F` remains pending on DE's flip handoff. Do not pre-promote.
