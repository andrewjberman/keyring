# WS-5 (WSE_COTMDL) -- STOP-BEFORE-BUILD, shape re-ruled, IAM grounded. Plus Deliverable 2 design + one retraction.
**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, DEPLOY
**serial:** 0.7.0_AE_CloudOps
**window:** 2026-07-22 ~13:06Z -> ~13:40Z (session start; prior log = mdpf_exact9_flip_ROLLED_BACK_p0.md)

## STATE
Spawned onto WS-5 as a FLIP PRECONDITION (not flip-custody). **Nothing mutated in the estate this session
-- deliberately.** WS-5 re-scoped by CTO and re-staffed as a PAIR (me = TF/estate + exercise;
`0.6.2_AE_PartnerETL~A` = converter/stamp). Deliverable 2 designed + committed, apply HELD for Andrew.

## THE CALL THAT MATTERED: REFUSED THE BRIEFED FIX BEFORE BUILDING IT
Brief (COO 131124Z, MSTR 131108Z, blessed by three): *"extend the notification filter to `.json`."*
I grounded it first and it does not work. Six findings; five load-bearing, one wrong (below).
1. **DECISIVE -- `.xlsx` is pinned in the CONVERTER, not only the S3 filter.** `mirror_conversion.py:92-94`
   `_BD_RE` requires one of 5 tables + `_DAILY_{date}.xlsx`; `classify_key:152-188` falls through to
   `unrecognized`. **A `.json` filter would deliver events to a converter that refuses them -- GREEN, and
   converts nothing.** COO had already written the suffix fix into the project record.
2. **Per-object self-races at this shape** (~56-62 objects/day) -- verbatim the failure CTO's own SMARTX
   WS-A7 ruling prohibits at `silver.tf:111-120`.
3. `.json` on that prefix admits the **137 legacy `_BRONZE_COMPLETE.json` markers** (only ~62 are rebalancer).
4. **The 05:00Z sweep does NOT backstop this feed** -- `expected_partitions:506-524` admits only
   `kind=="data"`. **NO event path AND NO sweep path** -- stronger than CTO's original framing.
5. 07-22 bronze byte-identical to 07-21 (ETags exact). **Refused to call it stale** -- from S3, stable-roster
   and frozen-feed are byte-indistinguishable. Now a named co-sign term: `feed-liveness = UNDETERMINED`.
6. **WRONG -- retracted, see below.**
**Outcome:** CTO adopted the read whole, ruled **completion-keyed whole-day convert (eclipse/smartx), NOT
per-object**, re-scoped WS-5, and **moved the date rather than squeezing the lane.**

## THE SELF-TRIGGER FINDING (sent "before you rule", while not blocked)
Q2 was on_success vs stamp-key-as-S3-event. I found `write_manifest` (`:600-602`) PUTs to
`{source}/{scope}/meta/conversions/{run_id}.json` -- **the converter writes its own output into the proposed
trigger prefix**, from BOTH `run_event` and `run_sweep`. Converter -> manifest -> event -> converter.
Held apart only by `-complete.json` vs `{run_id}.json`; S3 cannot negative-match, so Belt-1 does not hold.
**Worse than the eclipse trap: there the admitted object is producer-written (bounded); here it is
converter-written (self-sustaining).** CTO had already ruled on_success on the Door-6 argument and recorded
that he *"ruled correctly on incomplete information"* -- both arguments agreed, so the ruling held, but had
they diverged he would have decided without the decisive fact.

## MY ERROR, AND WHAT IT COST
**Finding #6 was wrong.** I claimed the 06:00Z runner was not the producer because bronze read
`02:00:4xZ`. **`aws s3 ls` renders LOCAL time with no marker -- I appended the `Z` myself.** Box is EDT
(-0400); `list-objects-v2` gives `2026-07-22T06:00:45.000Z` for the same objects. Verified independently
before retracting (I did not take the refutation on self-report either). **COO had already retracted a TRUE
premise upward to CTO and MSTR on my error.** Retracted to all three within ~9 minutes.
**Why it survived three of us:** `cot-bd-session-daily` really IS `cron(0 2)`, so the mis-rendered timestamp
landed exactly on a real independent scheduler -- **it arrived pre-corroborated, carrying a mechanism, not
as noise.** And it failed **RED**, not green: a false *refutation* of a true claim, which travels fast in a
fabric rewarded for refusing. I had the right instrument in hand (used `list-objects-v2` for ETags the same
pass) and read units off the wrong one.
**META (escalated to MSTR):** this is the **FIFTH** occurrence of this trap (06-30, 07-06 x2, 07-13, today)
and it was **already banked in memory FOUR TIMES**. Four agents each hit it, failed to find the existing
copies, and wrote another. **The duplicates are a measurement of the recall path failing.** Consolidated
rather than writing a fifth; proposed a gate -- our own law says gates teach at violation time while prose
taxes every session, and here prose was written 4x and did not stop #5.

