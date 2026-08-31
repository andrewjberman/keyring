# /self-drive D2 & D3 — tick 96 (2026-08-30 15:40Z) — state: ARMED

Covers tick 96 and the acts since the tick-95 log (`38710d3040`, LOCAL; origin @`bbdaa9fdc8` at the 15:07Z
CLOSE, own is-ancestor read 15:40Z). Cron `1c261f82` :07/:37. Paired `/drive D2 & D3 @ 2.0.0_SA_COO`.

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → 10 projects (1 complete). Open TOs **26** (D2 22 + D3 4). Ledger **19 / 0
unconsumed**. Acked READ this tick: 88191, 88198, 88202, 88203, 88206, 88211, 88216, 88218.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 8** (R1–R5; R6 the C02-g-11 card at AE~L; R7 CARRIED 14:30Z as REC YES; R8 the
five scratch S3 objects, folded onto R7's card).

## Verdicts since the tick-95 log (§3)

- **CVO 88206: OPAL_ADVIPOINTERS.INF-DRIFTCENSUS CLOSED at the grader — PASS**, ground-truthed on the
  grader's own instrument on `inf-billing-daily` (live package downloaded, members diffed against the
  recorded commit's blobs). DC-2's zero on record-lag is the finding: none of the eight is fixed by a row
  edit; seven are redeploys.
- **AE~K 88211: INDEXBYTES-DEPLOY closed on the one act** — proof @`411d1aea64` declaring
  `introduces: ["git show :", "_index_blob", "REFUSED (rc=2)"]`, each PRESENT at the pin and ABSENT at
  `<pin>~1` (2/0, 2/0, 1/0, tilde form), VALID rc=0 unpiped at checker `ecce0820d2`, 1 row CONTENT-resolved.

## Driver's own acts (tick 95 → 96)

**Three corrections, all against the gate's own words (88225):**
1. **The sec-7b sequencing premise WITHDRAWN.** 88193 twice sequenced `1.0.0_SA_CTO~X`'s checker items
   "behind the sec-7b engine-pin disarm, that lane's BLOCKING item". Measured (88203): both items were
   DISARMED at 87781, 14:1xZ; the correction record `1eba52e86c` and c0''' `2a35583ce1` on origin since the
   14:43Z CLOSE. The gate sequenced behind a hold lifted 40 minutes earlier, from a state it had read rather
   than one it had re-read. Cost zero (the seat delivered both anyway); the class is that a sequencing
   instruction is a claim about another seat's state and needs the same freshness as any other claim.
2. **The DRIFTCENSUS mechanism hypothesis REFUTED by the gate's own read.** 88207 proposed "the pre-DRIFTD
   recorder stamping one HEAD across packages built from older sources on 05-13", with the discriminator
   `TZ=UTC git log -1 --format=%cI 46d0b98aef`. It reads **2026-06-11T16:26:23Z** — 29 days AFTER the 05-13
   `LastModified`; a deploy cannot record a commit that does not yet exist. The CVO measured the same
   relation independently on inf-billing-daily. **The measured shape:** a LATER pipeline-wide act on 06-11
   stamped the then-current commit onto functions last deployed 05-13 — the same defect INF-RECORDER-SCOPE
   closed this afternoon, now with an instance in history. Consequence for the remedy cell: each leg's
   behavioural diff runs from the vintage its PACKAGE MEMBERS resolve to (DC-1's column), never from the
   row's commit.
3. **The (a)/(b)/(c) bucket set had an UNCOVERED MEMBER — the gate's own taxonomy.** AE base's read-only act
   (88216) on `inf-etf-ownership-daily`: the packaged member MATCHES the recorded commit (the record is
   CORRECT), the deployed zip is a coherent older vintage, and HEAD's source has since added two modules —
   0 ImportError and 7 clean daily runs, so nothing is broken. That is **(d) UNDEPLOYED CHANGE**, which none
   of (a)/(b)/(c) covers; the seat had placed it in (c) on a set-difference technicality and said so. The
   set gains (d); the eighth reclassifies (c) → (d); the classifier's ORDER is the fix — record-vs-artifact
   first, then artifact-vs-HEAD, then set-difference (which is downstream of a vintage gap and swallows it).
4. **A GATE on that leg, adopted from AE base:** at the new vintage `dedup_core` and `trading_calendar` are
   REQUIRED imports, so a redeploy shipping the current single-member shape would ImportError on the first
   fire — turning a healthy function into a broken one. The leg asserts packaged members == `files[]` at
   HEAD (3) before the apply, and its read-back includes the next fire's REPORT with 0 ImportError.
5. **DS~V's two-arm acceptance TEMPLATE adopted** (`INF_ONEWRITER.TWO_ARM_ACCEPTANCE_TEMPLATE.json`
   @`5dbb7c7795`): the gate's 88210 had named "the pre-registered N/A conditions carried over verbatim"
   while they lived across five message ids and a scratch file — seven legs would have re-derived five
   different acceptances. Each leg's face now cites the template at a pin; one addition, from (2): the
   comparison vintage is the package's resolved commit.

## In motion, not mine

The seven-leg remedy cell (issuer, on the shape at 88207 as amended here); AE~L's C02-g-11 card; **Monday
12:45Z** (a06's registered line + A7-4 + V-4's first) and **Tuesday** (V-4's second); DS~V's single-writer
billing read ~11:18Z Monday; MSTR's next NON-ZERO-ceiling window = IB-5's production read, which retires the
standing pre-push hand-compare; Andrew's word on R2, R6, R7 (+R8).

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`directives-check.py --json`, project JSON statuses, the ledger count, `ls-remote` + `merge-base
--is-ancestor`; `TZ=UTC git log -1 --format=%cd --date=format-local` on `46d0b98aef` (the mechanism
discriminator, which refuted the gate's own hypothesis); Msg-IDs read from each inbox file. No comp-find, no
comp-state.

state: ARMED · next log at a verdict or tick 102 (floor)
