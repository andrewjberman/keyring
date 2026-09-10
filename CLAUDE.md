# CLAUDE.md — Opal Capital Workspace

**HOW WE WORK and HOW TO THINK: fast and accurate, in that order.** Read sections 1–3 before acting.
This is the LAW INDEX: every rule = imperative + mechanism + pointer. The full annotated text behind
every rule (incidents, measured numbers, history) is `docs/doctrine/CLAUDE_ANNEX.md` — cite it when
a rule's reasoning is contested. Startup mechanics: `org/XXX.md`. Also when you talk to another agent,
*YOU MUST REFER TO THEM BY FULL SERIAL; NEVER SAY HER/HIM/THEM/YOU WHEN COMMUNICATING WITH OTHER AGENTS!*

⛔ **RULE NUMBERS ARE STABLE IDs, NOT READING ORDER** — the list has gaps; sections carry the order.
Rules 4–12, 18 live in `/cloud-ops`; rules **15, 17, 17a, 17b** (data architecture) and **19, 23,
25, 26** (portal/SES/dormancy/apply-locality) live in `docs/doctrine/CLAUDE_ANNEX.md` — numbers
stable, citations resolve there. DS/AE seats read their sections before touching those surfaces.

---

## 1. HOW WE WORK

27. **Every directive/project runs the CANONICAL WORKFLOW L1-L10, ONE OWNER PER STEP, IN ORDER.
    THIS RULE IS A REPRESENTATION OF `/canonical-flow` (Andrew-direct 2026-09-10: "Rule 27 should just be
    a representation of /canonical-flow") -- it is NOT an independent source. Where this text and that
    skill differ, THE SKILL WINS and this rule is the defect. The skill's own reference is the spine,
    `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` section 1 (the limbs and their owners), READ AT HEAD.**
    ⛔ **NO VERSION IS PINNED HERE, DELIBERATELY.** This rule pinned `v3.2` while the spine had reached
    v3.6 with three further amendments unreadable on one fabric -- a constitutional pointer aimed at a
    superseded copy. The skill cites the spine BY PATH ONLY; so does this rule now, and the staleness
    becomes structurally impossible rather than merely corrected.

    | limb | owner (spine s.1) |
    |---|---|
    | L1 brief | `4.0.0_SA_CRO` |
    | L2 endpoint | `1.0.0_SA_CTO` |
    | L3 register | `1.0.0_SA_CTO` — and `0.0.0_AB_MSTR` HOLDS the directive register the row must appear in |
    | L4 PRD | `1.0.0_SA_CTO` (no COO, no CVO) |
    | L5 decomposition + battery | `2.0.0_SA_COO` |
    | L6 task orders, ONE ISSUANCE covering EVERY cell | `2.0.0_SA_COO` |
    | L7 execution | the WORKER named in `<issued_to>`, a subagent of the COO that issued the order |
    | L8 compilation | `3.0.0_SA_CVO` — **its engagement with the project BEGINS HERE, at L8 and not L9** |
    | L9 adjudication | `3.0.0_SA_CVO` |
    | L10 slug / read / recut / close | `3.0.0_SA_CVO` issues the slug; `1.0.0_SA_CTO` routes, ALWAYS; `2.0.0_SA_COO` recuts |

    **L10 HAS TWO STATES AND THE SKILL'S LADDER SEPARATES THEM: `L10 slug` (the slug cut and sent to the
    CTO) then `L10 answered` (a `ROUND_ANALYSIS.round<N>` or a bumped `prd_version`), and the COO's recut
    follows. CLOSED IS A THIRD THING AND NEEDS TWO ARTIFACTS: `COMPLETION_REPORT` + `COMPLETION_GRADES`,
    every grade `REALIZED`.** A round is not closed because every FWD reads REALIZED somewhere.
    L6 fan-out is derived from the decomposition's dependency chains and stated as `fanout:` in the
    issuance commit (default cap 8). The TO's WORKER FACE is the worker's whole context -- cell text,
    absolute paths, ONE clause per criterion with its invocation and expectation; the RECORD FACE never
    travels; a compound criterion is refused at the cut. A worker's write surface is exactly the `<paths>`
    its non-terminal order names (`.tools/owned-paths-validate.py`), its rows mint `<CODE>-W<n>-S<k>`, and
    it writes no telemetry (L7 reads from git). Three tracks share FILES, never messages: the CVO's one
    send is the slug, the CTO's one send is the analysis, a worker cannot be messaged. `0.0.0_AB_MSTR`
    integrates and never works a project. Mid-round the spec AND the decomposition are FROZEN; the only
    off-spec act is a surprise ROW (s.2 below). Gate: `.tools/to-pipeline-gate.py` (the L6 neck).

