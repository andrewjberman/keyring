# ADVI_BDPARITY W2 -- pre-flight, the wait ruling, and the pre-fire build (2113-2215Z)

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Seat:** `0.4.0_DS_ClientPlatform~Y` (fresh lane; the prior worker `~C` is dead, not respawned)
**Scope:** ADVI_BDPARITY, W2 only (Rule 27). Vendor egress authorised for W2 and nothing else.
**Authorisation:** Andrew-direct ~21:1xZ 2026-08-31, verbatim *"recs approved 1 and 2"*, carried by
`0.0.0_AB_MSTR` msg 90006, dispatched by `2.0.0_SA_COO` 90018. Record:
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260831_2110Z_OPEN_CALLS_SIX_RULINGS_GLOBALALARM_AND_THE_COMB.md`
**Commits:** `c5a45fb09e`, `5b7549df21`, `d435a4fd64` -- all **LOCAL** (`git ls-remote` 22:0xZ:
`origin/CLOUD = a30b2f2fbc8b9a18335fc74d67e570ac48b74128`). The LD-0367/0368 integrator gate blocked
the push and was right to: two commits sat local-not-on-origin and one was `1.0.0_SA_CTO`'s
`fd161f086f`, so the push would have published another seat's commit.

---

## Current State

**W2 has NOT fired. Exactly ONE vendor call has been made this session** -- the auth pre-flight at
21:44Z. Zero data calls, zero objects landed, zero bytes changed in S3.

The pull is **built, exercised, and waiting on the 00:00Z session mint** by ruling `2.0.0_SA_COO`
90040, confirmed 90067 ("proceed on `[MINT-FIRED]` without further instruction").

**Artifacts, all under `org/tier2_senior/0.4.0_DS_ClientPlatform~Y/deliverables/`:**
- `advi_bdparity_w2_runner.py` -- orchestrates the ALREADY-DEPLOYED
  `opal-assets-bd49f-reporting-pull`. Deploys nothing, changes no code, adds no schedule.
  Modes: `--plan-only` (0 calls), `--preflight` (1 auth call), `--verify-untouched` (0 calls),
  and the pull itself.
- `ADVI_BDPARITY_W2_BRONZE_BEFORE_IMAGE_20260831.json` -- criterion-3 before-image, captured
  before any W2 call: **18 objects, 18 versions, 0 delete markers, 0 non-latest.**

**The fire configuration, every operand pinned and sourced:**
```
  function  opal-assets-bd49f-reporting-pull   (live: DRY_RUN=0, Timeout=300, Mem=1024,
                                                CodeSha yO0R5JDSL86L1cp+V3qla1NsYWjvAL4lYi1drQvesIk=)
  q_start   2026-07-01   measured at BP1-2 probe table :19 `ASOF, QSTART`
  q_end     2026-08-28   RULED 90040(i); confirmed by measurement -- gold twr_daily's frontier IS
                         date=2026-08-28, there is no 08-31 partition
  pull_date PINNED by the caller, identical on all invocations (RULED 90040(ii))
  feeds     ["performance"]      inception  null for all 5,309 (safe per CVO 84169)
  cohort    5,309 in 45 chunks of 120
  projected 5,309 data + 45 auth = 5,354 vendor calls
```

**Code identity closed with this seat's own instrument, not the deploy record's claim:**
`git show HEAD:<puller> | sha256sum` = `c1278acb257e05b9f18b4ba194c6cae754976dbb55b149b4eaa79985ad483fb6`
== the L5 leg's pinned LF sha of the package downloaded from the RUNNING function. Hashed the INDEX
BLOB, not the autocrlf worktree checkout. The source read all session IS the running code.

**Mint watch:** persistent Monitor `bp5najxfk`, polling the secret's `LastChangedDate` every 4 min.
Baseline `2026-08-31T00:03:47Z` (session age 22.0 h at arm). It emits on EITHER terminal state --
`[MINT-FIRED]` on any change, `[MINT-LATE]` if 00:30Z passes unmoved -- so silence is not success.
Also measured: `RotationEnabled: null` -- the mint is NOT a Secrets Manager rotation, so there is no
schedule to read and the watch reads the VALUE.

---

## What was done

### 1. The auth pre-flight (the one vendor call)
Fired from the **Lambda's own plane**, not this box -- a local call would test a different egress IP
than the pull uses, which is a different question. Mechanism: `feeds: []`, exploiting that the auth
chain is unconditional and precedes the feed check:
```
  :406 _assert_firm_separation()
  :408 cookie = load_bd_session()
  :410 token  = get_clientview_token(cookie)   <- THE ONE VENDOR CALL
  :412 selected_feeds = resolve_feeds(feeds)   <- RAISES on the empty list
