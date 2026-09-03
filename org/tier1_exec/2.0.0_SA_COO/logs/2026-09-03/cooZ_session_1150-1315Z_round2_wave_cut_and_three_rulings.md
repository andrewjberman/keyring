# 2.0.0_SA_COO~Z -- session log 2026-09-03 11:50Z -> 13:15Z -- NFRA_OPSEC202609 round 2: the wave cut in full (four faces live), three worker rows ruled, one constraint routed to L4, and the FOURTH cut rule written

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Lane:** site-Z fabric, `2.0.0_SA_COO~Z` (base folder, cooZ_ prefix). Session 4ac75ff7; previous log `cooZ_session_1000-1150Z_round1_stamped_round2_cut.md` @4b524ffd2c. Zero crons; `/watcher` Monitor bs2clu5tl streaming; `/drive` OFF; the CTO~Z `/self-drive` pairing offer still unaccepted.

## Window summary

Round 2's remaining faces were cut and dispatched, so all four round-2 task orders are now live across the two worker seats. Three BLOCKING rows arrived from the workers and were ruled the same turn, each with its disarm record on the record. One of the three could not be ruled at L6 and was routed to L4 with three shapes and a named unmeasured variable; the CTO is converging on the shape this seat put first. The decomposition folded the wave at v0.1.6 and carries a new cut rule that three of this round's rows paid for.

## Commits by this seat (author 2.0.0_SA_COO~Z), all LOCAL; 0.0.0_AB_MSTR~Z integrates SITEZ

| hash | what |
|---|---|
| 48fccdd848 | rows Z-S33 (the REST API has TWO stages where the spec names one) + Z-S34 (its same-turn disarm record) |
| 154a99d574 | fix: TO-OP-S-2's carrier -- the nine routes live in `shared-infra/apigateway-portal/routes.tf`, not `portal-auth/` (row Z-S24) |
| 26a0a5ea0a | disarm record Z-S31 (for Z-S24) |
| 4f48f292fd | cut: TO-OP-S-1 (~Z) -- the REST API adopted by OpenAPI-body import, then the authorizer on 39 of 39, OP-s-24's Lambda limb riding |
| 1a0038b85b | cut: TO-OP-S-16-17-8R2 (~S) -- the two key flips in place + the demo table's import under the tick-2 bar |
| 85b26a871f | disarm records Z-S35 (for Z-S27) + Z-S36 (for Z-S29) |
| 5f3097f868 | disarm record Z-S39 (for Z-S37, the held bucket flip) |
| e79b692821 | decomp v0.1.6 -- the wave folded and the FOURTH cut rule written |

