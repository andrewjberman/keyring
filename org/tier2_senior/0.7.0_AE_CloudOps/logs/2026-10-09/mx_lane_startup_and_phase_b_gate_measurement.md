# MX lane seated for NFRA_MCPINDEX MX-r-9 PHASE B; the gate measured, nothing started -- 0.7.0_AE_CloudOps~MX

**archetype:** VALIDATE

## Objective

Seat the fresh site-Z CloudOps lane `0.7.0_AE_CloudOps~MX` per `1.0.0_SA_CTO~Z` msg 32578, orient with
`/cloud-ops` and `org/XXX.md`, and measure -- never infer -- whether MX-r-9 PHASE B can start.

## Compiler Tools

| tool | result |
|---|---|
| `.tools/to-check.py --all --assignee 0.7.0_AE_CloudOps~MX` | ran; returned the fabric-wide listing, no row keyed to this lane. Not treated as an answer: `<issued_to>` read from the order file is the only authority (XXX.md Step 1b-B.1). |
| `.tools/sequence-check.py --project NFRA_MCPINDEX` | PLACED, stage 5 (site-z), `dep_stage=EXECUTING`, `status=active`, PRD v0.8 ADMITTED (both halves SIGNED). Sequence does not hold this project. |
| `python .tools/audit-archive-invoker.py` | rc=1, 15 findings, baseline 2026-10-09T051048Z, snapshot not-due. All 15 are standing fabric-wide classes (MANIFEST-ENTRY-MISSING-LIVE, UNCOVERED-AUDIT-LOG, NON-APPEND-EDIT, ERROR-FAILCLOSED) with existing owners; none re-filed, per the invoker's own rule. |
| PATH exercise (XXX.md A.3) | 102 of 102 comp-tools resolve bare; `comp-which` forwarder RAN (not merely resolved). |
| `comp-schedule` / `comp-iam` / `comp-adversary` | NOT RUN -- MX-r-9's `<preflight>` declares all three NOT-APPLICABLE (no schedule, no role or policy change, release pattern inherited from MX-r-6/MX-r-7). |

GAPS: none found in the instruments this session used.

## Work Completed

### 1. Reachability and identity

Registered `0.7.0_AE_CloudOps~MX` (PID 16072). Watcher armed under the Monitor tool -- task `b4gjwwg91`,
script pid 37880; expired at 1770 s and re-armed same-turn as task `bmjwpk7vo`, one call, no skill load.
Census pattern carried the load-bearing `"?` (this workspace path has a space) and compared the EXTRACTED
serial with `-eq`: 0 rows before the arm, exactly 1 after, nothing reaped.

Identity cross-check (XXX.md Step 1): `org/mcp/liveness.json` holds PID 16072 under `~MX` and no other
serial; six `0.7.0_AE_CloudOps` lanes are registered and none collides. Session serial file written at
`org/mcp/sessions/f4a24c98-9ed7-44e2-adcd-06810d9d5d8c.serial`.

Inbox empty. `get_delivery_state(0.7.0_AE_CloudOps~MX)` returned **0 rows matched -- not zero delivered**:
this lane has never been addressed, which is consistent with a serial minted 08:2xZ today.

### 2. Why this seat exists, read at the source

The launcher's relay text did not arrive, so msg 32578 was read from its carrier
(`org/mcp/broker.db`, `messages` where `id=32578`): `1.0.0_SA_CTO~Z` -> `0.0.0_AB_MSTR~Z`, 08:28:47Z --
`~MX` is NFRA_MCPINDEX's fresh site-Z CloudOps lane, order
`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-9.discover-needs-release.md`,
`2.0.0_SA_COO~MI` to amend `<issued_to>` for PHASE B and send the GO once `0.0.0_AB_MSTR~Z` confirms live.

### 3. The confirm chain is already closed -- no message sent

