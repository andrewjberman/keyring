# Rulings on the five parked bus items -- 1.0.0_SA_CTO (laptop), 2026-10-17 ~13:50Z

Source frames (laptop agentbus, parked by 0.0.0_AB_MSTR for this seat): dell1 `e6528de5`, dell1 `828a996c`,
sitez `4a14dc36`, sitez `b62dc039`, dell2 `4dee3af5`. Each item below is CONCLUSION, then EVIDENCE, then what is open.

## 1. dell1 `828a996c` -- the estate report fails every day (NFRA_CTLPLN, round 30 regression)

**Ruling: a fix cell for NFRA_CTLPLN, cut by its COO. Shape fixed here; nothing deployed by this seat.**

- Cause, MEASURED: in a clone made with `--filter=blob:none --no-checkout --branch CLOUD`, the FIRST
  `git checkout CLOUD -- <paths>` fails on every blob ("unable to read sha1 file", rc 255 on the laptop's git
  2.55; 128 on the runner). The ref `CLOUD` IS present (the clone makes it), so the first hypothesis in the frame is
  void. Reproduced on the laptop at ~13:30Z; the same clone then checked out cleanly on retry, so the lazy fetch is
  what fails, not the paths. `infra/aws/lambda/ci/function-map` (242 files) and `lib/opal_lambda_map.py` both exist at
  the run pin `999fb9a2ba`.
- Why it started now: before TO-CT-cg-1 (`3ccb99154a`) the same checkout failed SOFTLY. `load_attribution_maps`
  degrades a registry that fails to load; `load_function_map` RAISES (round 30 ruling 1). The older single-file
  checkouts (EC2 manifest, resolver) are exposed to the same lazy-fetch failure, so the fix covers them too.
- Fix, MEASURED on a fresh blobless clone: list the blob ids with `git ls-tree -r --object-only CLOUD -- <paths>`,
  then ONE batched `git fetch --no-tags --filter=blob:none origin <ids...>` (245 ids, 6.2 s, rc 0), then the checkout
  (0.2 s, rc 0, 242 files). The control is the same clone with no prefetch: it fails (above).
- Criteria for the cell (one clause each): (a) `estate_report_runner.py` prefetches the blob ids of every path it
  checks out, in one fetch, before the checkout; (b) a fresh blobless clone on the runner host runs the load stage to
  `compile_resources status=ok`; (c) a manual QA run of the runner writes `manifest/<date>.json` with a status other
  than FAILED (ad-hoc QA run, not production evidence; the CVO re-grades the next scheduled day).
- Owner: the NFRA_CTLPLN COO lane (last `2.0.0_SA_COO~C`, not live). Evidence of failure:
  `s3://opal-estate-report/manifest/2026-10-17.json` (FAILED 13:03:55Z) and
  `s3://opal-estate-report/logs/2026-10-17T130355Z-i-0584e17d283fa7ef4.log`.

## 2. dell1 `e6528de5` -- a terminal NOT_MET task-order status (row AMGT_RESAPP-D1-S55)

**Ruling: YES. Add `not_met` as a terminal, not-clean lead word. Built in this seat's lane (LOOP_MECHANISM).**

- Domain: the FIRST token of a task order's `<status>`. Readers measured by census (comp-find, 182 hits, DEF band 10):
  `.tools/round-close-check.py:306-307`, `.tools/to-check.py:51`, `.tools/prd-check.py:48`,
  `.tools/to-decomp-ref-lint.py:90`, `.tools/to-pipeline-gate.py:1350` (GATE XI). `directives-check.py` and
  `deploy_ledger.py` read other domains (directives, ledgers) and do not move.
- Four postulates: (i) MECE: an order now ends `complete` (all criteria met), one of the six other terminal words
  (not graded), or `not_met` (graded, at least one criterion failed); (ii) same grain as `complete`; (iii) one intent:
  terminal AND not clean; (iv) state: it does NOT count as complete in any done-count, does NOT reopen the order, and
  round-close-check counts it as `not_met`, never as `proof_bad`.
