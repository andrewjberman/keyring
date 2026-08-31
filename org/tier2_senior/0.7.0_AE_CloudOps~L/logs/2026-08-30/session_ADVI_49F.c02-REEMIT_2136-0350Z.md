# 535 partitions re-emitted under one convention, and the finding that mattered came from refusing to round 77,072 of 77,087 into a pass — 0.7.0_AE_CloudOps~L

**archetype:** MIXED
**secondary_archetypes:** BUILD, DIAGNOSE, VALIDATE

**Date:** 2026-08-30
**Task Order:** ADVI_49F.c02-REEMIT (cell C02-g-3)
**Status:** COMPLETE — round GRADED AND ACCEPTED by `3.0.0_SA_CVO` 85166

---

## Objective

Re-emit `canonical/twr_daily` for every stored partition under ONE gross-leg convention, on a
build-only campaign, against the engine at the `C02-g-2` vintage. Seated with R-1/R-2
(measure + plan) live and emission gated on `0.4.0_DS_ClientPlatform~N`'s commit; that gate
opened mid-session and the campaign ran to completion.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 EXERCISE half — proved a forwarder RAN, not merely resolved. `PATH: 105 of 105`. |
| audit-archive-invoker | `python .tools/audit-archive-invoker.py` | WARN | rc=1, exactly the 2 KNOWN OWNED-UNTIL-`rv0057-f001` findings. No third finding. Not re-filed, per XXX.md's own instruction. |
| commit-gate.sh | on each of 4 `.py` deliverables | PASS | Clean on all. The acceptance instrument failed ruff twice (unused `pandas` after the boto3 rewrite; 3 placeholder-less f-strings) and was **re-gated AND re-exercised** each time — a fix is not verified by the fix. |
| deploy_ledger.py | `open` (6 legs, 8h) → 6× `close-leg` → `close`; `check --red` | PASS | Opened THROUGH THE TOOL so it carried a sentinel and was indexed. Closed with all 6 legs proven; `check --red` returns 0 rows for the slug. |
| proof-of-spec-check | positional form, `R-1,...,R-7` | PASS (2nd run) | First run **INVALID, 11 violations**. Recorded inside the instance rather than quietly fixed. |
| lib/trading_calendar | `is_trading_day` swept over the domain span | PASS | Found the 5-day chain outage nobody had named, and reconciled the domain: 539 − 5 + 1 = 535. |
| boto3 (in place of the CLI shim) | s3 / ssm / scheduler clients | PASS | `.tools/aws` is a bash script; Windows python cannot exec it (WinError 193). |

**What worked:** the *paginated* census. `list_objects_v2` returned 535 partitions from 1,070
objects **over 2 pages** — a bare call stops at 1,000 keys and would have reported roughly half
the domain with no error at all. Every denominator in the round rests on that one habit.

**What failed:** three instrument faults, all mine, all fixed and recorded — a `pipefail`
bashism on a dash host; a 403 because I deployed the vehicle to a *tidier* prefix the instance
role cannot read; and a `comm(1)` that returned zero-overlap on a CRLF artifact. The last one
would have read as "535 brand-new dates".

**Gap found:** `deploy_ledger.py` still has no close path for hand-authored records. I met that
class three times in one session (COO's catch on the floor-hold entry, my own 08-29 prediction
of it, and the two-fabric P14 record I reconciled at `7ab7866018`).

---

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | `/watcher` — register + arm | task `btw2s65pf`; **0 of 36** inbox-watch processes named `~L`, so a clean arm with no orphan |
| 2 | R-1 at source; R-2 on the live plane | (i) absent at HEAD; (ii) viable but needs a 5-object mirror — the named BUILD act |
| 3 | Vehicle built, gated, deployed local→S3→host | `c73c047862`; `_code/`, LF, md5 == ETag |
| 4 | Date-1 dry-run on the box | 2.33 s; rows 7370/cols 15 — matching DS~N's independent QA exactly |
| 5 | Driver + ledger opened; date-1 emission | `e1141a5905`; R-3 0.000000e+00, R-5 4,076/4,076 |
| 6 | Campaign, 22 batches | **535 of 535** ARTIFACT-COMPLETE, 0 halts, 22.3 min |
| 7 | Acceptance pass over all 535 | R-3/R-5/R-6/R-7 PASS; **R-4 reported NOT MET AS WRITTEN** |
| 8 | Amended R-4 relation census | 77,087 of 77,087, violations 0 |
| 9 | Proof-of-spec VALID; ledger closed | `9f59f39892`, `f097afcf90` |

