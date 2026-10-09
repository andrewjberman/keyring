# OG-da-1 Phase B deployed (and its blast radius corrected mid-flight); IAM-v-1 accepted; the source map recorded

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE, SCRIBE

**Serial:** `0.7.0_AE_CloudOps~Z` | **Window:** 2026-10-09 ~06:1xZ -> ~10:0xZ (continues
`logs/2026-10-09/two_nfra_oplgtw_applies_and_the_etfs_hold.md`, which closed at ~05:0xZ) | **Device:** site Z
(relaunched after the 02:58 local reboot)

Three orders moved. One deploy landed and then corrected its own signed blast radius; one governance acceptance
landed against a gate that refused it; one record commit closed an item I had surfaced as owed in the previous
report.

## Work completed

### 1. `NFRA_OPLGTW.TO-OG-da-1` -- the data_refresh admission fails closed: COMPLETE, AC1 + AC2 PASS

Phase A had landed at `d9539cc0b7` (06:52Z) with the ask and the caller census; this window ran Phase B.

**Both halves verified AT HEAD before the first act**, by reading their bytes and by `is-ancestor` on each named
commit rather than trusting the GO's words: CTO~Z `@93ddbb1288` (blob `fc82968861`, 3652 B) and COO~O
`@014c45557d` (blob `4c79003`, 3556 B). The GO itself was msg 32501, and it arrived only after I asked each
half-holder directly -- the CTO half was owed and unrequested when this session started, and one message moved it.

- **Artifact built from HEAD via `git show`, never the working tree**, so the deploy ships reviewed bytes and an
  uncommitted edit could not ride along. The member set came from the source map's own `files[]` list and the
  builder ASSERTS the built set equals it: 2 members, `lambda_function.py` 83888 B and `check_triggered_by.py`
  1825 B, 0 CRLF pairs in either (read in binary -- a text-mode read here CRLF-ifies without raising and would
  have changed every line ending and the hash).
- **Uploaded with the `content-sha256` user metadata the module reads** (`modules/yang-lambda/main.tf:39`), and
  verified by `head-object` on size AND a byte-equality comparison of the metadata string. That check is the one
  that would have caught an argv mangling of a base64 value full of slashes; `rc=0` was never the oracle.
- **Plan graded from `show -json`**, never the rendered text, which hid 28 attributes behind a redaction line.
  The one non-no-op row changed exactly `source_code_hash`, `s3_object_version` and `last_modified` -- nothing
  outside the three the ask allows. Applied from the SAVED plan so the applied set equals the audited set.
- **Read-back:** `CodeSha256 qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM=` equal to the built hash by string
  comparison, `State Active`, `LastUpdateStatus Successful`, role/environment(5 keys)/timeout 60/memory 256/
  runtime/handler identical before and after, `portal-time-machine` untouched.

**THE FINDING, AND IT WAS MINE.** The post-apply FULL root plan did not read clean. A second yang-lambda in the
same root, `module.data_refresh_api_qa_scratch` in `qa-scratch-instance.tf`, reads the byte-identical
`artifact_key`, so one upload became a pending code change on TWO resources. My own ask's section 5 said "One
Lambda's code ... Nothing else" and both halves signed that text; I had read `main.tf` and not
`qa-scratch-instance.tf` when I wrote the radius. Nothing out-of-radius was deployed -- the apply was
`-target`'d from a saved plan and the clone's live `CodeSha256` never moved -- but the root no longer planned
clean, so a full apply by any seat would have shipped these bytes to the clone with no sign-off covering it.

I did not apply it and did not revert the signed change (its read-back was exact and the halves' rollback
trigger, a caller reading REFUSED, had not fired). Filed `NFRA_OPLGTW-Z-S72` ARMED with the production and clone
reads as each other's control, held leg RB open so the entry stayed RED, and asked the half-holder for the
disposition instead of choosing one. `2.0.0_SA_COO~O` ruled disposition (b) in amendment A1 `@888b6c9699` --
pin the clone, **not ratified as a widening** -- and added `qa-scratch-instance.tf` to `<paths>`.

