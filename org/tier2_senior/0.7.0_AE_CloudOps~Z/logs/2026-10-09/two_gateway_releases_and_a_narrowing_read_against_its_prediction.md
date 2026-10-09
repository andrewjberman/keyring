# Two gateway releases live, a narrowing read against its prediction, and five orders closed

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE, SCRIBE

**Serial:** `0.7.0_AE_CloudOps~Z` | **Window:** 2026-10-09 ~10:1xZ -> ~16:0xZ (continues
`logs/2026-10-09/og_da1_phase_b_deployed_and_iam_v1_accepted.md`) | **Device:** site Z

Six orders moved this window; five closed. Two of them put code on the gateway host.

## Work completed

### 1. `NFRA_OPLGTW.TO-OG-ap-3` -- the r29 gateway release: COMPLETE, AC1 + AC2 PASS

Three steps, each under its own discipline.

**The secret.** `gateway/mail/commassist-bearer`, VersionId `5c368b4d-d6e8-4366-8988-92f4eb4b8fcd`, AWSCURRENT,
rotation off, 64 hex characters. **The value never left one process:** generated with `secrets.token_hex(32)` and
handed to boto3 in memory, so it never entered argv, a file, a log, Terraform state or a commit, and only its
LENGTH was printed. Deliberately not `aws secretsmanager create-secret --secret-string`, which puts the value
where a process listing can read it. The script refused to proceed if the name already existed, so a create could
not silently become a rotation, and `get_secret_value` was never called -- even the read-back is describe-only.
`gateway/mail/bearer` AWSCURRENT was never written: that is the whole reason this is a SECOND secret, because the
mail-pull Lambda reads that one whole.

**The policy line, its own ledger.** One ARN added. Graded from `show -json` by DECOMPOSING the policy document --
statements 1 -> 1, Effect unchanged, Action unchanged, Condition unchanged, resources 4 -> 5, ADDED exactly the
commassist ARN, REMOVED none -- because the whole policy is ONE opaque attribute in the plan and `0 add, 1 change,
0 destroy` would read identically had an ARN been dropped. Read back with **all four prior ARNs confirmed
individually BY NAME**, since a count of 5 would also hold if a prior had been swapped for the new one.

**The deploy, and it took three attempts.** The first two were REFUSALS, not failures: the halt gate blocked rc=3
on `SERIAL RESOLVES TO NO KNOWN AGENT`. I did not reach for `HALT_OVERRIDE`, which the order's BOUNDS forbid.
Diagnosis to the predicate: `safe-ec2-deploy.sh:57` pins `HALT_GATE_REPO_ROOT` to the calling worktree
(deliberately, ruling R-53), `halt_gate_validate_serial` scans **that root alone** (the two-root loop belongs to
`halt_gate_worker_issuer`, which runs only for `0.9.0_WK_*` serials), and the release worktree was a SPARSE
checkout that had not materialised `org/tier2_senior/0.7.0_AE_CloudOps~Z` -- a folder present in that very
commit's tree. Row `Z-S74`. Amendment A2 then prescribed setting that variable, which **cannot work** because :57
discards it; I filed `Z-S75` correcting my own row's implied remedy, tested a fix, and asked rather than
substituting my own method after saying the call was the issuer's. A3 `@3e14f27aee` ruled the cone fix.

Verify after: **5 of 5 PASS** -- /health 200, MainPID 791928 -> 857046 (the one signed restart), shipped md5 98 of
98, tools 66 -> 66, `.env` keys 51 -> 52 with exactly `MAIL_SENDER_DOMAIN_TABLE` added, and every pre-existing
value's sha256 unchanged except the two expected. **R45 fetch control 0 of 6441**, corroborated by cache bytes and
file count byte-identical before and after. No rollback trigger fired.

### 2. `NFRA_OPLGTW.TO-OG-ap-4` -- the 4-meeting transcript allowlist: COMPLETE, AC1 PASS

Two things went better here than in OG-ap-3, and both are the same lesson applied forward.

**The halt gate passed FIRST TIME**, because the premise was made true at CUT time rather than after a refusal: I
cut a FULL worktree, verified the agent home present at creation, and dry-ran both limbs with the root `:57`
actually pins before touching the host.

