# AMGT_HARVST round 97 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-18 16:0xZ. **Round class:** WORLD (one Lambda deploy by Terraform, two gold-object writes; the other two cells are code with offline tests and a read-only census). **Authority:** the CTO's round-96 analysis (`ledger/ROUND_ANALYSIS.round96.md` @db6c34a7cc, msg 8092): the four legacy raw objects stay in place (no migration, rename or delete); the `pull_enqueue` Lambda writes the canonical spelling; the BP dossier is rebuilt only if a census shows a served field would move.
**Push state of everything cited (measured 16:02Z, `git ls-remote`):** `origin box/dell1` = `3abc50669e06`; this round's later commits (the close `7ab32562b3` and this packet) are LOCAL (the integrator pushes; a hook bars this seat's push). `origin/rel-amgt-harvst-ck3` = `922ee425fea4`. The Lambda is not in a git ref of its own: the merge `349e7ee0da` carries its source. `6575999df5` and `3b94a83e05` are still not in `origin/CLOUD` (site Z lands them in its round 43; MSTR carries it). The objects of `cl-4` are in the harvest bucket, not in git.
**Gate reads:** `round-close-check --project AMGT_HARVST --round 97` = `orders=4 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise` = `armed 1` (`D1-W171-S3`), `defects 0`.

## THE ROUND IN ONE LINE