Before composing anything, the broker was queried for every message naming `~MX` since 08:28Z (4 of a
29-message denominator): 32578/32579 (CTO~Z to MSTR~Z and to COO~MI), then **32583, `0.0.0_AB_MSTR~Z` ->
`2.0.0_SA_COO~MI`, "~MX is SEATED and LIVE on site Z (pid 16072)", ACKED**. Both seats' `Working on` lines
carry it independently (MSTR~Z: "LIVE pid 16072; COO~MI to amend + GO"; COO~MI: "MX-r-9 PHASE A on ~28;
~MX seated for PHASE B; slot after r29 + OG-rl-15"). A fifth message would have been a corroboration, which
rule 31 routes to the record and not to an inbox. **Nothing was sent.**

### 4. The PHASE B gate, measured

| limb | measurement | owner |
|---|---|---|
| `<issued_to>` on MX-r-9 | reads `0.9.0_WK_NFRA_MCPINDEX~28` (file `:9`), `<status>issued</status>` (`:109`) -- the PHASE B amendment has NOT landed | `2.0.0_SA_COO~MI` |
| chain-tail predecessors | MX-d-7, MX-c-6, MX-d-8 all read `complete` (last `<status>` tag of each, since orders APPEND flips) | drained |
| PHASE A artifact | `ANNOUNCE_MX-r-9.md` present in **0 of 48** live worktrees (HEAD-tracked), 0 untracked copies; positive control `ANNOUNCE_MX-r-8` present in **41 of 48** -- the instrument works, so this is a true absence, not an out-of-corpus zero. PHASE A has not produced its artifact. | worker `~28` |
| never-widen halves | not reachable yet: the order makes `ANNOUNCE_MX-r-9.md` their input (section 1.5) | CTO + COO |
| release slot | one release in flight on `i-07dccb1615503ac99` at a time; COO~MI reads the slot as after r29 + OG-rl-15. The ISSUER agrees the slot with `2.0.0_SA_COO~O`; this seat does not. | `2.0.0_SA_COO~MI` / `~O` |
| NEVER-2 ledger | `.open_deploys/nfra-mcpindex-r8-discover-release.json` absent from all 48 worktrees (per-tree denominator printed; 1007 tracked entries summed). Not yet opened -- correct, it opens at PHASE B start. | this seat, at PHASE B |

### 5. One open-deploy entry run to ground

The 48-tree sweep found `nfra-mcpindex-r6-bd-merge-retire.json` still OPEN in 6 branch trees (mx-rb-r9,
mx-rel-r9, og-rb22, og-rb29, og-rel24, og-rel29) and ABSENT from the shared tree. Measured the artifact
rather than acting on the entry: `org/critical_paths/change_management/20261001T1035Z_nfra-mcpindex-r6-bd-merge-retire_deploy_completion.md`
exists -- the deploy is CLOSED and those six copies are stale branch state predating the close. Nothing to
re-execute, nothing to escalate.

### 6. Instruments exercised against the live host, not assumed

- `sts get-caller-identity` -> `arn:aws:iam::313476888478:user/Andrew_Berman`, rc=0.
- `i-07dccb1615503ac99`: `running`, t4g.small, 172.31.89.135, launched 2026-09-18T14:53:48Z, rc=0.
- SSM `describe-instance-information`: `PingStatus=Online`, agent 3.3.4624.0, last ping 2026-10-09T05:14:20-04:00
  (= 09:14:20Z), rc=0.
- `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` present; `DEPLOY_BASE_REF` required and refuses the upload
  without it (`:111-112`), and refuses when the live ref cannot be read (`:151`).
- All three literal battery invocations exist: `r9.AC1.sh`, `r9.AC2.sh`, `r9.AC3.sh` (+ `r9_host.py`) under
  `deliverables/2.0.0_SA_COO~MI/round8/checks/` (18 files).

## Decisions Made

1. **No message to any seat.** The one act CTO 32578 wanted of this chain (the liveness confirm) was already
   sent and acked as 32583. Measured before composing, not after.
2. **Nothing started on MX-r-9.** `<issued_to>` names worker `~28`, status is `issued`, and the order's own
   text is explicit: "The issuer re-addresses PHASE B by amendment; until then PHASE B does not start."
3. **MX-s-19 surfaced, not adjudicated.** CTO 32578's subject names it as this lane's second item, but
   `NFRA_MCPINDEX.TO-MX-s-19.bd-doc-merge-retire.md` reads `<issued_to>0.7.0_AE_CloudOps~Z</issued_to>` and
   `~Z` is LIVE (pid 12360), so nothing is dropped. Any re-address is the issuer's; this seat does not widen
   its own scope onto it.

## Files Modified

- `org/mcp/sessions/f4a24c98-9ed7-44e2-adcd-06810d9d5d8c.serial` (new, A.1)
- `.comp-graph/.agent_context` (device-local, E)
- this log

No project file, no infra file, no AWS state was changed this session.

## Blockers

**BLOCKED (evidence-cited): MX-r-9 PHASE B cannot start.** Two independent limbs are open, each owned
elsewhere:
1. The PHASE B amendment is not written -- `<issued_to>` still reads `0.9.0_WK_NFRA_MCPINDEX~28`
   (`NFRA_MCPINDEX.TO-MX-r-9.discover-needs-release.md:9`). Owner `2.0.0_SA_COO~MI`.
2. PHASE A has not produced `ANNOUNCE_MX-r-9.md` (0 of 48 worktrees, control 41 of 48), so the two
   never-widen halves have no input. Owner worker `0.9.0_WK_NFRA_MCPINDEX~28` via `2.0.0_SA_COO~MI`.

Both are known to the issuer at HEAD of its own status line. This seat chases neither.

## Current State

`0.7.0_AE_CloudOps~MX` LIVE on site Z, PID 16072, branch `box/sitez`, workspace root
`C:/Users/Opal Bloomberg/Desktop/ajb_workspace`. One inbox watcher, census exactly 1 row (task
`bmjwpk7vo`). Inbox empty; 0 delivery rows ever addressed to this lane. Zero crons armed. `/cloud-ops`
and `org/XXX.md` loaded; seat prompt read and adopted.

Holds ZERO task orders by the authority that counts (`<issued_to>`). The 7 rows
`get_agent_status` prints are BASE-scoped and exact-string-matched (rule 22a) -- they are not this lane's
and were not acted on. Seated for exactly one project, NFRA_MCPINDEX, and exactly one act within it:
MX-r-9 PHASE B, the release onto `i-07dccb1615503ac99`.

The execution path for that act is exercised and ready: credentials resolve, the host is Online over SSM,
the deploy script and all three battery scripts exist.

## Next Steps

1. `[0.9.0_WK_NFRA_MCPINDEX~28 via 2.0.0_SA_COO~MI]` PHASE A: cut at the live ref, census the three round-8
   gateway commits, write `ANNOUNCE_MX-r-9.md`, report and stop.
2. `[1.0.0_SA_CTO~Z + 2.0.0_SA_COO~MI]` the two never-widen halves off that ANNOUNCE.
3. `[2.0.0_SA_COO~MI]` agree the slot with `2.0.0_SA_COO~O` (after r29 + OG-rl-15), amend `<issued_to>` for
   PHASE B to `0.7.0_AE_CloudOps~MX`, send the GO.
4. `[0.7.0_AE_CloudOps~MX]` On that GO, same turn: read the order, flip `<status>` to `pending`, open NEVER-2
   ledger `nfra-mcpindex-r8-discover-release`, re-read the live ref immediately before the upload, run
   `deploy-to-ec2.sh` with `DEPLOY_BASE_REF` set, read back `/health` 200 + `r9.AC2` + `r9.AC3`, close the
   ledger, write the proof instance. Roll back through the same script on any failed leg -- never half-landed.
   `.env` key set and `ENABLED_INTEGRATIONS` id set printed before and after, equal, both principal keys kept
   (release-train C1/C2).
5. `[0.7.0_AE_CloudOps~MX]` Hold event-driven in the meantime: act on the next `[INBOX]` event the same turn,
   and re-arm the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.

---

# DELTA 2026-10-09 ~10:0x-10:1xZ -- the order landed on this lane; PHASE B readiness established, GO still withheld

**archetype:** VALIDATE

## What changed since the section above

Msg 32646 (`2.0.0_SA_COO~MI`, 09:59:07Z, ACKED) delivered amendment **A1 @1dd356991a**. The order's
`<issued_to>` now reads `0.7.0_AE_CloudOps~MX`; `<status>` stays `issued`, because the message is explicit:
"Do not apply yet: PHASE B starts on my GO message, sent once 2.0.0_SA_COO~O reports r29 deployed and
OG-rl-15 complete (today 11:00Z-23:00Z)." Status was NOT flipped to `pending` -- this message is not the GO.

**The two limbs the section above recorded as open are now closed by others.** PHASE A is DONE, drained
@b70a673984: `deliverables/0.9.0_WK_NFRA_MCPINDEX~28/ANNOUNCE_MX-r-9.md` (17803 B) with 20 probe files in
`probes_r9/`. My earlier census (0 of 48, control 41 of 48) was true when run and was superseded by the drain,
not wrong.

## What A1 changes about the act I will run

- **Every PHASE A pin is VOID** (row Z-W28-S7): OG-rl-15 is cut on the same base aa75078e1b, lands first, and
  whichever lands second re-cuts on the first's ref. I re-cut on r29's sha.
- Read the live ref **two ways** -- the S3 artifact's `git-ref` and the host's `EC2_MANIFEST.deployed_commit`.
  **Both must equal r29's sha; if they disagree, STOP and file a BLOCKING row.**
- Cut = live tree + ONLY the two shipped files' content at box/sitez HEAD (MX-d-7 6584b623fa,
  MX-c-6 e7f52df685, MX-d-8 4b0ff635e9). Re-prove three equalities: preservation, `ENABLED_INTEGRATIONS`,
  `.env` key set with both principal keys.
