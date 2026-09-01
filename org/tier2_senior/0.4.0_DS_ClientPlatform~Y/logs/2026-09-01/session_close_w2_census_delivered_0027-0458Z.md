# SESSION CLOSE -- ADVI_BDPARITY W2 fired, completed and GRADED PASS (2026-09-01T00:27Z - 04:58Z)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

**Seat:** `0.4.0_DS_ClientPlatform~Y` | **Scope:** ADVI_BDPARITY, W2 only (Rule 27)
**Window:** since `bdparity_spot3_si_brief_and_mint_finding_2215-0027Z.md` @ `3aa8bcf273`
**Commits (4):** `75e7f333b8` `16f1762977` `e352f70476` `3637812fbc`
**PUSH STATE: LOCAL** -- `git ls-remote` 04:57Z: `origin/CLOUD = 173a873139`; local HEAD
`3637812fbc`. Integrator-only gate (LD-0367/0368); no override taken.

---

## Current State

**P2-2 IS COMPLETE AND GRADED PASS.** `3.0.0_SA_CVO` 90748 graded against criteria it filed BEFORE
the fire and **re-derived every arithmetic line at its own seat** -- all close, no residual.

```
  accounts pulled     5,309 of 5,309 (100%)      cells attempted     15,927
  cells COMPARED     15,445                      SELF-INVALID           112 over 61 accounts
  NO-LINKABLE-DAYS      370                      15,445+112+370 = 15,927 EXACT

  QTD 5,138  EXACT 1,812  TIGHT 3,103  LARGE   223   range_match 5,138/5,138   day-resid  45
  YTD 5,151  EXACT 1,411  TIGHT 2,961  LARGE   779   range_match 5,151/5,151   day-resid 240
  1Y  5,156  EXACT 3,003  TIGHT 1,161  LARGE   992   range_match 5,156/5,156   day-resid 949
  ALL 15,445 EXACT 6,226  TIGHT 7,225  LARGE 1,994   range_match 100%
  p50 1.95 bp | p75 4.74 | p90 15.50 | p95 43.08 | p99 ~9,854 | max ~71,772
```
**Deliverable:** `.../deliverables/ADVI_BDPARITY_P2-2_CENSUS_RESULT_20260901.md` @ `3637812fbc`.
**Bronze:** `blackdiamond/49f/bronze/reporting_performance/2026-09-01/`, 5,309 objects.
**Vendor ledger CLOSED: 5,843 calls** (5,792 data + 51 auth) vs a clean 5,358 = **+485, +9.1%**.
**Criterion 3: 18 of 18 baseline objects at pinned VersionId. UNTOUCHED.**

**STANDING SENTENCE (ratified, quotable-safe):** *performance-feed parity is MEASURED at n=15,445
cells over 5,309 accounts, with 1,994 LARGE (1,516 not explained by coverage) open. NOT "parity
proven."* **LEAD: the census is a TWO-WAY AUDIT and is finding more on OUR side than on BD's.**

---

## What was done

### 1. The mint correction -- I reported a non-fault as a finding
Reported "the 00:00Z mint has NOT fired" to four seats and put it in a committed brief. **Wrong
implication.** `bd-49f-session-trigger` ran ON SCHEDULE at 00:00:18Z and **SKIPPED the mint BY
DESIGN** on a positive cookie probe (Lever A), with the previous night's opposite branch as positive
control. **I measured the secret four times and the producer zero times** -- and my own evidence
("alive at 23.83 h") WAS the condition that makes it skip. Corrected at the same width in both
durable carriers @`75e7f333b8`. Also retired my own watch's `[MINT-LATE]` arm as wrong for a
conditional producer: **it fires on a healthy night.**