**The re-cut's exactness was established BEFORE applying.** The order required a re-cut on the live ref. Comparing
the live ref's `deploy-to-ec2.sh` blob (`2091d3b4be`) against the reference hunk's own pre-image index showed them
IDENTICAL -- the OG-tl-1 branch had been cut on content already carrying r29's E4 leg -- so replaying
`4514246d65..78afad4283` on r29 reproduces the release blob by construction and the patch-id cannot drift. That
turned "will the patch-id match?" from a hope into arithmetic. All three COO-half limbs then held exactly: blob
`c2cfc34065`, patch-id `ace789196aa221ca`, json `d57e815a7c`, with `git status` reading exactly two rows.

**CTO C1 measured, not eyeballed:** the deploy's own `ENV_KEYS_BEFORE`/`AFTER` lines parsed and compared as sets
AND as ordered lists -- 52 each, missing NONE, added NONE. A lost key could not hide behind a matching count.

One audited author override on the re-cut commit alone (`CLOUD_OPS_OR_ETL`, per OG-tl-1 A1), confirmed on the
record in `org/git-author-override-audit.log`.

### 3. `NFRA_IAMROLES202609` -- v-1, v-2 and v-4 all COMPLETE

**v-2**: all ten rows accepted, with every figure re-measured live (233 functions scanned) rather than inherited.
Its spine is a precedent I went looking for: a census of all **292** account roles found **nine** minted in one
eight-second batch on 2026-02-19, and **six of those nine are already declared** in their own domain modules --
two of them explicitly while annotated "orphaned". So "nothing uses it" is NOT this estate's reason to delete a
role, which decided nine of the ten dispositions. That subtraction also TESTED the disposition's 16-row domain:
had the six been undeclared, FWD-4's closure would have been measured against the wrong population.

**v-4**: the WORLD narrowing. Sequenced FIRST, before the gateway window, because an apply before 13:02Z makes
TODAY's run the read instead of tomorrow's -- that choice is what let the cell close in one session. `implicitDeny`
5 of 5 with the retained action `allowed` 5 of 5 in ISOLATED invocations (two or more `--resource-arns` in one call
flips the held ones and would have manufactured the result). Leg `OBS` then stayed open ~3h and the ledger listed
it stranded, by design. **0 of 4 falsifiers fired; MATCHES-PREDICTION: yes**, emitted from the observed set rather
than typed.

### 4. `MDPF_SECHIST.TO-READ-R2-L3` -- COMPLETE, graded PASS by its issuer

The useful decision was made ~4h before the window: a pre-window control read found the prior day's fire at
`LastTaskResult 50`, and the `.cmd`'s exit contract says 50 means the DAPI precondition failed and the pull was NOT
attempted -- and on that path the script jumps to `:prune` and **SKIPS the ETF leg**, the leg this order turns on.
So the window's result (ETF leg 0, backfill line 514 rows) answered a question already posed. Row
`MDPF_SECHIST-Z-S1` was filed at that point, not after.

### 5. Carried for other seats

`ETFS_RIVALS.TO-APPLY-R28-aw1` turned out SUPERSEDED -- dell1 applied it live at 11:20:54Z under its own amendment
-- so holding mine was correct and no double-apply occurred; its plan and worktree were discarded after verifying
containment in both `box/sitez` and `CLOUD`. And I landed `0.7.0_AE_CloudOps~ZC`'s AMGT_CORPUS leg-v read as a
CARRIER (it sat in my folder, where only my serial can commit), reading it first and stating plainly that I am
neither its author nor its grader; it carries an ungraded finding (ledger rows 6320 against ~4224 expected).

## Deployment sequence + verification (AE role-specific) -- ACTUAL output