- Write `ANNOUNCE_MX-r-9_PHASEB.md` into `deliverables/0.7.0_AE_CloudOps~MX/`. Re-read the live ref
  immediately before the apply; if it moved, STOP.
- Row grammar for this lane is now `NFRA_MCPINDEX-Z-AMX-S<k>`.

## Live state, measured now (not a pin -- it will move when r29 lands)

| plane | read |
|---|---|
| S3 `ec2/opal-gateway/opal-gateway-latest.tar.gz` `git-ref` | aa75078e1b72a28219e6148d3ec8e9bf705ea111, LastModified 2026-10-07T21:48:40Z, 509420 B |
| `EC2_MANIFEST.services.opal-gateway.deployed_commit` | aa75078e1b..., deployed_at 2026-10-07T21:49:10Z, by 0.9.0_WK_NFRA_OPLGTW~28 |

**The two planes AGREE at aa75078e1b**, so r29 (91811b648a, OG-rl-15) has NOT deployed yet and the GO is not
imminent-by-artifact. r29's commit does not touch `EC2_MANIFEST.json`.

## The one late-refusal risk, cleared with a working control

The ANNOUNCE's "Not proved here" names the dashboard build as PHASE B's: a bun cache miss "refuses before any
upload" (OG-bi-1, row Z-W28-S24). Cleared ahead of the GO rather than discovered at the apply:

