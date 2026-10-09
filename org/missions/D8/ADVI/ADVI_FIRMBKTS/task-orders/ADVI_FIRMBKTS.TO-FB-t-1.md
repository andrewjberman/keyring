# ADVI_FIRMBKTS task order -- `FB-t-1` -- THE KEY CENSUS OF THE THREE LEGACY BUCKETS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP.md</decomp_doc>
<owned_cells>FB-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~1</issued_to>
<issued_by>2.0.0_SA_COO~F1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the only AWS act is list_objects_v2 by the box's existing identity.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~F1) on dell1 -- r1_census.py --static 0 of 5 and --live 0 of 2 at base (census.json absent); 5 of 5 and 2 of 2 against the issuer's reference census (163 classes, listed 2026-10-09T20:19:02Z); the live arm ran in 39 s.
EGRESS CLASS, declared: AWS READ ONLY (list_objects_v2 on opal-data-bd, opal-data-inf, opal-data-cot).
</preflight>

## 1. THE CELL -- `FB-t-1` (round 1, THE THREAD for FWD-1; decomposition v1)

FWD-1 reads: *anyone who looks at where a piece of data is kept can tell what it is and whose it is, without opening
it.* The thread runs from the legacy keys to two readers. This cell is its first hop: every key in the three legacy firm
buckets, known by CLASS, with a denominator from the live plane. Your census is the input to `FB-t-2` (the mapping
table), which another order in your queue places class by class.

The three buckets, and the firm each holds (the firm's LONG form is how later cells name it):

| bucket | firm (long form) | objects at the issuer's listing, 2026-10-09T20:19:02Z |
|---|---|---|
| `opal-data-bd` | `49financial` | 131,391 |
| `opal-data-inf` | `inflection` | 99,668 |
| `opal-data-cot` | `cottonwood` | 7,802 |

1. **List all three buckets with boto3** (`boto3.client("s3").get_paginator("list_objects_v2")`), every page, and count
   client-side. Take `listed_at` (UTC, `%Y-%m-%dT%H:%M:%SZ`) **before** the listing starts. Three threads list all
   three in about 40 s. Do NOT use the `aws` CLI with `--query length(Contents[])`: it prints one count per page.
2. **Group every key into a CLASS at the TABLE grain.** A class is a literal key prefix ending in `/`, or one whole key
   (a single-key class). The rules:
   - Collapse partition segments (`date=2026-09-11`, `2026-09-11`, `20260911`, any `k=v`) and entity-id segments (one
     account, client, advisor, run or person; `platinum/accounts/{id}/...` is ONE class `platinum/accounts/`). At a
     naive depth-3 grouping `opal-data-bd` gives 11,165 classes, which is the entity ids leaking in.
   - A class is homogeneous: one kind of thing. If a prefix holds served JSON next to parquet tables, or state next to
     data, split it deeper so each class is one kind.
   - Directory classes are disjoint (no class prefix is a prefix of another directory class). A single-key class may
     sit under a directory class; it owns its key and the directory class does not count it.
   - **Two keys in `opal-data-inf` are single-key classes, always:** `gold/meta/pipeline-complete.json` and
     `orion/jwt/current.json`. Both are subjects of Andrew's rulings, placed as decisions by the next cell.
   - Odd shapes are classes like any other. Keys with a LEADING SLASH exist in `opal-data-inf` (`/clients/...`); their
     class prefix keeps the slash. Logs, backups and rollback copies are classes too. Do not drop or judge anything:
     this cell counts, the next one places.
   - At most 500 classes per bucket.
3. **Write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/census.json`, in exactly this shape** (AC1 and AC2 bind it):
   ```json
   {"listed_at": "2026-10-09T20:19:02Z",
    "instrument": "boto3 list_objects_v2 paginated, as <the caller ARN from sts get_caller_identity>",
    "buckets": {"opal-data-bd": {"objects": 131391,
                                 "classes": [{"prefix": "platinum/accounts/", "objects": 7557,
                                              "sample_key": "<one real key in the class>",
                                              "last_modified_max": "<newest LastModified in the class, %Y-%m-%dT%H:%M:%SZ>"}]},
                "opal-data-inf": {}, "opal-data-cot": {}}}
   ```
   `objects` per bucket is the listing's count, and the classes' `objects` sum to it. Pick each class's `sample_key` as a
   representative key: a real data file where the class has one (not a `_SUCCESS` or a `.keep`), and a recent date
   partition where the class is dated.
4. **Write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/CENSUS.md`**: the instrument, the caller ARN and `listed_at`
   at the top; one table per bucket (class prefix, objects, sample key, newest), sorted by prefix, each table headed by
   its denominator. State in one line that the census covers the three legacy buckets only and is not a statement about
   any other bucket.

## 2. BOUNDS

1. **AWS is READ ONLY**: `list_objects_v2`, `head_object` and `sts get_caller_identity` only. No `put`, `copy`, `delete`,
   no `get_object` of a client file, no apply, no deploy, no install, no push. REFUSE, do not rescue.
2. **CLIENT DATA:** never open an object's bytes and never print a client figure. Keys are the only data here. Account
   ids and client names appear inside keys: write a key into `census.json` only as a `sample_key`; in `CENSUS.md` print
   the class prefix and the count, and write a sample key with its entity-id segment replaced by `{id}`.
3. Only the files in section 3 change.
4. No non-ASCII; LF line endings; JSON written with `indent=1` and `ensure_ascii=True`.
5. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/census.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/CENSUS.md
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md` (IV.3 names the key classes the graph
attributed), the PRD `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md`, and the issuer's checks under
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/` (never edit them).

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
  <criterion id="AC1" cell_refs="FB-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/r1_census.py" --static; echo "exit=$?"</invocation><expect>ROUND 1 CENSUS STATIC: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="FB-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/r1_census.py" --live; echo "exit=$?"</invocation><expect>ROUND 1 CENSUS LIVE: 2 of 2 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 grades the file alone. AC2 is the seam probe against the real neighbour: it lists the three buckets again and
requires every key that existed at `listed_at` to fall in exactly one of your classes, and every class to hold a live key.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~1/ADVI_FIRMBKTS.TO-FB-t-1.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `ADVI_FIRMBKTS-D1-W1-S<k>`, with `surfaced_at` from `date -u +%FT%TZ`
at filing. Report once: the files (one line each), the three bucket denominators and class counts, the output line of
every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (FWD-1) over PRD v1.3 @30d612d5e5 (ADMITTED). Base box/dell1. LF only. Checks
positive-controlled against the issuer's reference census before the cut (L5_FACTS section 1).

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's (msg 3113: a PRD commit is refused until it gains a KEY SURFACES section). Every other limb passed in the issuer's dry run.
<status>pending</status>
<round>1</round>
<to_id>ADVI_FIRMBKTS.TO-FB-t-1</to_id>
<slot>~1</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
