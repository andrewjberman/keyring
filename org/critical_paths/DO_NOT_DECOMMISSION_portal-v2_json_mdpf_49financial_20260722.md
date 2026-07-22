# DO NOT DECOMMISSION — `opal-data-portal-v2/json/mdpf/**` IS A LIVE PRODUCER INPUT

**Status:** ACTIVE HOLD — binding until the decouple work item closes.
**Opened:** 2026-07-22 by `2.0.0_SA_COO` (custody), clause authored by `1.0.0_SA_CTO`.
**Class:** retained runtime dependency / decommission blocker.

---

## THE ONE-LINE VERSION

> **`s3://opal-data-portal-v2/json/mdpf/49financial/aggregate-aua-timeseries.json` IS NOT A LEGACY
> LEFTOVER. IT IS A LIVE BUILD-TIME INPUT to the MDPF *revamp* producer. Removing it, freezing it,
> expiring it, or clobbering it SILENTLY BREAKS 49Financial account counts in the revamp.**

If you are here because you are cleaning up portal-v2 after the MDPF cutover: **stop and read the whole
file.** This is the exact action this record exists to prevent.

## WHY THIS IS THE DEFAULT FAILURE PATH, NOT AN EDGE CASE

The MDPF cutover's entire purpose is to replace the legacy portal-v2 MDPF artifacts. So after cutover,
retiring them is **the obviously-correct next cleanup** — it is what a competent engineer does next.
**That is precisely why this needs a blocker and not a footnote.** The dependency runs *backwards* from
what the cutover implies: the replacement still reads the thing it replaced.

## THE MECHANISM (source-confirmed)

`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`
- `:476-500` (wired at `:812`) — imports `account_count` **from the LEGACY SERVED artifact by date-join**.
- `:427` — already computes a correct count, which is then **discarded** in favour of the legacy import.
- `:628` — the same import path for the 49F/global legs.

For **inflection** and **global**, the 2026-07-22 rebuild fixes this (count derived from the same eclipse
snapshot as the values). **For 49FINANCIAL it is NOT fixed and CANNOT currently be fixed** — see below.

## WHY 49F CANNOT SIMPLY BE FIXED (this is real work, not a wiring change)

`0.4.0_DS_ClientPlatform`, schema-grounded 2026-07-22: **there is no per-date 49F account-count source in
existence.**

| candidate | why it does not work |
|---|---|
| `fact_model_aum_daily` | 1,224 days of history but **per-MODEL grain, no account column** |
| `fact_model_allocation_roster` | account grain (`allocation_id`) but **only 8 `date=` partitions** (07-14..07-21) — a point-in-time roster, not a history |
| derive from `opened_ts` | **REJECTED** — ignores closures; the producer's own docstring rules it out |

**The decouple therefore requires building a per-date 49F account-count history that does not exist today.**
DS correctly refused to invent a source. Do not "fix" this by inventing one either.

## THE FAILURE MODE IF IGNORED — SILENT, NOT LOUD

If portal-v2 MDPF is decommissioned / lifecycle-expired / frozen / overwritten:
- the date-join finds nothing (or finds stale rows), and
- **49F account counts break or FREEZE.**

> **A FROZEN COUNT IS INDISTINGUISHABLE FROM A STABLE ROSTER.** (CTO, 2026-07-22)

There is no alarm for "this number stopped moving because its source died." It will read healthy.
Compounding it: **the fingerprint instrument that would detect a 49F count misalignment is VACUOUS on 49F**
— legacy and revamp sit on different bases there (the Andrew-ruled EXCLUDE/B rebase), so it returns
`0 matched / 0 misdated`, which means *the instrument could not discriminate*, **not** that 49F is clean.
**So the detection story for this failure is: nothing detects it.**

## WHAT IS BLOCKED

Any change touching `s3://opal-data-portal-v2/json/mdpf/**`:
- bucket/prefix deletion or emptying
- lifecycle / expiry / transition rules
- versioning or retention changes that could remove current objects
- halting whatever still writes those objects
- any "post-cutover cleanup" sweep that includes this prefix

**-> Route to `1.0.0_SA_CTO` + `2.0.0_SA_COO` for never-widen co-sign BEFORE acting. Not after.**

## STATUS OF THE DECISION — KNOWINGLY ACCEPTED, NOT UNDISCOVERED

This debt is **declared, not cleared**, and is a named TERM of the MDPF re-land never-widen co-sign:

