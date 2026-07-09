# `Sole` was in the negative space: a sovereign ruling turned on 6,063 accounts nobody's question contained (lane ~B)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE, SCRIBE

**Agent:** 0.4.0_DS_ClientPlatform~B
**Window:** 2026-07-09T21:36Z -> 22:20Z (delta since `71e826e81`)
**Commits:** `37cecb3fe` (decision brief). **No code touched.**

---

## Current State

CTO GO'd a read-only dataflow trace: does any serving artifact consume `accounts_dimension.account_type`
(0/10,545 non-null)? **Answer: yes -- `D_00` -> `gold/artifacts/filters/dimensions.json`, "Account Type" filter
renders with 0 options.** Verified on the SERVED object (LastModified `2026-07-09T09:53:12Z`), not source.

- **S2, not P0** -- argued down against CTO's pre-registered trigger and accepted. An empty dropdown is not a
  wrong number. CTO then named the deeper thing himself: **his trigger bound severity to the READER'S IDENTITY,
  itself a proxy**, and would have fired on `D_04` -- a grep false positive that reads `account_type` off the
  *populated* silver parquet. **Four of eight candidates were false positives, including a trigger.** A
  pre-registered trigger exists to defeat motivated reasoning at the moment of discovery; that one was
  proxy-bound. **The night's thesis ate its own countermeasure.**
- **`D_00b:1314` loads the column and never uses it.** Loads-and-discards. Invisible to any loader/column-list
  trace; it reads as a consumer.
- **The inversion, now fabric law:** the filter draws `values` from `account_type` but filters on
  `account_owner_type`. The null column is an **accidental safety**. Populating it -- the obvious `A_00` fix --
  fills the dropdown with 30 options of which **28 select zero rows**. Visibly-broken becomes silently-wrong.
- **Andrew ruled (A)** (`4146d7455`): repoint `values` -> `account_owner_type`. I declined to recommend; the
  trade (label fidelity vs coupling a client-facing control to the upstream fragility that has frozen the served
  AUA for nine days) is a product judgment, not an engineering one.

Brief: `docs/briefs/bd-account-type-filter-semantics-decision-20260709.md` (`37cecb3fe`).

## `Sole` -- the part COO asked be kept in my words

**I nearly did not print it.** The overlap table answered the question I was *asked* -- which options match rows
-- and `Sole` is in neither domain the question named. I printed the full three-way split because *"what would
not have surfaced"* had become reflex by then, and `column-only` was simply the third cell of a table I was
filling in for completeness.

```
in BOTH     -- work by coincidence :  Joint, Trust                  ( 2 of 30)
values-only -- select ZERO rows    :  IRA Brokerage RothIRA + 25    (28 of 30)
column-only -- never offered       :  Sole   <- 6,063 accounts, the LARGEST cohort
```

**The finding that decided the ruling came out of the negative space, not the query.** A sovereign decision on a
client-facing control turned on 6,063 accounts that appeared in **neither half of the question anyone had asked**
-- printed only because completeness had become a habit rather than a virtue.

COO's framing, which is better than mine: *every instrument that failed tonight failed by reporting confidently
on the thing it WAS looking at. `Sole` is what that looks like from the other side -- the answer sitting in the
cell nobody's query addressed.* Filling in the third cell is the same discipline as bounding a negative. It is
cheap, it feels like padding, and it is where the answer was.

## Two hazards I refused a sovereign-derived dispatch over -- both accepted (`49867f5f4`)

**1. The fix deploys itself into the run we are all watching.** `safe-deploy.sh` (Rule 13) auto-deploys
`data/black_diamond/scripts/gold/*.py -> opal-data-bd` **on push**. So step 1 or step 2 landing tonight makes new
code **the code the ~04:00Z gated gold executes** -- the un-freeze run, already a one-in-three coin flip on
`perf.date.max()`. And step 2 edits **`D_00`**, which is not merely the filter producer: it holds the served AUA
via `_resolve_served_aua` / BRANCH-A (`b5a95c9f5` -- my own L5 guard). COO: *"a fresh agent reading `4146d7455`
would have deployed into the window on my authority."* I checked what a **push** does, not what an **edit** does.

**2. `ABSTAIN` is an unratified verb whose two readings differ by an estate.**
- *abstain from the ENRICHMENT JOIN* -> columns stay null, output byte-identical, producer loud. **Loud-and-null.**
- *abstain from WRITING `accounts_dimension_latest.parquet`* -> **17 consumers** lose the artifact
  (`A_01 A_04 B_00 B_01 B_02 C_00 C_01 C_02 C_03 C_05 C_06 C_07 D_00 D_00b D_00f D_01 D_04`), including `C_02`'s
  certification and `D_00`'s served output. **Loud-and-gone.**

