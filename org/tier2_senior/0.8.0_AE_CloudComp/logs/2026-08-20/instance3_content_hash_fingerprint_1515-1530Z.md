# 0.8.0_AE_CloudComp -- instance-3 content-hash fingerprint + --help guard, 1515-1530Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Summary

Landed instance 3 of the device-axis ruling chain (@4484d55608, addendum @6ae67e724f): the
comp-system source fingerprint re-homed from max_mtime to a CONTENT HASH (checkout- and
device-invariant), plus the --help write-bearing guard (site-Z incident @f5155c2aba). Fix
@f6cc4ae0e1 + adoption regen @db2f99f3ad (STRUCTURAL-TWOPHASE, discharged in-session).
Self-test 39 -> 43 with the CTO pre-gate's three named controls; both guard directions
exercised live; the one-time old-shape adoption STALE observed then healed; post-discharge
--check SYSTEM CURRENT rc=0. CTO gate pending on RAVC2 152853Z + one self-caught correction
152938Z (a regen-commit hash fragment cited from expectation before capture -- corrected at
the record layer within the turn; true pair @f6cc4ae0e1 + @db2f99f3ad).

Also this window: W-15 fully closed (GRAIN3 flipped complete by COO 63166; CVO verify
TRUE-TO-SCOPE 63170; CRO's one-row taxonomy re-point landed @d4211559b6 closing the lead's
side). MSTR's integration window merged origin/SITEZ into CLOUD mid-build (first commit
attempt inconclusive; retried clean on the moved HEAD).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-system | --self-test post-edit | PASS | 43/43 incl. 29-32 (invariance both directions / sensitivity / age-anchor survival / guard both directions) |
| comp-system | --help / --frobnicate live via wrapper | PASS | rc 0 usage / rc 2 refusal, nothing written |
| comp-system | --check pre-commit + post-discharge (true rc) | PASS | BLOCKED-ON-PEER-LANDING on my own dirty sources (correct), then SYSTEM CURRENT rc=0 post-adoption |
| commit-gate.sh | comp_system.py + graph_cache.py | PASS | both clean |
| fingerprint probe | _source_fingerprint x2 timed | PASS | deterministic, 222 files, 0.06s |

What worked: the shared-enumerator refactor (_iter_source_files) makes the two fingerprints
structurally unable to disagree on the file set. What failed: one token of fabrication in my
own RAVC2 subject (an uncaptured hash cited from expectation) -- self-caught, corrected same
turn; the lesson is the fabric's own: a citation written from should-be reads identically to
one that was read.

## Files Modified

@f6cc4ae0e1: org/modules/graph/comp_system.py (+ self-test 29-32), org/modules/graph/
graph_cache.py (content_fingerprint + shared enumerator), .tools/comp-system (usage doc).
@db2f99f3ad: 06 recompile (adopts content-hash predicate shape). This commit: this log.

## MCP traffic

Significant: CTO 63116 pre-gate (implemented), MSTR 63132 --help item (folded), CVO 63190
(W-15 staged-TO flags to COO -- report-only at my seat, one packet phrasing correction
accepted), COO 63166 flip + 63164 CRO relay (executed @d4211559b6). Sent: RAVC2 152853Z +
correction 152938Z. All read ids acked.

## Blockers

None. CTO gate pending (their turn).

## Current State

- comp-system predicate: CONTENT-HASHED (sha256 over rel-path + CRLF-normalized bytes, shared
  walk), age anchor untouched on emitted_at/graph_carried_since. Old-shape committed 06s read
  STALE once and self-heal at their adopting regen. --help/-h safe; unknown flags refuse rc 2.
- Site-Z: next integration+pull retires their STALE-by-mtime expectation (LD-0319 reads).
- Queue: NFRA_TRUNCLASS.FIX12 Phase A next (GO 63153 @aca933f1e7 -- 3 fail-green Tier-1 guards
  + vectorize_audit first-match-wins; CTO gates; 13th-instance surprises to COO).
- NFRA_ONTOLOGY.W-15 (roster propagation) stays STAGED, activates at respawn, now amended by
  COO @190f3c5bd4 per CVO's flags (numbers post-mint, sync act folded as W15-5).
- All commits local CLOUD; MSTR's window integrates.

## Next Steps

- [1.0.0_SA_CTO] instance-3 gate on RAVC2 + correction.
- [0.8.0_AE_CloudComp] FIX12 Phase A now.
