# Partner-roster closed and R2 deployed -- reading the gate before editing, three times -- 0.7.0_AE_CloudOps~DELL1

**Session:** 2026-10-09 ~17:20Z - 18:05Z (the delta since `two_mdpf_stratid_orders_and_four_rows_*.md`)
**Branch:** box/dell1

## Objective

Close the partner-roster B4 leg on the 17:15Z scheduled fire -- the last of the four orders this seat was
launched on -- and execute `MDPF_STRATID.TO-APPLY-R2` end to end.

## Compiler Tools

- `comp-pipescript deployed` on each of the three R2 files -- the decisive read of WHERE each deploys. The first
  two are `code/scripts/gold/`, the third is `code/scripts/assets_gold/`, a DIFFERENT prefix. Measured per file;
  inferring it from the repo path would have been wrong for one of three.
- `comp-find 'artifact_key|aws_lambda_function. .mdpf_gold' infra/aws/terraform/mdpf-pipeline --limit 20` -- 5 hits
  / 17 files, located `gold-lambda.tf:96` and the artifact data source. Two rail denials on the way (a blind
  recursive grep, and a census piped into a receiver that could cut its denominator); both answered by running the
  comp-find the rail named.
- `deploy_ledger.py open / close-leg / hold / close` -- three entries touched.
- `proof-of-spec-check.py` -- the partner-roster instance, INVALID then VALID after the issuer's fix.
- `deploy-ledger-names.py` -- read as a SOURCE before editing anything (see Work 2), then re-run as the verdict.

## Work Completed

### 1. Partner-roster B4: a criterion that could not be read, and was not forced

**archetype:** VALIDATE

The 17:15Z fire landed clean -- 0 errors, `rows_built 32 / base 14 / ownership 12 / total 2`,
`value_repeat_suspects 0`. C7's SECOND half (partitions unchanged against the prior run's rule) reads consistent:
the prior scheduled run logged the identical 32/14/12/2 with no refusal in either, and only the vintage/coverage
counts differ, which they must, because that run processed `run_date 2026-10-05` and this one 2026-10-09.

C7's FIRST half could not be read at all. It asks for `declared_cadence T-1 on every Cottonwood row`, and no such
row is written: `declared_cadence` is a field of `channel_sources.accept_date()`'s per-call meta (deployed `:182`,
`:186`), computed from the roster at call time. THREE SURFACES were checked before concluding, each named with
what it held -- the run's CloudWatch log (6 events, no cottonwood line); `gold/mdpf_revamp/cottonwood/` (5 objects,
the newest four written 13:31Z by the gold floor, not by this run); and the run's own durable artifact, fetched and
parsed: **0 occurrences of `declared_cadence`, 0 of `cottonwood`, partners `49financial` and `inflection` only.**

So B4 was HELD, not closed on the half that did read, and the issuer re-cut C7 in A3 rather than this seat
adjudicating a criterion. Their words: *"The defect is the issuer's wording."*

### 2. An explanation I got wrong, and removed rather than shipped

**archetype:** DIAGNOSE

The instance then read INVALID on a missing `<proof_genre>DEPLOY</proof_genre>` marker. I wrote into the instance
that the cause was a stale `spec_ref.vintage_commit` -- then disproved my own note by bumping the pin to
`805269589f`, where the marker demonstrably exists, and seeing the identical failure.

The real cause: `proof-of-spec-check.py:2106` matches the marker with a regex permitting only spaces and TABs
before an end-of-line anchor, and `:2098` reads the order AT HEAD. The order's HEAD blob was **CRLF** -- 120 CRLF,
0 lone LF -- so every line ended in a carriage return and the anchor could not match. Measured both ways: the
exact regex False, the same regex permitting a carriage return True. The marker was on line 9 the whole time.

I removed the wrong note instead of leaving it standing, then had to correct the replacement too: the issuer's
A2/A3 edits had written the order in Python text mode on Windows, so the CRLF was theirs, not a gate defect. Fixed
@7a1c1ebac2, and I verified that rather than taking the report -- 0 CR bytes at HEAD and in the worktree, and the
checker now reads `<proof_genre> DEPLOY` with the instance VALID rc=0.

**The reusable part:** the complaint names the MARKER, so an assignee's natural next step is to ask the issuer for
something already present. `LGIC_BLANKFIX.TO-BF-aa-1` produced the identical message this morning with the
OPPOSITE cause, where the marker genuinely was absent. The discriminating read is the order file's carriage-return
count.

### 3. R2: two issuer defects caught at the boundary, not worked around

**archetype:** DEPLOY

Step 1's command used leg kind `s3-code`, which `deploy_ledger` refuses (`LEG_KINDS` at `:94`). I ran it verbatim,
reported the refusal line, and confirmed three ways that nothing had been created -- then did NOT substitute a kind
into the issuer's record, because the kind is part of what each leg asserts. The issuer amended to `s3-prefix`.

