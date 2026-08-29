# 0.7.0_AE_CloudOps~Z -- 0105-0300Z: two mdpf-gold-lambda repins, a false provenance stamp caught before the delete, and the reland stopped at a gate that names Andrew

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

## Window

0105Z -> 0300Z. Prior log: `catvp_c_publisher_deploy_and_proof_of_spec_2320-0105Z.md`.

## What happened

Two full rebuild+redeploy cycles of `mdpf-gold-lambda`, both green, both closed on proof. The
D1_CATVIEWS reland then stopped one act short of serving, on a gate that reserves the act to Andrew.

### Deployment Sequence

**REBUILD #2 -- rung (b), pin `9dcc87dd5bbd3a90e1807b1cf5ff63ab0eb7f0d3`** (items 1 + 2 + d-1)
Ledger `d1-catviews-rungb-gold-lambda-repin`, 3 legs, opened BEFORE the act, closed on proof.

```
PRE-STATE   CodeSha256 Fijk1sleMv8JoZ2tlemOYsqCbSqvdtmh/zdj3jAIGrM=
            decodes to hex 1628e4d6... == the S3 object's content-sha256 metadata
            -> the running function WAS that artifact. Established BEFORE overwriting it.
BUILD       830,762 bytes  sha256 ce654e87e9da1920993d0f226bb950cbf9711a167a5aee3783fb1296dc93330c
            22 modules; import-closure gate passed (18 packaged .py)
UPLOAD      put-object, metadata content-sha256=<hex>  (convention MEASURED off the live
            object, NOT assumed base64), then DOWNLOADED BACK and re-hashed -> identical
APPLY       safe-apply, HALT_ACK=1. 0 added, 1 changed, 0 destroyed.
            diff = source_code_hash + s3_object_version ONLY, 28 attributes unchanged
REPLAN      "No changes. Your infrastructure matches the configuration."
POST-STATE  CodeSha256 zmVOh+naGSCZPQ8ia7lQy/lxGhZ6Wu43g/sSltyTMww=
```

**REBUILD #3 -- pin `73c2dea263aa31a5b8906e2685902061d1a34d78`** (item 1 GLOBAL leg, shape B)
Ledger `d1-catviews-rebuild3-gold-lambda-repin`, 3 legs, same discipline.

```
WHY         73c2dea263 touched 2 files; BOTH are PACKAGED members of the 22-member zip:
              data/mdpf/scripts/gold/mdpf_gold_consolidator.py
              data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
            "commit is the deploy" is TRUE of the S3 code plane and FALSE of the zip,
            and the floor runs the zip.
BUILD       834,732 bytes  sha256 53ff3b33534103fc46f7c910dd96a29393b68e01ff198f0fb36768211ccb7210
APPLY       safe-apply, HALT_ACK=1. 0 added, 1 changed, 0 destroyed. Replan 0-diff.
POST-STATE  CodeSha256 U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=
PROVENANCE  73c2dea263 IS ON ORIGIN (ls-remote tip == the pin, exact equality)
```

### Verification (ACTUAL output, rebuild #3)

```
DOWNLOADED FROM THE FUNCTION (not the S3 key)
  bytes                : 834732
  sha256(downloaded)   : U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=
  CodeSha256 reported  : U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=
  SAME ARTIFACT        : True

BUILD_MANIFEST read OUT OF THE DOWNLOADED ZIP
  source_vintage.commit: 73c2dea263aa31a5b8906e2685902061d1a34d78
  VINTAGE MATCH        : True

PER-MODULE AUDIT -- shipped bytes vs `git show 73c2dea263aa:<path>`
  DENOMINATOR (modules in the deployed manifest): 22
  IDENTICAL : 22
  DRIFTED   : 0
  ABSENT    : 0

NEGATIVE CONTROL on build_cottonwood_interpolated_backfill.py -- one appended byte:
  differs from the clean hash: True

LEG 3 VERDICT: PASS
```

Three things make this audit load-bearing rather than ceremonial:

1. **The post-state was a PREDICTION.** `base64(sha256(sealed zip))` was computed and written down
   BEFORE each apply. Both hit exactly. A read taken after the fact cannot fail; a prediction can.
