# comp-kuzu n.id -> n.node_id: the program's FIRST end-to-end residue-clearing cycle — PENDING-VERIFY

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **status:** DELIVERED + COMMITTED, closure claim
**PENDING-VERIFY** (CVO~Z verifies the sensor + closure pair as one story, per dispatch)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T112804Z · **scope ruling:** 113225Z (8-site fix ENDORSED + the
run_validation verdict-delta limb added)
**instrument:** ~E's item-1b sensor, used as-committed (`d2f29501c5`) — no modification, no flags added.

> **Sensor detects → fix lands → sensor confirms closure: the self-healing delta loop Andrew chartered,
> demonstrated at unit scale. PENDING-VERIFY.**

---

## 1 · Denominator (the dispatch-mandated sweep)

**8 CloudNode-bound `.id` sites across 3 of the sensor's 7 LAYER_FILES** — the pinned 2 undercounted,
and my own first grep (`n.id`) missed `a.id`/`b.id`/`p.id`; the real predicate is *any bound-var* `.id`
(predicate-vs-token, self-caught, disclosed):

| # | Site | Class |
|---|---|---|
| 1 | `.tools/comp-kuzu:3` (wrapper usage comment) | TEACHING (pinned) |
| 2 | `kuzu_cli.py:6` (module docstring example) | TEACHING (new) |
| 3 | `kuzu_cli.py:125` (schema help, `n.id, n.name`) | TEACHING (pinned) |
| 4 | `kuzu_cli.py:127` (schema help, `a.id, b.id`) | TEACHING (new) |
| 5 | `kuzu_cli.py:129` (schema help **DO:** exemplar, `a.id, b.id`) | TEACHING (new) |
| 6 | `kuzu_load.py:190` (`run_validation` Q1, `n.id, m.id`) | **EXECUTED** |
| 7 | `kuzu_load.py:211` (`run_validation` Q2, `n.id, n.arn`) | **EXECUTED** |
| 8 | `kuzu_load.py:222` (`run_validation` Q2, `p.id`) | **EXECUTED** |

Residual sweep post-fix: the same bound-var-`.id` grep over all 7 layer files = **0 hits**, positive-
controlled (the identical grep on HEAD's `kuzu_load.py` = 3 hits). `extract_portal_stitch.py:124`
excluded with reason: Python attribute access on a Node object, not Cypher teaching, and not in the
sensor's LAYER_FILES.

## 2 · The scope fork, surfaced mid-execution and ruled

Sites 6–8 are `conn.execute()` calls, not prose. Fixing only teaching sites could never close the
sensor's orphan (the sensor dedupes every ref into the single element `column:CloudNode.id`; any
surviving ref keeps orphan=1). Surfaced with disposition, ENDORSED by CTO~Z 113225Z: the executed sites
were **exercised broken-live before fixing** (`Binder exception: Cannot find property id for n`,
verbatim, read-only via ~E's direct pattern) — dead-on-arrival code has no behavior to change; the
"no behavior change" guard protects the DB, the engine, and working logic, all untouched.

## 3 · run_validation revival — the added acceptance limb, verdicts disclosed honestly

**(a) How the Binder exceptions were handled today: PROPAGATING, not swallowed** (measured: no handler
on the `run_validation` path — the `:171` try/except belongs to `_load_edges`; `validate` **defaults
True** with a `--no-validate` opt-out, `kuzu_load.py:296-298`). So any bare full-load since the schema
rename would have crashed loudly post-load. The absence of such crash reports suggests the
full-load+validate path has simply not been run since the rename (consistent with the canonical DB
living on the incremental-refresh path) — that last clause is INFERRED, not measured.

**(b) First-ever post-fix execution** (read-only connection, live canonical DB):
- **Q1 CLEAN with real numbers:** 342 Lambda→S3 READS edges (5 shown, all real ARNs).
- **Q2 IS A FINDING, not smoothed:** `34 EC2 total / 33 with profile / 1 without` — instance
  `i-06376c11d8b3c3443` carries **no IAM instance profile**. The check was blind; now it sees, and what
  it sees is one WARN. Routed to CTO~Z for ownership (0.7.0 CloudOps territory), not chased by this lane.

## 4 · Closure by sensor — the actual accounting, not the inherited arithmetic

| | pre-fix (~E, committed JSON) | post-fix (this run) |
|---|---|---|
| Verdict | VERDICT rc=2 | **CLEAN rc=0** |
| Accounting | N=13 = covered 11 + member 1 + orphan 1 | **N=12 = covered 12 + member 0 + orphan 0** |
| doc_only | N/A-DECLARED by shape | unchanged |

The dispatch predicted `N=13 = 12+1+0` and said to read the real structure instead — the real structure
is better: **`column:CloudNode.id` left the assumed plane entirely** (all 8 refs corrected → N 13→12,
orphan→0), and **`column:CloudNode.node_id` moved member→covered** (pre-fix evidence line: "declared in
loader DDL, present live, never query-referenced" — the corrected literals now reference it, so the
member cell emptied too). Every cell movement is explained by the fix; nothing else moved.

**One discrepancy surfaced in reconciling (small, ~E's record):** ~E's memo §3 prose names the member
as `CloudNode.props`; ~E's own committed report JSON names it `column:CloudNode.node_id`. The artifact
is the authority, and the post-fix movement corroborates it (a `props` member would not have moved on
this fix). One-line memo correction for ~E/CTO~Z, not adjudicated here.

Exercised repro (acceptance a): the corrected canonical example returns live rows read-only
(2 LAMBDA node_ids); the corrected Q1 form returns 5 rows; the two-var help form returns rows. Gate
clean on both `.py` files; zero non-teaching/non-broken lines touched.

## 5 · For CVO~Z (verifies sensor + closure as one story)

- Closure re-derivation is ONE command, ~E's sensor as-committed, no flags: it prints the accounting
  line and rc. Pre-fix state is pinned in ~E's committed JSON.
- The scope-extension grounding (broken-live) is re-derivable read-only: run the HEAD version of the
  `:190` query text against the canonical DB → Binder exception; the working-tree version → 5 rows.
- The Q2 WARN (`i-06376c11d8b3c3443`, no instance profile) is one query to re-derive; whether it is
  materially wrong is explicitly NOT this lane's claim.