## IAM (live primitive -- comp-iam fails GREEN on new resources)
- **Converter needs ZERO new S3 grants.** `opal-assets-silver-blackdiamond-role` is PREFIX-scoped
  (`.../bronze/*`, `.../silver/*`, `.../meta/*`), not feed-scoped -- rebalancer feeds + `fact_model_*`
  already covered. **The TO scoped me a new exact-ARN role the estate does not need** -- recorded as a TO
  correction rather than manufacturing the work.
- **ONE grant missing, and it is 0.6.2's:** `cot-rebalancer-runner-role` -> `lambda:InvokeFunction` on
  `opal-assets-silver-blackdiamond` = **implicitDeny**. **An on_success destination without it fails
  SILENTLY** -- pull succeeds, stamp writes, gates pass, nothing converts, no error. Destination + grant
  must land in ONE apply; destination-without-grant is worse than neither because it looks wired.

## Compiler Tools
| tool | run | result | note |
|---|---|---|---|
| `comp-which` | routed the notification-config question | near-tie (comp-aws/comp-iam/pipescript) | honest tie, not a false confidence; I read descriptions and picked |
| `comp-grep` | `filter_suffix` / `xlsx` over `infra/aws/terraform` | 8 + 26 hits, denominators printed | found `silver.tf:127` + `:528`, the decisive config |
| `aws iam simulate-principal-policy` | 3x, **ONE `--resource-arns` each, SEPARATE invocations** | target implicitDeny / positive-control allowed / firm-sep explicitDeny | positive control proves the deny is real, not a shut instrument (22a) |
| `aws s3api list-objects-v2 / get-role-policy / get-bucket-policy / get-bucket-lifecycle-configuration` | live grounding throughout | PASS | **used ISO8601 explicit-Z after the `s3 ls` error, for the rest of the session** |
| `safe-commit.sh -F` | Deliverable 2 design | PASS @bc75454f0 | `-F` per LD-0276; surface-check OK; risk-reflex CLEAN (1 file vs 1239 danger nodes) |
| `comp-blast` | **NOT yet run** | pending | owed on orion/eclipse when 0.6.2's roster diff lands (`mirror_conversion.py` is shared by 3 families) |

## Deliverable 2 -- portal-v2 `json/mdpf/**` DENY (design @bc75454f0, NOT applied)
Two defects in the control **as specified**, both found before build:
- **A bucket policy CANNOT block lifecycle expiry** (service-performed, not principal-performed). As
  specified it lands, exercises GREEN on a denied delete, and leaves the named vector open. The lifecycle
  vector needs `Deny s3:PutLifecycleConfiguration`, which is BUCKET-level and cannot be prefix-scoped --
  broader than the hold, so **CTO/COO's scope call, not mine.**
- **The cited 17a precedent does not transfer:** it was a pure ADD to an empty policy (`monolith.tf:230-231`).
  portal-v2 already has 2 CloudFront Allow statements and `aws_s3_bucket_policy` REPLACES the whole policy --
  **a naive build takes the portal data plane dark, including the artifacts the hold protects.**

## Blockers
- **0.6.2** -- the `lambda:InvokeFunction` grant + roster diff (event + sweep land together).
- **Andrew** -- 07-17 alert-suspension adjacency; CTO will not confirm Deliverable 2 until answered.
- **CTO** -- Deliverable 2 V2 scope (bucket-wide lifecycle deny, or record the vector explicitly unclosed)
  + placement root for a policy on an unmanaged bucket.
