# bd-plane six-week delta REVIEW -- `cot_bronze_ingest.py` (shared, Model-B)

**TO:** `ADHOC.bd-plane-sixweek-delta-review` · **Author:** `0.7.0_AE_CloudOps~B` · **2026-08-04**
**To:** `1.0.0_SA_CTO` (rulings) · `0.4.0_DS_ClientPlatform` (recommended deploy seat) · `2.0.0_SA_COO` (routes)
**Mode:** READ-ONLY. **Zero bd-plane writes from this seat.** The deploy is a DS lane per Rule 13.

**VERDICT: BOTH CHANGES `SAFE-AS-IS` ON bd. ZERO `EXCLUDE-CANDIDATE`. ZERO `NEEDS-BD-CONFIG`.
DEPLOY RECOMMENDED** -- as a deliberate reviewed act, never a sync (CTO d-2 232535Z).

---

## PHASE 1 -- THE PINNED ARTIFACT

A review of an unpinned artifact is a review of nothing. What was reviewed:

```
DEPLOYED (bd)   s3://opal-data-bd/code/bronze/cot_bronze_ingest.py
                Size          56,885 B
                LastModified  2026-07-09 09:11:54 GMT
                ETag          fa9fd5a9652e7c7aea60776ed469c773
                sha256        3db53a8b60eb53c65c4272da789e99d9f1edfda4e6f44b3bd5d90a897a0e2123

REPO HEAD       data/cot/scripts/bronze/cot_bronze_ingest.py
                Size          73,220 B
                sha256        09e47da2c94d0a170c806eb804e7faf03436972270f51fe7dc074cb53f76d884

DELTA           +16,335 B
```

**FORK POINT IDENTIFIED EXACTLY, not assumed:** the deployed bd bytes are **byte-identical to
repo commit `4632383568`** (2026-07-09 05:11:18 -0400, `0.6.0_AE_PartnerETL`). S3
`LastModified` 09:11:54 GMT = 05:11:54 EDT -- **deployed 36 seconds after its commit.** The bd
plane is not drifted-from-nothing; it is cleanly pinned at a known commit.

*(Method: hashed `git show <c>:<path>` for every commit touching the source since 2026-06-25 and
matched against the deployed sha256. The fork point is measured, not inferred from dates.)*

---

## PHASE 2 -- THE CHANGE LEDGER

**The window `4632383568..HEAD` contains exactly TWO commits touching this file. There is no
"everything else" bucket because the residual is EMPTY** -- the TO named both, and both are
accounted for.

### CHANGE 1 -- `545bde4e9a` (2026-07-24, `0.4.0_DS_ClientPlatform`)
*"generalize the retry-net from holdings-only to ALL SNAPSHOT_TABLES + 3-state heal-forward predicate"*
`+301 / -35` lines.

**bd impact: NONE. The code is UNREACHABLE from the 49f runner's call path.**

| Evidence | Cite |
|---|---|
| `backfill_snapshot_net` is reachable only behind a CLI flag | `cot_bronze_ingest.py:1134` (`dest="backfill_snapshot_net"`), `:1157` (`if getattr(args, ...)`), `:1166` |
| The 49f runner **imports the script as a MODULE** and never parses argv | `bd-49f-runner/lambda_function.py:45,75` (`importlib.util.spec_from_file_location`) |
| The 49f runner invokes only its four REST tables | `:64` `BD_REST_TABLES = ("transactions","allocations","realized","unrealized")`, `:121-122` |
| **Zero references** to `backfill_snapshot_net` / `retry_net` / `backfill` in the 49f runner | grep = 0 hits |

**POSITIVE CONTROL ON THAT ZERO:** the same grep over the same file returns **2 hits** for
`BD_SNAPSHOT_ASOF_LAG_BDAYS` -- so the container demonstrably holds the terms being counted, and
the zero is a real absence rather than a broken pattern.

**VERDICT: `SAFE-AS-IS`.** On bd this change is inert code. It activates only on the cot plane's
CLI invocation. Deploying it changes no 49f runner behavior.

### CHANGE 2 -- `bf4c0aabbe` (2026-08-03, `0.4.0_DS_ClientPlatform`)
*"LAG=1 parity for cot snapshot tables -- `BD_SNAPSHOT_ASOF_LAG_BDAYS` default 0 -> 1;
no-op for 49f (env-explicit per bd-49f-interim.tf:310)"*

**The commit's own no-op claim was VERIFIED AT SOURCE, not accepted** (TO: *"env-explicit guards
are the pattern to verify, not assume"*):

```
script  :100   BD_SNAPSHOT_ASOF_LAG_BDAYS = int(os.environ.get("BD_SNAPSHOT_ASOF_LAG_BDAYS","1") or "1")
                                                                                          ^^^ default now 1
infra/aws/terraform/bd-pipeline/bd-49f-interim.tf:310
               BD_SNAPSHOT_ASOF_LAG_BDAYS = "1"        <-- 49f sets it EXPLICITLY
```

49f's env value (`"1"`) and the new default (`"1"`) are **the same value**, so the default flip
cannot move 49f in either direction. Consumption is at `:301-302`, gated on
`> 0 and table in SNAPSHOT_TABLES`.

**VERDICT: `SAFE-AS-IS`.** The claim holds. **And note it holds because 49f is env-explicit, not
because the values coincide by luck** -- if the default flipped again tomorrow, 49f is still
pinned.

---

## FINDINGS (routed to CTO -- neither blocks the deploy)

### F1 -- DECLARATIVE DRIFT: two Terraform comments now assert a default that no longer exists

`bf4c0aabbe` moved the default `0 -> 1` and **did not update the two comments that document it.**