## 2. HOW MUCH TO CHECK — the speed governor

⛔ **VERIFICATION SCALES WITH THE COST OF BEING WRONG. WHEN THE NEXT CHECK WOULD NOT CHANGE WHAT YOU DO,
STOP.** Most work checks nothing; an unneeded check burns the context the high-stakes judgment needs
later — a CORRECTNESS cost, not a speed one.

22. **EVIDENCE LAW — four axes; who eats the error decides how many you check.**
    | If being wrong costs… | Ask |
    |---|---|
    | me, this turn | nothing. Act. |
    | me later, or another seat | **GRAIN + COVERAGE** |
    | the record (commit, message, TO, report) | **+ STATE** |
    | the world (deploy, delete, grant, served key, claim to Andrew) | **+ DISCRIMINATION** |

    **GRAIN** — the object read IS the object claimed, at the level and vintage claimed. **COVERAGE** —
    evidence spans the claimed set; PRINT THE DENOMINATOR. **STATE** — DESIRED ≠ APPLIED ≠ EXERCISED; a
    description is never a state. **DISCRIMINATION** — could the evidence differ if the claim were false?
    ⛔ **The ORDER is the mechanism: DISCRIMINATION passes inside a wrong GRAIN/COVERAGE/STATE** — every
    instrument then agrees about the same wrong thing. ⛔ **A second seat's confirmation via the FIRST
    seat's method is REPETITION, not corroboration** — name your instrument and whether it differs.
    ⛔ **A CHECK SCOPED TO THE MEMBERS CANNOT SEE A DEFECT IN WHAT THE MEMBERS SHARE.** Verifying each
    member of a set certifies the set CLEAN while a shared dependency beneath it is broken — and every
    per-member arm passes, so nothing fails. **Ask what the members have in COMMON, and check THAT on
    its own; then re-read the population UNSCOPED once.** COST: one extra unscoped read after a scoped pass. NON-APPLICATION: members with
    no shared dependency, and a scoped check that IS the whole question rather than evidence for a
    wider one.
    **"proof / root cause / definitively / source-confirmed" are RESERVED** — legal only past STATE at
    EXERCISED; cite `file:line @ <commit-ish>` (a citation without a vintage is not a citation). It
    governs SUPPLEMENTARY controls, never the substance of the act; size by the claim your work FEEDS;
    re-derive with a DIFFERENT instrument or cite the peer's — never re-run the same command.
    Catalogue: `docs/doctrine/CONTROLS_OVER_CARE.md`.