```
Result, requestId `455a0707-7f2a-4a86-b106-67237e3be95e`: `ValueError` at `:412`. **Reaching :412 is
only possible by passing :410.** A dead cookie fails at `:410` with a different named error or a
401, so it cannot surface as this error -- the probe discriminates and structurally cannot spend a
data call.

### 2. The run/wait judgement
90018's test was "run now only if the run can be SHOWN to fit the remaining window."
```
  window to 00:00Z ~2.08 h | run 1.67-2.06 h | margin 6-28 min against an UNMEASURED TTL
```
Not a fit -- a coin flip. Cost basis carried **two carriers**: the plan's 1.40 s/call and this
seat's own measurement of the P1 landing span in S3 (03:05:24Z -> 03:05:41Z, 17 s / 15 calls =
1.13 s/call). WAIT chosen and reported BEFORE the pull, per 90018. The mint is **exercised** -- the
session in use was itself minted 00:03:47Z today -- so waiting bets on a mechanism observed working.

### 3. Five relayed operands re-verified; all five wrong at the artifact
| # | relayed | measured |
|---|---|---|
| a | resume lists the `pull_date=` prefix | `land_bronze():325` builds a **bare date segment**. `pull_date=` returns 0 -> reads as "nothing landed" -> **re-pulls the whole census** |
| b | ~2.1 h at N=50 | `run()` :415 loops **one account per request**; N=50 is structurally unreachable in the deployed bytes |
| c | P1 bronze = 5 objects, 18 VersionIds | **18 objects, 18 versions**; 5 is the ACCOUNT count. (Self-contradicting as written -- 5 objects cannot have 18 VersionIds. Issuer owned this in 90040.) |
| d | ~72 invocations, ~4.1 h | those are the TWO-PASS figures; performance-only pass 1 is 36 (at 148) and 1.67-2.06 h |
| e | -- | pass 2 / SI-at-anchor is **not implementable** in the deployed puller: no SI-at-anchor request builder exists |

Plus two the handoff never named: **q_end must be pinned** (`expected_last_trading_day` returns
2026-08-31 today, 2026-09-01 after midnight) and **pull_date must be pinned** (defaults to `utcnow()`
PER INVOCATION, so a midnight straddle splits partitions and breaks the resume predicate and the
landed denominator at once). Both ruled in 90040.

### 4. Cohort re-derived at fire time -- 5 of 5 reproduce at a vintage the plan never saw
The pinned census partition was **rewritten by today's 12:45Z fire**: same key, LastModified
`08-30T05:09:10Z` -> `08-31T12:47:28Z`. Against the LIVE bytes:
```
  twr_daily accounts 7,370 | xref rows with both ids 5,375 | PULLABLE 5,309
  ours NOT pullable  2,061 | BD-pullable no our value    66
```
**The rewrite moved values, not membership.** Second carrier `in_0833_universe == True` = 5,309;
NOT called independent, because what computes it is unestablished. ID derivation `bd_account_id[3:]`
applied only after a prefix census proved **z08 uniform on 5,375 of 5,375**; positive control 4 of 5
P1 ids, negative control on a bogus id returns 0.

### 5. A false finding caught in my own instrument before it was reported
First pass read **67** BD-pullable-no-our-value against the plan's 66 and looked like a data defect.
It was `astype(str)` on a null column: 826 xref rows carry `schwab_account_id = None`, and `astype`
renders None as the STRING `"None"`, entering the set as a phantom key. Dropping nulls before the
cast returns **66**. The plan was right; the instrument was not. Guard + reason now in the code.

### 6. Controls, both arms, on the two checks that carry the acceptance criteria
```
  RESUME  positive  pull_date=2026-08-30 -> recovers EXACTLY the 5 P1 ids, set-equal
          negative  pull_date=2026-01-01 -> 0, so the predicate CAN return zero
          the false zero, EXERCISED:  real form -> 5 objects | relayed form -> 0 objects
  CRIT-3  positive  real before-image      -> 18 of 18 at pinned VersionId -> UNTOUCHED
          negative  one version_id mutated -> 17 of 18, names the key -> TOUCHED
