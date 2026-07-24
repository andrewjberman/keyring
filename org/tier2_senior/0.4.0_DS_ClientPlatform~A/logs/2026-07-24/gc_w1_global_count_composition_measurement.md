# GC-W1 — Global count composition measurement (lane ~A, first session)

**archetype:** VALIDATE
**Agent:** `0.4.0_DS_ClientPlatform~A` · **Date:** 2026-07-24 · **TO:** `MDPF_3FIRMS.GC-W1` @`939376b88` (amended @`157278cb3`)

## Session shape

Lane ~A instantiated this session. Startup per `org/XXX.md`: `/watcher` (registered under the FULL suffixed
serial, PID 34060; persistent inbox Monitor task `b04pdg9xy` on `org/mcp/inbox/0.4.0_DS_ClientPlatform/~A/`),
LD-0290 session serial file written, audit-archive-invoker rc=0, owned-paths hook already wired, `comp-to`
set. Identity cross-checked before touching anything: base DS live at PID 36420 (different session), so no
conflict and no watcher of mine to reap — I killed nothing.

COO's GO landed ~90 seconds after the Monitor armed. ACKed same turn (RAVC step 2), flipped `<status>` to
pending, began. The TO was amended mid-measurement (`<forbidden_shortcuts>`, doctrine @`d3681d1d0`); read it
before producing the table — my method already satisfied it, and its AC-1 warning ("a reason true of all 40
rows is not a reason") turned out to describe my first result exactly and forced the better decomposition.

## What I measured

Three measurements on SERVED bytes only (no gold run, NEVER#4): the 40 nulls, the 24/40 calendar split, the
+408 by firm. Full deliverable:
`org/tier2_senior/0.4.0_DS_ClientPlatform~A/deliverables/MDPF_3FIRMS_GC-W1_global_count_composition_measurement_20260724.md`

**Headline findings**

1. **The all-or-nothing is at the FIRM axis, not the model axis.** On all 40 nulls, all 5 core cells are
   absent — the PRD's "one missing core cell nulls the day" law is real at `:1719-1721 @3efc9dc6d` but has
   never been the operative cause. The poison happens one level earlier, at `:1656`. Exercised on 2026-05-21:
   49F served 6,788 real accounts, INF was absent, Global published `None`.
2. **CTO's 24/40 corrected to 22/40.** 24 is exactly reproducible as a *weekday* count; the two extra are
   2026-06-19 (Juneteenth) and 2026-07-03 (July 4 observed). Same root produced a second wrong number in the
   brief: "3 of the last 12 trading days" reproduces exactly as 3 of the last 12 *spine rows*; on the
   trading-day axis it is 5 of 12. Both are the 447-spine-vs-429-trading-axis confusion — i.e. W-7 has
   already leaked into load-bearing numbers.
3. **The +408 does not decompose the way the inference predicts:** +442 (cottonwood entering) − 126 (49F −114,
   INF −12) + 92 (composition residual) = +408. The +92 is not a firm at all: +85 SMA preserve, +7
   frontier-stamp roster split. Swept all 407 non-null dates — Global equals Σfirms on 406; 07-22 is the sole
   exception and the sole `frontier_stamp` date.
4. **Cottonwood verdict: CONFIRMED in direction and dominant driver, REFUTED as to magnitude and
   sufficiency.** Grounded on my own decomposition, not the brief.
5. Side finding for W-6(count-reconcile): `json/mdpf/aggregate-aua-timeseries.json` is byte-identical to the
   global key (same ETag) — a duplicate, not a disagreeing artifact.

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| `comp-pipescript io` | `comp-pipescript io dim_mdpf_aggregate_aua_timeseries.py` | PASS — manifest returned | Gave the consumer/feed set (5 monolith silver reads, `account_distribution.json` runtime read). Told me `WRITES: (none detected)` — the served key is written outside the path extractor's view, which is why I resolved the output key from source (`:66-67`, `:568-569`) and then from S3 rather than trusting the manifest's silence. **Gap worth filing: the manifest cannot see this producer's writes.** |
| `comp-to` | `comp-to MDPF_3FIRMS.GC-W1` | OK | race-free per-session TO context |
| `comp-validate` | *not run* | **N/A, stated explicitly** | Per the TO's `<before_commit>`: this is a read-only measurement — no gold script was run and no artifact was produced by me, so there is nothing for `comp-validate` to validate. Recording the reason rather than leaving it blank. |
| `comp-surface-check` | *not run* | **N/A** | I touched no SEV1 surface — deliverable + log + TO status only, zero portal files, zero producer edits. (Noting the 2026-07-24 CLAUDE.md Rule 20 correction: portal-side it is a real blocking gate; workspace-side advisory. Neither applies to a docs-only commit.) |
| direct `s3api get-object` | 4 served keys + `list-objects-v2` | PASS | Explicit-Z metadata throughout; `aws s3 ls` deliberately avoided (local-time rendering would shift date boundaries — the exact hazard this TO is about). |
| `git show <pinned-sha>:<path>` | positive control on 7 cited lines | PASS | 1,926 lines returned (not 0/3) — control against the broken-retrieval-reads-as-absent class before citing any `file:line`. |

## Grounding posture

Every mechanism claim carries `file:line @3efc9dc6d` (the producer's last-touching commit — the TO's cite
`@275b51aee` has since moved, so I re-pinned and said so). Denominators printed on every scan (447 spine /
429 trading days / 407 non-null / 40 null). One claim explicitly left **INFERRED and not claimed**: *why*
49F's legacy import axis omits those 20 dates — the artifact self-labels them "UNCHECKED, not clean" and I
did not open the upstream import.

## Scope discipline

Measurement only. No fix, no design, no code change; read-only on the producer throughout. Obvious fixes went
into §5 notes for W-2/W-3/W-6/W-7 (including the specific lines W-3's writer will need, so it inherits my
reading) rather than into the tree. Picked up no other work — W-1 first and alone, per the GO.

## Next

Reported to CTO (gates W-2/W-3/W-6) and COO in the same window. Lane idle pending routing.