⛔ **FOUND SOMETHING ODD OFF-TASK? Do NOT halt-and-investigate — APPEND ONE ROW (`spec_asserts` + `world_is`)
to the project's surprise channel and KEEP WORKING. A broker message is NEVER the carrier** (a notifier watching files cannot see an inbox). Tree project: `org/missions/D*/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v{N}.md`
or legacy flat `org/surprise_channel/<CODE>/INVESTIGATION_v{N}.md` — BOTH lane ANY:
the seat that sees it appends its own row; REMEDIATION rows stay CVO's. An ARMED hazard still disarms same-turn via the row's
`disarm_owner`. Gates: `.tools/surprise-row-gate.py` (the row, at commit) + `.tools/proof-of-spec-check.py`
SURPRISES LIMB (a `surprises` entry with no resolving row id blocks a tree TO's `complete` flip).
`docs/doctrine/THE_SURPRISE_CHANNEL.md`.

⛔ **DO NOT MANUFACTURE FRICTION:** (a) **NEVER implement an approval gate on any work unless Andrew
explicitly asks** — an agent-made gate is invisible to him (pre-existing mechanical gates stand; proposing
is legal, implementing is not); (b) **NEVER convert Andrew's word to ONE agent into a gate/stop on
another** — verbatim scope; relay, never adjudicate wider OR narrower; if wider seems plausible, ASK.
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260804_1827Z_NO_INFERRED_GATES_NO_SHADOW_PIPELINES.md`.

## 3. FINDING THINGS FAST

21. **`comp-which "<plain-English question>"` is the reflex; a comp-tool is the DEFAULT for search +
    inspection, raw grep the exception** (text-local, connection-blind). ⛔ **EVERY standalone repo search
    in Bash — `grep/rg/egrep/fgrep/findstr/ack/ag` recursive or directory-scoped, `find` with anything — is
    DENIED per SEGMENT (`&&`/`;`/newline split) and routed to `comp-find`; raw-`aws` INSPECTION is classified
    on ITS OWN SEGMENT.** Mechanism: `.tools/hooks/comp-tool-hud.sh` (kill switch `org/mcp/comprail-gate1.enforce`;
    falsifier `.tools/comprail-gate1-fptest.sh`). NOT gated: a pipe-RECEIVER grep (`cmd | grep`),
    `# rail-checked: <why>`, `/freeform`, native `Grep`/`Glob`, `Read`, operational `aws`. `comp-grep` is a
    forwarder onto `comp-find`.
    ⛔ **A SINGLE-FILE GREP ROUTES TO `comp-read`.** `comp-read <file> --for "<question>"` returns the file's
    SHAPE, regions tagged AUTHORITATIVE-vs-DESCRIPTIVE, every QUALIFIER that limits/negates/corrects a nearby
    claim, intra-file CONTRADICTIONS, and an UNREAD LEDGER; `comp-read <file> --enumerate '<regex>'` prints its
    DENOMINATOR, bands hits (DOCSTRING/COMMENT/DEF/CODE), separates WHOLE-VALUE from SUBSTRING, and WARNs when
    every hit is a fragment — a count is not a reason to reach for `grep`. **NON-APPLICATION:** `grep -q` as a
    pure predicate; any pipe-RECEIVER; FILES OUTSIDE THE REPO CORPUS (a transient tool log, a `/tmp` run output,
    a scratch file — grepping one is NOT off-rail); WRONG-OBJECT errors (comp-read cannot tell you that you
    handed it the WRONG FILE). ⚠ **MECHANISM IS DESIRED-NOT-APPLIED until `comp-tool-hud.sh` changes:** the
    single-file carve-out is live at `:138`/`:141`, `:155-156` and `:182`; until those route to `comp-read`, this
    clause binds agents by reading and nothing by enforcement.
    Traps before quoting any comp-find number (case, substring, denominator certifies the SWEEP not
    the pattern): `docs/architecture/NFRA_COMPRAIL_PRD.md`.
    ⛔ **Never `head` ANY census — `comp-find` OR A RAW GREP.** Use `--band HEAD/DEF`, `--files`,
    `--limit/--page`, `--all`, and `-i` for any token census.
    ⛔ **A PAGE IS NOT AN ANSWER; never conclude from page 1.**
    ⛔ **Do not stop at the first plausible hit** — an early stop and a true absence read identically.
    ⛔ **SCOPED COVERAGE QUALIFIERS: the corpus is `.gitignore`-BOUNDED, NOT tracked-only** — **the DEFAULT is
    `all`** = tracked + untracked + gitignored minus a PRINTED ephemeral floor; `default` = tracked +
    untracked-not-ignored; `ignored` = only-gitignored MINUS the same printed floor; `raw` = everything (an
    every-file denominator uses `raw` — `all` AND `ignored` understate by the floor, disclosed on their own
    denominator lines). comp-find is REPO-ONLY by ruling (a pathspec outside the worktree is not a zero, it is
    `git rc=128`) — **except `--corpus aws`: the LIVE AWS plane** — regex over every aws CloudNode's
    name+arn+props, pathspecs = node_type filters, `drift_class` per hit (`LIVE-no-DECLARED` = in AWS, not in
    the repo), denominator = nodes scanned, vintage = the DB's own `built:` line. **`--hidden <path>` is the
    census verb: run it before converting a zero into an absence, and `0 hit(s) across 0 file(s)` IS
    OUT-OF-CORPUS, NOT ABSENCE.**
20. **Check the dependency graph BEFORE any cloud/infra/data change and before frontend commits** — pick
    from `org/modules/graph/graph-call-manifest.yaml`; QUERY, never rebuild; read the provenance header;
    verify your OWN fresh change against live artifacts, never the graph. `comp-surface-check` is RETIRED
    (no commit-time guard on MP/benchmark/ADVI). `docs/architecture/NFRA_GRAPHS.md`.

## 4. CLAIMS AND SCHEMAS

**THE BUILD LADDER — new code is the LAST resort, in order:** (1) YAGNI; (2) the estate already has it —
`comp-which` for code, `comp-estate --layers/--definitions` for infra + ratified terms; (3) stdlib;
(4) native platform feature; (5) already-installed dependency; (6) one line; (7) only then the MINIMUM
code that works. **No non-ASCII in production code/logs/AWS** — use `OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`.

⛔ **A VALUE MUST CARRY ITS CLAIM — in a field a consumer can reject on** (`measured/inferred/held/absent`);
no such field → you may NOT treat it as measured. **The consuming half is the whole mechanism** — an
unenforced provenance field drifts to unpopulated. `docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md`.

24. **TAXONOMY LAW — four postulates for ANY schema an agent authors or ADOPTS:** (i) MECE over a DECLARED
    domain (hunt the uncovered member); (ii) SAME GRAIN; (iii) INTENT COHERENCE (one axis, one intent);
    (iv) STATE COHERENCE (name which values one remedy does NOT move). **Outcome arrays, typed-result sets
    and predicates ARE schemas.** A value-enum proposal arrives WITH its four-postulate record + word-boundary
    token census, or it is not a proposal. `rcg/rulings/RULINGS.jsonl` R-0006/R-0009.
22a. **INSTRUMENT TRAPS you cannot re-derive at the call site.** CODE: diff deployed bytes against the
    BUILD INPUT (source-map/manifest), never by filename; a cherry-picked/ephemeral pin is resolved by
    CONTENT (`git show <pin>:<file>` + negative control), never `merge-base --is-ancestor`; running-bytes-
    older-than-built passes every rung. DELIVERY: SENT ≠ EMITTED ≠ READ — only an agent-side ACK is a
    sound oracle; an orphaned watcher reads REACHABLE *because* the agent is deaf (anti-correlated).
    RETRIEVAL: a failed retrieval returns a VALUE; paginated `list-*` + `--query length()` returns the
    PAGE count and `--no-paginate` is the hazard; `aws s3 ls` renders LOCAL time, `s3api` UTC; never type
    a literal `Z` into a `--date=format` (renders local, stamps UTC). IAM traps: `/cloud-ops`. Annex §22a.
28. **THE SUBSTRATE TEST — before you BUILD ON a resource, card it: 7 questions, 3 grains** — PROCESS
    (1 methodology, 2 cadence/trigger DESIRED-vs-APPLIED), ARTIFACT (3 persistence/authority, 4 exact
    location), TRUST (5 coverage + denominator, 6 key/identity space, 7 failure mode distinguishable from
    a genuine negative). **Every row carries its OWNER** (remedies do not move together). Binds only when the resource becomes LOAD-BEARING;
    never card what you merely consult. Contract: `org/standards/SUBSTRATE_CARD.schema.json`. Annex §28.
- **NEVER** trust a producer's self-report or rc=0 — verify against the SERVED artifact / live state.

## 5. HARD STOPS (NEVER)

- **NEVER** move served output without never-widen sign-off (CTO+COO); verified DELTA=0 needs no hold.
- **NEVER** leave a confirmed deploy half-landed — finish in-session or roll back + escalate loud; ledger
  entry in `org/critical_paths/change_management/` opened at start, closed at completion. **An IMAGE act (a
  build, a push, a tag move) names in that entry EVERY task family that pulls the tag it moves** — a shared
  `:latest` reaches every family at once and no Terraform-plane control can see it (NFRA_CLDGRPH-S31: two
  builds re-pointed seven families in one night, five counted); pin per family by digest where a family must
  not move. COST: one `describe-task-definition` sweep per image act. NON-APPLICATION: a tag no task
  definition references. ⛔ **An entry a
  device left OPEN proves only that THIS device saw no completion** — before acting on any open/`--red`
  entry, measure the ARTIFACT (rev-parse + describe + is-ancestor with positive control); world-done →
  close SUPERSEDED, never re-execute (a re-execute of an overtaken promote is a REWIND). Annex §NEVER-2.
- **NEVER rebase on a shared branch** (CLOUD/DEV/PROD/main); rejected push = pull-merge, re-push. Gate:
  `.tools/hooks/never-rules-gate.sh`; audited override `# never-override: <reason>`. Scratch branches free.
- **NEVER call a pipeline stale/broken until you resolve the TRADING CALENDAR — count trading days.**
  Everything is `T-1` unless declared; Friday IS Monday's answer. One frontier: `lib/trading_calendar.py`;
  a `comp-freshness` entry lacking `freshness_basis: trading-day-frontier` false-alarms every Monday.
- **NEVER stand up a shadow/build-alongside pipeline, duplicate output path, or standing parity
  comparator** (Andrew complete veto) — build correctly, port directly, same-window rollback; consolidation
  fine. `memory/feedback_no_shadow_channels_veto_build_correctly_and_port.md`.
- **NEVER build an alert/alarm/SNS/SES-send/notification/freshness-checker/monitor unless Andrew explicitly
  asks. Standing moratorium** — canonical routes FIRST; a monitor on an unsettled route measures the wrong
  thing precisely. Findings land as gates or owned blocking items. `docs/architecture/MDPF_DEBTCLEAN_PRD.md` §11–12.
- **Ad-hoc gold runs are PERMITTED FOR QA; production pipelines MUST be scheduled** — success-of-upstream
  as the only trigger is a defect; ad-hoc artifacts are never production evidence.
- **NEVER write device-specific logic into ajb_workspace/portal — DERIVE, don't hardcode** (workspace root
  → `git rev-parse --show-toplevel`; drive prefix → `test -d /cygdrive/c`). Legit only when device-ness is
  the code's PURPOSE. Direction ratified, remediation NOT authorized — surface, don't chase. `LD-0405`.
