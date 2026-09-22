# NEVER-WIDEN -- CTO HALF -- mdpf-gold-lambda Cottonwood fix-forward (pin 5991626d4f) -- SIGNED, one condition

**Packet:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NEVER_WIDEN_SIGNOFF_PACKET_MDPF_COTTONWOOD_FIXFORWARD_20260922.md`
**Blob:** `0194edad411b85ce45be6be9814b0c8877cc5191`. I re-derived it with `git hash-object` and it matches the request (msg 99523).
**Signer:** `1.0.0_SA_CTO`, 2026-09-22 ~15:0xZ.
**Scope of this half:** s.2, s.4, s.5, s.6 (including the C rows).
**Authority for the act:** Andrew-direct at the `0.7.0_AE_CloudOps~V` terminal, ~13:4xZ: *"render the necessary fix/fixes, deploy, and issue a manual run."*

Every figure below was re-read by this seat. None is carried over from the packet. Where the instrument differs from the packet's, that is stated.

## s.2 -- LEG A: the pin and its bytes (VERIFIED)

**The zip file**
- `.scratch/mdpf_cot/built_fix2.zip` is 872,699 B.
- `sha256sum` gives `e5a28d1f9581bda84c43cddf63425a34c8ce96aa2aea90803491d588b445c194`, which matches the packet.
- The expected Lambda `CodeSha256` is b64 `5aKNH5WBvahMQ83fY0JaNMjOlqoq6pCANJHViLRFwZQ=`.

**Pin ancestry**
- `74d7efe144` (signed 09-21) is an ancestor of `5991626d4f`.
- Exactly 3 commits sit between them: `47e00fa9ad`, `3756c846a4` and `5991626d4f`.
- `1465fd3f7d` (Andrew's 09-11 null-tail guard) is NOT an ancestor of the running `48b8671569`. The packet's new finding is confirmed: the deployed plane has never carried the guard.

**Member census, a different instrument from the packet's**
- The packet compared 2 of 2 members. This seat unzipped and compared EVERY `.py` member to `git show 5991626d4f:<path>`, with CRLF normalised.
- 24 members in total. **19 of 19 `.py` members are byte-equal** to the pin. `trading_calendar.py` equals `lib/trading_calendar.py`.
- The other 5 members are non-code (manifest and config).

**The running plane, read live**
- `CodeSha256 evIYCXUR...`, 835,383 B, modified 13:25:35Z, `MDPF_GOLD_COMMIT 48b8671569`.
- This matches the packet's baseline.

## s.4 -- LEG B: the synced keys (VERIFIED; one CONDITION)

This seat ran `head-object` on all five keys on `opal-data-mdpf` and compared each ETag against `git show ac571ef0c7:<path> | md5sum`:

| key | ETag vs HEAD | result |
|---|---|---|
| `dim_mdpf_aggregate_aua_timeseries.py` | `3d775af9...` vs `a2b5f598...` | differs: this is the ONE key that changes |
| `mdpf_gold_consolidator.py` | equal | unchanged |
| `mdpf_revamp_model_crosswalk.py` | equal | unchanged |
| `build_cottonwood_mdpf_slice.py` | equal | unchanged |
| `build_cottonwood_mdpf_pair.py` | equal | unchanged |

Current VersionId of the changing key: `FjrdsfCycvPskUPoDXPsBdDggc1WMsy.`, 194,495 B.

⚠ **CONDITION (the push-time grain).** LEG B's write set is set by the diff AT THE PUSH, not by `ac571ef0c7`. A push of CLOUD carries every seat's commits.

This seat read `git diff --name-only origin/CLOUD HEAD` restricted to `data/*/scripts/{gold,silver,bronze}/**.py`. It returned TWO paths:
- the spine;
- `data/mdpf/scripts/gold/tests/test_frontier_lag_trailing_none.py`.

This half covers both branches:
- **(a) The hook syncs only the spine.** This is as the packet states.
- **(b) The hook also syncs the tests file.** That file would be a NEW key that no runner imports. Its rollback is deleting that one key.

**Any OTHER pipeline script in the push is OUTSIDE this half.** The seat that pushes (`0.0.0_AB_MSTR`) prints the hook's synced-key list, and `0.7.0_AE_CloudOps~V` checks that list against (a) or (b) before closing LEG B.

## s.5 -- EC2 reachability today (VERIFIED)

- `i-02448edb624a7a7cf` is `running`, launched at 13:40:23Z.
- Today's chain log `mdpf_daily_20260922_125237.log`:
  - `:245-246` show `ModuleNotFoundError: No module named 'lib.opal_naming'`;
  - `:247` shows `STAGE6-REVAMP rc=1 dur=1s`.
- So the EC2 path reaches no Cottonwood or spine code today, and LEG B stays inert there. The exposure recorded in msg 99490 is unchanged in shape, and after the push it carries the FIXED spine.
- Andrew's LEG B word stands: *"Leave them, cover in the fix"* (msg 99503).

## s.6 -- Rollback, all legs (VERIFIED)

**Rollback versions exist, read with `head-object --version-id`:**
- LEG A: `uYOduyR_y0a0IH8bEnA8Lukn4qQRzcAR`, 835,383 B, 13:22:47Z.
- LEG B: `FjrdsfCycvPskUPoDXPsBdDggc1WMsy.`, 194,495 B.

**Bucket versioning is `Enabled` on all three write buckets:** `opal-data-assets`, `opal-data-portal-v2` and `opal-data-mdpf`. So per-key rollback by prior VersionId is available for the C-gold and C-serve rows.

**LEG C blast radius, both branches of s.3.**

Writers of the named served properties: TWO.
- `mdpf-gold-lambda` writes `portal/gold/mdpf/{4 scopes}x{4 types}` and `_manifests/`.
- `opal-assets-mdpf-portal-publisher` writes `platinum/mdpf/*`.
- The third historical writer, EC2 Stage 6, is dead at import (s.5).

The branches:
- **16 of 16:** 8 keys are rewritten and 8 added. Each rollback is the key's prior version.
- **15 of 16:** `global/account-distribution` is ABSENT, the gate refusing as designed. Nothing is written for that key, so nothing needs rolling back for it.
- **Worst reachable (a crash mid-build):** partial gold writes. Rollback is per key, and tomorrow's 13:30Z fire supersedes.

~~Under either branch, no key outside those two prefixes is reachable.~~ ⛔ **RETRACTED BEFORE COMMIT.**

That sentence is the packet's own claim. This seat copied it after counting only the SERVED writers, which is the
two-writer blindness this seat's own law names. `4.0.0_SA_CRO` (msg 99525, review @`3a9e95a335`) read the production
branch of `run_cottonwood_family` (`mdpf_gold_consolidator.py:1113` @`5991626d4f`). That branch writes THREE
Cottonwood staging keys on `opal-data-assets` BEFORE any portal key:
- `:1206`, bdmp `--upload`: `blackdiamond/cottonwood/gold/dim_model_portfolio/date=<adate>/data.parquet`
- `:1212`, slice `--upload`: `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json`
- `:1216`, pair `--upload`: `gold/mdpf_revamp/cottonwood/<file>`, including the `account_units.json` sidecar that s.3 relies on

Every day's fire already writes these keys, so this is not new exposure. It is a COMPLETENESS gap in the named blast
radius. **The s.6 C-rows are therefore REFUSED in this half as well**, on the same ground and with the same clearing
amendment:
- a C-stage row names the three keys, with `opal-data-assets` versioning (Enabled, read above) and per-key rollback by prior VersionId;
- it names the `adate` the invoke will write (the newest `fact_model_assignment` partition), with that key's prior version as its rollback;
- "two prefixes" becomes "four".

This seat re-signs the C-rows on the amended blob in one read.

## VERDICT

**SIGNED for s.2, s.4 (subject to the push-time condition), s.5, and the LEG A and LEG B rows of s.6.**
**REFUSED for the s.6 LEG C rows, pending the staging-writer amendment above.**

This half does not sign the CRO's sections (s.1, s.3 and s.7). The act proceeds when both halves are on the record.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
