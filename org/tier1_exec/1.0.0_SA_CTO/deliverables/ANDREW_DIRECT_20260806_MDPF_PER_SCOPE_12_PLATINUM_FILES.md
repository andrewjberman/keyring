# ANDREW-DIRECT — 2026-08-06 ~2205Z, CTO~Z terminal (site Z)

**Channel:** Andrew-direct, terminal of `1.0.0_SA_CTO~Z`, in answer to the per-scope design call
surfaced in the `/exec-sum` card ~2158Z.
**Recorded by:** `1.0.0_SA_CTO~Z` — same turn, per `org/XXX.md`.
**Broadcast:** `0.0.0_AB_MSTR~Z`, `2.0.0_SA_COO~Z`, `0.4.0_DS_ClientPlatform~Z`,
`0.7.0_AE_CloudOps~Z`, `3.0.0_SA_CVO~Z` — same turn.

---

## VERBATIM

> "Yeah obviously we need the three files for each scope. that means aggregate-aua-timeseries.json,
> aum-metrics.json, and account-distribution.json for Global, for 49 Financial, for Inflection, and for
> Cottonwood. 3 files times 4 scopes means that this pipeline needs to generate 12 platinum files into
> the relevant scope path buckets in opal-data-portal-v2/platinum/mdpf/{scope} every single day, is that
> abundantly clear?"

**THE PHRASING IS THE RULING. Do not paraphrase it into a plan and then cite the plan.**

---

## What it settles

The open design call was: *the unscoped `aggregate_aua/{date}.json` carries multiple partners in one
document, so one writer writes every partner — a partner failure either blocks the file or silently
drops that partner out of it.* **Answered: per-scope files.**

**THE DAILY CONTRACT, stated as he stated it:**

```
opal-data-portal-v2/platinum/mdpf/{scope}/   for scope in {global, 49financial, inflection, cottonwood}
    aggregate-aua-timeseries.json
    aum-metrics.json
    account-distribution.json

3 artifact types x 4 scopes = 12 platinum files, EVERY SINGLE DAY.
```

**Why it is load-bearing and not merely tidy:** per-scope pathing makes channel independence
**physically enforceable** rather than a property the builder must remember to honour. With one file per
scope, one partner's failure **cannot** silently remove another partner from a document — the failure
is confined to that scope's own file, and absence becomes visible as a missing/stale file rather than as
a quietly shorter payload. A single multi-partner document cannot be channel-independent by
construction, whatever the builder intends.

**"every single day"** is part of the ruling, not decoration: it binds the scheduled production path
(CLAUDE.md ad-hoc-runs rule — a production pipeline must have a schedule) and it binds the 12 as a
**daily denominator**, so a run that emits fewer than 12 is incomplete rather than merely quiet.

## Scope, not adjudicated — ONE clarification surfaced, holding nothing

**SURFACE, DO NOT ADJUDICATE (`org/XXX.md`).** His 12 = 3 types x 4 scopes covers the three **uniform**
types. The pack's measured live denominator is **14 (scope, artifact-type) pairs**
(`02_NEEDED_VS_NOT_AUDIT.md` §"Canonical artifact denominator") — the same 12 **plus two
scope-specific extras**:

| Extra pair | Pack's status |
|---|---|
| `cottonwood/account-units` | live served pair |
| `global/non-model-assets` | *"Global current served contract"* |

Two readings, and **the difference is whether two currently-served artifacts continue to exist**:

- **(a)** the 12 are the uniform core he is mandating for every scope; the 2 scope-specific extras
  continue alongside → **14 total emitted.**
- **(b)** exactly 12; the 2 extras are dropped → **two served artifacts are retired.**

**Reading (b) would be a served-output change and is NEVER-rule #3 territory (never-widen sign-off).**
It is therefore not something the fabric may infer. **The question is surfaced to him; nothing is held
on it** — the 12 he named are unambiguous, are the whole uniform contract, and P1-1 designs against
them now. If (a), the two extras simply keep their existing paths and nothing about the 12 changes.

## Immediate effects

1. **P1-1 designs against per-scope pathing.** The multi-partner single document is not the target
   shape; it is the mechanism the ruling removes.
2. **12 is a daily completeness denominator.** A cycle emitting fewer than 12 is incomplete — and per
   the standing governing criterion (acceptance asserts the OUTCOME, never the intervention),
   acceptance asserts *the 12 objects exist for the day*, not that the emitter ran.
3. **Serving-tier location is confirmed as `opal-data-portal-v2/platinum/mdpf/{scope}`**, consistent
   with CLAUDE.md Rule 17b (platinum is the serving tier under `opal-data-portal-v2`).
4. **`json/mdpf/*` is untouched** — the hyphenated `account-distribution.json` legacy served bell stays
   exactly where it is. This ruling is about the platinum scope paths, and does not move a served key.
