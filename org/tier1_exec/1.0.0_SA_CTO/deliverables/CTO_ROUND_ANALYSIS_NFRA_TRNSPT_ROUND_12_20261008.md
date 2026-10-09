# CTO ROUND ANALYSIS -- NFRA_TRNSPT round 12 (FWD-10 AI investment commentary thread)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-08 ~22:5xZ | **Input:** `2.0.0_SA_COO~T2` msg 1838; packet
`org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R12_CLOSE.md` @21eec739ed. The CVO's slug is not yet in; this analysis
is written on the COO packet and is revised if the slug differs.

## The one decision asked: is C-WIPE-GATE recorded passed?

**RULING: YES. C-WIPE-GATE is PASSED at current code.**
- `NFRA_TRNSPT.TO-TR-w1` is `complete`, with its proof VALID (d15a6e9951, 2026-09-30). TR1-w1-AC1 is the planted-token test that the
  PRD's C-WIPE-GATE names.
- The wipe changed after that: round 11's allowlist (256c5a4386). So this seat re-ran the gate at HEAD 49c04cd4b2:
  `python -m pytest data/transcripts/scripts/tests/test_wipe_planted.py -q -p no:cacheprovider`. Result: **13 passed**.
- Its result is "the planted classes were removed". That is not "no PII remains" (PRD C-WIPE-GATE).

**What this unlocks:** the first real Kimi K3 call, under Andrew's 2026-09-30 word (PRD C-KIMI). The input is the abstract fields only.
Any second use of the vendor needs his word for that use.
- **Measured state:** gold holds 0 objects, so the first draft is the no-precedent draft.
- **Not decided here:** gold body text sent as precedent waits on gold existing. When it does, the gate is re-run at that HEAD.

## Enrichment list (round 13)

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | D2-S6: the drafter emits `generated_at`, matching ~V2's ticket contract | the H6 contract test passes; the trace reaches H6 without a dead letter |
| E2 | The first real Kimi call: one no-precedent draft from abstract fields | one call, logged by request id with no prompt body; the draft lands as a ticket DRAFT that only Opal can see |
| E3 | The journey trace re-run H2 to H6, with the gate real (not simulated) | every hop reads OK, or names the one hop that breaks |

H1 (the analysis report's READY event, from ~P2) and H5 (the ticket service route, ~V2's FWD-6 workstream) stay stubbed until their
owners land them.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-08 ~23:0xZ) -- round 13 drain-end (`~T2` msg 1862, `R13_CLOSE.md` @ab11f097f3) and the D2-S7 ruling

**Measured, from the packet:** E1 to E3 are met on the stub. One Kimi K3 call was made on synthetic inputs and returned a no-precedent
DRAFT of 3,908 characters with no planted identity. D2-S6 (`generated_at`) is fixed. **Andrew's 2026-09-30 word for the first call is
now spent:** every further call needs his word per use (PRD C-KIMI).

**D2-S7 RULING: household is NOT required on a ticket the `svc-commentary` principal creates.** It is not sourced either.
- **Why:**
  - C-KIMI limits the commentary path to abstract fields with no client identity, and the household is client identity. Giving the drafter
    a household source would widen what it holds for no reader's benefit.
  - The `analysis_request` definition's `household` question (`lambda_function.py:86`, `required: True`) is the human form's question
    (FWD-1).
- **The rule:** a type's `required` set is evaluated per creating principal. The `svc-commentary` create requires `report_request_id`,
  `draft_commentary`, `generated_at` and the firm, and nothing else. Anyone opening the ticket reaches the household through
  `report_request_id`, by IRPT's firm-fenced read.
- **Owner:** `2.0.0_SA_COO~V2` (C-TYPE: data, not code), one cell in its F10 workstream.
- **Order with the F10-d-1 deploy:** leg D (CTO half @a4ccfb4439) may ship first, because the widening is unreachable until leg M. Leg M
  (the mint) waits for this fix to be live, or real reports dead-letter on the first call.
- **Direction:** under C-PACKAGE (TCKT_VNEXT ADDENDUM 2) the commentary lands on the REQUESTING ticket, which already carries the household
  from the human form. The separate svc-commentary ticket is the interim path.

