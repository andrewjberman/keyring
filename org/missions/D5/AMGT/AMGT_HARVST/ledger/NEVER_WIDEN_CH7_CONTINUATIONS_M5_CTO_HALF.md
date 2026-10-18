# NEVER-WIDEN -- CTO HALF: `HVST-ch-7`, 78 continuations at method /5 (round 93)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~04:5xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round93/NEVER_WIDEN_HALF_COO_CH7_CONTINUATIONS_M5.md` as committed at
dc5611d194, sha256 `19d80c8bf6bafa94157d1152cc2bcf9f8a11a58fe0c21dc877c49f0dbf8f213c`. Any edit to that file voids this half.

## What I read at signing

- **The writer's rule** (N = 1): `continuation.write_one` (`lib/research/corpus/continuation.py:1049-1069`).
  - It builds fresh, names the object `_inputs_sha16(document["inputs"])`, and writes through `gold.gold_put`, which never overwrites.
  - Each /5 object is therefore new, beside the old one. `dossier.write_one` is not called.
- **The list:** `ch7_securities.txt` has 78 lines, sha256 `db965262...698ac`, equal to the half.
- **The measurement** (ch-8, re-run by the issuer): 78 of 78 names read `fields_changed=0` with inputs equal. The positive control reads 0
  and the planted negative reads 1. So the only served moves are `continuation_key` and `source_keys` naming the new object, and the half
  names both as expected.
- **The code pin, measured at this seat's HEAD:** `git diff --stat 091ebacda9 HEAD -- lib/research` is NOT empty. RESAPP round 116 (bw-1,
  bw-2) has since changed 22 files under `lib/research/print/` and `lib/research/api/scoped_amgt.py`. The "or a later commit" limb of C-1
  therefore fails at today's HEAD, and the seat must use a worktree AT `091ebacda9` exactly (condition 1 below).

## Blast radius

- 78 gold keys are added under `amgt/harvest/gold/research-continuation/`. Nothing is overwritten or deleted.
- Served: for each name, `continuation_key` and `source_keys` move to the new object. Every `continuation_fields` value stays equal.
- Dossiers, fund forms, silver, the gateway code and service, IAM and schedules are untouched.

## Both branches

Branch A and Branch B are as the COO half states them, per name. A Branch-B repair is a still newer /5 object, decided by the issuer and
this seat; the seat deletes nothing.

## Rollback

ADD-ONLY. Removing the 78 keys restores the pre-act pick. That is an S3 delete, Andrew's act, and it is not pre-approved here.

## Conditions of this signature

1. **The worktree is cut AT `091ebacda9`, and `git rev-parse HEAD` is printed in `ch7_before.out`.** A later commit qualifies only if
   `git diff 091ebacda9 <commit> -- lib/research` prints empty, which today's HEAD does not.
2. **C-1 to C-10 bind as written.** That includes:
   - C-6: no dossier write;
   - C-7: the UNH-then-CPA canary, read through the gateway before the other 76;
   - C-8: the picker census re-reads `no_current=0 new_differs_from_gateway=0`, and the dossier count is unchanged;
   - C-10: site Z is told first, and there is no GO before its answer.
3. **The S44 rule** applies (foreground, batches of 10 at most, a manifest line flushed per name), and the NEVER-2 close is COMMITTED with
   the manifest.

## VERDICT: SIGNED (CTO).
