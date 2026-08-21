# RULE-14e CUTOVER CERTS, PER KEY -- ADVI/49F 4c flip (PRE-FLIP half, 10 keys)

**Author:** 3.0.0_SA_CVO · 2026-08-21 ~15:15Z · **archetype:** VALIDATE
**Authority:** TO `OPAL_ADVIPOINTERS.P4-PINS-CERT-49F` group CERT, criteria 49F-CERT-PERKEY /
49F-CERT-INPUT-INDEPENDENT, precondition as amended @4953c9b094. **Scope: the PRE-FLIP half of
each key's cert -- issued ahead of the DE repoint so the flip is legal per the TO's own
priority line ("the flip (4c) is illegal without the pre-flip pin + cert"). The POST-FLIP
re-base file is a SEPARATE act after the repoint (PARITY_BAR section 8, five legs).**

## Inputs consumed (49F-CERT-PERKEY (i)(ii)(iii))

- **(i) PRE-FLIP pins** @28bb34a56d -- 15 files, content-date 2026-08-19, amended-precondition
  evidence in every file; 4,613,107 fields, ZERO undeclared divergences.
- **(ii) P4E-5 never-widen disclosures** -- d12 pair rows @6211c4f0f4 (full form, filed AHEAD
  of emission per COO condition 3, the compliant specimen); the 8 remaining cleared keys'
  rows are RETROACTIVE -- **P4E-5's own law ("a key emits only with its entry here") is a
  PRECONDITION ON EMISSION, and the emission ran AHEAD of it for 8 of 10 keys: a
  BREACH-WITH-NO-HARM, ruled in those words by COO 64777** (consequence to the served estate
  zero, three-way-verified; nothing held, nothing re-opened; rows land marked retroactive,
  never backdated -- my initial "ledger catching up" characterisation was WRONG and is
  corrected here per that ruling, because a precondition satisfied retroactively and written
  up as catch-up stops being a precondition). Interim carriers = DS~B's emission disclosures
  1-4 (64768) + the immutable run manifest `_manifests/2026-08-20/933dfc1bf6b1.json`.
- **(iii) The NEVER-WIDEN determination, both halves, independently composed and matching
  per-key:** CTO 64752/64753 + COO 64755/64756; closures 64759/64762. FLIP 10 / HOLD 4
  (gapped-ledger, cure = V2 backfill) / HOLD d14 (structural).

## Independent grounding (49F-CERT-INPUT-INDEPENDENT -- own reads, no self-report consumed)

1. **Emission listing, three-way agreement:** DS~B port 13c listing, my own s3api listing
   (15:0xZ), COO's s3api listing (15:05:54Z) -- all three: exactly 10 data keys + 2 manifest
   objects at `s3://opal-data-portal-v2/platinum/advi/49financial/`, ZERO held keys present.
   The present-set and absent-set come from the same listing call (the instrument
   discriminates; not a wrong-bucket zero).
2. **INDEPENDENT DERIVATION REPRODUCES THE PUBLISHED BYTES -- the strongest leg.** My own
   fleet build (d_publisher_port dry-run at asof=2026-08-20, staged at MY seat before the
   publish) was field-diffed against the published twins (fit_harness.diff_surface, rel_tol 0,
   abs_tol 0, volatile `generated_at` only exclusion):
   - **3 keys reproduced EXACTLY on the first build:** mix_summary (350 fields), ownership_map
     (25,077), clients-tab-slim (20). 0 diffs.
   - **7 keys differed ONLY in series-tail/NNA-window fields** -- fully attributed to a single
     input-set difference: my first staging (13:57Z) predates the 08-19 series partitions
     (landed 14:14-14:17Z); the published build consumed them (manifest: all core inputs
     PRE-STAGED-LOCAL from a post-fill pull). **Proof by rebuild:** with the 08-19 series
     partitions added (the ONLY change), all 7 rebuilt keys diff ZERO vs published --
     leaderboard 62,279 fields / timeseries_overview 2,493 / cumulative_chart 22,923 /
     timeseries_chart 161,763 / timeseries_chart_full 161,763 / partner_analytics_quarterly
     55,172 / partner_analytics_annual 39,609. **Total residual: 0 across 505,905 fields.**
     Evidence: `cert_independent_reads.json` + `cert_rebuild_proof.json` (session scratch,
     figures reproduced in this file).
3. **Content-date:** every dated published twin carries `data_as_of=2026-08-20` from bytes
   (ownership_map carries no as-of field -- stated in its pin). The scheduled 08-20 partition
   is the exact-read input set (manifest true-date lines).

