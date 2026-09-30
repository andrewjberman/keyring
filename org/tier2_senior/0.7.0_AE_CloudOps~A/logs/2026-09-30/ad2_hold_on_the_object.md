# AMGT_RESAPP.TO-AMGT-ad-2 -- the hold on the object: 179 no-span sentences moved onto 12 stored D-1 documents

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Agent:** `0.7.0_AE_CloudOps~A` | **Fabric:** site-z | **Session:** a248016e
**Window:** 2026-09-30 ~18:55Z (session start) -> ~21:00Z. First and only order of this session.
**Prior log:** `ac3_slash_key_window.md` (previous session, AMGT-ac-3).

## What was asked

GO msg 27327 from `2.0.0_SA_COO~Z` for `AMGT_RESAPP.TO-AMGT-ad-2` (AMENDMENT 1 @`2de4b63291`): run
AMGT-ad-1's `drafting_build --hold-unspanned` LIVE from the pin, moving every stored D-1 document's no-span
sentences from `sections[].sentences` to the object's `held_no_span`. WORLD class, one never-widen pair,
one NEVER-2 entry.

- Pin: CLOUD `4852128779` (the ad-1 drain). Run from a checkout at the pin, never HEAD.
- COO half `deliverables/2.0.0_SA_COO~Z/round54/NEVER_WIDEN_HALF_COO_AD2.md` @`18ac256769`
- CTO half `ledger/NEVER_WIDEN_ROUND54_AD2_CTO_HALF.md` @`04f779ac51`

## Deployment sequence

1. **Act-start gate** -- re-read all 12 VersionIds at `s3://opal-data-harvest/drafting/v1/` against the COO
   half's table. 12 of 12 unmoved; 22 versions in the prefix, 0 delete markers (read explicitly, not
   inferred from a query error). Population key verified NEWEST of 6 under `crosswalk/v1/`.
2. **NEVER-2 entry** opened (5 legs, 3h window) and committed before any act.
3. **Pre-act capture** -- `ad_2_hold.py --what save` -> 12 stored bodies (1,127,498 B) + 12 served /thesis
   bodies, 0 empty.
4. **Worktree at the pin** -- sparse cone (`lib/` only) to avoid this device's known full-checkout OOM;
   HEAD read back as `485212877976160af79b8365972bce09082ca1f3`.
5. **Dry-run at the pin**, graded mechanically against the half's table: 12 names, 0 beyond, 0 missing, 179
   total, 0 refusals, 225 ABSENT + 12 with-doc = 237 target names.
6. **Live act**, fired in the SAME tool call as a second VersionId re-read so nothing could enter the gap.
7. **AC1, AC2, AC3**, then the CTO half's after-read conditions. Entry closed.

## Verification (actual output)

```
HELD 12 of 237                          (12 post_act_sha256 receipts, exit=0)
unmoved count after the act (want 0):  0      -- all 12 rolled to new VersionIds

AC1  documents 12; sentences moved 179 ; no-span left 0 each
     EVERY STORED D-1 DOCUMENT HOLDS ITS NO-SPAN SENTENCES AND MOVES NOTHING ELSE: YES   exit=0
AC2  12 of 12: at_read N -> 0, on_object 0 -> N, count unchanged   (under AMENDMENT 2)
     THE SERVED /THESIS TEXT IS UNMOVED AND READS THE HOLD FROM THE OBJECT: YES          exit=0
AC3  documents 12; pack sentences removed 179; no-span sentences pre-act 179
     THE POSTURE PACK LOSES EXACTLY THE NO-SPAN SENTENCES: YES                           exit=0

CTO after-read: held_no_span 179 (table 179), per-key exact on all 12; no-span left 0
                span-carrying sentences compared 210 (half says 210), not byte-equal 0
                /thesis ASML(8) + VLO(26) text identical True, basis READ_GATE_PLUS_OBJECT
                CTO AFTER-READ CONDITIONS 2/3/4: ALL MET                                 exit=0
```

## The two findings of this session

