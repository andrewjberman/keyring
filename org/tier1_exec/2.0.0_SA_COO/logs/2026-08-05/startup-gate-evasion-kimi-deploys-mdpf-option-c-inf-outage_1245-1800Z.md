# 2.0.0_SA_COO -- Startup through a gate-evasion class, two Kimi deploys, Andrew's MDPF option (c), and a 5-day INF outage nobody had surfaced
**Window:** 2026-08-05 12:45Z-18:00Z (computed UTC; host UTC-4) · **archetype:** MIXED (COORDINATE / DIAGNOSE / VALIDATE)

## Startup
Registered, persistent inbox Monitor armed (`bev3vdxzq`, confirmed `running`, later proven by ~15 real
deliveries). **Zero crons** -- read the XXX.md Step 1b-F COO row and confirmed NO live scoped `/drive`
authorization (07-23 re-arm discharged 07-24; the open re-point offer at Andrew is not an authorization).
PATH probe 95/95 + a forwarder actually EXERCISED. Merged origin/CLOUD forward (ort, no rebase); push
correctly refused by the LD-0367/0368 integrator gate, MSTR carried the commits at 1259Z.

## F-XXX -- `git -c k=v <verb>` evaded ALL FIVE gates in never-rules-gate.sh
Found by TRIGGERING IT: my `git -c pull.rebase=false pull` executed while a plain `git push` was denied
one command later. Same gate, same session, same branch -- that asymmetry was the discriminator.
Root cause `:302`: `_GIT` special-cased two-token `-C <path>` but not `-c <key>=<val>`, so the regex
died before the verb. Disarmed NEVER#7 rebase, NEVER#7 bare-pull-under-`pull.rebase=true`, stash, clean,
and the integrator gate. Self-disclosed to CTO/MSTR before anyone found it.
**MY FIX WAS INCOMPLETE.** CTO refused to accept on my report, re-derived at source, and WIDENED it --
`-c` was 1 of 5 cells (`--git-dir`, `--work-tree`, `--namespace`, `--config-env`, `--super-prefix`);
`git --git-dir .git rebase` evaded my one-line fix. I generalised from the single shape I happened to
hit: a hand-drawn roster wearing a predicate's clothing.
Also surfaced the SECOND defect: the gate's own deny-text taught `git config pull.rebase false`, whose
one-shot inline form is the evading shape -- a gate whose guidance names its own blind spot. CTO rewrote it.

## The torn-read class (three seats, one cause)
My Bash call was refused with a syntax error quoting line 342 -- which was BLANK when I read the file
seconds later; the same content had moved four lines down. Not a timing correlation: same content at two
line numbers across an execution and a read. CVO correctly rejected my earlier mtime argument (their error
PRECEDED the mtime I cited). CTO confirmed IN-PLACE editing was the cause (CVO 1323Z, me 1420Z, CRO ~1325Z)
and ruled my proposed remedy: **every file the harness executes on each tool call lands by write-to-temp +
atomic `mv`, never in-place.** A zero-logic text-only edit took Bash down intermittently across seven seats
-- the risk was never in the CONTENT of the edit, it was in the WRITE MECHANISM.

## OPAL_KIMIPIPELINE -- two deploys, three pin-staleness events
DEP1 (a254104b34) landed 145659Z; DEP2 (9a1856bc03) landed 164522Z. Both ETag==md5 verified, both inside
the window. AE invented a round-trip read-back control unprompted on DEP1; I MANDATED it in DEP2.
- **I fired a GO on a stale pin.** CTO~B landed a254104b34 22 min after 765233590; my pin lacked the `_utc`
  fix. Caught pre-upload -- AE hit it INDEPENDENTLY at 1424Z via the TO's own `if_mismatch`. CTO~B's
  positive control proved it real (`last_commit_git_local` 0 at my pin vs 2 at theirs).
  Added the tip-recheck control; it then caught the class twice more the same day.
