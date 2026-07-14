# 0.7.0_AE_CloudOps -- OPAL_ASSETS: C1 monolith LIVE, C2 mirror collision self-caught, C9 STOP, and a 685MB self-inflicted incident

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, DIAGNOSE, COORDINATE
**serial:** 0.7.0_AE_CloudOps | **date:** 2026-07-14 | **window:** ~01:09Z (session start) -> ~04:10Z

## Summary

Andrew's exclusive NFRA_WEBSITE assignment ended mid-startup when COO dispatched OPAL_ASSETS.C1 (the
monolith bucket) -- the P0 critical path four agents block on. Delivered C1 LIVE (bucket + prefix grammar +
router IAM one-way fan-in fence, applied + independently re-verified by COO). Built the INF sentinel deny as
a superset policy, then CANCELLED it per Andrew-direct ("no more sentinels and alarms; new territory"). Then
caused and repaired a branch-blocking incident (a 685MB terraform provider .exe committed via a directory
pathspec). Delivered C2 (polling mirror) infra LIVE -- and its first backfill exposed a data-corruption bug
IN MY OWN CODE (dst-key collision) that MY OWN denominator guard passed; caught it, fixed it, mutant-tested
the fix. C9 became a STOP-and-route (49F input traces into bd/RPS held domain) that Andrew ruled correct and
answered by lifting the whole 49F/bd sovereign block. Started the Andrew-direct connector sweep.

## Andrew-direct instructions (VERBATIM, recorded + broadcast same turn per org/XXX.md)

Channel: COO relay of Andrew's interactive channel, 2026-07-14.
1. (~02:05Z) *"We're building this in parallel, there should be no reason to touch the existing
   buckets/structures, we are building a new territory."* -> THE NEW-TERRITORY RULE (a TF plan not pure
   "to add" is out of scope). Recorded; C2 reshaped around it.
2. (~02:05Z) *"I dont want more sentinels and alarms, i have made it excessively clear this is not
   productive..."* -> sentinel deny CANCELLED.
3. (~03:3xZ) *"Oh that is retarded, 49 is back on the menu now, take the sovereign block off completely,
   that is no excuse to not verify the work."* -> the 2026-07-09 49F/bd/RPS/Schwab sovereign block LIFTED
   ENTIRELY (triggered by my C9 stop). INF chain hold SEPARATE + unchanged.
Broadcast to COO same-turn each time; COO carried to CTO/MSTR + folded into PRD/memory.

## Work done (chronological)

1. **Startup + /watcher REAPED AN ORPHAN.** Fresh session found `inbox-watch.sh 0.7.0_AE_CloudOps stream`
   pid 2851729, parent DEAD -- draining my inbox, manufacturing REACHABLE. Killed it, armed a fresh Monitor
   (task bmdoa3z72). Second consecutive session my serial was orphaned. Registered, serial-file, hooks, comp
   context. LD-0290 honored.
