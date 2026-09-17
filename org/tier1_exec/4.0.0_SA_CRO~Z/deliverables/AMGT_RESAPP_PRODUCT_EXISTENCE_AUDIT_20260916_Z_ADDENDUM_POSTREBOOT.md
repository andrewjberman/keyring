# AMGT_RESAPP -- PRODUCT EXISTENCE AUDIT, ADDENDUM: the served plane re-measured after the 07:56Z reboot

**Author** `4.0.0_SA_CRO~Z`. **Written** 2026-09-16 13:45-13:58Z at HEAD `933a40dab2` (SITEZ). **Push state:** LOCAL
(LD-0522; `0.0.0_AB_MSTR~Z` pushes; none requested). **Extends** `AMGT_RESAPP_PRODUCT_EXISTENCE_AUDIT_20260916_Z.md`
@`a10eece02e` (PRD v0.8) and `AMGT_RESAPP_POST_ROUND12_RESIDUAL_PROJECTION_20260916_Z.md` @`1d5454312a`.

**Why now.** Site Z rebooted at 07:56:32Z and every ~Z seat and the six round-12 workers died with it. Andrew-direct
~13:33Z (record @`933a40dab2`, msg 23438): pick up `/canonical-flow AMGT_RESAPP`. This seat's role on the project is
his item 5 (record @`c05a41c0f4`): refer back to the PRD and assess whether the product exists. The PRD moved
v0.8 -> v0.10 while this seat was down, and a reboot can move box-plane preconditions in BOTH directions, so the
audit's box-plane rows were perishable and are re-read here rather than carried forward.

---

## 0. THE VERDICT, UNCHANGED, WITH TWO MOVES

**Nothing on the served plane moved between 04:57Z and 13:50Z.** The four gaps G1-G4 stand exactly as measured.
Two things did move, neither on the plane a person touches:

| move | direction | evidence |
|---|---|---|
| the Bloomberg DAPI on this box is UP | in the product's favour | `bloomberg_health` 13:4xZ `ok: true`, `//blp/refdata` at `127.0.0.1:8194` (04:5xZ read `ok: false`). The model-block producer's precondition (G2) and the on-demand pull's terminal (G4) are reachable again; the producer itself is still a script a person runs |
| the union universe was rewritten by a worker whose branch is NOT merged | world ahead of record | `s3://opal-data-harvest/universe/v1/2026-09-16.json` written 07:32:10Z (pool now 133 objects, was 132); by its `resolution` field 191 MEASURED / 59 UNRESOLVED of 250 rows (the audit read 33 / 223 of 256 on the 2026-09-15 object). Its producer, proof instance and four rows `W25-S1..S4` sit on `wk-amgt_resapp-12-25` @`0a5064ded5` (rk-4), unmerged at HEAD |

**The PRD delta v0.8 -> v0.10 adds one outcome and no surface.** FWD-20 (a filings-and-history-seeded house
free-cash-flow forecast with Divergence on the Model tab, bar EXERCISED) was appended at L10 of round 11; it has no
route, no component and no producer on any plane this seat read. **1 of the 16 round-12 task orders names it**
(`comp-find 'FWD-20' task-orders/`: 3 hits in 1 of 80 files scanned): rk-5, and only for its REPORTING side --
Divergence D on the Model tab, with the order's own line *"FWD-20's house forecast does not [serve]"*. No cell produces
the house forecast itself. It is a fifth no-surface outcome beside FWD-7, FWD-12 and FWD-14, with the difference that
its producer has no cell yet. (A first draft of this line said "0 of 16"; the rail census corrected it before commit.)
The corrected contract `C-ROUND12-PULL-WIRED` (no Lambda consumer) matches this seat's projection note K.

---

## 1. THE GAPS, RE-READ (same instruments, new vintage)

| gap | 04:57Z | 13:50Z | round-12 cell that owns it | state of that cell at HEAD |
|---|---|---|---|---|
| G1 page not served | DEV `be8cf218` 0 of 48 files | DEV `be8cf218` (= `origin/DEV`) **0 of 47** files under `src/pages/SecurityAnalysis`, 0 route lines; drain `refs/drains/rj-portal` `b616b759` 47 files (this instrument is `ls-tree -r` on the folder; the earlier 48 is not re-derived here). Portal branch `wk-amgt_resapp-12-23-portal` exists, checked out in a worktree, unmerged | rk-1 (`~23`) | pending; worker died at the reboot |
| G2 model block does not reach the page | `/thesis` 200 `model_status ABSENT`, 0 figures | **same**: 200, `ABSENT`, `header_figures 0`. Adapter `opal-amgt-scoped-api` LastModified `2026-09-15T19:01:10Z`, CodeSha `9ubWPnhz`, env 2 keys (no `MODEL_BLOCK_ROOT`) -- unchanged. `derived/model_block` 14 objects / 4 keys, newest 2026-09-11 -- unchanged | rk-2 (`~24`) | pending; the never-widen halves for the model-block read are landed (`ledger/NEVER_WIDEN_ROUND12_MODEL_BLOCK_READ_{COO,CTO}_HALF.md`) |
| G3 print 500 | `/print` 500 | **same**: 500 | rk-6 (`~24`) | pending |
| G4 on-demand pull disconnected | `/refresh` 501; enqueue Lambda unwired; 0 consumers | enqueue Lambda `opal-research-pull-enqueue` unchanged (2026-09-11); **0** consumer processes on the box; queue not re-read (no change signal) | rk-7 (`~24`) | pending |
| posture route | cited Z-S107 (adapter predates the route) | **now MEASURED**: `/posture` **404** on the deployed adapter -- CODE-AHEAD-OF-DEPLOY confirmed by direct invoke **[WRONG -- CORRECTED in s.3g: no `/posture` route exists in any route table by design; posture rides the thesis and overlay bundles]** | rk-2 / rk-8 | pending |
| box collection plane | 3 of 3 Opal research tasks DISABLED | **same**: `Opal Data Harvest - Local Publications`, `OpalResearch-ExecManagement`, `OpalResearch-FilingsAnalyzer` all Disabled after the reboot (6 other `OPAL_*` tasks Ready) | reserved to Andrew (@`9db2a36cdc`) | -- |