### 2. W2 fired, and my bounded probe caught a 5x vendor overspend -- mine
Fired chunk 1 of 45 as a rate-limit probe rather than committing all 45. It returned
`ReadTimeoutError` reporting **ZERO landed**. False: a default boto3 client (read_timeout 60 s vs a
168 s chunk) **RETRIED a non-idempotent vendor-spending invoke five times.** Measured by
object-version census: **120 keys x 5 versions = 600 calls for 120 accounts. 480 wasted, exactly
5.0x.**
>> **It failed SILENT IN THE DIRECTION THAT COSTS MONEY** -- the runner said nothing happened while
   the vendor had been charged 5x. Had all 45 chunks fired as one act: **~26,500 calls instead of
   5,309.** The probe cost 480 to find a ~21,000-call defect. <<
**And my FIRST fix was also wrong:** `retries={"max_attempts": 1}` renders as `total_max_attempts: 2`
-- **the field you set and the field that governs are different fields.** It would have halved a 5x
overspend to 2x and reported success. Caught only by reading the APPLIED config. Fixed
@`e352f70476` with import-time asserts, both arms exercised, and **confirmed on live bytes: 5,189
keys at exactly 1 version beside chunk 1's 120 at 5, no third value in the prefix.**

### 3. The producer finding -- the census caught OUR gold, not BD's
Account `0077573397`, 2025-10-15: `bmv $2.33 -> emv $1,164.46`, `cf_net 0.0`, `r_net 498.77`
(+49,877% in one day), `status OK`, clearing `NEAR_ZERO_BMV=1.00` by $1.33.
Per `2.0.0_SA_COO` 90726 I opened **all 114 rows** above `|r_net| > 1.0` rather than shipping a
threshold:
```
  TWR identity holds 114 of 114 -- the algebra is right, the INPUTS are wrong
  A no recorded flow   79 rows / 70 accts    B flow >10x base 21/17    C undispositioned 14/12
  A CLUSTERS ON DATES: 2026-01-26 x19, 2025-10-15 x10, 2026-04-09 x7, 2026-05-06 x5
  FOUR DATES = 52% of the class, over 35 distinct dates
  CONTROL: those dates carry a NORMAL population cf_net==0 rate (84-86%); control dates ZERO blowups
```
**Not 70 broken accounts -- ~35 DATES where flows for a subset failed to ingest. Per-DATE re-ingest.**
⛔ **And I killed my own BMV hypothesis by measurement**: of rows with BMV < $10, only **0.3%** blow
up. Raising `NEAR_ZERO_BMV` would flag 13,211 rows to catch 36. **The producer must not act on my
earlier note.**

### 4. Rulings consumed
`1.0.0_SA_CTO` 90702 ruled SELF-INVALID a **PRIOR GATE**, not a fourth magnitude band -- a magnitude
threshold cannot separate a data blowup from a methodology difference because they are IDENTICAL ON
THE NUMBER. Implemented as a screen ahead of comparison, withdrawn from the parity denominator, two
denominators printed. `2.0.0_SA_COO` 90726 separated the screen's **two consumers with opposite error
costs** -- P3 needs only a SAFE exclusion (over-inclusion free), the report needs a MEASURED count --
which unblocked P3 without waiting on precision it did not need.

---

## Briefs written (DS role addition)

| Artifact | Purpose | State |
|---|---|---|
| `ADVI_BDPARITY_P2-2_CENSUS_RESULT_20260901.md` | the census result, 4 criteria + 5 non-claims | `3637812fbc`, GRADED PASS 90748 |
| `advi_bdparity_w2_runner.py` | retry/timeout fix + import-time asserts | `e352f70476` |
| `docs/briefs/advi-bdparity-spot3-and-si-recommendation-20260901.md` | corrected mint section + LARGE localization | `75e7f333b8`, `16f1762977` |

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `parity_period_returns.py` | `link()` batched, 36 batches | PASS | equivalence-tested against unbatched BEFORE use |
| `.tools/aws` cloudwatch | Invocations + Errors | PASS | 51 invocations, 1 error (the deliberate pre-flight) |
| `.tools/aws` s3api | `list-object-versions` x6 | PASS | **the instrument that caught the 5x overspend**; runner's own count was disqualified |
| `.tools/aws` logs | `get-log-events` on the mint trigger | PASS | producer log + previous-night positive control |
| `.tools/commit-gate.sh` | 2 runs | PASS | clean |
| `.tools/safe-commit.sh` | 4 commits | PASS | msg-verify MATCH each |

