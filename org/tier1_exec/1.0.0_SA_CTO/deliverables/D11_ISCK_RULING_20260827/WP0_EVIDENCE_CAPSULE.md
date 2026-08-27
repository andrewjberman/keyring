# WP-0 EVIDENCE CAPSULE — the C2/C3 evidence estate, pinned

**Act:** ISCK ruling WP-0 (Andrew-direct 2026-08-27, `RULING.md` this directory): *"pin the existing
C2/C3 evidence and its producer into immutable, digest-addressed storage."* Executed by
`1.0.0_SA_CTO~X`, 2026-08-27. Storage decision: **git** (12.4 MB total, within the recommended
retention split of git <50MB / S3 above; recorded as REC pending Andrew's retention-policy word).

## THE EVIDENCE FILES — now TRACKED, digest-pinned

| canonical name | sha256 (raw bytes, no normalization — binary-faithful data pin) | bytes |
|---|---|---|
| `c2_motifs.json` | `cc9b66271a16614e52cc3e5d010afb5eda4c57b734b1a40f825127786eb5fc6a` | 10,329,963 |
| `c3_structures.json` | `5502513236d159f9c13d2e673396662cad493d2ccb669eaa870870aad7d9a7d5` | 2,115,118 |

Home DIR: `org/tier1_exec/3.0.0_SA_CVO/deliverables/kimi_subdivision_harness/`

**CANONICAL RENAME (Andrew-direct at the CTO~X terminal, 2026-08-27, verbatim: "we should use
c2_motifs.json since thats canonical naming for what they actually are"):** the file previously on
disk as `c2_instances.json` is pinned under the canonical name **`c2_motifs.json`**. Digest verified
byte-identical across the rename (`cc9b6627...` both sides) — **the identity survived; the binding
changed** — which is the ISCK discipline exercised on its own first artifact.

⚠ **BINDING NOTE, recorded not remedied:** the producer still names the OLD key —
`c3_cover.py:251` default `--in c2_instances.json`, `c2_individuate.py:641` default output
`c2_instances.json` (4 references total, all inside the harness; 0 in `docs/architecture`). A fresh
producer run would emit under the old name beside the canonical pin. The remedy belongs to the
canonical-materializer rebuild (or a CVO-lane edit — the harness is `3.0.0_SA_CVO`'s artifact), NOT
to this capsule. Until then: readers use `c2_motifs.json`; the old name in code is a stale binding.

## SOURCE FRONTIER — recovered from the artifacts' own headers, then stated with its limit

Both files EMBED their provenance (read from bytes, not recalled):

```
producer (c2)      "3.0.0_SA_CVO c2_individuate -- one node per MATCH (DONE-MEANS item 1)"
producer (c3)      "3.0.0_SA_CVO c3_cover -- anchor-NODE overlapping-domain-cover (DONE-MEANS item 2)"
graph_vintage      nodes_snapshot_id  8601547680771488785
                   edges_snapshot_id  6655148935215910630
                   db_built_at        2026-08-07T02:20:12.291927+00:00
supersedes (c2)    motif_c2c3_materialize.json / motif_c2c3_materialize_ab.json (shape)
file mtimes        c2 2026-08-07 00:49 local · c3 2026-08-07 00:55 local
fabric             LAPTOP (this device; the files never existed elsewhere)
```

**The frontier is PARTIALLY RECOVERABLE, better than the repo-state audit feared:** the Iceberg
snapshot ids pin exactly which `graph_nodes`/`graph_edges` versions fed the run, and the Nessie
`_refs`/`_objs` store (once registered as L0 parts per WP-3) is the authority that can resolve them.
**Seeds: NOT APPLICABLE for these two files** — `c2_individuate` and `c3_cover` are deterministic
(anchor-keyed cover, no stochastic step). The seed-instability finding (AMI 0.505) belongs to the
**SBM structural-view run, which is a DIFFERENT artifact with NO committed producer** — that
reconstruction remains open as WP-0's residual (below).

## THE PRODUCER — bound at blob grain, at the pinning commit's HEAD

| file | git blob (HEAD at pin time) |
|---|---|
| `c2_individuate.py` | tracked; blob pinned by the capsule commit itself |
| `c3_cover.py` | tracked; blob pinned by the capsule commit itself |
| `kimi_pipeline.py` / `kimi_steps_monolith.py` / `stage1_sides.py` | tracked; same |
| 4 `test_*.py` | tracked; same |

(The pinning commit hash IS the immutable producer-version reference: `git ls-tree <this commit>
-- <harness dir>` enumerates every blob. A separate digest table would be a typed-beside-derived
duplicate of what git already guarantees — deliberately not minted.)

⚠ **Producer-version LIMIT, stated:** blob-grain is NOT the full ISCK `materializer_version` bundle
(no dependency lock, no configuration digest, no declared-opinions contract). That bundle shape
lands with 3A; this capsule pins what is pinnable today and names the gap rather than faking the
rest.

## WP-0 RESIDUAL — open, named

1. **The SBM structural-view producer is NOT in the repository** (repo-state audit, corroborated by
   sweep). The 177,474-nat / purity-0.989 headline evidence has no committed producer. Options:
   locate (it may live outside the repo trees swept) or reconstruct against the pinned snapshot ids
   above. NOT done in this capsule; it is the remaining half of WP-0.
2. Retention policy REC (git <50MB / S3 above) awaits Andrew's word — if he rules S3, these pins
   move by copy (digests travel), never by deletion-first.

— `1.0.0_SA_CTO~X`, 2026-08-27
