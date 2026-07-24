# NFRA_TOOLARCH.CANON — CVO~Z re-ground + disposition

**archetype:** VALIDATE
**author:** 3.0.0_SA_CVO~Z · 2026-07-24 · all citations `@ ec07c2ec38` unless noted
**input:** CTO~Z brief (ferried by Andrew, 2026-07-24) over TOs `NFRA_TOOLARCH.CANON` +
`NFRA_TOOLARCH.CANON2` (both `<status>pending</status>`, assigned `0.8.0_AE_CloudComp~D`, lane idle)
**method:** re-ran `tool_source_audit.py` live; re-measured all 5 artifacts; re-grounded each
load-bearing tool AT SOURCE per the brief's own §5 instruction; **exercised** every behavioural
claim (Rule 22a) with positive and negative controls as **separate invocations**.

---

## 0 · Verdict in one line

**The brief's §3 measurements are CONFIRMED. Its §4 headline is REFUTED. And the actual live
failure in this cluster is one the brief does not name: `stitch_graph.json`'s producer has been
hard-failing on a tripped guard, backgrounded and unattended, for 17 days.**

---

## 1 · CONFIRMED from the brief

| Claim | My independent result |
|---|---|
| §3 freshness table | **CONFIRMED**, all five, within 0.1h: graph.json 0.1h · nerves-risk-edges 6.7h · nerves-edges 253.6h · stitch_graph 412.0h · **estate-coverage-resolver 601.0h (25.0d)** |
| §5 "the audit is text-signal based, re-ground each tool" | **CONFIRMED AND VINDICATED** — it caught me a **third** false positive (§3 below). This instruction was the single most valuable line in the brief. |
| bare `pipescript` is resolver-backed AND already carries a loud vintage banner | **CONFIRMED BY EXERCISE.** It prints `SOURCE: estate-coverage-resolver.json SNAPSHOT -- last_review 2026-06-15 (39d old) -- NOT comp-kuzu canonical` plus an explicit VINTAGE WARNING naming the mdpf platinum key. The acute exhibit **already has its mitigation.** |

---

## 2 · REFUTED — §4's headline is false for `comp-pipescript`

> §4: *"Anyone tracing MDPF dataflow through comp-pipescript today is reasoning off a ~25-day-old
> projection and will not be told."*

**This is not what the tool does.** `estate-coverage-resolver.json` is referenced in
`pipeline_cli.py` at exactly **two** lines (`:1183` definition, `:1193` read), inside
`_load_estate_owner_map()` (`:1187`), whose **only** caller is `_estate_oos_guard()` (`:1216`),
whose **only** call sites are `cmd_io` (`:1245`) and `cmd_postdeps` (`:2796`).

It is a **routing guard** — "is this arg mine, or another tool's?" — **not a data source.**
Dataflow, I/O, DAG, chain, feeds and consumers are derived from **script source**.

**Exercised (negative control, separate invocation):**
`comp-pipescript io build_mdpf_wsc_inflection_feeder.py` → rc=0, returned a source-derived manifest
(`READS (1): gold/timeseries/client_performance.parquet [HARDCODED]`). The resolver contributed
nothing to that answer.

**Exercised (positive control, separate invocation):**
`comp-pipescript io bd-client-detail-api` → **rc=2**, `OUT-OF-SCOPE for comp-pipescript -> see
portal-consumer-tools`. The guard is live and loud.

**Consequence:** MDPF dataflow traced through `comp-pipescript` is **not** riding a 25-day
projection. Both stale-directions of the guard are loud-or-fall-through, **not silent-wrong on
dataflow**. The §5 catastrophic-blast-radius concern is real for the `graph.json`/`cli.py` family;
it does **not** transfer to `comp-pipescript`.

---

## 3 · A THIRD false positive — `comp-stitch-refresh`

The brief lists it as a floating-artifact **consumer**. It is the **PRODUCER**:
`.tools/comp-stitch-refresh` header — *"LOCAL producer for the NFRA_GLOBGRPH cross-layer stitch
graph … derive_stitch.py … -> stitch_graph.json"*. Reading/writing that artifact is its job.

