# Session log — grain-baseline re-derivation: STOPPED on two disagreements (+ the CTO owned-paths GO)

**archetype:** VALIDATE
**Agent:** `0.8.0_AE_CloudComp` (base) · 2026-07-25

Written **while the work is still blocked**, not after it closes. The IAM_USER finding below currently
exists only in an MCP message, and "the lesson lives only in an inbox message" is the exact failure
this session has been chasing all day. If this lane is killed before CTO~Z rules, the finding survives
here.

## Part 1 — CTO owned-paths GO (closed, ratified)

`1.0.0_SA_CTO` routed two orphaned `infra/aws/lambda` changes to this lane under SoD — the owned-paths
gate blocked them, correctly, and they declined to `--force`.

**Item 1 — `@156b8cf2c`.** MDPF roster row 7(c), pluggable layout resolution. Three files, one commit,
atomic: `partner_roster.json` flips `layouts` from strings to objects and only `mdpf_roster.py` parses
the object form, so a split would put an object-form roster in front of a string-form parser at HEAD.
Original author `0.7.0_AE_CloudOps~B` credited in the body. Re-ran the suite rather than accept it —
**27 passed**, matching CTO's number. Re-running was not doubt: *"27 passed" is a statement about a
tree state, not about a file*, and their run and my commit were separated by a tree other lanes are
actively touching.

**Item 2 — `@d191240715`, and the flagged check FIRED.** CTO could not confirm whether the two
`artifact_sha256` values matched what is deployed, and instructed a HOLD if they did not. They split:

| function | S3 zip sha256 | live `CodeSha256` | proposed | verdict |
|---|---|---|---|---|
| `opal-smartx-ingestion-pipeline` | `voja8Ji…` | `voja8Ji…` | `voja8Ji…` | **LANDED** — deployed |
| `smartx-rest-pull` | `lM6cnuZ…` | `SnPiO8B…` (= HEAD) | `lM6cnuZ…` | **HELD** — never deployed |

Established what the field *was* before comparing: `artifact_sha256` is base64, same encoding as
Lambda's `CodeSha256`. Then went past the encoding match and **downloaded both zips to compute sha256
directly**, because an ETag is an MD5 and on a multipart upload not even that. Both proposed values
equal the **S3 zip's** hash — so whatever produced them recorded the *artifact*, not the *function*.

**Why that is worse than a wrong string:** this file exists for CI drift detection against deployed
state (Rule 4). Writing the S3 hash in would make the detector compare the artifact to itself, match,
and report **no drift** — on the one entry where drift is currently true. Not merely inaccurate: a
detector aimed at itself, failing silent.

Went beyond land-or-hold and **restored** the held entry to its live-verified value, so the map now
matches deployed reality on both entries. CTO **ratified** rather than reversed it, and took the
operational item: `smartx-rest-pull` has run 07-16 code for 9 days while a 07-24 artifact sits
undeployed. They are not deploying it — unknown provenance, owner not live — and are routing it to
Andrew.

## Part 2 — grain-baseline re-derivation: THREE CONFIRM, TWO DISAGREE

CTO~Z's dispatch was explicit: re-derive every number from the live control plane, do not copy the
table, and **"if your number disagrees with mine, YOURS IS THE FINDING — say so and stop."** I stopped.

### Confirmed by independent derivation

| dimension | live | graph | verdict | source |
|---|---|---|---|---|
| `SQS_QUEUE` | 12 | 12 | **MATCHES** | `aws sqs list-queues`, us-east-1 |
| `ECS_TASK_DEFINITION` | 7 | 7 | **MATCHES** | families **and** revisions both 7 — checked both semantics because they can differ; here they do not |
| `SCHEDULE` | 10 | 10 | **MATCHES** | `aws scheduler list-schedules` |

CTO~Z's reading holds on these: the graph is right and the baseline is stale.

### DISAGREEMENT 1 — `IAM_USER`: 4 is not an under-read of 6

The dispatch instructed the `verified_reason` to state "explicitly that 4 is a known under-read of a
live 6." **It is not an under-read. It is a different population.**

```
graph (4):  Andrew_Berman, github-actions-portal, root, token.actions.githubusercontent.com
live  (6):  Andrew_Berman, Andrew_Berman_1, github-actions-portal, opal-portal-dashboard,
            Opal_Terminal, patricia@thewhitelabelcreative.com

OVERLAP                          2
REAL USERS MISSING FROM GRAPH    4
GRAPH NODES THAT ARE NOT USERS   2
```

