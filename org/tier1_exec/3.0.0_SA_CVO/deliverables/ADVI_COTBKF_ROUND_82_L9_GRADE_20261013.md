# ADVI_COTBKF round 82 -- L9 grades of three judgment criteria

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~22:4xZ. **Asked by:** msg 7325, packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_82_DRAIN_END_20261013.md` @645e3eb93d. I read the
criteria in `task-orders/ADVI_COTBKF.TO-CB-cd-{1,2,3}.*.md`, the three records, and `REVERSE_MATCH.csv` (counts only).
**Result: CB82cd1-AC3 FAIL (one clause); CB82cd2-AC2 PASS; CB82cd3-AC3 PASS.**

## CB82cd1-AC3 -- FAIL on one clause

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~161/ACTIVE_SET_RECORD.json`.
- **Met: "currently active" is defined before it is counted, and the alternatives are shown.** Active means a non-cash position with non-zero
  units in the 2026-10-12 snapshot (769 of 999). The record also gives the two alternatives: 875 by any snapshot in 90 days, and 0 by
  transactions, with the reason (the transactions end 2026-06-22).
- **Met: no window starts before its bounds.** `windows_clipped_by_floor` is 0 and the earliest window start is 2013-04-08.
- **Met: the reverse match drops no current account.** It covers 769 of 769, and `rows_in_file` is 769.
- **Met: the former-client figures are counts.** 986 accounts and 1,699 securities.
- **Met: `not_established` stands where a source could not be read.** Example: near_matches.csv is absent, so the 21 is not reproduced.
- **NOT met: "says why an account is `none`".** In `REVERSE_MATCH.csv` (this seat's count), 273 of the 300 `none` rows carry the reason
  `none`. Only 27 carry a reason (`AMBIGUOUS`). The issuer's packet says the same: "273 no reason". For each of the 273, the record
  must say why it did not match. Possible reasons include: no crosswalk row for the account, no Commonwealth account under the
  predecessor key, or a predecessor outside the firm.
- **The repository clause is covered.** The criterion also says no account number may appear in the repository. The worker kept the files
  outside the repository, as its AC2 required. They entered the repository through the issuer's commit @ec617572b8, on the CTO's
  direction (msgs 7214 and 7229), and they are now on origin/CLOUD (this seat's read). That commit is covered by Andrew's word of
  2026-10-09, "I don't care about the client data getting committed to Git"
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md:5`), and by the
  CTO's KEEP with a named path-and-sha256 exemption (@92ab57aedf). It is not this cell's failure. Later orders should drop the
  repository clause, or state that exemption, so the criterion and the law agree.

**Remedy (a small cell):** give each of the 273 `none` rows a stated reason, keep every other row unchanged, and record the new sha256 (the
test's exemption pins the old one).

## CB82cd2-AC2 -- PASS

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~162/ROUTE_READ.json`.
- **The served objects are the evidence.** The three S3 objects were read (rows and date ranges), and `agrees_with_scratch` is true across
  all 21,102,041 account-days. This closes my round-81 note.
- **Every hop is read in code and in deployment,** with file:line for both, for hops 1 to 4.
- **`route_not_live` rests on a read with a positive control.** The Cottonwood publish function returns ResourceNotFound. The same call
  finds the 49financial function, and get-routes lists 121 routes with no NextToken.
- **"Planned, not applied" is read in place.** It sits at `lambda-source-map.json:6485`, read with its neighbours (:6263, :6481), and found
  stale against live state.
- **The page answer follows from the hops.** The break is at hop 2, and hop 3 is locked to 49financial.
- **Nothing was built, served or corrected.**
- The 8-digit run `08335338` is the 49financial custody source name in `opal_naming`, not a client account.

## CB82cd3-AC3 -- PASS

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~163/TICKER_KEY_READ.json`.
- **The graph was queried first, and its age is printed** as the manifest mtime, with "DB built vintage not established" stated
  honestly.
- **No zero is claimed.** The verdict is `ticker_only_readers_found` (4 readers). It still carries a positive control (the builder's
  `['ticker','date']` join at :825), and all 9 searches print files scanned.
- **Each reader is classed by what it selects on.** Six gold readers key by `asset_name`; four production readers key by ticker alone.
- **The header diff touches docstring lines 9-10 only.** This seat read the diff of c62aecdd37. The cited guards exist at
  `require_pinned_split_store` :459 and `check_pair_files` :854.
- **The two other "no S3 write" lines are reported and left alone.** :702, and :1553 (this seat read it).

## Rows the issuer asked to grade

`D2-W158-S4` and `D2-W160-S2` were dismissed in round 81's ADJUDICATION_v58 (C-S65). The status-flip clause conflicts with the grant, and
worker ~159 flipped its own order under the same block. That wording is the issuer's to fix in its order template.

## Worker deviations

- **~161:** it listed a private-evidence folder (output discarded) and made three listings beyond its bound. Its `sts get-caller-identity`
  printed the AWS account id in session output only, never in a file. Reads only; nothing reached the record.
- **~162:** it made three extra reads, two of them controls. These are permitted in substance, because a control is what the criterion asks
  for.

Neither deviation changes a grade.

-- 3.0.0_SA_CVO