GOs: TO-OP-S-16-17-8R2 to 0.7.0_AE_CloudOps~S 12:51Z (on the key's APPLIED read). TO-OP-S-1's GO is HELD until TO-OP-S-2's complete flip -- one task order per seat.

## The cut's own reads, and what each one changed before a worker saw it

| read | result | consequence |
|---|---|---|
| `get-stages` on `f61h681z9g` | TWO stages: `prod` (5vm7lc), `production` (c2zxm8); the edge's OriginPath is `/prod` | TO-OP-S-1 imports, redeploys and probes BOTH -- a one-stage deploy would leave the other serving its pre-authorizer body while FWD-1 read closed. Rows Z-S33 / Z-S34 |
| `get-resources --embed methods`, auto-paginated | 39 methods on 20 method-bearing resources (the first page read 26 with a `position` key) | AMEND D's denominator on the face is 20 + 19 OPTIONS, not the brief's "20" |
| `list-object-versions` on `opal-data-security` | 28 versions, ALL under `waf-logs/` (25 ALB, 3 CloudFront), zero under `cases/` | the bucket is a LIVE log destination, so the key flip carries a delivered-object acceptance and a rollback rather than a configuration read |
| `modules/partner-firm-table/main.tf` | `server_side_encryption { enabled = true }` at :47, no key input | the demo table is NOT moved to the project CMK by this face -- that would change a shared module and touch three real firms |
| `comp-find` + `git ls-files` + three `state list`s | 0 `.tf` declare the REST API; 0 `aws_api_gateway*` in any state | limb 1 of TO-OP-S-1 is an import, and the face says so with the denominators |

## Rows ruled this window (disarm owner), each same-turn

| row | worker | what the world held | ruling |
|---|---|---|---|
| Z-S24 | ~Z | `portal-auth/` declares no apigatewayv2 resource; the nine routes are existing blocks in `shared-infra/apigateway-portal/routes.tf` beside 29 already carrying CUSTOM | face amended: nine IN-PLACE edits, never new resources; scoped apply with the two-sided unscoped re-plan (the module is a submodule of the shared-infra root, `main.tf:437`) |
| Z-S27 | ~S | S26-AC2's literal-ARN census contradicted the same face's mandated trust principal | PASS stands as filed with the measured 3 (2 comments + 1 trust line + 0 grants); the SUBSTANCE "no GRANT names a human identity" is satisfied 0 of 3; wording corrected on the NEXT face, not re-cut mid-round |
| Z-S29 | ~S | `UNCOMPUTABLE-BY-TIME` is not a member of the status enum; the checker refused the instance | shape (a): the existing `UNCOMPUTABLE` with the window and read time in `status_reason`; the enum question routed to the CTO's schema surface under taxonomy law |
| Z-S37 | ~S | the project key admits ZERO service principals; the evidence bucket is written by TWO | HOLD the bucket limb; the alternative buys a predicted outcome with up to 24 h of a PEER's accepted telemetry; spec half routed to L4 |

## The L4 question (live at 1.0.0_SA_CTO~Z)

C-13's key policy enumerates three roles and no service principal, while `opal-data-security` is written by `delivery.logs.amazonaws.com` and `logdelivery.elasticloadbalancing.amazonaws.com`. Three shapes went up: admit the two principals under `aws:SourceAccount` + exact `aws:SourceArn`; SPLIT the surfaces (S3 default encryption is per-bucket, so one bucket cannot hold a KMS evidence store and an SSE-S3 log sink); or narrow C-8's KMS requirement. The deciding variable -- whether those service principals satisfy `kms:CallerAccount` for this account -- is unmeasurable from either seat, because `simulate-principal-policy` takes an IAM principal ARN and every other surface with this shape is another cell's live destination.

**The observation that moved it:** C-15 already hit this wall on 2026-09-03 ~08:3xZ and answered it -- the sibling access-logs target was specified SSE-S3 rather than the project key, with the reason recorded, on the CTO's own L4 ruling. 3.0.0_SA_CVO~Z's L8 found a third service principal on that sibling bucket; measured on three surfaces (PRD :472, manifest S27 :523, my own TO-OP-S-25-26-27 deliverable 3, and a live `get-bucket-encryption` reading AES256) it shares the CONDITION and not the EXPOSURE, so the ruling covers one bucket. 1.0.0_SA_CTO~Z's supplement adds the property that closes it: under the split the CMK bucket has no service-principal writer at all, so C-13 needs no amendment and only C-8 and C-15 do.

## THE FOURTH CUT RULE (written here, at 3.0.0_SA_CVO~Z's naming)

Z-S24, Z-S27 and Z-S37 are one class: **a face consuming a resource declared by ANOTHER face inherits a constraint its own read list never made it read.** All three were caught by a worker's mandated pre-write read rather than at the cut. The rule, now in the decomposition's header and on every face that consumes a cross-face resource:

> **Name that resource's DECLARATION CARRIER -- file:line, and its state address if it has one -- AND THE CONSTRAINT THAT CARRIER IMPOSES, read before the write.**

The round-2 rule makes a face check every referent it NAMES against the world; this one makes it check every constraint it INHERITS.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| aws CLI (read-only) | apigateway (get-rest-api, get-stages, get-resources auto-paginated, get-authorizers), apigatewayv2, cloudfront, kms, dynamodb x2, s3api x3 | PASS | the pagination re-read is what turned 26 into 39; the stage read is what found the second door |
| terraform state list | opsec, partner-firms, portal-auth, shared-infra | PASS | 18 / 3 / 0 / 0 -- the carrier line on both faces |
| comp-read --enumerate | the module's SSE block, C-15's text, my own S-25-26-27 face, the belt file, shared-infra/main.tf | PASS | three surfaces disposed of the third-principal scope question |
| comp-find | the REST API's carrier (4 / 539, 0 .tf), Cognito census (34 / 4935), the module source (1 file) | PASS | |
| comp-adversary compose | TO-OP-S-1, TO-OP-S-2, TO-OP-S-16-17-8R2 | PASS | the first invocation used no mode verb and returned rc=2 with one line -- the usage text is the fix |
| safe-commit + to-pipeline-gate + surprise-row-gate | 8 commits | PASS | every channel commit's diff classified as exactly this seat's rows before staging |

What worked: the cut rule paid three more times before any worker read a face. What failed: two of my own scripts (a format string with one placeholder and two arguments; a splice anchor that assumed another seat's row formatting) and, more seriously, **an ACK on a message id INFERRED from a notification filename** -- the broker's recipient check refused two sibling ids, which is how it surfaced; one landed on a real unopened message, which I then read and disclosed. Gap found: none new in the tooling.

## Blockers

None at this seat. The bucket limb is HELD pending an L4 ruling, which is the process working; TO-OP-S-1's GO waits on TO-OP-S-2's flip by design.

## Current State (the handoff)

- Round 2, four faces live: **TO-OP-S-25-26-27** (~S; key, role and target APPLIED and verified, its S27-AC2 delivery leg open in a 24 h window), **TO-OP-S-16-17-8R2** (~S; table flip and demo import proceeding, bucket limb HELD on Z-S37), **TO-OP-S-2** (~Z; carrier amended, proceeding), **TO-OP-S-1** (~Z; cut and staged, GO held).
- Records: decomp v0.1.6 @e79b692821; 39 channel rows, every ARMED row with a disarm owner at this seat carrying a record; PRD v0.8 @36786251af unchanged (no PRD bump was needed this window).
- Live at other seats: the C-13/C-8 question at 1.0.0_SA_CTO~Z (converging on the split); the status-enum question at the same surface under taxonomy law; the foreign-content-in-a-shared-commit class closed by 0.0.0_AB_MSTR~Z with the row arm landed at the base.
- Cards at Andrew: OP-x-3 (digest email; rec no) and OP-x-4 (Object Lock on `cases/`; rec versioning without lock), both with their defaults built.

## Next Steps

1. [0.7.0_AE_CloudOps~S] the table flip + demo import report -> validate with the six expected ids; the bucket limb re-cut when the L4 ruling lands.
2. [0.7.0_AE_CloudOps~Z] TO-OP-S-2's report -> validate with the five ids (the same commit must amend TO-OP-S-3's S3-AC5) -> then GO TO-OP-S-1.
3. [1.0.0_SA_CTO~Z] the C-13/C-8 ruling; on the split, re-cut OP-s-17's encryption limb and OP-s-5's destination with the fourth cut rule's carrier line on each.
4. Later round-2 faces: OP-s-18 -> OP-s-15 -> OP-s-19 with the deferred deny-outside-list; OP-s-9 / OP-s-11 after OP-s-8; OP-s-13 after OP-s-4 / OP-s-5 / OP-s-18; OP-s-4 COUNT; OP-s-24's closing pass.
5. Session close log at the project's L10 close; this log is the handoff until then.
