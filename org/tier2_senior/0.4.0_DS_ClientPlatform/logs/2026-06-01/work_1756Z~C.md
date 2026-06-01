# work 1756Z — 0.4.0_DS_ClientPlatform~C — universe A/B decision-support brief

**Tick:** /work 2026-06-01 ~1756Z. **Trigger:** COO 175241Z — reconcile 7/7 ACCEPTED; Item-3 RETRACTED (folds into DS~B re-derive AC6, would collide on shared MDPF artifact); REDIRECT freed capacity to disjoint A/B decision-support.

## Done this tick
- Item-3: correctly NOT taken (COO confirmed it's not standalone — CVO root-caused 5c6f86840 + folded into DS~B AC6). Avoided a shared-writer collision.
- **Universe A/B decision-support brief** (`docs/briefs/find-insure-universe-ab-decision-support-20260601.md`, 2df9d38ec pushed) — read-only off the source-list + rep-BD gate I built; NO universe change. Arms Andrew's #2 (expand-to-WM/AM vs insurance-IMO-only):
  - Option B baseline: 99 insurance IMOs -> 24 in-scope (7 present + 17 adjacent; 75 absent); 23 ranked + 1 adjacent-WM sidecar (PMA); 109 contacts; 44 series-licensed.
  - A-narrow: +1 firm (PMA, ranks #1 0.858 but category-mismatch); ~3 more possible across full 99.
  - A-broad: new WM/RIA source, not quantifiable, separate sourcing + scoring rework.
  - Precision: rep-BD gate holds entity-resolution (category-agnostic); the THESIS signal (series-license=AM-transition) breaks for already-AM WM firms — that's the real risk, an Andrew judgment not a mechanical one.
  - Recommendation: B-core + FORMALIZE the adjacent_wm_targets sidecar (best-of-both, one-flag-reversible); defer A-broad as separate sourcing.

## Commits
- `2df9d38ec` (A/B decision-support brief) — pushed origin/CLOUD.

## RAVC2
- COO 175607Z (brief + recommendation; COO routes to Andrew with #2).

## State
- FIND_INSURE active work fully done; this brief arms the LAST open FIND_INSURE decision (Andrew's universe A/B). No disjoint work remains that doesn't collide with the DS~B MDPF constraint -> hold-warm per ToC unless COO has more disjoint work.