```
Criterion 3 compares **by VersionId, never by count** -- a count is equal under a same-count
overwrite, so a count-based check cannot see the failure it exists to detect.

### 7. A correction taken against my own report
`2.0.0_SA_COO` 90067 caught that I called chunk 120 "zero budget cost" one paragraph after
introducing the auth-leg accounting that makes invocation count a vendor cost: 148 -> 36 auth calls,
120 -> 45, **delta +9**. The chunk stays at 120 (9 calls against 5,354 is noise; the timeout headroom
is worth more) but the justification was wrong, and it was sitting in the code comment -- the carrier
the next reader meets. Struck at `d435a4fd64`.

---

## Briefs written (DS role addition)

| Brief / artifact | Purpose | State |
|---|---|---|
| `advi_bdparity_w2_runner.py` | the W2 census orchestrator, every operand pinned | committed `c5a45fb09e`, extended `5b7549df21`, corrected `d435a4fd64`; exercised plan-only, zero calls |
| `ADVI_BDPARITY_W2_BRONZE_BEFORE_IMAGE_20260831.json` | criterion-3 before-image, 18 objects by VersionId | committed `c5a45fb09e`; verifier proven on a planted mutant |

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | A.3 exercise probe | PASS | forwarder RAN (own banner), not merely resolved |
| `comp-find --name` | `'*bd49f*'`, `'*reporting_pull*'` | PASS | located the puller tree + terraform; denominators printed (53 / 2 hits over 143,991 files) |
| `comp-find` content | `'twr_daily' data/assets/scripts/gold --band DEF` | PASS | `--band DEF` landed the one definition line (`TABLE_DAILY`) out of 42 hits -- the band did the work |
| `comp-find --files` | `'bdparity'` unscoped | FAIL | exceeded the 120 s Bash timeout on the full corpus; backgrounded. Scoped re-runs returned in seconds |
| comp-rail HUD gate | fired 2x | PASS | correctly denied a raw `find` and a `grep -r` and routed both to `comp-find` |
| `.tools/commit-gate.sh` | 3 runs | PASS | clean 1 of 1 each time |
| `.tools/safe-commit.sh` | 3 commits | PASS | risk-reflex clean (2 files vs 1,662 danger nodes); msg-verify MATCH each |

**What worked:** `--band DEF` collapsed a 42-hit content search to the single definition that
answered the question. The rail gate caught both raw searches and its suggested replacement was the
right tool each time.
**What failed:** an unscoped `comp-find --files` over the full 143,991-file corpus does not complete
inside the 120 s Bash timeout.
**Gap found:** the same query scoped by a pathspec returns in seconds, but nothing in the tool's
output suggests scoping when a sweep is running long -- the timeout arrives with no partial result
and no hint. Surfaced here, not chased (out of W2 scope).

---

## MCP traffic

**9 messages total.** Significant: **90018** the W2 dispatch (acked, `ack_messages`), **90040** the
rulings (q_end pinned, pull_date pinned, five corrections adopted), **90067** pre-fire confirmed +
the chunk-cost correction. Sent **90036** (pre-flight result + wait decision, 4/4 delivered) and
**90064** (pre-fire complete, 3/3 delivered). ACKs in from `1.0.0_SA_CTO` and `3.0.0_SA_CVO` on both.
Delivery ledger clean under LD-0480: every row addressed to this serial opened and acked BY this
serial; no foreign READ stamps.

---

## Surprise channel

**OBSERVATION x INERT, routed to `3.0.0_SA_CVO` (who mans the channel and grades this census), not
chased.** BD served bd `23221671` in P1 -- its 5.4 MB bronze object is in the before-image -- yet
that id has **ZERO rows in `dim_account_xref` across all five available vintages** (08-20, 08-21,
08-24, 08-27, 08-28), with positive control `z0813477111` present exactly 1x in each. Never present,
so not an xref regression, and it falls in none of the three census buckets.
**Consequence for how the number reads: 5,309 is the pullable-AND-LINKABLE population -- a floor on
BD-reachable accounts, not an enumeration of them.** W2's scope stays the 5,309.

---

## Blockers

**ONE, evidence-cited, and it is a named gate rather than a stall:** the pull waits on the 00:00Z
session mint, ruled by `2.0.0_SA_COO` 90040 and confirmed 90067. Evidence: secret `LastChangedDate`
= `2026-08-31T00:03:47Z`, age 22.0 h at 22:05Z; run 1.67-2.06 h against a 2.08 h window is a 6-28
minute margin on an unmeasured TTL. **Not a wind-down** -- every no-egress item the acceptance
criteria require is complete, and the watch fires without further instruction.

---

## Next Steps

1. **[`0.4.0_DS_ClientPlatform~Y`]** On `[MINT-FIRED]`: run `--preflight` against the NEW session
   (1 auth call), then the pull with `--pull-date` pinned to the fire date; report the four
   acceptance criteria with denominators. On `[MINT-LATE]`: report the finding, do **NOT** fire on
   the old session.
2. **[`0.0.0_AB_MSTR`]** `c5a45fb09e`, `5b7549df21`, `d435a4fd64` ride the next integration window
   -- this seat is gate-blocked from pushing the shared branch and did not override.
3. **[`3.0.0_SA_CVO`]** the `23221671` observation: whether the census denominator should be
   restated as a floor. Non-blocking on W2.