> *inflection + global count axes SOURCE-VERIFIED post-rebuild; 49F count axis REMAINS on the legacy served
> import, structurally exposed, and UNMEASURABLE with current instruments (fingerprint vacuous under the
> EXCLUDE/B basis split) — **declared, not cleared.** Further: the 49F count axis constitutes a RETAINED
> RUNTIME DEPENDENCY of the revamp producer on the legacy served artifact it replaces — a post-cutover
> DECOUPLE debt, knowingly accepted, not an undiscovered residual.*

**"A debt we choose knowingly is fine; a debt someone discovers in six weeks is an incident."** — CTO.
**This file exists because knowingly-chosen is a property of the RECORD'S REACHABILITY, not of anyone's
intent at signing time.** The co-sign deliverable that carries the clause is not read by the person doing a
decommission; a path-keyed file in the critical-paths ledger is.

## THIS DOCUMENT IS THE WEAKEST OF THREE CONTROLS — SAY SO PLAINLY

**This file is PROSE THAT MUST BE READ, and it only fires for someone already suspicious enough to search
the path.** *"They will grep the prefix first"* is an assumption about a person, and assumptions about
people are the class we keep being wrong about. Our own law: **gates teach at violation time; prose taxes
every session forever.** The control ladder, in descending strength (CTO ruling, 2026-07-22):

| # | control | fires against | status |
|---|---|---|---|
| 1 | **S3 bucket-policy DENY** on `DeleteObject` / lifecycle-expiry for the prefix | **ANY actor at the moment of the act — console included, no repo, no reading** | **ROUTING — `1.0.0_SA_CTO` owns; build on `0.7.0_AE_CloudOps`** |
| 2 | commit-time gate on TF touching `opal-data-portal-v2` lifecycle/expiry/removal | the repo path; **misses the console** | proposed |
| 3 | **this document + `critical-surfaces.yaml` row** | someone who already thinks to look | **LANDED (this file)** / yaml row proposed |

Precedent for (1): the `.parquet`-under-`bronze/` bucket-policy deny (Rule 17a) — behavior-grade, exercised,
and the proven shape for exactly this problem.

**STANDING-ORDER COLLISION, FLAGGED NOT ADJUDICATED:** Andrew's 2026-07-17 direct order **suspends new alert
systems during consolidation**. **A bucket-policy DENY is a PREVENTIVE control, not an alert — it pages
nobody** — so CTO reads it as outside that suspension, and I concur. **But it is adjacent enough that it is
being put to Andrew explicitly rather than assumed**, because *"adjacent, so I assumed it was covered"* is
how a standing order gets quietly widened or quietly ignored. If Andrew holds it, controls (2) and (3)
carry alone — and this file's weakness above becomes the whole exposure.

## OPEN ITEMS

- [x] **OWNER NAMED (COO routing call, 2026-07-22):** decouple work item -> **`0.4.0_DS_ClientPlatform`**
      (owns the producer, proved the source gap). Bucket-policy deny + TF gate -> **`0.7.0_AE_CloudOps`**,
      routed by `1.0.0_SA_CTO`. **Sequenced BEHIND the current count-axis rebuild — named and queued, not
      started.** *Debt with no owner is debt nobody retires.*
- [ ] **BUILD a per-date 49F account-count history** — the actual blocker. **CLASS THIS CORRECTLY: this is a
      scoped DATA WORKSTREAM with a real dependency, NOT a cleanup task or a wiring change.** No source
      exists (see table above). **Whoever picks this up and sizes it as an afternoon will abandon it.**
- [ ] Bucket-policy DENY landed + **exercised** (behavior-grade: a denied delete that names the policy, plus
      an isolated positive control proving the test can fail).
- [ ] **Register in `org/modules/graph/critical-surfaces.yaml`** so a tooling gate — not only this document —
      fires on the prefix. **Proposed by COO; registry change is CTO's to land.**
- [ ] Close this hold only when 49F count derives from the same source snapshot as its values, verified by
      the CROSS-AXIS COHERENCE assertion (count == same-day source-derived roster where a partition exists;
      honest-None where it does not), **mutant-proven to go RED before it ships.**

## PROVENANCE

- Defect found: `0.4.0_DS_ClientPlatform` 2026-07-22 ~1228Z (count axis inherits legacy's date mis-stamp;
  frozen-9 inflection rendered 474 -> 540 -> 474 across Jul 6/7).
- Independently reproduced with a separately-run positive control: `1.0.0_SA_CTO` ~1233Z.
- Both exec never-widen limbs WITHDRAWN on it (re-land 0 of 3); COO limb withdrawn on **falsified premise**,
  not ETag movement — the co-signed evidence ran the VALUE axis and never covered COUNT.
- Decouple clause authored by CTO; this record opened by COO. Doctrine: LD-0330 §8.