- **NEVER** bare `terraform apply` (use `safe-apply`), bare `git commit` (use `safe-commit.sh`), or
  `aws lambda update-function-code` (Terraform only). ⛔ Only the terraform limb is mechanically gated —
  the other two are imperatives enforced by nobody. Annex §NEVER-9.
- **NEVER** reference another firm's data from a pipeline tree — **BUCKET *or* KEY-PREFIX**. ⛔ **THE
  MECHANISM IS SUBSTRATE-SHAPED AND BOTH SHAPES ARE LIVE:** shared bucket → key-prefix + IAM condition;
  per-firm buckets → bucket-scoped Deny. **An enumerated ban list lapses SILENTLY when a name changes**. Gate: `.tools/ds-precommit-check.py`
  `_CROSS_FIRM_FOREIGN_{BUCKETS,KEY_PREFIXES}` — **the guard is only as wide as its enumeration, so a
  new firm name is a GATE EDIT, not just an infra act.** ⚠ IAM limb: **DESIRED, apply UNVERIFIED**.

## 6. LANE + COMMIT MECHANICS

13. **DS owns commit→QA-deploy for `data/*/scripts/{gold,silver,bronze}/*.py`** incl. `aws s3 cp`; DT/AE =
    infra/PROD-triggers/multi-pipeline. Enforced by `.tools/safe-deploy.sh`; shared homes deploy under the
    S3-membership guard (404 = loud skip, first-mints explicit). **cot is a separate firm from bd — never
    mirror/sync.** `docs/architecture/ADHC_DSFLOW.md`.
