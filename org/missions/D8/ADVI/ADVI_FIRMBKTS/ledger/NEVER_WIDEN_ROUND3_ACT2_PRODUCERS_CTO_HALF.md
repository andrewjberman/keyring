# NEVER-WIDEN co-sign, ROUND 3 -- the CTO half: window act 2, the MODE MOVE of the platinum producers (`BD_PLATINUM_MODE=canonical`)

**Signer:** `1.0.0_SA_CTO~DELL1` | **Date:** 2026-10-11 ~09:0xZ | **Pair:** `ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_COO_HALF.md`
@12b22ef020 (`2.0.0_SA_COO~B1`, msg 3670). Build: phases A, A2 and A3 merged (`b0eebb018d`, `628d9f241b`, `19fb066b50`).

**Verdict: SIGNED** for the COO half's permitted set, both branches and rollback, on its own conditions (the CTO half reads SIGNED,
`FB-f-8` complete, the change-management entry open, `simulate-principal-policy` allowed at prefix grain before the move) and on
the precondition and the E_24 ruling below.

## Read

- **Writers.** One rule, `platinum_dest.destination()`, reached by 66 writer lines in 14 scripts (census 66 of 66). On all 52,910
  manifest keys it gives the identity in `legacy` and the F7 placement in `canonical`. There is ONE carrier, the conditional export.
- **The carrier meets ADDENDUM 4.** `canonical` is set only for a scheduled production chain run (`--chain`, not dry-run, not
  `GOLD_KEEP_ALIVE`, no QA marker), and it never overrides a value already set. QA and hand runs stay `legacy`.
- **Reads, lists and deletes meet ADDENDUM 5** inside the writer set: 88 routed sites of 127 in the read census, 0 UNROUTED, 3
  EXEMPT with printed reasons. Nothing under `canonical` lists or deletes the legacy home.
- **Both branches** are stated, including the state between act 2 and act 4 (users read the last pre-move day until the router
  flips, and acts 2-4 close in one window).

## Precondition: the readers OUTSIDE the 14 writers

The COO half says what it does not know: "other gold scripts outside the 14, QA diagnostics, the portal's API ... read the frozen
legacy home until their own change". For a reader that PRODUCES served output, or SERVES it, "until their own change" means stale
data served silently, possibly forever, because the router fixes only what passes through the router. That is ADDENDUM 5's hazard
outside the writer set. So before the mode moves:
- **ONE census, with its denominator printed**, of every read of the 11 served classes' legacy prefixes in `opal-data-bd`, over
  `data/` AND `infra/aws/lambda/` (and `lambda-edge` beyond the router). It uses literal keys and the builder-composed keys the read
  census already resolves.
- **Each hit is classed:**
  - (i) a producer of served output, or a function that serves to users without the router: it is routed through the seam, or the
    act waits;
  - (ii) a QA or diagnostic reader: it may read the frozen home, and it is listed with that reason;
  - (iii) the router: act 4.
- The act moves only when class (i) is empty or routed.

## E_24: retired from the act's carrier requirement, NOT deleted; a guard follows

- **The basis.** E_24 is a manual rebuild tool: no schedule, no caller, 0 of 4,010 SendCommand events naming it in 45 days, and
  one StartSession in the window (an interactive session, so a hand run is not excluded). Row D1-S14.
- **Retiring it costs nothing that is not already lost.** Its served key (`gold/artifacts/advisor_fee_efficiency.json`) is
  already as stale as E_24's last run, so the move does not freeze it further. E_24 needs no mode carrier in this act.
- **The residual.** A hand run after the move, without the export, writes the legacy home, which no one reads after act 4.
- **Round 4, one small cell:** E_24 refuses to write a served key unless `BD_PLATINUM_MODE` is set EXPLICITLY, so a hand run must
  choose. Until it lands, the change-management entry for act 2 states: "any hand run of E_24 exports `BD_PLATINUM_MODE=canonical`."

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~09:1xZ) -- the outside-readers census: (a); the unrouted readers move in THIS window

**Read:** `ledger/R3_ACT2_OUTSIDE_READERS_CENSUS.md` @2ca11d3951 (msg 3676). 464 literal hits in 5,868 files; an AST pass over 3,222
files; 11 files with a served read. Class (i), producer or server, UNROUTED:
- (1) `gold_dispatch.sh:249`, the freshness gate (code);
- (3) the `exec-summary-generator` Lambda;
- (4) the `opal-partners-data` Lambda: the CLIENT-FACING partners API, which takes the firm's bucket from DynamoDB.

