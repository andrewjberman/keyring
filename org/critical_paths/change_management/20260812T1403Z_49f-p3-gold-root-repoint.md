# Deploy-completion ledger: 49F P3 gold-root re-point (copy + re-point + verified emission)

**Status:** CLOSED
**Opened:** 2026-08-12T14:03Z (deploy-start) | **Closed:** 2026-08-12T14:20Z
**Operator:** 0.4.0_DS_ClientPlatform

**Authority chain:** Andrew-direct 2026-08-12 "all recs approved" (P3 authorized; relayed COO
132630Z, record `ANDREW_DIRECT_20260812_OPEN_CALLS_FOUR_RULINGS.md`) -> COO 135005Z ruling (a)
re-point-not-retire -> COO 140114Z approving method (a) COPY + one fresh verified emission.
**Precondition DISCHARGED:** AE IAM leg @b6e5cf9c2f, independently re-verified by this seat at the
exact emit key shape (Put/Get/List-with-context ALLOWED; List-without-context implicitDeny
reproduced deliberately as a control on the known false-deny mode).

## Scope (three acts, one ledger)

1. **COPY** the existing 526-partition series from `schwab/08335338/gold/` to
   `portal/gold/advi/49financial/` — 4,206 objects / 325.1 MB across 4 canonical tables.
   *Nothing removed at the source.*
2. **RE-POINT** the write knobs — the 1+10 surface at `P3_REPOINT_PREPARED_EDIT_SURFACE_20260812.md`
   @288653999f (K1 `OUT_ROOT`; new `GOLD_ROOT` + 10 gold re-derivations across 6 K2 files;
   ⛔ `SCOPE` UNTOUCHED — it derives 10 silver/meta READ paths).
3. **ONE FRESH VERIFIED EMISSION** at the new root, verified on the re-read, never the write rc.

## ROLLBACK (stated BEFORE the first write)

Delete the NEW prefix `portal/gold/advi/49financial/` and revert the re-point commit. The source
root is untouched throughout, so the act is reversible at every point. S3 object deletion requires
human confirmation per Agent Autonomy — rollback is therefore DECLARED-AND-ESCALATED (COO fires or
confirms), not unilaterally executed.

## ⛔ BINDING P4 EXIT CONDITION (COO 140114Z, recorded as an obligation, not an intention)

**THE OLD ROOT `schwab/08335338/gold/` MUST BE DECOMMISSIONED AT P4.**

> Right now the copy is a PORT — Andrew's sanctioned method, verbatim: *"we simply do something
> correctly the first time and port over."* **The moment P4 lands and the old root survives, the
> same bytes become the never-decommissioned duplicate his 08-04 veto bans** — and it will be
> indistinguishable from one, because nobody will remember it was a cutover artifact.
> **A duplicate with a written death date is a port. The same duplicate without one is debt with a
> good story.**

**P4 MAY NOT BE CLOSED while `schwab/08335338/gold/` still exists.** This line is the exit condition
P4 inherits.

*(Why the copy is not the vetoed shadow: the veto hits STANDING parallel EMITTERS and STANDING
COMPARATORS. A copy creates neither — no second emitter, no comparator. Forward-only (option b) is
what the veto actually describes: two roots, split series, consumers reading both, permanently.)*

## Verification plan (COO 140114Z, adopted verbatim)

- **Two-sided object count, asserted PER TABLE, not just in total** — a matching total with one table
  short and another long is a real outcome of a partial recursive copy.
- **Count the MATERIALISED object set client-side.** A `--query 'length(...)'` on a paginated
  `list-objects` returns the PAGE count: 1,052 could read as 1,000 and look plausible.
- ⛔ **rc=0 is NOT the copy's evidence.** `aws s3 cp --recursive --quiet` has reported success in
  this estate while S3 kept the old bytes.
- **Sample re-read: >=1 partition from EACH of the four tables, reading the PARQUET, not the key
  listing** — presence is not integrity.