## Verification

```
CAMPAIGN     535 of 535 ARTIFACT-COMPLETE | 0 ARTIFACT-INCOMPLETE | 0 NO-RUNNER-SUMMARY | exit 0
             per-date n=535 min 1.75 median 2.44 mean 2.50 max 3.53 total 22.3 min (from the LEDGER)
R-3  PASS    max |delta r_net| 0.000000e+00 over 2,593,321 matched OK account-days; 0 violations
R-4  GRADED  relation (r_gross-r_net)*BMV == cf_net-cf_gross : 77,087 of 77,087, violations 0
             inequality on BMV>0 : 77,072 of 77,072 | BMV<=0 : 15 NOT-EVALUABLE-BY-DOMAIN
             negative control non-fee gap EXACTLY 0 on 2,516,234 of 2,516,234
R-5  PASS    vintage on 3,021,660 of 3,021,660 ROWS; schema 1.1 on 535 of 535; ZERO at "1.0"
R-6  PASS    0 new versions across 4 out-of-domain tables (7,588 versions scanned)
PUSH  c73c047862 e1141a5905 f862baac5a 0b6a4b71a2 7ab7866018  ON ORIGIN @5a0e1df70b
      b115d9ad7f 9f59f39892 f097afcf90                        LOCAL (ls-remote 03:48:34Z)
      control: origin NOT an ancestor of c73c047862 -- the test discriminates
```

---

## Work Completed

### 1. R-1/R-2 measured at source, and the domain was wrong by one

The cell said 534. An s3api census said **535** — the extra being `2026-08-28`, the pre-fix
Saturday emission. Ratified by COO 84341 and CVO 84356, who retracted their own typed "534 of
534" as a number that had already gone stale.

`(i)` does not exist at HEAD; `(ii)` needs a 5-object mirror that nothing populates for a
c02-only run. That was the BUILD act, named to the issuer before building and cut by the issuer.
Crucially `(ii)` is **R-6-safe structurally** — the engine's only write is
`rc.emit(TABLE_DAILY)` — so R-6 became a confirmation rather than a hope.

### 2. Two findings surfaced BEFORE the first write

A **5-trading-day chain-wide outage** (2026-08-11..08-17), zero objects across all four tables,
which nobody had named. And its consequence: the "free discriminator" three seats were relying
on for `2026-08-18` **cannot fire**, because that date's D-1 sits inside the outage. Both
branches predict NOT-POPULATED, so the observation cannot separate them. Surfaced at 84527
before any emission; the outcome later confirmed the prediction exactly.

### 3. The campaign, and three pre-registered special dates

All three came back **AS PREDICTED**, predictions written into the ledger before driving:
`2024-07-08` REFUSED-NO-BMV 4,074/4,074 (census *identical* to stored), `2025-01-09`
NO-PRIOR-TRADING-DAY 4,808/4,808 (no return manufactured for a closed market), `2026-08-18`
REFUSED-NO-BMV 7,315/7,315.

### 4. R-4, and the thing this session is actually for

The acceptance pass returned 77,072 of 77,087. **I reported it NOT MET AS WRITTEN.** All 15
exceptions carry a NEGATIVE BMV; across 535 partitions 1,089 of 2,593,321 OK account-days have
`bmv < 0`, and exactly 15 of those carry a fee — an exact match, so `bmv < 0` is necessary and
sufficient. Old-vs-new on 5 of them showed every one flipping POSITIVE → NEGATIVE, i.e. the fix
was uniform; what breaks is the *meaning* of a comparison on a negative denominator.

CVO — who authored the bar — found it carried an **uncovered member** (Rule 24 (i)) and amended
it. `0.4.0_DS_ClientPlatform~N` then traced the population to `c02_twr_engine.py:224`, where the
near-zero guard tests `abs(bmv)` — MAGNITUDE where its own comment says VALUE — so a negative
BMV passes and the row serves status OK with a **sign-inverted `r_net`**. Pre-existing, now its
own cell.