**Why the served plane could not have moved:** the three round-12 orders that are complete (rk-9 criteria repair at
the issuer, rk-10 the social source classified, rk-11 the preserved breaches; proof instances VALID at HEAD, 3 of 3)
are record cells. None writes a route, a component, a deployment or a pool prefix a person reads.

---

## 2. THE ROUND-12 RECTANGLE AGAINST THE AUDIT (so the CTO's L10 can grade coverage, not just completion)

| audit item | round-12 cell | worker | status |
|---|---|---|---|
| G1 page onto DEV | rk-1 | ~23 | pending |
| G2 model-block read on the deployed plane | rk-2 | ~24 | pending |
| G3 print pack packaged server-side | rk-6 | ~24 | pending |
| G4 on-demand pull wired | rk-7 | ~24 | pending |
| FWD-7 / FWD-12 / FWD-14 no surface | rk-12 | ~23 | pending |
| FWD-6 compare-two-versions surface | rk-16 | ~23 | pending |
| FWD-18 the one chart | rk-15 | ~23 | pending |
| FWD-13 identity / union universe | rk-4 | ~25 | L7 done on the branch (2 criteria REFUSED with grounds), branch unmerged |
| price axis (Z-S105) | rk-3 | ~26 | pending |
| **FWD-20 house forecast** | rk-5 (reporting side only: Divergence on the tab) | ~25 | pending; **the forecast producer itself is uncut** |

Chain `~23` holds five of the seven product-surface cells (rk-1, rk-8, rk-12, rk-15, rk-16) and `~24` holds three
(rk-2, rk-6, rk-7); with both workers dead at the reboot, every product-surface gap waits on the COO's re-dispatch.
That is the COO's L7 act and this seat does not touch it; it is recorded so that a later "3 of 16 complete" is not
read as "3 of 16 gaps closed" -- **0 of the audit's gaps are closed at HEAD.**

---

## 3. WHAT THIS ADDENDUM DOES NOT CLAIM

- No FWD graded; no world act (GET invokes and reads only; no POST, no pool write, no merge, no deploy).
- The rk-4 branch's two REFUSED criteria are not adjudicated here (L9). The universe object's producer determinism
  and schema checks are the worker's own claims in its proof instance, cited not re-run.
- Whether the page builds against DEV is still UNMEASURED (merge-tree counts conflicts, not TypeScript).
- The residue the reboot left in the shared tree (a merge in progress on `wk-amgt_resapp-12-25` with the channel file
  in conflict, the stranded rows S111/S112) is the COO's; this seat read it and touched nothing.

## 3b. ADDENDUM 15:1xZ -- rk-1 is COMPLETE and the page is STILL NOT ON DEV; G1 changed class, not state

Round 12 moved to 5 of 16 terminal (rk-1, rk-4 added; rk-3 drained with AC3 FAIL-by-output). rk-1, the G1 cell, reads
`complete` with a VALID proof instance, 4 of 4 criteria PASS (`deliverables/0.9.0_WK_AMGT_RESAPP~23/...rk-1...proof_of_spec.json`,
drained @`b5882d4481`). Re-measured at 15:1xZ on the served plane:

| what | value |
|---|---|
| portal `DEV` local = `origin/DEV` | `be8cf218` -- **0 of 47** page files, **0** route lines, unchanged since the audit |
| the worker's branch `wk-amgt_resapp-12-23-portal` | tip `2453a7b4` (merge of the drain `b616b759`); contains DEV (`be8cf218` is its ancestor); 47 page files; 3 route lines; 16 commits DEV lacks; `merge-tree` against DEV = 0 conflicts |
| what rk-1 proved | AC1 the branch contains the drain and the files; AC2 `tsc -b` rc 0, 0 errors; AC3 `vite build` rc 0, 53 js assets, page token present, control absent; AC4 the gitlink and `origin/DEV` are UNCHANGED at `be8cf218` |

