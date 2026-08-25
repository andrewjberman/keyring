# 2.0.0_SA_COO~Z -- ANDREW-DIRECT two-defect relaunch: sequencing, rulings, and five claims stopped before Andrew

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Window:** 2026-08-25 ~07:45Z -> ~08:35Z (session start; no prior log this session)
**Serial:** `2.0.0_SA_COO~Z` (PID 36468) | **Directive:** ANDREW-DIRECT ~07:3xZ, "fix this and only this"

---

## 1. LAUNCH

- `/watcher`: registered; persistent inbox Monitor `bojq9zzft` armed, `TaskOutput` = running.
  No orphan watcher existed for this serial (`ps` = 0 matches). Prior session read OFFLINE (PID 15352).
- `org/XXX.md` startup done. **Step 1b-F COO row: BOTH scoped `/drive` re-arms are struck/discharged
  (the 2026-08-11 and 2026-08-20 clauses). No live authorization -> ARMED NOTHING. ZERO crons.**
- Merge window (MSTR~Z 07:11Z) verified CLOSED before any commit: no `.git/MERGE_HEAD`.

## 2. WHAT I OWNED: SEQUENCING, NOT DISPATCH

MSTR~Z had already assigned all five lanes at 07:38Z. I did **not** re-dispatch. My product was the
cross-lane sequencing no single seat could hold:

- **THE THREE RUNGS** (adopted verbatim by `1.0.0_SA_CTO~Z` as the acceptance structure):
  RUNG 1 local render (DE~Z) proves CODE - RUNG 2 published artifact (DS~Z + AE~Z) proves DATA -
  RUNG 3 production render (DT~Z) proves CODE+DATA+DEPLOY. **Rung 1 does not imply rung 3**, and
  rung 3 was falling into the seam between "DE built it" and "DT shipped it".
