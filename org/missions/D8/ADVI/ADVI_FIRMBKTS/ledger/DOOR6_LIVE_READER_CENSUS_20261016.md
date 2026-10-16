# ADVI_FIRMBKTS Door 6 -- the live deployed-code census of the marker's readers (`2.0.0_SA_COO~B1`, 2026-10-16 ~19:4xZ)

**Asked by:** CTO erratum 1 (`ledger/CTO_DECISION_DOOR6_RETIREMENT_ORDER_20261016.md`, msg 6996): read every Lambda's deployed code package for `pipeline-complete`, not by name, denominator printed; read the runner scripts in `s3://opal-data-inf/code/runner/`; any live reader found gets its own step before step 3; if zero, step 1 drops. Read-only. Tool: `deliverables/2.0.0_SA_COO~B1/round9/door6_live_reader_census.py` (rerunnable); its record: `deliverables/2.0.0_SA_COO~B1/round9/DOOR6_LIVE_READER_CENSUS.json`. The needle is the string `pipeline-complete` (it matches the key and its failure sibling's text).

## 1. Lambda functions (deployed packages, 2026-10-16 ~19:2xZ)

Denominator: **244 functions listed; 240 zip packages downloaded from each function's `Code.Location` and searched member by member; 0 download errors; 4 container-image functions NOT scanned** (`opal-news-ai-sentiment`, `daily-sprint-generator`, `news-semantic-clustering`, `ycharts-session-capture`). Environment variables of the 240 were searched too: 0 hits.

**16 of the 240 contain the string; none reads the key.** Each hit line was printed and read:
- 8 functions bundle the vendored LGIC registry JSON (`infra/logic/registry/event_rules.json:78-79`, `key_rulings.json:436-438`): data rows that describe the key (`rivalfunds-publish-page-lambda`, `outlook-global-commentary-draft-lambda`, `rivalfunds-build-canonical-shape-lambda`, `rivalfunds-build-silver-lambda`, `etfs-rivalfunds-daily-lambda`, `etfs-rivalfunds-fetch-holdings-lambda`, `teams-global-transcripts-pull-lambda`, `outlook-global-transcripts-pull-lambda`; the first one's lines were printed, the other seven share the same file and line numbers).
- 4 `opal-assets-silver-{etf,blackdiamond,eclipse,orion}`: `mirror_conversion.py:12`, a comment: "nothing here writes -- or can write, the role fences it -- opal-data-inf/gold/meta/pipeline-complete.json (Door 6)" (all four lines printed).
- `opal-assets-ingest-mirror` (`lambda_function.py:58`) and `etfs-netassets-daily` (`:58`): comments about the role's Deny and the held chain.
- `inf-etf-ownership-daily` (`:14`): a docstring about a reversed trigger.
- `inf-portal-publisher` (`lambda_function.py:5`): the docstring "Triggered by: S3 ObjectCreated on opal-data-inf/gold/meta/pipeline-complete.json". It is documentation only: the publisher's trigger moved to the Scheduler in `FB-l-5`, and its deployed code does not read the key (the match is on line 5, in the module docstring).

The deployed `inf-gold-trigger` has 0 matches (row `D1-S61`).

## 2. Deployed scripts under `s3://opal-data-inf/code/` (read for the marker)

The CTO named `code/runner/`; it holds 2 objects (`run-gold-layer.sh`, `inf-gold-layer-runner.service`), both with 0 matches, and `run-gold-layer.sh` is byte-identical to the repo copy. **The gold dispatch script is not there: its deployed copy is `code/gold/orion-gold-dispatch.sh`** (113,445 bytes, last modified 2026-10-16T16:33:27Z). So the whole `code/` prefix was read: **271 objects listed (no continuation token), 271 downloaded, 0 errors, 4 with the string:**

| object | modified | what it is |
|---|---|---|
| `code/gold/orion-gold-dispatch.sh` | 2026-10-16T16:33Z | **the live writer**: the success-guarded `aws s3 cp - .../gold/meta/pipeline-complete.json` is at line 1906 of this deployed copy (and the failure sibling at 1919) |
| `code/gold-staging/orion-gold-dispatch.sh` | 2026-06-30 | a second copy that writes the marker (line 1575) |
| `code/rebuild/orion-gold-dispatch-rebuild.sh` | 2026-07-01 | a third copy that writes the marker (line 1574) |
| `code/rebuild/inf_rebuild_runner.sh` | 2026-07-01 | line 6 is a comment ("no live pipeline-complete.json"); not a reader or writer |

## 3. What this means for the order (read; the decisions are the CTO's)

1. **No live reader of the marker was found** in 240 Lambda packages, their environments, or 271 deployed scripts. By the CTO's rule step 1 drops, with the limits in section 4.
2. **Three deployed copies can write the marker, not one** (the writer count for the never-widen rule is N=3). Only `code/gold/` is the live one by the evidence read (modified today; the others are June and July). Stopping the write in `code/gold/` leaves the other two able to rewrite it if anything ever runs them.
3. **The repo copy is not the deployed copy** (repo `data/inf/scripts/gold/orion-gold-dispatch.sh` 119,270 bytes, deployed 113,445; sha256 prefixes `70b577442...` and `e9aef66bc...`, LF-normalized). The repo file carries edits from other projects (IRPT, 10-15 and 10-16) that are not deployed. The census's line `:1906` was correct for the DEPLOYED copy and is wrong for the repo copy (the same block is near line 1976 there). **Step 3 must change the deployed bytes' marker block only; deploying the repo copy wholesale would ship other projects' unreviewed edits.**
4. The step 3 precondition the CTO set ("after reading the deployed runner copy") is met for the live copy by this read.

## 4. Not read (named)

- The 4 container-image functions; Lambda layers; a key built from parts that never spell `pipeline-complete`.
- Non-Lambda readers: ECS task images, Step Functions definitions, Glue scripts, EC2 user-data, and any code outside `s3://opal-data-inf/code/`.
- S3 access logs and CloudTrail data events for reads of the key (the census did not query them either).
- Whether anything ever runs the staging and rebuild dispatch copies.
