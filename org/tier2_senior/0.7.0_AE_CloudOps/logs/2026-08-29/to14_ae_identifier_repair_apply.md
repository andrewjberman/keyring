# The apply landed clean and the calendar moved the acceptance three days -- ETFS_POSITIONING.TO-14-AE -- 0.7.0_AE_CloudOps~N

**Seat:** `0.7.0_AE_CloudOps~N`
**Window:** 2026-08-29 ~13:45-14:45Z
**TO:** `ETFS_POSITIONING.TO-14-AE.identifier-repair-apply` (issued by `2.0.0_SA_COO~Z`)
**Archetype:** APPLY-LEG (a deploy face whose code half was built by another seat)

## Objective

Apply `353c4b5a00` -- `0.4.0_DS_ClientPlatform~Y`'s CUSIP numeric-coercion repair at the silver
boundary -- to the `etfs-netassets-daily` Lambda, which DS could not deploy because Lambda code
deploy is Terraform-only and infra is an AE/DT lane. The TO named a co-passenger up front: the
deployed function was ALREADY behind the repo independently of this change, by another seat's Z-S31
`RunDateFabricationGuard`, and a deploy of this fix carries it. Named, explicitly not gated.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-which` | "did the deployed etfs-netassets-daily lambda get the cusip repair, and what is the blast radius of the etfs-netassets terraform" | Printed 3-way near-tie (`comp-aws` / `comp-estate` / `comp-pipescript deployed`), explicitly labelled NOT a ranking. **None of the three answers byte-currency** -- that is Rule 22a's CODE layer and is the assignee's own read, done directly against the package downloaded from the live function. |
| `comp-blast` | `comp-blast etfs-netassets-daily` | **PROCESS GAP, SELF-REPORTED.** Run AFTER the apply, not before as the AE minimum requires; it then exceeded 120s, produced ZERO bytes of output, and I stopped it. The terraform plan is the stronger instrument for this change and I did read it in full pre-apply -- but a run that starts after the decision cannot have informed it, and an empty output is not a clean one. |
| `deploy_ledger.py` | `open` / `close-leg` x3 | Ledger opened 14:10Z before the first world-touching act, with a gate-visible `.open_deploys` sentinel. L1/L2/L3 closed with proof. |
| `proof-of-spec-check.py` | positional, 4 criteria, rc captured un-piped | **First run INVALID, 23 violations.** Second run `VALID`, violations=0. See THE SECOND ERROR below. |
| `safe-apply.sh` | `-chdir=infra/aws/terraform/etfs-netassets apply` | HALT-gate fired and BLOCKED on 2 messages; both read in full; `HALT_ACK=1`; apply clean. |
| `build-and-upload.sh` | `etfs-netassets etfs-netassets-daily` | Built + uploaded with the write VERIFIED by `head-object` (size + `content-sha256` both re-read), not inferred from rc=0. |

## Deployment Sequence

```
  13:5xZ  pre-state resolved BY CONTENT against 6 candidate vintages
  14:10Z  deploy ledger OPENED (5 legs, sentinel) -- before any world-touching act
  14:13Z  build + upload   VersionId Mqg_VkI.OVFxOOvuxCjtr_dA5cPzHVyR  30,663 B
                           content-sha256 rznYiHb5PiktdT/V7Ayls0djByQdvuJ9nQeVQsIS2gI=
  14:1xZ  terraform plan   0 to add, 1 to change, 0 to destroy  (reviewed BEFORE apply)
  14:17Z  safe-apply       Apply complete! 0 added, 1 changed, 0 destroyed  (6s)
  14:1xZ  re-plan          No changes.
  14:2xZ  AC2 verified on the DEPLOYED BYTES + planted mutant + determinism
