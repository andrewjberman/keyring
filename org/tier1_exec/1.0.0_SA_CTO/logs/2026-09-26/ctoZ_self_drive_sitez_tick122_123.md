# self-drive ticks 122-123, `1.0.0_SA_CTO~Z`, 2026-09-26 ~20:30-21:50Z

**Arming record:** `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md` @`f3b85ff6a5`.
**state: ARMED.** Prior log ticks 119-121 @`cfaac6d083`. **Floor exceeded AND substantive delta.**

Broker DOWN for this seat; watcher re-armed 3x this block (129, 130).

---

## 0. CORPUS ACT A IS DRAINED AND I VERIFIED IT BY RE-RUN, NOT BY READING ITS REPORT

`2.0.0_SA_COO~X` drained act A @`6f0469ecb2` (21:21Z) at HEAD `e2075ec93b` under the signed pair
(COO `f283a6e15f`, CTO `8b27c6f2cc`). I re-ran its own verifier against the served store:

```
act keys 94 restamped 94
limb1 band_basis carry 53 without 41 should_carry 53 wrong_field 0
limb2 disposition_or_ratio_moves 0
limb3 excluded_same_stamp 3 of 3
CAT_US status SERVED ratio 0.5973927334701294 band [0.33, 3.0] currencies True band_basis True
```

**Reproduced digit for digit. Act A: GRADED PASS.** Change entry closed on the trunk (0 hits) with its
completion record written (1,561 B).

> **THE NEGATIVE ARM I ADDED WAS EXERCISED AND IT MATTERED.** `without 41` is the count the COO's original
> half did not state. A discriminator reading only `carry 53` would have passed a defect that stamped
> `band_basis` on all 94 -- attaching a calibration claim to refusals (`currency_mismatch`,
> `forward_eps_not_positive`, `no_price`) that return before the band branch and which the band never decided.
> **`wrong_field 0` is the other half of the same idea.**

The drain also honoured the binding I put on its report verbatim: **"Z-W2-S10: 1 of 3 re-minted, 6861_JP and
CSL_AU held by Z-S47."** It did not report cell 4 closed.

## 1. I RAISED A tt-2 STALL ALARM AND STOOD IT DOWN 30 MINUTES LATER. THE MEASUREMENTS WERE ALL TRUE

`2.0.0_SA_COO~Z` reported tt-2 live, `0.7.0_AE_CloudOps~A` re-seated ~20:25Z with its GO as an inbox file.
I measured three independent planes at ~21:12-21:15Z:

| plane | reading at 21:15Z |
|---|---|
| deployed function | `CodeSha256 = LK9h47ju...DcO4s=` -- **exactly the base AC1 requires to change**; LastModified 11:28:27Z |
| build artifact | newest version `T9JIi3D...80` @`11:01:00Z` -- **the same VersionId the COO half records as the rollback** |
| NEVER-2 entry | **none at the trunk HEAD (13 open) nor at any of 63 worktree HEADs** |

I sent the alarm. **Then `ee87bf1506` landed at 21:32:40Z: `0.7.0_AE_CloudOps~A | ledger(TO-AMGT-tt-2):
NEVER-2 entry OPENED`** -- the exact artifact whose absence was my strongest signal. **I withdrew the ask and
told the COO explicitly NOT to fire `/unstick`, because keying a working session types into it.**

> **THE DEFECT WAS NOT THE MEASUREMENT, IT WAS THE IMPLIED RATE.** All three readings were real and remain
> real for 21:15Z. What I did was treat 50 minutes of silence as evidence about the SEAT, when a
> build-plus-apply cell that opens its ledger entry at start had simply not reached its start.
> **Three planes agreeing on "not yet" is a statement about one instant, not a trend.** The honest form was
> *"no movement as of 21:15Z; expect the ledger entry as the first sign of start."*
>
> **And this is the correction `0.0.0_AB_MSTR~Z` made against itself today, which I accepted, and then
> repeated four hours later with better timestamps and the same underlying error.** A lesson written down is
> not a lesson applied.

**One thing I did keep right:** every figure carried its read time, so the staleness was legible to the
recipient and to me. That is what made the stand-down cheap instead of an argument.

## 2. AN INSTRUMENT CORRECTION THAT NEARLY COST A FALSE "HALF-LANDED" REPORT

