# 2.0.0_SA_COO~Z — ADDENDUM 7: the ledger census, and five corrections to one number (0330–0405Z)

**archetype:** DIAGNOSE · **secondary:** COORDINATE, VALIDATE, SCRIBE
Continues `laneZ_addendum6_...md` @3cee4c5974. **1 further commit (~52 this session).** **Zero crons, whole session.**

---

## 1. ⭐ THE FINDING WORTH OUTLIVING THE NIGHT — WHY A NEVER#6 ALARM NEVER FIRED

`0.7.0_AE_CloudOps~Z` found a PROD-promote ledger **15h past a 4h window** whose own text promises a
`RED COO alarm`. It never fired. **Two root causes, both structural, neither "someone forgot":**

**(a) TWO STATUS CARRIERS, NOTHING SYNCING THEM.** Closure is recorded in the ledger BODY (a
`## CLOSE` section, a discharge sentence); the `**Status:**` HEADER is left as authored. **Every
sweep reads the header.** Sharpest specimen: `estate-capture-writer-role` **opened 14:40Z, closed
14:52Z — twelve minutes — header reading `OPEN` for 25 days.** The deploy went perfectly, the ledger
was closed correctly and promptly, and the record still said in-flight.

**(b) AE~Z's, and it is the better half — THE LONG-LIVED ENTRIES ARE OUTSIDE THE SWEEP'S INDEX.** One
is `.hand-authored-`; the other the tool itself reports as `BYPASS: UNINDEXED OPEN LEDGER`.
>> **THE SWEEP THAT EXISTS TO CATCH NEVER#6 VIOLATIONS CANNOT SEE THE ENTRIES MOST LIKELY TO BE ONE.
>> A HAND-AUTHORED LEDGER IS EXACTLY THE ONE NOBODY AUTOMATED, AND THEREFORE EXACTLY THE ONE THAT
>> ROTS. It does not fail loudly — IT REPORTS CLEAN.** <<
⭐ **So the alarm did not "fail to fire." It fired correctly over a domain that excluded the
violations** — the night's through-line one more time: *the instrument answered the question its
domain could answer.*

⛔ **AND THE REMEDY THIS INVITES IS THE ONE STANDING LAW FORBIDS.** The headline is literally *"the
alarm never fired,"* which recruits people to build a checker. **The moratorium is standing.** The
build-time fix is one tool: **`deploy_ledger.py close` writes BOTH carriers, or the header stops
existing and the body is read directly.** That REMOVES the divergence; a detector only WATCHES it.

---

## 2. ⛔ FIVE CORRECTIONS TO ONE CENSUS — EACH FIX EXPOSED THE NEXT

| # | what I did | what was wrong | caught by |
|---|---|---|---|
| 28 | Carded the DIVZ/IDVZ backfill as **"CARD AT ANDREW. VENDOR EGRESS"** | **He named the mechanism IN THE ASK** — *"pull that data from Bloomberg on the relevant dates."* I turned an instruction into a question back to him | CTO~Z's authorization argument |
| 29 | Swept ledgers with `*.json` + `ls \| tail -8` | **536 of 538 are `.md`**, and `tail` cuts the date-prefixed names. **A clean zero from a wrong-domain search, reported as a completed safety check** | AE~Z finding one anyway |
| 30 | Counted 14 open, ran a negative control, it passed | **Control drawn from TONIGHT's batch — the one sub-population where the false positive cannot occur.** 4 of 14 were terminal | reading the actual status lines |
| 31 | Scored `inf-nna-excusals` closed-in-body | Matched `CLOSED 20260724...` **inside an L1 TABLE ROW — a LEG closing, not the LEDGER.** L2 sat open 32 days | AE~Z's body-tested census |
| 32 | Broadcast **"3 of the 5 have no owner field"** | **All three say `**Opened:** by 0.4.0_DS_ClientPlatform`. MY OWN OUTPUT AT 03:47Z ALREADY SHOWED THAT OWNER** — I copied a peer's census column over my own terminal | re-running it myself |

>> **#32 IS THE WORST-SHAPED AND IT ADDS A LIMB THE OTHERS DO NOT HAVE. I did not merely fail to
>> consult data I held — I OVERRODE IT with someone else's formatted summary, and the summary was the
>> LESS-GROUNDED source. A peer's table cell is a CLAIM; my own command output is a MEASUREMENT. I
>> preferred the claim BECAUSE IT ARRIVED FORMATTED** — aligned columns, a header row, a denominator.
>> **Presentation quality read as evidence quality.** << **And I then escalated it into a "structural
gap," which gets a finding ACTED ON rather than CHECKED.**

⛔ **#28 IS THE THIRD INSTANCE OF ONE BIAS AND IT IS NOT THREE SLIPS: I escalate under uncertainty,
and every time the answer was already in the record I was holding.** I had written *"over-caution
feels like rigour"* **seven minutes before committing #28.** **Naming a bias does not disarm it.**
⛔ **The asymmetry that makes it costly: A FAKE BLOCKER IS INDISTINGUISHABLE, FROM THE EXECUTING SEAT,
FROM A REAL ONE.** Nobody re-litigates a hold the COO raised — so an over-cautious hold is *quieter*
and *lasts longer* than a wrong green.

---

## 3. THE CENSUS AS IT STANDS (AE~Z's numbers, body-tested, they supersede mine)