Both non-users verified live, not inferred:
- `aws iam get-user --user-name root` → **`NoSuchEntity`** — the account root is not an IAM user.
- `aws iam list-open-id-connect-providers` → `arn:aws:iam::313476888478:oidc-provider/token.actions.githubusercontent.com`
  — an **OIDC provider** typed as a user.

**Why I refused to write it:** the IAM_USER split exists precisely so we do not certify a value known
to be wrong. Writing "a known under-read of a live 6" encodes a *false characterization* — the graph
did not find fewer of the right things, it found 2 right and 2 of the wrong kind. That is the same
hazard the dispatch was guarding against, one level deeper than it anticipated: **4-vs-6 looks like an
under-count and the arithmetic works, but the sets barely intersect.** Item (b) is also bigger than
stated — 4 missing users *and* 2 type-confusions, which are different extractor defects with different
fixes.

**Enumerate what the number is OF before explaining why it differs** — a rigorous instrument on the
wrong population survives review because the digits are plausible.

### DISAGREEMENT 2 — `REACT_QUERY_KEY`: 57 vs 85, and a naming fork underneath

The canonical graph's node_type is **`ReactQueryKey`** (57), not `REACT_QUERY_KEY` (which returns **no
rows**). The baseline key is `REACT_QUERY_KEY` (32). The dispatch has graph = 85.

I do **not** claim 85 is wrong: the baseline's own `source` says `kuzu_stitch_db unioned (97-route)`
and I queried the canonical comp-kuzu DB. Those may be different populations, which would explain the
gap with neither party mistaken. **I could not reconcile them, so I reported rather than picking one.**

**The part needing a ruling before any number is baselined:** `grain_sentinel.check_magnitude`
iterates the *baseline's* keys and looks up that exact key in the node counts
(`grain_sentinel.py:127`; `:120-121` skips classes absent from the baseline). So if the node stream it
is fed uses `ReactQueryKey` while the baseline says `REACT_QUERY_KEY`, the lookup yields 0, ratio
`0.00x`, and it renders **byte-identical to a real collapse**. I have *not* established which naming
the sentinel's actual input carries — that needs the stitch's node stream, not the canonical DB — so
this is flagged as a fork to resolve, **not** a live defect I have proven.

### Not done, deliberately

Stopped before grounding `REACT_QUERY_KEY` with `.tools/comp-cache`: the naming fork makes the target
ambiguous, and counting query-key literals in portal source is a *third* population again. Producing a
third number without knowing which one the baseline certifies would add noise, not evidence.

**Nothing written to `grain_baseline.json`** (exec-locked; CTO~Z lands it). No `verified_reason` drafted.

## Blockers

**BLOCKED-ON-RULING (CTO~Z):** which population is authoritative for `REACT_QUERY_KEY`, and how to
characterize `IAM_USER` now that 4 is known not to be a subset of 6. Recommendation offered, not taken:
recalibrate the three verified-matching dimensions now (clean, and unblocks most of the sentinel), hold
the other two.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `.tools/comp-kuzu` | Derive graph counts for the 5 dimensions independently | 4 rows; `REACT_QUERY_KEY` absent → led to the `ReactQueryKey` naming discovery |
| `.tools/comp-grep` | Locate the sentinel / baseline readers | 0 matches for `grain_baseline` — **and that was correct**, cross-checked against native grep, which agreed |
| `.tools/commit-gate.sh` | Rule 14 on item-1 `.py` files | clean, 2 files |
| raw `aws` (rail-checked) | Live control-plane ground truth | comp-aws models DESIRED/TF only; the dispatch required LIVE, so raw was the correct instrument |

**A control note on my own method:** my first "positive control" for `comp-grep` was invalid — I
searched for a string I *assumed* was in file contents rather than one I *knew* was. It returned 0 and
I nearly read that as a broken tool. What actually resolved it was a **second, independent instrument**
(native grep) agreeing. A control you picked badly is not a control; a second instrument is.

## Files Modified

- `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/grain_baseline_rederivation_stopped.md` (this log)

Commits this segment: `156b8cf2c`, `d191240715` (both CTO-validated).

---

## RESOLUTION (~1846Z) — GO on all five, built, exercised, **sentinel PASSES and the stitch PUBLISHED**

CTO~Z ruled on both disagreements (183918Z).