CLAUDE.md NEVER-2 says to read `.open_deploys/` across **every** live worktree and union them. I did, got 30
distinct entries, and saw `amgt-rs-2-the-redeploy.json` -- round 44's redeploy, which completed -- reading as
**open**. I was one sentence from reporting a half-landed deploy.

**Measured instead:** the **trunk HEAD carries 13** open entries and `amgt-rs-2` is **not** among them. The 5
worktrees still carrying it are `wk-amgt_corpus-6-*`, cut before the close and holding the pre-close bytes
forever.

> **THE UNION OVER-REPORTS OPEN DEPLOYS: 30 vs 13.** The law's instruction is right for FINDING an entry a
> worker holds on its branch, and wrong for deciding OPEN. **Union to FIND; read the TRUNK to decide CLOSED;
> a worktree-only entry is in-flight or stale, and its branch's cut date decides which.** The tell was that
> the shared tree's own listing did not contain the file the union reported.

## 3. THE BARRIER TO CLOSING RESAPP, AND IT IS NOW PLANNED

`AMGT_RESAPP`'s PRD header fence lists **`FWD-1`..`FWD-31`** (31 ids, lines 12-42) and **no full-pass
artifact exists** -- `comp-find --name '*OUTCOME*'` over the CTO deliverables returns 6 of 1,413 scanned:
CORPUS has its 19-outcome pass, RESAPP has only a clause-1 render partial and the `FWD-30` regrade.
**So RESAPP's REALIZED count does not exist anywhere, and a project cannot reach a zero-graduation round on
grades nobody took.**

`2.0.0_SA_COO~Z` confirmed: **round 46 carries a full `FWD-1..FWD-31` pass as a cell, shaped like `CRPS-i-5`,
ordered AFTER tt-2's served sweep.**

**The ordering is not a preference.** tt-2 AC1 requires `CodeSha256` to move and AC2 sweeps the live library
on the served plane, so **tt-2 replaces the served export**; a pass run before it would grade the clause-1
export outcomes against bytes tt-2 discards.

## 4. MY OWN RECURRING INSTRUMENT ERROR, THIRD INSTANCE TODAY

`python <script> | tail -12; echo "rc=$?"` reported **rc=0 for a script that died on an `IndexError`** -- the
rc belongs to `tail`. Earlier today the same shape gave me a false `rc=0` on `git apply --check` and a false
UTC label from `--date=format-local` with a typed `Z`. **Stop appending `rc=$?` after a pipe; redirect to a
file and read the rc directly** -- which is how the verified act-A run above was taken.

## Step 0 reads

```
REGISTER: 6 sitez live directives -> 20 projects | ARMED SCOPE 5 / 18 (D6 carved out, arming record s.2a)
COMPLETION TEST: NOT DONE -- 4 of 20 register-scope / 4 of 18 armed-scope status:complete
INBOX: 2 read this block, 3 sent; 0 unread at close
OPEN CALLS IN SCOPE: 0 adjudicable | 1 RESERVED (serp = metered SPEND, Andrew's)
```

## Scope state -- RECORD plane

| project | orders | where it sits |
|---|---|---|
| `AMGT_RESAPP` | tt-1/3/4 **complete**, tt-2 pending | tt-2 **IN FLIGHT**: entry opened 21:32:40Z; served plane still at base |
| `AMGT_CORPUS` | i-1..i-4 **complete**, i-5 pending | **act A drained and CTO-verified**; act B pending under limb 4; `i-5` is the 19-outcome pass |
| `AMGT_HARVST` | 20 of 21 | `v-2` pending at `2.0.0_SA_COO~Y`; CVO holds L8/L9 until it lands |

## Cards at Andrew -- ONE, unchanged

1. **The `serp` BUILD** -- metered, so 92 names is SPEND, excluded BY NAME from his egress term.

## Still owed by this seat

- **Nothing blocked on me.** Next CTO acts: grade act B at its drain (limb 4 is the gate), the round-45
  analysis when tt-2 closes, and HARVST's round-7 analysis when `v-2` lands.

## Compiler Tools

The act-A verifier RE-RUN with its before-state argument rather than its committed output adopted, and its rc
read from a redirect instead of through a pipe -- the trunk read as the authority for CLOSED after the
worktree union over-reported 30 against 13 -- three independent planes measured before raising a stall, and
the stand-down sent the moment the ledger commit contradicted them -- and every figure stamped with its read
time, which is what made a 17-minute-stale alarm cheap to withdraw.
