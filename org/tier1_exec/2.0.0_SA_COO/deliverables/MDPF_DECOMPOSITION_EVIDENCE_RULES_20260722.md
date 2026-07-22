# MDPF Decomposition — Evidence Rules Binding on the COO

**Owner:** `2.0.0_SA_COO` · **Written:** 2026-07-22 ~1633Z · **Status:** BINDING on me at decomposition time
**CVO-verified:** `/molecule` @2cb4b2e67 (`3.0.0_SA_CVO`, main lane per LD-0325) — **facts accurate,
3 inference defects found, all corrected below.** Survived 6 of 8 of its own rules on the first pass.

> **RULE IDs ARE `D#` — "DECOMPOSITION". DO NOT CITE THEM AS `R#`.**
> CVO WATCH-2: CTO's plan carries **R1–R13**, where `R2` already means both *the coverage-denominator
> rule* and *"Cottonwood joins the trading-day axis."* **A TO citing "R2" is ambiguous.** These were
> `R1–R10` until 1645Z; renamed to close the collision. **Any citation of "COO R#" predates this file.**

> ## ANDREW-DIRECT — ROUTED TO CVO FOR `/molecule`
> **VERBATIM, ~2026-07-22 1635Z, at the COO terminal:**
> > ***"Give this to CVO to /molecule"***
>
> **Target of "this":** this file, at `@83800a6cb` (pushed, origin/CLOUD `@399d6f834`).
> **Routed to `3.0.0_SA_CVO` (main)** — CVO confirmed the lane is his, not `~Z`'s.
> **Recorded + broadcast same turn** (CTO @163735Z, MSTR @163757Z) per `org/XXX.md`.
> **Sequencing was left to CVO and deliberately NOT ranked by the COO. The question then dissolved:
> CVO was 12 of 12, not 4 of 12 — the `/verify` completed at `399d6f834`, the same commit this file
> was pushed under.** Nothing slipped; there was never a conflict to rank.
>
> **A NOTE THE VERIFIER SHOULD NOT HAVE TO FIND FOR HIMSELF:** several rules below — **D3 above all**
> — were **written by the agent they constrain, about defects in his own evidence.** That is exactly
> the provenance a verifier should distrust. **Authorship here is a reason for a harder pass, not an
> easier one.** *CVO's DIG-1 below is that pass earning its keep: I was about to strike the only limb
> pointed at the worst defect in the plan.*

## Why this file exists

Andrew set the resumption path at ~1552Z: *"send to CVO for review and /verify of assumptions.
Then we can issue to COO for decomposition of TOs and dispatch."* **I am the step immediately after
the gate.** The rules below were derived today, in MCP threads, from defects found in evidence I was
going to sign. **A bound whose only carrier is a message is a clock with no keeper** — and I am
between resets. This is the carrier.

> **⚠ CVO WATCH-1, UNRESOLVED AND STATED PLAINLY: this carrier has ONE consumer, who is also its
> author, and NOTHING READS IT AT DECOMPOSITION TIME.** It correctly stops being a message-bound.
> **It does not thereby become a gate.** Until something reads it, its enforcement is my own
> diligence — *which is the thing this whole document argues is not a control.* **Closing this is a
> decomposition item, not a note.**

---

## D1 — Quote the READ fraction. Treat token/absence/alias sweeps as LEADS, NOT CLEARANCE.

`0.4.0_DE_ClientPlatform` ran doctrine §7f against his own four census fractions (@64c3ed4b1).
**Three of four FAIL** — **and CVO's DIG-3 adds a fourth failure that is mine, not his:**

| axis | denominator derived from | verdict |
|---|---|---|
| A firm-token | files containing a token **from a list he chose** | HIS CONFIG — **FAILS** |
| B arity (read) | **lines read / total lines in the file** | THE WORLD — **SOUND, per file** |
| C absence | the enumerated lists **he decided to diff** | HIS CONFIG — **FAILS** |
| D alias | the alias set **he defines** (bd/inf/cot) | HIS CONFIG — **FAILS** |
| **E file-set** | **WHICH FILES get read — an enumerated list somebody chose** | **MY CONFIG — FAILS** |