- **RUNG 2 ORDERED 2a/2b** after `0.4.0_DS_ClientPlatform~Z` raised the publish-first hazard:
  deploy the Lambda FIRST, then invoke. Refined again later (sec. 5 #3).
- **STATE CORRECTION carried to all seats:** ETFS_POSITIONING was ALREADY on PROD (v2.1.165,
  `d9a98bcc` @05:47:35Z, `etfAdapter.ts` present at `Positioning/shared/`). Several seats spawned
  holding the pre-06:00Z "PROD has no ETF adapter" belief. This promote ships two fixes onto a LIVE
  page, which raises the passenger bar.
- **PROMOTE PASSENGERS measured for DT~Z** (`origin/PROD..origin/DEV` = 4 commits) and surfaced that
  one is a SECOND ADVI_PERFRP commit -- routed to CTO~Z, NOT adjudicated by me.
- **`PerfrpTable.tsx:29` RACE CLOSED.** Three rulings inside 59 seconds; `0.4.0_DE_ClientPlatform~Z`
  held a live Tier-1 delete order that a Tier-0 seat prohibited 59s later. I closed it out loud once
  all three positions converged (CTO~Z reversed to (b) at 08:03:29Z -- the only ruling written with
  the full picture). DE~Z was explicitly waiting for someone to say so.

## 3. RULING ISSUED -- Z-S48, AS NAMED DISARM OWNER

Ratified `0.4.0_DS_ClientPlatform~Z`'s 2-ticker scope (SALXX + FXFXX) on a distinction the row did
not draw: **UNREADABLE VENDOR STRING** (vendor cruft -- share-class tokens, a maturity date; what
Andrew reported) vs **MERELY UPPERCASE** (JPM/MRVL/VZ -- correct name, wrong case) vs **LEGITIMATELY
UPPERCASE** (BP/GSK/MPLX -- Andrew's product fork).

**AMENDED MY OWN PUBLISHED ACCEPTANCE ORACLE, 4 names -> 2.** The oracle (msgs 8457-8461) fixed its
values in advance and would have **FAILED THE CORRECT FIX** -- loudly, because it was deliberately
built to be unpassable-by-changing-something -- at the moment somebody verified a sovereign-ordered
change. The 4-name oracle is SUSPENDED, not deleted: it remains the oracle for the case-normalisation
defect. **Z-S48 stays UNDER_INVESTIGATION / ARMED; tonight's act did NOT disarm it.**

**FINDING ON THE ROW'S OWN DETECTOR:** FXFXX is **not all-caps**, so Z-S48's predicate never saw it.
The row already recorded that the detector cannot separate correctly- from wrongly-uppercase INSIDE
its match set; this is the mirror failure OUTSIDE it. All-caps was a PROXY for "a vendor string that
is not a display name", and it over-matches and under-matches simultaneously. **Its count of 7 is
neither a floor nor a ceiling.**

Durable at `org/tier1_exec/2.0.0_SA_COO/deliverables/ZS48_ORACLE_AMENDED_TONIGHT_CHANGES_TWO_NOT_FOUR_20260825.md`
@`ab272bf71d` -- **landed LOCAL, rides integration.** Carrier note IN the file: `org/surprise_channel/**`
is the CVO_WORKSPACE lane (my own 2026-08-24 ruling), so the row on disk still carries the 4-name
oracle until CVO~Z applies it. The divergence is named rather than hoped past.

**HOLD DISCHARGED:** my 06:00Z "does a non-ETF row belong in `etf-classifications`" hold. The shipped
fix writes NOTHING to that table, so the write I was holding does not exist. A hold on an act nobody
is performing is a phantom gate; released in writing by the seat that set it.

## 4. GROUNDING FINDING -- THE SERVED ARTIFACT WAS NOT PRODUCED BY ITS PRODUCER

Correlated S3 object versions against CloudWatch invocations:

```
SERVED NOW  04:53:51Z  126,863 B  vJ1OASSl  -> NO Lambda invocation, ANY of 11 etf log groups
            04:45:15Z  125,915 B            -> EXACT match to producer stream lastEvent 04:45:15Z
   08-24    23:12:42Z / 23:00:45Z           -> match streams to the second (POSITIVE CONTROL x3)
   08-24    12:30:47Z + the 08-21 versions  -> PREDATE the log group (created 22:52:48Z)
log group age 9.4h  ->  ZERO 13:00Z instants elapsed in its lifetime
```

**The artifact on the client-facing page was produced locally, from this workstation.** Three versions
correlate to a stream to the second, so the absence is MEASURED, not a blind spot.

**REFINEMENT I ADDED to CTO~Z's "the schedule has never fired":** true, but it has never had the
OPPORTUNITY -- nothing is failing. Today's 13:00Z is the first, and it is simultaneously the
schedule's acceptance event and the first production publication of the SALXX fix. CTO~Z amended
their own deliverable @`1dbddf6fdb` off this ("TRUE AND TOO COARSE -- the coarseness hid the rung").

## 5. FIVE CLAIMS STOPPED BEFORE THEY REACHED ANDREW -- THREE OF THEM MINE

| # | claim | disposition |
|---|---|---|
| 1 | **MINE, never sent:** "the prescribed fix ships GICS, which Andrew said to replace" | **FALSIFIED BY ME** before sending. ETF-mode GICS ordering is wired (`bookSet.ts:193`, `sectorSortKey`) and cites Andrew-direct ~23:44Z "order by the economy code" -- 8h LATER than the condition. Three measurements had supported it. |
| 2 | **MINE, SENT to 6 seats:** "`current_holdings[code]` does not exist; use `portfolios[code].holdings[]`" | **WRONG-PLANE. RETRACTED BY ME.** True of the ARTIFACT, false of the COMPONENT'S PROPS -- `etfAdapter.ts:128-131` downgrades that shape to `{ticker,weight}` (anchored grep: 2 `sub_asset_class` hits, ZERO in the A-form). Would have aggregated 187 rows into one `undefined` bucket and rendered an empty panel that reads as a failed fix. Caught by CTO~Z; I re-verified at source before retracting. **DE~Z never took it.** |
| 3 | **MINE, amplified twice:** "deploy-first makes 13:00Z a verified no-op / D5 skips" | **FALSE. D5 CAN NEVER FIRE** -- `generated_at` sits inside the hashed body (DS~Z exercised it both ways). **DS~Z had ALREADY RETRACTED it and their retraction was in my inbox while I was measuring.** I re-broadcast a retracted mechanism to six seats. Remedy unchanged, justification inverted: 13:00Z overwrites UNCONDITIONALLY, so look at the Lambda's output before it writes unattended. |
| 4 | fabric-wide: "EventBridge has ZERO rules at hour 11" | **FALSE -- NINE fire in hour 11.** The 0 is a `cron(0 11` PREFIX test; none fires at minute :00. **I carried this myself in msg 8668.** DS~Z caught it; **I re-derived independently** (137 rules materialised client-side, hour FIELD parsed). True + stronger claim: ZERO rules match bbg/bloomberg/terminal at ANY hour (positive control `etf` = 8). |
| 5 | DE~Z's IDVZ filing: "the 3.18 gap is ICT+MER plus 2602335D" | **DOES NOT RECONCILE.** ICT+MER = 2.69 against a 3.18 gap; 2602335D is on PFDE and has weight 0. **TWO components:** the book's own total is 99.51 (not 100) PLUS 2.69 sitting off-axis. PFDE sums to 100.01 -- OVER. Andrew adds things up. |

**The pattern in me, banked:** #3 and #4 are both claims I amplified without checking. An originator
retracts to ONE reader; an amplifier broadcasts to SIX. Memory updated at
`memory/a-quotable-formulation-outruns-its-correction.md` -- **deep measurement is exactly when you go
blind to inbound corrections, and exactly when you are assembling the broadcast that propagates them.**

## 6. COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| (none run) | -- | -- | reason below, and it is a Rule-22a reason rather than an omission |

Every question I owned this window was an **APPLIED-plane** question: what is actually DEPLOYED
(`lambda get-function-configuration`), actually SERVED (`s3api head-object` + `list-object-versions`),
actually INVOKED (`logs describe-log-streams`), actually SCHEDULED (`events list-rules`, materialised
client-side rather than `--query` over a page). **Rule 22a states a comp-tool models DESIRED state and
cannot tell landed from planned**, so routing these through `comp-iam` / `comp-freshness` /
`comp-estate` would have answered a different question with more confidence. The HUD nudged twice on
raw `aws` inspection; I proceeded deliberately on that basis.

**Gap found: none new.** The comp-adjacent hazard re-confirmed is `comp-estate`'s served-name
evidence-class mixing (CLAUDE.md Rule-21 table) -- which is precisely why I read the served bytes
directly instead of trusting any topology or served-name claim.

## 7. FILES MODIFIED

| file | why |
|---|---|
| `org/tier1_exec/2.0.0_SA_COO/deliverables/ZS48_ORACLE_AMENDED_TONIGHT_CHANGES_TWO_NOT_FOUR_20260825.md` | the oracle amendment + the detector under-coverage finding (@`ab272bf71d`) |
| `memory/a-quotable-formulation-outruns-its-correction.md` | appended the amplify-a-retracted-mechanism mechanism (untracked memory dir) |
| this log | -- |

**MCP traffic:** 9 broadcasts (54/54 DELIVERED, 0 QUEUED, 0 REFUSED) + 1 direct to AE~Z. 17 messages
read and READ-acked: 8561, 8567, 8574, 8581, 8590, 8593, 8596, 8601, 8604, 8623, 8630, 8634, 8638,
8648, 8650, 8656, 8660.

## 8. BLOCKERS

**None at this seat.** Nothing I own is blocked and I am not holding anything.

**RESOLVED DURING WRITING:** rung 2b was unrun ~25 min after the 08:19:03Z apply; I sent
`0.7.0_AE_CloudOps~Z` a direct check-in (sequenced-behind-something, or simply next?). **AE~Z ran it
at 08:31:06Z and rung 2 is DISCHARGED** -- see sec. 11.

**ONE OPEN ITEM FOR THE FABRIC, AND IT IS NOT MINE TO CLEAR:**
`0.2.0_DT_PortfolioAnalytics~Z` is **HOLDING AT THE PUSH** with an OPEN deploy-completion ledger --
PROD merged locally at `a7a7ff16`, GATE 5 denied their `git push origin PROD` (integrator-only).
**That is the NEVER#6 merged-but-unpushed shape**, and DT~Z pre-flighted this exact denial at 08:0xZ
(msg 8647) precisely so it would not happen mid-deploy; that message went unanswered. They merged,
typechecked (rc=0), built (rc=0), and **held loudly at the only reversible point rather than
overriding.** Escalated to `0.0.0_AB_MSTR~Z` (msg 8841) with a rec of option (A) -- MSTR runs the
push, no override needed. **I cannot clear it myself: GATE 5 restricts push to `0.0.0_AB_MSTR`
serials and I am not one. That is the gate working correctly.**

## 9. CURRENT STATE (written for a reader with zero prior context)

```
DEFECT A (Asset Sub-Categories, frontend)
  portal f67b3a48 on origin/DEV (MSTR~Z pushed). One file: PositioningSummary.tsx.
  ETF rows aggregate from current_holdings[code].holdings[] (the adapter's B-form).
  Attribution stays OFF for ETFs -- there is no ETF attribution feed to fetch.
  RUNG 1 DISCHARGED ON A RENDER: 12 rows; ETF BEFORE was ["-","N/A","N/A","N/A","N/A"].
  Models regression control: two full-page PNGs, SAME sha256. tsc rc=0, eslint 0 problems.
  DE~Z's unit catch: models weight = PERCENT (sums 100.0), ETF weight = FRACTION (sums ~1.0),
  rendered via toFixed() with no conversion -- x100 applied once, at the seam.

DEFECT B (SALXX/FXFXX display name, data)
  data/etfs/scripts/gold/etf_positioning_publisher.py @2e9737af49 -- DISPLAY_NAME_OVERRIDES at the
  PLATINUM publisher (Rule 17b serving tier; CTO~Z ruled @e6e3ffa7d8, MSTR~Z confirmed).
  Fallback = the INCOMING NAME, never the key -- the property that killed remedy #3.
  DEPLOYED 08:19:03Z: CodeSha256 p/mc7hvScGyYxxMK9QY7qWQQ3gZqsWvH/GbJQVIbnvY= == staged content-sha.
  *** NOT PUBLISHED. Served artifact still 04:53:51Z; both raw strings on Andrew's page. ***
  Oracle PASSED at DS~Z: 4 of 187 ROWS (= my 2 of 169 TICKERS; SALXX in DIVZ+IDVZ, FXFXX in
  PFDE+PFOE), fields ['name'] only, mutant (fallback=key) damages 8/8 controls.

REMAINING     2b invoke (AE~Z) -> DT~Z promote from origin/DEV -> RUNG 3 production render.
              cron(0 13) fires ~13:00Z and OVERWRITES UNCONDITIONALLY. ~4.4h out at time of writing.
FILED NOT FIXED
  DEV CI has not type-checked/built since 02:08:25Z (8 red runs; steps 8-11 SKIPPED, not failed)
    -- I OWN this as carried-forward.
  PerfrpTable.tsx:29 untouched, AT ANDREW.
  Book-name branding divergence (served "Polen ..." vs shared map "Opal ...", 3 of 4)
    -- escalated to Andrew by MSTR~Z.
  IDVZ 96.82 column (sec. 5 #5) -- no "Other" bucket added, deliberately.
```

## 10. NEXT STEPS

- [`0.7.0_AE_CloudOps~Z`] Rung 2b: **invoke the DEPLOYED Lambda** (not a local run) and **READ THE
  OUTPUT** -- its last run produced 125,915 B against the 126,863 B now served; a size or row-count
  surprise is information, not noise. Then the pipelines-scheduled/robust report using the
  **name-match** form, not the hour-11 form.
- [`0.2.0_DT_PortfolioAnalytics~Z`] Cut from `origin/DEV` (= f67b3a48), re-derive the manifest AT the
  cut, ephemeral worktree (Rule 19), typecheck+build before the PROD push, ledger opened at
  deploy-start. **Rung 3 is ONE check covering BOTH defects** -- if 2b has not run, the honest report
  is "rung 3 PARTIAL", never "promoted, verified".
- [`0.0.0_AB_MSTR~Z`] Portal submodule pointer bump (bookkeeping -- does NOT gate DT's cut).
- [`3.0.0_SA_CVO~Z`] Apply the Z-S48 oracle amendment + the detector-under-coverage finding to the row
  itself; the surprise-channel tree is your lane, not mine.
- [`2.0.0_SA_COO~Z`] Carry the DEV-CI finding forward past this session. Do NOT let it die with the
  fence.

## 11. RUNG 2 DISCHARGED -- VERIFIED AT MY OWN SEAT, NOT TAKEN ON REPORT

`0.7.0_AE_CloudOps~Z` invoked the deployed Lambda at 08:31:05Z. I did not accept the report: I
diffed the LIVE served bytes against the pre-fix copy I had already pulled at 08:1xZ.

```
SERVED  08:31:06Z  126,809 B  ONaG1Gs874U9j1sB1a5if_i7zxCdBt.5
        (was     04:53:51Z  126,863 B  vJ1OASSl...)
  SALXX  DIVZ -> "State Street U.S. Government MMKT"      <- Andrew's ruling string, EXACT
  SALXX  IDVZ -> "State Street U.S. Government MMKT"
  FXFXX  PFDE -> "First American Treasury Obligations Fund"
  FXFXX  PFOE -> "First American Treasury Obligations Fund"
NAME CHANGES vs the pre-fix served copy:  4        UNCHANGED:  183
```

**THE AMENDED ORACLE HIT EXACTLY** -- 2 distinct tickers = 4 rows; 183 rows byte-identical.
**The ORIGINAL 4-name oracle would have FAILED this correct fix.** The amendment (sec. 3) earned its
keep roughly 40 minutes after I wrote it, which is the strongest argument I have for amending a
control the moment its scope moves rather than after it fires.

**AND THE SEQUENCING WORRY RESOLVED THE RIGHT WAY: 2b landed BEFORE the promote**, so rung 3 will
verify BOTH defects in one look instead of showing Andrew a half-fixed page. That was the entire
reason for raising it at 08:2xZ.

**Directive status at log close:** Defect A fixed + rendered + pushed (`origin/DEV` = f67b3a48);
Defect B fixed + deployed + published + verified on served bytes. **Rungs 1 and 2 discharged. The
only remaining acts are the PROD push (MSTR~Z), rung 3 (DT~Z), and AE~Z's pipelines report.**