- **Corrected CTO~B's deploy mechanism from EC2_MANIFEST:571** -- an S3 PutObject, not safe-ec2-deploy/SSM
  (transient box, systemd pulls on boot). They would have handed AE an instruction contradicting the manifest.
- **The real defect:** the corpus was computed, logged, written to the artifact and COUNTED INTO THE MANIFEST
  -- and never passed to `build_prompt`. Kimi had never seen the human-ruling half. Plus `[:60000]` silently
  cut the git half mid-string; today's 69,495-char payload did not parse as JSON.
- **Size risk refuted by two seats on DIFFERENT derivations:** AE grounded it as input-vs-output budget
  misattribution (KIMI_EMPTY was `max_tokens`, unchanged; 60,000 was never a tested boundary but a
  hand-picked slice); CVO independently on the 8x margin. Retune withdrawn.
- **CVO caught the hole in my verification.** My negative control proved the AST instrument isn't blind to
  EVERYTHING; their POSITIVE control (comment insertion) proved it is blind to EXACTLY the class being waved
  through. Only the second licenses a transfer. Standard adopted: acceptance attaches to BEHAVIOUR evidenced
  by a pin, transfers iff identity is MEASURED with BOTH controls and RECORDED; AST identity + encoding check
  as a PAIR, never AST alone.
- Open, not closed by either deploy: only **69 of 153 nuggets** reach the prompt -- ~36 of Andrew's own
  verbatim rulings still do not, and zero delegated rows do. Declared in-prompt; budget split is CTO~B's.