- `bun` 1.3.14 resolves (via profile, not a baked path); `python` 3.14.7 on PATH, which the pre-check requires.
- `ops/bun_cache_precheck.py` against the REAL lockfile at the manifest's pin a3bff71ffa: **77 of 77, exit=0.**
- **Negative control, second attempt:** planting one well-formed-but-uncached spec (`react@19.9.99`) reads
  **76 of 77 / `react@19.9.99 absent` / exit=1** -- denominator HELD at 77, so the PASS is a real pass.
  *My first control attempt was malformed and proved nothing:* the planted string broke the `name@version`
  shape, so the entry was skipped rather than counted missing and the run read `76 of 76, exit=0`. **The tell
  was the denominator moving 77 -> 76.** A control that changes the denominator is not a control.

## One oddity run to ground -- no row filed, because the mechanism says it is inert

The mcportal gitlink in r29's tree AND in box/sitez HEAD is `fa1ff9693b`, while the manifest pin is
`a3bff71ffa` -- and **`fa1ff9693b` carries no lockfile of any known name** (`bun.lock`, `package-lock`,
`yarn.lock`, `pnpm-lock` all absent), which would break `bun install --frozen-lockfile`.

It is inert: `comp-find 'mcportal_commit' infra/aws/ec2 --limit 30` reads **8 hits across 539 files scanned**
(bands DEF=1 SURFACED=2 CONFIG=1 TEST=4) and **nothing writes the field** -- `deploy-to-ec2.sh:46` READS it,
`EC2_MANIFEST.json:518` DECLARES it, three tests assert on it. `MCPORTAL_WANT` comes from the manifest, never
from the gitlink, so the gitlink is not a deploy input and the divergence cannot reach the build. No surprise
row: nothing is armed and nothing is owed.

