# AMGT_RESAPP round 63 -- the memory-only act to 1769 and am-7 AMENDMENT 3's three officer objects -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Date:** 2026-10-02
**Task Order:** AMGT_RESAPP.TO-AMGT-am-6 (memory-only act), AMGT_RESAPP.TO-AMGT-am-7 section 8 (AMENDMENT 3)
**Status:** COMPLETE -- both acts landed and graded; am-7's AC1 now passes outright.

Delta since `380d078abb`, which covered am-6 legs 1 and 2 and am-7's first four keys.

## Objective

Two further ordered acts, each on its own never-widen pair and NEVER-2 entry: drop `memory_size` to 1769 on
the CTO addendum that my own flat-curve measurement produced, then write the three officer objects that
Andrew's one Bloomberg pull finally made possible.

## Compiler Tools

| Tool | Invocation | Result |
|------|-----------|--------|
| `git show <pin>:<path>` | the addendum @`4d0f049203` and both A3 halves | PASS. Authority verified by PRINTING THE BYTES at the pin, never by grepping for the quote. |
| `terraform plan` / `show -json` | memory act | PASS. 49 `resource_changes`, 1 non-no-op, ONLY differing attribute `{memory_size: 10240 -> 1769}`, `source_code_hash` UNCHANGED. |
| `.tools/safe-apply.sh` | one memory apply | PASS. 0 added, 1 changed, 0 destroyed; re-plan `-detailed-exitcode` 0. |
| `terraform fmt -check` / `validate` | after the tf edit | PASS. fmt clean, validate Success. |
| `boto3` S3 | 3 PUTs + head + get + list | PASS. All 3 NEW, read-back by content 3 of 3. |
| `r63_served.py` c2/c3/c4/c5 `--where deployed` | literal invocations | PASS. c3/c4/c5 unchanged at 1769; c2 now exit=0 SERVED YES. |
| sort assertion in code | the key-order claim | PASS. 3 of 3 new keys sort last, discriminating bytes printed, fabricated-key negative control. |
| `.tools/deploy_ledger.py` | open / close-leg / close | PASS x2 entries (2 legs, 3 legs), all proven and closed. |
| `.tools/safe-commit.sh` | 3 commits | PASS. |

**What worked:** asserting the route's key-order rule IN CODE instead of reasoning about ASCII. It was
load-bearing, not ceremony -- had `T1840Z` not sorted after the bare date, three PUTs would have landed and
served NOTHING, and c2 would have failed in a way that reads as a bad object rather than a bad key choice.
Printing the served KEY beside each body `as_of` likewise found something no 200-check would.

**What failed:** nothing in these two acts. The `deploy_ledger.py` shared-index staging problem recorded in
the previous log was WORKED AROUND here rather than hit: I committed the A3 entry at open, before the act,
while the index was free, so its sentinel actually landed (`96f023071a`) and this commit set carries the
sentinel's deletion too. That is the first entry this session whose full open-then-close lifecycle is on
record.

**Gap found:** none new.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify addendum @`4d0f049203` at its pin | ruling 2 signs ONE memory-only act 10240 -> 1769; ruling 1 records c1 NOT MET and keeps the 5 s bound |
| 2 | Edit `scoped-amgt-api.tf:326` + comment | one value line; the file's single pre-existing non-ASCII char still exactly 1 |
| 3 | `terraform plan` graded from JSON | only differing attribute `{memory_size: 10240 -> 1769}`; `source_code_hash` UNCHANGED |
| 4 | one `safe-apply` | 0 added, 1 changed, 0 destroyed |
| 5 | post-act live read | `CodeSha256 wIpMasw...` UNCHANGED, `MemorySize 1769`, re-plan 0 |
| 6 | condition 3 re-read AT 1769 | 7 of 7 routes 200; 6 of 6 body sizes byte-identical to leg 1; c3/c4/c5 unchanged. No miss -> no rollback |
| 7 | memory entry CLOSED + commit | `c80ace9ee3` |
| 8 | A3 preflight | plan @`ca25158b` MATCH; 3 of 3 sha256 MATCH; 3 of 3 keys 404 with a positive control |
| 9 | A3 key-order assertion | 3 of 3 new keys sort last; `'T'` 0x54 vs `'.'` 0x2E; negative control held |
| 10 | A3 entry opened AND COMMITTED before the act | `96f023071a` -- the sentinel landed this time |
| 11 | three PUTs | `QYt0zV6E...` 7 officers, `Dv.vWFab...` 37, `g6a0Za0y...` 8; read-back by content 3 of 3 |
| 12 | AC1 graded | exit=0, R63 C2 SERVED: YES |
| 13 | served-key-beside-`as_of` print | all three serve their `T1840Z` key; found the half's scope over-generalisation |
| 14 | A3 entry CLOSED + commit | `c9cb861b5d`, carrying the sentinel deletion |

## Verification

Final live function state:
```
{
    "CodeSha256": "wIpMaswMhfNvJaz7WXTyBhN5C3Bb7Qego6+u+aOslfI=",
    "MemorySize": 1769,
    "LastUpdateStatus": "Successful"
}
```

