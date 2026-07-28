# 1.0.0_SA_CTO — MDPF_DEBTCLEAN: the design phase, locked

**archetype:** MIXED (COORDINATE + IMPLEMENT)
**Session:** 2026-07-28, ~1740Z → ~1955Z. **Delta since `dd457c01cf`** (the P0 log, 1256–1740Z).
**Lanes:** `0.7.0_AE_CloudOps` · `0.4.0_DS_ClientPlatform` · `0.2.0_DT_PortfolioAnalytics` ·
`0.4.0_DE_ClientPlatform` · `2.0.0_SA_COO` · `0.0.0_AB_MSTR`.

---

## 1. What this window was

The P0 closed at ~1740Z. This window was **design**: Andrew issued a three-part mandate, then answered
every structural question needed to lock a target layout. **The design phase is now closed and committed;
P1 has landed.** Twelve PRD commits, `6327252481` → `c7c631cb5e`.

---

## 2. Andrew-direct rulings, verbatim, in order

| ~time | ruling |
|---|---|
| 1725Z | *"We don't need freshness checkers at this point… create established, canonical routes and schedules"* → **§11** |
| 1741Z | *"trace every necessary channel… make sure that they are getting to the Gold DDB table"* |
| 1743Z | serving-bridge architecture + kill **drift opportunities** |
| 1754Z | *"I dont care about the alarm, I care that the system has clear flow end to end"* |
| 1815Z | **THE MANDATE — three parts** → **§12** |
| 1820Z | **MORATORIUM** on alerts/SES/monitors → **landed in `CLAUDE.md`, `638cf6c36d`** |
| 1834Z | *"migrate mdpf_revamp now… very explicit with the design and structure before implementing"* |
| 1852Z | platinum = `/aggregate-aua` + `/{firm}`, **no artifact-type subfolders** |
| 1858Z | `/gold/mdpf/` moves to `/portal`; **`/json` should not even be there** |
| 1906Z | **all five open decisions answered** → **§16 LOCKED** |
| 1918Z | *"a clean repoint and follow an identical pattern for each"* |
| 1930Z | canonical names as primary keys + **fix the AGG defect against the architecture, not as a point fix** |

---

## 3. THE LOCKED LAYOUT (§16) — the session's central artifact
```
ACCRUAL   opal-data-assets/portal/{layer}/{product}/{scope}/{artifact-type}/{YYYY-MM-DD}.json
SERVING   opal-data-portal-v2/platinum/{product}/{scope}/{artifact-type}.json

{product} mdpf | advi     {scope} 49financial | inflection | cottonwood | global
```
**`{product}` is a REAL level — `advi` follows the identical pattern.** That is the constraint that binds
the build: **we are not building an MDPF publisher, we are building the client-facing-product publisher and
MDPF is its first instance.**

**`portal/` is a TIER**, which resolves the grammar gap found in §15.2: the bucket had a source-scoped tier
(`{source}/{scope}/{layer}/`) and **no declared home for a cross-source aggregate**, which is why MDPF was
scattered at top level. Not arbitrary — undeclared.

---

## 4. Findings that changed decisions

**B-14 — THE FIFTH COTTONWOOD MECHANISM, and the only one enumeration could never find.** `:523`'s
AccessDenied + `|| return 1` short-circuits `:524`/`:525`, the two cottonwood emitters. **Stage 6's rc=1 and
the missing cottonwood artifact are ONE defect**, tracked separately all day by three agents. **It lived in
shell control flow, not in a list.** *(DS established; AE independently rated it above the fix.)*

**The `_interpolated` read-preference.** `load_cottonwood_slice:1552-1553` prefers a 07-23 one-off over the
daily artifact. **Even with the IAM fixed, a fresh cottonwood slice would be produced and then ignored** —
every surface signal would have said success. Found *prospectively*.

**FOUR competing display vocabularies** for the same five models (§19.1). **Root cause stated
architecturally: the display name is being used as a JOIN KEY.** A `codeMap` patched to today's strings
**would break again at cutover** — fixing against the current shape schedules the identical incident.

