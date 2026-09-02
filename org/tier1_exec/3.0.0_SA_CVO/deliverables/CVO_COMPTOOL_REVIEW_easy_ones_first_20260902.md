# CVO COMP-TOOL REVIEW — "the easy ones first"

**Andrew-direct 2026-09-02 (CVO terminal), VERBATIM:** *"let's do the easy ones first, comp-kuzu/kuzu-inc
should be consolidated as described. comp-trace i want you to analyze the underlying function and see if it
really is the same as comp-blast, if so it should be retired, but i suspect its a lot more similar to
comp-platinum. comp-similar -dups should be assessed how they differ, if the dups function could be rolled in
through a --dups command or if that is even relevant. comp-pulse we definitely need to review. comp-heat i
want to review, including anything else that is in the deterministic substrate of the daily "Semantic
Evolution Pipeline", i know there are a handful of comp-functions involved there and I want a census and
analyses of those."*

**Seat:** `3.0.0_SA_CVO` (base — Andrew's designated lane for direct comp-tool inquiries, @`98b1a59907`)
**Vintage:** repo HEAD `65213d06c2` · usage window = last 30d of `org/mcp/comp-tool-runs.jsonl` +
`org/mcp/comp-which-rail.log` (both instruments, because each is blind to tools the other logs)
**archetype:** VALIDATE

**Method note that governs every row below:** every "same tool" claim was tested by reading the WRAPPER'S
EXECUTABLE BODY, not its header. Two of my own earlier statements to Andrew failed that test and are
corrected inline (comp-dups; comp-trace).

---

## 1. `comp-kuzu` / `comp-kuzu-inc` — RULED BY ANDREW: consolidate. Evidence says it is already one program.

```
.tools/comp-kuzu       python infra/aws/globgrph/kuzu_cli.py            "$@"
.tools/comp-kuzu-inc   python infra/aws/globgrph/kuzu_cli.py --mode inc "$@"
```
Identical engine, identical env exports, **one literal flag of difference.** `--mode inc` already exists
on the CLI. So the consolidation is not a build — it is **deleting one 17-line wrapper** and redirecting
its callers.

**Callers, last 30d:** 14 runs — `1.0.0_SA_CTO` 7, `4.0.0_SA_CRO` 6, `1.0.0_SA_CTO~B` 1. Three seats,
all exec, all reachable by one broadcast. Every call is a Cypher query; none depends on the wrapper name.

**Owner:** `infra/aws/globgrph/` is `0.8.0_AE_CloudComp`'s. **This seat does not edit code** (charter);
the ruling is recorded here and routes to that seat with this evidence. Zero risk; do it.

---

## 2. `comp-trace` vs `comp-blast` vs `comp-platinum` — trace is a SUBSET of blast. Platinum is unrelated.

**Andrew's suspicion (trace ≈ platinum) is WRONG. His instinct (trace should be retired) is RIGHT — but
into blast, not platinum.**

```
.tools/comp-trace      python org/modules/graph/cli.py  trace  "$@"
.tools/comp-blast      python org/modules/graph/cli.py  blast  "$@"
.tools/comp-platinum   python org/modules/graph/platinum_cli.py    "$@"    <- DIFFERENT ENGINE
```

**trace and blast are two subcommands of ONE CLI over ONE TraceGraph**, and their argparse contracts
(`cli.py:1478-1530`) show blast as a strict superset:

| | `trace` | `blast` |
|---|---|---|
| graph | TraceGraph | TraceGraph (same) |
| `--direction up/down/both` | yes | yes |
| `--depth` | yes | yes |
| `--function` (function grain) | — | yes |
| `--overlap-sweep`, `--compare`, `--grain`, idf weighting | — | yes |
| exit-code contract (rc=4 if zero consumers) | — | yes |
| help text | "Trace data path from a node" | "Show blast radius of a change" |

**Everything trace does, blast does with the same flags.** Blast additionally carries the change-impact
analytics. `cli.py:1113`: *"the default is now BOTH directions. 'What breaks if I change X' is genuinely
bidirectional"* — trace's `--direction both` default IS blast's default.

**comp-platinum is not a graph traversal at all.** Its header: *"Chains together comp-transform +
comp-routes + comp-pipescript to answer: for a given portal page, what platinum/gold files does it need,
what fields does it render, and what gold scripts produce those files."* It is a **composite of three other
comp-tools, scoped to portal-page → gold-script.** Different engine, different question, different corpus.

**Usage 30d:** trace 45 (`0.7.0_AE_CloudOps~F` 18, `0.8.0_AE_CloudComp~D` 14, `3.0.0_SA_CVO` 11) · blast
167 · platinum 7.

**Disposition:** **retire `comp-trace` as a name; `comp-blast <node>` is the replacement, byte-for-byte on
the traversal.** The 45 callers lose nothing. Not touching platinum — it is a different tool.

⚠ **Correction to what I told Andrew earlier:** I said "comp-trace and comp-blast share ONE implementation,
same function." They share one CLI FILE and are DIFFERENT SUBCOMMANDS. The conclusion (retire into blast)
survives; the mechanism I stated did not.

---

## 3. `comp-similar` vs `comp-dups` — DIFFERENT engines, DIFFERENT corpora, both BM25. A `--dups` mode is feasible but the case for it is weak.

⚠ **Correction to what I told Andrew earlier:** I said "comp-dups already forwards to comp-similar" and
called the docstring's declared separation a contradiction. **FALSE — my regex matched the word
`comp-similar` inside the wrapper's docstring.** The executable body:

```
.tools/comp-dups      runpy.run_path( org/modules/graph/debtscan/dup_scan.py )
.tools/comp-similar   python          org/modules/graph/debtscan/comp_similar.py
```
Two engines. The docstring was right and I was wrong. Withdrawn.

**How they differ — same algorithm, different corpus, different question:**

| | `comp-dups` (`dup_scan.py`) | `comp-similar` (`comp_similar.py`) |
|---|---|---|
| corpus | resource **NAMES + file BODIES** | resource **SUMMARIES** (derive-at-scan from comp-kuzu) |
| question | *what a resource IS* — same name / same body | *what a resource DOES* — same job |
| twin type | near-dup files, drifted copies (dogfood: the trading_calendar copies) | functional twin + heat divergence → supersede candidate |
| suppressors | env-triplet, per-agent-tree, service-suffix, cross-firm same-name | firm-cross, env, service; hold-aware |
| authority | CTO arch-gate GO 2026-06-26, 4 conditions | CTO arch-gate ruling 3: *"own tool, not a comp-dups mode"* |
| 30d usage | **0** (all-time 0 in runs.jsonl) | 30 |

**Could dups be a `comp-similar --dups` mode?** Mechanically yes — same BM25 family, same debtscan
package, and `comp-similar` already has a mode dispatcher (`supersede` / `cluster` / query). **But a CTO
arch-gate ruling explicitly decided the opposite** (ruling 3, cited in `comp_similar.py:6`), on the ground
that they read different corpora and answer different questions. Folding them would re-open a ratified
architectural decision to save one wrapper file.

**The more relevant fact is usage: comp-dups has ZERO logged runs, ever.** The question is not "fold or
not" — it is whether the NAME/body-twin question is asked at all. If it is not, retire comp-dups outright;
if it is, the ruling stands and it stays its own tool. **Recommend: retire on usage, do not fold.** Owner
of that call: `1.0.0_SA_CTO` (it is their ruling).

---

## 4. `comp-pulse` — "the most-used tool in the estate" is a HOOK, and agents reach for it 5 times a month.

**What it is** (`org/modules/graph/comp_pulse.py`, 707 lines, NFRA_NERVES L5, Andrew-direct "build
comp-pulse"): it **invents nothing** — it composes four carriers and prints their intersection:

```
  RUNS   org/mcp/comp-tool-runs.jsonl        L2 traffic  (which tools ran, where)
  EDGES  nerves-edges.json                   L3 co-change
  RISK   nerves-risk-edges.json              L3b danger map (holds, incidents)
  rail   org/mcp/comp-which-rail.log         rail signals
```
Headline section = **DANGER × TRAFFIC**: *"a node under a hold or a recorded incident that someone is
walking into right now."* Every number carries vintage + denominator; missing source → UNKNOWN-VINTAGE,
never fabricated. It has a self-test and a danger-map auto-refresh (added after the map sat 207h stale
while the tool honestly printed `!! STALE` on every commit for 8 days and nothing acted).

**The number that reframes it:**
```
  comp-pulse, last 30d:  8,364 runs
     diff           8,359   (100%)   <- the safe-commit RISK-REFLEX hook, every commit
     --help             2
     --self-test        1
     --top              1
     claims             1
```
**8,359 of 8,364 invocations are the pre-commit hook.** Agent-chosen use: **5 in 30 days.** So comp-pulse
is not "the most-used tool" — it is a **commit-time control that nobody reads by hand.** Whether it is
"functioning properly" (Andrew's question) therefore has two answers: as a HOOK it fires reliably (I saw
`[risk-reflex] comp-pulse diff ... REFLEX CLEAN` on all four of my commits today); as a MORNING READ
(*"read this first, each morning"*) it is essentially unused.

**Defect inherited, not its own:** its L2 traffic source is `comp-tool-runs.jsonl` — which **does not
record comp-find or comp-read** (they log to the rail log; measured today: 3,722 + 2,401 rail rows, 0 in
runs.jsonl). So comp-pulse's "traffic" is blind to the two most doctrinally central tools. It does also
read the rail log for `rail_signals`, so partial coverage exists; whether the traffic section merges both
is UNVERIFIED here.

**Disposition:** marquis as a HOOK, not as a tool. Review its danger×traffic output once with a human
reader before deciding whether the morning-read half has any consumer.

---

## 5. `comp-heat` + the Semantic Evolution Pipeline's deterministic substrate — CENSUS

### 5a. What comp-heat is
`.tools/comp-heat` (377 lines, NFRA_HEATMAP_OBJECT, engine `org/modules/heatmap/`): **repo/estate OBJECT
write-freshness + hygiene** — hot/warm/cold per path, ranked cold subtrees (archive candidates), drift.
Derived on demand from git; advisory + read-only; never recommends delete (that is O3, separately
guardrailed). Its own header disambiguates the name that trips people: **`comp-freshness` = DATA-PIPELINE
freshness (S3/DDB); `comp-heat` = REPO object freshness.**

**Usage 30d: 0.** All-time in runs.jsonl: 0. It is consumed as a LIBRARY by `comp-similar`
(`load_heat_live()` → "comp-debris + comp-heat") — so its heat is used, its CLI is not.

### 5b. The census Andrew asked for — and the answer is a zero with a reason

**Runner:** `infra/aws/ec2/estate-report-runner/estate_report_runner.py` (2,333 lines; the S3 copy is
`code/estate_report_runner.py` in `opal-estate-report`).

```
  comp-* tokens in the file           4   (comp-tools, comp-pipescript, comp-heat, comp-freshness)
  imports from org/modules            0
  subprocess calls to a comp-* tool   0   (every subprocess.run is `git ...`)
```

>> **THE DAILY SEMANTIC EVOLUTION PIPELINE INVOKES ZERO COMP-TOOLS.** The three it names live in ONE
   docstring, `:1397-1408`, and that docstring says why: <<

> *"GROUP A -- DECLARED UNAVAILABLE ON THIS HOST, deliberately and loudly. The ladder's instruments
> (comp-heat drift, comp-pipescript deployed, served-artifact md5, comp-freshness) require a checked-out
> workspace with estate tooling; this runner works from a blobless no-checkout clone on a minimal box.
> Running lookalike reimplementations here would be the build-ladder violation ... The group is
> UNMEASURED daily — stated in the report, never silently absent — until a strata producer exists."*

So `_stratum_propagation()` returns `status="INSTRUMENT_UNAVAILABLE"` **every day.** The deterministic
substrate is **git history + the runner's own code**, and the propagation stratum (committed→deployed→
served) is honestly, standingly UNMEASURED. The planned fix it cites: *"the recompile-from-cloud pipeline
substrate (ruling @09355b6d93)."*

**This is the right kind of zero** — declared, reasoned, disclosed in every report. But it means the
"handful of comp-functions involved" Andrew remembers are **designed in and not wired in**, and the daily
report has carried that gap since it shipped.

**Disposition:** comp-heat is a real tool with a real engine and no direct users; its value today is as a
library under comp-similar. Whether it earns a marquis slot depends on whether Group A ever gets a strata
producer — that decision (`@09355b6d93`) is upstream of this tool.

---

## SUMMARY TABLE

| tool | 30d use | finding | disposition | owner of the act |
|---|---|---|---|---|
| `comp-kuzu-inc` | 14 | one flag from `comp-kuzu` | **retire wrapper**, callers → `comp-kuzu --mode inc` | `0.8.0_AE_CloudComp` |
| `comp-trace` | 45 | strict subset of `comp-blast` | **retire name** → `comp-blast` | `0.8.0_AE_CloudComp` |
| `comp-platinum` | 7 | different engine (transform+routes+pipescript) | keep, unrelated to trace | — |
| `comp-dups` | 0 | separate engine by CTO ruling; zero use | **retire on usage**, do not fold | `1.0.0_SA_CTO` |
| `comp-similar` | 30 | D1-D3 fixed today @`b8a73cc064` | keep | — |
| `comp-pulse` | 8,364 (5 by hand) | a commit hook, not a read | marquis **as hook**; review morning-read half | — |
| `comp-heat` | 0 (library use only) | real engine, no CLI users, named-not-wired in daily report | depends on `@09355b6d93` | `0.7.0_AE_CloudOps` |

**Not done here, deliberately:** no wrapper deleted, no code edited, no gate. Every disposition names its
owner. Two of my own earlier claims were wrong and are corrected in §2 and §3.

— 3.0.0_SA_CVO