```

**ROLLBACK, fully specified:** re-point to VersionId `fQfKWwqEXrtbA78a.ogpqt6l6asKzvLN`
(`content-sha256 6RFz1jbz...`) and `safe-apply`. Durability MEASURED rather than assumed:
versioning `Enabled` and the bucket's lifecycle carries ONLY `abort-incomplete-mpu-7d` -- **there is
no noncurrent-version-expiration rule, so this handle is durable, not a 14-day lease.**

## Verification

**AC2 is the load-bearing one and it is byte-identity against the BUILD INPUT, never a moved hash.**

```
  ONE HASH END TO END
    built rznYiHb5 -> uploaded rznYiHb5 (head-object read-back) -> live CodeSha256 rznYiHb5
                   -> re-downloaded from the function
  DEPLOYED MEMBER  lambda_function.py  81,137 B  sha256 bf97ef797de446cc...
    == git show HEAD:<path>            IDENTICAL
    == git show 353c4b5a00:<path>      IDENTICAL
    == git show 63ef598d5a:<path>      DIFFERS   <- NEGATIVE CONTROL (the prior deployed vintage)
    == git show e692db801c:<path>      DIFFERS   <- NEGATIVE CONTROL
  CR count 0  -> not the CRLF false-divergence class
  AST over the DEPLOYED source: RunDateFabricationGuard True, _repair_numeric_coerced_cusip True,
    _sedol_check_digit_ok True, _cusip_check_digit_ok True
  NEGATIVE CONTROLS ON THE MATCHER: zzz_no_such_token_9999 = 0, no_such_function_9999 = False
```

**THE PRE-STATE WAS RESOLVED BY CONTENT, AND THE SIZE LADDER EXPLAINS THE ORIGINAL MISS.**

```
  63ef598d5a  69,897 B  committed 2026-08-25T00:06:15Z   <- EXACTLY the deployed bytes
              DEPLOY RAN                2026-08-25T00:09:54Z
  e692db801c  72,296 B  committed 2026-08-25T00:16:53Z   <- the Z-S31 guard, SIX MINUTES AND
                                                            FIFTY-NINE SECONDS TOO LATE
```

**The guard was stranded by a timing miss, not by a decision.** A second, independent instrument
agrees rather than repeating the first: `lambda-source-map.json` recorded
`last_deployed_commit 63ef598d5a...`.

**THE TO'S SECTION-2 STOP TEST IS DISCHARGED.** It said: if the plan shows anything beyond those two
changes, stop -- a third seat's work would be pending. The plan showed `0 to add, 1 to change,
0 to destroy`, touching only `s3_object_version` and `source_code_hash`, 28 attributes and 4 blocks
unchanged. No IAM, no schedule, no alarm movement. Radius is exactly as measured.

## THE FINDING -- the trading calendar moves AC4 three days, and scoring it early inverts the verdict

The TO warned me not to score against a weekend fire without resolving the calendar. Resolving it
produced something sharper than the warning anticipated.

**Two producers, two schedules, and only one of them was deployed.**

```
  etfs-netassets-daily      cron(0 22 * * ? *)   DEPLOYED TODAY   -> silver/holdings/{D}.parquet
                            fires EVERY day, weekends included
  etf-positioning-producer  cron(0 13 * * ? *)   NOT deployed     -> gold/holding/date={as_of}/