**The guard's trigger -- a 0-row allocations partition -- is TRUE RIGHT NOW.** Reading 2 does not fail rarely; it
fails tonight, on the first run. I did not pick a reading, and did not ask COO to. Routed to CTO for verbatim
ratification. Same shape as `NFRA_EDGES.P3`'s `req1` verb, ratified accept-side because its literal reading was a
grounded corruption.

COO's generalization, worth more than the catch: ***a verb is a wrapper.*** `ABSTAIN` names a behaviour without
specifying which behaviour -- exactly as `comp-freshness` names "freshness" without specifying which property,
and `gap_pct` names a "gap" between two operands that fail together. **Ratify the property, not the name.**

## Sequence (GO given, gated)
1. **CTO ratifies ABSTAIN**, verbatim. Nothing before it.
2. After 04:00Z closes + `0.6.0` reports: open a deploy ledger (NEVER#6 -- a code-prefix deploy), implement step 1,
   **exercise BOTH directions** -- it must **alarm on the 0-row stub** and **stay silent on the real 07-08
   partition.** The positive control is the whole test; a guard that alarms on everything is the cry-wolf failure
   with the sign flipped.
3. Then step 2 (`D_00`: `values` -> `adim['account_owner_type']`), verified on the **SERVED**
   `filters/dimensions.json` after the **next scheduled** gold. **Never an ad-hoc run** (NEVER#4).
4. **Step 3 (populating `account_type`) stays PROHIBITED** until CTO + COO lift it in writing. The reason goes
   **in the code at the site**, the way `_drift_warn_alert` carries CTO's promotion conditions -- because
   *"repoint the values"* and *"populate the column"* are one keystroke apart, and the reason stops being obvious
   the moment the dropdown works. **A prohibition must outlive the memory of why it exists.**

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-pipescript io` | `A_00`, `A_04`, `A_01`, `D_00` | PASS -- gave the 17-consumer blast radius that made hazard 2 legible; a grep could not have |
| `comp-grep` | `account_type\|account_registration_type` over bd gold | PASS -- 8 candidates, and **establishing nothing** was the point |
| `comp-pipescript deployed` | `D_00.portal_aggregates.py` | PASS -- `4 MATCH, 0 STALE`; proved the auto-deploy hazard is live, not theoretical |
| `comp-surface-check` | `list-watched-files` | PASS -- `D_00`/`A_00` are NOT watched critical surfaces (checked rather than assumed) |

**What worked:** `comp-pipescript io` is the reason hazard 2 is a paragraph and not an outage. "17 consumers" is
not a fact a careful reading of `A_00` produces; it is a graph query.

**Gap found:** no comp-tool resolves *"which FRAME is this column read from?"* -- the exact question that
separated `D_00` (real consumer) from `C_02`/`C_04`/`E_19`/`D_04` (silver readers) and `D_00b` (loads-and-discards).
`comp-blast` works on functions, `comp-pipescript io` on artifacts; column-level frame provenance is unserved,
and it is the question this trace turned on.

---

## Blockers

**BLOCKED-EXTERNAL (evidence-cited, not idling):**
- **[1.0.0_SA_CTO]** verbatim ratification of the `ABSTAIN` verb. Nothing I write can precede it.
- **[1.0.0_SA_CTO]** the independence trade on `8abaaa87d` (single-sourcing `_qualifies_as_held` removed the only
  cross-check that worked); COO recommends *share the predicate for the LABEL, keep the DERIVATION independent
  for the VERDICT, make disagreement a reportable finding.*
- **[0.6.0_AE_PartnerETL]** where `perf.date.max()` lands at ~04:00Z -- decides whether the un-freeze fires at all.
- **[2.0.0_SA_COO]** the live clean-fabric pass of `fabric-check --blocks` (Defect 2 is `exercised-in-fixture`,
  **not** `exercised-live`; neither of us is claiming it).

## Next Steps
1. **[1.0.0_SA_CTO]** Ratify `ABSTAIN`. Rule the independence trade.
2. **[0.6.0_AE_PartnerETL]** Ground `perf.date.max()` before 04:00Z; report post-run.
3. **[0.4.0_DS_ClientPlatform~B -- me]** On the verb + the window: ledger -> step 1 (both directions) -> step 2
   (served verify) -> stop. Step 3 prohibited.
4. **[2.0.0_SA_COO]** Report the live clean `--blocks` pass when the fabric goes clean on its own.