**IAM_USER: my correction UPHELD, their characterization WITHDRAWN.** Their words: *"I compared
CARDINALITIES and concluded 'under-count.' A count comparison cannot detect a population mismatch — and
the arithmetic looked plausible the whole way."* Item (b) resized to what it is: 4 missing users **and**
2 type-confusions, different defects with different fixes.

**Naming fork RESOLVED, and my hypothesis did NOT fire.** The sentinel is fed the **stitch stream**,
which uses SCREAMING_SNAKE and matches the baseline keys. My 57 was the canonical DB — genuinely a
different store, exactly as I suspected but could not resolve. **CTO~Z's 85 stands, and the published
artifact confirms it at exactly 85.** Reporting both and refusing to pick was right; picking would have
been wrong either way.

### Built and exercised

Baseline written with 5 `per_class` updates + 5 recertification entries, each `verified_reason` carrying
live source + count + date + **MATCHES-live vs APPROACHES-live**, plus a `_naming_fragility_note`
recording the dormant lookup hazard where the next person changing a node_type will see it. IAM_USER's
reason names the composition and never uses the phrase "under-read."

```
GRAIN-SENTINEL: PASS (0 identity-format + 0 magnitude violations)
OK: wrote infra/aws/globgrph/stitch_graph.json      UNIONED nodes = 22355, edges = 43633
```

| | before | after |
|---|---|---|
| mtime | 2026-07-07T15:45:33Z | **2026-07-25T18:44:34Z** |
| size / edges | 3,170,624 B / 5,651 | 25,489,187 B / 43,633 |

All five confirmed **in the published artifact**: SQS 12 · ECS 7 · SCHEDULE 10 · RQK 85 · IAM_USER 4.

### FINDING — the acceptance criterion was always satisfied

*"`stitch_graph.json` EXISTS"* could never discriminate. **The file existed throughout the 17-day
block** — at `infra/aws/globgrph/`, a **third root** outside the two COO~Z's absence finding was
honestly bounded to; 18d 2h stale; and **gitignored**, so `git log` shows nothing for it and a
git-based check reads as "never existed."

**An existence test would have returned GREEN for the entire outage.** It cannot distinguish
*published* from *an 18-day-old corpse*. I used **mtime advance** instead and kept the pre/post values
so the claim is checkable. Same class as the fails-open harness earlier today: *a check whose passing
state is indistinguishable from the failure it exists to catch.*

### FINDING — `derive_stitch` still exits 1 on a SEPARATE, previously-masked defect

`DERIVE_RC=1` — `ERROR: genuine (non-wildcard) dangling edges = 8`. The grain block was hiding it.
Order is: dangling check → ERROR (rc set) → GRAIN-SENTINEL PASS → artifact **written**. So **the
artifact publishes and the producer still reports failure**; any consumer keying on exit code still
sees a failing stitch, and COO~Z's "hook fires and still hard-fails" chain is only half resolved.

Offered, not adjudicated: several dangling targets are AWS-**managed** resources with an **empty account
field** (`arn:aws:ssm:us-east-1::document/AWS-RunPowerShellScript`) — externals our extractor would
never emit as nodes, plausibly needing the same treatment the code already gives wildcards rather than
being 8 real defects. Two ELB `IN_SUBNET` edges look like a different and more plausibly real gap.

### On my own claim, corrected by CTO~Z

I wrote that recalibrating the three clean dimensions *"unblocks most of the sentinel."* It would have
unblocked **nothing** — the sentinel refuses on any violation, so 5 → 2 still yields no artifact. The
win would have been *isolation*, not progress. "Most" invites someone to expect a file that will not
appear.

I also checked CTO~Z's IAM rationale in both directions rather than accepting it: baselining the live 6
would **also** pass today (4/6 = 0.67x, in band), so band arithmetic does not discriminate between 4 and
6. Their ruling stands on the stronger reason — a baseline certifies *what a healthy graph produces*,
and that number is not yet known for this class.

## Blockers

**`grain_baseline.json` is ON DISK, UNCOMMITTED** — exec-locked, CTO~Z lands it. Flagged to them the
same turn it was written, deliberately: an exec-locked artifact sitting on disk unannounced is precisely
the orphan shape cleared earlier today, and the mitigation is that its owner knows within seconds rather
than days.

Extractor defects (a) and (b) not yet filed as a formal item — awaiting CTO~Z on where they belong.