**Act only Andrew can do (cited):** a standing word for one Kimi call per Analysis Request in this workflow. Citation: PRD C-KIMI ("any
other use of a vendor call carries his word per use") and CLAUDE.md "NEVER call an external vendor API without Andrew's explicit per-use
word". Without it, the automated workflow stops at the commentary step on every request.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (2026-10-08 ~23:3xZ) -- FWD-7 graded REALIZED (`~T2` msg 1946)

**Read by this seat on the served log** (`/aws/lambda/outlook-global-transcripts-pull-lambda`, filter `window_days`, since 23:29Z):
`MAIL-PULL-FIRE run=20261008T233013Z window_days=7 listed=12 admitted=0 landed=0 skipped_known=0 list_refusals=0 silver_rows=0 held_out=0`.
This is the scheduled fire, not an ad-hoc one. The C3 ledger closed @7b234d0031.

**FWD-7: REALIZED**, by round 4's test ("REALIZED when L5 closes").
- `admitted=0` of 12 listed is the admission filter's own verdict on tonight's mail. It is not an outage, and it is not graded here.
- The mail_pull hold lift is MSTR's act, and ~T2 has told it.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 3 (2026-10-09 ~02:3xZ) -- CVO compile of rounds 12-14 (msg 2200, `ADJUDICATION_v9.md` @8e9c5eee4c)

- **CORRECTION, adopted:** round 13's first Kimi call rested on Andrew's **2026-10-07 Dell-egress word**, not the 09-30 word this seat
  cited in ADDENDUM 1.
- **Either way, the live calls of the AWS Lambda (`outlook-global-commentary-draft-lambda`) need his standing word** (CALL 1). That stays on
  the act list.
- **The Apple exception is APPROVED by the CVO**, with 2 residual contexts named. Round 12's curated list closes.
- Rows are held until TO-TR-j15 is terminal; the slug follows it.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 4 (2026-10-09 ~03:2xZ) -- round 16 drain-end (`~T2` msg 2290, `R16_CLOSE.md` @5346c6bccc)

**Measured:** TR-h16 merged (R16-H16-OK, drain 367 passed, MAY-CLOSE). Two served runs were not run and are carried: the Apple re-write and
the 365-day backfill. The CVO's slug for rounds 15 and 16 is owed to this seat; this addendum is written on the COO packet.

**Round 17 enrichment (ONE issuance):**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | TR-c-17: complete `commentary.tf` (row D2-S8) | the 5 env names are present; the composition and svc-commentary secret reads are in the role policy; addresses are `address()` output; plan printed. Then the Lambda's apply pair |
| E2 | The Apple re-write, run by `0.7.0_AE_CloudOps~DELL2` under its existing approval (CVO msg 2200) | stored bytes re-read: Apple turns present, PII sweep 0, held_out unchanged |
| E3 | The 365-day backfill, run by `0.7.0_AE_CloudOps~DELL2` under the pair (CTO half @a22adefb0e, AMENDMENT 1 @9160ba58fc) | simulation passes first; listed, admitted and gold rows printed (counts only); prior silver VersionIds committed before |

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 5 (2026-10-09 ~06:5xZ) -- row NFRA_TRNSPT-D2-S9: the backfill's precedent set stays EMPTY

Asked by `2.0.0_SA_COO~T2` msg 2722. Both served runs are DONE:
- the Apple re-write is CLEAN (@38c9f3967f);
- the 365-day backfill read on the stored bytes @ff31f846ed: listed 453, landed 24, silver 6 held out 6, gold 0, inside the signed write set.

**RULING: keep it empty.** The residual check withholds every row, and at least one of those rows holds a real name, so it is working as a privacy
guard. Widening the allowlist to produce precedent would trade privacy for drafting input that FWD-10 does not need. A widening is opened only
when a FWD needs precedent, and it needs a privacy review approved by the CVO (the Apple precedent). None is ordered.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 6 (2026-10-09 ~08:2xZ) -- round 17 carried runs closed; what NFRA_TRNSPT's next round covers (`~T2` msg 2890)

**Read:** `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R17_CARRIED_RUNS_CLOSE.md` @b85c74058c.
- a17 is COMPLETE: Apple has 17 turns in 9 meetings.
- b17 is DONE: gold 0 rows, D2-S9 ruled empty (ADDENDUM 5). Its proof is owed by the applier.

### Grade state of the endpoint (PRD v0.3, 11 FWDs)

| FWD | state | basis |
|---|---|---|
| FWD-7 | **REALIZED** | ADDENDUM 2 |
| FWD-10, FWD-11 | **MOVED** to IRPT_ANLREQ (msg 2460) | graded there (commentary FWD-3, package FWD-1). Not graded in NFRA_TRNSPT |
| FWD-1 to FWD-6, FWD-8, FWD-9 | **UNGRADED** in this seat's record | no grade on this fabric's record. `STATUS.md` names partial evidence (FWD-1's trace, FWD-8's second reader with no principal) |

**NFRA_TRNSPT is NOT at CLOSED:** 8 FWDs carry no grade.

### Ruling: round 18 is a COVERAGE round, then the next rectangle

1. **Cell TR-g-18 (`~T2`, read-only):** one evidence row per ungraded FWD (1-6, 8, 9). Each row names the act that exercises it now, on demand, with its
   invocation and its read. Where no act exists, it names the missing hop. Output: `R18_COVERAGE.md`. **This seat grades each row from it**, REALIZED or
   NOT REALIZED with the hop, in the analysis that answers it.
2. **Two known gaps are cut in the same issuance, because they need no coverage read to know they are open:**
   - **FWD-8:** the second named reader gets its AWS principal. Andrew named the readers; the principal is minted by name through `name()`, under a
     pair. It is a laptop identity-allow-list act if dell2 cannot write it (dell2 IAM limits), so the issuer routes it through MSTR.
   - **FWD-2:** the Research Meeting's arrival is read from the ordinary scheduled run, not a seat-started one. The schedule is read by name.
3. **FWD-10 and FWD-11 get no NFRA_TRNSPT cell.** A PRD addendum marks them MOVED at the next ENDPOINT change. It does not need its own re-sign now.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 7 (2026-10-09 ~08:3xZ) -- the Teams pull was never applied (`~T2` msg 2903, `R18_FWD2_SCHEDULED_READ.json` @3f7583537b)

**Measured by `~T2`:**
- `pull.tf:1` is DESIRED ONLY. `teams-global-transcripts-pull-lambda` and its hourly rule do not exist (153 rules scanned; the outlook pull is live as the
  control).
- `research_meeting` is allowlisted and has never landed.
- **One missing hop is shared by FWD-1, FWD-2 and FWD-3's new-landing arm.**

**RULING: round 18 cuts the apply, in two steps under one pair.** It is not deferred to round 19.

1. **Step 1, a preconditions read (no write), which gates step 2.** The file's own header names the gates:
   - S04: the gateway's transcript tools are live. Read one tool call by name.
   - S05: the stored sign-in's lifetime is measured. Print the secret's token expiry, never its value.
   - The KMS path: the writer role's `aws_kms_grant` on the transcripts key needs `kms:CreateGrant`. Dell2's key access is Decrypt-only (msg 2445), so
     simulate first. A refusal routes to `0.0.0_AB_MSTR~DELL2` as a laptop act, and the step names it. It is never worked around.

   Any precondition unmet means STOP, with the missing one named.
2. **Step 2, the apply:** `pull.tf` through `safe-apply`, by `0.7.0_AE_CloudOps~DELL2`.
   - The names are `name()` output (the file already records them).
   - The plan carries pull.tf's resources only. Any other line in the transcripts root means STOP (the shared-root rule @29a9a2c684).
   - **The writer is a third principal.** It writes only `teams/transcripts/*` and is not added to the reader variable. The pair names it.
   - It has its own cron (C-MORATORIUM): no alarm, no SNS.
3. **The proof is FWD-2's: the first scheduled fire that lands `research_meeting`.**
   - It is not a wait. A seat invokes the function once at apply to prove the hop, and the scheduled fire is the acceptance (the organic arm).
   - FWD-1 and FWD-3's new-landing arm are re-read on the same landing.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 8 (2026-10-09 ~08:5xZ) -- grades on the round-18 coverage (`~T2` msg 2936, `R18_COVERAGE.md` @ed84ea7977, 8 of 8 rows)

### Grades

| FWD | grade | the hop that is missing (from the coverage row) | where it is cut |
|---|---|---|---|
| FWD-1 | NOT REALIZED | the Teams pull (no scheduled landing) | TO-APPLY-p18, GO under half @b972f130c9 |
| FWD-2 | NOT REALIZED | the Teams pull, and the Research Graph 403 | p18, plus round 19: the 403's permission read by name |
| FWD-3 | NOT REALIZED | the new-landing arm rides the Teams pull | p18 |
| FWD-4 | NOT REALIZED | the "expired" cause is not reachable by any act | round 19 cell |
| FWD-5 | NOT REALIZED | no analyst route: the scoped wiped-silver reader role does not exist | round 19 cell, after W1-S7 is fixed (below) |
| FWD-6 | NOT REALIZED | no act exists (PowerPoint intake) | round 19 cell |
| FWD-7 | REALIZED | -- | ADDENDUM 2 |
| FWD-8 | NOT REALIZED | TO-APPLY-a18 is at the laptop (half @f2ec32dea4) | the laptop through MSTR |
| FWD-9 | NOT REALIZED | no act (one question across meetings, updates and commentary) | round 19 cell |
| FWD-10, FWD-11 | MOVED | -- | IRPT_ANLREQ |

### The two privacy rows

1. **W1-S8 is ARMED (disarm owner `~T2`).** `read_meeting.py` prints held-out Research rows that `research_read.py` withholds. That is a reader-side leak:
   a seat could copy withheld content into a log, which FWD-8 forbids.
   - **Ruling:** both readers call ONE shared holdout filter (the one `research_read.py` uses). `read_meeting.py` is fixed in round 19 before its next use,
     with a test that a held-out row is never printed.
   - **Until the fix lands, `read_meeting.py` is not run** against Research silver.
2. **W1-S7: Teams silver is UNWIPED while PRD C-TIERS says silver is wiped.**
   - **The exposure today is bounded.** The narrower wiped-silver reader does not exist (coverage row FWD-8 (b)), so only the named original readers can
     read Teams silver. This is a spec breach, not a live leak.
   - **Ruling:**
     - Round 19 re-runs the wipe over the existing Teams silver objects. That is a rewrite of served objects, so it needs a pair whose blast radius names
       every key.
     - From the p18 apply on, new silver lands through the wipe (COO half: "the same wipe for silver").
     - **No narrower reader role (FWD-5) is created until every Teams silver object reads wiped.**

### Enrichment list (round 19)

1. W1-S8: the shared holdout filter in `read_meeting.py`, plus its test.
2. W1-S7: the re-wipe of existing Teams silver, under a pair.
3. FWD-2: the Research Graph 403, read by name for the permission it lacks.
4. FWD-4: an on-demand act that reaches the "expired" cause.
5. FWD-6: PowerPoint intake, one file kept byte-exact.
6. FWD-9: one question answered across meetings, updates and commentary. Read-only, by a named reader.

FWD-5's reader role follows item 2. At most three mechanical criteria per build order.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 8.1 (~08:5xZ, `~T2` msg 2941): correction -- new Teams silver does NOT land wiped

ADDENDUM 8's line "From the p18 apply on, new silver lands through the wipe" rested on a false COO line. `parse_silver.py:5-6` reads "No PII wipe on transcripts
this round".

**RULING: (a), apply p18 now, with three conditions.**
- **Why (a):** Teams silver holds the same content as bronze, which is the raw tier. Both are readable only by the named original readers through the key
  policy, so unwiped new silver adds no reader and no reach. FWD-1, FWD-2 and FWD-3 need the pull.

**Conditions:**
1. **The narrower-reader gate is unchanged and is now explicit.** No principal outside the named original readers is granted on `teams/transcripts/*` until both
   of these hold:
   - every existing Teams silver object reads wiped (the W1-S7 re-wipe);
   - the pull wipes on landing.
2. **Round 19 adds the wipe-on-landing to the pull as item 2b,** with a planted-token test (the C-WIPE-GATE pattern), before FWD-5's reader role.
3. **PRD C-TIERS is breached until item 2b ships.** The breach is named in the NFRA_TRNSPT record and is not silent: row W1-S7 stays OPEN.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 9 (2026-10-09 ~09:1xZ) -- row D2-S10: the Teams pull's transport is a STUB and its secret is absent (`~T2` msg 2981, @353bf58b5b)

**Measured by `~T2` at TO-APPLY-p18 step 1** (stopped there; the KMS limb passed):
- `teams/global/gateway-token` does NOT exist.
- `gateway_client.py:5,:81` `GatewayTransport` is a STUB ("each method raises GatewayToolsAbsent ... no network call").
- Applied as written, the function would run hourly and land nothing. **p18 stays HELD.**

**RULING (REC adopted): a round-19 amendment cell, LOCAL build, before p18 re-runs from step 1.**
1. **A real Teams gateway transport** on the mail pull's proven pattern (`outlook/gateway_mail.py`).
   - Tests run against a recorded fixture of one allowlisted meeting.
   - It makes no live call in the cell. The first live call is p18's step-1 S04 read.
2. **`pull.tf` reads the bearer by data source,** as `mail_pull.tf:28-30` does.
   - **The secret's NAME is the gateway owner's to give** (NFRA_OPLGTW). It is NOT chosen between `gateway/teams/bearer` and `gateway/transcripts/bearer` by guess.
   - `~T2` asks the owner through `0.0.0_AB_MSTR~DELL2`. The cell carries the name as a variable until the answer lands.
   - **If no Teams bearer exists, the owner's minting of it is the precondition.** It is named on the row with its owner. It is never worked around by
     reusing the mail bearer.
3. **p18 re-runs from step 1 on the new build:** S04 is a live tool call, S05 is the bearer's expiry, and the KMS limb was already passed. The CTO half
   (@b972f130c9, AMENDMENT 1) binds the rebuilt zip by its sha256 in the ledger. No new half is needed, because the blast radius is unchanged.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 10 (2026-10-09 ~09:4xZ) -- round 19 drain end (`~T2` msg 3009, `R19_CLOSE.md` @a32646d928)

Written on the COO packet; it is revised if the CVO's slug differs.

**Read:**
- 5 cells drained (406 passed).
- **W1-S8 is DISARMED:** both readers use the shared holdout filter.
- The re-wipe tool and wipe-on-landing are built. The served re-wipe needs its pair.
- The FWD-4, FWD-6 and FWD-9 acts are built.
- **TR-r-19: the Research Graph 403 is meeting MEMBERSHIP, not a scope.**

**Rulings:**
1. **The Research 403 is an act only Andrew can do.** The reading account must be added to the Research Meeting series, an entitlement in his tenant that
   no seat holds. It is listed for him with that citation: CLAUDE.md, spend, contracts or entitlements beyond his grants. FWD-2's Research arm waits on it,
   and the other series do not.
2. **The served re-wipe of existing Teams silver (W1-S7) is cut in round 20 under a never-widen pair.**
   - The blast radius names every key and its prior version id.
   - Rollback is a `copy-object` of each prior version.
   - The planted-token test is run on the rewritten bytes.
3. **The FWD-4, FWD-6 and FWD-9 acts are EXERCISED in round 20,** each once on demand, with the read recorded. This seat grades each from the read. Built is
   not REALIZED.
4. **The transport cell (ADDENDUM 9) waits on NFRA_OPLGTW's bearer name and route contract,** through MSTR. That is a named owner and condition, not a silent
   wait.

### Round 20

1. The W1-S7 re-wipe pair and its apply.
2. The FWD-4, FWD-6 and FWD-9 exercise reads.
3. The transport cell, when the owner's answer lands.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 10.1 (~09:4xZ) -- the CVO's slug for rounds 17-19 (msg 3023, `ADJUDICATION_v10.md` @67046ae880): ADDENDUM 10 stands

The slug matches the COO packet ADDENDUM 10 was written on (3 dismissed, ARMED 0). Its three items are already ruled:
- **W1-S7, the Teams silver writer applies no wipe:**
  - no reader is granted beyond the named original readers until every Teams silver object reads wiped and the pull wipes on landing (ADDENDUM 8.1);
  - the served re-wipe pair is in round 20 (ADDENDUM 10).
  This is exactly the CVO's "grant no reader until one holds".
- **D2-S10, the transport is a stub and the bearer is missing:** ADDENDUM 9. A round-19 transport cell is built; the bearer name comes from NFRA_OPLGTW, never
  guessed.
- **D2-S9, the backfill precedent is empty:** ADDENDUM 5. It is kept empty, and the residual check is the privacy guard.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 11 (~10:2xZ, `~T2` msg 3117, row D2-W2-S6, BLOCKING): the gateway contract serves no metadata VTT

**Read:**
- TR-t-20 merged @488c840f48 and @7e2a14edee (412 passed). The real transport is built to the owner's contract, and `pull.tf` reads `gateway/transcripts/bearer`.
- `pull.py:98` reads `fmt="metadata"` for the observed wall-clock times.
- `/hx/transcripts` serves content VTT only, so a live pull raises `GatewayFormatUnsupported` on its first row.

**RULING: (a) as the permanent path, and an interim landing that keeps the three-clock rule. Not (b).**
1. **`~T2` asks NFRA_OPLGTW, through `0.0.0_AB_MSTR~DELL2`, to add a metadata VTT path to `/hx/transcripts`.** The observed wall-clock comes only from the
   source.
2. **Interim, so the pull is not blocked:**
   - the transport fetches content VTT only;
   - silver lands each row's wall-clock start and end as NULL, with `wallclock_basis: absent (metadata path not served)`;
   - the cue offsets are kept as served.
   - Wall-clock is NEVER derived from `createdDateTime` plus offsets. That is the derived clock the three-clock rule forbids, and a consumer could not tell it
     from an observed one.
   - FWD-1's "who said what" needs speakers and text, not wall-clock, so it is served by the interim.
3. **When the metadata path ships,** a backfill fills wall-clock for the interim rows from the source, under its own pair, and flips the basis to `observed`.
4. **p18 re-runs from step 1 on the rebuilt zip** under the existing half (@b972f130c9). The ledger binds the new sha256.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 12 (2026-10-09 ~11:4xZ) -- round 20 close (`~T2` msg 3208, `R20_CLOSE.md` @159471cd01)

**Read:**
- MAY-CLOSE, 415 passed.
- **The Teams pull is LIVE:** 9 added; the outlook pull's CodeSha256 is unmoved; the rule is ENABLED.
- **W1-S7 is CLOSED:** 30 of 30 keys re-wiped, residual 0.
- D2-S11 (the host allowlist) is TAKEN by site Z (ruling @261e2c42a0).

### Grades

| FWD | grade | basis |
|---|---|---|
| FWD-4 | **REALIZED** | the on-demand exercise reaches the `never_recorded` cause and names it (`R20_EXERCISES_FWD4_FWD9.json`, @e18849b58c) |
| FWD-9 | **NOT REALIZED** | one question answered across meetings (1,462) and mail (17), but commentary is 0. The FWD names all three. It realizes when one commentary is served (IRPT_ANLREQ's commentary Lambda, step B), re-read then |
| FWD-1, FWD-2, FWD-3 | NOT REALIZED | the pull is live but lands 0 until site Z widens the host allowlist (D2-S11). The Research arm also needs Andrew's meeting membership |
| FWD-5 | NOT REALIZED | the narrower wiped reader follows wipe-on-landing being live (ADDENDUM 8.1) |
| FWD-6 | NOT REALIZED | intake is built (r19). It needs one real market-update deck |
| FWD-8 | NOT REALIZED | TO-APPLY-a18 is at the laptop |

**FWD-6's real deck is an act for Andrew,** listed with its citation: it is a document only he or his team produces. A synthetic deck would grade nothing.

### Round 21

1. **D2-S12 repair:** a `lambda-source-map.json` entry and a `transcripts-v*` tag for the transcripts root's Lambdas (deployment rules 4 and 6). It is a build input record,
   not a served move.
2. **Re-probe D2-S11 when site Z lands its env release:** one read, named in the row. Then the first scheduled landing grades FWD-1, FWD-2 and FWD-3.

**Carried:**
- the metadata-VTT route (site Z, @7f58eb8f77);
- the FWD-8 laptop apply;
- the Research meeting membership and the real deck, both Andrew's.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 12.1 (~11:4xZ) -- the CVO's round-20 slug (msg 3212, `ADJUDICATION_v11.md` @37ad2cddeb): ADDENDUM 12 stands, plus one unlock

The slug matches ADDENDUM 12: ARMED 0; W1-S7 and D2-S10 closed; D2-S11, W2-S6 and D2-S12 open. **It also records that the live pull WIPES ON LANDING.** With W1-S7's re-wipe
closed, **both conditions of ADDENDUM 8.1's reader gate now hold.**

**Round 21 adds item 3: FWD-5's narrower reader role.**
- It reads Teams and outlook SILVER only, never bronze, through `name()`, under a never-widen pair.
- Its proof is FWD-8's pattern: the role reads one wiped silver object, and is REFUSED on one bronze object.
- **It is a NEW reader of client meeting content,** so its holder is named in the pair: an analyst principal on Andrew's C-READERS list, or a new name on his word. It
  is never inferred. If no analyst principal is named today, the role is built with no trust and graded once Andrew names one.

-- 1.0.0_SA_CTO~DELL2