**What worked:** the object-version census. It was the ONLY instrument that could see the overspend,
and it supplied its own positive control (chunk 1's 5-version keys sitting beside the fixed 1-version
keys in one prefix).
**What failed:** two of my own script designs -- 5,309 serial S3 gets, then `link()` scanning a
1.76M-row frame 15,927 times. Both were mine, both were fixed, neither touched the data.
**Gap found:** **`| tail -N` on a background job hides ALL progress until EOF.** I diagnosed a job as
stalled twice when I had simply blinded myself. A background job whose progress matters must not be
piped through a terminal filter.

---

## MCP traffic

**~30 received, 9 broadcasts sent.** Significant: **90605** (Andrew's egress grant, verbatim),
**90614** (both limbs discharged separately -- the name-collision defence), **90702** (the taxonomy
prior-gate ruling), **90726** (the two-consumers ruling), **90748** (PASS). Sent: **90623** (the
9b-ii expectation BEFORE the fire), **90645** (the self-reported overspend), **90665/90733** (the
producer finding), **90744** (delivery). All received rows acked from their Msg-ID lines.

---

## Blockers

**NONE.** P2-2 is complete and graded. P3-EXACT's precondition is met on the bytes; its input is the
15,445 screened population with the 61 SELF-INVALID accounts excluded **provisionally** (excluded is
not condemned -- any account the 114-row read labels legitimate returns to P3's population).

---

## Self-corrections this window

1. **Reported a non-fault as a finding** (the mint) -- corrected at the same width in both carriers.
2. **A 5x vendor overspend from my own client config** -- self-reported with the bill as evidence,
   before anyone asked.
3. **My first fix was also wrong** (`max_attempts` != `total_max_attempts`) -- caught by reading the
   applied config rather than the one I wrote.
4. **My BMV hypothesis, refuted by my own measurement** before the producer could act on it.
5. **An equivalence test that reported a false failure** -- 21 `days_linked` "mismatches" were
   `NaN != NaN` on both sides. Batching was sound; my comparison was not.

>> **The recurring shape, four times in one session: an instrument reporting a difference or an
   absence that belonged to the instrument rather than the world.** The retry that reported zero
   while spending 5x; the truncated secret history that produced a confident 1,415 h; the NaN
   comparison; the piped-`tail` "stall". **Each was cheap to check and each conclusion would have
   been wrong.** <<

---

## Next Steps

1. **[`2.0.0_SA_COO`]** P3-EXACT seats on the 15,445 screened population; 61 accounts excluded
   provisionally.
2. **[the gold producer owner, via `2.0.0_SA_COO`]** The per-DATE flow-ingest defect -- ~35 dates,
   four carrying 52%. **Do NOT raise `NEAR_ZERO_BMV`; that fix is refuted.** What the four dates
   have in common is unread and is theirs.
3. **[`1.0.0_SA_CTO` / `3.0.0_SA_CVO`]** The `SELF-INVALID` four-postulate record before the token is
   minted anywhere, carrying the state-coherence answer: a producer fix moves a cell to UNCLASSIFIED
   PENDING RECOMPUTATION, never to EXACT.
4. **[P3]** The 1,516 residual LARGE, and the undiagnosed 1Y day-count asymmetry (949 of 5,156 =
   18.4% vs QTD 0.9%).
5. **[`0.0.0_AB_MSTR`]** Four commits ride the next integration window; this seat is gate-blocked from
   pushing CLOUD and did not override.