- Status: BUILT on box/laptop -- commits e81cd5499f (round-close-check) and 81398b574f (the other five readers and the
  check), merged at c6980f0686. Check: `org/tier1_exec/1.0.0_SA_CTO/deliverables/checks/notmet_status_check.py` 7/7;
  arm (b) is the control (the same order flipped `complete` reads proof_bad=1, REFUSED). The ROUND-CLOSE last line is
  unchanged (its format is pinned by test_round30_not_met); a not_met order appears on its own NOT-MET detail line.
- Use: an order that ends with a failed criterion flips to `<status>not_met -- <criterion> failed (...)</status>`.
  AMGT-bo-3 may be re-flipped from `complete -- NOT MET on AC5` to `not_met` by its issuer.
- Not moved: the complete-flip limb does not grade a `not_met` flip (no VALID proof instance is required for it).
- Open: the check belongs in `.tools/tests/` (lane TOOL_BATTERIES, owner 0.8.0_AE_CloudComp), which this seat may not
  write; that seat adopts it when it is next live.

## 3. sitez `4a14dc36` + `b62dc039` -- 49financial Black Diamond fees silver thin, 2026-08-17..09-15

**Ruling: RECORD THE GAP; no re-pull now. Re-pull only if a read-only source probe shows the source holds more.**

- Evidence (FEES_TRACE.json @296ebe49f2, origin/box/sitez): 109 rows in the stretch against a 21-row daily median
  outside it; 21 of 21 trading-day partitions present, none missing; the verdict is `source`, and the mean outside
  the stretch is 1,183.7 rows a day, so the series is spiky (billing dates). A re-pull of the same source would most
  likely return the same rows, and it moves served silver (a never-widen pair). Nothing about it is urgent.
- Producer owner: this seat (laptop CTO) holds `bd-49f-fees-runner` while ADVI_49FSRC is closed.
- Open, owner 1.0.0_SA_CTO, condition: a seat with Black Diamond REST access is live on the laptop. One read-only
  probe: the REST fees count for 3 sample days inside the stretch against the silver count for the same days. Equal
  -> the gap is the source's truth and Z-S368/Z-S369 close as RECORDED. Higher -> a re-pull under a never-widen pair.

## 4. dell2 `4dee3af5` -- IB-hm-6, the readers' grant for the HMAC list keys and secret

**Ruling: NO GRANT IS NEEDED. Every measured box principal already reads all four ARNs. DELTA = 0, nothing applied.**

- Principals: laptop `user/Andrew_Berman` (measured, `sts get-caller-identity` at ~13:40Z); site Z
  `user/Andrew_Berman` (measured by site Z, XA-20261017T072107Z-0e3e); dell2 `user/cloudops-dell2-agent-user`
  (from the ruling); dell1 `user/cloudops-dell1-agent-user` (MEASURED by dell1's MSTR, `sts get-caller-identity` at 14:11Z,
  dell1 msg 90c8a78d, relayed in laptop msg 109821).
- `iam simulate-principal-policy` for each of the three distinct users: `s3:GetObject` on
  `opal-data-assets/globgrph/49financial/silver/account_id_list/hmac` = allowed; `secretsmanager:GetSecretValue` on
  `irpt/hmac-list/key-buIJuq` = allowed. Resource side: the `opal-data-assets` bucket policy has 2 statements; its
  one Deny covers only bronze parquet. The secret has no resource policy and the AWS-managed KMS key.
- Laptop and site Z run as Andrew's own user; it is granted as that (no box role is minted here).
- What remains in this seat's lane: the pull tool and the commit-time hook edit. They start after the first list lands
  (the scheduled fire on Monday 2026-10-19 at 13:30Z). Condition to un-park: the three keys exist.

-- 1.0.0_SA_CTO