**4 of 4 orders terminal. The `opal-research-pull-enqueue` Lambda now writes a slash ticker's status object under the canonical prefix (deployed 15:24Z, ledger CLOSED 15:40:17Z: the one real invoke for `BP/ LN Equity` wrote `packs/BP-SLASH-_LN_Equity/status.json` and nothing under the raw prefix), and the two slash dossiers were added again after the 13:02Z model blocks (BP 15:51:21Z, NG 15:54:12Z, ledger CLOSED 15:58:39Z; only `model_rows` moved for each).** One thing is NOT shown: the box consumer has not drained the queued BP pull request in 33 minutes, so the REQUESTED to LANDED path for a slash ticker has not been seen end to end.

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-cl-1` | the Lambda's code: a stdlib copy of `crosswalk.slash_safe_key`, the status key built through it, the raw key kept in the status body and the SQS message, a refused key a 400 before any write; offline tests with a mutant; no deploy | worker `~174` (`5df3755664`, proof `34e78a930d`; merged `349e7ee0da`). I re-ran AC1 (`16 passed`) and AC2 (`22 passed`) and read the 26-line diff; `lambda_function.py` md5 `45c83ddf74640e90368e8bebf712b52c`. The worker's first AC2 was `1 failed, 21 passed`: MY provisioning error (section 4). Row `D1-W174-S2` accepted: a slash-free ticker the shared rule refuses now gets a 400 with zero writes (the box consumer's own call of the rule refuses it too) |
| `HVST-cl-3` | a no-write census of what a dossier rebuild of `BP/_LN_Equity` and `NG/_LN_Equity` would move after the 13:02Z data, with the CTO's model-block guard | worker `~175` (`ed5d5db57e`, proof `736d60a092`; merged `b8014771a1`). I RE-RAN the census (768 requests, read-only): committed output unchanged. Both names would move exactly ONE field, `model_rows` (cause `model_block`: BP cites the block `20261017T130241Z`, the build `20261018T130249Z`; NG `...130649Z` against `...130703Z`); the guard passes (91 and 91 valued rows for BP, 64 and 64 for NG); no `cause=other`. The guard read the model-block status through `dossier._model_block_read` because `build()` returns no such field (row `D1-W175-S2`); the CTO confirmed that read in his `cl-4` half |
| `HVST-cl-2` | the Lambda redeployed by Terraform only, plan read first, one side-effect-free refusal probe and ONE real invoke through the queue (the CTO's ruling in his half: my recommendation of no was overruled) | seat SC1; pair COO half `a72a3823...` and CTO half `5e345c92f5`; `build-and-upload.sh`, plan 15:20:30Z (53 resources, 52 no-op, ONE in-place update of the function: `s3_object_version`, `source_code_hash`, `last_modified`), `safe-apply` 15:24Z, plan after "No changes"; ledger CLOSED 15:40:17Z (`1a3c10badf`). I read the plan before the apply landed and `cl2_after.out`: `CodeSha256` equals the new zip, the deployed entry's sha256 equals the source's, byte for byte; the refusal probe (the `ZZ-SLASH-PROBE` ticker) returned the 400, the queue stayed at 0, no object written; the real invoke returned 202 and the status object sits under `BP-SLASH-_LN_Equity` only; `cl2_served.out` five PASS |
| `HVST-cl-4` | the two slash dossiers added (add-only, BP first as the canary), under the `cj-5` shape and the CTO's added condition (the guard's block key equals the written object's model-block input) | seat SC1; site Z CTO CLEAR 15:22Z for 90 minutes; pair COO half `512874fb...` and CTO half `de80883964`; BP written `...b8aef145b89bc510.json` and NG `...255bb27c74280fb6.json` under the encoded partition; ledger CLOSED 15:58:39Z (`3b1a44e7b6`). My own read-only script (`deliverables/2.0.0_SA_COO_W1/round97/cl4_issuer_verify.out`): 1558 objects (1556 + 2), 446 continuations unchanged, both picks name the manifest key, hashes recompute equal, moved fields exactly `model_rows` for each name; my gateway reads: NG (raw spelling) and BP (encoded) return the new `dossier_key`, the whole record |

## 2. The real run (read by the issuer)

- **The Lambda:** deployed bytes equal the merged source; the refusal probe and the real BP invoke as above. The status object `packs/BP-SLASH-_LN_Equity/status.json` (190 bytes, `security_key` the RAW `BP/_LN_Equity` in its body) is the only status object; `packs/BP/_LN_Equity/` holds only the 09-25 `input_ledger.json`.
- **The dossiers:** the gateway after the writes returns for `NG/_LN_Equity` and `BP-SLASH-_LN_Equity` the new `dossier_key`, `method_version` `amgt-corpus-dossier/15`, the continuation, the ai_fill blocks, the reports and the roster. BP's listed dossier count is 17, NG's 16.

## 3. What is NOT established or NOT closed

- **The consumer has not drained the queued BP pull request** (my read at 16:00:29Z through the `.tools/aws` shim: the SQS queue `opal-research-pull-requests` holds ONE message; the status still reads `REQUESTED`, `updated_at` 15:26:59Z). I did not read whether the box consumer is meant to be running today, or whether the Bloomberg queue's budget refuses it. The message is a real BP pull request through the Bloomberg queue; it will be drained whenever the consumer runs. I did not purge it (a delete) and did not touch the consumer. Rows `D1-S63` (SC1's) and nothing of mine; I had drafted a duplicate row and removed it before committing.
- **`model_rows` through the gateway for either name was not read by me** (the responses are large); the move is proved at the S3 level by my script and by SC1's reads. SC1 reports the gateway returns `model_rows`; my COO half of `cl-4` said the size cap omits it: that was wrong for these two names, corrected in the order note.
- **NG after the write is the gateway's answer to my one read, not a before and after;** SC1 read it by reading, not by script (its own limit). The census covered two names, as ordered; the other 75 names' dossiers were not examined.
- **Three copies of the slash-key rule now exist** (`crosswalk`, the gateway's `harvest_keys.py`, the Lambda's `_slash_safe_key`), each guarded by an equality test over the same 105-key fixture; the cross-adjudication XA-20261018T094750Z-cbaa (call `48ae`, row `D1-W171-S3`, still ARMED) rules where the rule lives.
- **The Lambda has no source-map row** (`D1-S62`, SC1's): `record-terraform-deploy.sh` refused to stamp its deploy; the deploy is verified by the reads above; not fixed (outside SC1's paths).
- **The dossiers fall one day behind again within hours:** the model blocks of both names land about 13:0xZ every day (stamps 10-17 and 10-18); this round's write brought them level with 2026-10-18's block and does not change that. The CTO's round-98 candidate is a scheduled refresh with the census and guard built in.
- **The four legacy raw objects** stay in place (the CTO's ruling) and are recorded SUPERSEDED in the `ck-3` order with each key, size and timestamp.
- **The Lambda's artifact rollback:** the previous artifact version `pHqpZEyjzx1PPaeKAGgJUIB.1hQUU.v2` is still stored; not taken.

## 4. My errors, corrected in the record

- **`cl-1`: I gave worker `~174` a wrong sparse path** (the RESAPP deliverables folder under `AMGT_HARVST/` instead of `AMGT_RESAPP/`), so an existing test's file was absent and its first AC2 read `1 failed, 21 passed`; my provisioning check counted output lines and hid the error. I fixed the sparse set and re-ran. The third provisioning miss of mine in this workstream (round 92 `cg-5`, round 95 `cj-2`): from now the check prints each file by name and fails on any miss.
- **`cl-4` COO half: I wrote that the gateway's size cap omits `model_rows`**; SC1 read it returned. Corrected in the order note.
- **A claim I nearly recorded: "the queue message was drained within 30 seconds"**: the queue count 0 was the message's visibility, not its consumption; SC1's later read (queue 1) and mine (16:00Z) show it never drained. I caught it before it reached a row.
- **A duplicate row id:** I appended a row numbered `D1-S62` while SC1's uncommitted `D1-S62` and `D1-S63` were in the file; I read the diff, saw the duplicate and removed my row (it also duplicated `D1-S63`), so only SC1's rows remain. I should have read the channel's tail first.
- **Decisions:** I accepted the Lambda's new 400 for a refused ticker (`D1-W174-S2`) and carried it into the pair; I sent the `cl-4` GO at 15:23:11Z, one minute after site Z's CTO CLEAR, with "start only after `cl-2` is closed" so one seat never ran two orders, and kept `ca-5` (the RESAPP COO's order) behind `cl-4` by agreement with the RESAPP COO. I typed a nudge to an idle SC1 at the `cl-2` GO (read 8 seconds later) and did not nudge a busy SC1 for the `cl-4` GO (read at its next leg boundary, 20 minutes).

## 5. The rows

SC1's: `D1-S62` (no source-map row), `D1-S63` (the BP request not drained). The workers': `D1-W174-S1` (blocking, resolved by my sparse fix), `-S2` (accepted), `D1-W175-S1` to `-S3` (INERT: the census summary, the guard read through `dossier._model_block_read`, the stale `_pick_dossier` line numbers and the HEAD provenance). Mine this round: none filed. `comp-surprise`: armed 1 (`D1-W171-S3`), defects 0.

## 6. For the slug (candidates for round 98; the CTO rules)

1. **The scheduled dossier refresh** after the daily model-block landing, with the `cj-4` census and the guard built in (names outside the allowed moves skipped and reported), under its own pair: the CTO's candidate.
2. **The box consumer and the queued BP request:** is the consumer meant to be running; if not, the queued message is a standing real pull request; whether to leave it, start the consumer, or have Andrew word a purge.
3. **The release refs reaching `CLOUD`** (`6575999df5`, `922ee425fe`, the Lambda's merge): site Z's round 43 and OG-ap-42 (MSTR carries it).
4. **`D1-W171-S3`** (call `48ae`): now three copies of the rule.
5. **The Lambda's source-map row** (`D1-S62`): a small repair, not mine.
6. **`D1-S51`:** the idle-seat instances (the `cj-3`, `cj-5`, `ck-3` and `cl-2` GOs were read only after a typed nudge or, for `cl-2`, 8 seconds after it) and the busy-seat reads (`cj-4`, `ck-3` order, `cl-4`); whether an armed watcher wakes an idle seat is still untested.

-- 2.0.0_SA_COO~W1
