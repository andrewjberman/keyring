# Deploy Completion Record
**Date opened:** 2026-10-12T13:40:56.795772+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-11 act 4 dell1 leg (GO @8cd6a18a3b): the eight IRPT consumers deploy the flipped loaders.py (re-pin e274a0e60c to flip commit 69679b90e3), BEFORE and AFTER authorization sample, first hour; pair COO 0a4d82ac06 + ADDENDA 1-2, CTO 507d3b3ce1 + ADDENDA 1-5; rollback by prior artifact object versions (no published versions exist) and act 2's gold_dispatch.sh prior VersionId
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pair bytes and SIGNED; pre-flip reads r4_oai 3 of 3, r4_flipcommit 4 of 4, r4_repin 3 of 3 (detached worktree at e274a0e60c); authority at the 8 function ARNs; the eight current CodeSha256 values; CloudFront TTL read and named; producers' next chain start | each last line printed in the entry | r4_oai 3 of 3; r4_flipcommit 4 of 4; r4_repin R1 PASS 8 of 8 rows, R2/R3 FAIL for irpt-ycharts-generate only (built from branch scratch/r4-act4-ycharts-pin, not at the re-pin); simulate at 8 function ARNs UpdateFunctionCode allowed 8 of 8, control explicitDeny; TTL named: CachingDisabled 0/0/0, opal-scoped-advisor-by-firm 1/60/31536000 (max-age 60 injected), json-tiered 0/300/31536000, api-general 0/300/31536000; no invalidation | CLOSED 20261012T142626Z |
| L2 | verify | BEFORE sample: SAMPLE_BEFORE.json, a granted and a refused viewer per side-effect-free function, status and body sha256 only; 5xx at baseline is a STOP | record count and status denominator | SAMPLE_BEFORE.json 14 records, 7 functions x granted and refused; statuses 200 403 404 422, 0 5xx; second run 14 of 14 records equal (determinism control); taken 14:00:41Z-14:03:20Z | CLOSED 20261012T142626Z |
| L3 | s3-prefix | build-and-upload.sh investor-reporting for the eight functions (ycharts from branch scratch/r4-act4-ycharts-pin c4ca0c9a99 in a throwaway worktree); ACT4_EXPECT.json written; each hash printed beside the rehearsal | the eight artifact sha256 beside the rehearsal values | 8 of 8 artifact hashes equal the issuer rehearsal (ycharts from c4ca0c9a99, narrative rebuilt clean, row D1-S37); ACT4_EXPECT.json written; each prior S3 object version equals its deployed CodeSha256 (8 of 8) | CLOSED 20261012T142627Z |
| L4 | activation | eight scoped plans, each changing the function's code hash only (s3_object_version, source_code_hash, last_modified); plan check script prints the attribute diff | each plan summary line and the attribute check | 8 scoped plans each Plan: 0 to add, 1 to change, 0 to destroy; differing attributes last_modified, s3_object_version, source_code_hash only; env equal; after hash equals artifact 8 of 8 | CLOSED 20261012T142627Z |
| L5 | activation | eight safe-apply on the saved plans, begun not before 13:45Z the same minute as the laptop leg; first and last unit apply times printed | the first and last apply times, each read-back CodeSha256 equals its artifact | 8 safe-apply, each Apply complete 0 added 1 changed 0 destroyed rc 0; first unit start 14:03:43Z, last unit end 14:13:46Z; read back CodeSha256 equals artifact 8 of 8 (r4_act4 8 of 8 arms); COO HOLD msg 4408 at 14:21:30Z arrived after the last unit; ruling msg 4416 LEAVE in place | CLOSED 20261012T142627Z |
| L6 | verify | AFTER sample SAMPLE_AFTER.json, r4_sample_eq.py all EQUAL, irpt-ycharts-generate same answers; irpt-performance-adapter invoked once and its evidence artifact KEY named not under a served class | the sample last line and the key | SAMPLE_AFTER.json 14 records; r4_sample_eq SAMPLE EQUAL: 14 of 14 cases; granted 7 refused 7; ownership reads at the canonical key 0 (field empty by construction, row D1-S39; canonical key evidenced at the artifact 8 of 8); performance adapter census event refuses at input validation, no evidence artifact written, invoked twice (row D1-S39) | CLOSED 20261012T142627Z |
| L7 | verify | first hour: router behaviors origin responses (CloudFront metrics) over the first hour after the last unit, denominator printed; 403 or 404 is Branch B | the metric read and denominator | first hour read 15:14Z: IRPT functions 52 invocations, 36 real, 0 AccessDenied/NoSuchKey/Traceback/timeout lines; distribution aggregate 641 requests since first unit, 5xx 0, 4xx concentrated in one 499-request burst at 14:13Z comparable to pre-flip bursts; router behaviors origin responses NOT separable (logging disabled, no additional metrics: row D1-S39); maps EQUAL at 15:00Z | CLOSED 20261012T151503Z |
| L8 | verify | AC1 r4_act4.py --arms irpt 8 of 8; AC3 act-3 compare DEST-VS-MANIFEST EQUAL; platinum_dest_view.py shipped at close so FB-f-9 AC1 reads 20 of 20 | the three outputs quoted |  | OPEN |
| L9 | git | source-map artifact_* record committed (the M3 commit), proof instance written, TO-FB-f-11 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261012T134056Z OPENED by 0.7.0_AE_CloudOps~FB1 with 9 leg(s)
- 20261012T142626Z LEG L1 closed: r4_oai 3 of 3; r4_flipcommit 4 of 4; r4_repin R1 PASS 8 of 8 rows, R2/R3 FAIL for irpt-ycharts-generate only (built from
- 20261012T142626Z LEG L2 closed: SAMPLE_BEFORE.json 14 records, 7 functions x granted and refused; statuses 200 403 404 422, 0 5xx; second run 14 of 14 r
- 20261012T142627Z LEG L3 closed: 8 of 8 artifact hashes equal the issuer rehearsal (ycharts from c4ca0c9a99, narrative rebuilt clean, row D1-S37); ACT4_E
- 20261012T142627Z LEG L4 closed: 8 scoped plans each Plan: 0 to add, 1 to change, 0 to destroy; differing attributes last_modified, s3_object_version, so
- 20261012T142627Z LEG L5 closed: 8 safe-apply, each Apply complete 0 added 1 changed 0 destroyed rc 0; first unit start 14:03:43Z, last unit end 14:13:46
- 20261012T142627Z LEG L6 closed: SAMPLE_AFTER.json 14 records; r4_sample_eq SAMPLE EQUAL: 14 of 14 cases; granted 7 refused 7; ownership reads at the can
- 20261012T151503Z LEG L7 closed: first hour read 15:14Z: IRPT functions 52 invocations, 36 real, 0 AccessDenied/NoSuchKey/Traceback/timeout lines; distri

## ACT 4, THE DELL1 LEG -- hand record (0.7.0_AE_CloudOps~FB1, 2026-10-12T14:23:54Z; GO @8cd6a18a3b)

- **Pair:** COO half `0a4d82ac06` + ADDENDA 1 and 2, CTO half `507d3b3ce1` + ADDENDA 1 to 5, read at HEAD, 0 uncommitted. Flip commit
  `69679b90e3dc52b670d33fddd96d06be1deaac90` (in HEAD), re-pins `e274a0e60cf43ce8f80db87e20f0e070d62906e0` (in HEAD).
- **Pre-flip reads (13:4xZ-14:02Z):** `r4_oai.py` 3 of 3; `r4_flipcommit.py --verify` 4 of 4; `r4_repin.py` run in a detached worktree at the
  re-pin: R1 PASS (8 of 8 rows), R2/R3 FAIL for irpt-ycharts-generate only (that function builds from the kept branch below, not at the re-pin);
  the other seven read the rehearsal hashes. Authority: `simulate-principal-policy` at each of the 8 function ARNs for the actor
  `user/cloudops-dell1-agent-user`, one resource per call: UpdateFunctionCode and GetFunctionConfiguration `allowed` 16 of 16; control
  `shared-advisor-router` `explicitDeny`; s3:PutObject at the artifact key `allowed`. No grant created.
- **TTL, READ AND NAMED:** distribution EVTSA9VEHNZVH, 29 behaviors, 4 cache policies: Managed-CachingDisabled 0/0/0;
  opal-scoped-advisor-by-firm min 1 / default 60 / max 31536000 (the origin's max-age governs; the router-response injects max-age=60 per the
  GO); json-tiered-5min-cache 0/300/31536000; opal-api-general-5min-cache 0/300/31536000. No invalidation was added.
- **Builds (8 of 8 equal the issuer's rehearsal, `ACT4_IRPT_EXPECT_ISSUER.json`):** seven from the main tree; irpt-ycharts-generate from the
  kept branch `scratch/r4-act4-ycharts-pin` (c4ca0c9a99) in a throwaway worktree (`NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM=`); irpt-narrative
  rebuilt from a clean detached worktree at the re-pin after the main-tree build read cQ+WcTub... (row `ADVI_FIRMBKTS-D1-S37`; that object version
  never applied). Each prior S3 object version re-read: its bytes equal the function's deployed CodeSha256 (8 of 8): the rollback record,
  `act4_irpt/builds_and_priors.json`. `ACT4_EXPECT.json` written.
- **BEFORE sample (14:00:41Z, determinism control: a second run, 14 of 14 records equal):** 7 functions x (1 granted, 1 refused viewer), viewers
  drawn from the ownership map and `opal-users-v2` (a partner row and an active profile each; not named); statuses {200, 403, 404, 422}, 0 5xx.
  The performance adapter is outside the seven, per the census.
- **Plans (8, scoped `-target`, parallel):** each `Plan: 0 to add, 1 to change, 0 to destroy`, exactly the function, differing attributes
  `last_modified`, `s3_object_version`, `source_code_hash` only, environment equal, after-hash equal to the artifact (8 of 8).
- **Apply, sequential via `.tools/safe-apply.sh`, FIRST unit start 2026-10-12T14:03:43Z, LAST unit end 2026-10-12T14:13:46Z** (about 10 minutes
  end to end, 8 x about 75 s), each `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`, rc 0. Order, per unit start and end:
  `act4_irpt/apply_times.txt`. **The flip units began without the laptop leg: I did not confirm FBL's start minute, and the COO's HOLD
  (msg 4408) was sent at 14:21:30Z, after the last unit.** The split with the edge units is open until FB-f-19 lands.
- **AC1** `r4_act4.py --arms irpt`: `ROUND 4 ACT 4 IRPT: 8 of 8 arms`, exit 0 (14:14Z). **AC2** `r4_sample_eq.py`: `SAMPLE EQUAL: 14 of 14 cases;
  granted cases 7, refused cases 7; ownership reads at the canonical key 0` (the field is empty by construction, row `ADVI_FIRMBKTS-D1-S39`).
  **AC3** act-3 compare: `DEST-VS-MANIFEST: EQUAL` (53031 present, 0 missing, 0 mismatch), exit 0 (14:18Z). Deployed artifacts: 8 of 8 carry
  `loaders.py` equal to the flip commit's blob and name `opal-data-49financial`.
- **Performance adapter (named, as ordered):** the census event refuses at input validation (`explicit server-issued selection required`); no
  evidence artifact written, no key to name; invoked twice (sampler, one debug re-run), both refused (row S39).
- **platinum_dest_view.py** shipped at 14:17Z (`safe-deploy.sh`, 1 path, DEPLOYED and VERIFY OK); `deployed-equal` then reads 18 of 20, the other
  two being another project's undeployed commits (row `ADVI_FIRMBKTS-D1-S38`).
- **Post-flip OAI read** (14:21Z): `r4_oai.py` 3 of 3 again.
- **Seat hygiene:** one debugging print of mine showed the head of one directory-search response in this seat's session output (no write to
  any file or message); the printing was removed from the sampler path. Two scratch worktrees (`wt_repin`, `wt_ycharts`) sit under this seat's
  scratch directory; they are not removed here (recursive deletion).
- **Open:** the first hour's read (ends 15:13:46Z), the COO's ruling on leave-or-roll-back, the close.

## THE COO'S RULING ON THE OPEN SPLIT (msg 4416, 2026-10-12T14:22:36Z)

- Leave all eight in place; no rollback now (copies byte-equal, no producer writes the legacy home, sample 14 of 14 equal).
- Until the edge leg lands: read BOTH ownership maps at 15:00Z, 16:00Z and 17:00Z and print their VersionIds. Any difference, or the laptop leg
  unable to begin by 17:00Z, means ROLL ALL EIGHT BACK. Nothing else moves.
- Split record: first unit 2026-10-12T14:03:43Z (irpt-49f-reporting-read-lambda), last unit end 2026-10-12T14:13:46Z (irpt-ycharts-generate).

## ROLLBACK ACTOR, NAMED (0.7.0_AE_CloudOps~FB1, 2026-10-12T14:44:09Z; COO msg 4433, CTO ADDENDUM 7)

**The rollback actor for the eight IRPT units AND for act 2's dispatcher is `0.7.0_AE_CloudOps~FB1`** (dell1; identity
`user/cloudops-dell1-agent-user`; authority read at 14:0xZ: UpdateFunctionCode allowed 8 of 8 at the function ARNs). Not mine: the three edge units
(`0.7.0_AE_CloudOps~FBL`, `FB-f-19`) and the registry and source-map pin commits (the issuer's revert and regeneration). A dark laptop blocks nothing here.

**Triggers (any one):** an inequality in the hourly ownership-map reads (VersionId or content hash, legacy vs canonical, 15Z to 21Z); the edge leg
not BEGUN by 21:00Z (CTO ADDENDUM 7); any Branch B condition of the pair. **Deadlines:** act 2's dispatcher back before the producers' 23:00Z chain;
every rollback read back before 02:00Z. The COO's word is not awaited once a trigger holds.

**IRPT units (per function, in the census order; the previous object versions below were re-read: each one's bytes equal the CodeSha256 the
function ran before this act):**

| function | S3 key (bucket opal-313476888478-lambda-artifacts) | PRIOR S3 VersionId | prior CodeSha256 (re-read: equals the deployed one at 13:40Z) | root / module |
|---|---|---|---|---|
| `irpt-49f-reporting-read-lambda` | `investor-reporting/irpt-reporting-read-lambda.zip` | `oQIs2ioYDFqWbAMROuJnyxpiN5WGqe5n` | `8ySmTtYXTqZgnpFY/cnFKnbsGGO/qm6qLCxGLXhIVCI=` | `reporting-read` / `module.irpt_reporting_read` |
| `irpt-directory-search` | `investor-reporting/irpt-directory-search.zip` | `MjZTtOj09NrJCiHLBUmYt_38x9JBgCx8` | `RwgwXI5+xiss9h7OmVPqk6EujzQalXYCciQkvTBGj+c=` | `directory` / `module.irpt_directory_search` |
| `irpt-export-render` | `investor-reporting/irpt-export-render.zip` | `3xfTd055xcuh84iYVxtLUu3LzWt6bFha` | `c7jOyysB/zo6OjtzCNdUZiu0o4fxNE9XeCM1FxXIHhk=` | `export` / `module.irpt_export_render` |
| `irpt-holdings` | `investor-reporting/irpt-holdings.zip` | `EXYWixzhP1B6gsNLQC1guU6jYE8uqV_g` | `CKpZUMD5RVWyY/2oyo8zZwN7Ss8J2FbkeNFr2XYbXD8=` | `holdings` / `module.irpt_holdings` |
| `irpt-narrative` | `investor-reporting/irpt-narrative.zip` | `7acZDre86_QNcw96bQt66G805ztwbMSS` | `x0SqAx2US8UXLnn7Xqy5l3Ttd0Iv1TZQ2jlxgCQtflU=` | `narrative` / `module.irpt_narrative` |
| `irpt-performance-adapter` | `investor-reporting/irpt-performance-adapter.zip` | `B_U4XGkpDqMHPVl6u.quhmEerpseF5oC` | `9kYLdR64P0p2TEbDXcQu1hrpQ9KtqjPNnFDpoE/W31A=` | `performance` / `module.irpt_performance_adapter` |
| `irpt-status` | `investor-reporting/irpt-status.zip` | `sNe8hzDee69r.z596UgjXChHWPMxoGxl` | `6idtFvAmYk73wJdr5DPRIyEPrLeWgzjlqbdNr5f1wxc=` | `ops` / `module.irpt_status` |
| `irpt-ycharts-generate` | `investor-reporting/irpt-ycharts-generate.zip` | `.epN9U3xZSMhU5WmEudwCrbjnydqg4N6` | `tdpterTMfJlWXjnoAQCwil+wN/Jf8Q/yLjGxTk7yUkk=` | `ycharts` / `module.irpt_ycharts_generate` |

1. `aws s3api copy-object` the PRIOR VersionId over the same key (a new latest version carrying the prior bytes), read the object back: its sha256
   (base64) equals the prior CodeSha256 column.
2. Scoped plan of the root, `-target=<module>`, saved: `Plan: 0 to add, 1 to change, 0 to destroy`, only `last_modified`, `s3_object_version` and
   `source_code_hash`, the hash equal to the prior CodeSha256, environment equal (the same rule the forward plans were graded by).
3. `.tools/safe-apply.sh` of that saved plan. Never `aws lambda update-function-code` (Terraform only).
4. Read `get-function-configuration`: CodeSha256 equals the prior value, State Active, LastUpdateStatus Successful. After all eight: the BEFORE sample
   `SAMPLE_BEFORE.json` re-run (viewers re-drawn by the same rule) reads EQUAL to `SAMPLE_BEFORE.json` (14 of 14).

**Act 2's dispatcher:** `s3://opal-data-bd/code/gold/gold_dispatch.sh`, PRIOR VersionId `VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM` (LastModified
2026-10-01T08:41:28Z, 74731 bytes, git blob `631d6e6f4ae39909b88926a500499646fd6ccb01`); copy that version over the key with `aws s3api copy-object`
(SSE AES256 as the act did), download the key and `cmp` it to the blob. The producers' next chain then writes the legacy home again (CTO half
condition 1). Entry of record for the dispatcher: `20261012T0615Z_advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012_deploy_completion.md`.