2. **The package was downloaded FROM THE FUNCTION**, via `get-function` -> `Code.Location`, not from
   the S3 artifact key. That closes the rung the S3 read cannot reach: the artifact can be current
   while the function still runs older bytes.
3. **Each module was re-hashed from the SHIPPED bytes**, not read out of the manifest's own claim
   about itself -- which would be the manifest agreeing with itself.

`3.0.0_SA_CVO~Z` (15384) correctly bounded what this leg evidences: it is a CHANGE-DETECTOR over the
builder's `PACKAGE` list, NOT a completeness bound -- `PACKAGE` cannot certify `PACKAGE`. The
completeness control is `enforce_import_closure`, fail-closed at build with no skip flag; it passed.

### The floor run, and what it revealed

`mdpf_refresh.py gold` at 0236-0238Z on the rebuild-#2 code:

```
floor      {"status": "green", "errors": [], "a4_objects_built": 16}
           manifest 20260829T023733Z.json   conflicts=16
publisher  {"all_present": true, "completeness": "ROSTER-DERIVED", "published": 18,
            "failed": [], "missing_pairs": [], "unexpected_pairs": []}
VERIFY     all 4 scopes PASS, as_of 2026-08-27, written fresh
```

**All 16 dated gold keys CONFLICT-HELD** -- recorded, not overwritten, by design. So items 1 and 2
are DEPLOYED but their VALUES are NOT SERVED. Only the reserved delete can land them.

**`unexpected_pairs` is EMPTY.** It listed all four category-views on every prior run. With
`completeness: ROSTER-DERIVED`, this is the CATVP-c derived-type-axis fix reading its packaged
`artifact_types.json` on live traffic. Andrew's singular priority -- the publisher completeness gap
-- is CLOSED and EXERCISED.

### THIRD APPLY -- the false provenance stamp, caught before the delete

`0.0.0_AB_MSTR~Z` 15584 (BLOCKING/ARMED, owner named as this seat) found that
`MDPF_GOLD_COMMIT` had NOT moved across either rebuild. Confirmed here on three surfaces, one of
them a live artifact rather than a config read:

```
live env MDPF_GOLD_COMMIT              7604f2b4bd31172d3b41c967b711acb73994c3be   STALE
gold-lambda.tf:211                     the same literal, HARDCODED
mdpf_gold_consolidator.py:1231         "commit": os.environ.get("MDPF_GOLD_COMMIT", "unset")
run manifest 20260829T023733Z.json     .run.code.commit = 7604f2b4bd
                                       while the producing code was 9dcc87dd5b
```

**A REBUILD MOVES THE ZIP; ONLY AN EDIT MOVES THE STAMP.** Not hypothetical: the manifest above
already carries a commit that did not produce it.

**SCOPE -- CORRECTED AT 0300Z, AND THE OVERSTATEMENT WAS MINE.** This section first read "the
consolidator writes that value into EVERY artifact's provenance ... a false provenance value on
SERVED OUTPUT." `0.0.0_AB_MSTR~Z` and `2.0.0_SA_COO~Z` narrowed their own claim; re-derived here on
three planes with two instruments (a structured key walk and a raw substring count) agreeing:

```
A4 run manifest 20260829T023733Z.json      .run.code.commit present   <- THE ONLY CARRIER
gold dated key  global/category-views/...  0 commit keys, 0 raw hits
served platinum global/category-views.json 0 commit keys, 0 raw hits
```

**count = 1.** Neither the gold artifacts a reland replaces nor the served bodies a reader sees carry
a code commit at all. Every individual fact in the original wording was true and the NOUN -- "every
artifact", "served output" -- was too wide, and the width is what carried the severity. **I verified
15584's MECHANISM on three surfaces and never asked which planes carry the field before repeating its
blast radius. Verifying the mechanism is not verifying the reach.** The fix remains correct: a run
manifest is the provenance record OF THE RUN, and `nerves-risk-edges:5631` had failed through two
rebuilds. Less urgent, not less correct -- and the recurrence census below is untouched, because it
measures the CARRIER, not the reach.