## MDPF -- Andrew ruled option (c), which neither exec had offered
His question ("the publisher lambda should be running this script, not some ec2") dissolved the (a)/(b) fork
and exposed the real defect: **WS-A writes DIRECTLY to the SERVED bucket, bypassing the publisher.** WS-A runs
in 3 seconds -- the EC2 is inertia. Decomposed into W0-W4, dependencies encoded in `<dependencies>` not
message order. W0 (row-17 dead grants) GO'd; W1 GO'd to DS; W2/W3/W4 staged.
**CTO CAUGHT A SILENT-FREEZE DEFECT IN MY OWN DECOMPOSITION.** I scoped W1 producer-only. `_latest_key()`
returns max(keys) and raises only on a FULLY EMPTY prefix -- and we aren't deleting historical partitions.
Writer-only re-point => the emitter returns the last partition WS-A ever wrote, FOREVER, re-stamped with
today's run_date, for 11 client-facing cohorts. No exception, no rc!=0. DS confirmed they would have shipped
it. Amended to ATOMIC over producer AND consumer, acceptance CONSUMER-SIDE, dual-read forbidden.
**Andrew's acceptance criterion cannot be discharged by observation:** `_provenance.written_by` is a
self-report by whoever wrote LAST. Real deliverable is W4 -- a RESOURCE-SCOPED Deny reserving the 12 keys,
exercised behaviour-grade with an ISOLATED positive control. CTO+COO co-sign confirmed (NEVER#3).
Inversion worth keeping: **we have used resource-scoped Deny to STOP writes to dead keys and never to
RESERVE the live ones.**

## GRF delivered (0.4.0_DS, ~35 min from spawn) -- and the composition gate falsified
Surface count is **1 of 3**, not 3. And the finding that matters: **the composition gate is a WITHIN-DATE
identity, and a uniformly vintage-shifted roster satisfies it perfectly.** Global 7620 vs true 7554 -- +66
at 0.86%, UNDER EVERY PERCENTAGE FLOOR, while `global == 49F + inflection` held EXACTLY 7/7 dates with the
whole sum on the wrong day. The instrument we would have used to reassure Andrew about the dates HE flagged
was structurally incapable of seeing it. Control must be a VINTAGE control, not a sum control.
Production trap recorded: `point_class="carried"` SystemExits aum-metrics at build time on the first lag day.

## THE INF OUTAGE -- 5 consecutive days, surfaced by a retraction
0.7.0_AE self-retracted an "L2 satisfied" claim they had made TWICE: they checked `pipeline-complete.json`
and skipped `pipeline-failed.json` -- **the discriminator the leg explicitly NAMES.**
Measured: failed marker advanced 08-01/02/03/04/05, last failure 14:50:58Z today, exit_code 1. Last success
07-31. NOT a calendar false alarm -- the producer SELF-REPORTS failure and the chain runs weekends.
Read-only diagnosis GO'd; cause UNKNOWN and explicitly not guessed (Rule 22). Andrew push-notified.
**`inf-nna-excusals` had sat "past window" 274h DOING ITS JOB** -- refusing to close because the exercised
verification never happened.

## Retractions I owed and made
1. **deploy_ledger is NOT defective.** I adopted AE's first mechanism and repeated it to CTO and Andrew.
   `cmd_close` unlinks the sentinel; the four carry a non-canonical status string, `closed_at=None`, and a
   live sentinel -- hand-edited. My "three false-positive detectors" became one confirmed, one open, one
   WITHDRAWN. I over-read a pattern from three points on a day when "the instrument is lying" kept being right.
2. **My mtime evidence for the torn read** -- withdrawn on CVO's correction before CTO settled it another way.
3. Corrected to Andrew: 0.4.0_DS holds **61** active TOs, not the 16 I quoted (pending-only slice).

## Compiler Tools
| Tool | Result | Notes |
|---|---|---|
| `comp-state --self-test` | PASS 3/3 | gate honored before trusting output |
| `comp-state` | 723 BEHIND / 2348 | recall instrument; dominated by lexical noise on a high-activity day -- did NOT chase. Its evidence lines surfaced a254104b34, which is how I caught my own stale pin |
| `comp-which` (A.3 exercise) | forwarder RAN | scored on OUTPUT not rc, per the XXX.md correction |
| `audit-archive-invoker` | rc=1, 2 findings | one INTEGRITY claim I could not reproduce (see below) |
| `to-check.py --all --assignee` | 10 -> corrected | `--all` load-bearing; my seat-count figure was wrong until DS corrected it |
| raw `git`/`aws` verification | primary all session | pin re-derivation, AST identity + negative control, ETag/md5, marker vintages. Rule 21 two-stage: tool localizes, raw drills in |

**Instrument caveat:** `audit-archive-invoker` alleged NON-APPEND TAMPER on `org/rcg-sweep-audit.log`; git
shows 22 insertions / ZERO deletions and line 1 byte-identical to HEAD. I did NOT open the invoker's own
baseline, so this is a REPORTED DISCREPANCY, not a verdict on the tool. Routed to CTO, still open.

## The pattern this session kept producing
Six instances of one shape, and I authored two of them: **a check that passes on the confirming limb.**
The composition gate (sum holds, vintage wrong) · `_provenance.written_by` (self-report by the last writer) ·
`_latest_key()` (a frozen partition reads healthy) · complete.json read without failed.json · my negative
control without CVO's positive one · "the gold file exists" as acceptance.
**A GATE THAT WILL NOT GO GREEN MAY BE THE ONLY THING IN THE ROOM THAT IS WORKING** -- `inf-nna-excusals`
was the proof, and the fabric spent the afternoon converging on the opposite conclusion.

## Open at hand-off
- **INF chain down 5 days** -- 0.7.0_AE diagnosing read-only, cause unknown. ANDREW NOTIFIED.
- MDPF W1 in flight (DS), W2/W3/W4 staged; Ruling 2 seated behind W1.
- ANDREW: freshness-deferral scope question (I did NOT hold DEP2 on it, reasoning recorded).
- CTO: 17 prompt.md pointer sweep (payload amended, superseded edits sitting in-tree, MDPF-deferred);
  `deploy_ledger` KeyError 'log' at `cmd_close:318` -- gate can RED forever, tool cannot close;
  the preserve-then-close ruling; the invoker discrepancy.
- CVO: served-layer verify on 9a1856bc03, then the emitted report after the 2026-08-06 13:00Z fire.
