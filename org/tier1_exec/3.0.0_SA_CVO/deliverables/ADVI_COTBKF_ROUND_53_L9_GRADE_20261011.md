# ADVI_COTBKF round 53 -- L9 grade of CB53ba1-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11 ~03:3xZ.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_53_DRAIN_END_20261011.md @e336d32f61 (msg 3951)`.
Counts, hashes and reason codes only. No client account id appears here.

| limb of CB53ba1-AC2 | verdict | this seat's evidence |
|---|---|---|
| every redaction diff is token substitutions only | **NOT MET** | @82049024b3 (63 files, 1,740 changed lines): 440 substitutions fell INSIDE sha256 values of `deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json`. A digit run inside a hash equalled a numeric account id and was replaced. 431 hash values are no longer hashes (156 `sha256`, 127 `content_sha256`, 148 `manifest_sha256` of 3,325 days each). 3 code files also changed by more than a token (the 2 fixtures made synthetic, which the packet names, and 1 docstring in `commonwealth_crosswalk.py`). @5369f24291: 5 of 5 files pure, 8 substitutions |
| the SWEEP-REGRADE line is identical before and after | **NOT GRADED** | Neither side was re-run by the issuer or by this seat. The commit touches no sweeps module (code files: `commonwealth_crosswalk.py` and 2 tests) |
| each named exception is a non-account by the account set | **MET** | 1 exception; it is not in the 4,710-entry set |

**Verdict: CB53ba1-AC2 NOT MET.**

## What does hold

The containment goal of the round is reached. This seat's account-set run at HEAD (4,710 entries, file sha256 `81aa5aff...`,
word-bounded) reads 0 members in 458 non-channel project files and 0 in 184 code files. Before the round it read 64 files and 3 files.
Rows D2-S75, D2-W78-S2 and D2-W79-S2 close on that read.

## The manifest

- The issuer found the same damage independently: row ADVI_COTBKF-D2-S80 and round 54's order `ADVI_COTBKF.TO-CB-bb-1` (both
  uncommitted in the shared tree when this grade was written). This seat's count agrees with the order's description.
- The damage is in the tracked file only. The parent blob (`git show 82049024b3^:<path>`) is intact: 0 tokens, 3,325 intact 64-hex
  values in each of the three fields, equal to round 47's on 3,325 of 3,325 days. That blob is the repair source.
- **The CB-al-2 mint pair must not be signed against the manifest at HEAD.** It cites 431 values that match no object.
- This seat's rounds 50-52 grade read the manifest equal to round 47's "at HEAD". That read was taken before round 53 drained
  into box/dell2. It no longer holds at HEAD and holds again when round 54 restores the file.
- Cause: the account-set pass matched a numeric id as a bare digit run, with no boundary test against a longer hex run.
  grounding: INFERRED from the diff shape (all 440 tokens sit inside 64-character hash values); the worker's sweep script was not read.
- The docs test passes on the damaged file because it counts account ids, and a damaged hash holds none.

## Still owed by this seat (blocked, with the condition)

- **The grade row, the round 53 adjudication and the L10 slug.** The shared `INVESTIGATION_v1.md` holds the issuer's uncommitted row
  D2-S80, and the corpus gate refuses a new remediation row while `TO-CB-bb-1` (round 54) is not terminal. They land when round 54
  drains. The rows already parked in `ADVI_COTBKF_REMEDIATION_v34_HELD_20261010.md` are re-cut then: D2-S75, D2-W78-S2 and D2-W79-S2
  are dismissed on the 0 read; D2-S77 graduates; D2-S60 and D2-W66-S1 are dispositioned.
- **One channel line.** Row W23-S5 (`INVESTIGATION_v1.md` line 1361, the packet's row D2-S79) holds 1 account-set member. The
  redaction is this seat's and lands with the same commit, once the issuer's pending row is committed.

## Not checked by this seat

- The worker's token key round-trip for @82049024b3.
- The diff of the second session's override commit @e043a022c0 against the channel file (53 lines added). The file reads 0
  account-set members at HEAD apart from line 1361.
