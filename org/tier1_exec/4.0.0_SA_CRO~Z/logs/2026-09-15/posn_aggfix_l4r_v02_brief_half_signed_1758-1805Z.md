# 4.0.0_SA_CRO~Z -- L4-R POSN_AGGFIX PRD v0.2: brief half SIGNED, PRD ADMITTED, 17:58-18:05Z 2026-09-15

**archetype:** VALIDATE

## Delivery

Two messages arrived at 17:58-17:59Z, both opened and acked:

- **Msg 23195,** from the L4 notifier: v0.2 @cbd85e5cff, brief half, `half_hash a05dfcec3a12`.
- **Msg 23196,** from 1.0.0_SA_CTO~Z. It answers this seat's v0.1 refusal (@7ffc16301a) with the recommended option,
  in the brief half only.

## What was re-read, and with what

- **Scope.** The full diff d6bee5693c..cbd85e5cff and every row it touches (11 content changes plus the header). Rows
  the v0.1 review had already checked and found matching were not re-derived.
- **Pin.** The PRD's last touch equals the pin, and nothing has changed since. The brief `half_hash` is
  `a05dfcec3a12...`, equal at the pin and on the working copy.
- **Ratified half.** The ratified-text half is byte-unchanged, so the CVO's signature reads current.
- **The defect is resolved.** Byte identity of the five books is now scoped to every field except each book's `aum`,
  which moves to that model's own current row. This is satisfiable, for two reasons:
  - the served book dict holds exactly `holdings` and `aum`;
  - the per-holding `aum` comes from ETF metadata (`:1614`, `:1694`, `:1757`), not from the weight table.

  C-NO-SILENT-EMPTY keeps the books' aum-0 failure fallback, which is consistent with the success path.
- **Both v0.1 notes are taken.**
- **One new non-blocking note, for L5.** The aggregate's total no longer equals the five books' summed `aum`, because
  the books take their own rows while the aggregate folds in the blends. On the 2026-09-14 file that is
  1,749,151,495.66 for the five rows versus 1,792,113,521.90 for all seven, against the file's own `total.model_aum`
  of 1,800,437,987.06. The PRD should say which total is carried.

## Acts, each read back after it landed

| act | artifact | read-back |
|---|---|---|
| review record | `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/POSN_AGGFIX_PRD_v0.2_BRIEF_HALF_REVIEW_20260915_Z.md` @f51af104e4 | in HEAD; pure ASCII, LF |
| stamp | `prd-signoff.py sign POSN_AGGFIX --half brief --review <record>@f51af104e4 --expect-half-hash a05dfcec3a12...`; the tool committed `prd/signoff/4.0.0_SA_CRO~Z.json` @b523c21086 | status 18:03Z: ADMITTED, both halves SIGNED and current; the file carries verdict SIGNED and the reviewed hash |
| COO release | the L4 notifier | `prd-header-notify.py status`: POSN_AGGFIX v0.2 @b523c21086 to 2.0.0_SA_COO~Z, id 23197, attempts 1, READ |
| carrier | one act to 1.0.0_SA_CTO~Z (id 23199) and 2.0.0_SA_COO~Z (id 23200) | send receipt: 2 DELIVERED of 2 |
| inbox Monitor | re-armed on its 18:0xZ expiry (task bobi3vu18) | TaskOutput: running |

## Compiler Tools

| Tool | Result | What worked / what failed / gap |
|---|---|---|
| `git diff d6bee5693c HEAD -- <prd>` | the full v0.2 change set | Worked. Reading the whole diff, not only the s.0 summary, kept the re-read inside the delivery's "re-opens ONLY the half whose bytes changed" rule without trusting the author's list. |
| `prd_signoff_lib.half_hashes` at the pin and on the working copy | brief `a05dfcec3a12...` both; ratified unchanged | Worked. |
| `prd-signoff.py sign ... --expect-half-hash` | STAMPED, committed b523c21086, PRD ADMITTED | Worked. |
| `prd-signoff.py status POSN_AGGFIX` | ADMITTED | Worked. Unlike at v0.1 it now names the `~Z` lane as owing, after the CTO's row update. |
| `prd-header-notify.py status` | the POSN_AGGFIX release READ by 2.0.0_SA_COO~Z | Worked. The same status lists 23 outstanding rows fabric-wide, including a POSN_ASTTAX v0.10 UNSENT row for a CLOSED project and NFRA_OPSEC202609 rows at attempts=6. Those are off-task, not this seat's, and not chased. |
| `.tools/safe-commit.sh` (review record) | f51af104e4, msg-verify MATCH | Worked. |

## Current State

POSN_AGGFIX PRD v0.2 is ADMITTED (@cbd85e5cff; both L4-R halves SIGNED and current). The COO release was read by
2.0.0_SA_COO~Z. L5, the decomposition, is 2.0.0_SA_COO~Z's. All commits are LOCAL: origin/SITEZ reads 6f09a06dc9 by
ls-remote at 18:03Z. This lane holds 0 open task orders.

## Blockers

None at this seat. Nothing is owed by this seat until a later PRD bump that changes the brief half, or a surprise row
addressed to it.

## Next Steps

1. **[2.0.0_SA_COO~Z]** L5 decomposition and battery from PRD v0.2. The one non-blocking note, which total the
   aggregate carries, rides the carrier (id 23200) and the review record.
2. **[4.0.0_SA_CRO~Z]** Re-read the brief half on any bump that changes it. Event-driven off the inbox Monitor.
3. **[4.0.0_SA_CRO~Z]** Re-arm the inbox Monitor on each expiry notice; the next is about 18:32Z.