14. **Every `.py` edit passes `.tools/commit-gate.sh`** (py_compile + ds-precommit + ruff py39). Universal.
14a. **Commit via `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -F <msgfile> -- <paths>`;
    do NOT pre-`git add`; `-F` not `-m`** — and the message file must be written by a NON-SHELL writer
    (Write tool / python): a `printf`/heredoc-built file re-opens the injection one step earlier. `--force`
    bypasses only contamination checks, never a lane refusal — that escape is `GIT_COMMIT_AUTHOR_OVERRIDE=
    <LANE>`, audited, SINGULAR (N lanes = N commits). `docs/architecture/ADHC_OWNPTH.md`.
14b. **While other seats are LIVE, commit anything bigger than a one-file edit in YOUR OWN linked
    worktree and merge it back in a gap** — five seats plus their worker subagents share ONE MUTABLE
    INDEX, so the check-then-act window is now shorter than the staging cadence: `2.0.0_SA_COO` measured
    `staged=0` and had the very next merge refuse on a file staged in the seconds between. Mechanism:
    `git worktree add ../<slot> -b <branch>` — a linked worktree carries its OWN index AND its own merge
    state, which is why `/dispatch` already mandates one per worker slot; merge back with
    `.tools/safe-merge.sh` (its `--continue` limb keeps a conflicted drain inside the guards).
    ⛔ **THE GUARDS ARE NOT THE PROBLEM — every refusal measured so far was CORRECT and each prevented a
    real sweep** (`org/git-author-override-audit.log`: 3 audited `MERGE-REFUSED`, 2 on `2.0.0_SA_COO`
    and 1 on `1.0.0_SA_CTO`, each naming a FOREIGN MERGE_HEAD and `nothing staged by this run`). Only
    those three are offered as contention evidence: two further refusals the same evening were traced by
    their own author partly to itself, and a self-inflicted block is not a crowding measurement.
    The refusal RATE rises with the live-seat count, and a correct refusal you could have avoided still
    costs a retry and sometimes a round trip.
    ⛔ **IT INVERTS FOR AN APPEND-ONLY SHARED FILE AND YOU MUST NOT ISOLATE THERE** (`2.0.0_SA_COO~A`,
    accepted by `2.0.0_SA_COO` without reservation): two branches appending to one channel land at the
    SAME OFFSET and both restate the header, so a side branch converts a SECONDS-LONG STAGING RACE into a
    GUARANTEED CONFLICT — measured 3 of 3 on round 4's drains (NFRA_CLDGRPH-S36). Trading a probabilistic
    race for a certain conflict is a bad trade, and the conflict path is the one that cost this estate a
    hand-finished merge with neither guard running. So:
        a file only YOU touch          -> ISOLATE (a worktree costs 30 s and touches nobody)
        an APPEND-ONLY SHARED file     -> DO NOT ISOLATE; take the shared index's seconds-long race
        (a surprise channel, a log)
    ⛔ **AND EDIT IN THE WORKTREE WHERE YOU WILL COMMIT.** Copying an edit out to a branch leaves the
    original behind in the shared tree as a blocker against your OWN merge ("local changes the merge would
    overwrite"), and it reads exactly like another seat's contention until you read the refusal text.
    `2.0.0_SA_COO` traced two of its own four "contention" instances to precisely this and said so.
    COST: one `git worktree add` plus a merge back. NON-APPLICATION: a trivial one-file commit; a seat
    working alone; an append-only shared file (above); and any commit that MUST be graded against the
    shared index (a drain — that is what `safe-merge.sh` grades). Found by `2.0.0_SA_COO` 2026-09-04
    after it and `0.0.0_AB_MSTR` hit the same contention from opposite sides within minutes and chose
    opposite remedies, both defensible — which is the tell that the contended RESOURCE, not either seat,
    was the problem.
16. **Local bash = Git Bash 3.6.7 default utilities only** (no pgrep/pkill/flock/pidof/setsid/wget without
    guarded fallback). `.tools/jq.exe` is vendored — resolve it first, fail closed loud. ⛔ **Never
    `2>/dev/null` a read whose EMPTINESS carries a verdict.** `docs/architecture/ADHC_BASHFIX.md`.

## Agent Autonomy

**Do NOT ask permission** to read/write/build/test/commit/push CLOUD-DEV/run scripts/call Opal-owned APIs.
**Excluded: all egress off Opal infrastructure.** Human confirmation ONLY for: recursive deletion,
destructive git, dropping tables/S3 deletes, stopping EC2, anything unrecoverable.
- **NEVER call an external vendor API without Andrew's explicit per-use word** — availability is not
  authorization. `memory/feedback_availability_is_not_authorization_vendor_egress.md`.

**NEVER self-wind-down, never default to "tonight"** — drive every addressable task NOW; wind-down only on
Andrew's word. **"Waiting for the scheduled run" is the same coast-failure** — fire the ad-hoc QA run (it
tests; the scheduled fire stays the acceptance); the one exception is when the ad-hoc would destroy the
discriminator the scheduled run exists to produce — name that evidence or the wait is the defect.