**Remove it from the target list.** False positives now **3 of 12** (`comp-manifest-check`,
`comp-graph`, `comp-stitch-refresh`) — the true set is **9**, not 10.

---

## 4 · MECHANISM — §6b answered, and "just regenerate" is a TRAP

`gen-estate-resolver.py` joins two inputs. **Neither is "a refresh path that stopped."**

- **Census half — there was NEVER a refresh path.** `gen-estate-resolver.py:17` hardcodes
  `CENSUS = org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-15/estate_census` — a **date-pinned path into
  a one-time log directory**. Its last commits are the NFRA_PIPESCRIPT close (June 15). It cannot
  advance; regenerating re-joins the same June-15 census.
- **Manifest half — hand-run only, no trigger.** `estate-coverage-manifest.yaml` refreshes when
  someone edits it and manually re-runs the generator. Last such run: `7a914124cf`
  (**2026-06-29 14:40 -0400**) — which is exactly the resolver's mtime. The 25 days are simply
  "nobody has edited the manifest since 06-29."

> ### ⛔ DO NOT RE-RUN `gen-estate-resolver.py` AS A "FIX".
> It would stamp a **new mtime** while the census half stays frozen at 2026-06-15 — **laundering a
> frozen census as fresh** and destroying `last_review: 2026-06-15`, the one field that currently
> tells the truth. **A freshness fix that only moves the clock is a downgrade.** De-pin the census
> input first, or change nothing.

---

## 5 · NEW FINDING (not in the brief) — the live one

**`stitch_graph.json` is 412h old because its producer has been hard-failing for 17 days, silently.**

The hook is wired and **is running** — `.git/hooks/post-commit` → `.tools/git-hooks/stitch-refresh-post-commit.sh`;
its trigger pattern (`:23`) matches `org/modules/graph/`, which **288 commits** have touched since
07-07; `/tmp/stitch-refresh.log` is 517KB, last written **today 14:58**.

Every run ends:

```
GRAIN-SENTINEL: FAIL (6 violation group(s))
  [AC-GRAIN.2] EXTERNAL_ENDPOINT:      count  0 vs baseline  3 = 0.00x
  [AC-GRAIN.2] REACT_QUERY_KEY:        count 85 vs baseline 32 = 2.66x
  [AC-GRAIN.2] SQS_QUEUE:              count 12 vs baseline  4 = 3.00x
  [AC-GRAIN.2] ECS_TASK_DEFINITION:    count  7 vs baseline  2 = 3.50x
  [AC-GRAIN.2] SCHEDULE:               count 10 vs baseline  3 = 3.33x
  [AC-GRAIN.2] IAM_USER:               count  4 vs baseline  1 = 4.00x
ERROR: grain-sentinel FAIL -- refusing to publish a grain-violating stitch (no artifact).
```

**The guard is working exactly as designed** (`exit 2 = refuse to publish`). What failed is the
**notification**: the hook backgrounds the refresh in a detached subshell (`:26`) and `exit 0`s
unconditionally (`:27`), so **no commit has ever surfaced this to anyone.** A correct refusal that
nobody hears is indistinguishable from a pipeline that is fine.

**Two different things are inside that failure, and they must not be triaged together:**
- `EXTERNAL_ENDPOINT: 0 vs 3` — a count collapsing to **ZERO** smells like a broken extractor, not
  drift. **This is the one to look at first.**
- The five high-side trips (2.66x–4.00x) look like **17 days of legitimate estate growth** against
  a stale baseline band.

**This is the genuine instance of Andrew's "artifacts that are NOT refreshed" — and its mechanism is
a tripped guard plus a deaf channel, not a missing refresh path.**

---

## 6 · NEW FINDING — `postdeps` answers an unknown arg with a clean-sounding negative

Exercised, unknown argument:

| call | output | rc |
|---|---|---|
| `comp-pipescript io <unknown>` | `Unknown script: <unknown>` + valid-ID list | **0** |
| `comp-pipescript postdeps <unknown>` | **`No dependencies declared for: <unknown>`** | **0** |

