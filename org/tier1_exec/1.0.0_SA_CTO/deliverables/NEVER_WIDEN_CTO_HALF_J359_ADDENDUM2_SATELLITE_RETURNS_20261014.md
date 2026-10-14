# NEVER-WIDEN SIGN-OFF -- CTO HALF -- J359 addendum 2: satellite trailing returns = the models' realized returns blended with GLD

**Signer:** `1.0.0_SA_CTO~DELL1`. **Counterpart:** `2.0.0_SA_COO~J1`, COO half
`org/tier1_exec/2.0.0_SA_COO~J1/deliverables/NEVER_WIDEN_J359_ADDENDUM2_SATELLITE_RETURNS_COO_HALF.md` @`5500bce348` (branch `wk-remote-J359b`),
**sha256 `800adb5434b6225e01ff6c1b05a395f61d85f80f393b783a217cbeba318a0740`**. This half signs those bytes; any other bytes re-open it.
First pair (scalars, unchanged by this act): COO @`e1dfba9db8`, CTO `NEVER_WIDEN_CTO_HALF_J359_SATELLITE_CHARACTERISTICS_20261014.md` @`2b6f842af2`. Pure ASCII.

## 1. WHAT I READ (each a byte read, never a self-report)

| item | read | result |
|---|---|---|
| IAM patch `J359_evidence2/benchmarks_read_grant.tf.patch` @`5500bce348` | `git show` piped to `sha256sum` | `0391a7d9...d738`, equal to the COO half. ONE element added to Sid `ReadServedPositioningData`: `opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json`, `s3:GetObject` only. No ListBucket, no prefix, no Put, no new bucket |
| producer `build_satellites_characteristics.py` @`7337fdfa6d` vs deployed pin `efb3f6550f` | `git diff --stat`; `model_blend_returns` body read in full | 1 file, +141/-75. The rule is as the COO half states. `load_benchmarks()` has no fallback. `validate()` refuses a satellite whose every window is NULL. A null GLD publishes the model part and is named in `returns_note`. g = 0 publishes the model average |
| verifier output `J359_evidence2/verify_producer_returns.out.txt` @`5500bce348` | tail read | 9 of 9 satellites OK against the oracle. Difference control: 26 tickers equal; 9 x (total_weight, sources, 4 scalars, window keys) equal. Null-GLD arm OK. Negative controls: 1 and 9 refusals. `VERDICT: RETURNS-RULE-OK` |
| writers of the key | the COO half's census (s.4), unchanged from the first pair, which I counted at @`2b6f842af2` | **N = 1** (`publish()`; the one PutObject statement pinned to the key) |

## 2. ONE REACHABLE STATE THE COO HALF DOES NOT NAME (covered here, not a refusal)

**A window where only some of a satellite's sleeve models have a return.** `model_blend_returns` skips a model whose `returns[w].model` is
null and divides by the weight of the models that are present (`den` = the sum of the present sleeves' weights). So such a window publishes the
average of the PRESENT models re-weighted to 100%, not NULL. The artifact records it: `contributors.returns.windows[w].models` lists exactly
the models used. That is the producer's own rule, and the record is in the artifact, so this half accepts it under **condition C4**.

## 3. CONDITIONS

- **C1 -- the build.** The producer members are exactly the COO half's s.3 candidate column (`7337fdfa6d`), and the plan is exactly the patch
  (sha256 `0391a7d9...`). It shows one Resource element added and the function's `s3_object_version` / `source_code_hash` changed, nothing
  else. Anything more is NOT SIGNED, and nothing is applied.
- **C2 -- the windows check (first pair's C2, kept).** Before any portal step, for every `bbg` ticker in the served `tickers` block at the
  run's `bbg_as_of`, print the windows under the deployed rule beside the candidate's. A move not explained by a changed input is Branch B.
- **C3 -- the clock (first pair's C3, kept).** No leg straddles the dell1 restart at 21:00Z. The order starts the deploy leg only with at least
  45 minutes left. At this signature (~20:05Z) that means it starts by 20:15Z or waits for the re-seat. Either is covered.
- **C4 -- partial sleeves.** The served read prints, for each satellite and window, `windows[w].models` beside the satellite's registry sleeve
  codes. Every window built from fewer than all of its sleeve models is NAMED in the receipt. That is Branch A. It becomes Branch B only if a
  model's return is present in the benchmarks object at the run and still missing from `models` (the reader dropped a model it had).
- **C5 -- the portal.** The two-sentence deletion (COO s.7) is on a page CW can open, so it is client-facing and waits on Andrew's word after C2
  and C4 are read. It goes through `portal-merge-forward.sh` on an approved row, then the dell1 DT (`0.4.0_DT_ClientPlatform~H1`) by
  `portal-release-build.sh`.

## 4. BOTH BRANCHES AND THE ROLLBACK

These are as the COO half's s.6 states them, which I adopt. **A:** served artifact per s.1 (only `returns`, `returns_note`, `contributors.returns`,
`method`/`inputs` move; `coverage` removed), the rule unchanged, and C2 and C4 printed. **B:** before the apply, nothing is written. After
the apply and before the invoke, re-point the function to the prior artifact (VersionId `3yaAgYL1...`, CodeSha256 `mpFb3up8...`) and revert
the `.tf`, the same session. After the invoke: `copy_object` from the version read at the cut (a new version, never a delete), read back
byte-equal, plus the re-point and the grant revert, and a row filed. The change-management ledger entry opens before the apply and closes with
proof (NEVER-2).

**Not signed here:** the portal promote (C5); the Satellites 90/98 GLD-in-holdings question (Andrew's, raised by this seat; it does not gate
this act, because g = 0 publishes the ULT models honestly); the benchmarks object's own writer; any monitor or alarm.

## 5. SIGNED -- CTO HALF GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       J359 addendum 2: producer code + artifact + one READ-only IAM element; dry-run, then ONE driven invoke
KEY       s3://opal-data-cot/platinum/satellites/characteristics.json ; N = 1 writer
BINDS     COO half sha256 800adb54...0740 @5500bce348 ; build 7337fdfa6d ; patch sha256 0391a7d9...d738
CONDS     C1 build/plan exact ; C2 bbg windows side by side ; C3 no leg across 21:00Z (start >= 45 min before) ; C4 partial sleeves named ; C5 portal on Andrew's word
COO half  2.0.0_SA_COO~J1, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-14 ~20:05Z
```

-- `1.0.0_SA_CTO~DELL1`
