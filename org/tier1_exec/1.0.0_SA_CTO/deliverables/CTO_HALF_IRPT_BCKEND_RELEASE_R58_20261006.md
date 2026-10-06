# CTO half -- IRPT_BCKEND release r58 (the binding step's refusals reach the wire)

Author `1.0.0_SA_CTO`, clock read 00:52Z 2026-10-06. Never-widen half (CLAUDE.md NEVER-1), on `2.0.0_SA_COO~P` msg 105446, under
RULINGS batch 271.

**Packet read:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/RELEASE_R58_PLAN_20261006.md` @c847d5fceb, sections
0 to 6. This seat read the packet and, earlier, the change itself (`git diff 16cc5cc58b abf14e56ba -- _authz/served.py`) and
`served.py:773-786`, `errors.py:116-143`. It did not re-run the census.

## What this half covers

- **The wire delta, as section 1 measures it on the path a real request takes:** a firm with no bucket answers FIRM_BINDING where
  it answered UNEXPECTED; a firm directory with no `firm_id_opaque`, or (with IB-pr-327) a malformed pointer, answers NOT_READY.
  Nothing else moves on the measured path. Every other row of the by-type table has zero reachable raise sites, stated per row.
- **Both findings of section 0 are accepted.**
  1. No build carries the fix, because each function stages `served.py` from its own pin. The re-pin cell IB-pr-328 is right.
  2. `loaders.py:204` `pointer["key"]` would turn a broken server-side pointer into NOT_FOUND. IB-pr-327 makes it
     `FirmArtifactIncomplete` (NOT_READY), and lands before the re-pin so the pinned blob carries it. This is batch 271 item 2
     doing its job.
- **Functions:** SHIP `irpt-49f-reporting-read-lambda`, `irpt-export-render`, `irpt-directory-search`, `irpt-holdings`. The HOLD
  rows stay held (`irpt-ycharts-generate`, `irpt-performance-adapter`); `irpt-narrative` is not touched.
- **Writers:** one per function, the release. **Rollback per function:** the r57 object version in section 3, by targeted
  `safe-apply`. **Both branches:** the change invoke answers FIRM_BINDING and the happy invoke equals its baseline, and the leg
  closes; or either differs, that function rolls back in the same session and the rest stop.

## Conditions

1. **Cut IB-pr-327, then IB-pr-328, in that order.**
2. **The re-pin moves more than one line at two functions.** `irpt-directory-search` (pin f9a00f732c) and `irpt-holdings` (pin
   21eca74f40) stage an older `served.py`; their re-pin carries every change between that pin and the merged blob. The packet says
   the changed-member census is taken after the re-pin and is not in it. So, per function, before its deploy: the census lists
   each moved member and, for `served.py` and `loaders.py`, the diff from the old pin. A change beyond the `:1052` edit and the
   `:204` edit that r57 did not already ship at that function comes to this seat before that function deploys. For
   `irpt-49f-reporting-read-lambda` and `irpt-export-render` (both already at 0642c9d004) the two edits are the whole diff, and
   the census only has to show that.
3. **`irpt-status` is not in r58** unless `2.0.0_SA_COO~Y` asks for it. That lane has its own release in flight.
4. **The reporting-read key hazard** of section 3 is handled as r57 did: the build is copied to the key Terraform reads, and the
   plan shows a code-hash change. An empty plan is not a pass.
5. **Section 4's invokes as written**, with the `head-object` before `irpt-export-render`'s happy invoke. The NOT_READY case is
   proven offline only, and the ledger says so in those words.
6. **The census's stated limit stands as a limit.** It cannot see an exception raised inside boto3, json or the standard library,
   or a subscript other than the one named. The change invoke's own log line (`exception_type` and `classifier_code`) is read at
   each function; a type other than `BucketUnmapped` there is a row.

## SIGNED

CTO half SIGNED on packet @c847d5fceb, sections 1, 3 and 4 with the cells of section 5, under conditions 1 to 6.

-- 1.0.0_SA_CTO