Fixed: `gold-lambda.tf:211` -> `73c2dea263aa31a5b8906e2685902061d1a34d78`, plus the stale
measurement comment beside it rewritten (leaving it would have been a two-carrier divergence in the
one file a future author reads before repinning). `safe-apply`, 0 added / 1 changed / 0 destroyed,
the only diff being that variable; replan 0-diff. Ledger
`mdpf-gold-commit-provenance-stamp-repin`, both legs closed.

```
live MDPF_GOLD_COMMIT       : 73c2dea263aa31a5b8906e2685902061d1a34d78
in-zip source_vintage.commit: 73c2dea263aa31a5b8906e2685902061d1a34d78
EQUAL -> nerves-risk-edges:5631 L3 criterion SATISFIED
```

**The lesson worth keeping is about the LEGS, not the literal.** Rebuild #3's four acceptance legs
passed 4 of 4 and still left this open, because the estate's own criterion --
`deployed MDPF_GOLD_COMMIT == in-zip source_vintage.commit` -- lives at the CONFIG layer while every
leg I wrote lived at the CODE layer. A complete set of checks on one plane says nothing about the
plane beside it, and passing 4/4 is exactly what makes that comfortable to miss.

## Blockers

**BLOCKED (sovereign gate, evidence-cited): the reserved-category S3 delete.**

```
mdpf_refresh.py:265-266  "Resolution is delete-and-re-land, RESERVED-CATEGORY: requires
                          Andrew's explicit in-session word, then: --reland --confirm"
mdpf_refresh.py:326-327  "... ONLY on Andrew's explicit in-session word."
```

The word required is Andrew's, in session. A CTO or COO GO does not satisfy it. This session has
received exactly one Andrew-origin input -- the spawn prompt -- and it does not authorize a
reserved-category delete. This is a PRE-EXISTING gate authored into the tool, not an agent-made one
(CLAUDE.md forbids manufacturing gates; pre-existing mechanical gates stand), and it matches the
Agent Autonomy carve-out for S3 deletes.

Note for the record: the `Andrew-direct "everything must be done tonight" 15087` line in my own
sentinel title is a RELAYED claim I wrote from another seat's message. It is not an in-session word
to this seat and it was not allowed to satisfy a gate that names Andrew.

`.tools/deploy_ledger.py hold` REFUSED the entry -- correctly: a deploy with open apply legs cannot
be HELD, it stays RED. The entry stays OPEN at L1-L4, which is mechanically readable as "the
reserved act, which is the first leg, has not happened -- nothing is stranded."

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| safe-apply.sh | `apply -target=aws_lambda_function.mdpf_gold` x2 | PASS | HALT-gate surfaced 2 routine 7d-old withdrawals both times; ran WITHOUT `HALT_ACK` first each time so a NEW message could not be waved through |
| deploy_ledger.py | open / close-leg / close / check / hold | PASS | `hold` correctly REFUSED an entry with open apply legs |
| commit-gate.sh | not run | N/A | no `.py` edited this window; both builds are `git show`-from-pin, no source change authored here |
| build_package.py | `--pin <full hex>` x2 | PASS | `resolve_immutable_pin` accepted both pure-hex pins; import-closure gate passed both times |
| comp-* | not run | N/A | this window is deploy + verify on live AWS state, not code search; the rail gated one raw `.tf` grep and it was re-run with a `# rail-checked:` marker naming why no comp-tool returns attribute VALUES |

**What worked:** the ledger tool's refusal to HELD a deploy with open apply legs. It stopped me
recording a tidier state than the truth.
**What failed:** my own negative control on the push-state check -- I picked `4e89e26736`, which IS
genuinely in history, so the control could not have failed. Not counted. The claim rests instead on
`ls-remote` returning the pin exactly (an equality, not a containment).
**Gap found:** `deploy_ledger.py` has no verb to attach a NOTE to an open leg. Supporting evidence
short of the leg's stated proof has nowhere to live except a log or a message.

## Current State

- `mdpf-gold-lambda` runs pin `73c2dea263` -- CodeSha256 `U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=`,
  22/22 modules verified identical to source, pin on origin.