**1. AC2 failed as cut, and the rollback was NOT fired.** Every substantive limb passed on all 12; the sole
failure was the top-level `model` key. Measured before being characterised: a leaf-by-leaf diff gave
CHANGED = 1 of 5533 leaves (ASML), 1 of 5454 (VLO), 1 of 5076 (BABA), and that one leaf was
`/generated_at`, 19:37Z -> 19:54Z. Confirmed structurally rather than by timing luck --
`comp-read --enumerate 'generated_at'` on `scoped_amgt.py` returns 10 of 10 hits as `_now_iso()`, a
read-time stamp, so the limb is act-independent and could not have passed for ANY act. The check's
VOLATILE exclusion reached top-level key names only. Both rollback routes stayed live; this seat did not
adjudicate. The issuer reached the same finding independently (msg 27355) and cut AMENDMENT 2 @`9d5bd13f74`
(recursive `unvolatile()`). **Re-falsified after the amendment by this seat:** a nested NON-volatile plant
(VLO `model.cases.base.px_last.value` 382.86 -> 383.86) still FAILS, exit=1 -- the amendment did not blind
the check. An empirical two-read control was also run and is reported INCONCLUSIVE, not claimed: both reads
landed in the same minute (20:01Z).

**2. Row `AMGT_RESAPP-Z-S322`** (OBSERVATION, INERT, disarm_owner `2.0.0_SA_COO~Z`): `deploy_ledger.py open`
STAGES its two files into the shared index, so two concurrent peer drain merges -- `3ac5a8666e`
(`2.0.0_SA_COO~RV`) and `f3980a84ab` (`2.0.0_SA_COO~H`) -- absorbed the NEVER-2 entry under THEIR author
lines before this seat could run safe-commit. safe-commit refused correctly twice on a merge in progress and
staged nothing; the absorption happens upstream of it, and the absorbing commits are merges, where the
owned-paths merge exemption means no lane check sees the payload. Entry content is correct and committed.

## Instrument traps hit and recorded (all in git, per the 2026-09-24 memory rule)

- **A diff reporting ALL 12 rows changed on character-identical text was the CRLF of the `aws` shim against
  an LF heredoc table.** Read literally that was a STOP and a re-sign on a signed WORLD act. `od -c` settled
  it before any conclusion; CR-normalised the diff is empty, and a mutated-VersionId negative control DOES
  fail the same diff, so the empty diff is not a blind instrument.
- **A backtick inside a double-quoted bash argument executes.** `deploy_ledger.py close-leg --proof "...
  under \`model\` made ..."` printed `model: command not found` and SILENTLY dropped the word from the stored
  L3 proof. Same execution-vector class as LD-0276, reached through a TOOL ARGUMENT rather than a commit
  message. Repaired by re-closing the leg through a python argv list.
- **`git log --diff-filter=A -- <path>` returns EMPTY for a file that IS in HEAD** when the add came in via a
  merge -- default history simplification hides it; `--full-history` shows it. And `git status --porcelain`
  prints nothing once index, worktree and HEAD agree, so the absorption leaves no trace a status read sees.
- **`git log --since='2026-09-30 18:00'` is LOCAL time.** My own commit (16:39 EDT = 20:39Z) fell outside my
  own filter, and the query read as "this seat has no commits" on a commit that exists.
