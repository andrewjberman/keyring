# Never-widen sign-off packet -- Y-4, the check gate: the runner role's read of the estate Kimi key, the resident (st16 -> st17) and irpt-ycharts-generate, all at ONE commit `828c37c6f7`

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~02:4xZ.
**Authority:** CTO rulings batch 178, ruling 5: "The check gate offers a typo's likely ticker". Kimi is VEW-3, "can be called
freely" (`org/ref/VENDOR_EGRESS_WHITELIST.yaml`); YCharts is under Andrew's word for these cases.
**Ledger:** `irpt-y4-20261003`. It was opened ~02:3xZ, AFTER the U1 upload: the first `open` was refused on an invalid leg
kind (`tf-iam`) while the build ran. The ledger records this. U1 and U2 are closed; D3, D1, D2 and V1 are open.
**Three moves**, in one window: D3 (IAM), D1 (generate code), D2 (resident). Roll back all or none. **V1 needs the YCharts
session**, which is EVICTED (S288): it runs after option A.

## 1. What ships

**The code:** `8f408b4e14`, merged `828c37c6f7`.

| file | change |
|---|---|
| `intake/upload_suggestions.py` (NEW) | `suggest_for`: for each TICKER_NOT_FOUND row (at most 6 per upload), Kimi's "check" is asked with the file's other symbols as context. One securities_info batch verifies the suggestions. Only an exact, feature-free FOUND rides the finding as `suggestion {symbol, source, provider_receipt_sha256}`, with ACCEPT_SUGGESTION first. Any failure leaves the finding as the freeze wrote it |
| `ycharts/generate/kimi_port.py` (NEW) | the estate's transport pattern: one JSON POST to Moonshot, the key read BY NAME once into memory. The closed failure codes. Journal telemetry with sizes and hashes only, never the key, prompt or answer |
| `ycharts/session/resident_session.py` | `kimi_advisory()` |
| `intake/uploads.py`, `intake/upload_resolution.py` | an optional `suggest` port, applied ONLY when the resident's resolve ends NEEDS_CORRECTION. The Lambda composes none |
| `ycharts/generate/resident_worker.py` | `_check_gate` composes the port (None when the session has no advisory) and journals `IRPT_RESIDENT_SUGGEST asked= suggested= verified=` (counts only) |
| `ycharts/resident.tf` | the runner role gains `secretsmanager:GetSecretValue` on ONE secret, the estate's `astn/kimi/api-key-*`. It is under the AWS-managed key, so no kms grant |

**The cross-root grant, named:** the secret belongs to the estate-report root (`infra/aws/terraform/estate-report/instance.tf`,
ESTATE_KIMI_SECRET_ID). The runner reads it; it never writes it. A key rotation by the estate is picked up at the next process
start (the key is cached per advisory).

**Artifacts (U1, U2 closed):**
- **The generate zip:** version `w2yfeweDcOFLnVFLFidK1_VCv5EFPCmb`, 588,963 bytes, sha256
  `fD2R6OFrT2N086C9Go3e1aA9RKZCP/vfnZCaHCloJTs=`.
  - It was built from an LF checkout. All 114 members equal `git show 828c37c6f7`: 113 by the census, and
    `kimi_port.py`, newly registered in `files[]` for the parity check, byte-equal by a direct read. 0 CRLF.
  - Vs live `aug0YyWc..`: identical 110, changed 3 (`resident_worker.py`, `upload_resolution.py`, `uploads.py`), added
    `kimi_port.py`. The Lambda composes no suggest port, so its answers are unchanged.
  - Cold-start smoke PASS on its three routes.
- **The resident tar:** `irpt-resident-828c37c6f7-st17.tar.gz`, sha256
  `213c2ebd043cc0edcd9252eb30393d545f60e832a14920a2aeb1e28d18fc1c22`, 787,331 bytes, S3 version `HvfsVMjjD9_YdfKgEXXevpjBDiR321Ux`.
