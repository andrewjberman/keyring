# CVO Verify-Channel Verdict — DEMOV1.004 attempt-10 rate-magnitude — 2026-05-23 ~23:13Z — **YELLOW**

**Charter:** MSTR CY-0051 magnitude-sanity finding routed to CVO MECHANICAL verify-channel. Observed 0.39 obj/sec on DS~C attempt-10 transform; 7-12× over original wall estimate (45-90m → ~12h projected).

## Question (a): is 0.39 obj/sec plausible for this transform shape?

**Plausible but suspicious.** Multi-tier S3 PUT + Python pseudonymization + fake-identity dedup + advisor/client/account fan-out is non-trivial per-object, but:
- S3 PUT rate-limit is ~3,500 PUT/sec per prefix; 0.39 obj/sec is **4 orders of magnitude below** that ceiling — S3 is NOT the bottleneck.
- 0.39 obj/sec ≈ 2.6 sec per object. For Python-side pseudonymization workloads of this shape, more typical rate is 10-50 obj/sec.
- The slowness is more consistent with per-object processing overhead (Python-side fake-identity probing, S3 connection setup if not reused, hash computations, set membership checks).

**MECHANICAL (a): YELLOW** — rate is below expected baseline for this workload shape; not definitively pathological but warrants empirical comparison vs prior attempts.

## Question (b): could attempt-10 fixes introduce per-record overhead?

**YES — empirically traceable in the diff at `data/demo/scripts/transform/fake_identities.py:159-212`** (commit `9e02fc35d`):

The `client_name()` method for distinct-surname couples was changed from single-execution → **`for probe in range(4096)` loop**. Each probe iteration does:
- 4× `_bucket(seed, real_name, f"cc/l{p}", len(_LAST_NAMES))` hash computations
- 2× component-string construction (`c1`, `c2`)
- 2-3× set-membership checks against `_used_person`
- Total per-probe: ~6 hash ops + 3 set lookups

**Worst case:** 4096 probes × ~9 ops = ~36k Python ops per distinct-surname couple. For couples that find a clean fake on the first probe (which the leak-fix anchor expected), the cost is ~9 ops — negligible. But for ANY couple that hits collisions, the cost can balloon.

The **pre-seed** `_used_person.update(real_advisor_and_client_names)` is one-time at `build_mapping()` and not a per-record cost. But it **enlarges `_used_person` by O(real-name count)**, which means every probe's set-membership check is now operating against a much larger set (still O(1) but with constant-factor cost in hash-bucket walks for large sets).

The attempt-10 fixes are a **credible incremental contributor** to per-record cost, especially if the distinct-surname-couple fraction is high in the input data. Whether they're the dominant cost driver depends on:
1. What fraction of clients are distinct-surname couples
2. How often the probe loop iterates past 1 (i.e., collision rate post-pre-seed)
3. Whether other per-record costs (S3 PUT setup, other transform stages) dominate

**MECHANICAL (b): YELLOW — credible contributor, not dominant** without empirical profile-comparison. Recommend DS~C add timing on a representative slice vs attempt-8/9 to isolate.

## Question (c): is 30m polling cadence contributing to slowdown?

**NO.** Polling cadence is wall-clock heartbeat / status-check frequency on the DS~C session. The transform runs continuously regardless of polling interval. Polling cadence is purely about *observability* (how stale DS~C's broker summary is between heartbeats); it doesn't affect throughput.

**MECHANICAL (c): GREEN — orthogonal concern.**

## Verdict — **YELLOW** with one empirical recommendation

- (a) YELLOW: rate suspicious-low for workload shape
- (b) YELLOW: attempt-10 probe loop is credible incremental cost but not dominant without profile-comparison
- (c) GREEN: polling cadence is unrelated to throughput

**Recommendation:** DS~C runs a 100-object profile slice timing each major stage (S3 PUT, pseudonymization, fake-identity probe, dedup hash, advisor/client/account fan-out). Comparison against attempt-8/9 same-shape baseline isolates whether attempt-10 changes are dominant or merely incremental.

**Watch-class classification check:** the "watch-class" framing was correct for monitoring, but if profile-comparison shows attempt-10 added >2× per-record cost without correctness benefit, the project owner may want to consider whether the leak-detection mechanism itself (substring-scan) should be reconsidered (cousin to CY-0045 META observation that attempt-10 was already root-cause-rediagnosis from attempt-9; one more such pivot may indicate the mechanism needs structural rethink rather than further iteration).

**LD-0018 implication:** DEMOV1.004 wall-time stretching to ~12h shifts VALFIN.010/.011 absorbed-bundle pickup right; LD-0018 ratification window correspondingly delayed. No structural impact — just longer wait. Already noted in MSTR's framing.

**NOT BLOCKING DS~C.** Transform continues running. This verdict is verify-channel only.

— 3.0.0_SA_CVO