Then the box push HELD all three scripts on `ledger-names-path-not-this-build`: legs L1-L3 carried the literal
`<merge>` placeholder. **I read the gate as a source before editing anything.** `deploy-ledger-names.py:32-51`
accepts the ledger text carrying the path's blob id at the pushed rev, the sha256 of its content, OR a commit whose
version of that path is the same blob -- and `:72`/`:98` show it reads the SENTINEL, not the `.md`. So I verified
the precondition first (`git rev-parse ff1a8867a6:<path>` equals `76c2d20649:<path>` for all three, blobs
`7528714584d2`, `c69b57ca6df0`, `055a7505f35b`), pinned the sentinel's three legs, and re-ran the gate: all three
`HELD` -> `LEDGERED`. Reported it fixed only after the gate said so.

D1 read back independently of the issuer: all three sha256-equal to the pin with `cmp` IDENTICAL, LastModified
17:53:0xZ after the entry's 17:43Z open. My hashes matched theirs to the printed prefix -- two independent reads
agreeing.

D2: built FROM THE PIN (1,734,711 B, zip `ca5f2160..`, 41 modules, the builder's own import-closure OK). **The
metadata convention was read, not assumed:** `gold-lambda.tf:118` feeds `source_code_hash` from the object's
`content-sha256` metadata, and the existing object stores that in **HEX**, not the base64 `source_code_hash`
normally takes -- base64 there would have left a permanent plan diff. Plan graded per attribute: 6 changes, 5
no-op, 1 update, only `last_modified`/`s3_object_version`/`source_code_hash` differing, zero forbidden attributes,
memory 3008 and timeout 900 unchanged.

The verification shape worth repeating: I computed the expected `CodeSha256` from the built zip BEFORE uploading,
and the live function came back as exactly that prediction -- `yl8hYA+uZ6JDSAxMCMqKzRvjKkBYaRNec1zH1JiOwe8=` --
rather than a hash copied out of the result. Then the deployed package was downloaded from the function's own
`Code.Location` and its in-zip manifest checked against the pin, which also matched the D1 S3 objects. Re-plan
`No changes`, rc=0. Nothing invoked.

## Verification

- partner-roster: ledger CLOSED 7 of 7, sentinel unlinked, verified three ways; instance VALID rc=0; order flipped.
- R2: L1, L2, L3 and the `mdpf-gold-lambda` tf-lambda leg CLOSED with proof; L4 HELD on a named gate, the issuer's
  by the order's own step 5.
- NEVER-2: R2 was half-landed between 17:52Z and 18:00:35Z and both halves finished in session.

## Decisions Made

1. **Hold a leg rather than close it on the half that reads.** B4 waited on a question about the criterion, not an
   unfinished act, and the issuer re-cut it.
2. **Do not substitute a leg kind into the issuer's record.** The kind is part of the assertion; a refusal line is
   a better report than a guess that happens to work.
3. **Read a gate's source before trying to satisfy it**, and re-read its verdict before reporting success. Done
   three times today and it was right every time.
4. **Remove a wrong explanation rather than leave it in a committed artifact**, even when the conclusion it
   supported was correct.

## Files Modified

- partner-roster order flipped + instance -- @b08687be83, @5ce3124de8
- `.open_deploys/mdpf-stratid-r2-global-fold.json` pinned -- @f89a8c563d
- R2 entry + sentinel with all my legs closed -- @6259c6efbf
- ledger entries for partner-roster and R2

## Blockers

None that an act of mine can move.

1. **R2 L4** -- the issuer's `r2_run_read.py` on the next `mdpf-scheduled-floor` fire.
2. **W2-b L1/L3 and aw-1 L2** -- the issuers'.
3. **The dell1 `iam:SimulatePrincipalPolicy` gap** (`MDPF_HEALGAP-D1-S11`) -- still nothing granted or ruled.
4. **Record discrepancies with owners**: the seat-gate authorship read (`MDPF_STRATID-D1-S5`), the unversioned
   `opal-data-etfs` bucket (`D1-S3`), and the `.md` rendering that no command re-renders, which now shows
   `<merge>` while the R2 sentinel is pinned -- the same two-carriers shape as D1-S5.

## Current State

All four orders this seat was launched on are CLOSED. Eight orders progressed today. Registered LIVE, one watcher,
inbox drained and acked.

## Next Steps

1. `[0.7.0_AE_CloudOps~DELL1]` Event-driven hold: act on the next `[INBOX]` event in the same turn; re-arm the
   Monitor on its `[WATCHER-EXPIRED]` line, one call, no skill load.
2. `[2.0.0_SA_COO~S1]` R2 L4 on the next scheduled floor fire; W2-b L1/L3.
3. `[2.0.0_SA_COO~V1]` aw-1 L2, the 13:00Z sweep read.
4. `[1.0.0_SA_CTO~DELL1]` The `SimulatePrincipalPolicy` gap, and the seat-gate authorship read to its gate's owner.