### 5. Four corrections against myself

The CRLF zero-overlap; the `2024-07-08` prediction where I predicted what a code *comment*
promises rather than what the code does; mis-attributing one command's output to another while
hunting an orphaned message; and my own printed NOTE that `2026-08-17` would supply BMV,
falsified in the same breath by the census I had just run.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Report R-4 NOT MET AS WRITTEN rather than 99.98% | A near-pass reported as a pass is the failure mode. It is what exposed the 1,089-row served defect. |
| Acceptance instrument SEPARATE from the driver | A wrapper that both performs an act and certifies it is a shape this fabric has been bitten by. |
| Prior version resolved BY TIME, not position | "Second newest" would silently compare against another campaign write if a date were ever re-driven. |
| Pre-register the three special dates before driving | So the grade reads a prediction, not a post-hoc explanation. |
| Deploy the vehicle to `_code/` after the 403 | The tidier `_campaign/` prefix was the broken one — the instance role cannot read it. |
| Do NOT delete the `_campaign/` stray | An S3 delete is a confirm-first act; a harmless orphan is better than an unauthorised deletion. |
| Do NOT create the 5 missing outage partitions | Out of domain; producing them needs a00..c01, the prohibited (iii). |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `deliverables/c02_reemit_mirror_pull.py` | the c02-only vehicle | `c73c047862` |
| `deliverables/ADVI_49F.c02-REEMIT_CAMPAIGN_DRIVER.py` | driver | `e1141a5905`, `0b6a4b71a2` |
| `deliverables/ADVI_49F.c02-REEMIT_ACCEPTANCE.py` | acceptance instrument | `f862baac5a` |
| `deliverables/ADVI_49F.c02-REEMIT_R4_RELATION_CENSUS.py` | amended-R-4 census | `9f59f39892` |
| `deliverables/…_CAMPAIGN_LEDGER.jsonl` + `…_ACCEPTANCE_RESULT.json` | oracle + result | `b115d9ad7f` |
| `deliverables/ADVI_49F.c02-REEMIT.proof_of_spec.json` | instance, VALID | `9f59f39892` |
| `change_management/20260830T0251Z_…` | ledger open→closed | `f097afcf90` |
| `change_management/20260827T2018Z_…` | P14 cross-fabric reconcile | `7ab7866018` |

## Blockers

**NONE at this seat.** Nothing held, nothing stranded. Not mine, listed so they are not read as dropped:

- The floor-hold **lift** (H-4) — condition MET and read; the act is `0.7.0_AE_CloudOps` base's.
- The **negative-BMV served defect** (1,089 account-days) — a new ADVI_49F cell at `0.4.0_DS_ClientPlatform~N`.
- The **label item** (NO-PRIOR-TRADING-DAY vs REFUSED-NO-BMV) — held by that seat; blast radius measured at **1 of 539, one BY CONSTRUCTION**.
- The **5-day outage** — surfaced, owner routed by MSTR 81931.

## Current State

`canonical/twr_daily` reads ONE gross-leg convention across all 535 stored partitions, each
carrying `gross_leg_vintage = 946b5c5a3c…` and `schema_version "1.1"`, with zero left at "1.0".
Nothing served, no publisher, no platinum key. The round is GRADED AND ACCEPTED. Three commits
are LOCAL and ride the next integration window.

## Next Steps

1. **[`0.7.0_AE_CloudOps` base]** Lift `advi-49f-gold-floor` on the issuer's word — TF State ENABLED, targeted safe-apply, `scheduler get-schedule` read back live.
2. **[`0.4.0_DS_ClientPlatform~N`]** The negative-BMV cell; first act is the census, before any status value is proposed.
3. **[any seat]** `_code/c02_reemit_mirror_pull.py` removal, on the issuer's word now that the round is graded; and the `_campaign/c02-reemit/` stray, which needs a confirmed delete.
4. **[carried, not mine]** A bulk re-emission is a **read hazard for every concurrent consumer** of its prefix — `0.4.0_DS_ClientPlatform~C` hit an `s3fs FileExpired` mid-campaign and correctly held BP1-2. The next campaign of this shape should name its readers before the first write.
