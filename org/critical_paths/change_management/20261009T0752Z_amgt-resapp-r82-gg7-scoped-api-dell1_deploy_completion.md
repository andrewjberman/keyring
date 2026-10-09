# Deploy Completion Record
**Date opened:** 2026-10-09T07:52:43.622911+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-gg-7: redeploy opal-amgt-scoped-api from dell1 at build pin 7b84cfc5a9, ONE code leg and no snapshot leg (risk WORLD; GO 2.0.0_SA_COO~R1 msg 2022). NEVER-WIDEN PAIR READ WHOLE BEFORE THE FIRST LIVE ACT: COO half org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND82_GG7_COO_HALF.md @520c6e0f92 sha256 a4b9e5abd43b44d99d3dffd995f06d50e8b249336f300ffd3cbd684426834526; CTO half NEVER_WIDEN_ROUND82_GG7_CTO_HALF.md @fab454cb98 sha256 82814b488b32c40d99b095299c0269d8a22a09f8c4f7435d6a1e0c41a603fc6a (SIGNED, ee-6 conditions 1-5 carried plus 6 and 7). Live pre-act measured fresh: CodeSha256 aAkcp2l1TkaeMnZKjpeg/U6og+p0WR12O1YKp53Pvyc=, LastModified 2026-10-09T05:23:48Z, Memory 1769, Runtime python3.11, Timeout 29, State Active -- i.e. this lane's own ee-6 build at pin 881540dcfd. No snapshot object is written by this act.
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | ROLLBACK CAPTURE: download Code.Location, sha256 base64 must equal the live CodeSha256, keep the path | base64 sha equality + kept path | PASS. aws lambda get-function --function-name opal-amgt-scoped-api, Code.Location downloaded to C:/Users/Test/AppData/Local/Temp/claude/C--Dev-ajb-workspace/dbd06e5d-56e1-44dd-8f7e-9035184f9f1b/scratchpad/amgt/LIVE_ROLLBACK_opal-amgt-scoped-api_aAkcp2l1.zip -- 42021913 bytes, sha256 base64 aAkcp2l1TkaeMnZKjpeg/U6og+p0WR12O1YKp53Pvyc=, EQUAL to the live CodeSha256 read fresh from get-function-configuration. Negative control run beside it: the same digest compared against the ee-6 base OUOsYXaJSklKJ65vpIe2jWfcXm9jvP0bCyia15F8Bxs= reads False, so the equality is discriminating and not a constant True. This file IS the rollback (the COO half's PER-KEY ROLLBACK: this package through the module, one safe-apply, same session; no store object is written by this act) and is AMGT_DEPLOYED_ZIP for the build. | CLOSED 20261009T075339Z |
| L2 | verify | wheel folder C:/tmp/r80-wheels re-hashed against round78/BB18_WHEEL_FOLDER_SHA256_20261008.txt BEFORE the build | 6 of 6 sha256+bytes equal, both denominators printed | PASS. C:/tmp/r80-wheels re-hashed against org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/BB18_WHEEL_FOLDER_SHA256_20261008.txt BEFORE the build. RECORD DENOMINATOR 6; FOLDER DENOMINATOR 6 .whl plus 1 non-wheel SHA256.txt sidecar; 6 of 6 EQUAL on both sha256 and byte count; DECLARED-BUT-ABSENT none; NOT-IN-THE-RECORD none. attrs-26.1.0 aa97b256ec689d4d/67548, jsonschema-4.26.0 756dd1cd8812465d/90628, jsonschema_specifications-2025.9.1 80d57274293a297e/18437, referencing-0.37.0 b9a6046f8b50bf51/26763, rpds_py-2026.6.3-cp314-cp314-win_amd64 0be972be84cfcaf4/220380, typing_extensions-4.16.0 8bcbfab4891bda69/45571. Both denominators are printed because a record-only count cannot see an extra file and a folder-only count cannot see a missing one. | CLOSED 20261009T075340Z |
| L3 | verify | BUILD from a DETACHED worktree at EXACTLY 7b84cfc5a9, --build-only, PIP_NO_INDEX=1 + PIP_FIND_LINKS + PIP_LOG; CONTENT-DIFF graded against the COO half list, each off-round member admitted only with its closure reason (condition 1) | build sha + content-diff file list + off-list count + pip index-request count 0 |  | OPEN |
| L4 | verify | CONDITION 6: whether ANY request path of the function CALLS publication_gold's alias matcher (_match_counts / mention_rows / build_mention). A caller is a STOP before apply; inert ships with the line printed | the call-graph read from the BUILT files, printed either way |  | OPEN |
| L5 | verify | CONDITION 7 + ee-6 condition 2, pre-apply, from the BUILT package: load_registry(), lookup('4698') off the built scopes.json, and one existing address() byte-equal as the negative arm | the three reads, with built-package provenance asserted |  | OPEN |
| L6 | activation | upload the built file, then ONE safe-apply on infra/aws/terraform/harvest/ with the plan graded UNTARGETED; exactly ONE resource may move | plan counts + the single resource named + apply output |  | OPEN |
| L7 | verify | new CodeSha256 DIFFERS from aAkcp2l1 AND equals the built file's; 0-diff re-plan; ee-6 condition 2 post-apply /thesis 200; the existing address() byte-equal AFTER (condition 7's negative arm) | get-function-configuration read + /thesis GET + the post-apply address() read |  | OPEN |
| L8 | git | ee-6 condition 5: record-terraform-deploy.sh run so the function's source-map entry carries the deploy | commit hash + the entry's values |  | OPEN |
| L9 | verify | AC1 r82_deployed.py (3 lines) and AC2 r81/r80_deployed.py regression arm | every criterion's output lines + exit=0 |  | OPEN |

## Log

- 20261009T075243Z OPENED by 0.7.0_AE_CloudOps~RA1 with 9 leg(s)
- 20261009T075339Z LEG L1 closed: PASS. aws lambda get-function --function-name opal-amgt-scoped-api, Code.Location downloaded to C:/Users/Test/AppData/Lo
- 20261009T075340Z LEG L2 closed: PASS. C:/tmp/r80-wheels re-hashed against org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/BB18_WHEE