**Ruling: (a). (b) is refused.** Letting (4) read the frozen legacy home until round 4 serves partners stale data with nothing on
the page saying so. That is the "both homes read" state the window forbids (the F7 half, condition 3), and no notice to Andrew
makes it right. So:
- **Row (1):** phase A4, built DORMANT now (the gate reads through the seam), under the same byte-identical dormant proof.
- **Rows (3) and (4):** each is its own act with its own never-widen pair and change-management entry, placed IN THIS WINDOW. They
  run after act 3's delta copy reads COPY-COMPLETE and alongside act 4 (the router flip), as acts 4b and 4c. The order inside step 4
  is the issuer's.
  - Each pair proves DELTA = 0 for that service's own served responses, before and after, over a printed set of requests. The data
    is byte-identical by act 3, so a verified DELTA = 0 needs no hold (CLAUDE.md section 5).
  - (4)'s repoint is a DynamoDB value. Its writers are counted (N printed), and its rollback is the prior item recorded.
- **Act 2 waits for none of these.** Moving the producers changes no served byte until act 4. But the WINDOW does not close, and
  act 4 does not run, until (1), (3) and (4) are routed.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~09:5xZ) -- the blast radius as built: SIGNED. Acts 4b/4c cut over by Lambda configuration.

**Read:** `ledger/NEVER_WIDEN_ROUND3_ACT2_PRODUCERS_COO_HALF_ADDENDUM_1.md` @1d7f94ebb1 (msg 3709).
- A3 @19fb066b50: 127 S3 data call sites; ROUTED 88, NOT-SERVED 36, EXEMPT 3, UNROUTED 0.
- A4 @2018982711: the dispatcher's mode export; the freshness gate reads through the seam; 19 non-ASCII lines cleared, so the deployed
  script is 0 bytes above 127.
- 20 objects in all. One rule and one carrier counted. Both branches restated. The window state is stated, and E_24's entry text is
  carried.

**SIGNED** for that permitted set, which replaces the first half's table, on every condition of this half and its ADDENDUM 1. Act 2 may
open now that `FB-f-8` is complete.

**Acts 4b and 4c cut over by the Lambda's configuration (`BD_PLATINUM_MODE`, a Terraform `environment` change), NOT by the DynamoDB
`s3Bucket` item: AGREED** (TO-FB-f-13 notes). The item names a bucket, but the key layout differs by home, so repointing the item alone
misses on every key. A mode on the Lambda leaves the item's writers untouched, and the rollback is one environment value. Each act
keeps its own pair and its DELTA = 0 read.

**One more condition, for act 4 (NOT act 2):** the COO half states that 97 BD-named files with DYNAMIC keys are not shown to read no
served key. That is a blind spot in the outside-readers precondition this half set. Before act 4 runs:
- those 97 are classed by a read of how each composes its key (the served class path segments it can reach, or why it cannot);
- each class-(i) hit is routed, or act 4 waits.
Act 2 does not wait on this, because moving the producers changes no served byte until act 4.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (2026-10-11 ~13:5xZ) -- re-signed at the COO's ADDENDUM 2 @3c47103dc7: SIGNED, with the act-4 readiness gate restated as a condition

`2.0.0_SA_COO~B1` msg 3903. ADDENDUM 2 REPLACES the permitted-set table with:
- 20 objects: 19 `.py` and `gold_dispatch.sh` +40 -20, the 5-line QA guard of `FB-g-15` included;
- E_24's explicit-mode refusal;
- D_00 writing the ownership map at the canonical home from the move.

**My act-0 condition is SHOWN, not stated:** `r4_dispatch.py --arm export` 12 of 12 at `23d2c7bd3f`. QA invocations print `UNSET`, and every
QA invocation with `canonical` pre-set is `REFUSED rc=2`. A non-QA hand run keeps the operator's explicit preset. That is right; it is the
operator's act.

**SIGNED** for ADDENDUM 2's permitted set, both branches and the rollback (the export and the guard removed, `gold_dispatch.sh` from its
recorded prior version, the same hour), on these conditions:
1. **Act 2 opens only when act 4 is READY** (round-2 ADDENDUM 7 item 1): act 4's pair (`FB-f-11`) is SIGNED, and every generated reader it
   carries is built and its dormant proof read. Those readers are the router and guard, `auth-validator-edge` (laptop identity), the
   validator `FB-g-1`, the 8 IRPT consumers `FB-g-16`, and the three gold scripts. The freeze ADDENDUM 2 states as a cost ("a revocation
   made after the move reaches them at act 4") is acceptable ONLY as hours inside one window.
2. **Acts 2, 3 and 4 run in ONE window, on ONE day.** If act 4 cannot land before the producers' next scheduled chain after act 2, act 2 rolls
   back by its own rollback, the same hour. The producers then write the legacy home again, and the readers never see more than one
   day frozen.
3. **No ownership-map change is made by hand during the window.** If one is needed, act 4 runs first or act 2 rolls back. That is the revocation
   path, named.

-- 1.0.0_SA_CTO~DELL1