2. **C1 -- THE MONOLITH.** Authored `opal-data-assets` (versioning-without-expiry ruling 17, AES256 default,
   NO deny statement per 13a-amended after a build-with-dissent/revert cycle, PAB, no CORS) + the router IAM
   (three-belt one-way fan-in fence: structural NotResource + enumerated 17 source buckets + Door-6 sentinel
   Deny; per-source write policies scope-enumerated so 0824/0833 cannot commingle by construction). Applied
   via safe-apply under CTO GO. Half-landed on an IAM-tag-charset ValidationError (parens rejected in IAM tag
   values); FINISHED in-session (NEVER#6). 0-diff verified. Fence EXERCISED: live simulate, exact object-key
   ARNs, one --resource-arns/call, with a PAIRED instrument control (real INF writer allowed / router
   explicitDeny on the SAME ARN) proving the instrument can fail. Grammar probed 10/10 under `_probe/`.
   Tag opal-assets-v0.4.0. COO independently re-verified against live AWS -> RAVC-4 CLOSE.
3. **THE SENTINEL DENY -- built then CANCELLED.** Measured BEFORE writing HCL that opal-data-inf's bucket
   policy is console-managed (TF-unowned) and carries two live ADVI CloudFront grants; a deny-only policy
   would REPLACE them (singleton) -> ADVI outage. Built it as a SUPERSET in a dedicated module, import-then-
   plan (0 add/1 change/0 destroy, zero removal lines). Then Andrew cancelled it. Unwound cleanly:
   `terraform state rm` (state-only, zero AWS mutation), module deleted, inf-pipeline pointer comment
   reverted; opal-data-inf verified byte-identical to found state.
4. **THE 685MB INCIDENT (self-inflicted, repaired).** A `safe-commit` DIRECTORY pathspec force-added the
   `.terraform/` provider cache (685MB .exe) into commit e5a8d90fb, GH001-blocking every push to CLOUD for
   all agents. Also a `reset --soft` in the shared worktree orphaned 0.6.2's commit 2d4dda428. Andrew
   authorized the history rewrite. Removed the deny rule from settings.json (audited), ran filter-branch in
   a THROWAWAY BARE CLONE (never touching the shared worktree's live agent edits), pushed the cleaned
   fast-forward, restored the deny rule. Verified: count preserved, all authors intact, blob gone, 2d4dda428
   still recoverable. Published old->new SHA map. Root cause (`.terraform/` ignored for one hardcoded path
   only) closed by CTO~Z's global rule.
5. **C2 -- THE POLLING MIRROR.** Authored the mirror (raw-only ruling 16, three rows, denominator mandate
   built in) + TF (new Lambda + 2 schedules grounded on live pull windows, C1's fenced role, pure to-add).
   Surfaced the orion-generation fork (flat vs date-dir), CTO ruled flat generation (my rec). Applied 8/0/0.
   **First backfill exposed a COLLISION BUG IN MY OWN CODE:** `_dst_key` stripped the {type} segment, so
   same-date objects across 4 types overwrote each other (4640 orion -> 2269 corrupt keys), and MY
   write-counting denominator PASSED it ("OK: mirror cycle complete"). First diagnosis was throughput
   (labelled INFERRED because logs were missing); logs arrived and corrected it. Fixed: per-row strip_prefix
   preserving {type} + pre-write injective collision guard + distinct-landings denominator + concurrency=1
   (CTO permanent-shape). MUTANT-TESTED locally (guard RAISES on synthetic type-collapse). Plan 0/1/0 on
   CTO's gate. NOT applied, NOT re-run.
6. **C9 Phase A -- STOP-and-route.** Read-only grounding showed the 49F ETFS_CANON input traces into
   bd-49f-etf-ownership-daily-canonical + avgcap_bd_rps_recon.py = bd/RPS/49F held domain. STOPPED at the
   finding, took zero bd reads, routed same-turn (the door declined). Andrew ruled the stop CORRECT and
   lifted the block; Phase-A grounding reopens (queued behind C2).
7. **C6 contract + connector sweep.** ACKed DS's C6 event contract (fan-in shape = his call, I wire
   monolith-side; he chose (a) queue+debounce). Started the Andrew-direct connector sweep: enumerated 134
   EventBridge rules (paginated past the 100-cap lie) + 7 scheduler = 141 ligaments, state-classified,
   held-discriminated. Deferred the landed-bytes verdicts (my first prefix guesses were unverified -- the
   instrument-lying trap -- did NOT report them as failures).

## >> THE FINDING THAT BECAME DOCTRINE <<

**A CONSERVATION GUARD CONSERVES THE WRONG THING IF THE QUANTITY IS WRONG -- count what LANDS, not what you
DID.** My denominator mandate (built to stop the component lying about its own work) counted copy_object
CALLS, not DISTINCT LANDED KEYS -- so 2781 writes collapsing onto 2269 keys read as clean. CTO ruled it
estate-wide: every conservation guard in the consolidation is audited on "does it count the actual landed
property or a proxy (writes/calls/rc/presence)?" 0.6.2's 6,932/6,932 held because it computed SET-IDENTITY.
Folded as the connector sweep's FIFTH verdict per ligament.

## Deployment Sequence + Verification (AE)

| Step | Commit / action | Verify (EXERCISED / live) |
|---|---|---|
| C1 apply | `dc81fd20c` code, `safe-apply` | head-bucket OK us-east-1; SSE=AES256; versioning=Enabled; get-bucket-policy=NoSuchBucketPolicy; 0-diff plan |
| C1 half-land fix | de-parenthesise IAM tag; re-apply | apply completed; bucket+IAM consistent; NEVER#6 satisfied |
| C1 fence | live simulate-principal-policy | router explicitDeny on inf sentinel/bronze + cot; allowed on monolith; PAIRED control: inf-api-txn-role ALLOWED on same ARN router DENIED |
| C1 tag | `opal-assets-v0.4.0` | pushed --follow-tags |
| 685MB strip | filter-branch in bare clone | count preserved, authors intact, blob gone, fast-forward push |
| C2 apply | `a22295c9c` | 8/0/0; both schedules ENABLED+NEW; Lambda Active 512/900 |
| C2 backfill | async invoke | COLLISION found: 2269/4640 orion, 624/624 eclipse, 30/30 cot; source-confirmed from logs |
| C2 fix | `55dd545d2` | plan 0/1/0 (code hash + concurrency -1->1); mutant-test: guard RAISES on synthetic collapse |

## Compiler Tools

| Tool | Situation | Result | Note |
|---|---|---|---|
| `comp-iam gaps` | C1 IAM baseline + post-change | PASS | 2 pre-existing gaps (astn, etfs-reports, other lanes); ZERO new. Correctly NOT used as new-bucket acceptance (fails GREEN) |
| `simulate-principal-policy` | C1 fence acceptance (Rule 22a) | PASS | one --resource-arns/call; paired instrument control; first control was WRONG (measured author not instrument) -- caught via get-role-policy |
| `comp-grep`/`comp-glob` | C2 map grounding, C9 producer trace | PASS | rail-checked on live-state aws (no comp-tool models S3 layout / bucket policy / EventBridge) |
| `terraform validate`/`fmt`/`plan` | C1, sentinel, C2, C2-fix | PASS | 0-diff C1; 0/1/0 sentinel + C2-fix; 8/0/0 C2 |
| `commit-gate.sh` | mirror lambda x2 | PASS | py_compile + AST + ruff clean |

**What worked:** live primitives as the authoritative oracle throughout (head-bucket, get-role-policy,
get-bucket-policy, ListObjectsV2 landed counts, CloudWatch metrics); the mutant-the-guard test locally
before trusting the fix. **What failed / instruments that lied:** (1) an orphan watcher (reaped);
(2) `aws s3api list-objects-v2 --delimiter /` returned None (MSYS-mangled) -- nearly authored ARNs against
"empty" held buckets; (3) `git push --dry-run` reported success on the 685MB blob (dry-run doesn't transfer
the pack -> can't detect the receive-side failure); (4) `length(Rules)`=100 was the CLI page cap not the
total (real: 134); (5) MY OWN denominator counted writes not landings. **Gap (load-bearing):** a conservation
guard must assert set-identity/distinct-count, never a write/call tally -- now doctrine + connector-sweep
verdict (e).

## MCP traffic

~30 significant. **Out:** Andrew-direct verbatim broadcasts (new-territory, no-sentinels, 49F-lift) ->
COO/CTO/MSTR; C1 RAVC-2/3/4 -> COO; sentinel finding (singleton/ADVI-outage) -> COO; 685MB [STOP] + hold +
SHA map -> COO/0.6.2/0.5.0/DS; C2 map fork + RAVC-3 -> COO; C2 stall [STOP] + collision SUPERSESSION [STOP]
+ corrected-fix plan -> COO; C9 STOP finding -> COO; C6 contract ACK -> DS; unblock GOs -> 0.6.2.
**In:** COO GOs (C1, sentinel-placement, C2 apply, C2-fix gate bar), rulings relays (13/13a-amended/14/15/16/
18, v1.4.4 flat-gen, concurrency-permanent-shape, distinct-landings-doctrine), C9 close + reopen, DS C6
decision, 0.6.2 SSE/scope/orphan coordination.

## Files Modified

See commit messages: `dc81fd20c` (C1 monolith.tf + router_iam.tf + inf-sentinel-deny + inf-pipeline pointer),
`0d5b0cdda` (C1 apply evidence + IAM tag fix), `6105adec3` (sentinel removal), `a22295c9c` (C2 mirror lambda
+ mirror.tf + source-map), `55dd545d2` (C2 collision fix). Blob strip: history rewrite 6d030a99d..5305bbb65.
**AWS state:** opal-data-assets LIVE; opal-assets-ingest-router-role + fence + 7 write policies + read policy;
opal-assets-ingest-mirror Lambda + 2 schedules. **Deleted (AWS):** none this session (sentinel never applied).

## Blockers

**None self-owned that are stranded.** Correctly gated:
- **C2 fix apply** -> CTO's gate (plan 0/1/0 ready, gate-bar item 1 met). Not stranded -- on his desk.
- **The 2,269 corrupt orion orphan keys** -> ANDREW's deletion call (s3-rm human-confirmation class; source
  intact so re-derivable). Routed with rec; NOT deleted on my authority.
- **C9 Phase-A grounding** -> reopened, queued BEHIND the C2 close (no mid-backfill context switch).

## >> SESSION-REFRESH HANDOFF -- READ THIS FIRST, FRESH AGENT <<

You are 0.7.0_AE_CloudOps continuing OPAL_ASSETS. Do startup (org/XXX.md + /watcher -- EXPECT AN ORPHAN
WATCHER on this serial, reap it before arming). Then this is your board, in order:

**1. THE ONE LIVE ACTION, gated: apply the C2 fix.**
   - Fix is committed (`55dd545d2`), pushed, planned `0 add / 1 change / 0 destroy` on the existing
     `opal-assets-ingest-mirror` Lambda. It is ON CTO's gate via COO. **Do NOT apply until CTO GOs it through
     COO.** When he does: `safe-apply` in `infra/aws/terraform/opal-assets/` -> then the C2 close bar below.
   - Gate-bar item 1 (mutant-test the fixed guard) is ALREADY MET and recorded. Items 2+3 are POST-APPLY.

**2. TWO THINGS ARE HELD ON A HUMAN -- do NOT do them yourself:**
   - **The 2,269 corrupt orion orphan keys** in `s3://opal-data-assets/orion/inflection/bronze/*.jsonl.gz`
     (flat, no /type/ segment) are ANDREW's DELETION call (s3-rm = human-confirmation). They are corrupt
     COPIES; the source in opal-data-inf is INTACT, so deletion loses nothing. Clean path = delete-then-
     clean-re-backfill. **DO NOT delete on your own authority; DO NOT trust those 2,269 objects as data.**
   - **C9 Phase-B (any 49F fix)** scopes through CTO's Rule-22 gate. The 49F/bd block is LIFTED (verify is
     now demanded), but the INF chain hold is SEPARATE + UNCHANGED (Door 5/6, frozen 3, mdpf freeze stand).

**3. DO NOT RE-RUN THE C2 MIRROR before the fix is applied** -- it writes MORE collisions. After the fix
   applies, a re-run IS the clean backfill.

**4. TRAPS that bit me this session, so they don't bite you:**
   - `aws s3api list-objects-v2 --delimiter /` returns None (MSYS-mangles the bare `/`); use `aws s3 ls`.
   - `git push --dry-run` reports success even on a GH001-oversized blob; it does not transfer the pack.
   - `length(Rules)` = 100 is the CLI page cap, NOT the total (134 rules exist); paginate.
   - NEVER pass a DIRECTORY pathspec to safe-commit (it force-adds gitignored `.terraform/` = the 685MB
     incident). Enumerate explicit FILE paths.
   - comp-iam FAILS GREEN on a new bucket; a fence needs a live simulate + a PAIRED control on the exact ARN.
   - A conservation guard must count DISTINCT LANDINGS, not writes/calls/rc -- doctrine now.

**5. QUEUED behind the C2 close:** C9 Phase-A grounding (read the bd 49F producer, calendar-first, Rule 22);
   the connector sweep landed-bytes verdicts + its 5th verdict (guard-counts-landed-not-proxy); C6 monolith-
   side (a) queue+debounce wiring when DS's converter nears deploy.

**Coordination is COO's lane (2.0.0_SA_COO). Apply gates + arch forks go to CTO through COO. Andrew writes
directly to workers -- record verbatim + broadcast same-turn.**

## Current State (handoff surface -- zero prior context assumed)

- **C1 COMPLETE + LIVE + CLOSED.** `s3://opal-data-assets` (us-east-1, AES256 default, versioning on, no
  bucket policy, no KMS). Router role `opal-assets-ingest-router-role` fenced (provably cannot write any
  source; Door-6 sentinel key explicitDeny). Tag opal-assets-v0.4.0. TF: `infra/aws/terraform/opal-assets/`
  (monolith.tf, router_iam.tf).
- **C2 infra LIVE, backfill OPEN pending the fix.** Lambda `opal-assets-ingest-mirror` (512/900,
  concurrency going 1). Schedules `-inf-daily` cron(15 14), `-cot-daily` cron(30 3), ENABLED. **orion holds
  2269 CORRUPT type-collapsed keys** (do NOT trust them). eclipse (624/624) + cot (30/30) are CORRECT.
  The fix (commit 55dd545d2) is planned 0/1/0, awaiting CTO's gate. Handler:
  `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py`, TF: `mirror.tf`.
- **C2 close bar (post-fix-apply):** clean serialized re-backfill -> 13c listing verify per row -> ruling-16
  negative probe (a known parquet-only INF date lands NO object) -> idempotent re-poll -> distinct-landing
  conservation EXERCISED -> 4-distinct-types-per-orion-date on landed bytes -> per-source backfill table.
- **The sentinel is CANCELLED-SOVEREIGN**; opal-data-inf untouched (its 2 ADVI grants intact). Door-6 held
  institutionally + by the router role's Deny; ETag baseline fbcddcbf.../135B is a MANUAL reference only.
- **CLOUD branch healthy** (blob incident fully repaired; 0.6.2's 2d4dda428 recoverable).

## Next Steps

- **[1.0.0_SA_CTO]** gate the C2 fix plan (0/1/0, commit 55dd545d2). Gate-bar item 1 (mutant-test) met.
- **[Andrew]** the 2,269 corrupt orion orphan-key DELETION (source intact, re-derivable; delete-then-clean-
  backfill is the clean path).
- **[0.7.0_AE_CloudOps]** on CTO gate: apply C2 fix -> clean serialized re-backfill -> full expanded close
  bar -> RAVC to COO. THEN C9 Phase-A grounding (49F bd producer, calendar-first). THEN the connector sweep
  landed-bytes verdicts + the 5th (guard-counts-landed) verdict. C6 monolith-side (a) queue+debounce wiring
  when DS's converter nears deploy.
- **[0.4.0_DS_ClientPlatform]** C6 converter; the three-way schwab {master,date} completeness thread with 0.6.2.
