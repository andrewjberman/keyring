# Deploy-completion ledger: ADVI_PERFRP -- advi:gold `_code/` sync, COMPLETE 6 of 6 (3 + 3 after the sovereign discharge)

**Status:** CLOSED-COMPLETE. **71 MATCH / 0 STALE.**

⛔ **SCOPE LIMIT ON THIS ENTRY'S OWN COMPLETION EVIDENCE -- added 2026-09-01T07:0xZ, and it is the
limit a future reader most needs.** Every `71 MATCH / 0 STALE` in this file comes from
`comp-pipescript deployed`, which compares **LOCAL WORKTREE <-> S3**. It does **NOT** compare
**ORIGIN <-> S3**, so it certifies that the served bytes are the ones this seat intended to serve --
and says **NOTHING** about whether those bytes are on the record.
>> **A CLEAN `MATCH` IS NOT A STATEMENT THAT THE MATCHED BYTES ARE PUSHED.** A currency check against
   the DEPLOYED plane is not a currency check against the RECORD. <<
**MEASURED CONSEQUENCE, and it is why this limit is not theoretical:** from 00:10:20Z until the
integration push, `s3://opal-data-49financial/_code/` served bytes whose authorizing commit
(`9c7011f93d`) was **NOT on `origin/CLOUD`** -- the served plane AHEAD of the record, the inverse of
the staleness class this entry was opened for. **The instrument above could not have detected that by
construction**, and it did not: it was found by a separate `ls-remote` + `merge-base --is-ancestor`
read, positive-controlled. `0.7.0_AE_CloudOps~G` 90887 confirmed the same limit against its own
activation sweeps and corrected its ledger @`2912ff3973`.
**Nothing in this entry's measurements is retracted** -- the ETags, denominators and controls all
stand. What is added is what they never certified.

✅ **DIVERGENCE CLOSED 2026-09-01T07:0xZ -- MEASURED, INCLUDING THE COMPARISON THE INSTRUMENT ABOVE
CANNOT MAKE.** The integration push landed; `origin/CLOUD` @`2912ff3973`.
```
ANCESTRY, my own ls-remote + merge-base, with BOTH controls:
  9c7011f93d                                  -> ON ORIGIN
  79a2eff0ed  POSITIVE CONTROL                -> ON ORIGIN   (instrument can read TRUE)
  ffff...ffff NEGATIVE CONTROL                -> not ancestor (instrument can read FALSE)

SERVED ARTIFACT, s3api ETag vs the values recorded at deploy time:
  perfrp_emit_core.py     6adffc4949ffbfffea2d9a3ff116ab1f   IDENTICAL
  perfrp_rollup.py        f01dd090d503776a79b16b033e5a0b27   IDENTICAL
  perfrp_transactions.py  1ebf3016a32f79311289dec08812e1e5   IDENTICAL
  -> nothing re-deployed, nothing rewound, no second act performed.

ORIGIN <-> SERVED, i.e. `git show origin/CLOUD:<path> | md5sum` vs the served ETag:
  all three  ORIGIN == SERVED
```
>> **THAT LAST BLOCK IS THE POINT.** It is the question `comp-pipescript deployed` cannot ask by
   construction, and it is the one the 6.5-hour gap turned on. **The record and the served plane now
   agree, and that agreement is measured rather than inferred from the push report.** <<
Post-push sweep unchanged: 71 object(s) / 71 checked / 0 unrendered -> **71 MATCH, 0 STALE**, 0 in
every non-verdict class.

---

⭐ **SUPERSEDING UPDATE 2026-09-01T00:2xZ -- THE HOLD WAS DISCHARGED AND THE REMAINING THREE LANDED.**
Andrew discharged the 2026-08-19 BUILD-ONLY cap (relayed `1.0.0_SA_CTO` 90310 s.1, record `ce77e285b1`);
90310 s.3 handed the sentinel removal to this lane BY NAME; `2.0.0_SA_COO` 90331 s.1 sequenced it GO NOW.
- Sentinel released @`9c7011f93d` (18 deletions = 8+5+5, the whole comment BLOCK), `SERVE-RELEASE-ACK:`
  on one line, `comp-pipescript io --pipeline advi` rc=0 on all three.
- Re-derived TWICE before syncing (bound): both runs 71/71/0 unrendered, 68 MATCH / 3 STALE, identical
  set, 0 non-verdict rows.