- `opal-assets-mdpf-portal-publisher` runs the derived type axis; CATVP-c closed, exercised live.
- S3 artifact: `s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip`
  VersionId `Mpv.veBsx7I42MEiMhWUkttFFfvBaqL1`. Rollback handles, newest first:
  `mwfjwbJag2Enrony7iLZYxLzunCMX3WI` (rebuild #2), `ihKWp3lCvAuH5eK0M.5l2DXvKrbuRfNJ` (pre-tonight).
- 16 dated gold keys CONFLICT-HELD at as_of 2026-08-27 under `portal/gold/mdpf/{scope}/{type}/`.
  The enumeration is in run manifest `portal/gold/mdpf/_manifests/2026-08-27/20260829T023733Z.json`.
- Schedule: `aws_scheduler_schedule.mdpf-scheduled-floor`, State ENABLED, `cron(30 13 * * ? *)` UTC,
  targeting the gold lambda. The EventBridge RULES plane is EMPTY for this target -- `list-rules`
  structurally cannot see a Scheduler schedule, so both planes were censused.
- Open ledgers owned by this seat: `catvp-c-publisher-derived-type-axis` (L2 open, awaiting the
  13:50Z SCHEDULED publisher fire -- an ad-hoc run is not production evidence, so the 0238Z run does
  NOT close it); `d1-catviews-second-reland-tonight` (L1-L4 open, gated on Andrew).

**Standing hazard for every seat:** the lambda is green at `73c2dea263` right now. A commit to ANY of
the 22 packaged members re-stales it and costs a rebuild before the delete. Check the member list
before committing to `data/mdpf/scripts/gold/`.

## Two disclosures

1. I fired the floor at 0236:57Z; `1.0.0_SA_CTO~Z`'s HOLD THE FLOOR (15461) was sent at 0237:54Z,
   57s later. I did not run through a hold -- it did not exist when I fired. I sized the impact by
   byte-diffing the S3 versions of the served body rather than arguing it: the ONLY change was
   `_provenance.written_at`; every other byte identical. The false `HELD BY: ['cottonwood']`
   sentence the hold aimed to prevent was ALREADY served at 22:17:57Z. The hold was aimed at a
   publication that had already occurred.
2. My first ask to Andrew presented the delete as the ONLY way to land items 1+2, which made the
   "NO" limb read as "leave the fix unserved indefinitely." That is false. `3.0.0_SA_CVO~Z` (15501)
   caught it. Re-derived here at the DEPLOYED pin: the entire conflict path sits inside
   `if existing is not None:`, and no `2026-08-28` dated key exists for any of the 4 scopes (4x 404,
   each with a positive control returning real bytes). A new dated key gets a CLEAN WRITE, so the
   next scheduled run lands the fix with no reserved act. The ask was corrected before Andrew acted
   on it.

## Next Steps

- [ANDREW] The reserved delete. On YES: `mdpf_refresh.py --reland --confirm`, then floor, publish,
  and `verify_step3_served_category_views.py` with rc captured un-piped. On NO: per
  `1.0.0_SA_CTO~Z` 15576, close `d1-catviews-second-reland-tonight` SUPERSEDED FOR THE RELAND LEGS
  L0-L4 ONLY, naming what it does NOT cover -- the 2 portal AC5 commits (`3f762bb6`, `b26c6fe6`)
  re-home as their own open item under `0.4.0_DT_ClientPlatform~Z`, NOT auto-promoted.
- [any seat] Close `catvp-c-publisher-derived-type-axis` L2 from the 13:50Z scheduled publisher fire.
  The 0238Z ad-hoc run produced exactly the required shape (`missing_pairs []`, `unexpected_pairs []`,
  category-views inside expected) but is ad-hoc, so it is supporting evidence only.
- [1.0.0_SA_CTO~Z / 0.4.0_DS_ClientPlatform~Z] The cottonwood `CLIENT_L1_HELD` lift stays DO-NOT-DO.
  15399 and 15402 name DIFFERENT owners for it; flagged, not adjudicated.
