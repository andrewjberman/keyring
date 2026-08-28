# CTO~Z ARCHITECTURE + TAXONOMY RULINGS — D1 / D4 session, 2026-08-28 ~00:5x–02:0xZ

**Author:** `1.0.0_SA_CTO~Z` · **Basis:** Andrew-direct "bring tier1 agents on, they need to finish
D1 and D4", then his ~01:3xZ scope message (recorded verbatim @`7a4383d937`).

> ⛔ **WHY THIS FILE EXISTS.** Every ruling below was issued as a broker message and nothing else.
> **A ruling whose only carrier is a message is the exact stale-carrier class this seat ruled on
> three separate times tonight** (msg 11481), and it binds its author first. Message ids are cited
> for provenance, **but this file is the carrier** — a successor should not have to reconstruct a
> contract from an inbox.

---

# ⛔ READ THIS BLOCK FIRST — WHAT IS BINDING NOW

| # | BINDING NOW | msg |
|---|---|---|
| 1 | **`GICS_INDUSTRY_GROUP_NAME` lands as a NEW, PARALLEL field.** `sub_asset_class` is NOT overwritten and its value set is NOT redefined | 11382 |
| 2 | A satellite's **BOOK-GRAIN period return is PRODUCER-SIDE or RENDERED EXPLICITLY ABSENT** — never synthesised client-side from an as-of weight vector | 11464 |
| 3 | **The PRODUCER converts satellite constituent weights to PERCENTAGE (0-100).** The consumer contract does not move | 11559 |
| 4 | The **first-leg-wins guard is on `returns` AGREEMENT ACROSS SHARED TICKERS**, not on a shared `as_of` — the as_of form is WITHDRAWN (it could never fire) | 11626 |
| 5 | Satellites fetch: a **SCOPED route**, firm resolved to BUCKET never to a key segment, consumer seam is the existing default parameter | 11617 |
| 6 | **DO NOT strike** `satellites_registry.py`'s "WHY THERE IS NO PREDICATE" section — strike its TITLE and CONCLUSION, KEEP the measured sweep, and correct `:54-58` | 11583 / 11588 |
| 7 | **`BLOCKED-BY-GATE`** proposed for `PROOF_OF_SPEC.schema.json` `acceptance[].status`, **plus** the `if/then` conditional making `status_reason` required — ONE act or neither | 11448 / 11488 |
| 8 | **A DIRECTIVE OR STATUS CLAIM CARRIES ITS VINTAGE**; a directive without one is a HYPOTHESIS — measure the artifact before executing it | 11481 |
| 9 | WORKING ASSUMPTION (reversible on Andrew's word): the **ETFs GICS condition-(ii) work RUNS BESIDE item 2**, not superseded — the two govern different surfaces and never conflicted | 11629 |
| 10 | **Served key = `industry_group`, OPTIONAL, snake_case** — and **`industry_group_basis` MUST be served with it**, or the value reaches the consumer stripped of its claim | 11831 |
| 11 | ⛔ **WITHDRAWN 2026-08-28 ~02:1xZ — THE PREMISE WAS FALSIFIED BY A PLAN.** I ruled the two edge changes were ONE DEPLOY. `terraform plan` reads **0 add / 1 change / 0 destroy, NO `aws_lambda_function` in the diff** — neither router is republished, and there is ONE pending edge change, not two. The edge functions track an **S3 ARTIFACT**, not `index.mjs` (`lambda-edge.tf:245-248`), so **Terraform cannot see a source edit**. ⭐ **REPLACED BY THE WORSE FINDING IT EXPOSED — see §8: APPLY ≠ SHIP on this tier.** The 11813 s.3(b) disclosure discipline survives on its own merits. | 11813 → withdrawn 11914 |

**WITHDRAWN, do not cite:** *"the AE half may be DONE"* (11649 — the route is DESIRED, **not
deployed**: 0 of 26 cache behaviors) · *"condition (i) reads DISCHARGED on the data plane"* (11370 —
see §5) · the `as_of` form of ruling 4 · the re-mint **directive** limb of 11559 (the unit ruling
stands; the WRITE authorization was the issuer's, 11594).

---

## 1. RULING 1 — industry group is a PARALLEL field (Rule 24)

A naive swap of `sub_asset_class` to the industry-group grain **fails three postulates**:
**(i) MECE** — GICS industry groups classify EQUITIES; every non-equity row (money-market security,
canonical cash line, synthesized residual, the fixed-income sleeve) becomes uncovered.
**(ii) SAME GRAIN** — sector and industry group are two LEVELS OF ONE HIERARCHY; moving only the
equity members leaves cash/ultra-short at the old level **in the same field**.
**(iii) INTENT** — `sub_asset_class` already mixes an economic-sector axis with an
asset-type/duration axis; refining one of two co-resident intents deepens the incoherence.
**(iv) STATE** — re-pointing the producer moves the 11 sector values and **nothing else**.

**Second, independent reason:** `sub_asset_class` is a RATIFIED CONSUMER CONTRACT.
`etf_positioning_gold.py:141-147` records that its two fixed-income strings were byte-verified
against `SUB_ASSET_CLASS_ORDER`, `SUB_ASSET_COLORS`, and HoldingsTab's sort — and warns **in source**
that a near-miss spelling *"does NOT fail loudly … presenting as a SORT BUG on the consumer's surface
rather than a producer defect."* Replacing 11 known values with 24 unknown ones walks every row into
that at once, **and it ships green**.

## 2. RULING 2 — book-grain satellite performance

Blending period returns by a snapshot weight vector **assumes the weights held still across the
window**, and for a satellite that is **false by construction** — the rebalancer artifact those
weights derive from IS the record of the weights changing. The failure produces a plausible number
nothing on screen can falsify. **ABSENT IS A LEGAL v1 STATE**; not zero, not an ambiguous em-dash.

⚠ Scope: this governs the **BOOK grain only**. The **holdings-grain** Performance grid needs no blend
arithmetic at all — a ticker's return is a property OF THE TICKER, carried not blended, and it is
built, exercised, and populated 110/110 on the served artifact.

## 3. RULING 3 — the producer converts units

`satelliteSet.ts:44` declares `weight` a PERCENTAGE (0-100) and `:48` **names the converting party in
advance**: *"fraction or a percentage is TO-1's measurement to make and to convert AT ITS boundary."*
The defect was a **missed conversion at a named boundary**, not a contract gap. Do NOT relax
`validateSatellite` or widen its epsilon — that trades a loud named refusal for silent 1/100th weights.

## 4. RULING 4 — guard the premise, not a proxy

Withdrawn form: *assert constituent books share an `as_of`.* **`as_of_date` is null on 5 of 5 books**,
so the comparison passes universally — **a control that cannot fail.** Replaced: **when a ticker
appears in more than one leg, assert its `returns` agree.** It needs no vintage field, and its
failing condition has already been exhibited (a planted 0.11 / 90.11 discriminator, where 90.11
vanished silently). Remedy on disagreement is **SURFACE**; refuse-vs-surface is the DE lane's call.

⚠ `prior_date` varies 2-across-5 and is **NOT** a vintage signal — my reading (it is a REBALANCE date)
is an **inference, unverified**. If it holds, no field on this contract expresses per-book data
vintage, and that is a producer-side gap rather than a frontend assert.

## 5. §5 — WHAT I GOT WRONG, so a successor does not inherit it as fact

| I claimed | Truth | Caught by |
|---|---|---|
| "GOLD HAS NEVER RUN" (relayed) | running daily, `run_class: scheduled`, 3 days | my own measurement |
| condition (i) DISCHARGED on the data plane | **4/4 FULL is a LUCKY TUESDAY** — `build_tables` takes ONE `as_of` for four funds; a late fund renders SHELL. TO-7 | `2.0.0_SA_COO~Z` |
| the satellites fetch prefix | `/api/scoped/satellites/` — built that way **by my own B1 ruling** | `0.7.0_AE_CloudOps~S` |
| "the AE half may be DONE" | route DESIRED, **0 of 26 behaviors deployed** | `0.7.0_AE_CloudOps~S` |
| binding-now row 11 says strike | I contradicted **my own table** without reading it | myself, late |
| ULT = Ultra-SHORT → ladder broken | **Ultra-LONG.** No anomaly ever existed | `0.4.0_DS_ClientPlatform~L` |

⛔ **THE COMMON MECHANISM: I reasoned from a SUMMARY of my own ruling instead of the ruling.** A
handoff, a status line, a binding-now row quoted from memory — **lossy copies that read as
citations**, so the usual tell never fires. My own handoff said *"START AT THE BINDING-NOW TABLE"*;
I skipped it and quoted the table's contents for six hours.

⭐ **What bounded the damage: every wrong claim carried a label** (REPORTED-not-measured, a pattern
not evidence, a relay). Labels did not prevent the errors — one reached the sovereign — **but every
one was falsified by a peer within minutes.**

## 6. §6 — THE CARRIER CLASS, measured (the session's largest tax)

**EIGHT instances, three distinct mechanisms**, each true when written:
- **STALE VALUE** — "GOLD HAS NEVER RUN" (08-24 figure relayed 08-28 without its vintage) → a whole
  seating ranking rebuilt.
- **STALE STATUS/DIRECTIVE** — `D1_NAMEDISCOVERY` TO-1/2/3 reading ACTIVE over accepted+certified+
  pushed work; `ETFS_POSITIONING` **five** faces reading ACTIVE over a live daily producer; the
  `D1-i-2` launch directive naming work completed 2h earlier → **seats spent and re-dispatched**.
- **SCHEMA-VERSION GAP** — `ETFS_POSITIONING.TO-7`, an ANDREW-DIRECT P1, authored in a pre-`<issued_to>`
  format, rendered `[??] (unassigned)` by the board tool **every seat is told to run**. It sat three
  days. **17 of 101 TOs render `[??]`**, and several are RECORDS that correctly have no assignee —
  so a genuine unowned P1 was **camouflaged by legitimate noise** (Rule 24 (i)/(iii) failing on the
  DIRECTORY as a type).

⭐ **The receiving half paid for itself four times**: `0.4.0_DS_ClientPlatform~Q` refused a false
re-dispatch, `0.7.0_AE_CloudOps~Z` refused a spent directive, `0.7.0_AE_CloudOps~S` tested a route
instead of building it, `0.7.0_AE_CloudOps~I` checked a build input and found a package that would
have **written gold and died before platinum** on a client-facing key.

---

## 7. §7 — RULING 11 IN FULL: why the collision is not a race

`portal-auth/cloudfront-distribution.tf:60/:66/:68` — both routers are resources in ONE stack, both
bound by `qualified_arn`, and the file's own comment records *"qualified_arn auto-bumps every deploy
since `publish = true` on each edge"*. DENOMINATOR: **1 CloudFront distribution in the account**
(`EVTSA9VEHNZVH`, 26 behaviors, NextMarker absent), so "possibly the same distribution" had no other
outcome available.

⛔ **A RACE IMPLIES ONE APPLIER WINS. HERE BOTH CHANGES LAND EITHER WAY** — the only question is
whose acceptance criteria have run when they do. **The real hazard is a change GOING LIVE BEFORE ITS
OWN ACCEPTANCE RUNS.**

⛔ **AND THE CONTROL THAT WORKED ON THE LAMBDA WILL NOT CATCH IT.** `0.7.0_AE_CloudOps~I`'s "8 of 9
resources unchanged" was sound because there the blast radius WAS the diff. Here the plan *does* show
the movement — a `qualified_arn` bump — but an applier reading *"arn version changed"* does not read
*"and the other lane's feature is now live."* **THE PLAN SHOWS THE MECHANISM AND HIDES THE MEANING**;
a seat can run a disciplined plan review and still not know what it shipped.

⚠ **STANDING PROPERTY, NOT A REGRESSION.** Both routers have always shared this stack. Tonight is
simply the first time two lanes hold pending edge changes at once — when a latent coupling becomes a
live one. **Do not refactor the stack against a clock**; separating the routers has its own blast
radius and is not this session's work.

---

## 8. §8 — RULING 12 (replaces the withdrawn 11): **APPLY ≠ SHIP ON THE EDGE TIER**

`0.7.0_AE_CloudOps~S` ran the read-only plan that falsified their own collision claim, and it exposed
something worse. The plan's single change is:

```
+ path_pattern = "/api/scoped/satellites/*"
+ lambda_arn   = ...:function:shared-advisor-router:24
```

⛔ **IT WIRES THE NEW ROUTE TO v24 — THE ARTIFACT PUBLISHED 2026-08-21T16:00Z. THE SATELLITES BRANCH
WAS COMMITTED 2026-08-27T22:42Z. v24 DOES NOT CONTAIN THE SATELLITES CODE.** The route would go live
pointing at a router that does not implement it.

**AND IT IS SILENT IN EVERY DIRECTION A SEAT WOULD CHECK:** a behavior exists → green. A router is
attached → green. The apply succeeded → green. **The behavior census that CORRECTLY proved the route
was not deployed (0 of 26) would flip to 1 of 26 and read as success — the same instrument that
established the gap would falsely certify its closure.**

>> **RULING: THE ARTIFACT MUST BE REBUILT AND PUBLISHED BEFORE, OR IN THE SAME ACT AS, THE BEHAVIOR
   THAT POINTS AT IT.** A behavior added ahead of its router version is a half-landed deploy in which
   **the visible half is the one that works.**
>> **ACCEPTANCE BAR:** the artifact at `portal-auth/shared-advisor-router.zip` must contain the
   satellites branch, **VERIFIED BY CONTENT** (a token present in the new branch and absent from v24,
   with a negative control), and the pinned version must be the one containing it.

⛔ **THIRD INSTANCE TONIGHT OF "THE PLAN SHOWS THE MECHANISM AND HIDES THE MEANING"** — after the
Lambda member list (gold written, platinum dead) and the collision this seat wrongly ratified. **The
plan is correct and complete about what Terraform will do, and that is exactly why it misleads: the
thing that must happen first is not in Terraform's world.**

---

*Push state is stated in the broadcast that accompanies this file, measured, never defaulted.*
