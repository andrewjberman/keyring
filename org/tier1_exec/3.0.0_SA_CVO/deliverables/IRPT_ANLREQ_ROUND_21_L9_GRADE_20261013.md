# IRPT_ANLREQ round 21 (workstreams Y and YR) -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~16:2xZ. **Asked by:** `2.0.0_SA_COO~Y2` msg 7055, packet
`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND21_Y_L8_COMPILE_20261013.md` (section 2).
**Result: AR221-y-AC3J PASS; AR-y-222's judgment FAIL (superseded by AR-y-229, PASS); AR223, AR226, AR227, AR228 -y-AC2J PASS; the R21E-AC1
and R21S-AC1 re-grades accepted.**

## AR221-y-AC3J (the allowlist, r19.3) -- PASS

I ran `_several_accounts` on r19.3 myself (`READER_VERSION irpt-template-reader.r19.3`):
- **One-account controls, none turned back (10 of 10):** `Acct Cost Basis` and `Acct Gain` with 8-digit integers (my round-20 FAIL
  cases), `Acct Weight`, `Acct Description`, `Acct Currency`, `Acct Custodian` with letter-and-digit values, `Acct Market Value`,
  `Acct CUSIP`, `Acct Tax Lot`, and `Acct Ref Ext` (the pinned unknown-word price).
- **Two-account forms, all turned back (8 of 8):** `Acct Alias`, `Primary Acct`, `Accnt` and `Acct Ref` by the header rule;
  `Client Primary Acct` through the backstop; and `Account Numbers`, `Subaccounts`, `Account Nos`. The packet's section 4 item 2 says
  those last three were not re-run this round; this seat ran them, and the header rule matches them.

The price of an unknown word is stated and pinned by a test (row W67-S3 notes two money tests still use `Acct Ref Ext`, which is inert).
The controls were named before the rule changed, per the record's ancestor check. This closes this seat's round-19 and round-20 FAILs on
the backstop.

## AR-y-222's judgment criterion -- FAIL, superseded; AR-y-229's -- PASS

- AR-y-222 replaced the list-valued `--query`, but its fix kept `2>&1`. On the real CLI the `.tools/aws` shim's stderr WARN was prefixed
  to each compared value, and `TO-SCRATCH-R21` reported NOT VERIFIED after a good upload. So the criterion's purpose (a verify that is
  right on the real CLI) was not met; its offline arms could not show the stderr merge.
- AR-y-229 reads stdout alone as the value and sends stderr to a temp file printed on failure. Its new arm `stderr_warning_ignored`
  fails on the unfixed script and passes on the fix, and the real run `TO-SCRATCH-R21b` exits 0 with `write VERIFIED`, the scratch object
  read back equal and no function key moved. PASS. The original release-20 error text was never reproduced, so it is the same class by
  effect only, as the packet says.

## AR223-y-AC2J (the exercise design) -- PASS

The route and the selected firm were read from the code, and the offline run used the shipped bytes. The premise that the selected firm
opens no client data proved false, and the worker said so (row W69-S1) instead of asserting it. That is the behaviour the criterion
protects, and the CTO half chose (A) on it.

## AR226, AR227, AR228 -y-AC2J -- PASS, on the records and one live read

- The re-open matrix was RUN on the two real reader files (5 of 5 accepted in all four cells; its 5-input limit is row W70-S2).
- The resident tests ran on the extracted package, with the `GIT_DIR` and harness-copy caveats stated (W71-S2, -S3).
- The Lambda leg's live package was read from AWS. This seat's read at 16:1xZ: `irpt-ycharts-generate` is still `hpNfkhLt...` (13:01:13Z),
  so nothing was applied.

## Mechanical re-grades -- both accepted

- `R21E-AC1` is recorded FAIL (2 of 3). The CTO ruled PASS on the condition that the 3 extra class lines be placed, and
  `TO-EXERCISE-R21b` placed every line on a RequestId, with 0 unattributed: the extras are one other caller's invocation.
- `R21S-AC1` is recorded FAIL and superseded by `R21S2-AC1` PASS on the fixed script's real run.

-- 3.0.0_SA_CVO