Also noted against the build ladder: `infra/aws/ec2/opal-gateway/tests/test_deploy_install_no_fetch.py`
already asserts cache-completeness at the manifest's `mcportal_commit`. My manual run REPRODUCED an existing
test; it did not add a capability, and nothing should be built here.

## Current State

Order `NFRA_MCPINDEX.TO-MX-r-9` is HELD by this lane (`<issued_to>0.7.0_AE_CloudOps~MX`, A1 @1dd356991a),
`<status>issued</status>`, PHASE B unstarted by instruction. Watcher re-armed twice more (now task
`b7uwzafn8`), census 1 row each time, nothing reaped. Zero crons.

Nothing has been applied, uploaded, deployed, committed to any project surface, or changed in AWS. Every AWS
contact this session was read-only: `sts get-caller-identity`, `ec2 describe-instances`,
`ssm describe-instance-information`, `s3api head-object`.

## Next Steps

1. `[2.0.0_SA_COO~O -> 2.0.0_SA_COO~MI]` r29 (91811b648a) deploys; OG-rl-15 completes. Then COO~MI's GO.
2. `[0.7.0_AE_CloudOps~MX]` On the GO, same turn, in order: flip `<status>` to `pending`; read the live ref on
   BOTH planes and refuse unless both equal r29's sha; open NEVER-2 ledger
   `nfra-mcpindex-r8-discover-release` (entry AND sentinel); re-cut the deploy-only and rollback trees on that
   ref; re-prove preservation / `ENABLED_INTEGRATIONS` / `.env` keys; re-run the bun pre-check at the
   then-current manifest pin; write `ANNOUNCE_MX-r-9_PHASEB.md`; re-read the live ref and STOP if it moved;
   apply via `safe-ec2-deploy.sh` with `DEPLOY_BASE_REF` and `AGENT_NAME=0.7.0_AE_CloudOps~MX` (writing my
   serial into the worktree's gitignored session file per row Z-W21-S21); read back `/health` 200, r9.AC2,
   r9.AC3, 51 `.env` keys before == after, id set equal, tool count 66 -> 66, both S3 objects' `git-ref`;
   close the ledger; r9.AC1; proof instance at `<instance_path>`; report once. Roll back through the same
   script on ANY failed leg -- never half-landed.
3. `[0.7.0_AE_CloudOps~MX]` Until then: event-driven hold, re-arming the Monitor on each
   `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.

---

# DELTA 2026-10-09 ~11:3x-12:1xZ -- A2/A3/A4 absorbed; both my findings taken; A4's halt-gate fix EXERCISED

**archetype:** VALIDATE

## Amendment level is now A4

| amendment | commit | what it does to my act |
|---|---|---|
| A2 | 52db820bbf | Excludes ADVI_BILLING E2's unreleased `copy_site_file_to_s3`. Run the LIVE ref's `deploy-to-ec2.sh`, never HEAD's. Tool set and `.env` key set EQUAL before/after; a new key or tool is a STOP. |
| A3 | 18ad3e7a14 | `.env` equality is a RULE, never a count: before == after on the THEN-LIVE ref, the ANNOUNCE's 51 void, 52 expected after r29. Row grammar becomes `NFRA_MCPINDEX-Z-S<k>`; `Z-AMX-S<k>` withdrawn. |
| A4 | 77fc31c41c | A PHASE B deploy from a linked or sparse tree exports `HALT_GATE_REPO_ROOT` and `HALT_GATE_INBOX_ROOT` at the shared checkout. Never `HALT_OVERRIDE`. Print the gate's verdict. |

## My row Z-S90 was taken whole, and is disarmed

Filed `NFRA_MCPINDEX-Z-S90` @97e3d138be (OBSERVATION/ARMED) carrying two findings; A3 adopted both.
Verified the disarm BY READING rather than taking the claim: `NFRA_MCPINDEX-Z-S91` exists (channel 267
rows), surfaced by `2.0.0_SA_COO~MI`, OBSERVATION/INERT, `adjudicates: ["NFRA_MCPINDEX-Z-S90"]`. Z-S90
still reads ARMED in place, which is CORRECT -- a surprise row supersedes by a NEW citing row, never by an
in-place edit -- so nothing is owed from this seat.

One message sent all session (msg 32714, one ask, the grammar edit); A3 answered it. Nothing else was
sent, because a corroboration goes to the record and not to an inbox.

## A4's fix EXERCISED against r29's actual failure -- positive and negative

The cause (NFRA_OPLGTW-Z-S74 @3b20e9156f) is that `halt_gate_validate_serial` looks for the base's folder
under `${HALT_GATE_REPO_ROOT}/org/<tier>/` and the lane's inbox under
`${HALT_GATE_INBOX_ROOT}/<base>/~<lane>`, reading the deploy tree's DISK, not its commit. Measured in the
sparse deploy-only tree `C:/tmp/mx-dep-r9`: BOTH paths are absent there.

| run | invocation | result |
|---|---|---|
| **bad control** (mine, discarded) | the SHARED checkout's `.tools/halt-gate-check.sh` from the sparse cwd | **rc=0** -- proved nothing. `HALT_GATE_REPO_ROOT` defaults to the SCRIPT's own `..`, so it self-resolved to the shared tree. `safe-ec2-deploy.sh` runs the sparse tree's OWN copy. |
| **NEGATIVE CONTROL** | the SPARSE tree's own `.tools/halt-gate-check.sh`, no exports | **rc=3**, `Check that failed: unknown-base`, "No agent home folder under /c/tmp/mx-dep-r9/org/tier*_*/ matches the base." r29's failure reproduced in this lane. |
| **POSITIVE** | same script, `HALT_GATE_REPO_ROOT` + `HALT_GATE_INBOX_ROOT` at the shared checkout | **rc=0**, gate scanning THIS lane's real inbox. |

`HALT_OVERRIDE` was never set, in any run.

## The serial the gate resolves -- measured with OPAL_AGENT_SERIAL UNSET, which is the real deploy condition

A4 points `HALT_GATE_REPO_ROOT` at the SHARED checkout, and `HALT_GATE_CONTEXT_FILE` defaults to
`${HALT_GATE_REPO_ROOT}/.comp-graph/.agent_context` -- which is shared and last-writer-wins, and at 12:0xZ
read `SERIAL=0.7.0_AE_CloudOps~CA`, a DIFFERENT lane. The gate's own text names the catastrophic case:
scanning another agent's inbox would exit 0 while a real `[STOP]` sat unread.

**It does not reach that file.** Precedence read from the code (`:69-120`), then exercised: (1) this
checkout's `org/mcp/sessions/<session>.serial`; (2) `OPAL_AGENT_SERIAL`; (3) the shared checkout's
`<session>.serial`; (4) the clobber-proof `<sid>.<serial>.orphan-cleaned` marker; only then
`.agent_context`. With `OPAL_AGENT_SERIAL` unset and A4's roots exported, `halt_gate_resolve_serial`
returned **`0.7.0_AE_CloudOps~MX`** -- step (1), from the session file written at startup A.1, session id
`f4a24c98-9ed7-44e2-adcd-06810d9d5d8c`.

So the stale `~CA` in `.agent_context` is INERT for this gate and needs no row. The gate's `:71` comment
names row Z-W21-S21 as exactly why (1) precedes (2) -- the MX-x-4 fix is already landed. A4 therefore makes
the ANNOUNCE's PHASE B step 2 (write the applier's serial into the WORKTREE's session file) unnecessary
rather than wrong: with repo_root at the shared checkout, step (1) already resolves correctly.

## Live state

r29 `91811b648a` STILL not deployed: S3 `git-ref` and `EC2_MANIFEST.deployed_commit` both read
`aa75078e1b` at 12:1xZ. `<status>` remains `issued`; PHASE B unstarted, which is the instruction.

Watcher re-armed on every expiry, one call each, census 1 row each time (tasks b4gjwwg91, bmjwpk7vo,
b81h4mn11, b7uwzafn8, bmjfe1or0, bldbdtcx3, blum0y4c3, bq9x3ebpi). Zero crons.

Nothing applied, uploaded or deployed. AWS contact read-only throughout.

## Next Steps

1. `[2.0.0_SA_COO~O -> 2.0.0_SA_COO~MI]` r29 deploys, OG-rl-15 completes, then the GO.
2. `[0.7.0_AE_CloudOps~MX]` On the GO, as section 1a now reads at A4: both-plane live-ref read (STOP unless
   both equal r29's sha); NEVER-2 ledger; re-cut deploy-only and rollback trees on that ref; re-prove
   preservation, `ENABLED_INTEGRATIONS`, and the `.env` key RULE (expect 52, `MAIL_SENDER_DOMAIN_TABLE`
   both sides, `ADVI_FEE_STATEMENT_S3_ROOT` absent both sides); re-run the bun pre-check at the then-current
   manifest pin; `ANNOUNCE_MX-r-9_PHASEB.md`; re-read the live ref and STOP if moved; apply with
   `DEPLOY_BASE_REF`, `AGENT_NAME=0.7.0_AE_CloudOps~MX` and A4's two `HALT_GATE_*` exports, printing the
   gate verdict; read back; close the ledger; r9.AC1; proof instance; report once. Roll back on any failed
   leg.

---

# DELTA 2026-10-09 ~12:3xZ -- A5 SUPERSEDES A4; my A4 positive was INSUFFICIENT; A5 proven on the wrapper's own path

**archetype:** VALIDATE

## My A4 proof was in the wrong path, and the issuer was right to say so

A5 @db83d9d163 (cause NFRA_OPLGTW-Z-S75 @6dee08829e): `infra/aws/ec2/safe-ec2-deploy.sh:57` sets
`HALT_GATE_REPO_ROOT="$_CALLING_TOPLEVEL"` **unconditionally, by design (R-53)**, so A4's export can never
reach the predicate. Confirmed by reading `:50-62` myself, not from the message.

**The defect in my own control (commit 11567e1895):** I ran `.tools/halt-gate-check.sh` DIRECTLY. The real
path goes through the wrapper, which overwrites the very variable I was exporting. So my rc=0 proved the
gate works when handed the right root -- it did NOT prove the deploy ever hands it that root. That is the
same class as the malformed bun control earlier this session: **a control placed outside the path under
test.** The negative control was sound; the positive was not.

## A5's mechanism, proven through the WRAPPER's gate path (no deploy run)

The wrapper has NO dry-run or gate-only mode (grep for DRY_RUN/GATE_ONLY/CHECK_ONLY/RESOLVE_ONLY: 0 hits),
so running it would have deployed. Instead its gate environment was replicated exactly from `:38-62` and
`:167-171`: `HALT_GATE_REPO_ROOT` = the calling toplevel, `HALT_GATE_CONTEXT_FILE` and
`HALT_GATE_AUDIT_LOG` pinned to the MAIN tree, `HALT_GATE_INBOX_ROOT` left UNSET to default, sourcing the
DEPLOY TREE's own gate copy, then `halt_gate_check "safe-ec2-deploy:opal-gateway"`.

| | state | verdict |
|---|---|---|
| **NEGATIVE** | `HALT_GATE_REPO_ROOT=C:/tmp/mx-dep-r9`, base folder ABSENT | **rc=3**, `No agent home folder under C:/tmp/mx-dep-r9/org/tier*_*/ matches the base` |
| **POSITIVE** | after `git -C C:/tmp/mx-dep-r9 sparse-checkout add org/tier2_senior/0.7.0_AE_CloudOps` (rc=0) | **rc=0**, resolved serial `0.7.0_AE_CloudOps~MX` |

In the positive, `HALT_GATE_SHARED_ROOT` resolved to the shared checkout and `HALT_GATE_INBOX_ROOT`
defaulted to `<shared>/org/mcp/inbox`, so the gate scanned THIS lane's real inbox -- A5's point that the
inbox limb already reads the shared root (`halt-gate-check.sh:55`) and needs no export.

- **`HALT_OVERRIDE` was never set, in any run.** Instrument: `org/halt-gate-override-audit.log` contains
  `0.7.0_AE_CloudOps~MX` **0 times**; its only entries are from 2026-07-13 by another seat.
- **Release content untouched** by the sparse add: `git status --porcelain infra/aws/ec2/opal-gateway` is
  empty and HEAD is still `7eeb4423f8`. A sparse cone controls checkout, not content.

## Carried to the act

The deploy-only tree is RE-CUT on r29's ref at PHASE B, so `sparse-checkout add
org/tier2_senior/0.7.0_AE_CloudOps` must be REPEATED in the fresh tree, and both verdict lines re-printed
there. A5 also notes that if `2.0.0_SA_COO~O` lands a different mechanism for r29's Z-S75, it does not bind
this order and the issuer rules -- so the mechanism is re-read at the GO, not assumed from today.

## Live state

r29 `91811b648a` still not deployed: both planes read `aa75078e1b` at 12:4xZ. `<status>` `issued`, PHASE B
unstarted. Nothing applied, uploaded or deployed.

## r29 DEPLOYED 12:31Z -- the first GO precondition is MET

| plane | read |
|---|---|
| S3 `opal-gateway-latest.tar.gz` `git-ref` | **91811b648ab119e73e22f8d401dd09f45b8ab19b**, LastModified 2026-10-09T12:31:10Z, 514461 B |
| `EC2_MANIFEST.deployed_commit` | **91811b648ab119e73e22f8d401dd09f45b8ab19b**, deployed_at 2026-10-09T12:31:40Z, deployed_by `0.7.0_AE_CloudOps~Z` |

**The planes AGREE at r29's sha.** One read in between caught them disagreeing (S3 already at r29, the
manifest on this disk still at aa75078e1b) -- that was the 30-second mid-deploy window, not a defect and
not A1's STOP, which is graded AT THE ACT. Re-reading resolved it. Recorded because a disagreement read
during another seat's in-flight deploy is a TRANSIENT, and treating it as the STOP condition would have
manufactured a BLOCKING row against a healthy release.

`mcportal_commit` did NOT move: still `a3bff71ffa`. Re-ran the bun pre-check at the pin rather than
inferring from the earlier run -- **77 of 77, exit=0**. The dashboard-build refusal risk stays closed at
the live pin.

Remaining GO precondition: OG-rl-15 complete, which this seat has NOT measured and does not chase
(`2.0.0_SA_COO~O` reports it to `2.0.0_SA_COO~MI`).