**DIG-3, and it is D1's own objection unapplied to itself:**
> **"X is 31% read" is evidence about X. "Phase 0 is 10/33/31% read" is evidence about THREE FILES
> CHOSEN BY THE INSTRUMENT.**

**So the read fraction is sound PER FILE and config-derived ACROSS FILES.** Quote it per file, name
the file, and **never aggregate it into a Phase-0 completeness number** — aggregation silently
re-introduces the defect the rule exists to prevent.

**Consequence for TOs:**
- *"the firm-token sweep found N sites in area X, so X is enumerated"* → **UNSAFE.**
- *"`<file>` is 31% read"* → **honest and actionable.**
- **Fewer confident cells, more explicitly-open ones.**

**This reframes DE's `bd` hole from a mistake into a symptom.** A's denominator was his to define, so
any token he failed to think of is invisible **to the fraction AND to any review of the fraction**.
Nobody auditing the number could have caught `bd` — the number never had a slot for it.

## D2 — A coverage fraction is only evidence if its denominator comes from OUTSIDE the instrument's own configuration.

Doctrine §7f @f9f6a4c72, from `0.7.0_AE_CloudOps`. Three live signals satisfy the coverage-fraction
rule **while lying**: `count_axis_source_audit` (hardcoded keys), `keys_staged: 7` (literal),
`all_present` (`len(PUBLISH_MAP)` — **CVO confirmed at `publisher:103,106`**).

> R10 was not insufficient because it was wrong. **It was insufficient because the defect could
> satisfy it honestly.**

**Ledger convention:** record what each denominator is derived FROM.
`"9/9 where 9 = len(PUBLISH_MAP)"` and `"9/9 where 9 = keys actually staged"` render identically and
**only the second is evidence.**

## D3 — Every co-sign limb states (a) coverage, (b) its FALSIFIER, (c) whether that falsifier is REACHABLE, (d) what its DENOMINATOR IS DERIVED FROM.

**A limb whose falsifier cannot occur is STRUCK, not passed.** It may still run as a regression
tripwire, **explicitly labelled NON-PROBATIVE.**

**Example 1 — STRUCK, stands.** 49F count axis: *"407 of 407"* is an instrument artifact →
UNBOUNDED-BY-CONSTRUCTION.

**Example 2 — ⚠ CVO DIG-1: MY CLASSIFICATION WAS PREMATURE. THE LIMB IS NOT STRUCK. IT IS DEFERRED.**
I classified *"every pre-07-21 Global value is byte-identical with Cottonwood absent"* as **TRUE BY
CONSTRUCTION** because Cottonwood holds **2 data days** (CVO independently confirmed: exactly 07-21
and 07-22, zero pre-07-21). **The NUMBER is right. The INFERENCE carried a hidden assumption** —
*"cottonwood has no pre-07-21 data"* ⟹ *"cottonwood in the fold has no pre-07-21 effect."*
**FALSE under the all-or-nothing null rule** (`dim_mdpf_aggregate_aua_timeseries.py:1226-1240`):

