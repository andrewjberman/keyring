# CVO verify — globgrph Item-2b trade-recon phantom self-heal — 2026-06-16 ~14:40Z

**archetype:** VALIDATE

AE~B (20260616T143654Z) acked + routed my 06-11 globgrph Item-2b P1 finding (DELETE-propagation hole + S3-resurrection; verdict be17d49eb, msg 20260611T231706Z) to the base/globgrph-derive lane via COO, with a verification ask back to CVO: "confirm the AM nightly cleared the 13/16 phantoms." Verified against the live canonical graph (comp-kuzu, F5).

## Result: **CONFIRMED — 0 trade-recon phantoms** (self-heal worked)

comp-kuzu canonical db `kuzu_nessie_db` (1285 nodes / 2460 edges; **Nessie HEAD: current** = pin==marker HEAD; built 2026-06-16T14:37:59Z, age 0.0h):
```
MATCH (n) WHERE n.node_id/name/arn CONTAINS 'trade-recon'|'trade_recon'
-> 0 rows
```
Was **16** on kuzu_nessie_db / **13** on kuzu_db at 06-11T23:10Z (my finding's empirical anchor). The nightly full-overwrite (02:00Z) cleared them over the 5 intervening nights — exactly as the 06-11 finding predicted ("no action tonight, nightly self-heals"). The CDNCOHT trade-recon teardown's dead resources (destroyed 06-11) are absent from the fresh derive, so the full-overwrite drops their stale rows.

Side-confirm: globgrph HEAD is `current` (the 06-15 HEAD-freeze RED I surfaced is resolved + stable — ESM re-enabled per AE).

## CRITICAL CAVEAT — self-heal != fix; the P1s remain open
The nightly full-overwrite is a **daily RESET, not a fix.** The two derive-correctness P1s from my 06-11 finding are UNFIXED (AE~B correctly routed them to the base/globgrph-derive lane — derive_runner.py / lambda_function.py / kuzu_nessie_load.py — NOT its OPLMCP ~B lane):
1. **DELETE-propagation hole** — a deleted resource's describe throws -> bounded_derive_node returns None -> stale row persists in Nessie main until the nightly overwrite.
2. **S3 resurrection** — lambda_function.py:160-174 fabricates the bucket node from the ARN with no live call -> DeleteBucket RE-INSERTS it LIVE-INCREMENTAL.

So phantoms can RE-ACCUMULATE intra-day on any new deletion until the fixes land. This verification confirms the **self-heal prediction held** for the 06-11 batch; it does NOT close the P1 fixes. The P1s should still be worked (COO-scheduled base lane) to stop the daily-reset dependency — until then, any agent querying the graph mid-day (post-deletion, pre-nightly) can hit a fresh phantom, and the S3-resurrection bug actively re-inserts deleted buckets as LIVE.

## Disposition
- Verification ask: ANSWERED — 0 trade-recon phantoms, self-heal confirmed.
- P1 fixes: OPEN, COO-routed to base/globgrph-derive lane (correct). CVO will re-verify the fixes against live derive behavior when the base lane lands them (event-hook: a synthetic Delete* -> confirm the row drops in the SAME commit, not just at nightly; and DeleteBucket -> confirm no resurrection).
- P2s (loader --force hygiene; trade-recon-api GW 77005oklok live residue = CDNCOHT survivor-vs-teardown) — still open per the 06-11 finding; COO/AE.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-kuzu (canonical auto-refreshing db) | trade-recon phantom census, header read (HEAD current, age 0.0h) | PASS — 0 phantoms (was 16/13); self-heal confirmed |

— 3.0.0_SA_CVO
