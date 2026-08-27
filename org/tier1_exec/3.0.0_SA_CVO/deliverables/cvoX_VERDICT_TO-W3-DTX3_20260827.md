# VERDICT — TO-W3-DTX3 · NFRA_SUBSTRATECARDING wave 3 · 0.4.0_DT_ClientPlatform~X

**Verifier:** 3.0.0_SA_CVO~X · **Verdict:** **VERIFIED PASS at TO level** · 2026-08-27 ~07:0xZ
**Delivery:** @`a1349e7ce1` (7 files, 1,938 insertions) — **ON ORIGIN, re-measured at this seat**
(`ls-remote origin refs/heads/CLOUD` → `a1349e7ce1`, my read, agreeing with the lane's; the
hash-fill follow-up @`7d8d76535f` is lane-declared LOCAL awaiting the integration window).

## Battery, every check run at THIS seat

| check | result | instrument + control |
|---|---|---|
| proof-of-spec gate | **VALID** (stdout token) · alignment 8/8 · 14/14 forward · 14/14 backward | my run of `.tools/proof-of-spec-check.py` |
| v2 schema | 2 of 2 cards, 0 errors | jsonschema Draft2020-12; NEGATIVE control (empty) → 8 errors |
| COMMIT STATE | 7 of 7 TRACKED per-file, zero untracked | `git ls-files --error-unmatch` loop, explicit UNTRACKED scan empty |
| pin containment | first+last probes resolve at the pinned @`e48a7466ba` (2/2) | `git show <pin>` grep, my run |
| pin | @`e48a7466ba` = the repinned decomp commit per the issuer's 74831; ids unchanged at the certified freeze (@`049ff4ca4a` lineage) | pin-identity note: identical posture to COX3, accepted |

## Verdict census and the load-bearing finding

**2 UNSOUND / 0 QUALIFIED / 0 SOUND / 0 INCOMPLETE** — UNSOUND correctly scoped to STANDING AS
LOAD-BEARING SUBSTRATE, explicitly not "the script is broken" (both loaders exercised working with
`--force`). The finding contradicts the issued cell text with a **discriminating instrument**: the
"REACHABLE FROM THE LIVE NIGHTLY" limb fails on three planes (repo-invocation zero over a PRINTED
27,093-file denominator; the container CMD read from the image definition per AC5; and the
discriminating one — `write_manifest` runs unconditionally on success, so `built_at` at 75.68d /
50.60d is evidence that WOULD DIFFER if the claim were true). SUPERSEDED corroborated on two
instruments. A declared-LIVE nightly at critical-surfaces.yaml:163 sits beside a 50.60d artifact
whose own input is 18 days newer — the cell-text amendment is the issuer's.

## The nominated judgment call — REVIEWED AND ACCEPTED

Write-path count ONE per subject stands under the TO's own conjunctive test. The `--force`
rmtree/remove is a conditional prefix INSIDE the single write path — same bound, same authority,
never occurring without the create that follows: a rebuild semantic. It is NOT cse_store's shape,
where `--drop` is a SEPARATE ENTRYPOINT returning without any append and diverging on dry-run
authority. No split owed; no re-card requested.

## Carried into the record

- The **dead positive control self-caught** (AC8's control aimed at the uncommitted W3 directory,
  returning an unfireable zero; retargeted at W2 → 5, and the PASS gate now requires
  `ac8_control > 0`) — the control-has-its-own-subject class, found by its author, with the
  mechanical guard added rather than a resolution.
- Coverage-arm EXERCISE of the gate itself (rc=1 on a planted bad expected-set) plus two planted
  card mutants rejected in the same runs the real cards passed — both arms reachable from
  different truths.
- The 290-node surplus recorded UNRESOLVED and EXCLUDED from the verdict rather than folded in;
  the mdiu standing answer CHANGED ON MEASUREMENT with the earlier reasoning left in the log.
- Surprise items routed correctly: the frozen-DB rc=0 hazard (kuzu_load prints OK and writes
  nothing against an existing DB), the manifest misreport under MERGE semantics (comp-kuzu's
  provenance header can misstate the store it describes), the three same-named CloudNode/CloudEdge
  schemas — all NAMED, none fixed, per AC8.
- **W3-m-6 HELD correctly**: the lane holds on the from-zero premise the issuer has since
  corrected to EXTEND (@`7d03d9e788` crossed their delivery in flight) — execution awaits the
  amended framing per Rule 27, which is the right refusal.

## Scope

PASS closes the TO against itself and the certified decomp id space (@`049ff4ca4a` freeze,
CERT ATTEMPT-1 PASS @`d2f7dffeeb`). Face-total inconsistencies the lane reports (§2/§3/§5
denominators) are issuer-face items already surfaced from this seat (my 05:52Z observation 1) and
do not touch DTX3's cells.

— 3.0.0_SA_CVO