| build | pre-07-21 row |
|---|---|
| cottonwood **absent from fold** | the number |
| cottonwood **in fold contributing nulls** (what CTO's R2 mandates) | **`None`** |

**Not byte-identical. The limb FAILS — and what it catches is exactly the pre-07-21 NULL-WIPE from
CVO's verify §7. Its falsifier is REACHABLE, so D3's own criterion does not apply.**
**Striking it would have removed the only limb pointed at the worst defect in the plan.**

**HONEST DEPENDENCY, and it cuts both ways (CVO's own caveat, kept):** §7 is a **derived prediction
about unbuilt code.** If S2a is built with **pre-onboarding-absence = ZERO**, cottonwood contributes
0 pre-07-21, the row computes identically, and **my classification becomes correct.**
> **DISPOSITION: DEFERRED until S2a's null-handling is decided. Do NOT strike it, and do NOT
> reclassify it probative either.** The same limb is genuinely non-probative under one design and
> genuinely load-bearing under the other.

**The irony is worth keeping because D3 is a good rule:** it exists to strike limbs that *would pass
with a broken pipeline* — **and I applied it to a limb that would FAIL with the specific breakage the
plan is about to introduce.**

## D4 — Coverage does not compose across agents. Keep limbs unmerged.

Two agents each correctly reporting their own honest denominator **can still compose a false picture
of the whole.** Live instance — `publisher/promote`, three cells that must not merge:

```
publisher / IAM face       CLEAN on firm axis (wildcard, no firm enumerated)   -- a real pass
publisher / PUBLISH_MAP    TWO-FIRM. Hardcoded 9-entry dict, no Cottonwood.
                           At cutover: 9/9, all_present=True, COTTONWOOD UNSERVED.  [CTO R13]
publisher / producer logic NOT COVERED BY ANYONE  <-- MY CLAIM, UNVERIFIED BY CVO.
                           An absence claim needs a stated denominator; I have not stated one.
```
**"Publisher: IAM clean" and "publisher: blocked" are both true and either alone is misleading.**
The composite is the COO's to hold; no lane can catch this from inside its own limb.

## D5 — The axis list is OPEN. Every fraction is PROVISIONAL.

Four axes: firm-TOKEN · unnamed-ARITY · ABSENCE · ENCODING-BY-ALIAS.
**Each was discovered BY A FAILURE, NOT BY A REVIEW** — two from `0.7.0` hitting walls, one from
CVO's A11 FAILING, one found **by accident** in DynamoDB while verifying something else (CVO confirms
this himself). **Not one came from anyone auditing the taxonomy.**

> A census cannot state its own completeness. It can state which kinds of encoding its instruments
> can return, and how many kinds it has been surprised by. That number is four, today, and the
> honest expectation is that it is not final. — `0.4.0_DE_ClientPlatform`

**Corollary — CVO: "the sharpest line in the document," endorsed without reservation, and it belongs
in CTO's plan and not only here:** discovery is failure-driven, so the axis list grows exactly as
long as work keeps hitting walls. **During a hold, work stops hitting walls — so axis discovery stops
too.** The enumeration is the one thing that should still be running.

## D6 — A set-difference is sound ONLY if the list and the population share a KEY-SPACE.

Firm-keyed lists (IAM Resource sets, argparse choices, `FIRM_CONFIG`): both sides are firms, diff is
sound — this caught the `AssetsRevampSilverRead` omission. **Date-/partition-keyed lists: establish
the key-space FIRST.** `fact_model_aum_daily` is **RUN_DATE**-partitioned with full history inside
each partition (**1,225 distinct data days — my claim, UNVERIFIED BY CVO**); counting run-date folders
as data dates yields a confident, specific, **wrong** absence of eight July days that do not exist.

## D7 — Do not decompose on a STALE verify predicate. ⚠ THIS RULE'S OWN PREDICATE WENT STALE IN MINUTES.

**AS WRITTEN 1633Z:** *"CVO's verify is testing 12 assumptions; 8 are unverified and A11 has already
FAILED — a decomposition drafted now would bake in the assumptions the verify exists to test."*
**AS OF `399d6f834`: 12 of 12. ZERO unverified.** The verify completed **at the same commit this file
was pushed under.**

**No fault on either side — I wrote an accurate number and CVO's next action invalidated it.** CVO
flagged it as **the strongest available evidence that hazard #4 is real:** *a cascade sourced from a
message cannot detect its own supersession* — **demonstrated on the document that names it, within
minutes of it landing.**

> **THE RULE THAT SURVIVES: do not decompose against a REMEMBERED verify state. RE-READ THE VERIFY
> STATUS AT DECOMPOSITION TIME.** (This is D9 applied to myself. The original predicate was a fact
> with a shelf life; the rule is not.)

**What was preparable then and is preparable now:** the **FIRMSEP.11** onboarding frame — structural,
assumption-independent. A content-layer phase Andrew-direct deferred 2026-05-07 (*"cant be implemented
yet"*), **never given a task order**; FIRMSEP.10 shipped only the tenancy/routing half. The placeholder
TO's authoring trigger reads *"COO authors TO file when product timeline materializes"* — **that
trigger condition came true with nobody watching it.** The slot is mine.

## D8 — Decompose against the ONBOARDING sequence, not against remaining WS numbers.

**This is a FIRM ONBOARDING, not a data fold.** A plan built on the onboarding checklist answers
*"firing from the hip"*; a plan built on remaining WS numbers is the same reactive mode with a
document attached.

**MDPF is the LAGGARD, not the FRONTIER — and CVO says state this at FULL STRENGTH:** 3-firm canonical
tuples in `etfs-canon-fanin:47` and `opal-assets-daily-emitter:696` are **DEPLOYED AND EXERCISED**
(his A3), not merely present. Every MDPF two-firm site is **known-divergent from a SHIPPED, RUNNING
pattern.** That should raise confidence in the estimate, not lower it.

## D9 — A MESSAGE IS A NOTIFICATION. IT IS NEVER AN AUTHORIZATION.

> **The authorization lives in the DURABLE CARRIER. RE-READ THE CARRIER AT FIRE TIME.**
> **Nobody has to reach the agents carrying a stale ruling, because nobody fires on a carried ruling.**

`0.0.0_AB_MSTR`, ~1639Z. **The supersession problem is unfixable at the message layer** — a message is
a snapshot with no back-channel — **so it must not be solved there.** My 25-second-stale relay **was
not a failure of care; it was a message being used as an authorization.** *Nothing I could have
checked would have helped, which is exactly the tell that the layer was wrong.*

**Demonstrations, same day, none aware of the others:** I re-verified the ETag pin **at fire time**
(data) · `0.7.0` **declined THREE authorizations it was holding** — CTO's superseded cascade, my
25s-stale unpark, Andrew's 1621Z priority (instructions) · CTO **landed 12 rulings into a carrier**
(the carrier half) · **and D7 above, where my own file went stale in minutes.**

### D9a — R1 FIRE-TIME CHECKLIST (I am the keeper of CTO's R1 trigger)

**R1 fires on ANY flip re-sequencing.** Live owner `0.7.0_AE_CloudOps`; **COO keeps the trigger.**
**When it fires I RE-READ. I do not fire on what I carry.** Read, in order:

1. `org/critical_paths/MDPF_CONSOLIDATED_PLAN_20260722.md` (R1 row) + `org/tier0/ledger/LD-0330.md`
   — **count-axis audit wiring lands before the SECOND post-flip cycle, preempting WS-5 if needed.**
2. **The count-source-audit tripwire is ARMED and NOT YET TRIPPED** (`gold/mdpf_revamp/` has no
   `cottonwood/` prefix). **The third audit leg MUST land in the SAME change as the staging loops**,
   or the nightly returns non-zero and the parity streak cannot accrue **even with perfect
   artifacts.** R1 constrains the back of that window; the tripwire constrains the front.
3. **⚠ NOT CARRIED BY ITS OWNER** (`0.4.0_DS`, 1638Z): the §7f **apply-gate** bind — *"will not land
   DS's diff as prepared"*, *"Control 5 is a precondition"*, *"one step, not diff-first-fix-after"*.
   `0.7.0`'s `@5bcd9bec5` carries **the doctrine, not the bind.** DS placed a backstop STOP atop the
   diff (`@930d85108`). **A backstop catching a bind is not the bind surviving. Treat as UNCARRIED
   and re-derive at fire time.**

**Banked from DS's second catch:** a diff header read `CTO: APPROVED AS WRITTEN 134926Z` — **true,
never retracted, three hours older than the defect.** Marked **SUPERSEDED IN PART, not deleted**
(*a removed approval reads as never-approved — a different falsehood*).
> **THE HAZARD IS NOT THE APPROVAL. IT IS THE APPROVAL WITHOUT ITS VINTAGE.**
Sibling of CLAUDE.md's *a line citation without a vintage is not a citation*, applied to
authorizations instead of code.

## D10 — An EVENT-SCOPED carrier retires with the event. Only a CLASS-SCOPED carrier survives.

`0.4.0_DS`, ~1642Z, **amending his own fix rather than defending it.** Three carriers guard the
dispatch defect — his STOP block, `0.7.0`'s ledger entry, and D9a cell (3) above. **ALL THREE ARE
SCOPED TO LANDING THIS DIFF AND ALL THREE BECOME HISTORICAL THE MOMENT IT LANDS. THE DEFECT CLASS
DOES NOT.** A future hand adding a **fourth firm** meets the identical trap with **every carrier
already retired.**

> **THE DURABLE FIX IS THE REGISTRY** — the only one still doing work in six months.
> **Decomposition consequence: the registry is ONE item, not two.** Splitting it produces two TOs
> each of which looks complete while the class stays open.

**DS's amendment against his own backstop is the model for stating a control's reach:** his STOP sits
atop **his diff document**, but the hand lands on `mdpf-daily-dispatch.sh` — **silent for anyone who
edits the marker block without re-opening his file.** *Same shape as the defect: a fix one hop
upstream of where the decision is made.*
> **A control's coverage is where the HAND lands, not where the REASONING was recorded** — and the
> honest version of a control states the hop it does not cover.

**At decomposition, every proposed control is asked: EVENT-scoped or CLASS-scoped, and how many hops
from the hand?**

---

## D11 — BINDING DECOMPOSITION CONSTRAINTS (FE workstream, `0.4.0_DE` spec @3bbdddbd1)

Andrew asked DE to land the Cottonwood FE fix set as a workstream spec:
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/WSE_COTMDL_FE_WORKSTREAM_SPEC_20260722.md`.
**SPEC ONLY — landing it is not a request to begin it.** Constraints that bind my TO-cutting:

**D11a — D6 FORKS THE WORKSTREAM. DO NOT CUT SET B BEFORE ANDREW'S MERGE-VS-ADD RULING.**
- **MERGE** ⇒ the B-items **VANISH** (`STACK_SERIES` already holds canonical keys; charts populate).
- **ADD** ⇒ **B1 is MANDATORY or EVERY Cottonwood model renders blank** — render-confirmed with a
  discriminating control @c95210ec3.
**A TO drafted now bakes in the assumption the ruling exists to settle.** This is D7 one level down.
**Set A (3) and C1 are D6-independent and can be cut whenever the gate clears.**

**D11b — SEQUENCING TRAP: B1 HAS A TWIN AT THE OTHER END OF THE PIPELINE. SEQUENCE THEM TOGETHER.**
The producer-side **`GLOBAL_MODEL_KEYS`** omission (census 4a-3) and FE's **`STACK_SERIES`** are the
**same defect at opposite ends** — closed lists that silently omit a third firm's models.
> **FIXING ONE END WITHOUT THE OTHER STILL YIELDS AN INVISIBLE COTTONWOOD.**
**They sit in DIFFERENT LANES, so they would naturally be scheduled apart.** This is the
cross-lane-composite failure (D4) as a *scheduling* hazard rather than a *reporting* one.

**D11c — THREE SILENT PER-FIRM ENUMERATIONS, NONE NAMING COTTONWOOD. PARTIAL COMPLETION IS INVISIBLE.**
`PUBLISH_MAP` · the exact-key **bucket policy** · the **exact-9 CF behaviours**.
> **UPDATE TWO OF THREE AND YOU GET A PARTIAL SERVE THAT NO SINGLE INSTRUMENT SEES.**
**These are FE's preconditions and are NOT owned by FE** (spec §3) — decomposition must not strand
the workstream behind them, and must not let them be closed independently.

**D11d — ACCEPTANCE IS A RENDER, NOT A DIFF.** Every defect in the spec was found **by reading a PNG**;
**none was visible to `tsc`, and four census limbs missed them.** Required per item: **all four
selections · a DISCRIMINATING CONTROL** (*a render that cannot fail is not evidence* — D3 applied to
FE) **· `tsc` + Surface-Check · ANDREW VISUAL SMOKE AS THE CLOSE LEG.**
**Precedent, not theory: MDPF_SCOPED required exactly that as its S5 leg and REOPENED 2026-05-29
without it** — *"data layer passed but the portal did NOT work for firm-scoped views."*

**D11e — TWO SIZING DISTORTIONS IF THE ITEM COUNT IS TAKEN AT FACE VALUE.**
1. **B1's cost is the RE-VERIFICATION, not the diff** — it changes rendering for **all four
   selections**, so the work is a **four-cell render matrix**. Size it there.
2. **A2 is a DECISION, not a cleanup.** CTO's *"narrow sibling, migrate only what must"* ruling was
   applied **deliberately** when the firm-total sites were migrated and these two were not.
   **Widening it needs CTO's acknowledgement IN THE TO**, or an implementer reads a deliberate scope
   line as an oversight and "finishes" it. *(Sibling of `0.8.0`'s unflagged rename: an undocumented
   deviation and an omission are indistinguishable to the next reader.)*

**D11f — SET C IS THE ONLY ITEM THAT PAYS FORWARD TO FIRM FOUR.** It makes the three silent per-firm
contracts **exhaustive-by-type**, as `MDPF_SOURCE_ATTRIBUTION` already is — **converting a
render-discovered defect class into a BUILD FAILURE.** By D10 it is the only **CLASS-scoped** item in
the workstream; everything else is EVENT-scoped and retires when Cottonwood ships.

**OUT OF SCOPE, cited so nobody re-opens it:** Benchmark/Peers are **firm-blind by Andrew's standing
ruling 2026-05-07** (`ADVI_FIRMSEP.md:133` — portfolios/peers/latest are permanent house view; only
`model_portfolios` was transitional), independently corroborated by `comp-cluster`. **The only
genuinely open thing there is the ATTRIBUTION SEAM, and it is a product call at Andrew.**
**`demo`'s missing MDPF registry entry is real and live TODAY but is a DIFFERENT TENANT** — fix
separately, **do not smuggle it into Cottonwood.**
**Also live TODAY and not Cottonwood-specific:** A3's AUA/AUM label contradiction affects **49F and
Inflection right now.**

## ⛔ PROHIBITION — NEVER RUN `pull_eclipse_portfolios.py` WITH `--date`

**SOURCE-CONFIRMED by the COO at `b0cad1965`** (found by `0.6.2_AE_PartnerETL~A`, verified
independently rather than relayed). **The reserved word is used deliberately.**

```
data/inf/scripts/bronze/pull_eclipse_portfolios.py @ b0cad1965
  :228  def eclipse_get(path, eclipse_jwt, timeout=60)   <- NO DATE PARAMETER EXISTS AT ALL
  :270  date_iso = args.date or <now UTC>                <- silently defaults to TODAY
  COMPLETE enumeration of every date_iso use (not a sample):
    :272 log · :296/:306/:316/:331 S3 keys · :347 metadata · :361 sentinel · :369 log
    >> NOT ONE REACHES A REQUEST <<
  POSITIVE CONTROL: asOf|as_of|effectiveDate|startDate|endDate|params.*date -> ZERO HITS
```

**`--date` IS AN OUTPUT FILENAME, NOT A QUERY.** `--date 2026-07-13` run today fetches **today's
live Eclipse state** and writes it into `bronze/eclipse/2026-07-13/` — **exit 0, `pull_complete.json`
sentinel written, mirror carries it to the monolith, silver converts it.** **A fabricated historical
partition that passes every absence check in the estate.**

> **⚠ THIS IS AIMED AT A CAREFUL AGENT, NOT A CARELESS ONE. "Verify ABSENT, never overwrite" PASSES:
> the partition genuinely IS absent, the write genuinely IS additive, 17a is respected, nothing is
> overwritten. A competent, guardrail-respecting run produces the corruption AND REPORTS SUCCESS.**
>
> **ABSENCE IS THE WRONG CONTROL WHEN THE FAILURE IS CONTENT, NOT COLLISION.** — `0.6.2`

**ECLIPSE `2026-06-01`, `07-01`, `07-13`, `07-14`, `07-15` ARE PERMANENTLY UNRECOVERABLE —
RECORDABLE, NEVER FILLABLE.** All four consumed endpoints are current-state; across the vendor's
493-path OpenAPI surface, date parameters exist **only on `/auditlog/*`**. **The plan needs a
RECORD-AND-MOVE-ON path for eclipse, not a fill path** — CTO's July matrix reads as a gap awaiting a
re-pull, which for eclipse is false and will keep sending people at it.
**ORION IS THE OPPOSITE CASE and IS recoverable** — the RAW producer died after 07-10 while the
PARQUET producer kept running; cause is **ours**, mirror and converter exonerated.

**⚠ EVERY CARRIER FOR THIS PROHIBITION IS CURRENTLY EVENT-SCOPED AND WILL RETIRE (D10):** this file,
`0.6.2`'s report, CTO's plan text, the broadcast. **The only CLASS-scoped fix is making `--date`
REFUSE rather than mislabel** — a puller whose date argument cannot reach the vendor should **error**,
not silently relabel today's data. **That is a bronze-script change (DS's lane, Rule 13), routed to
CTO, not started under the hold.** Until it exists, **a fourth firm's puller written by copying this
one inherits the defect.**

## Standing hazards to carry into any TO I write

- **`bd` does DOUBLE DUTY** — firm alias for 49financial **AND** a custody-source enum. **CVO
  CONFIRMED** at `mdpf-daily-trigger:76-84,404-411` — a real `bd|schwab` SSM switch. An alias sweep
  must disambiguate **by ROLE, not by token**, or it trades false-negatives for authoritative-looking
  false-positives.
- **`07-13/14/15` mean OPPOSITE things in two committed deliverables** — data ABSENT (eclipse) and
  data PRESENT (49F legacy-vs-serve-real). A grep hits both and cannot tell them apart; the 49F list
  reads as corroboration of a vendor outage **while proving the reverse.**
- **Three instruments that fail toward FALSE CLEAN:** `Glob`/`comp-glob` case-sensitivity ·
  `comp-grep -l` silent truncation at `--max` · run-date-vs-data-date partition counting. None
  errors; each returns a confident, well-formatted, wrong negative. *An instrument that fails toward
  FALSE ALARM gets fixed the first time it fires. One that fails toward FALSE CLEAN is only ever
  found by someone who already knew the answer.*
- **A cascade sourced from a message cannot detect its own supersession** — see D9, and see D7 for
  this file doing it to itself within minutes of landing.

## Claims in this file NOT verified by CVO — stated so nobody inherits them as verified

- D4: *"publisher / producer logic NOT COVERED BY ANYONE"* — **an absence claim with no stated
  denominator. Mine.**
- D6: *"1,225 distinct data days"* — **mine, unverified.**
