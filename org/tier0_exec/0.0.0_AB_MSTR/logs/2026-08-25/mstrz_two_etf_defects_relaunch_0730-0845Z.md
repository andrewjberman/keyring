# MSTR~Z 0730-0845Z: both ETF defects fixed to production in 72 minutes -- and I shipped four broken retrievals doing it

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE, DEPLOY

Seat `0.0.0_AB_MSTR~Z`, site Z. Follows `mstrz_adhoc_proof_and_render_0230-0520Z.md`.

## 1. THE DIRECTIVE AND THE OUTCOME

Andrew, ~07:3xZ: *"i need all of that fixed, bring your fabric back online with the express
instruction that they are to fix this and only this, verify visually that it is fixed (and confirm
pipelines are scheduled/robust), commit, push / prod-deploy, and do all necessary logging."*

```
origin/PROD  a7a7ff16   Deploy to Production SUCCESS   site index.html @08:42:19Z
DEFECT A  Asset Sub-Categories: ["-","N/A","N/A","N/A","N/A"] -> 12 rows, all four books
DEFECT B  SALXX -> "State Street U.S. Government MMKT"   FXFXX -> "First American Treasury
          Obligations Fund" (the meaningless 01/01/2040 gone)
```
**Six seats relaunched from zero at 07:35Z. Fix in production 72 minutes later.**

## 2. BOTH OF HIS HYPOTHESES WERE WRONG, AND DIAGNOSING BEFORE SPAWNING IS WHAT MADE IT FAST

He asked *"data lack or frontend mapping?"* and *"missing terraform apply or something?"* **I measured
both BEFORE the spawn, so the brief carried answers instead of questions.**
- **A: FRONTEND MAPPING.** `PositioningSummary.tsx:361` gates the whole panel on `attributionData`,
  a MODELS-only feed, `:562 enabled: caps.attribution` OFF in ETF mode. The artifact already carried
  `sub_asset_class` on every holding, 13 values. **Not a bug -- a deliberate decision that predated
  the ETF path** (its own comment says *"disabled rather than fetched-and-ignored"*), correct when
  written, defective when the ETF path started carrying the data. **Seventh instance of the class.**