**Recorded cost of leaving the split open:** while the edge units read the legacy ownership key and the eight read the canonical one, an ownership
change would be seen by only one side; both maps were byte-equal at 13:56Z and nothing is hand-edited (COO msg 4416). The hourly reads are the bound.

## THE FIRST HOUR (0.7.0_AE_CloudOps~FB1, read 2026-10-12T15:14Z; window 14:13:46Z to 15:13:46Z after the last unit)

- **The eight functions' own logs** (`act4_irpt/first_hour_irpt_logs.out`): 52 invocations in the window, 36 of them real traffic after this seat's
  runs (all `irpt-directory-search`); `AccessDenied`, `NoSuchKey`, `Traceback` and `Task timed out` lines: 0 in all eight groups. No error
  event carrying a public reason code in the real-traffic part.
- **The distribution aggregate** (`act4_irpt/first_hour_cloudfront_aggregate.out`; the only series that exists): 641 requests since the first unit,
  5xx 0.00 percent; 4xx 50.23 percent request-weighted, of which 499 requests at 61.92 percent are ONE five-minute bucket (14:13Z, the minute the
  last unit applied); the other 10 buckets hold 142 requests, none above 27 percent. Pre-flip bursts of 150 to 500 requests at 38 to 63 percent
  existed at 11:33Z to 12:18Z (row `ADVI_FIRMBKTS-D1-S39`).
- **What cannot be read:** the router behaviors' origin responses (403 or 404 on a served class) are not separable: logging is disabled and
  there is no additional-metrics subscription. The edge units have not moved, so the router still rewrites served classes to the legacy home;
  a served-class read through the canonical home is the edge leg's. This leg's part of the first hour reads clean on the data that exists.
- **Ownership maps, 15:00:04Z:** EQUAL (legacy VersionId `FcsnGhU7Rt280E9rmDacateI5WiK8S28`, canonical `HXMgugyoEpzWQF_6VFAt.MMOklh53bK2`, 474,841
  bytes, one sha256); `act4_irpt/ownership_maps_1500Z.out`. Reads at 16Z through 21Z follow.
