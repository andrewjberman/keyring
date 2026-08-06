# BRIEF (POCKETED) — retire the `mdpf_revamp` name from the gold tree

**Status:** ⛔ **SEQUESTERED — NOT AUTHORIZED, NOT SCHEDULED, NOT IN THE CURRENT BUILD.**
**Author:** `1.0.0_SA_CTO~Z` · 2026-08-06
**Trigger to un-pocket:** the `MDPF_CANONICAL_PLATINUM` PRD/rubric work is **complete** (R1–R14 pass on
one unattended scheduled cycle) **AND** Andrew re-opens it.

> **Andrew-direct 2026-08-06, VERBATIM:** *"I would recommend that gold does appends to
> opal-data-assets/portal/gold/mdpf/{scope} mirroring the path of the
> opal-data-portal-v2/platinum/mdpf/{scope}. I do not like the mdpf_revamp naming."*
>
> **And on this brief, VERBATIM:** *"Your framework is better, yes. Let's sequester this for now, you can
> draft a brief and keep it pocketed for later after the agents are done with the work laid out in the
> PRD/rubric."*

---

## 1. What is ALREADY handled by the current build — do not re-scope it

The naming directive splits cleanly, and **the easy half is already in flight:**

**IN THE BUILD (contract A3/A4, pre-dates this exchange and stands on its own):** the gold consolidator
writes `opal-data-assets/portal/gold/mdpf/{scope}/{artifact-type}/{data-as-of}.json` **directly**. The
mirror is exact through `{scope}/`; gold's trailing `/{date}.json` **is** the append.

```
opal-data-assets/portal/gold/mdpf/{scope}/{artifact}/{date}.json    gold      — APPENDS
opal-data-portal-v2/platinum/mdpf/{scope}/{artifact}.json           platinum  — CURRENT
```

**Measured 2026-08-06:** that canonical tree **already exists and is already populated** — four scopes,
hyphenated types, dated files. Today it is written by the 09:40 accrual bridge copying out of
`mdpf_revamp`. When A4 lands, the spine writes it directly and **the bridge stops having a reason to
exist** (rubric R11).

**⇒ CONSEQUENCE, and this is why most of the rename needs no work:** once A4 lands, the scoped
`gold/mdpf_revamp/{firm}/*` objects **stop being written** and become inert residue. Nothing has to
*rename* them. **This brief is only about what is left after that.**

---

## 2. What is POCKETED — and why it is the hard half

### 2a · `_aggregate_aua` — the live emitter contract

`gold/mdpf_revamp/_aggregate_aua/{date}.json` is **not residue.** It is the producer contract
`opal-assets-daily-emitter` reads.

| fact | measured |
|---|---|
| partitions live | **440** |
| producer | `mdpf_aggregate_aua.py:80` (`PLATINUM_PREFIX`) |
| consumer wiring | `infra/aws/terraform/opal-assets/emitter.tf:213` |
| also referenced | `infra/aws/terraform/mdpf-pipeline/lambdas.tf:88`, `build_mdpf_etf_ownership_timeseries.py:76` (OWNTS — separately retiring) |

**⚠ THREE REASONS THIS IS NOT A RENAME:**
1. **It has no scope.** Multi-partner **by computation** — the `aggregate` block and `reconciliation`
   only exist because all partners are in one payload. It **cannot** live under `{scope}/`.
2. **W-1a moved this exact contract TODAY**, and its consumer-side legs are still open. Moving it again
   the same day is a second atomic re-point on a contract whose first one has not closed.
3. **Its rollback target was archived tonight** (444-object archive, 21:42Z; W-1a addendum 2155Z). The
   cheap-rollback assumption that made the first move safe **is not currently true.**

### 2b · The residue left inert by A4

`gold/mdpf_revamp/{49financial,inflection,cottonwood,global}/{account_distribution,aggregate_aua_timeseries,aum_metrics}.json`
· `cottonwood/account_units.json` · `cottonwood/aggregate_aua_timeseries_interpolated.json`
· `global/non_model_assets.json` · `global/non_model_assets_precutover_frozen.json`
· `_audit/legacy_*.json` · `meta/cycle-complete.json`

**⛔ Inert is not deletable.** Deleting served-adjacent objects is on CLAUDE.md's human-confirmation list
and is Andrew's. `meta/cycle-complete.json` in particular is a **completion marker** — establish nothing
gates on it before touching it.

---

## 3. The recommendation (Andrew: *"your framework is better"*)

**Target:** `opal-data-assets/portal/gold/mdpf/_aggregate_aua/{date}.json`

Same canonical tree · **underscore-prefixed**, matching the `_audit/` and `_manifests/` reserved prefixes
already present · **excluded from scope discovery**, so it is visibly not-a-scope · and it honors "no
`mdpf_revamp`" without inventing a second tree.

**Sequencing — the whole point of pocketing it:**
1. The PRD/rubric build completes; **R1–R14 pass on one unattended scheduled cycle.**
2. W-1a's consumer-side legs **close**, and a **current** rollback target exists (the archived one is
   not it).
3. **Then** the `_aggregate_aua` move runs as **its own atomic step** — producer + emitter re-pointed
   together, equivalence-proved, same-window rollback — **not riding along with twelve other changes.**
4. Residue disposition is a **separate, human-confirmed** act after that.

---

## 4. Preconditions before this brief is picked up

- [ ] `MDPF_CANONICAL_PLATINUM` rubric R1–R14 PASS on one unattended scheduled cycle
- [ ] Gold writing A4 canonical keys directly; **bridge invocations = 0**
- [ ] W-1a's `_aggregate_aua` re-point legs CLOSED, with a live rollback target
- [ ] Andrew re-opens this brief
- [ ] Emitter re-point planned as **one atomic change**, equivalence-proved, same-window rollback

---

## 5. ⛔ Why this document exists rather than the work

A naming cleanup is cheap-feeling, adjacent to work already in flight, and would read in review as
tidying. **It is a live producer contract with an open re-point and no current rollback target.**
Andrew sequestered it deliberately. **Do not scope any part of §2 into the current build.**

If a fresh seat sees `gold/mdpf_revamp/_aggregate_aua/` referenced in the deliverable contract's **A7**
and reads it as stale: **it is not.** A7 says *preserve that contract*, and that instruction is correct
and current. This brief is why.