**So rk-1 is correctly complete AND the frontend still does not exist on the plane a person is served from.** The
order's own text reserves the DEV push (LD-0367/0368; the LD-0522 hold at `0.0.0_AB_MSTR~Z` on Andrew's word), and
AC4 asserts that DEV did NOT move. G1 moved one class: from CODE-ONLY on a drain ref to **BUILT, TYPE-CLEAN AND
INTEGRATED ON A BRANCH CUT FROM DEV, AWAITING TWO ACTS** -- (1) the merge of `wk-amgt_resapp-12-23-portal` into
local `DEV` (a COMMIT-class act under the freeze's COMMIT YES / PROMOTE NO; the earlier page-onto-DEV merge on this
box was `0.0.0_AB_MSTR`'s, `a4ef8853`), then (2) the reserved push of `DEV`. Neither is carded anywhere this seat
read: `2.0.0_SA_COO~Z`'s 13:37-15:05Z log names CARD 1 (model-block pull) and CARD 2 (filings batch) as the calls at
Andrew and nothing on the portal. **A round-12 L10 that grades FWD-15..19's carrier on rk-1's `complete` would grade a
branch, not a page.** This is the exact failure Andrew named at item 5 -- the record reads complete and the part is not
where a person would open it -- caught by measuring the served branch rather than the status field.

**CORRECTION 15:2xZ, from `0.0.0_AB_MSTR~Z` (msg 23454), corroborating every number above on a second instrument and
narrowing what the two acts BUY.** Read from `portal/.github/workflows/` on DEV: `ci.yml` runs on a push to DEV and only
lints, type-checks and builds; `deploy.yml` fires on a push to PROD; `promote-to-prod.yml` is dispatch-only. **So a DEV
push serves nothing** -- it makes the page DURABLE and CI-VALIDATED on origin, and the only served plane those
workflows touch is PROD, which Andrew's ~05:0xZ word takes off the table ("No portal promote necessary"). Also measured
there: 0 remote branches contain `2453a7b4` (positive control: 2 contain `be8cf218`) -- the whole AMGT frontend exists on
ONE DISK, the box that rebooted this morning. The sentence above, "awaiting two acts" before the page exists "on the
plane a person is served from", therefore over-claims: after both acts the page is on origin DEV and CI-green, and
nobody is served it. **Where G1 CLOSES under a no-promote definition of done -- origin DEV + CI green, a DEV-built
artifact a person can open somewhere, or something else -- is a PRD question for `1.0.0_SA_CTO~Z`**; the audit's own
G1 row was written against a served page and says so. Both pushes (DEV and SITEZ) are carded at Andrew at the
`0.0.0_AB_MSTR~Z` terminal as of 15:2xZ. (A deploy hook outside the repo's workflows is UNMEASURED by both seats.)

**RULED 15:26Z by `1.0.0_SA_CTO~Z` (msg 23459; register @`6bbc21605b`):** (a) CARD 3 -- the local DEV fast-forward and the
DEV push are ONE reserved leg at Andrew (LD-0367/0368), executed by `0.0.0_AB_MSTR~Z` on his word, CTO rec YES NOW as
durability and CI, never a promote; (b) **G1's CLOSURE CLASS for the round-12 L10: FWD-15..19 grade EXERCISED when the
BUILT page renders the header and the five tabs against the DEPLOYED adapter and that render is CAPTURED** (the goal's
DONE item 4); a local build against the deployed adapter reaches it with no push; which cell carries the capture is
carried to the L10. **What this seat will measure G1 against from here** is therefore the capture: its existence, that it
was taken against the deployed adapter (not a local one), and its vintage against the branch tip. WARN: Read beside the
rest of this record: the deployed adapter today answers the Model tab with `model_status ABSENT` (G2) and print with 500
(G3), so a capture that satisfies (b) will show a header and five tabs with an empty Model tab and a refused print --
FWD-15..19 can grade REALIZED while FWD-1 and FWD-5 stay ABSENT. That is consistent with the PRD's outcome grain (the
carrier is one outcome set, its content another) and is noted so nobody reads a REALIZED page as a filled one.

## 3c. ADDENDUM 16:1xZ -- THE SERVED PLANE MOVED BACKWARD: the adapter was redeployed by rk-2 and the routes that answered 200 now answer 500

Round 12 at 7 of 16 terminal (rk-3, rk-5 joined). Re-read of the deployed adapter at 16:10:30Z, same instrument as
s.1 (boto3 `get_function_configuration` + direct GET invokes for `BA_US_Equity` with `x-firm-id`):

| what | s.1 (13:50Z) | 16:10Z |
|---|---|---|
| `opal-amgt-scoped-api` | LastModified `2026-09-15T19:01:10Z`, CodeSha `9ubWPnhz`, 747,396 B | **LastModified `2026-09-16T15:19:34Z`, CodeSha `Di6/6ju9`, 749,036 B** -- redeployed by the rk-2 worker (`~24`); env still the two table names, no `MODEL_BLOCK_ROOT` |
| `/thesis` | 200, `model_status ABSENT`, 0 figures | **500** |
| `/print` | 500 | 500 |
| `/posture` | 404 | 404 |

So the one component s.3 of the audit called "deployed, edge-authorized and answering" no longer answers on the
Model tab's route; `/overlay` **500** on this seat's own invoke at 16:11:07Z (`"internal error in the AMGT scoped read
API"`), agreeing with `1.0.0_SA_CTO~Z`'s 15:59Z second-instrument read (tick 5 @`e987b69f1e`); `/peers` **200** at the
same instant, so the regression is on the per-security read path, not the whole function -- the discriminator that
separates a broken archive from a dead one.
**This is already RULED and OWNED, not a new finding of this seat:** co-sign AMENDMENT 2 @`aa97d2ea9f` names the
blast radius (every route the function serves, 11, where the half named two), rules ROLLBACK-FIRST with a 16:05Z bound
at `2.0.0_SA_COO~Z`, and fix-forward as packaging rather than a pool read; the CTO's 16:17Z tick verifies the rollback
or says the bound was missed. **Measured by this seat at 16:10:30Z: the regressed build was still live, five minutes
past the bound.** Recorded here because it is the product-existence fact -- for the interval since 15:19Z a person
opening the page against the deployed plane gets a header with no thesis and no overlay, which is LESS product than
the audit measured -- and because G2's mechanism (the adapter reads a folder that is not in Lambda) is now joined by a
second one on the same route (the redeployed archive fails before it reaches the read). Rollback restores s.1's
state exactly (sha `9ubWPnhz`); it does not close G2. No act by this seat: the rollback is the COO's under the ruling,
and a duplicate row on a ruled class costs a line. Next re-read: after the CTO's 16:17Z tick lands.

**CLOSED 16:39:49Z, this seat's own instrument:** the adapter reads LastModified `2026-09-16T16:18:57Z`, CodeSha
`9ubWPnhz`, 747,396 B -- the s.1 build restored, 14 minutes past the ruled bound; `/thesis` 200 `model_status ABSENT`
0 figures, `/overlay` 200, `/print` 500 -- **byte-for-byte the s.1 state.** The COO's change-management entry
`org/critical_paths/change_management/20260916T1606Z_amgt-scoped-api-rk2-rollback-20260916_deploy_completion.md`
(@`817d827e39`) opened 16:06:56Z and CLOSED; the CTO's tick 6 @`877782d502` verified it on a second instrument; rk-2
was drained OPEN (@`ec4bf1f8d0`: AC2/AC3 PASS, AC1/AC4/AC5 FAIL, rows W24-S3/S4 ARMED) and re-cut under ISSUER
AMENDMENT 9 @`1c0639a019`. Three instruments agree. The served plane is back where the morning audit left it, and G2
is exactly as open as it was.

## 3d. ADDENDUM 18:1xZ -- G2's PLANE half is CLOSED on the served plane for the first time; its POPULATION half is exactly as projected

Round 12 at 8 of 16 terminal. rk-2 COMPLETE 8 of 8 under ISSUER AMENDMENT 9 (drained @`2b6be09533`; the adapter
redeployed 17:23:29Z past a non-regression census; CTO ticks 8-9 @`79e0f6744c`). Re-read on this seat's own instrument
at 18:11:11Z, one pilot name and one non-pilot covered name:

| | adapter | `/thesis` | `/overlay` | `/print` | `/posture` |
|---|---|---|---|---|---|
| vintage | LastModified `2026-09-16T17:23:29Z`, CodeSha `x3KrEBvZ`, 754,470 B; env still the two table names | | | | |
| `BA_US_Equity` (a block in the pool) | | **200 `model_status SERVED`, header_figures 14, fiscal_year_figures 165** | 200, header_figures 14 | 500 | 404 |
| `COST_US_Equity` (no block in the pool) | | 200 `model_status ABSENT`, 0 / 0 | 200, 0 | 500 | 404 |

**So the Model tab serves figures on the deployed plane for a name that has a block -- the first movement of any
gap on the served plane since the audit.** Read against s.0 G2's two halves: the PLANE half ("the deployed adapter reads
a folder that is not in Lambda") is closed -- the rules data travels in the archive and the read reaches the pool; the
POPULATION half ("4 of 89 covered names have a block") is untouched and reads exactly as the residual projection
@`1d5454312a` said it would: a non-pilot covered name still opens to an empty Model tab, and that is CARD 1 at Andrew
(the model-block pull over the keyed names, reserved by the DAPI dependency), not a cell. G3 (print 500) and the
posture route (404, still absent from the deployed router at this sha **[MISREAD -- CORRECTED in s.3g: absent by design, not by deploy lag]**) are unchanged. The audit's component row for S1
moves from DEPLOYED-NOT-SERVING to **SERVED-PARTIAL, 4 of 89** -- the denominator is the product's remaining gap.
Non-application of the never-widen half is this seat's own read: rk-2's redeploy is inside the co-sign's named blast
radius and the census the drain cites; this seat measured the OUTPUT only.

## 3e. ANDREW-DIRECT ~19:2xZ (relayed by `1.0.0_SA_CTO~Z`, msg 23475; record @`0d780cf6f8`): the four reserved cards are answered YES

Verbatim, as relayed: *"Give me the reserved calls"* then *"Yes on all four, execute them."* What it authorizes, by
owner (the CTO's routing, not this seat's): ONE model-block pull and ONE price-axis pull over the 33 keyed coverage
names (`2.0.0_SA_COO~Z`, as producer orders; no cadence, not the 89); the filings + drafting batch over the same 33
and the BA pilot re-run (`2.0.0_SA_COO~Z`); the portal DEV fast-forward to `wk-amgt_resapp-12-23-portal` and its push,
CI only (`0.0.0_AB_MSTR~Z`); the SITEZ push and the CLOUD -> SITEZ merge leg (`0.0.0_AB_MSTR~Z`). Still reserved: any
cadence, any pull over the 89, the harvest collection mechanism, any PROD promote.

**What this moves in this record, prospectively:** CARD 1 (s.3d's population half, 4 of 89) becomes a bounded run whose
result is measurable -- blocks landed against 33 attempted, printed with the refusal list -- and the served-plane
denominator for the Model tab moves from 4 of 89 to at most 33 of 89 when it lands; CARD 3 (s.3b's G1 durability)
becomes a push whose result is `git ls-remote` on `origin/DEV`. Nothing is measured here yet: this seat re-reads the
served plane after the runs and the push land, on its own instruments, and records the numbers then. No act by this
seat on the word itself; the record is the CTO's.

## 3f. ADDENDUM 19:4xZ -- CARD 3 EXECUTED: the page is on `origin/DEV`; CARD 1 not yet landed; the SITEZ push is done

Measured on this seat's own instruments at 19:4xZ, after `0.0.0_AB_MSTR~Z` executed items 3 and 4 of the word:

| what | value |
|---|---|
| portal `DEV` local = `origin/DEV` = `git ls-remote` | **`2453a7b4`** (was `be8cf218`); a pure fast-forward (origin/DEV is an ancestor, 0 local-ahead) |
| page on DEV | **47 of 47** files under `src/pages/SecurityAnalysis`, **3** route lines in `App.tsx` (was 0 / 0 since the audit) |
| superproject gitlink `HEAD:portal` | still `be8cf218` (` M portal` in the shared tree) -- the gitlink update follows under `0.0.0_AB_MSTR~Z`'s own mechanics, per 23475 |
| workspace `SITEZ` | `origin/SITEZ` = local HEAD `6f46ed0703` by ls-remote -- **this record's push state is now ON ORIGIN**, and every hash cited above `6f46ed0703` resolves on origin |
| `derived/model_block/` | 14 objects, 4 keys, newest 2026-09-11 -- **CARD 1's pull has not landed yet** |
| adapter | unchanged at `x3KrEBvZ` (17:23Z); `/posture` 404, `/print` 500 unchanged (rk-8 completed @`128d2ad67d` without a redeploy; rk-6's is authorized by both co-sign halves and pending) |

**Read against s.3b:** G1's DURABILITY half is closed -- the frontend exists on origin, CI-validated by the repo's own
workflow on that push, on more than one disk. G1's EXISTENCE half is unchanged by construction (a DEV push serves
nothing, s.3b correction) and closes on the ruled class: a CAPTURED render of the built page against the deployed
adapter (msg 23459). Round 12 at 10 of 16 terminal (rk-8, rk-13 joined), no slug. Next re-read: when the 33-name
pull lands in `derived/model_block/` (the population half of G2) and when rk-6's print redeploy lands (G3).

## 3g. ADDENDUM 01:1x-01:2xZ 2026-09-17 -- after the 7:10 PM ET hold: the Model tab serves 33 of 89 covered names; the ceiling moved from the PULL to IDENTITY; the Lead Panel is empty on the page's own call every night; one correction

Direction: `1.0.0_SA_CTO~Z` msg 23492 (23:11Z), per Andrew-direct ~22:2xZ (record @`2eb6bec53a`): *"4.0.0_SA_CRO~Z -- re-read
the served plane now: rk-17's 33-name model-block pull landed ... and the 2026-09-15 price generation exists."* Read at HEAD
`c0aa291a17` (= `origin/SITEZ` by ls-remote). Round 12 at 10 of 18 terminal. Adapter UNCHANGED: `x3KrEBvZ`, LastModified
`2026-09-16T17:23:29Z`, 754,470 B, 0 layers.

### The Model tab (FWD-1's carrier) -- the population

| read | value |
|---|---|
| `universe/v1/2026-09-16.json` | 250 rows. COVERED = `source` coverage 83 + both 6 = **89**. Of those, keyed (`resolution MEASURED`) **33** = 27 + 6; **56 UNRESOLVED, no `security_key` at all** |
| pool `derived/model_block/` | 47 objects, **34 keys**, newest `2026-09-16T20:20:18Z` = the 33 pulled + `NVDA_US_Equity` (uncovered, 2026-09-11) |
| `/thesis` over the 33 keyed covered names, each invoked as the page's client builds the URL | **33 of 33 `200 model_status SERVED`**, header figures 9-15 per name |
| served-plane population | **33 of 89 covered names** open to a filled Model tab (at 18:11Z: 3 of 89 covered plus uncovered NVDA -- s.3d's "4 of 89" counted NVDA, which is not covered) |
| `NVDA_US_Equity` | `200 ABSENT` despite its 2026-09-11 block; outside the covered denominator; recorded, not chased |

**CARD 1 did exactly what it was carded to do, and it exhausts what a pull can do.** The remaining 56 covered names
have no canonical key, so no pull over "keyed names" reaches them: the population ceiling on FWD-1 is now the
IDENTITY layer, not the model-block producer. That partition is already carried at `1.0.0_SA_CTO~Z` (rows W25-S2,
S117, S120; the ADR-to-home-line join ruled un-guessable in W25-S2) and is not adjudicated here. Whether FWD-1's bar
reads against 89 covered names or against the keyed ones is a PRD question for the round-12 L10.

### The Lead Panel (FWD-15)

| request | `ranking_status` | rows | generation |
|---|---|---|---|
| TRENDING CHATTER, **no date** (as the page sends it), 01:19Z -> `as_of_date` 2026-09-17 | **ABSENT** "no generation pointer ... not an empty membership" | 0 | -- |
| TRENDING PRICE, **no date**, 01:19Z | **ABSENT**, same reason | 0 | -- |
| TRENDING CHATTER, `as_of=2026-09-16` | SERVED | 10 | `20260916T100027Z-efd7e544dd59` |
| TRENDING PRICE, `as_of=2026-09-16` / `2026-09-15` | ABSENT / ABSENT | 0 / 0 | -- |
| TRENDING PRICE, `as_of=2026-09-10` | SERVED | 32 | `20260916T065448Z-9b7ffda3dcdc` |

**The page's own call cannot reach any served ranking for most of every day.** `getLeadPanelRankings` on DEV `2453a7b4`
sends only `?limit` (`src/api/endpoints/amgt-lead-panel.ts:67-69`), and the adapter defaults the date to UTC today
(`lib/research/api/scoped_amgt.py:522` @`c0aa291a17`). The chatter generation writes at its 10:00Z schedule, so from
00:00Z to ~10:00Z (8 PM to 6 AM Eastern) the chatter panel is empty; the price panel is empty on every default read,
because no generation is written for the current date and the one that exists is dated 2026-09-10. The rows under
2026-09-15 are unreachable on a dated read too, which corroborates `3.0.0_SA_CVO~Z`'s row Z-S137 on a DIFFERENT
instrument (a direct invoke of the served route, against that row's store read). **Both are already OWNED:** the
default-date gap is the "dated fallback" ruled onto AMGT-rk-7 (CTO never-widen half @`7e84705c7a`, rk-7 pending), and the
price rows' shape is Z-S137. Recorded as the served-plane measurement, not re-filed.

### Unchanged since s.3f
`/print` 500 for BA (rk-6 pending). `filings/v1` 10 objects / 5 names and `drafting/v1` 5 / 5 (rk-18 not run).
`peers/v1` grew to 415 objects / 191 keys (newest 18:23Z; was 33). Portal `DEV` = `origin/DEV` = `2453a7b4` (s.3f).

### CORRECTION -- posture, three lines above
s.1 said `/posture` 404 was "CODE-AHEAD-OF-DEPLOY confirmed by direct invoke", s.3d said the route was "still absent
from the deployed router at this sha", and s.3c/s.3f tabulated it beside `/print` as an open gap. **All three are
wrong.** No `/posture` route exists in the adapter's route table at HEAD (`scoped_amgt_route_table()`,
`scoped_amgt.py:2615-2631`, eleven routes) or in the page's client, whose own comment reads *"O-1 posture (AMGT-rj-9).
No route was added for them."* (`amgt-lead-panel.ts:128-130`). Posture rides the thesis and overlay bundles: at 01:2xZ
both carry `posture` with `status SERVED` for `BA_US_Equity` (verdict `hold`, comparable `DE_US_Equity`). The 404 measured
a route nobody calls, so it could never have confirmed a deploy lag. Whether the earlier `9ubWPnhz` build carried posture
in its bundles was not read and can no longer be (that build is not deployed). The same claim went to `1.0.0_SA_CTO~Z`
in this seat's 14:07Z message and is corrected there.

**And a near-miss on this same read, recorded because it is the same instrument error:** a first pass invoked the two
keys that contain a slash (`BP/_LN_Equity`, `NG/_LN_Equity`) with the slash raw in the path, got 404 on every
per-security route, and read like two covered names that can never open. The page URL-encodes the key
(`encodeURIComponent`, `amgt-lead-panel.ts:125-151`) and the adapter splits on `/` before `unquote` (`scoped_amgt.py:2503`,
`:2545`), so `BP%2F_LN_Equity` routes and serves 13 header figures. Nothing was filed. **A direct invoke is evidence
about the page only when it is built from the page's own call.**

## 3h. ADDENDUM 02:5xZ 2026-09-17 -- rk-18's filings batch landed: thesis prose serves for 12 of 33 keyed covered names; the 21 without a reason carrier

rk-18 (worker `0.9.0_WK_AMGT_RESAPP~30`, order still pending) finished its batch at 02:34:17Z: 11 names analyzed plus the
BA pilot, USD 6.2791 on its own log. World writes read directly, then the page's thesis call for all 33 keyed covered
names at 02:52:08Z, each URL built as the client builds it:

| read | before (s.3g) | 02:5xZ |
|---|---|---|
| `filings/v1/` | 10 objects / 5 names | 24 objects / 12 key directories |
| `drafting/v1/` | 5 / 5 | 12 / 12, newest 02:34:19Z |
| thesis `drafting_status SERVED` | 5 names | **12 of 33 keyed covered names** (5 drafted sections each) = 12 of 89 covered |
| thesis `drafting_status ABSENT` | -- | 21 of 33, reason `no drafted document ... NoSuchKey` |

The batch's plan line names the 21 as UNRESOLVED-SOURCE, "each an explicit object at
`filings/v1/<security_key>/UNRESOLVED-SOURCE.source.json`"; the store holds 0 such objects and its done line counts 0.
rk-18 AC2/AC3 pass either at 33 of 33 or when every missing name carries a NAMED REASON, so that arm can read MET on the
log while no reason reaches any plane a person reads. Filed as row `AMGT_RESAPP-Z-S139` @`91fe4070e9`, mid-flight; it
resolves if the objects land before the drain. Unchanged: adapter `x3KrEBvZ`, `/print` 500, rankings as s.3g. rk-17
drained COMPLETE 5 of 5 (@`52dd9a8c37`) with Z-S137 still open, per `3.0.0_SA_CVO~Z`'s L9 record s.7 @`4ace3fa7e1`.
Round 12 at 11 of 18.

## 3i. ADDENDUM 03:2xZ 2026-09-17 -- rk-12 COMPLETE is the CLIENT half of FWD-7/12/14; the served half is rk-6 AC4 and the three routes answer 404

rk-12 drained COMPLETE @`43d24c39d0` (round 12 at 12 of 18); its drain subject reads *"three unsurfaced outcomes get served
routes and page panels"*. Measured at 03:21:44Z:

| read | value |
|---|---|
| portal `wk-amgt_resapp-12-23-portal` `f276d732` | 1 commit past `origin/DEV` `2453a7b4`: `CoverageFreshnessPanel`, `InputLedgerPanel`, `ListRegisterPanel`, `ResearchInputsPanel`, and client calls `GET {BASE}/freshness`, `GET {BASE}/security/<key>/ledger`, `GET {BASE}/lists`; `requestRefresh` now posts to `/api/private/research/pull` |
| adapter route table (`scoped_amgt_route_table()`) at HEAD as of 03:2xZ (after `e916462c65`) and on rk-6's branch `wk-amgt_resapp-12-24` | 11 entries each, **none** naming freshness, ledger or lists; the one HEAD file matching a freshness pattern is a moratorium comment in `infra/aws/terraform/harvest/dynamodb.tf:146` |
| deployed adapter `x3KrEBvZ`, the three GET routes | **404** each, "no /api/scoped/amgt route for GET ..." |
| rk-12's proof (3 criteria, all PASS) | AC2 surface tokens and reasons in the page components; AC3 the ledger classes READ-ONLY; AC4 the refresh call re-pointed on the chain's own portal branch -- **no criterion invokes a served route** |
| rk-6 AC4 (ISSUER AMENDMENT 8 moved rk-12 AC1 here) | routes naming freshness, ledger and lists in the table AND each GET answering 200 on the DEPLOYED adapter; rk-6 pending |

So the cut is correct and nothing is filed: the page half is built on a branch and the served half is a pending
criterion that measures exactly the served plane. Recorded because the drain subject says "served routes" and a
reader of `complete` would count three surfaces that answer 404. FWD-7, FWD-12 and FWD-14 remain no-surface on the
served plane until rk-6 deploys, and the panels on the branch would render refusals against today's adapter.

## 3j. ADDENDUM 03:4x-04:0xZ 2026-09-17 -- THE rk-6/rk-7 REDEPLOY: print serves, the three no-surface outcomes serve, the compare surface serves, the Lead Panel serves on the page's own call

The adapter was redeployed at **2026-09-17T03:27:57Z**: CodeSha `zHmPoWu9`, 781,832 B, **layer `opal-amgt-print-deps:1`**
(the first layer), built from AMGT-rk-6's worker branch (`wk-amgt_resapp-12-24` @`8fcb2e0e26`, 16 route entries against
HEAD's 11; rk-6 and rk-7 pending, not drained at read time). Pre-deploy state, the rollback target: `x3KrEBvZ`,
2026-09-16T17:23:29Z, 754,470 B, 0 layers. Every invoke below is built from the page client's own call.

| outcome / gap | before (s.3g-s.3i) | 03:47-03:55Z |
|---|---|---|
| **G3 / FWD-5 print** | 500 for every name | **valid PDF for 31 of 33 keyed covered names** (BA 76,184 B / 8 page objects, COST 79,887 B / 9, each `%PDF-` ... `%%EOF`); **500 on exactly the two slash keys** BP/_LN_Equity, NG/_LN_Equity -- log: `FileNotFoundError ... '/tmp/pack_NG/_LN_Equity.pdf'` (row **Z-S141**) |
| FWD-7 coverage freshness | `/freshness` 404, no route | **200**, rows per covered name |
| FWD-12 input ledger | `/security/<key>/ledger` 404 | **200** for BA, per-class sources |
| FWD-14 list register | `/lists` 404 | **200**, owners carried as UNASSIGNED with the reason |
| FWD-6 compare two versions | no surface | `/security/BA_US_Equity/versions` **200**, `/compare` **200** (model-block stamps) |
| FWD-15 Lead Panel, the page's no-date call | ABSENT on both axes overnight | **SERVED**: chatter as_of 2026-09-16, 10 rows; price as_of **2026-09-10**, 32 rows -- rk-7's dated fallback. As Z-S137 predicted, the price panel's "latest" is 2026-09-10 while 2026-09-15 rows sit unreadable beside it |
| non-regression | -- | Model SERVED 33 of 33 keyed covered; drafting SERVED 12 / ABSENT 21 (unchanged); overlay, peers, coverage 200 for BA |

**Read against the audit's four gaps:** G3 CLOSED on the served plane for 31 of 33 keyed covered names. G2's plane half
closed at s.3d, population 33 of 89 (identity ceiling). G1 durability closed at s.3f, existence still per the capture
class. G4: the refresh carrier is declared and the client posts to the enqueue route on the chain-23 branch; the consumer
side is not re-read here. **Three of the three no-surface outcomes now answer on the deployed adapter** -- but the panels
that read them live on `wk-amgt_resapp-12-23-portal` `f276d732`, one commit past `origin/DEV`, so a capture of the built
page would come from that branch, not from DEV.

**The record half of the deploy is missing:** no change-management entry exists for this deploy on either tree
(`org/critical_paths/change_management/`: 0 files touched since 00:00Z; the worker's worktree: none for AMGT), which is
the gap the worker's row W24-S7 raised before the deploy (its grant does not name that directory). Filed as row
**Z-S142** with the rollback sha, since nothing else records it; the entry is the issuer's to write. Both rows
@`13ff9bccc9`.

**UPDATE 04:4xZ -- the record half is now written, by its owners.** `1.0.0_SA_CTO~Z` row Z-S143 (04:26Z) verified the deploy
against both signed halves, found every blast-radius limb HELD, ruled NO ROLLBACK and directed a RETROACTIVE entry;
`2.0.0_SA_COO~Z` wrote it @`31efe1425e`:
`org/critical_paths/change_management/20260917T0432Z_amgt-scoped-api-rk6rk7-combined-20260917_deploy_completion.md`, opened
04:32:20Z, CLOSED 04:37:10Z, carrying the pre-act `x3KrEBvZ...` and post-act `zHmPoWu9...` hashes and a 0-diff targeted re-plan
(read here by enumerating those tokens in the file). So "no change-management entry exists" above was true at 04:0xZ and is
superseded; Z-S142's disposition is `3.0.0_SA_CVO~Z`'s at L9. `2.0.0_SA_COO~Z` row Z-S144 gives the ROOT CAUSE of the stale
price panel: `price_axis_pull.py` writes no `_CURRENT` pointer, so the 2026-09-15 rows are invisible to the pointer-based
reader and fallback -- which refines Z-S137. rk-6 drained COMPLETE @`1bc69f1b59`; HEAD's route table now carries 16 entries,
so the deployed routes are no longer ahead of the record. Z-S141 (print on the two slash keys) has no remedy yet.

## 4. INSTRUMENTS AND VINTAGES

| instrument | observes | vintage |
|---|---|---|
| `mcp__bloomberg__bloomberg_health` | the DAPI on this box | 13:4xZ |
| boto3 `get_function_configuration` x3; `invoke` GET `/thesis` `/print` `/overlay` `/posture` for `BA_US_Equity` with `x-firm-id` | the deployed adapter and what it answers | 13:50:40Z |
| boto3 `list_objects_v2` paginated (133) + `get_object universe/v1/2026-09-16.json` | the pool | 13:5xZ |
| `git -C portal ls-tree -r`, `for-each-ref refs/drains/`, `branch --list 'wk-*'` | which branch carries the page | DEV `be8cf218`, 13:4xZ |
| `Get-ScheduledTask`, `ps -ef` | box pipelines and consumers | 13:4xZ |
| `git branch --no-merged`, `git status --porcelain`, `.git/MERGE_HEAD` | the residue | HEAD `933a40dab2`, 13:5xZ |
| `.tools/proof-of-spec-check.py` on rk-9 / rk-10 / rk-11 | the three terminal orders | HEAD |
| `git diff 1170b4da69 49aedcf88b -- prd/` ; `grep FWD-20 task-orders/*rk-*.md` | the PRD delta and its coverage | HEAD |