29. **A REPORT IS NOT THE DELIVERABLE WHILE UNBLOCKED WORK REMAINS — the turn ends when the WORK does.**
    The tell: a forward-looking closer ("cutting the TOs now"). Gate before ending ANY turn: *"is there an
    act this turn said it would do that it has not done?"* — yes + unblocked → do it, report after.
    Ending on a report is CORRECT only when the next act is blocked/gated/out-of-lane — SAY WHICH. Cost
    zero: the rule reorders a turn. `LD-0461`.

## Detailed Documentation

Deploy protocols `docs/deployment/` · graph `docs/architecture/NFRA_GLOBGRPH_PRD.md` · critical surfaces
`org/critical_paths/README.md` · start guide `org/XXX.md` · **Bloomberg, ANY scenario: READ
`integrations/bloomberg/READ_HERE.md` FIRST** (two-phase budgeted sign-in; a refusal names the SURFACE;
derived layer is current-day-only; never mint `data/bloomberg/`).

## Git

- Working branch `CLOUD`; portal submodule `DEV`/`PROD`. Shims reach shells via `~/bin` FORWARDERS (profiles
  never load): on WARN run `bash .tools/provision-path-shims.sh`. AWS via the `.tools/aws` shim (+`aws.cmd`,
  both or neither); never bare `MSYS_NO_PATHCONV=1 aws`.
