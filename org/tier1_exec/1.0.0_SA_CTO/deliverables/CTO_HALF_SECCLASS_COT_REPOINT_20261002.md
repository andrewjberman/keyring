# CTO half -- the Cottonwood re-point: Cottonwood gold classifies from the canonical table by the ruled rule (MDPF_SECCLASS)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_COT_REPOINT_20261001.md` @40cc2e2108,
**blob `59c1da5458`** (equal at HEAD). Asked by `2.0.0_SA_COO~M`, msg 104063. Rulings: batch 86 items 5-8, batch 93, batch 99,
batch 113 (the six name-pattern entries). This half is a separate file bound to that blob.

## SIGNED, 2026-10-02 ~05:3xZ, by 1.0.0_SA_CTO -- CONDITIONAL: the served legs wait for the readers on every deployed portal build

On the blast radius the packet states: Cottonwood gold only, 554.62 M USD reclassed by the ruled rule with 97.72 M (17.6 percent)
served `unclassified` as the named residue (a correction of today's default guess, no regression in the ruling's terms); 871
served keys, one producer each (measured from the keys' version lineage); the mix gains `commodities`, `structured` and
`unclassified` as classes; seven portal readers change in leg P; one IAM read statement on the Cottonwood host role; Black Diamond
and Inflection unmoved. Both branches are covered (I or A fails: stop before G, nothing moves; R or the walk fails: G and P roll
back). Rollback per key is stated. The three preconditions are met (seed rows, CUSIP rows, the cash rule in the act).

**THE CONDITION.** The served keys this act rewrites are read by EVERY deployed portal build, not only DEV, and leg P lands on DEV.
PROD runs the strict readers (portal PROD `f2731ad3`), and seven of them drop a class they have not seen -- the census's own
finding. Batch 99 item 3: "A reader that would silently drop a class blocks the re-point." So:
- legs M, I and A may run now (code merged, one read statement, the shared client deployed -- each inert on what is served);
- legs **G, R and S wait** until leg P's readers are on every deployed build that reads these keys, PROD included. A portal PROD
  promote is Andrew's act; the served legs wait for it. Leg R writes the same served keys as a scheduled run, so it waits too.

Read by this seat at signing: the whole packet, including the merge trap and its fix (the dry merge differs from CLOUD in exactly
the ten files of leg M), the writer-per-key sweep (871 keys, 0 interleaved lineages), the re-measured values, and the six
name-pattern entries in `COT_REPOINT_TODAY_BY_TOMORROW_20261001.md` @e0f8d95bd8.

Named by this half in addition:

1. Leg I: its plan is read at the act; the plan must add exactly the one statement `CanonicalClassificationsRead` and change
   nothing else in `infra/aws/terraform/cot-pipeline`, or the leg stops -- the packet's own stop, made a condition here.
2. The colour gap: `unclassified` shares grey with `other` in the advisor Mix chart. Not a blocker; `2.0.0_SA_COO~D`
   (`chartColors.ts`) gives `unclassified` its own colour before leg S's walk.
3. Not verified by this seat: the 22 gold tests and the B_00 negative control, the re-measure script's run, the writer sweep's
   run, the portal branch's tests.

-- 1.0.0_SA_CTO

## ADDENDUM 1 -- 2026-10-02 ~05:5xZ: re-bound to the corrected packet, blob `801c2a9778`

`2.0.0_SA_COO~M` msg 104074 added a CORRECTION paragraph after both halves: `platinum/firm/mix_summary.json` has a second declared
writer, `data/cot/scripts/gold/runners_cot/d08_cot_mix_summary.py` (a fleet emitter), dormant -- the key's last three versions are one
daily lineage in D_04's shape. Its rule is read: it classes from its own A_07 table, which this act does not touch. Declared writers 2,
both rules read; the blast radius is unchanged. This half now binds blob `801c2a9778`, with every condition above unchanged: legs G, R
and S still wait for leg P's readers on every deployed portal build, PROD included -- leg P on DEV (`eb90f2ad`) does not release them.
Named: if d08 ever writes that key after the re-point, the firm view flips between two classifications; d08 is not scheduled while
D_04 writes the key, and its write of the key retires at the next change to `runners_cot`.

## ADDENDUM 2 -- 2026-10-02 ~17:5xZ: leg W, the watermark set back one partition before leg R (`2.0.0_SA_COO~M` msg 104332)

Legs M, I, A and G are closed (17:30Z). Leg P holds: PROD `f76b02acb6` carries `eb90f2ad`, read by this seat (batch 173). C_06's two
watermark keys read `data_as_of` 2026-10-01, so an ad hoc incremental run would recompute nothing on the new code, and leg R would
test nothing.

**SIGNED, leg W added before leg R** -- the same path as the Black Diamond re-land's leg W (batch 118 path (a)):
- Before the copy, record the current VersionId of each of C_06's two watermark keys. Those are the rollback.
- Copy each key back from its `data_as_of` 2026-09-30 version (`copy-object`, metadata COPY).
- Leg R's one ad hoc QA run then recomputes 2026-10-01 on the new code. Its acceptance is the packet's.
- Rollback for leg W: copy the recorded current versions back onto both keys. Nothing is deleted.

**Blast radius:** unchanged in kind. The recompute rewrites Cottonwood's 2026-10-01 served mix outputs, which is the re-point's
served move this half already covers. Leg S (the 10-02 scheduled fire) stays the acceptance.

-- 1.0.0_SA_CTO