- **B: TWO INDEPENDENT REASONS, NEITHER TERRAFORM.** `get-item etf-classifications SALXX` -> EMPTY
  (positive control QQQ present, negative control discriminates), AND the producer never reads that
  table (`:822` takes the issuer's raw string from silver). **Terraform manages the TABLE, never an
  ITEM.**

⭐ **AND HIS CONDITION (ii) FROM 08-24 *WAS* DEFECT A** -- caught by `0.2.0_DT_PortfolioAnalytics~Z`
40 minutes after I wrote the opposite into the promote-authorization record. See s.4.

## 3. WHAT THE FABRIC DID WELL, AND IT IS NOT THE FIX ITSELF

- ⭐ **`0.4.0_DE_ClientPlatform~Z` HELD a one-line, auto-fixable, obviously-correct deletion** because
  it was not theirs to make (`PerfrpTable.tsx:29`, under Andrew's DEV-only hold). **Three seats
  converged on that line within minutes; DE~Z was the one who did not act.** A scope fence only
  costs you something when it stops an act you want to take.
- ⭐ **`0.4.0_DS_ClientPlatform~Z`'s fallback design is the whole fix**: `DISPLAY_NAME_OVERRIDES.get
  (ticker.upper(), NAME)` -- **falls back to the INCOMING NAME, never the key.** The falsified
  seeder remedy used `.get(ticker, ticker)`, which writes the literal `"SALXX"` and presents as
  success. **Same idiom, opposite blast radius.** They also marked the FXFXX string
  `DERIVED BY THIS SEAT, NOT HIS WORD` in the code -- separating a ruling from a judgment, in the
  artifact, where the next reader gets it free.
- ⭐ **DE~Z's scale control beat the one I asked for.** I asked them to hand-check arithmetic. They
  used **two independently-computed panels in ONE screenshot agreeing to the digit**: the
  sub-category column sums 99.80, the asset-class bars on the same image read 0.58 + 99.22 = 99.80.
  **A fraction-scaled column would read 0.998 against bars saying 99.80 and could not pass.** A
  control the author cannot accidentally satisfy; hand arithmetic by the code's author is not.
- ⭐ **DS~Z stopped a false claim of mine before it reached Andrew** (s.4), and **COO~Z re-derived it
  independently rather than relaying** -- naming that amplifying-without-checking had become a
  pattern in themselves.

## 4. MY OWN ERRORS -- FOUR BROKEN RETRIEVALS IN ONE HOUR, ALL CLEAN CONFIDENT ZEROS

| # | claim | mechanism | caught by |
|---|---|---|---|
| 1 | promote condition (ii) MET | verified the DATA plane + his confirmation of a DIFFERENT panel | DT~Z |
| 2 | "zero commits since relaunch" | `git log --since='07:35'` reads **LOCAL** -> 11:35Z -> future | me, late |
| 3 | "EventBridge ZERO rules at hour 11" | `cron(0 11 ` **PREFIX** generalised to "hour 11". Truth: 9 | DS~Z, re-derived COO~Z |
| 4 | "14 messages, ZERO render evidence" | `ls -t \| head -12` + keyword grep, **no positive control** | COO~Z |

>> **EVERY ONE RETURNED A CLEAN, CONFIDENT ZERO WITH NOTHING IN THE OUTPUT NAMING ITS OWN SCOPE.**
A zero invites no suspicion -- had any returned 3 I would have questioned it. **I have been the
loudest voice in this fabric about exactly this class all night.** <<
⛔ **AND A FIFTH, THE MOST DANGEROUS, CAUGHT BY MY OWN POSITIVE CONTROL:** verifying the promote
merge I ran `git worktree list | awk '{print $2}'` -- **the worktree path contains a space**
(`C:/Users/Opal Bloomberg/...`), so every check ran against a PATH FRAGMENT. Output: parity "0
bytes", both fix-greps "0", and **`PROD ancestor? NO -- STOP`**. **A BROKEN RETRIEVAL PRODUCED A
CONFIDENT STOP ON A HEALTHY PROMOTE, with two readings that looked like corroboration.** Caught only
because I asked *does this ref resolve at all*. **`0.7.0_AE_CloudOps~Z` independently hit the same
space-in-path class the same hour.**
✅ **THE ONE THAT WORKED EVERY TIME: a positive control.** It caught #5 and would have caught #4 in
one line.

## 5. THE HOLD, AND WHY IT WAS RIGHT FOR THE WRONG REASON

I refused to push PROD without a render. `2.0.0_SA_COO~Z` pressed on NEVER#6 (open ledger on a
merged-unpushed ref). **I declined on RISK, not process:** PROD then rendered `'—'`, a visible
defect; an unverified fix could ship a POPULATED panel wrong by 100x -- **invisible, on a page whose
job is proportions.** `tsc rc=0` and `build rc=0` cannot separate those; both scales compile and
render. **NEVER#6 offers two exits and rollback was fully available, so the hold was compliant.**
⛔ **But my stated premise -- "no render exists" -- was false (#4).** The render existed and answered
2 of 3 questions; only Q3 was genuinely open, because DE~Z's first fixture was the **PRE-FIX**
artifact and the SALXX publish landed 8 minutes later. **Right conclusion, wrong reason, and COO~Z
was right on both halves.** I withdrew the 10-minute rollback clock; DE~Z re-rendered in ~6 min.

## 6. CURRENT STATE

- **origin/PROD `a7a7ff16`** (ls-remote) · **origin/DEV `f67b3a48`** · **origin/SITEZ `e4b241a80f`+**
- **Served artifact** 126,809 B @08:31:06Z, `data_as_of 2026-08-24`, vocab 13 over 187 rows.
- **`/integrate merge` leg 1 LANDED** (overlap 6/363 = 1.65%, 26 objects deployed = ceiling exactly).
  **LEG 2 (SITEZ->CLOUD) OUTSTANDING at the base fabric.**
- ⛔ **AT ANDREW, none blocking:** the **Polen/Opal branding divergence** on DIVZ/IDVZ (CLIENT-FACING,
  LIVE, filed-not-fixed by DS~Z under the fence) · **`PerfrpTable.tsx:29`** -- one line, restores the
  DEV compile gate, untouched by anyone · **PERFRP on PROD** under his DEV-only hold (data gate held,
  no wrong figure reachable) · **FXFXX display string** (DS~Z's derivation, not his word).
- ⚠ **DEV CI has not type-checked or built since 02:08:25Z** -- ESLint fails at step 7, steps 8-11
  SKIP. `deploy.yml` runs typecheck+build but NOT eslint, a **controlled absence**, which is why PROD
  compiled correctly throughout. **Local `tsc` is the estate's only compile signal on DEV.**
- ⚠ **Leftover promote worktree DIRECTORIES**: `.runtmp/portal-promote-20260820T183300Z/` (5 days) +
  today's two. Registrations pruned, directories persist.

## 7. COMPILER TOOLS

| tool | use | result |
|---|---|---|
| `aws dynamodb get-item` + both controls | is SALXX in etf-classifications? | **PASS -- EMPTY with QQQ present and a bogus key returning None. The controls are what made the zero a finding.** |
| `git ls-remote` | every push oracle (DEV, SITEZ, PROD) | PASS -- never the local ref, never the report |
| `./node_modules/.bin/tsc -b --noEmit` | pre-push compile gate | PASS rc=0 -- **mandatory because CI cannot** |
| `gh run list --json headSha` | CI on the promoted sha | PASS -- Deploy to Production SUCCESS |
| `git worktree list \| awk` | resolve the promote sha | **FAIL -- space in path, produced a false STOP.** Use `git -C "$WT" rev-parse HEAD` |
| `git log --since='<UTC-looking string>'` | progress counting | **FAIL -- reads LOCAL. Use `%cI` and compare instants** |

**Gap found (unchanged, now with a second instance):** nothing routes *"is this commit on any remote
branch"*. `git branch -r --contains` is the answer and sits in no comp-tool -- **the estate's
push-state law still has no instrument.**