- Deployed via `safe-deploy.sh`, per-script `VERIFY OK`, rc=0. **Never `aws s3 cp`.**
- POST-SYNC: `71 object(s), 71 checked, 0 unrendered -- 71 MATCH, 0 STALE, 0 TIMEOUT,
  0 AWS_UNREACHABLE, 0 ETAG_NOT_COMPARABLE`.

| file | ETag now | written (s3api, UTC) |
|---|---|---|
| `perfrp_emit_core.py` | `6adffc4949ffbfffea2d9a3ff116ab1f` | 2026-09-01T00:10:20Z |
| `perfrp_rollup.py` | `f01dd090d503776a79b16b033e5a0b27` | 2026-09-01T00:10:24Z |
| `perfrp_transactions.py` | `1ebf3016a32f79311289dec08812e1e5` | 2026-09-01T00:10:28Z |

⛔ **THIS CLOSES THE `_code/` SYNC ONLY. IT IS NOT AN ACTIVATION SIGNAL.** `2.0.0_SA_COO` 90368 s.1
WITHDREW this lane's completion report as the CALL 2 trigger, and `1.0.0_SA_CTO` 90378 HALTED the
P4I-3 serve on an unmet pseudonymisation precondition (`perfrp_book_advisor.json`: 3,290 real client
display labels). Resumption needs a new message from `1.0.0_SA_CTO` citing that precondition MET, or
an Andrew waiver given with that fact in front of him. The 08-19 and 08-21 holds remain DISCHARGED --
the serve halt is an unmet ENGINEERING precondition, not a re-imposed sovereign hold.

⛔ **AND THE SERVE-RELEASE AUDIT DID NOT FIRE ON THIS RELEASE -- A FAIL-OPEN, REPORTED AT 90422.**
`_resolve_serve_refs` pins `old_ref="HEAD~1"` for an explicit-file invocation. Two peer commits landed
in the 12 minutes between `9c7011f93d` and the deploy (`9f0d8a84dc` at 00:10:17Z, **3 seconds** before
the first object write), so `HEAD~1` was `be22deaf9e` -- already past the removal. Sentinel count there
is 0/0/0; at the release commit's TRUE parent `a50dd6721a` it is 1/1/1 (positive control). So
`removed` came back empty and the ACK check AND the audit write were BOTH skipped. **A valid ACK was
present and never read; with no ACK at all this deploy would have run identically at rc=0.** The
`:283` header claim "All three checks FAIL CLOSED" holds for every ERROR path and does not cover this:
nothing errored, the PREMISE lapsed. Owner `1.0.0_SA_CTO`; not fixed here, and a fix must not loosen
either regex -- the defect is the chosen BASELINE.

---

*Original entry, at the time only three rows could land, retained unedited below.*

# (ORIGINAL) advi:gold `_code/` sync, 3 of 6 SERVED and 3 SOVEREIGN-HELD

**Status:** CLOSED (partial by design -- see HELD REMAINDER; this is NOT an open deploy and must NOT be re-executed)

⛔ **THIS IS NOT A RED/OPEN ENTRY AND NEVER-2 IS NOT ENGAGED** -- `2.0.0_SA_COO` 90236 s.3, verbatim:
*"this is NOT a half-landed deploy -- no red ledger entry belongs here. The 3 that landed are complete
and verified; the 3 that did not were REFUSED BY A GATE DOING ITS JOB. A gate refusal is not an
incomplete act."* This file exists ONLY as the CLOSED completion record for the three objects whose
served bytes moved -- it holds their pre/post ETags, which nothing else in the fabric carries. If the
issuer wants no artifact here at all, delete it; this lane is recording, not adjudicating.
**Opened:** 2026-08-31T23:1xZ (first object write) | **Closed:** 2026-08-31T23:2xZ (post-sweep read)
**Operator:** `0.4.0_DS_ClientPlatform~G` | **Deploy executed by:** `.tools/safe-deploy.sh` (Rule 13 DS lane), `HALT_ACK=1`, rc=0

**Authority:** `2.0.0_SA_COO` msg-id 90157 (seating, ADVI_PERFRP only, Rule 27) + `1.0.0_SA_CTO` msg-id
90172 s.3 (RULING: this sync COMPLETES BEFORE any P4I-3 publish activation -- a hard precondition, not a
cleanup). Reproduction handed over by `0.7.0_AE_CloudOps~G` at 90166. Report out: 90231-90234.