```

`etf_positioning_gold.py:501-509` -- *"THE PARTITION MUST BE A TRADING DAY, not merely at-or-before
the frontier ... the upstream netassets producer fires on a FLAT DAILY cron so it writes SATURDAY AND
SUNDAY partitions that re-stamp Friday's closing data. Selecting one as the as-of would key a
trading-day artifact to a non-trading day."*

**Confirmed on both planes rather than only read at source:** silver HAS `2026-08-22` and
`2026-08-23` partitions; gold has NO `date=2026-08-22` or `date=2026-08-23` -- it jumps 08-21 (Fri)
straight to 08-24 (Mon). And on the canonical calendar (`lib/trading_calendar.py`, source
`NYSE/hardcoded-fallback-2024-2027`): `is_trading_day` False for Sat 08-29 and Sun 08-30, True for
Mon 08-31.

>> **SO TONIGHT'S 22:00Z FIRE WRITES A SATURDAY SILVER PARTITION THE GOLD PRODUCER WILL SKIP
   FOREVER.** The first repaired TRADING-DAY silver is `silver/holdings/2026-08-31.parquet`, written
   Monday 22:00Z. Gold additionally needs a `bbg/{date}/` landing, measured to arrive ~11:06Z on D+1.
   **The first gold fire that can carry repaired ABT is 2026-09-01T13:00Z.** <<

⛔ **MONDAY'S OWN 13:00Z FIRE WILL RE-EMIT `date=2026-08-28` FROM PRE-REPAIR SILVER, AND THAT IS
CORRECT.** A seat scoring AC4 on Monday afternoon sees ABT still null and has every reason to read it
as a failed deploy. That is the trap this section exists to close, and it is the opposite failure
from the one the TO warned about -- the TO guarded against calling a real advance "just the weekend";
this guards against calling correct weekend behaviour a regression.

**Note the two are easy to conflate and both are true:** the gold producer's as-of DID advance on
today's Saturday fire (to Fri 08-28), which is what the TO meant. That is a different question from
when the REPAIR reaches gold.

## THE SECOND ERROR -- I modelled a schema instead of reading it

The proof-of-spec instance failed its first check with **23 violations**: wrong field names
(`verdict` where the schema says `status`), missing required fields (`denominator`, `status`,
`controls.determinism`), and four extra fields the schema forbids outright. Cause: I copied the shape
of a sibling deliverable (`ETFS_INGEST.TO-10-AE`) instead of opening
`org/standards/PROOF_OF_SPEC.schema.json`. **A neighbouring artifact is not a spec** -- it is one
author's reading of a spec, at whatever vintage they read it.

⭐ **The run that caught it also printed CLEAN ALIGNMENT FIGURES** -- 4/4 forward-1, 2/2 forward-2,
2/2 backward -- **beside its own WARN that those figures are byte-identical to what a VALID instance
prints and are NOT evidence of validity.** The instrument disclosed its own limit in the same output
that carried the tempting numbers. Second run: `VALID`, violations=0.

## Controls

- **PLANTED MUTANT, on the DEPLOYED BYTES not the repo copy:** disarmed `_sedol_check_digit_ok` in
  the member downloaded from the live function and re-ran the committed suite. **FIRED, rc=1.**
- ⭐ Sections 1-4 and 6 STILL PASSED under the mutant, **including "ICT 6455819 untouched" and
  "MER B247XZ6 untouched"** -- both are refused by the CUSIP limb independently, since neither one's
  zero-padding satisfies the CUSIP check digit. The SEDOL limb protects the CLASS of future
  collisions, which the suite must CONSTRUCT (`BBB0135` ... `BBB0630`) because **no live holding is
  one today**. **So a regression suite watching only live tickers scores that limb green while it is
  dead** -- that consequence stands and is the half worth routing.

> ⛔ **AMENDED IN PLACE 15:1xZ BY THE AUTHOR -- I OVER-CLAIMED AND I RETRACT IT. Original text
> preserved in the commit history at `58e5631fba`.** This bullet read *"AND IT REFINED THE TO'S OWN
> TABLE ... the TO's section-1 table reads as though the SEDOL limb is what protects ICT and MER."*
> **Applying `3.0.0_SA_CVO~Z`'s check from 16797 -- name the artifact that would be WRONG if a
> stranger read it tomorrow, then GO OPEN IT -- I opened both candidates and BOTH REFUTE ME:**
> ```
>   TO section 1     "ICT 6455819 -> no padding passes CUSIP mod-10 . VALID SEDOL -> untouched"
>                    It ALREADY RECORDS the CUSIP-check failure that is exactly why ICT survives
>                    the mutant. It lists BOTH limbs' verdicts per row and claims nothing else.
>   test docstring   "Section 5 is the one that matters ... they are why the SEDOL limb is not
>                    decoration."  -- 0.4.0_DS_ClientPlatform~Y stated the design outright.
> ```
> **The mutant CORROBORATED a design both documents already carried. It refined neither, and both
> `0.4.0_DS_ClientPlatform~Y` and `2.0.0_SA_COO~Z` had it right before I ran it.** The measured facts
> are unchanged; what changes is that this is a CONFIRMATION, not a discovery. **What survives is
> narrower and still worth having: the mutant EXERCISED the claim instead of reading it, and it
> names which single assertion carries the limb.**
>
> ⛔ **SECOND AMENDMENT, on `2.0.0_SA_COO~Z` 16801 -- I ran the same 16797 check against THIS
> correction and it fired again, on a file I had already amended once.** The paragraph above read
> *"and `2.0.0_SA_COO~Z` routed it onward (16789 §4) under my discovery framing, which is why the
> retraction had to travel."* **A stranger reading that tomorrow would believe a live route exists.
> Two things are now measured and neither supports it:**
> ```
>   (i)  ROUTE WITHDRAWN   2.0.0_SA_COO~Z read test_to13_cusip_repair.py themselves and ruled
>                          "a regression owner receiving this route would be told something the
>                          suite already documents and already guards. NOT WARRANTED."
>   (ii) ROUTE NEVER RAN   they grepped every inbox: ZERO recipients outside that thread. 16789 §4's
>                          "I am not letting it sit in a report" named no recipient, so it sat in
>                          exactly that report.
> ```
> **Correct state: no owner, no route, nothing outstanding.** The confirmation lives in the instance
> and goes nowhere, which is where `2.0.0_SA_COO~Z` ruled it belongs. ⭐ **Corroborated
> independently by `0.4.0_DS_ClientPlatform~Y` (16802) on their OWN mutant run: under the disarmed
> limb ICT and MER still passed and only the BBB rows failed** -- two seats, two instruments, same
> result, and it was never a gap in the suite.
>
> ⚠ **AND THE SHAPE IS THE ONE I MYSELF REPORTED AN HOUR EARLIER.** My §2 self-report was *"a
> derived fact does not chase down the artifacts it invalidates."* This is its mirror: **an
> over-claim rides the same carriers a finding does, and the volume of propagation reads as
> corroboration.** Five carriers -- instance, log, commit `58e5631fba`, RAVC2, and COO's reply --
> and not one of them was a check, because **nobody opened the two documents the claim was ABOUT.**
> `3.0.0_SA_CVO~Z`'s one-line check caught it on its first application, at a cost of two `sed`s.
- **DETERMINISM: STABLE on both instruments.** The package was independently re-downloaded and
  re-hashed (identical), and the suite re-run with byte-identical stdout under `cmp` -- which also
  establishes that its "325 of 400 sampled values are refusable" line is seeded, not per-run luck.
- **EXERCISE OF THE DEPLOYED BYTES, rc=0 captured un-piped:** the committed
  `test_to13_cusip_repair.py` run against the exact deployed member -- ABT `2824100` ->
  `('002824100','zero-pad-restored')`, ICT and MER both `as-delivered` and unchanged.

## Why no ad-hoc QA run -- named, so the wait is not a coast-failure

The standing order says fire the ad-hoc run rather than wait, unless the ad-hoc would destroy the
discriminator; name the evidence or the wait is the defect. **Here both ad-hoc routes cost more than
they buy:**

- A **fetching** run performs TrueShares issuer HTTP. The standing approval baked into
  `netassets-lambda.tf` is scoped verbatim to a **"STANDING DAILY cadence"**. An extra pull widens
  Andrew's word, and a seat does not adjudicate that wider OR narrower.
- The zero-egress route, `ETFS_REPLAY_FROM_BRONZE=1` against a past date, **WRITES**
  `silver/holdings/{that date}.parquet` and would overwrite a SERVED past-date artifact.

The scheduled fire is ~7h away and free. In its place I ran the strongest thing that touches
nothing: the committed suite against the deployed bytes, plus the mutant.

## Decisions Made

1. **Acked the HALT gate on CONTENT, not age.** Both messages (4349, 4355, both 8 days old, both
   `2.0.0_SA_COO~Z`) read in full: withdrawals of `D7_TICKETING` apply TOs, stating in terms
   "nothing to approve, decline or hand back; neither is a gate". Neither STOP-class, neither
   touching ETFS. **No HALTGT pass is cited anywhere as evidence of anything.**
2. **Put the event-gated acceptance legs in the SAME ledger as the deploy legs** rather than closing
   a deploy record while its own acceptance was unmeasured. Consequence: AC1 says "opened AND
   closed" and the entry is still open. **Flagged in the instance rather than smoothed**, so the
   validator can score AC1 FAIL if the literal reading governs.
3. **Did not consume messages 4349/4355 into `read/`.** They are addressed to the BASE serial;
   draining another seat's inbox is not a lane's call.

## Files Modified

| Path | What |
|---|---|
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/ETFS_POSITIONING.TO-14-AE_PROOF_OF_SPEC.json` | New. 4 criteria, VALID, violations=0. |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ETFS_POSITIONING.TO-14-AE.identifier-repair-apply.md` | `<status>` pending -> active, state token PLAIN (a bolded token has rendered a face wrong here before); verified `[ACTIVE]` in `to-check`. |
| `org/critical_paths/change_management/20260829T1410Z_..._deploy_completion.md` + `.open_deploys/....json` | Ledger + sentinel; L1-L3 closed. |
| `infra/aws/lambda/ci/lambda-source-map.json` | `artifact_sha256` advanced by the builder (Rule 4). |

**No `.py` was edited this session** -- the code half was `0.4.0_DS_ClientPlatform~Y`'s and shipped
verbatim, so `commit-gate.sh` had no `.py` to gate.

## Blockers

**NONE at this seat.** Nothing in this face waits on anyone.

## Current State

`etfs-netassets-daily` is LIVE at `CodeSha256 rznYiHb5PiktdT/V7Ayls0djByQdvuJ9nQeVQsIS2gI=`,
deployed 2026-08-29T14:17:24Z, carrying BOTH `353c4b5a00`'s CUSIP repair AND `e692db801c`'s Z-S31
`RunDateFabricationGuard`, verified by byte-identity against the build input with two negative
controls. **`POS-TO14-AC1` + `POS-TO14-AC2` PASS; `POS-TO14-AC3` + `POS-TO14-AC4` are
`UNCOMPUTABLE-BY-CONSTRUCTION` on two NAMED fires.**

⛔ **THE FIRM TOKENS ARE NOT DECORATION HERE -- `0.4.0_DS_ClientPlatform~Y` (16802) CAUGHT A
NUMBERING COLLISION IN MY OWN PROSE.** `ETFS_POSITIONING.TO-13-DS` has its own `AC1`-`AC4`, and they
are DIFFERENT CLAIMS: TO-14-AE's are about the APPLY landing; TO-13-DS's are about the SERVED
artifact carrying the repaired identifier. **I wrote bare "AC1 + AC2 PASS" in four messages and in
this log.** The instance itself was always safe -- its criteria are firm-tokened `POS-TO14-ACn`,
which is exactly what that convention is for -- but **the prose travels further than the instance,
and a reader carrying "AC1 + AC2 PASS" across the two faces closes TO-13-DS on evidence that does not
touch it.** `0.4.0_DS_ClientPlatform~Y` measured the discriminator: the newest silver partition is
STILL `2026-08-28.parquet`, written 22:00:16Z on 08-28, which **PREDATES the 14:17:24Z deploy** -- so
TO-13-DS's ACs have no post-change row to read and stay UNCOMPUTABLE. **Bare AC numbers retired from
this log; use the firm token or name the face.**

## Next Steps

- **[any seat, after 2026-08-29T22:00Z]** Close L4 / score AC3 on `silver/holdings/2026-08-29.parquet`.
  EXPECT: ABT `cusip 002824100`, `cusip_basis zero-pad-restored`, `cusip_as_delivered 2824100`;
  ICT `6455819` and MER `B247XZ6` both `as-delivered` and unchanged.
- **[any seat, after 2026-09-01T13:00Z -- NOT BEFORE]** Close L5 / score AC4 on
  `gold/holding/date=2026-08-31/holding.parquet`. EXPECT the 0-of-8 population to go **6 -> 5 of
  189** (four CASH rows + `2602335D`, which stays null BY DESIGN), ABT at 8-of-8, ICT and MER still
  8-of-8. ⛔ **Do NOT score this on Monday** -- see THE FINDING.
- **[`2.0.0_SA_COO~Z`]** RAVC2 sent. Validate, or return REWORK against the AC text. Two OBSERVATION
  items are yours in the surprises section below.

## Surprises (channel: `3.0.0_SA_CVO~Z`, class OBSERVATION, standing INERT -- not chased)

1. **The `etfs-netassets-daily` package has no `BUILD_MANIFEST.json`**, so the builder's layer-
   dependency check is ADVISORY and `requests` is undeclared -- "a layer import is indistinguishable
   from a missing module". PRE-EXISTING (the prior artifact had none either) and the import IS
   satisfied by the pinned layer, so the package is sound. Owner is the producer's lane, not this face.
2. **Messages 4349 and 4355 will fire the HALT gate on every future apply by any lane of
   `0.7.0_AE_CloudOps`**, costing each one a full read of two 8-day-old withdrawals. Friction, not
   risk. Addressed to `2.0.0_SA_COO~Z`, who authored both.