**Killing `json/` in opal-data-assets killed option 2b** and re-opened the fan-in fence as the critical-path
decision — **hidden while `json/` existed as an origin.** Recommendation accepted: a **separate egress
principal**, because 11 of 12 fence members are ingest roles and the publisher is the only egress one —
**a misclassification, not a carve-out.**

---

## 5. What landed

- **`MDPF_DEBTCLEAN` PRD §11–§19** — mandate · complete bucket chain · locked layout · gold + platinum specs
  · publisher + 9-row consumer re-point · naming law · consumer contract.
- **`CLAUDE.md` MORATORIUM** (`638cf6c36d`) — no alerts/SES/monitors unless Andrew asks. **Recorded as
  SUPERSEDING-BY-WIDENING the 07-15 ruling**, with the narrow scoping named as why it recurred.
- **`.owned-paths.yaml`** (`ab5987c01e`) — `org/missions/**` → TIER0_MSTR. **CTO as grantor, SoD.**
- **P1 ACCRUAL LIVE** (DS, `6493257fc`) — 11 objects, R5 exercised both directions, scopes roster-derived,
  `{product}` a parameter. **`advi` is two data entries and zero code.**

---

## 6. Rulings I issued

`global` is a scope · `{product}` is real · start-forward, no backfill · no `_interpolated` variant ·
`_audit`/`_manifests_qa` underscore-prefixed inside `mdpf/` · **refuse-to-clobber** (DS's code right, my PRD
wording wrong) · **`aum-metrics` is DRIFT not by-design** (the consumer templates on `firmId`) ·
`account-units` **left UNVERIFIED rather than ruled from the same instinct twice** · IAM before
read-preference (production before consumption) · **C1–C4 the consumer contract.**

---

## 7. Corrections against me

1. **I led with the alarm** — *"the cheapest fix on the list"* — while the mandate was already on the table.
   Andrew: *"meaningless and distraction."* **COO corrected the attribution (it originated the phrase); I
   kept my share: I am the gate on what reaches him and I amplified it unfiltered.**
2. **I ratified two COO findings without testing either** — "the set is five", then "a complete parallel
   serving namespace." Both retracted. **The pattern was the problem, not the corrections.**
3. **I recommended a bridge publish Andrew approved, then cancelled it myself** on measurement — cottonwood's
   gold was 5 days stale, so it would have recreated the split-brain my own spec forbids.
4. **AE corrected my risk framing in its own favour and flagged it anyway** — the Stage 6 grant is not the
   16:39Z shape.

---

## 8. Compiler Tools

| tool | result |
|---|---|
| `comp-routes behaviors` | established `S3-opal-data-assets` is **defined and UNREFERENCED** — the measured mechanism behind 2b's auth safety, replacing my hypothesis |
| Gate-1 rail | denied an `infra/` grep; **one rail-checked override** used with a stated reason (prefix-existence + partition grammar — neither a freshness nor a routing question) |
| `safe-commit` / `safe-apply` | 12 commits clean; **`TMPDIR` workaround holds — zero tag-gate overrides this window** |
| live S3 / DDB / IAM | the whole of §15, §16, §18.4, §19.1 |

**No comp-* query tool fitted the bucket-grammar work** — enumerating prefix shape across two buckets is not
a freshness, routing or blast-radius question. Raw `aws s3 ls` + `head-object` was the instrument, per the
standing two-stage rule.

---

## 9. Open at window end

**AT ANDREW:** nothing blocking. *(Fence decided; layout locked; publisher specified.)*
**AE:** ① Stage 6 grants — **pre-computed, declined on NEVER#6, ~10 min for a fresh session** ②
`PIPELINE_MAP` + the Rule-12 class ③ the egress principal ④ `public-data-router` fork.
**DS:** read-preference removal (**waits on AE's grants + a demonstrably fresh cottonwood artifact**) ·
`aum-metrics` re-declared to all scopes.
**DT:** traces 1 and 2. **DE:** AGG weighting, **designed against C1–C4, not a string fix.**
**CTO:** `declared_types(product, scope)` once traces land · `account-units` consumer trace · the
`|| return 1` sweep (a *different* sweep from the enumeration one).

**Serve state: `5f758b47` / 254,419 B / 13:41:05Z — unchanged all window.**