**The pin, executed inside that one file.** The pinned version was server-side copied to the clone's OWN key
`data-refresh/opal-data-refresh-api-qa-scratch.zip` (19753 B, ETag `15413b4ac88881c9b0e19dae0eceb215` EQUAL to
the source version's, `content-sha256 E4944Imr...` verified) and the module repointed. The plan's only non-no-op
row changed `s3_key` and `s3_object_version` while **`source_code_hash` did NOT change** -- the positive proof
the pin moves no executable byte, and a fact invisible in the rendered plan text. A version-override variable on
`../modules/yang-lambda` was refused as the mechanism: it would have put all 231 of that module's consumers in
the blast radius to fix one clone.

### 2. `NFRA_IAMROLES202609.TO-IAM-v-1` -- rows 8 and 10 accepted as owner of record: COMPLETE

GO msg 32586 from `2.0.0_SA_COO~ZI`; owner of record per `1.0.0_SA_CTO~Z` `@fa8ec0e726`. Governance only --
nothing applied, no AWS write call, the inert adopting text's blob unchanged at `b3a1298d6b...`.

Both rows accepted on the merits. **Every figure the adopting text asserts was re-measured live rather than
inherited, and all of it held**: row 8's 5 inline policies and 1 attached managed policy, with all 5 inline
declared in this module, and all THREE Lambdas in the `data-refresh` root naming the role (the text's "3
consumers", checked by printing each function's role ARN); row 10's 1 inline, 1 attached managed,
`RoleLastUsed` EMPTY, created `2026-02-19T16:00:39Z`, max session 3600 and description, every value equal to the
text. I also had first-hand custody evidence for row 8 that no other seat had today: I deployed through that
role earlier in this same window and both plan audits recorded it unchanged.

**It hit a real structural blocker, not a mistake.** The order's `<paths>` grants
`deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md`, and the owned-paths lane
`TREE_DELIVERABLES` (clause 4) reserves it to the serial named by that sub-folder; `safe-commit` refused with
`agent=0.7.0_AE_CloudOps~Z not in permitted_agents`. The audited `GIT_COMMIT_AUTHOR_OVERRIDE` escape was
**refused, and not out of caution**: committing as the worker would have failed the order's own AC2 BY
CONSTRUCTION (it grades that file's author as this lane) and produced exactly the forged acceptance the cell
text forbids. Filed `NFRA_IAMROLES202609-Z-S19` BLOCKING with both dispositions, left the prepared edit
uncommitted so no work was lost, and said so in the acceptance document's own header so no reader could mistake
the document for a landed row edit. `2.0.0_SA_COO~ZI` ruled option (a) `@193ee5ac41`, amended AC2 to grade the
acceptance document's authorship, and landed my prepared text verbatim as carrier `3bd5f1d1d4`. **I verified
that "verbatim" with a whole-file diff of my worktree against HEAD (IDENTICAL) rather than accepting it.**

### 3. The source map -- the item I had reported as owed

`infra/aws/lambda/ci/lambda-source-map.json` carried this function's pre-deploy values. It was not in OG-da-1's
`<paths>`, so I surfaced it rather than hand-editing; `2.0.0_SA_COO~O` added it to OG-ap-3's `<paths>` in
amendment A1 `@fcd9717783` (its own lane cannot write the file). Verified the grant at HEAD before writing --
the path at line 67, A1 at line 102, `fcd9717783` contained -- then applied it as a SURGICAL TEXT EDIT, not a
json round-trip, so the shared 231-entry file is not reformatted under a peer's feet. The result was ASSERTED to
differ on exactly three lines (458, 459, 460); the file still parses and `files[]` is untouched.

## Deployment sequence + verification (AE role-specific) -- ACTUAL output

```
07:44Z  deploy_ledger.py open   nfra-oplgtw-og-da-1-data-refresh-admit  OK: OPENED (3 legs)
07:5xZ  s3api put-object        VersionId f0pfQmR1BByh9jcBQHwYymYRSfZ2IKih, 20716 B
                                head-object: Meta.content-sha256 EXACT MATCH, Size 20716
07:59Z  safe-apply (saved plan) Apply complete! Resources: 0 added, 1 changed, 0 destroyed
                                comp-tagauthz gate PASSED; tombstone-gate CLEAN (0 creates / 7 tombstones)
                                read-back: CodeSha256 qHMjXkK1... State Active LastUpdateStatus Successful
                                targeted re-plan: "No changes. Your infrastructure matches the configuration."
                                FULL root plan: 0 to add, 1 to change, 0 to destroy   <== the finding (Z-S72)
08:21Z  s3api copy-object       qa-scratch key: VersionId vd2cd6VmD378Vs1eiZgBDTZMzYJTACfM,
                                ETag 15413b4ac88881c9b0e19dae0eceb215 == source version's, 19753 B
08:24Z  safe-apply (saved plan) Apply complete! Resources: 0 added, 1 changed, 0 destroyed
                                clone read-back: CodeSha256 E4944Imr... State Active
                                FULL root plan: "No changes" (detailed-exitcode rc=0)
                                production opal-data-refresh-api: qHMjXkK1... unmoved by the pin
08:2xZ  deploy_ledger.py close  OK: CLOSED -- all 3 legs proven; sentinel removed
```

Criteria, run LITERALLY as written (not through a pipe -- their expect patterns include `exit=0`, and a pipe
reports the receiver's exit code rather than the script's):

```
OG-da-1 AC1  PASS   pytest rc=0; named tests passed 5 of 5; failed/error lines 0
OG-da-1 AC2  PASS   lambda_function.py equal-to-HEAD=True; CodeSha256=qHMjXkK1... State=Active
OG-da-1 AC3  UNVERIFIABLE-BY-INSTRUMENT -- judgment, 3.0.0_SA_CVO at L9
IAM-v-1 AC1  PASS   2
IAM-v-1 AC2  PASS   0.7.0_AE_CloudOps~Z   (one line, as amended)
IAM-v-1 AC3  PASS   b3a1298d6b2b8d99284b4211bfc0c18eaa707f19
IAM-v-1 AC4  UNVERIFIABLE-BY-INSTRUMENT -- judgment, 3.0.0_SA_CVO~Z
```

Both proof instances read `violations=0 ... VALID (rc=0)` BOUND via `--governing-order` with their declared
expected sets, and **both were negative-controlled**: the same instance against a wrong expected set returns
INVALID naming the silent omission and the unexpected additions, so the coverage limb is exercised rather than
declared. The OG-da-1 instance first read INVALID on three closed enums (`kind` 'code'/'infra', `method`
'judgment'); the IAM-v-1 instance first read INVALID on three rows because I had put the order's PROSE `<expect>`
text where the checker matches a pattern against `output_evidence`. Both fixed and re-run.

## Compiler tools

| tool | invocation | result | note |
|---|---|---|---|
| `terraform` | init; plan `-target` + `-out`; `show -json`; apply saved; re-plan `-detailed-exitcode`; then the same cycle for the pin | PASS | Every plan graded by a script that prints the changed-attribute set AND the `after_unknown` set and compares both against the ask's allow-list, so "code only" is a measured verdict rather than an eyeball of redacted text. That grader is what caught the qa-scratch row and later proved `source_code_hash` unchanged by the pin. |
| `safe-apply.sh` | `-chdir=infra/aws/terraform/data-refresh apply <saved plan>` x2 | PASS | Both from SAVED plans. `comp-tagauthz` PASSED and the tombstone gate read CLEAN on both. Its tag-authz limb printed a KEY COLLISION on `Project` for this root, which I carried into the IAM row-8 acceptance as a condition on any future adoption. No HALTGT pass is cited as evidence, per cloud-ops. |
| `deploy_ledger.py` | `open --lambda`, `close-leg` x3, `close` | PASS | `--lambda` not `--pipeline`, per the tool's own help, so `close()` does not blare on phantom S3-code legs. Leg RB deliberately held open across the finding so the entry read RED while the world was in a state the sign-off did not cover. |
| `proof-of-spec-check.py` | both instances, BOUND + declared set, each with a wrong-set negative control | PASS | Caught 6 real schema/pattern violations across the two drafts. The first run of each printed its own bound ("no expected_criterion_ids given -- COVERAGE UNCHECKED"), which is why both were re-run with the declared set rather than accepted on a bare VALID. |
| `safe-commit.sh` / owned-paths hook | 7 commits; ONE refused | PASS | The refusal is a finding, and the gate behaved correctly: in the same call it permitted my own deliverables path and refused the worker's. Treated as a routing question, never overridden. |
| `surprise-row-gate.py` | fired on 3 channel appends; `ID_RE` additionally tested directly against 3 candidate id forms | PASS | Testing the id form against the regex BEFORE writing saved a refusal round-trip and produced a second finding: the IAM order's declared `-Z-AEC-S<k>` form is refused by the gate's own regex. |
| `comp-read` / `comp-find` | named-file reads of `qa-scratch-instance.tf`, `modules/yang-lambda/{main,variables}.tf`, `lambda-source-map.json`, `scheduled_daily_pull.cmd`, `owned-paths` refusal text | PASS | Two reads changed what I did: `variables.tf` showed the module has NO pin input, which ruled out the module-variable shape and sent the pin to a separate key; `main.tf:39` showed `source_code_hash` comes from S3 USER METADATA, which is why the upload carries `--metadata`. |
| `aws iam` (read-only) | `list-role-policies`, `list-attached-role-policies`, `get-role`, `get-role-policy` | PASS | Policy names LISTED and counted client-side rather than read off a `--query length()`, per the paginated-list trap. Every call a read. |
| `comp-iam` | NOT USED | SKIP | Deliberate on both orders. cloud-ops states it models `(action)` and never `(action, resource)` and is a FLOOR, so it cannot confirm a specific ARN landed nor answer a custody question. Both orders declare it NOT-APPLICABLE and the plan audits confirmed no IAM resource in either changed set. |

**What worked:** grading plans from JSON rather than rendered text -- it found a defect that the rendered plan
could not show, and later produced the pin's own positive proof. **What failed:** a `-F /dev/stdin` heredoc
commit silently did not commit (gates all ran and passed, no commit); caught by checking `git status` and the
file's presence at HEAD rather than by reading the output tail. It also violated Rule 14a, whose message file
must be written by a non-shell writer -- redone correctly. **Gap found:** the IAM order's declared surprise-row
id form is refused by the surprise-row gate's own `ID_RE`, the same class the `MX-s-19` A3 amendment ruled when
it retired the `Z-AEMI-` form; and `--date=format` with a typed `Z` renders LOCAL time, so a `git log` "UTC"
column is wrong by the device offset unless the offset is printed.

## Blockers

1. **`IAM-v-1`'s row edit: BLOCKED, then RULED, then LANDED (closed within the window).** Evidence cited in
   section 2 above: the `safe-commit` refusal text, the order's `<paths>` granting that file, and AC2's own
   wording making the sanctioned override self-defeating. Resolved by amendment A1 `@193ee5ac41`; row Z-S19.
2. **`MDPF_SECHIST-Z-S1`: ARMED on a DARK owner, now dispositioned by its owner.** Found while taking the
   pre-window control read for the L3 order: the SH-t-4 reland is at HEAD (`19e50528d3`, "on Andrew's yes") but
   the vehicle that runs is the WORKING TREE of `etf_daily_pull.py`, which is HEAD minus that 15-line block.
   L2 is intact -- the working-tree blob `0e399c9523` is byte-identical to the blob the order pins L2 to -- so
   HEAD moved past the vehicle, not the other way. Filed ARMED because the uncommitted delta IS the deployed
   artifact, and `2.0.0_SA_COO~H1` read NOT REGISTERED, so the row was written as a PARKED carrier naming the
   condition that un-parks it. `1.0.0_SA_CTO~Z` relayed the owner's disposition at 09:02Z (msg 32597): that
   working tree IS the deployed state through the 11:00Z fire, and no checkout, stash, clean, reset or merge
   touches that path on site Z until the run is read.
3. **Not a blocker, stated so it is not mistaken for one:** the 2026-10-08 07:00 scheduled pull exited **50**
   (DAPI precondition failed, pull NOT attempted; the unsupervised sign-in fallback aborted at ZERO Bloomberg
   attempts, `C:\opal-elev\bbg_fallback_ESCALATION.txt`), and on the `rc=50` path `scheduled_daily_pull.cmd`
   jumps to `:prune` and SKIPS the ETF leg entirely -- which would leave the L3 order's manifest ABSENT. As of
   08:0xZ transport reads UP (`bbcomm` pid 36400 since 03:13 local, `127.0.0.1:8194` LISTENING with an
   ESTABLISHED link to the vendor) and `0.0.3_BG_BBGTerminal` reports `bloomberg_health ok:true`. This seat did
   NOT test entitlement: an agent-turn Bloomberg call is barred by R-21.

## Files modified

See commit messages: `d9539cc0b7`, `0422cbd3ee`, `deee55b3ef`, `99c3b4c1b1`, `5f63775be5`, `47c6a98f49`,
`1ca645fd25`, `673656f7d8`, `1416282c74`. Each carries its own per-file reasoning.

## MCP traffic

19 messages handled, all acked. The significant ones: IN 32496 (CTO half SIGNED), 32501 (Phase B GO, both
halves named), 32565 (Z-S72 ruled -> amendment A1), 32586 (IAM-v-1 GO), 32594 (source map added to my paths),
32597 (the SECHIST row's disposition), 32623 (Z-S19 ruled, carrier landed), 32540 (OG-ap-3 issued). OUT: the ask
that got the CTO half moving, the ask that got the COO half, the Z-S72 disposition ask, the OG-da-1 COMPLETE
report, the IAM-v-1 blocked report and its completion.

One send was REFUSED by the broker at 162 words against Rule 31's 150-word cap -- the rule working. I cut it to
the single ask plus file citations and it went. A separate lesson landed the hard way: a `heartbeat` re-emitted
three messages I had read off the FILESYSTEM and acted on but never acked. Reading a file never touches the READ
clock; only an ack does, and the cost lands on the sender.

## Current state

- **Live, changed:** `opal-data-refresh-api` `CodeSha256 qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM=`,
  `LastModified 2026-10-09T07:59:39Z`, State Active, runtime python3.11, timeout 60, memory 256, 5 env keys,
  role `opal-data-refresh-lambda-role`. Its admission now fails closed: `userType == 'Dev'` admits, else
  `is_opal_internal` (`tier == 'internal'` or `firmId == 'opal-capital'`, exact match after strip), else REFUSE;
  the no-authorizer path refuses and no longer names an actor of `dev@test.com`.
- **Live, decoupled:** `opal-data-refresh-api-qa-scratch` now reads its OWN artifact key and is PINNED at
  `CodeSha256 E4944Imr7Y4S4//rTR6HN5sbwczbwLw5DcaH4IZ0D0E=` -- the same bytes it ran before, so nothing about
  its behaviour moved. `portal-time-machine` untouched since 2026-03-12.
- **Rollbacks, named and available:** production artifact VersionId `WJQGGIAlTSMp0Vny8avvQ7LxflVuvLf6`
  (`CodeSha256 E4944Imr...`); for the pin, point `artifact_key` back at the production key. Bucket versioned.
- **Ledger:** `nfra-oplgtw-og-da-1-data-refresh-admit` CLOSED, 3 legs proven, sentinel removed. **No open
  deploy for this seat.** (`freshguard-leg4-writer-wiring-finish` is HELD-STALE under the base serial by design
  and gated on Andrew's word about the alarm moratorium; not this session's.)
- **Orders:** `OG-da-1` complete; `IAM-v-1` complete; `OG-ap-3` (r29 gateway apply) PENDING in its window;
  `MDPF_SECHIST.TO-READ-R2-L3` pending its window; `IAM-v-2` staged awaiting GO;
  `NFRA_MCPINDEX.TO-MX-s-19` explicitly NOT this seat's until its 10-13 re-point (amendment A6).
- **OG-ap-3 preconditions, all verified this window and all GREEN:** three halves + the ANNOUNCE at HEAD
  (CTO `@d3f04813df`, COO `@40b39ad88d`, CVO `@c348b51df9`, ANNOUNCE `@368e48e533`, all four contained);
  `C:/tmp/og-rel29` at `91811b648ab119e73e22f8d401dd09f45b8ab19b` and `C:/tmp/og-rb29` at
  `aa75078e1b72a28219e6148d3ec8e9bf705ea111`, **both survived the reboot, both clean**; the T tooling present;
  the live `gateway-read-secrets-policy` reads 1 statement and exactly 4 resources with no `commassist` ARN;
  `gateway/mail/commassist-bearer` does NOT exist (`ResourceNotFoundException`); the Terraform line
  `@98501422dc` at HEAD. **One ordering constraint worth carrying:** `gateway-read-secrets.tf:50` resolves that
  secret through a `data` source BY NAME, so a `plan` before the secret exists cannot resolve -- the ANNOUNCE's
  order of acts (create, then plan) is load-bearing, not stylistic.
- **ETFS R28-aw1:** steps 4-6 still waiting on `2.0.0_SA_COO~RV`'s second GO inside 11:15Z-12:55Z.
  `C:/tmp/rv-r8` survived the reboot detached at `39889dd4d7` with a clean tree, and
  `C:/tmp/rv_apply28.tfplan` is intact at 31454 B -- re-measured this window, because `archive_file` zips at
  plan time and re-planning would break the pairing step 5 depends on.
- Broker: live, ZERO crons, watcher re-armed on each 30-minute expiry (six arms this window, one script row at
  every census, nothing reaped).
- **Push state, MEASURED at 09:53Z:** `1ca645fd25` and `673656f7d8` ON ORIGIN; `1416282c74` LOCAL;
  `git ls-remote origin box/sitez` read `d80feca6e5`. Earlier commits through `99c3b4c1b1` are on origin.
  I pushed nothing -- box-sync is the integrator's scheduled carry.

## Next steps

1. [`0.7.0_AE_CloudOps~Z`] `NFRA_OPLGTW.TO-OG-ap-3`, inside 11:00Z-23:00Z, Half 2's acts in order: create
   `gateway/mail/commassist-bearer` (32-byte hex, value never recorded anywhere), its own ledger for the one
   policy line, then the NEVER-2 ledger and the r29 deploy with the bun-cache count that must read 0.
2. [`0.7.0_AE_CloudOps~Z`] `MDPF_SECHIST.TO-READ-R2-L3`, inside 11:45Z-13:30Z: read the 11:00Z fire's
   `LastTaskResult`, its whole fire log and the day's budget ledger into one evidence file. An `rc=50` repeat
   is a finding to write, not a failure of the order.
3. [`0.7.0_AE_CloudOps~Z`] ETFS R28-aw1 steps 4-6 on `2.0.0_SA_COO~RV`'s GO inside 11:15Z-12:55Z; apply nothing
   if it lands after 12:50Z.
4. [`3.0.0_SA_CVO~Z`] Grades OG-da-1 AC3 (each caller ADMITTED on its first real call after the deploy; 0 of 6
   observed at instance time, recorded as not-yet-observed, never a pass) and IAM-v-1 AC4.
5. [`2.0.0_SA_COO~ZI`] `IAM-v-2`'s GO; the amended v-2 has this seat prepare its rows uncommitted.
6. [`2.0.0_SA_COO~H1`] Owns whether the vehicle takes SH-t-4 after today's fire is read -- a separate act under
   its own pair, per the disposition relayed in msg 32597.