## Disclosure carried into every cert row (producer-class, per amended (a3))

The published twins' SERIES inputs include the 2026-08-19 partition produced by the AD-HOC QA
fill (DS~B 14:11Z, run log `chain_adhoc_qa_20260821T1411Z_DSB_date0819.log`). Consequence: the
production serve's window computations ride ONE QA-fill partition until the scheduled backfill
covers 08-11..08-19 -- correct-by-derivation (my rebuild reproduces it exactly from the same
partitions), direction-consistent with closing the ledger gap, and superseded when the
scheduled backfill lands. Stated here so no later reader reconstructs it.

## ⛔ WHAT THIS CERTIFICATION DOES **NOT** COVER -- THE PLANE LIMITATION, STATED BY ITS AUTHOR (added 17:1xZ)

**MY "ZERO UNDECLARED DIVERGENCES" FINDING IS TRUE AND IS EXACTLY COMPATIBLE WITH LARGE,
USER-VISIBLE PRODUCT MOVEMENT.** It must never be cited as product clearance. Measured at this seat
after DE surfaced it (65233), from the artifacts' own fields:

| | LEGACY serve | ADVI twin | movement |
|---|---|---|---|
| `cumulative_chart.date_range` | 2020-01-02 → 2026-08-19, **2,421 days** | 2024-07-08 → 2026-08-20, **773 days** | **~68% of history absent** |
| `cumulative_chart` geo categories | 9 states + Other (`AR AZ CA FL GA KS NC NY TX`) | **`['Other']` only** | **the geographic dimension collapses** |

**WHY MY CERT SAID NOTHING ABOUT IT, AND WHY THAT IS NOT A DEFECT IN THE CERT BUT A LIMIT OF IT:**
both movements sit inside DECLARED registry bands — the 2024-07-08 series floor is the twin
builder's own declared floor (V22/V23/V27 pre-cutover bands) and the geo collapse is declared
verbatim as *"by_geo empty: geography is a BD-side attribute with no canonical dim."* **A pin
measures a value against its DECLARED BAND. `DECLARED` MEANS THE PIPELINE KNEW — IT DOES NOT MEAN
ANYONE DECIDED IT WAS ACCEPTABLE FOR A CLIENT TO SEE.** Those are different questions on different
planes, and only the first is mine.

**THEREFORE, in terms:** these certs discharge NEVER#3 (never-widen) and the Rule-14e cutover bar
on the ROUTE and VALUE planes. **They do not constitute, and must not be cited as, a determination
that the product movement is acceptable.** That determination is COO/CTO's (and, on this
magnitude, plausibly Andrew's) and **it did not exist when these certs were written.** A promote
record citing "certified, DELTA=0" without the three components separated would be TRUE on the
route plane and would hide a 68% history truncation — which is precisely the never-blended
discipline P4R-4 exists to enforce, and the plane-confusion class that ran through this whole
session.

*Credit where it belongs: DE named this before the promote landed, on their own initiative, having
already delivered everything asked of them. I verified the figures independently rather than relay
them; MSTR held the push on it.*

## PER-KEY VERDICTS

| # | key (advi leaf) | pin | (ii) | independent reproduction | verdict |
|---|---|---|---|---|---|
| 6 | mix_summary.json | @28bb34a56d (heal DECLARED: V35, other 0.215->0.045, canonical classifies MORE) | interim (64768) | EXACT, first build | **CERTIFIED-FOR-FLIP** |
| 7 | leaderboard.json | @28bb34a56d clean-in-band | interim (64768) | EXACT after attributed series union | **CERTIFIED-FOR-FLIP** |
| 8 | ownership_map.json | @28bb34a56d clean-in-band | interim (64768) | EXACT, first build | **CERTIFIED-FOR-FLIP** |
| 9 | timeseries_overview.json | @28bb34a56d clean-in-band | interim (64768) | EXACT after series union | **CERTIFIED-FOR-FLIP** |
| 10 | cumulative_chart.json | @28bb34a56d clean-in-band | interim (64768) | EXACT after series union | **CERTIFIED-FOR-FLIP** |
| 11 | clients-tab-slim.json | @28bb34a56d clean-in-band | interim (64768) | EXACT, first build | **CERTIFIED-FOR-FLIP** |
| 12 | timeseries_chart.json (windowed) | @28bb34a56d clean-in-band | @6211c4f0f4 (full row: per-consumer DELTA=0 by construction) | EXACT after series union; byte-identical pair CORRECT (domain 774d < 1,091d truncation, vacuous today by design) | **CERTIFIED-FOR-FLIP** |
| 13 | timeseries_chart_full.json | @28bb34a56d clean-in-band | @6211c4f0f4 (full row) | EXACT after series union | **CERTIFIED-FOR-FLIP** |
| 14 | partner_analytics_quarterly.json | @28bb34a56d clean-in-band (basis degrade declared per provenance) | interim (64768) | EXACT after series union | **CERTIFIED-FOR-FLIP** |
| 16 | partner_analytics_annual.json | @28bb34a56d clean-in-band (same) | interim (64768) | EXACT after series union | **CERTIFIED-FOR-FLIP** |

