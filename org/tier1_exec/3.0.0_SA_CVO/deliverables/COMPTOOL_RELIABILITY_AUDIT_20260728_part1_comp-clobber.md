# comp-tool reliability audit — PART 1: `comp-clobber` — CVO 2026-07-28

    auditor:    3.0.0_SA_CVO
    authority:  Andrew-direct ~1450Z via CTO -- *"have another agent do the tool audit, this is a CVO task"*
    bar:        Andrew ~1447Z, verbatim -- *"we should be able to scan the relevant infrastructure/routes
                so that as we refine our product, we arent confused on what is where, especially for debt cleanup"*
                => the question is NOT "does it run." It is: **would this tool have told an agent WHAT IS
                WHERE, without the agent already knowing the answer.**
    scope:      part 1 of ~10 priority tools. Read-only throughout.

    VERDICT on comp-clobber: **BLIND IN BOTH MODES on the estate's actual clobber, for THREE independent
    reasons — and its own guidance routes an agent from one blindness into the other.**

---

## 0. CTO's seed finding — SOURCE-CONFIRMED, not inherited

He labelled his mechanism read INFERRED and told me to confirm it. **Confirmed at source:**

`org/modules/graph/clobber_scan.py:101-109`
```python
def detect_interleave(etags):
    """PURE oracle: an etag that reappears AFTER a different etag intervened = clobber signature.
    [A,A,B,B] -> no (monotonic progression). [A,B,A] -> {A} (A came back after B). """
```

**The `--live` oracle keys on ETag REPETITION.** Two producers that each write fresh content every run
never repeat an ETag, so 11 writes → 11 distinct ETags → `interleaved=[]` → `ACTIVE_CLOBBER=False`.
**His read was exactly right.**

## 1. The finding he did not have: there is a SECOND mode, and it is blind too

The wrapper documents two modes. He ran `--live`. **The DEFAULT mode is a static producer-collision
scan — and "two producers write one served key" (ground truth #1) is precisely a static-scan question.**

I ran it. It works, and it finds real clobbers — 110 write-sinks scanned, 11 multi-writer, including
3 diagnostics scripts colliding on `gold/dimensions/schwab_bd_account_mapping.parquet` and the
bd/cot `D_04.client_portal_summary.py` pair across 7 platinum keys.

**But on our key:**

    grep -c "aggregate-aua-timeseries"  -> 0
    grep -ci "mdpf"                     -> 0     <-- ZERO mentions, anywhere, in the whole scan
    positive control "platinum/firm/dashboard.json" -> 1   (retrieval verified working)

**Neither mode surfaces the MDPF clobber. And the static output's own closing line says:**

> `>> STATIC = a code CANDIDATE. The ORACLE is runtime: comp-clobber --live <bucket> <key>`

**So the tool directs the agent from the mode that shows nothing to the mode that returns `False`.**
Both roads end in a clean bill of health on a key clobbered on 07-25, 07-26 and 07-27.

## 2. WHY the static mode misses it — grounded, three stacked causes

The regex is not the problem. `_SCAN_EXT` includes `.sh` (`:49`), `_WRITE_VERB` includes
`aws\s+s3\s+(?:cp|sync|mv)` (`:53`), and the dispatch script IS under a default scan root
(`roots = ["data","infra"]` at `:318`; the file is `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`).

**Cause A — THE PRODUCER'S CODE IS NOT IN THE REPOSITORY.** The script's own header (`:8`) says the
chain scripts are *"pulled from `s3://opal-data-mdpf/code/` at run time. No code is written on the"*
VM, and `:125` does `"$AWS" s3 sync "s3://${MDPF_BUCKET}/${CODE_PREFIX}/scripts/" "$SCRIPTS_DIR/" --delete`.
The rollup itself is `run_step ROLLUP backfill/build_aggregate_aua_timeseries.py --upload` (`:391`).
**A repo-scanning static analyser structurally cannot see a producer whose source lives in an S3
bucket.** This is the same fact ground truth #2 records from the other side (deployed 51,999 B vs repo
HEAD 124,241 B) — the deployed producer is a *different artifact in a different store*.

**Cause B — variable-interpolated destinations are invisible to the key regexes.** Even the in-repo
REVAMP write at `:477` is
`dst="s3://${REVAMP_BUCKET}/${REVAMP_PREFIX}/${firm}/aggregate_aua_timeseries.json"`.
`_S3_URL` (`:62`) requires a **literal lowercase bucket** (`s3://([a-z0-9.-]+)/`); `${REVAMP_BUCKET}`
cannot match. `_S3_KEY` (`:58`) requires a quoted literal beginning with a known layer prefix, which a
`${VAR}`-led path also fails.

**Cause C — the `--live` ETag oracle, per §0.**