## Scope
Repo home `data/assets/scripts/gold/runners_49f/` -> `s3://opal-data-49financial/_code/`
(`safe_deploy_core.py` CODE_TREES `advi`, `deploy_gated: True`).
Worktree == `git show HEAD:<path>` for all six (md5, independent of the deploy tool); HEAD ==
`origin/CLOUD` @ `5b10b4eda0abfd6cf0e89f775e2d031496a84311`. **So the bytes served ARE origin's bytes**,
and the autocrlf class is excluded by measurement (`safe-deploy` independently: `worktree CR count 0 /
index CR count 0 / uploaded: index`).

### SERVED -- 3 of 3 attempted, each `VERIFY OK` per-script
| file | pre-sync S3 ETag | post |
|---|---|---|
| `a01_runner.py` | `e6ab112d7dac8a3a41b5597f3b41663b` (2026-08-19T01:22:33Z) | MATCH |
| `d06_firm_mix_summary.py` | `09f568f363913215540c35ee5da98412` (2026-08-19T01:22:37Z) | MATCH |
| `d14_advisor_nna_canonical.py` | `89f624d99e6176cc09133ac4f6bf6f7e` (2026-08-19T01:22:38Z) | MATCH |

### HELD REMAINDER -- 3 REFUSED, objects UNTOUCHED at their prior ETags
| file | S3 ETag (unchanged) | LastModified |
|---|---|---|
| `perfrp_emit_core.py` | `de684c77a72f8d879db38e30cdd2d61c` | 2026-08-25T07:17:50Z |
| `perfrp_rollup.py` | `f5495d7604abc764d7a63972883758a1` | 2026-08-25T07:18:01Z |
| `perfrp_transactions.py` | `3db19e6ae5bab05a9ebe1dc30b6a34a2` | 2026-08-25T07:18:04Z |

**REASON -- a machine-enforced sovereign hold, at LINE 1 of each of the three:**
`# DEPLOY-SERVE-HELD: ADVI_PERFRP.TO-R2-DS is BUILD-ONLY (Andrew 2026-08-19 open-calls`
Enforced by `.tools/safe_deploy_core.py:290` (`SERVE_HELD_RE`); `:281-282` records that REMOVING the
sentinel IS the act of authorizing serve and is itself gated. **Not taken by this lane.**

**RELEASE PATH (added from `1.0.0_SA_CTO` 90240 s.2, source-verified by that seat at `:285-296`):**
this is gated, not impossible -- an authorizing commit carries `SERVE-RELEASE-ACK: <reason>`,
non-empty, on the same line, tied to NEVER#2 never-widen. So the ask to Andrew is precise and small.
⚠ Both regexes FAIL CLOSED by construction, and the `[ \t]*` (not `\s*`) in the ACK pattern is
deliberate: `\s*` would cross the newline and let an empty ACK capture the next commit line as its
reason -- a fail-OPEN inversion. **Nobody may "fix" that to be more permissive.**

**TWO SOVEREIGN HOLDS, NOT ONE (`1.0.0_SA_CTO` 90240 s.3 -- surfaced, NOT adjudicated):**
| date | hold | scope |
|---|---|---|
| 2026-08-19 (open-calls) | `ADVI_PERFRP.TO-R2-DS` BUILD-ONLY | the SCRIPT-SERVE sentinel -- blocks deploying PRODUCER CODE to `advi:gold _code/` |
| 2026-08-21 | the 49F-FLIP hold | the P4I-3 PUBLISH ACTIVATION -- blocks serving CLIENT-FACING DATA to the portal |

**Different dates, different scopes, different risk. Deploying producer code publishes no
client-facing data.** Collapsing them makes the cheaper, safer act look like it costs the expensive
decision. Whether the 08-19 word discharges separately from the 08-21 word is Andrew's to say.

>> **THE SEATING'S OWN BOUNDARY IS THE BLOCKER.** 90157 s.3 scoped this sync "inside the BUILD-ONLY
   cap" and named `perfrp_emit_core.py` as the first target. The cap is what forbids serving it.
   `1.0.0_SA_CTO` 90172 s.3's clause "This ruling is INSIDE the BUILD-ONLY cap and consumes no part of
   the sovereign publish decision" is **FALSE for these three rows** (true for the three that landed).
   The ruling's SEQUENCE survives; its cap-claim does not. Reachable order:
   **Andrew lifts BUILD-ONLY for the serve -> sentinel removed -> sync completes -> activation.** <<

## Verification
`comp-pipescript deployed --pipeline advi`, run twice PRE (per 90166 s.3 -- a TIMEOUT is not a MATCH)
and once POST. Denominator every run: **71 object(s) / 71 checked / 0 unrendered.**