| File | Text | Status |
|---|---|---|
| `infra/aws/terraform/bd-pipeline/bd-49f-interim.tf:308-309` | *"default 0 = OFF = byte-identical prior behaviour, cot never sets it"* | **FALSE** -- default is 1 |
| `infra/aws/terraform/cot-pipeline/schedule-et.tf:18` | *"cot runs with `BD_SNAPSHOT_ASOF_LAG_BDAYS` unset (=0), so every table's window ends on run_date = today-UTC"* | **FALSE** -- unset now means 1 |

The second is the load-bearing one: **that comment carries an as-of-window derivation for the cot
schedule anchor, and its premise is now inverted.** A future scheduling decision reasoning from it
would compute the wrong window. The behavior change was intended (LAG=1 for cot was the point of
the commit); **the documentation describing the old behavior is what drifted.** This is infra
surface = AE lane; I did not edit it under a review-only TO.

### F2 -- `comp-pipescript deployed` IS STRUCTURALLY BLIND TO MODEL-B CROSS-TREE DEPLOYMENT

Run per the TO's mandate, the tool returned:

```
DEPLOYED STATUS [cot-gold]: local repo vs s3://opal-data-cot/code/{gold,silver,bronze}/
  [BRONZE] cot_bronze_ingest.py    MATCH
  Summary: 1 MATCH, 0 STALE, ... 0 UNCOVERED
  All checked scripts are up-to-date on S3.
```

**It checked only the cot tree and declared "all up-to-date" while the bd copy of the same file
was six weeks stale** -- the exact divergence this review exists for. The tool scopes by the
script's *repo home* (`data/cot/...` -> cot), so a **shared script deployed into a second firm's
bucket is outside its coverage entirely** -- and `0 UNCOVERED` is itself scoped to the cot tree,
so the counter that should have flagged the gap reports zero.

>> **A GREEN VERDICT WHOSE SCOPE EXCLUDES THE DEFECT.** Model-B one-source means a script has
**more deployment targets than trees**, and this instrument models one target per script. Nobody
running it on this file would learn the bd copy exists, let alone that it was stale. <<

Not a blocker; a coverage gap in the instrument that would otherwise be the natural detector for
the next occurrence of exactly this divergence.

---

## PHASE 3 -- THE HANDOFF (part of this TO, not after it)

**THE DEPLOY IS NOT THIS SEAT'S.** Rule 13 puts `data/*/scripts/bronze/*.py` in the DS lane and it
is pre-push enforced. CTO rider 2 (000023Z): *"do not let the review seat carry the deploy on
momentum."* **Zero bd-plane writes were made from this seat and none will be.**

**RECOMMENDED SEAT: `0.4.0_DS_ClientPlatform`.** They authored **both** commits in the window
(`545bde4e9a`, `bf4c0aabbe`) and hold the cot-plane context; the divergence was their own
232021Z item-4 finding. `0.2.0_DS` holds mdpf-chain context, which this file does not touch.

**RECOMMENDED DEPLOY FORM -- deliberate act, never a sync:**

1. Deploy **repo HEAD** `data/cot/scripts/bronze/cot_bronze_ingest.py`
   (sha256 `09e47da2c94d0a170c806eb804e7faf03436972270f51fe7dc074cb53f76d884`)
   to `s3://opal-data-bd/code/bronze/cot_bronze_ingest.py`.
2. **Pre-flight assert** the target still carries sha256 `3db53a8b…` / ETag
   `fa9fd5a9652e7c7aea60776ed469c773`. **If it does not, STOP** -- something moved since this
   review and the reviewed delta is no longer the deployed delta.
3. **What the deploy changes on bd, stated in advance:** nothing at runtime. Change 1 is
   CLI-unreachable from the runner; change 2 is value-identical under 49f's explicit env. **If the
   next 49f cycle behaves differently, that is a finding, not an expected outcome** -- and it means
   this review was wrong.
4. Acceptance evidence is the bd runner's next **scheduled** cycle post-deploy -- **the DS TO's, not
   this one's.** An ad-hoc run is a QA instrument, never production evidence.

**The hash pinning is what makes the handoff sound: the DS seat deploys the artifact THIS review
covered, by construction, rather than whatever HEAD happens to be when they execute.**

---

## Compiler Tools

| Tool | Command | Observed | vs `<expect>` |
|---|---|---|---|
| `comp-to` | set session TO | `ADHOC.bd-plane-sixweek-delta-review` | PASS |
| `aws s3api head-object` + `s3 cp` + `sha256sum` | pin the deployed bd artifact | 56,885 B / `3db53a8b…` / ETag `fa9fd5a9…` | **PASS** -- artifact pinned; review is grounded |
| `git show <c>:<path>` + `sha256sum` loop | locate the true fork point | **exact match at `4632383568`** | PASS -- fork measured, not inferred |
| `git log --since` on the source path | enumerate the window | **2 commits**, both named in the TO | PASS -- no misc bucket, residual empty |
| grep + **positive control** | is the retry net reachable from the 49f runner? | 0 hits; control term = 2 hits | PASS -- zero is admissible |
| `comp-pipescript deployed` | per-tree cross-check | `[cot-gold] MATCH, 0 UNCOVERED, "all up-to-date"` | **PASS as run, but see F2** -- it never examined the bd copy |

**What worked:** hashing every candidate commit against the deployed bytes turned "six weeks
diverged" into an exact fork point, which is what reduced a feared 6-week delta to two reviewable
commits.

**What failed:** `comp-pipescript deployed` (F2) -- it answered confidently about a tree that was
not the one in question. **The mandate's own cross-check could not see the defect the TO was
written about.**