- **Fresh emission:** live `head-object` at the new root (write-side leg) + read-side resolution
  (CVO parity bar §8). ⚠ **On a cutover-window grade an UNCHANGED vintage is a QUESTION, never a
  pass** — a stranded re-point and a quiet day are byte-identical from presence alone.

## Not in this act

- The `dim_relationship` two-writer defect (FILED @c127712198/@753aeef4f0, bundled to P5 with the
  knob-2 superseded-vs-stopped question). A cutover changes WHERE, not WHAT.
- P4, the platinum read/serve side, where NEVER#3 binds. Gold is not served.

## Execution log

(appended below as each act completes)

## Execution log — ALL THREE ACTS COMPLETE

**ACT 1 — COPY (14:05Z).** 4,206/4,206 `copy_object` calls succeeded, **zero failures**; server-side,
per-key (no `--recursive`, no `--quiet` — every object's outcome observed, never inferred from a
process rc). **Two-sided count asserted PER TABLE on objects AND bytes, both sides materialised
client-side:** canonical_valuation 1,052/1,052 · 148,690,690 B both · flow_ledger 1,052/1,052 ·
42,631,532 B both · nna_canonical 1,052/1,052 · 13,256,247 B both · twr_daily 1,050/1,050 ·
120,507,009 B both. **ALL TABLES MATCH.** **Parquet integrity sample, one partition from EACH of the
four tables, parsed not listed:** 2024-08-21 (4,209 rows) · 2026-02-18 (1,198) · 2025-09-18 (188) ·
2025-12-11 (6,190) — **all four frame-identical to source.**

**ACT 2 — RE-POINT (14:16Z, @aa72ab5bc5).** The 1+10 surface as ONE act. Post-edit verification:
**zero gold paths remain on the old root**; the **10 silver/meta reads still `{SCOPE}`-derived**
(a00 3 · c00 2 · c02 2 · c03 3). `SCOPE` untouched in both knobs and now carries an inline
DO-NOT-RE-POINT note. ⚡ *Ruff surfaced a real signal, not lint noise: `SCOPE` became an UNUSED
import in `c01_runner` — proof that runner is purely gold with no silver reads.*

**ACT 3 — FRESH VERIFIED EMISSION (14:17:42Z), all three CVO §8 legs:**
- **LEG 1 VALUES** — re-read parses at the new root: 7,254 rows, 20 cols, fair_value sum
  $1,790,149,499.56.
- **LEG 2 WRITE-side location** — `head-object` at the new root: LastModified **ADVANCED
  14:05:42Z -> 14:17:42Z**, so this is *not* an unchanged-vintage question. ⭐ **ETag
  `c6d570d87f7120d8939c343725ffca25` IDENTICAL to the copied bytes — a fresh computation reproduced
  the copy exactly, so the re-point changed WHERE and provably not WHAT.**
- **DISCRIMINATING CONTROL** — the OLD root's same key is **untouched at 2026-08-11T18:43:30Z**,
  pre-dating the re-point. Had the re-point failed, the write would have landed there and advanced
  it. It did not. Rollback surface intact.
- **LEG 3 READ-side** — `OUT_ROOT` resolves to `portal/gold/advi/49financial`, and a consumer's
  series listing at it returns **526 / 526 / 526 / 525 partitions (2024-07-08 .. 2026-08-10)**.
  ⚡ *This is exactly the leg the stranded-series defect would have broken: a forward-only re-point
  returns 1 partition here and computes qtd/ytd/12m over a single day.*

**Status:** CLOSED 2026-08-12T14:20Z — three acts complete, verified on re-reads throughout, nothing
removed at the source, rollback available.
⛔ **The P4 EXIT CONDITION above remains BINDING and OPEN: the old root must be decommissioned at P4,
and P4 may not close while `schwab/08335338/gold/` exists.**