```
PRE  (both runs, identical set)  65 MATCH, 6 STALE, 0 TIMEOUT, 0 AWS_UNREACHABLE, 0 ETAG_NOT_COMPARABLE
POST                             68 MATCH, 3 STALE, 0 TIMEOUT, 0 AWS_UNREACHABLE, 0 ETAG_NOT_COMPARABLE
POST STALE = exactly the three HELD rows.
```
The 15 `MISSING_ON_S3` are all `[SILVER]` rows (a different channel); the 1 `DECLARED-UNSWEPT` is the
lambda-zip channel the tool scopes out on its own face. Neither is in scope; neither was widened into.

**Negative control on the sentinel:** the three files that DEPLOYED carry `DEPLOY-SERVE-HELD` zero
times -- the sentinel is the discriminator, not an artifact of which files were newest.

**No fresh-against-stale pair was manufactured by the partial landing:** none of the three SERVED files
references any of the three HELD files. Positive control -- the same pattern does find the real
importers (`d_publisher_port.py`, `perfrp_activity_account.py`, et al).

**`d_publisher_port.py` still reads MATCH post-sync** (0.7.0_AE_CloudOps~G 90166 s.5), basis "raw bytes
... byte-identical", so the `deferred` disarm at `:589-591` is live on both planes. ~~and the served
denominator at activation stays **10 of 11**~~

⛔ **THE "10 of 11" IN THE STRUCK CLAUSE IS SUPERSEDED -- annotated 2026-09-01T01:4xZ, not adjudicated
here.** `1.0.0_SA_CTO` 90509 s.5 retracted that figure as its own: *"I ... broadcast 'the activation
denominator is 10 of 11' three times -- a figure I DERIVED from a clause about one key and never
censused. The measured would-publish set is FOUR."* Corrected by `0.7.0_AE_CloudOps~G`'s plural census
after a serve precondition had been censused on ONE leaf of FOUR (examined leaf 57 rows, unexamined
sibling 8,632).
⚠ **I REPEATED THAT FIGURE WITHOUT DERIVING IT** -- I carried it from 90157 s.4(a) / 90172 s.5 into
this ledger as though it were measured. Struck rather than deleted so the record shows what this
ledger asserted and on whose authority.

⭐ **GRAIN RESOLVED 2026-09-01T03:1xZ, by the seats that own it -- cited, not derived here.**
`2.0.0_SA_COO` 90619 states it plainly: **"only 4 of 11 families write"** -- so FOUR counts EMITTER
FAMILIES that write, matching `0.7.0_AE_CloudOps~G`'s plural census. When this annotation was first
written the grain was genuinely open and I declined to infer it; that restraint was right and the
answer then arrived from the right seats. Recorded here so this carrier is self-contained rather than
pointing at a number it does not hold.
⛔ **AND THE LIVE INSTRUCTION THAT TRAVELS WITH IT** (`2.0.0_SA_COO` 90619): the publishable set has
MOVED TWICE against the chain docstring -- **re-read the attempted set at fire time; never score
against a remembered denominator.** That applies to 4 exactly as it applied to 10.
⭐ **Nothing else in this entry depends on it.** The figure was context for an activation this lane
never performed; the `_code/` sync's own evidence -- 71 MATCH / 0 STALE, denominators printed, positive
and negative controls -- is independent of it and stands unchanged.

## Corrections carried out of this run
- 90157/90172 both say the S3 object "predates SEVEN DS round-2 commits." **Measured: 13 commits touch
  `perfrp_emit_core.py` itself** between that object's LastModified and HEAD (36 touch the tree).
  Not called wrong -- "round-2" may be a narrower denominator that was not re-derived here. The two
  denominators are unlabelled in both records. Direction is safe: it strengthens the precondition.
- `safe-deploy` instrument item (routed to `3.0.0_SA_CVO`): handed SIX files, served three, printed
  `OK: safe-deploy gate PASS -- all 3 file(s) deployed and verified` at rc=0. **The PASS line
  re-denominates to what was ATTEMPTED, not what was ASKED FOR.**

## Collision noted, not chased (base-owned)
The HALT gate surfaced `1.0.0_SA_CTO`'s incident relay: eight `runners_49f` uncommitted edits lost to a
19:37:15Z `git checkout`. **Five of the six sync targets are on that list.** This did not change which
bytes are correct -- the lost edits were uncommitted, were never on origin, and this task is "match
origin"; worktree==HEAD is itself consistent with the revert. Recorded so the owner knows the deployed
plane is now pinned to origin for three of them. Not acked, not drained -- read from the BASE inbox.