- `MSYS_NO_PATHCONV=1` only for TF imports/ARN args and `git show <ref>:<path>` with a slashed ref; NEVER
  for `git push`/`safe-apply`. **Never `2>/dev/null` a `git show`** — the mangle returns clean-empty; run a
  positive control beside any ABSENT verdict.
- Python/PS shelling to bash → `.tools/git_bash_resolver.py`; Python spawning ANY MSYS binary →
  `.tools/msys_argv_guard.py msys_safe_run()` — never bare unix names in argv. Corruption oracle: echo the
  argument back.
- **Put the control on the RETRIEVAL:** outputs don't carry their own frame — print the denominator beside
  the number; paginated `list-*` auto-paginate then count client-side; name the QUESTION'S plane before the
  sweep's (no control inside the wrong plane catches a wrong-plane error; authorship is not evidence).
- **A commit message is an EXECUTION VECTOR** — `-F <file>` authored by a non-shell writer; `-m` deprecated
  for any body with special characters. `LD-0276`.
- **NEVER compose a report of a COMPLETED act in the SAME tool call as the act — read the number, then
  write the sentence.** Does not bind the `safe-commit -F` message file (atomic by necessity). Envelope
  sibling: verify a substantive send by `wc -c` on the delivered file.
- **Never "you/your" about a specific seat in a multi-recipient message — name the serial + msg-id**
  (second person resolves per reader).
- **A commit report states its PUSH STATE as a MEASURED value:** "on origin @hash (ls-remote read)" ·
  "LOCAL @hash (ls-remote read)" · "push state UNREAD" — never a default; the claim is perishable and ages
  the moment an integrator runs.

## Portal

- `portal/` — `bun install && bun run dev --port 5175`; resolve bun via profile, don't bake a path.

## Changing this file

**A rule = imperative (≤2 lines) + mechanism + pointer — gates teach at violation time; prose taxes every
session.** A new verification rule STATES ITS COST AND NON-APPLICATION or it does not land (without that
clause the file only ratchets). **A law edit has THREE surfaces: commit + same-turn MCP broadcast to live
seats + push state stated in the broadcast** — the commit fixes the record, only the broadcast fixes the
fabric. **Where things go:** imperative+mechanism → here; principle → `docs/doctrine/`; what happened →
`docs/references/`; session mechanics → `org/XXX.md`; decision → `org/tier0/ledger/`. **Never cut a
MECHANISM to save space — but the incident that taught it is not the rule**; a principle earns its place by
being actionable WITHOUT its incident. Long-form text of any rule: `docs/doctrine/CLAUDE_ANNEX.md`.
