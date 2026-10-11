# ADVI_COTBKF round 53 -- L9 grade of CB53ba1-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T03:22:00Z. Row ADVI_COTBKF-D2-S81.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_53_DRAIN_END_20261011.md @e336d32f61 (msg 3951)`.
Counts, hashes and reason codes only. No client account id appears here.

| limb of CB53ba1-AC2 | verdict | this seat's evidence |
|---|---|---|
| every redaction diff is token substitutions only | **NOT MET** | @82049024b3 (63 files, 1,740 changed lines): 440 substitutions fell INSIDE sha256 values of `deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json`. A digit run inside a hash equalled a numeric account id and was replaced. 431 hash values are no longer hashes (156 `sha256`, 127 `content_sha256`, 148 `manifest_sha256` of 3,325 days each). 3 code files also changed by more than a token (the 2 fixtures made synthetic, which the packet names, and 1 docstring in `commonwealth_crosswalk.py`). @5369f24291: 5 of 5 files pure, 8 substitutions |
| the SWEEP-REGRADE line is identical before and after | **NOT GRADED** | Neither side was re-run by the issuer or by this seat. The commit touches no sweeps module (code files: `commonwealth_crosswalk.py` and 2 tests) |
| each named exception is a non-account by the account set | **MET** | 1 exception; it is not in the 4,710-entry set |

**Verdict: CB53ba1-AC2 NOT MET.**

## What does hold

The containment goal of the round is reached. This seat's account-set run at HEAD reads 0 members in 458 non-channel project files and
0 in 184 code files. Before the round it read 64 files and 3 files. Rows D2-S75, D2-W78-S2 and D2-W79-S2 are closed on that read.
The channel's one remaining member (row W23-S5) is tokenised @3cbc307fd3; the file re-reads 0.

Compile and slug: `surprise-channel/adjudications/ADJUDICATION_v37.md` and `surprise-channel/remediations/REMEDIATION_v34.md` @3cbc307fd3.
The issuer found the manifest damage independently (row D2-S80 @b047e3f3f0, msg 3970); this seat's count agrees. This seat's rounds
50-52 read of the manifest ("equal to round 47's at HEAD") predates the round 53 drain and holds again once round 54 restores the file.

## The manifest (row ADVI_COTBKF-D2-S80, ARMED)

- The damage is in the tracked file only. The parent blob (`git show 82049024b3^:<path>`) is intact and equals round 47's on 3,325 of
  3,325 days. That blob is the repair source.
- The manifest is the input to the CB-al-2 mint pair, which the issuer is re-cutting now. A pair written against the file at HEAD
  cites 431 values that match no object.
- Cause: the account-set pass matched a numeric id as a bare digit run with no boundary test against a longer hex or alphanumeric
  run. grounding: INFERRED from the diff shape (every one of the 440 tokens sits inside a 64-character hash); the worker's sweep
  script was not read.
- The docs test passes on this file because it counts account ids, and a damaged hash holds none.

## Not checked by this seat

- The worker's token key round-trip for @82049024b3.
- Whether the second session's override commit @e043a022c0 added an id: its 2 files hold 0 set members at that commit's proof file;
  the channel file's diff adds 53 lines and the file reads 0 members at HEAD.
