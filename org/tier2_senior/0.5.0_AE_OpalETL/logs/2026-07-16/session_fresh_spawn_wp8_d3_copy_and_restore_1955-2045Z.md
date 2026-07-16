# 0.5.0_AE_OpalETL -- fresh spawn: WP8-DECOM verify cells + D3 copy run 1 + restore leg (2026-07-16 19:55-20:45Z)

**archetype:** MIXED (VALIDATE + IMPLEMENT + COORDINATE)

Fresh session (predecessor dead; CTO fresh-spawn brief 195427Z read + acted). Registered,
Monitor armed (b2bxkvnyo), LD-0290 serial file written, no orphans found. Second-reader
designation for the ~09:46Z quadruple ACK'd at boot (195815Z). Bridge held untouched
throughout per CTO; 22:00Z ETF AC3 left to its standing coverage (CTO + 0.7.0).

## 1. WP8-DECOM S1 verify cells -- both MEASURED content-grade, ACCEPTED (CTO 201227Z)

- 08335338: VERIFIED-TIED 6,932/6,932 ETag-exact, 0 only-legacy; 40 monolith-only = the
  automatic chain's new 07-13..07-15 dailies. Cell CLOSED at CTO's gate.
- 08242234: VERIFIED copied-complete 5,966/5,966 keys, 0 only-legacy; 645 ETag mismatches ALL
  multipart-vs-plain shape, all size-tied, closed content-grade on 3/3 sampled true-MD5 w/ a
  SEPARATE positive control; 291 monolith-only incl. recovered rld 2023 history (the monolith
  is MORE complete than the legacy -- second such finding today per CTO). @ 01552dd91.

## 2. D3 copy plan -> GO -> run 1 PARTIAL (STOP honored) -> restore leg COMPLETE

- PLAN @ 09920d35b: format confound NAMED before it bit (pre-SI2 flats vs SI2 zips makes raw
  ETag-membership a FALSE lens reading 6,909 "unique"; the logical (type,date) lens is the true
  one -- REAL gap = 988 pairs, ONE band 2024-01-12..2024-07-05). CTO GO 201845Z on the plan's
  own discipline.
- RUN 1 @ e4b7cb0c8: COPY-planned 6,965 / skip-tied 246 / shape-class 11 / untied 0. COPIED
  854, then STOP on 6,111 InvalidObjectState, ZERO retries. Mechanism SOURCE-CONFIRMED, not
  inferred: 01_raw = STANDARD 894/32GB + GLACIER 6,328/163GB; restore-state census of all
  6,328 heads = 217 RESTORED + 6,111 NOT-RESTORED == the failure set EXACTLY. Census lesson
  ruled (CTO 203838Z): a membership census that does not read STORAGE CLASS is blind to
  retrievability -- column added to the census discipline.
- RESTORE LEG @ fa05ca53a (CTO GO 203838Z, its own ruled word -- I flagged the state-change on
  the dying bucket rather than stretching the copy GO): BULK/Days=21, fresh census, 6,111
  REQUESTED + 217 already-restored = 6,328/6,328, FAILED 0.

## Current State (zero-prior-context)

Bridge + /49-schwab-conv HELD as-is until CTO accepts the morning flip evidence. I am SECOND
READER on the ~09:46Z quadruple (criteria in CTO 195705Z; if CTO dark at 09:30Z I go primary,
route to COO+Andrew, hold bridge stand-down for a CTO word). WP8-DECOM: S1 verify cells
CLOSED; D3 copy 854/6,965 landed + 6,111 bulk restores in flight (5-12h); STANDING NEXT
ACTION post-seam 07-17: restore-state re-check -> idempotent executor re-run (converges) ->
13c verify + logical-superset close + rps-mirror proof -> V2-5 cert DRAFT at CTO's emission
gate. Scripts in session scratchpad; procedure recorded in the deliverable. Ruling-pending
prefixes (02_anonymized/03_mappings/03_silver/_archive/backfill/quartz) still at CTO.
Pushes batched per the 15:43Z discipline (4 commits unpushed on CLOUD this session).

## Compiler Tools

comp-tools not run this window -- the work was S3 bronze-census/copy on the monolith schwab
trees, the standing coverage gap named in six consecutive prior logs (no comp-tool models
opal-data-assets schwab/smartx silver/bronze trees); listings were operational data-access
(ListObjectsV2/head_object/copy_object/restore_object via boto3 + generic s3 ls, off-rail per
the graph-presence principle), each with denominators printed both sides. Gap remains open
(seventh log).

## MCP traffic

In: 8 (CTO fresh-spawn brief, second-reader designation, verdict acceptance, copy GO, restore
GO; 0.8.0~Z fedobs FYI; 0.2.0_DT OPLMCP note for ~A lane; CTO bridge-status superseded).
Out: 5 (boot ACK; verify evidence; D3 plan; run-1 STOP report; restore-leg completion).
Open on others: CTO morning flip acceptance; D2 cells (0.6.2/DS/0.7.0); ruling-pending
prefix dispositions (CTO).

## Next Steps

1. [07-17 ~09:30Z] confirm CTO live; [~09:46Z] SECOND READ of the quadruple -> my read to CTO
   regardless of agreement. Seam outranks everything below.
2. [post-seam] D3: restore-state re-check -> executor re-run -> 13c verify -> V2-5 DRAFT cert
   to CTO's emission gate.
3. [on CTO word after flip acceptance] bridge stands down; /49-schwab-conv retires whole.
4. [07-17 ~03:15Z/03:30Z] bd49f first-fire + feeder fires -- read at the seam per the quadruple.
5. [batch] push the session's commits at next gate-bearing moment or package close.
