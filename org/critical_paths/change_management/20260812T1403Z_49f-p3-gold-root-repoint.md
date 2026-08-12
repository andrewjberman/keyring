# Deploy-completion ledger: 49F P3 gold-root re-point (copy + re-point + verified emission)

**Status:** OPEN
**Opened:** 2026-08-12T14:03Z (deploy-start) | **Closed:** —
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