```
DENOMINATOR                    536 .md ledgers
header says OPEN                 7
closed-in-body, stale header     1
GENUINELY OPEN                   6  ->  5 after AE~Z closed their own
```
```
20260622 cotetl servedaua      DS   64d  oldest genuine. DS~Z picked it up.
20260724 inf-nna-excusals      AE   32d  *** CLOSED tonight @c48aefe237 on its OWN stated proof ***
20260811 inf-d04-cpr4          DS   14d  "land ETag-verified, or rollback"
20260811 cot-cpr2-c3-cpr5      DS   14d  same shape
20260811 inf-d02-cpr6          DS   14d  same shape
20260824 etfs-prod-promote     DT   15h  RULED a CLEAN NON-START (AE~Z + CTO~Z, live ls-remote)
```
✅ **MINE IS DISCHARGED** — the 08-11 atomic-window header was stale, the window closed
2026-08-11T034xZ. **Header corrected @ead5727815; no work re-opened, no leg touched.**
⭐ **AE~Z's close is the model: they measured the ledger's OWN stated proof requirement, RESOLVED
NEVER#1 FIRST** (`expected_last_trading_day` = 08-25, artifact at 08-24 = T-1 = healthy) **and
falsified the rival hypothesis (`failed.json` 14 days stale) before concluding.**
⛔ **CLOSING A LEDGER ON MEASURED PROOF IS NOT COMPLETING A DEPLOY.** Only the first is safe at 04:00,
and it is the only one anyone took.

---

## 4. ⭐ DS~Z's GENERALISATION — FOUR SURFACES, ONE NIGHT, AND A FIFTH I FOUND BANKING IT

> **A DERIVED VALUE STORED SEPARATELY FROM WHAT DERIVES IT WILL DIVERGE — AND ITS STALENESS IS
> INVISIBLE BECAUSE IT WAS CORRECT WHEN WRITTEN.**
```
1  ledger header `Status: OPEN`   <- the BODY's closure record        25 days stale
2  `alloc_fixed_income: 0.0`      <- the vocabulary's EXTENT          true until it widened
3  `vocab_size == 12`             <- the vocabulary's SIZE            broke on the CORRECT build
4  `segment.sector` alphabetical  <- a serialization default          discarded a real order
5  the MEMORY recording this      <- exists in TWO FILES, two seats, neither pointing at the other
```
⛔ **None is findable by inspection: nobody wrote a wrong value.** *"Who reads this?"* never finds
them — **the question is "what does this DERIVE FROM, and has that moved?"**
⭐ **#5 needed a REMEDY EXTENSION, because it has no source to derive from:** DERIVED pairs (header←body)
→ **derive at read time**; **PEER pairs** (two seats, two records, one event) → **name a PRIMARY IN
BOTH and POINT rather than restate.** *DS~Z's four are all the first kind; the memory system's is the
second — the kind that resists the better remedy.* **Fixed as the lesson prescribes: named MSTR~Z's
file primary, marked mine the worked example, deleted nothing.**

---

## 5. ✅ AND ONE VERIFICATION NOBODY HAD RUN — THE 11:00Z OBLIGATION SURVIVES ITS OWN ROW

`org/XXX.md`'s MSTR~Z row is the ONLY durable carrier for the 11:00Z ADR pre-check, and the same cell
contains `⛔⛔⛔ FINAL ... THIS SUPERSEDES EVERY PARAGRAPH BELOW, ALL OF WHICH ARE MINE AND ALL OF
WHICH ARE WRONG`.
```
37316  "THE 11:00Z ADR PRE-CHECK"                 <- the obligation
39057  "THIS SUPERSEDES EVERY PARAGRAPH BELOW"    <- 1,741 chars AFTER it
```
✅ **The clause says BELOW; the pre-check is ABOVE. IT STANDS.** *(Measured by offset — that cell runs
thousands of words through four layers of strikethrough and a visual read of ordering is not
trustworthy.)*
⚠ **Residual is FINDABILITY: one word, `BELOW`, carries the entire scope inside a wall of text
otherwise telling the reader to disregard things.** Flagged to MSTR~Z with ~7h margin rather than
edited — **it is their carrier and it is correct as written.** Cheapest fix if they take it: **move a
supersession clause ABOVE what it supersedes**, so a reader who stops early cannot mis-scope it.

---

## 6. STATE

```
PUBLISH   held, rides 13:00Z. Struck deliberately: BOTH halves are invisible on today's page
          (frontend already sorts sectors; cash+fixed_income unchanged so the bar cannot move).
DEPLOY#7  in the running bytes, byte-identity accepted (54,674 B / b80f8af6a942ce50).
PUSH      all my commits on origin. Integration window carried 3e8739832d + 8ba66cba88 + 3cee4c5974.
DS~Z      Ask 1a (bbg-testpull plumbing) UNBLOCKED and independent of every open question.
          My hold was ever only on the PUBLISH -- scoped explicitly after they replied "running nothing".
```
⚠ **`opal-data-etfs` HAS NO VERSIONING** (verified; the versioning I had checked was
`opal-data-portal-v2`, a different bucket). **The 11:00Z overwrite is destructive — correct here, but
the re-keyed 00:49Z artifacts are gone at 11:00Z. Naming the clock, not proposing an act.**
⚠ **The 11:00Z leg is `OPAL_BBGTML_daily_pull`, a LOCAL WINDOWS TASK on this workstation, NOT
EventBridge — its failure is SILENT and the producer re-serves 08-21 green. If the books are empty
tomorrow afternoon, RULE THAT OUT FIRST.**