`postdeps` returns an **affirmative-sounding negative** for a name it has never heard of — the
"empty result, not an error" class §5 names, sitting in the subcommand CLAUDE.md Rule 13/§postdeps
requires before any ad-hoc run. `io` is loud in text but **rc=0**, so any gate reading exit codes
sees success.

**Declarative drift:** the comment at `pipeline_cli.py:1219-1221` asserts the fall-through
*"caller's Unknown path is still LOUD."* For `postdeps` that is **not true**.

**Coupling to staleness:** a non-medallion thread created after 2026-06-15 is absent from the
resolver → the guard cannot fire → it lands in exactly this fall-through.

---

## 7 · DISPOSITION (§6c) — 9 true tools

| # | Tool | Backing artifact | Age | Disposition |
|---|---|---|---|---|
| 1-7 | `comp-blast` `comp-trace` `comp-xref` `comp-surface-check` `comp-gitdrill` `comp-diff` `comp-build` | `graph.json` | **0.1h** | **DEFER — architectural, not live risk.** Artifact auto-rebuilds. Any re-point ships **with** the §5 known-present-node adapter mutant. Non-negotiable. |
| 8 | `pipescript` (bare) | `estate-coverage-resolver.json` | 601h | **KEEP + LOUD VINTAGE — already satisfied.** Banner exercised and correct. **No action.** |
| 9 | `comp-pipescript` | same (routing guard only) | 601h | **KEEP, DO NOT RE-POINT.** Resolver is not its answer-source (§2). Separate fix: the `postdeps` unknown-arg fall-through (§6). |
| — | `comp-stitch-refresh` | — | — | **FALSE POSITIVE — producer, not consumer. Remove from list (§3).** |
| — | `estate-coverage-resolver.json` itself | — | 601h | **FREEZE. Do not regenerate** until the census input is de-pinned (§4). |

**Not everything must move.** Two of the three "live risk" items resolve to *already-mitigated* and
*misclassified*. The count went down; the severity moved sideways into §5.

---

## 8 · Recommended routing (CVO~Z verifies; it does not dispatch)

1. **`stitch_graph.json` producer (§5)** — the only item with a live, unattended, 17-day failure.
   Owner: NFRA_GLOBGRPH / `0.8.0_AE_CloudComp`. Start with `EXTERNAL_ENDPOINT 0 vs 3`.
2. **Hook deafness (§5)** — a producer that refuses correctly and tells nobody. Gate candidate.
3. **`postdeps` unknown-arg (§6)** — small, contained, and it is in a Rule-13 pre-run check.
4. **De-pin the census (§4)** — the precondition for the resolver ever being refreshable.
5. **graph.json family** — unchanged, deferred, mutant-gated.

## 9 · What I did NOT do

Did not modify either TO, did not re-point any tool, did not regenerate any artifact, did not touch
`~D`'s deliverables, did not run `gen-estate-resolver.py`. All §1/§2/§5/§6 numbers and behaviours
are measured or exercised by me today at `ec07c2ec38`.

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-grep "estate-coverage-resolver"` | 47 matches / 29 files / 23675 scanned — gave the producer+consumer set that located `gen-estate-resolver.py:17` |
| `comp-pipescript io` (×4, separate invocations) | positive control rc=2 LOUD; negative control rc=0 source-derived; unknown-arg rc=0 — the §2 refutation and the §6 finding |
| `comp-pipescript postdeps` (×1) | unknown-arg → clean-sounding negative at rc=0 (§6) |
| `comp-pipescript --help` | enumerated 13 subcommands; scoped the guard to 2 of them |
| `pipescript --list` | exercised the loud-vintage banner (§1) |
| `tool_source_audit.py` (re-run live) | 12 flagged / denominator 85 — refreshed the list rather than quoting the .md, per §6e |
| `comp-system --check` | STALE→CURRENT at load; **stood down mid-session on Andrew's direct instruction** (see log) |

**Gap found:** `tool_source_audit.py`'s text-signal method is at **3 false positives in 12 (25%)**.
It cannot distinguish a **producer** from a **consumer**, nor a **guard** from a **data source** —
both distinctions were decision-changing here. It is a candidate-generator, not a verdict.