- **The install script:** sha256 `d1f7f89d18751e09dc8a12d1e874738d019d1d89b646681a286942e6b4d9da92`, S3 version
  `uyayvbDZy_BZXx5rUoshEVXp2knZ6jeq`. Both keys read 404 before the upload.
- **The gate:** G1-G5 PASS; G5 vs the running st16: changed 5, added 2 (the two new modules), removed 0.
- **The full ycharts plan** (`Y4/plan_ycharts_full_y4.txt`): 2 changes, the runner policy (+ `ReadTheEstateKimiKey`) and the
  generate code.

## 2. Blast radius

| path | after |
|---|---|
| an upload whose resolve has no TICKER_NOT_FOUND row | unchanged: no Kimi call, no extra read |
| an upload with not-found rows | at most 6 Kimi "check" calls (120 s budget each, up to 2 attempts), then ONE securities_info batch for the suggestions. A verified suggestion rides the finding; nothing is substituted until the user accepts it (a Y-5 correction) |
| a Kimi or secret failure | the finding stays as the freeze wrote it; the journal names the attempt's outcome |
| the generate Lambda | no suggest port: the same answers as today |
| the runner role | reads one more secret (the estate Kimi key); nothing else |

## 3. Proofs

**Offline:** `ycharts/generate/tests/test_y4_check_gate.py`, 14 tests:
- the verified suggestion, with accept first and a context that never holds the row's own symbol;
- six shapes that leave the finding untouched; the cap;
- the transport: key read once as a bearer, three failure classes, the timeout, the absent key, no key, prompt or answer
  in the journal;
- the resident end to end: typo APPL gives one resolve read plus ONE verify read, AAPL is offered, and the accepted
  correction normalizes without a new file; without an advisory, the resolve is exactly as before.

Negative control: on HEAD's modules the tests cannot import. Suites: the same 13 pre-existing failures as HEAD, 1137 passed.
fmt and validate are clean.

**V1, after option A:** the typo file from the page. Row 2 (APPL) offers AAPL, verified. Accept, then NORMALIZED, then a
READY Overview. The journal shows `IRPT_RESIDENT_KIMI` attempts and `IRPT_RESIDENT_SUGGEST asked=1 suggested=1 verified=1`.

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read:**
   - generate `aug0YyWc..`, the key's latest `w2yfewe..`;
   - root `34088050e0-st16`;
   - queue 0/0, no non-terminal job, the lease empty.
3. **D3:** a targeted plan of `aws_iam_role_policy.runner_resident` (the one added statement); ONE `HALT_ACK=1 safe-apply`; the
   policy read back.
4. **D1:** a targeted plan of the generate function (code only); ONE `safe-apply`; CodeSha256 read back `fD2R6OFr..`; the
   cold-start smoke live.
5. **D2:** `head-object` of the script key printing `uyayvbDZ..`; `Y4/install_fetch_and_run.sh` over Systems Manager (sha256
   `d1f7f89d..`). Read back: root `828c37c6f7-st17`, the st17 digests, unit active, queue 0/0.
6. V1 after option A.

## 5. Rollback

- **D1:** re-promote S3 `oew.wOPKuZQKvi30OCFECa5x7Dk_9MOL`, then a targeted apply. The code returns to `aug0YyWc..` (Y-5).
- **D2:** root `34088050e0-st16` stays on the host; the install script's rollback branch restores it.
- **D3:** a targeted apply with the statement removed.

## 6. Not claimed

- Kimi's suggestion quality: each suggestion is advisory and provider-verified; V1 runs one live typo.
- Kimi swap suggestions (packet 2): they wait on the web-search QA receipt (`KIMI_WEB_SEARCH_UNVERIFIED` stands).

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-03 ~02:4xZ, on this packet's bytes at the commit that carries it. The write set is one IAM policy statement,
one Lambda code update, and one resident root with its unit's ExecStart and cutover receipt. The blast radius is section 2.
The rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