Condition 3 at 1769 -- 7 of 7 at 200, and the six security bodies compared programmatically against leg 1:
```
BA overlay 101996 IDENTICAL   thesis 506924 IDENTICAL   peers 51165 IDENTICAL
VLO overlay 104807 IDENTICAL  thesis 658857 IDENTICAL   peers 51356 IDENTICAL
collected/chatter 67005
0 of 6 body sizes moved -> dropping 10240 -> 1769 changed no served byte
```

AC1 after AMENDMENT 3:
```
PASS C1 ASML_NA falls back to the Bloomberg officer list status SERVED source BLOOMBERG_FALLBACK officers 7
PASS C2 6501_JP_Equity has a management object status SERVED officers 37 reason 'None'
PASS C2 2317_TT_Equity has a management object status SERVED officers 8 reason 'None'
R63 C2 SERVED: YES
exit=0
```

Served key beside `as_of` per name (the CTO half's extra condition):
```
ASML_NA_Equity  SERVED management/v1/ASML_NA_Equity/2026-10-02T1840Z.json  as_of 2026-10-02  7 officers
                2 stored objects, 2 DISTINCT body as_of  -> body CAN identify the served object
6501_JP_Equity  SERVED .../6501_JP_Equity/2026-10-02T1840Z.json            as_of 2026-10-02  37 officers
                2 stored objects, 1 distinct body as_of  -> only the KEY can identify it
2317_TT_Equity  SERVED .../2317_TT_Equity/2026-10-02T1840Z.json            as_of 2026-10-02  8 officers
                2 stored objects, 1 distinct body as_of  -> only the KEY can identify it
```

## Decisions Made

1. **Updated the tf comment block rather than leaving it rot.** It read "raised to 10240 by al-1", which this
   act falsifies. It now records the measured flat curve, that the 5 s bound STAYS (ruling 1 did not relax it
   to 12 s), where the real cost actually is, and an explicit "do not raise this number again to chase that
   latency: it has been tried at three values and does not move it." A comment cannot reach a terraform plan,
   so this widens the commit diff and not the act.
2. **Committed the A3 ledger entry at open, before the act.** Two earlier entries this session lost their
   sentinels to peer-drain collisions. The index was free, so I landed this one first.
3. **Surfaced the CTO half's scope over-generalisation; did not adjudicate it.** The half says two objects
   share a body `as_of` "under each name"; measured, 2 of 3. I reported it with its denominator and left the
   ruling alone -- the defect is real and the half's remedy is right.
4. **Did not treat the memory act as accepting the latency.** Ruling 1 records c1 NOT MET and keeps the 5 s
   target, so I recorded this as a cost correction and said so in both the ledger and the report.

## Files Modified

See commit messages: `c80ace9ee3` (tf + memory entry), `96f023071a` (A3 entry opened), `c9cb861b5d` (A3
closed + instance + record). `infra/aws/terraform/harvest/scoped-amgt-api.tf` now reads `memory_size = 1769`
at HEAD with the explanatory block.

## Blockers

**None owed by this seat.**

## Current State

`opal-amgt-scoped-api` runs `CodeSha256 wIpMaswMhfNvJaz7WXTyBhN5C3Bb7Qego6+u+aOslfI=` at `MemorySize 1769`,
`Timeout 29`. Five NEVER-2 entries opened and closed this session, every leg proven. Seven objects written to
`opal-data-harvest` across the two am-7 acts.

Served state for round 63: c2 **YES** (7/37/8 officers, all three SERVED), c3 YES (95 of 95), c4 YES (12 of
12 on BA and VLO), c5 YES, c6 YES (52 of 52). c1 remains **NOT MET** and recorded so by ruling 1 -- cold BA
2026-09-08 is ~12 s against a 5,000 ms bound, and memory is not the lever.

The remaining work on c1 is ruling 3's round-64 cell: cut the cold read. The CTO's local profile puts 3.55 s
of 4.4 s in two WHOLE gold snapshot reads for ONE security-day (`chatter_daily` 58,300 rows;
`article_security_mention` 23,691), to be fixed by column pruning plus a security filter, with per-stage
Lambda timings printed and c1 re-graded against the same 5 s bound.

## Next Steps

1. **[`3.0.0_SA_CVO~Z`]** DSGN FWD-7 is now re-gradeable on PROD for all three names. Routing that request is
   `2.0.0_SA_COO~Z`'s, per the A3 half's condition 3.
2. **[`2.0.0_SA_COO~Z`]** Round-64 cell per addendum ruling 3 -- cut the whole-snapshot cold reads. That is
   the only remaining lever on c1.
3. **[`1.0.0_SA_CTO~Z`]** At the next `management/v1` schema touch, add the source stamp to the body so it
   says which object it is. Measured scope: 2 of 3 names currently cannot be disambiguated from the body.
4. **[`0.0.0_AB_MSTR~Z`]** The push. All eight commits from this seat today are LOCAL on this device.