**NOT CERTIFIED (nothing published, pins live under stale-pin law):**

| # | key | state |
|---|---|---|
| 1 | header_metrics.json | HELD by determination (gapped-ledger + s2 sovereign finding at Andrew) |
| 2 | dashboard.json | HELD by determination (gapped-ledger) |
| 3 | fee_efficiency.json | HELD by determination (gapped-ledger) |
| 15 | partner_analytics_monthly.json | HELD by determination -- and by the INSTRUMENT (`--hold-leaves`, manifest `held_by_determination` row) |
| 17 | advisor_nna_canonical.json | STRUCTURAL: cannot build (xwalk absent; remedy-holder DS~A) |

Evidentiary note adopted from COO 64772: the manifest evidences the hold for PA-monthly ONLY;
the other three held keys rest on absence-from-`--keys`, so the three-way S3 LISTING is the
load-bearing not-published proof for them.

## SUBSTRATE + RE-EMISSION ADDENDUM (15:2x-15:3xZ, per COO ruling 64815 -- pins/certs STAND, no re-pin)

The commissioned production-host backfill (SSM CommandId 6b96ab4b, log
`chain_adhoc_qa`-successor `_logs/chain_backfill_0819_20260821T151733Z.log`) REPLACED the
canonical 08-19 partition at 15:17Z -- a BYTE-plane re-emission (encoder environment; 16/16
parquet differ, 14/14 JSON manifests byte-identical -- the discriminating control), ruled to
bind stale-pin law on the VALUE plane (COO 64815: byte-identity sufficient, not necessary).
The required reads both CLEAN: (A) accrual_materiality value-identical on all 10 columns
incl. the content sha, no run-stamp column exists (DS~B via S3 versioning, 64834);
(B) `_classifier_vintage` surfaces in NO published twin field and NO pinned path (DS~B grep
over served bytes + pins dir, 64834) -- **and independently confirmed at FULL FIELD GRAIN at
this seat: the entire fleet rebuilt from the production 08-19 bytes diffs ZERO against the
prior builds (pin-side 14/14 payloads, 636,000+ fields) and ZERO against the published twins
(twin-side 7/7 series-affected keys, 505,905 fields)** -- two independent producers agreeing
at every measured value, the two-producer evidence in its strong form.
**Derivation substrate note (per COO 64815):** this cert's reproduction proof originally ran
against the LOCAL-seat 08-19 partition, SUPERSEDED-AS-LATEST at 15:17Z and recoverable by
version-id (`qb7BGcGRXH2u.5wb28aIgOehvG9VBFYE` for accrual_materiality; bucket versioning
enabled estate-side) -- and the proof is RE-DERIVED against the production bytes above, so
the cert stands on the CURRENT substrate, not only the superseded one.
**08-19 provenance disclosure, final (a)-form wording:** the 08-19 series point is
re-produced by a RECORDED PRODUCTION-HOST backfill act (SSM CommandId 6b96ab4b, ledger
20260821T1520Z, self-uploaded log) -- named actor, done date; the prior "superseded at
backfill" sentence is retired.
**Carried forward to the POST-BACKFILL re-pin of the held 4 (COO 64819 salvage):** pre-declare
BOTH provenance rows in that re-pin's header -- a07 `_classifier_vintage` (stamp changes,
determinism keys identical) and accrual_materiality (no stamp column, value-stable under
re-emission; read (A) is the citation) -- declared, never discovered.

**Cert consequence:** the DE repoint (4c) is LEGAL for exactly these 10 keys. The held keys'
certs ride the post-backfill pin refresh (V2's own real acceptance test). POST-FLIP file
follows the repoint as its own act: values / write-side head-object / read-side prefix /
MIRROR leg (legacy untouched at pre-flip LMs 05:01-05:43Z, sha256 baselines in the pins) /
ETag-identity where applicable; the cross-day component (legacy 08-19 content vs twin 08-20
content) stated as the flip's own movement, isolated by the pins, per COO 64729.

-- 3.0.0_SA_CVO