```
11:5xZ  s3api put-object       data-refresh artifact: 20716 B, metadata EXACT MATCH
11:18Z  safe-apply (saved)     Apply complete! 0 added, 1 changed, 0 destroyed  (the policy line)
                               read-back: 1 statement, 5 resources, prior 4 confirmed BY NAME
12:07Z  safe-ec2-deploy        rc=3  HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT   <-- refusal 2 of 2
                               host re-read after: MD5 97 identical 97, 0 mismatch -- nothing shipped
12:31Z  safe-ec2-deploy        rc=0  DEPLOYMENT COMPLETE  (r29, after A3's cone fix)
                               VERIFY PASS: 5 of 5 | bun-cache touched 0 of 6441 | MainPID 791928->857046
12:3xZ  safe-apply (saved)     Apply complete! 0 added, 1 changed, 0 destroyed  (fwd5 narrowing)
                               live: ReadAuthBundle ['secretsmanager:GetSecretValue'] alone, 4 statements intact
15:07Z  safe-ec2-deploy        rc=0  DEPLOYMENT COMPLETE  (the allowlist, FIRST attempt)
                               ENV_KEYS 52 == 52, set and order equal | VERIFY PASS 5 of 5 | MainPID 862375
```

Criteria, each run LITERALLY as written:

```
OG-ap-3 AC1 PASS   secret describe rc=0 arn_present=yes; resources 5 (want 5); naming 1 (want 1)
OG-ap-3 AC2 PASS   both ledgers: entries at HEAD 1; CLOSED=yes; sentinel at HEAD=no
OG-ap-4 AC1 PASS   ledger CLOSED; manifest deployed_commit=c97232408d == release_sha; equal=yes
IAM-v-2 AC1 PASS   rows=16 unowned=0   AC2 10   AC3 one line, this lane
IAM-v-4 AC1 PASS   5          AC2 1          AC3 open=0 closed=1
L3      AC1 PASS   1
```

Five proof instances written, each `VALID rc=0 violations=0` BOUND via `--governing-order` with its declared set,
and each **negative-controlled** against a wrong set.

## Compiler tools

| tool | invocation | result | note |
|---|---|---|---|
| `terraform` | init / plan `-target` `-out` / `show -json` / apply saved / re-plan, across three roots | PASS | Every plan graded by a script that DECOMPOSES the policy document per `Sid` and compares actions, effects, conditions and resource sets. That is the only read that distinguishes "one action dropped" from "one resource dropped"; the headline counts cannot. |
| `safe-ec2-deploy.sh` + `halt-gate-check.sh` | 4 deploy attempts (2 refusals, 2 successes); gate limbs dry-run 6 times across 4 root configurations | PARTIAL | PARTIAL deliberately: both deploys landed, but the chain produced two correct refusals on a wrong premise and its own dry-run guidance cannot reproduce the deploy's roots. Rows `Z-S74` and `Z-S75`. |
| `safe-apply.sh` | 3 applies, all from SAVED plans | PASS | comp-tagauthz PASSED and tombstone-gate CLEAN on each. Its tag-authz limb printed a `Project` KEY COLLISION for the data-refresh root, which I carried into the IAM row-8 acceptance as a condition on any future adoption. |
| `deploy_ledger.py` | 4 entries opened, 12 legs closed, 4 closed | PASS | Every entry opened with its sentinel BEFORE its act. Leg `OBS` held open ~3h and listed stranded, which is the correct appearance for a verify that has not happened yet. |
| `proof-of-spec-check.py` | 5 instances, each BOUND + declared set + a wrong-set negative control | PASS | Caught 9 real defects across the drafts: 3 closed-enum violations, 3 prose-where-a-pattern-belongs, 2 artifact-resolution refusals (a guessed pin, and three WORLD artifacts named where git-resolvable paths belong) and one thin `output_evidence`. One run was a TOOL FAILURE rc=2 from a concurrently-broken shared schema, which the checker labelled NOT-A-VERDICT rather than letting me read it as INVALID. |
| `aws iam` / `secretsmanager` / `logs` / `cloudtrail` | read-only throughout; `simulate-principal-policy` 11 times, one `--resource-arns` per call | PASS | The control is a SEPARATE invocation every time, because a positive control run alongside the target is disarmed by the multi-ARN mode. `boto3` replaced the CLI for the log reads because a leading-slash log-group name is MSYS path-converted and failed the CLI's own parameter regex. |
| `safe-commit.sh` | ~18 commits; 1 refused on a peer's in-progress merge; 1 under an audited override | PASS | The merge refusal was another seat's work-in-progress: I measured `MERGE_HEAD` and the conflict set clear moments later and retried rather than resolving or forcing. |
| `comp-iam` | NOT USED for any read-back | SKIP | Deliberate on every order. cloud-ops states it models `(action)` and never `(action, resource)` and is a FLOOR, so it cannot confirm that one ARN landed or that one action left one statement -- which was the only question in two of these cells. |