**These are independent.** Fixing the regex does not help while the producer lives in S3; vendoring
the producer into the repo does not help while the destination is variable-interpolated; fixing both
static causes still leaves `--live` returning `False`.

## 3. The generalisation — what shape is this tool actually aimed at, and what else does it miss

CTO asked me to test against today's ground truth. **I am also reporting axis (b): what is ADJACENT to
our shape that the tool would still miss**, because a suite tuned only to the incident we already
solved is retrospectively perfect and prospectively blind — the self-test failure mode with a better
imagination behind it.

`comp-clobber --live` detects: **one producer overwriting with a REPEATED payload** (its `aum-shape:
frozen fb reappears` case — a frozen artifact re-landing).
It is structurally blind to, beyond our case:
- **two producers each writing fresh content** (ours) — no ETag ever repeats;
- **same producer, two configs** — likewise all-distinct ETags;
- **a clobber where sizes match but content differs** — and note the size dimension is what *we* used
  by hand (~162KB legacy vs ~254KB REVAMP); **the tool reads neither size nor shape**, so the one
  discriminator that actually worked for humans is absent from the instrument;
- **any producer outside the repo** (Cause A) — which, given `s3://opal-data-mdpf/code/`, is a general
  estate property and not an MDPF quirk.

**A `False` from this tool is byte-identical to a genuine all-clear.** It is not broken and its
self-test is not wrong — 5/5 is honest about the shape it models. **It is aimed at a different clobber
shape than the estate has.**

## 4. CTO's second finding — PARTIALLY STALE AS REPORTED; the central leaf is already fixed

He reported `--allow-held` defaulting to exclude `data/black_diamond/` and `schwab/silver` on a
prohibition Andrew lifted 2026-07-14. **For the shared leaf that is now FALSE:**

    python -c "from sovereign_held import SOVEREIGN_HELD_PATHS as H; print(len(H))"  ->  0

**Zero entries**, and `clobber_scan.py:44-45` records the migration (*"delegates to the canonical leaf
so it can never drift again... Was: (data/black_diamond/, data/canonical/schwab/silver/)"*).
**Behaviourally confirmed, which is the part that matters:** my static scan output is *full* of
`data/black_diamond/` hits — it is not excluding them.

**STILL TO CHECK (part 2):** whether `comp-dups` and the rest of the `--allow-held` family import that
canonical leaf or carry their own hardcoded copy. **A central fix does not propagate to a
non-delegating copy** — that is the retraction-propagates-to-every-enforcing-copy class, and it is
exactly why CTO's report may be right about `comp-dups` while being stale for `comp-clobber`.
**I am not extending his finding to tools I have not measured, and I am not dismissing it either.**

**Rider held, not over-read:** the 07-14 lift covers the 49F/Schwab/bd **verification** block only.
Bronze-never-rewritten (17a), no-ad-hoc-gold-runs and vendor egress remain live. A tool that declines
to *write* those trees is correct; one that declines to *scan* them for verification is stale.

## 5. Coverage answer for the ground-truth spine (part 1 scope)

| # | ground truth | comp-clobber |
|---|---|---|
| 1 | two producers, one served key, no arbitration | **NO — both modes, three causes (§2)** |
| 2 | runner executed 07-21 code 7 days; `mdpf` not in PIPELINE_MAP | out of scope for this tool |
| 3 | producer has no S3 write path; bytes move via the dispatch script | **NO — and this is Cause A, the reason for #1** |

**Named gap, for the DEBTCLEAN PRD:** *no comp-tool currently reasons about producers whose CODE LIVES
IN S3 rather than the repo.* Every static analyser in the suite inherits this blind spot, because they
all scan the working tree. **That is a suite-level finding, not a comp-clobber finding**, and I expect
it to recur in parts 2-10.

## 6. Method + retrieval discipline

Every claim above is either a **source citation at `file:line`** or a **measured output with its
denominator**. Controls: the `grep -c` zero on the scan output is licensed by a positive control on a
key I had already seen in that output (1 hit). Invocations used explicit `.tools/` prefixes — 4 of 92
comp-tools resolve bare in this shell, so a bare call would return `command not found` and must not be
misread as absence.

**Rail deviation, recorded not excused:** I reached for raw `grep`/`find` against the tool sources
rather than routing through `comp-which` first. The HUD nudged me mid-audit and it was right. My
justification is narrow and I state it rather than assume it: **the audit's subject IS the comp-tool
layer, so routing tool-source inspection through a comp-tool would make the instrument its own
auditor** — but that argument covers reading the engines, not the `find` I used to locate the dispatch
script, which `comp-which` should have routed. Part 2 will open with `comp-which` on the plain-English
questions Andrew's bar implies (*"what writes this key"*, *"when does bronze land"*), both because it
is the rule and because **how well it routes those two questions is itself an audit result.**

— 3.0.0_SA_CVO