- **The `/watcher` census recipe cannot see a harness-armed Monitor**: its `-notmatch ' -c '` clause excludes
  the very row the Monitor tool creates (`bash -c ...`), so the census reads `script rows: 0` while the
  watcher is live and delivering. Reaping or re-arming on that zero would split the inbox. The functional
  proof (an `[INBOX]` event, then an ack) is the sound oracle.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-read --enumerate` | `comp-read lib/research/api/scoped_amgt.py --enumerate 'generated_at'` | **PASS -- and it is what settled AC2.** 10 hits / 4693 lines / 148 sections, bands CODE=10, all whole-value, every one `_now_iso()`. Turned a timing argument into a structural fact. |
| `comp-find --name` | `comp-find --name '*.proof_of_spec.json' <deliverables>` | PASS. 15 hits / 307 files scanned, denominator printed, 9 ephemeral-floor excluded and reported. |
| `deploy_ledger.py` | `open` (5 legs), `close-leg L1..L5`, `close` | PASS on the contract; entry CLOSED, all 5 legs proven, 0 sentinels left. It also SURFACED row Z-S322 (it stages into the shared index) and exposed the backtick execution vector on L3. |
| `safe-commit.sh` | entry, row, final proof commit | Two correct REFUSALS on a merge in progress (MERGE_HEAD `ead1db469b`, then `1cdbe5df21`), staging nothing; final commit landed `bcada3e9ea`, 33 files. Landing confirmed by ASKING GIT, never by reading the wrapper's prose. |
| `proof-of-spec-check.py` | on the ad-2 instance | First run TOOL-ERROR (rc=2, not a verdict): it `read_bytes` a `path_or_key` that named a DIRECTORY. Re-pointed at representative files -> then one real VIOLATION (an invented `NOT-COMMITTED-DUPLICATE` sentinel is not a legal `commit_or_etag`) -> **VALID rc=0**, 0 violations, invocation-alignment 3/3, surprise row resolves. |
| `comp-iam` / `comp-schedule` | issuer-side / NOT-APPLICABLE per the order's preflight | SKIPPED -- declared in the instance's exclusions. |

**What worked:** `comp-read --enumerate`'s band split answered the AC2 question outright -- 10 of 10 CODE
hits, all `_now_iso()` -- where a prose read would have left it a judgment call.
**What failed:** `proof-of-spec-check.py` crashes with a raw `PermissionError` traceback when an
`artifacts_produced.path_or_key` names a directory. It labels itself NOT-A-VERDICT (rc=2), which is correct
and saved the read, but the failure mode is a stack trace rather than a row-level message.
**Gap found:** the never-widen act-start VersionId gate has no shared instrument -- each executor
hand-rolls the comparison, which is how the CRLF false-STOP became reachable. A tiny shared helper that
CR-normalises both sides, prints both denominators and self-tests with a mutated id would close it. Surfaced
for the owning seat (`2.0.0_SA_COO~Z`); not implemented here -- out of BOUNDS 1 and out of `<paths>`.

## Files modified

See commit message `bcada3e9ea` (33 files). Summary: the ad-2 proof instance, `evidence/` (5 files), the
irreproducible `ad2-pre/` capture (12 stored + 12 served bodies), surprise row Z-S322, the closed NEVER-2
entry and its removed sentinel.

## MCP traffic

3 messages, all handled and acked: 27327 (GO, acked at load), 27355 (RULING AMENDMENT 2, acked and applied
mid-order), and 1 outbound -- the completion report to `2.0.0_SA_COO~Z` at 20:57Z. The watcher expired and
was re-armed the same turn on each of 4 notices.

## Blockers

**None.** Nothing is owed by this seat on ad-2.

## Current state

`AMGT_RESAPP.TO-AMGT-ad-2` is COMPLETE and verified. The 12 stored D-1 documents at
`s3://opal-data-harvest/drafting/v1/` now carry their no-span sentences in `held_no_span` on the object
(179 total: ASML 8, BABA 2, BA 21, COST 24, HAL 7, HD 16, INTU 14, KMB 21, NU 19, PBR 13, SAP 8, VLO 26),
0 no-span sentences left in any stored section, and the 210 span-carrying sentences byte-equal to the base.
The served /thesis reads the same sentence text with `held_no_span_at_read` 0, `held_no_span_on_object` = the
count and basis `READ_GATE_PLUS_OBJECT`. Post-act VersionIds are in
`deliverables/0.7.0_AE_CloudOps~A/evidence/ad2_versionids_postact.txt`; the rollback bytes are in
`ad2-pre/store/` (committed) and `ad2-pre-bytes/` (on disk, byte-identical).

NEVER-2 entry `20260930T1921Z_amgt-resapp-r54-ad2-hold-on-object_deploy_completion.md` is CLOSED with all 5
legs proven and its sentinel removed. Proof instance is VALID.

**Push state: LOCAL @`bcada3e9ea600ca1db5277ec930ee4f76e46b194`** -- origin/CLOUD read by `git ls-remote` at
report time is `5fe52a896a5440ba8a145f77280b4496c8f569d7`, and my commit is not an ancestor of it. The pin
worktree was torn down (branch `wk-ae-ad2-pin` deleted, 0 porcelain rows before removal).

## Next steps

1. **[`2.0.0_SA_COO~Z`]** The `<status>` flip on `AMGT_RESAPP.TO-AMGT-ad-2` is the issuer's, per section 5.
   Completion reported at 20:57Z with the criteria, the commit and its push state.
2. **[`2.0.0_SA_COO~Z`]** Row `AMGT_RESAPP-Z-S322` is open with this seat naming it and the issuer as
   `disarm_owner`: `deploy_ledger.py open` stages into the shared index. Candidate repair named in the row
   (write the two files UNSTAGED, so the opening seat's own safe-commit is the only path into the index) --
   proposed, not implemented; amending another seat's tool is not this seat's act.
3. **[`0.0.0_AB_MSTR` / `0.0.0_AB_MSTR~Z`]** The push. Everything from this seat is LOCAL on CLOUD; the push
   is that seat's on Andrew's word.
4. **[`2.0.0_SA_COO~Z`]** NOT COVERED by this act, named in the CTO half: the next posture batch will move
   `posture/v1` on a pack that no longer carries the 179 sentences. That run is its own act and its diff is
   read at the round-54 L10.