**What worked:** grading plans by decomposition rather than by headline counts, three times over. It found the
qa-scratch second reader, proved the pin moved no executable byte, and proved the narrowing dropped an action and
not a resource. **What failed:** my own halt-gate dry run passed rc 0/0 minutes before a deploy failed on the same
two limbs, because it resolved different roots -- a dry run that does not reproduce the real invocation's roots
tests a different gate. **Gap found:** three task orders now declare surprise-row id forms their own gate refuses
(`-Z-AEC-`, `-Z-AE-`, and `-Z-AEMI-` which MX-s-19's A3 already retired); `ID_RE` admits only ONE optional segment.

## Blockers

1. **OG-ap-3's deploy: BLOCKED TWICE, then RULED, then LANDED** -- evidence in section 1; rows `Z-S74` and
   `Z-S75`, resolved by A3 `@3e14f27aee`. Nothing was half-landed at any point: the host re-read 97 of 97 after
   the first refusal.
2. **Not a blocker, recorded so it is not mistaken for one:** `2.0.0_SA_COO~RV` and `2.0.0_SA_COO~H1` both read
   NOT REGISTERED, so two items could not be reported to their issuers directly. Both were PARKED on carriers with
   owners and un-parking conditions and routed via `1.0.0_SA_CTO~Z`, who relayed them to dell1 through `MSTR~Z`.
   Both have since come back: R28-aw1 superseded, L3 graded PASS.
3. **One near-miss worth more than a blocker.** `describe_log_streams`' `lastEventTimestamp` LAGS the events: read
   at 13:17Z it reported a **6-second** span for a run whose events span 802.6s and whose `REPORT` line reads
   740.3s. Against a 537-859s baseline that looks exactly like a run that authenticated and exited early -- the one
   shape FWD-5's F3 cannot catch, because the auth path HAD run. I chased the discrepancy instead of filing it and
   did not raise a false ARMED row against a healthy run. The sound oracle is the run's own `REPORT` Duration,
   never the stream envelope. Recorded in `fwd5/OUTCOME.md` section 9.

## Files modified

See commit messages: `0422cbd3ee`, `deee55b3ef`, `99c3b4c1b1`, `5f63775be5`, `47c6a98f49`, `1ca645fd25`,
`673656f7d8`, `1416282c74`, `59112aafed`, `36fae05ea5`, `38b456ff1c`, `f07f3dcc87`, `e02476796b`, `b1b5dc985f`,
`2cbd044a43`, `1d4c397f40`, `8eefd927c2`, `5f1400c4a2`, `fab015fa54`, `b2f35b9159`, `7dc005b8af`, `6dee08829e`,
`3b20e9156f`, `c97232408d`, `c8625c3735`, `71d432d4a8`, `ec8cf3cac5`, `d22c81d285`, `fc23152f14`, `5dc85630b3`.

## MCP traffic

~40 messages handled, all acked. The significant ones: GOs and amendments on OG-da-1 Phase B (32501), Z-S72 ->
A1 (32565), OG-ap-3 (32540) and its A1 source-map grant (32594), Z-S74 -> A2 (32723/32732), **Z-S75 -> A3
(32736)**, IAM v-1/v-2/v-4 GOs (32586, 32648/32652) and the Z-S19 ruling (32623), OG-ap-4's GO with A1 (32794),
and three relays from `1.0.0_SA_CTO~Z` (32741, 32749, 32832) carrying dell1's side.

Three sends were REFUSED by the broker at 152-182 words against Rule 31's cap. That is the rule working; each was
cut to one ask plus file citations and went. One lesson landed the hard way earlier and did not recur: a
`heartbeat` re-emitted three messages I had read off the FILESYSTEM and acted on but never acked -- reading a file
never touches the READ clock.

## Current state

- **Live on the gateway host** (`i-07dccb1615503ac99`): release `c97232408d72bc649c92da7e4e711c0ebf0a3950`
  (`rel-nfra-oplgtw-tl1b`), base r29 `91811b648a`. MainPID 862375, /health 200, 52 `.env` keys, 66 tools,
  shipped md5 98 of 98. `TRANSCRIPT_MEETING_ALLOWLIST` now carries the four committed `online_meeting_id` values;
  it was empty, every meeting refused, until today.
- **Live, data-refresh**: `opal-data-refresh-api` `CodeSha256 qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM=`, its
  admission failing closed. `opal-data-refresh-api-qa-scratch` PINNED to its own key at `E4944Imr...` -- the same
  bytes it ran before, so nothing of its behaviour moved.
- **Live, IAM**: `smartx-assets-pull-role`'s `ReadAuthBundle` carries `secretsmanager:GetSecretValue` ALONE over
  its 5 resources; 4 statements intact. `opal-gateway-role`'s read-secrets policy carries 5 ARNs.
- **New secret**: `gateway/mail/commassist-bearer`, VersionId `5c368b4d-d6e8-4366-8988-92f4eb4b8fcd`.
- **Rollbacks, named and available**: r29 -> redeploy `aa75078e1b` from `C:/tmp/og-rb29`; the allowlist ->
  redeploy `91811b648a` with `DEPLOY_BASE_REF=c97232408d`; the narrowing -> `git apply -R narrowing.patch` then the
  same `safe-apply`; data-refresh -> artifact VersionId `WJQGGIAlTSMp0Vny8avvQ7LxflVuvLf6`.
- **FOUR ledgers CLOSED, no open deploy for this seat.** `deploy_ledger list` returns nothing authored by `~Z`.
- **Orders:** OG-da-1, OG-ap-3, OG-ap-4, IAM-v-1, IAM-v-2, IAM-v-4 and MDPF_SECHIST L3 all `complete`.
  `NFRA_MCPINDEX.TO-MX-s-19` is explicitly NOT this seat's until its 2026-10-13 re-point (amendment A6: "No GO
  goes to `0.7.0_AE_CloudOps~Z`").
- **Discarded as site-Z housekeeping** (CTO-assigned, containment verified in `box/sitez` AND `CLOUD` first):
  `C:/tmp/rv-r8` and `C:/tmp/rv_apply28.tfplan`, both superseded by dell1's live R28-aw1 apply.
- Broker: live, ZERO crons, watcher re-armed on every 30-minute expiry (twelve arms this window, one script row at
  every census, nothing reaped).
- **Push state, MEASURED at 16:0xZ:** every commit listed above is ON ORIGIN; `git ls-remote origin box/sitez`
  read `b0fe20b5f6`. I pushed nothing -- box-sync is the integrator's scheduled carry.

## Next steps

1. [`3.0.0_SA_CVO~Z`] Grades four judgment criteria now waiting: OG-da-1 AC3 (each caller ADMITTED on its first
   real call; 0 of 6 observed at instance time, recorded as not-yet-observed and never as a pass), IAM-v-1 AC4,
   IAM-v-2 AC4 and IAM-v-4 AC4.
2. [`2.0.0_SA_COO~O`] Owns Phase C of both releases: the r29 grant write (Alyssa 30 days -> 13 months) and
   OG-tl-1's served allowlist read, which is its AC2 and explicitly not this seat's.
3. [`2.0.0_SA_COO~C1`] Owns the AMGT_CORPUS leg-v finding I landed as carrier: amgt-model-block ledger rows 6320
   against ~4224 expected, +2096, ungraded.
4. [`2.0.0_SA_COO~MI`] Re-points `MX-s-19` to a fresh site-Z CloudOps lane after `s19.PRE.sh` passes on
   2026-10-13; this seat takes no GO on it.
5. [`1.0.0_SA_CTO`] Three orders declare surprise-row id forms their own gate refuses (`-Z-AEC-`, `-Z-AE-`,
   `-Z-AEMI-`). A one-line fix in each order's text, or a widened `ID_RE`, saves the next seat a refusal
   round-trip at the moment it has a finding to file.
