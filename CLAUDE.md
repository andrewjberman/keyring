# CLAUDE.md -- Opal Capital Workspace

**HOW WE WORK and HOW TO THINK: fast and accurate, in that order.** Read sections 0-3 before acting.
When you address another agent, use its FULL SERIAL; never her/him/them/you.

RULE NUMBERS ARE STABLE IDs, NOT READING ORDER. Rules 4-12 and 18 live in `/cloud-ops`; rules 15, 17, 17a, 17b
(data architecture) and 19, 23, 25, 26 (portal/SES/dormancy/apply-locality) live in `docs/doctrine/CLAUDE_ANNEX.md`.

---

## 0. HOW WE COMMUNICATE

0. **Write standard technical English. A prose response stays under 150 words unless asked for more; a technical
   spec or structured manifest (a JSON index, a YAML registry, a schema) is never truncated or abridged.**
   Mechanism: the broker refuses a message over 150 words unless it is a file path plus one line (`org/mcp/server.py`,
   LD-0615); a response binds by reading. Exceptions: a prose-specific skill's output (`/exec-sum`, `/daily-sprint`,
   `/outcome-check`) and a deliverable document (a brief, PRD, report or record). Threshold source:
   `docs/briefs/process-architecture-verification-bureaucracy-brief-20260924.md` section 1.4. Order:
   `ANDREW_DIRECT_20260924_160xZ_*` (tier1 CTO).
33. **Every path an agent posts is ctrl+click accessible: an absolute `file:///` URI (forward slashes, a space as `%20`) or
   a markdown link to one.** A path bound for another box (commit, broker message) also carries its repo-relative form,
   since an absolute path names one box. Binds by reading. Order: `ANDREW_DIRECT_20261013_174xZ_*` (tier1 CTO).

## 1. HOW WE WORK

27. **Every directive/project runs the CANONICAL WORKFLOW L1-L10, ONE OWNER PER STEP, IN ORDER.** Spec:
    `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` -- cite by path, read at HEAD, no version pinned here; where this
    rule and the spine differ, the spine wins. Gate: `.tools/to-pipeline-gate.py` (the L6 neck).
    - **L1 brief** -- `4.0.0_SA_CRO` only.
    - **L2 endpoint** -- `1.0.0_SA_CTO` only. NO FWD IS A WAIT: every outcome is provable by an act a seat can take on
      demand; a mechanism driven deliberately, the organic case kept as the negative arm. A genuinely essential wait is
      expressly qualified on the outcome with its reason and Andrew's word.
    - **L3 register** -- `1.0.0_SA_CTO` only, and the CTO writes every carrier itself in its own commit (tree row,
      generated index, `DIRECTIVES.yaml` members line, `MACROS.yaml` enum). `0.0.0_AB_MSTR` is PERMIT on the last two
      as integrator fallback and holds no gate.
    - **L4 PRD** -- `1.0.0_SA_CTO` only.
    - **L4-R sign-off** -- the PRD has TWO HALVES, each signed as a file in lane `TREE_PRD_SIGNOFF` bound to the HASH of
      its sections, never to `prd_version`. `3.0.0_SA_CVO` signs the RATIFIED-TEXT half (ENDPOINT + CONTRACTS), always;
      `4.0.0_SA_CRO` signs the BRIEF half, or a live `2.0.0_SA_COO` not holding the round in its stead. Stamp:
      `python .tools/prd-signoff.py sign|refuse <CODE> --half ... --review <path>@<pin>`; `status <CODE>` is the one
      read of what is owed. The L4 notifier delivers each owed half, withholds the COO delivery until both are SIGNED at
      the current bytes, nudges OVERDUE after 60 minutes with the CTO copied, and re-routes an overdue brief half to a
      live COO. `.tools/to-pipeline-gate.py` LIMB 6 refuses a NEWLY-ADDED task order against a PRD with an unsigned
      half; it does NOT fire on a modification, except GATE (viii) (`<placeholders>`), which also grades a MODIFIED order
      that already declares `<placeholders>` at HEAD. On a modification, "do not cut against a stale half" is human
      discipline. One rule for all three: `.tools/prd_signoff_lib.py`. A header-only bump re-opens nothing; an L10
      addendum re-opens only the half it changed. A citation ages separately from the text it quotes: verify a quote by
      printing the bytes at the cited line, never by grepping for the quote. PROPORTIONATE SIGN-OFF (Andrew-direct
      2026-09-24): for a single-round or sub-week project the CVO signs the ratified-text half once, the brief half
      is accepted when the CRO wrote the brief, and only an ENDPOINT change re-signs -- a wording change under the
      section hash does not re-open a half and withholds no delivery (until `prd_signoff_lib.py` binds the ENDPOINT
      hash alone, the re-sign of a wording change is a formality the notifier does not wait on).
    - **L5 decomp + battery; L6 ONE ISSUANCE covering every cell** -- `2.0.0_SA_COO` only; fan-out derived from the
      decomp's dependency chains and stated as `fanout:` data in the issuance commit, default cap 8. The issuer
      amends its own task-order criteria WITHOUT a CTO ruling (Andrew-direct 2026-09-24), stating in the amendment
      commit which gate limb graded the modification or that none did; the CTO reads amendments at the round-N
      analysis.
    - **L7 execute** -- WORKER SUBAGENTS of the COO, `0.9.0_WK_<CODE>~<n>`, one worktree each, no send tool. The TO's
      WORKER FACE is the worker's whole context (cell text, absolute paths, one clause per criterion with its invocation
      and expectation); the RECORD FACE never travels; a compound criterion is refused at the cut.
    - **L8 compile** -- `3.0.0_SA_CVO`, whose engagement begins here (spine `:320`, `:475`, `:489`). The spine's L8 is
      the CHANNEL compile (input: new investigation rows; output: the compiled channel + watermark). The COO's drain-end
      task-order packet is a different artifact sharing the label; that ambiguity is placed, not resolved.
    - **L9 adjudicate** -- JUDGMENT criteria are graded here and never self-graded.
    - **L10** -- ONE SLUG to the CTO, always, only after every task order of the round is terminal and every BLOCKING
      or ARMED row is dispositioned. The CTO answers with a PRD addendum (an FWD no cell served) or the ROUND-N ANALYSIS the COO recuts in ONE issuance;
      CLOSED when every FWD grades REALIZED. The three route tokens are retired.
    - **Round 1 builds the thread; every later round enriches** (spine v3.16-3.18). `FWD-1` of a product, pipeline or
      backend/infra product is ONE live journey end to end; round 1 decomposes over its hops; each round-N analysis
      ends in the ENRICHMENT LIST the next round cuts; a build TO carries at most THREE mechanical criteria, repo-wide
      hygiene running at the drain. A product in flight with no working journey goes to `/closer` on Andrew's word (a
      read-only trace needs none); `/canonical-drive` skips a row carrying `closer_contract`. Non-application: a pure
      governance project.
    - **Three tracks share FILES, never messages**: the CVO's one send is the slug, the CTO's one send is the analysis,
      a worker cannot be messaged. `0.0.0_AB_MSTR` integrates and never works a project. Mid-round the spec AND the
      decomposition are FROZEN; the only off-spec act is a surprise ROW (section 2).
    - **ONE ISSUER PER ROUND; a WORKSTREAM is a SCOPE, not a round.** Two COO instances issuing into the same round is
      the collision. One project may carry several workstreams with disjoint boundaries and disjoint write surfaces
      under different `~lane` instances.
    - **Seating: ONE PROJECT PER TIER-2 SEAT INSTANCE**, enforced by `.tools/to-decomp-ref-lint.py`'s seating check.
      It does NOT reach Tier 1: a Tier-1 seat may hold several projects and seat several Tier-1 lanes. Record:
      `ANDREW_DIRECT_20260910_173xZ_*` (tier1 CTO). CloudOps is the exception, seated by macro: rule 34.
    - A worker's write surface is exactly the `<paths>` its non-terminal order names (`.tools/owned-paths-validate.py`);
      its rows mint `<CODE>-W<n>-S<k>`; it writes no telemetry (L7 reads from git). The eight v3 carriers refuse (spine
      section 3), as does the drain's refuser on the merged index (`.tools/safe-merge.sh`); spine section 4 binds by
      reading.

32. **SEAT ROLES: MSTR runs infrastructure and rules no project; the CTO holds its fabric's open calls and rules
    the ones that touch only it, a cross-fabric call going MSTR to MSTR; COOs work by a drive skill; every fabric
    seats a CVO; the CRO briefs, and researches S3+ or WORLD operations.** Mechanism: launchers, skills and gates
    (DESIRED; binds by reading). Spec: `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` C-SEATS.
34. **CLOUDOPS IS SEATED ONE LANE PER MACRO PER BOX, never one per task: every CloudOps order of that macro's projects
    goes to the live macro lane (`0.7.0_AE_CloudOps~<MACRO><n>`); a fourth project with live orders at once seats a
    second lane for the macro.** Mechanism: MSTR's seating, and the seating check in `.tools/to-decomp-ref-lint.py`, which
    refuses a CloudOps order outside the lane's macro (DESIRED until landed there). Order:
    `ANDREW_DIRECT_20261016_154xZ_CLOUDOPS_ONE_SEAT_PER_MACRO_PER_BOX.md` (tier1 CTO).

## 2. HOW MUCH TO CHECK -- the speed governor

**VERIFICATION SCALES WITH THE COST OF BEING WRONG. WHEN THE NEXT CHECK WOULD NOT CHANGE WHAT YOU DO, STOP.** An
unneeded check burns the context the high-stakes judgment needs later.

22. **EVIDENCE LAW -- the `<risk>` class decides how much a piece of work is checked; no seat reasons its way to it.**
    `LOCAL` / `SERVED` / `WORLD` on every task order (spine v3.19 L6; `.tools/to-pipeline-gate.py` GATE xii), plus the
    COO's one real run of each outcome at close. The four-axis table and its corollaries (corroboration cap, shared-
    dependency check, ABSENT != EXERCISED-AGAINST, reserved words) are the data behind the class:
    `docs/doctrine/CLAUDE_ANNEX.md` section 2, rule 22.

**FOUND SOMETHING ODD OFF-TASK? Do NOT halt-and-investigate -- APPEND ONE ROW (`spec_asserts` + `world_is`) to the
project's surprise channel and KEEP WORKING. A broker message is NEVER the carrier.** Tree project:
`org/missions/D*/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v{N}.md`; legacy flat
`org/surprise_channel/<CODE>/INVESTIGATION_v{N}.md` -- both lane ANY; REMEDIATION rows stay the CVO's. An ARMED hazard
disarms same-turn via the row's `disarm_owner`. Gates: `.tools/surprise-row-gate.py` (the row, at commit) +
`.tools/proof-of-spec-check.py` SURPRISES LIMB (a `surprises` entry with no resolving row id blocks a tree TO's
`complete` flip). `docs/doctrine/THE_SURPRISE_CHANNEL.md`.

**DO NOT MANUFACTURE FRICTION:** (a) NEVER implement an approval gate on any work unless Andrew explicitly asks
(pre-existing mechanical gates stand; proposing is legal, implementing is not); (b) NEVER convert Andrew's word to ONE
agent into a gate/stop on another -- verbatim scope; relay, never adjudicate wider or narrower; if wider seems plausible,
ASK. `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260804_1827Z_NO_INFERRED_GATES_NO_SHADOW_PIPELINES.md`.

## 3. FINDING THINGS FAST

21. **Search the repo with `comp-find`, never blind recursive grep; read AWS through the served graph before you list
    it; a known path needs no router.** The rail DENIES four things: a recursive or directory-scoped repo search, a
    `find` over the repo, an AWS enumeration the graph holds, and a census output cut before its denominator. Every
    denial prints WHY and RUN NEXT, the command that answers: run it next. Mechanism: `.tools/hooks/comp-tool-hud.sh`
    + `comp_rail_direct.py` (kill switch `org/mcp/comprail-gate1.enforce`; falsifier `.tools/comprail-gate1-fptest.sh`).
    - A DENIAL RUNS NOTHING IN ITS CALL. Its REMAINDER line is the rest of your call, ready to run as is.
    - FREE, never denied: one named file (infra and `.tf` included), a named folder, a pipe receiver, any path outside
      a checkout, a live AWS `get`/`simulate`/`describe` of one resource, `comp-* --help`, native `Grep`/`Glob`/`Read`,
      `# rail-checked: <why>` (audited), `/freeform`.
    - `comp-which "<question>"` is for when you do not know which tool answers; a question naming an existing file
      returns `comp-read <path>`. Ask a file a question with `comp-read <path> --for "<question>"`; a denominator with
      `--enumerate '<regex>'`. COST: one denial round-trip. NON-APPLICATION: the FREE list.
    - Traps before quoting any comp-find number: `docs/architecture/NFRA_COMPRAIL_PRD.md`. Never `head` any census;
      use `--band HEAD/DEF`, `--files`, `--limit/--page`, `--all`, and `-i` for a token census. A page is not an answer.
      Do not stop at the first plausible hit: an early stop and a true absence read identically.
    - Corpus scopes: the DEFAULT is `all` (tracked + untracked + gitignored minus a printed ephemeral floor);
      `default` = tracked + untracked-not-ignored; `ignored` = only-gitignored minus the floor; `raw` = everything.
      comp-find is repo-only (a pathspec outside the worktree is `git rc=128`, not a zero) except `--corpus aws`, the
      live AWS plane (regex over every CloudNode's name+arn+props; pathspecs = node_type filters; `drift_class` per hit;
      denominator = nodes scanned; vintage = the DB's `built:` line). `--hidden <path>` is the census verb: run it
      before converting a zero into an absence; `0 hit(s) across 0 file(s)` is OUT-OF-CORPUS, not absence.
20. **Check the dependency graph BEFORE any cloud/infra/data change and before frontend commits** -- pick from
    `org/modules/graph/graph-call-manifest.yaml`; QUERY, never rebuild; read the provenance header; verify your OWN
    fresh change against live artifacts, never the graph. `comp-surface-check` is retired.
    `docs/architecture/NFRA_GRAPHS.md`.

## 4. CLAIMS AND SCHEMAS

**THE BUILD LADDER -- new code is the LAST resort, in order:** (1) YAGNI; (2) the estate already has it (`comp-which`
for code, `comp-estate --layers/--definitions` for infra + ratified terms); (3) stdlib; (4) native platform feature;
(5) already-installed dependency; (6) one line; (7) only then the MINIMUM code that works.

**No non-ASCII in production code/logs/AWS** -- use `OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`. In a file that already
carries non-ASCII, the only two safe moves are ALL non-ASCII out, or every reader explicit (`encoding='utf-8'`) --
never a subset, because a default cp1252 read raises only on five undefined bytes and decodes every other non-ASCII
character silently wrong. Detector: `len(b) - len(b.decode('utf-8'))` is a zero/non-zero detector whose magnitude is a
BYTE DELTA, never a character count; for a count use `sum(1 for ch in text if ord(ch) > 127)`.

**A VALUE MUST CARRY ITS CLAIM -- in a field a consumer can reject on** (`measured/inferred/held/absent`); no such
field -> you may NOT treat it as measured. The consuming half is the whole mechanism.
`docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md`.

24. **TAXONOMY LAW -- four postulates for ANY schema an agent authors or ADOPTS:**
    (i) MECE over a DECLARED domain. Hunt the uncovered member BY SUBTRACTION from a printed denominator, never by a
    forward list. The subtraction's domain must be the claim's population: falsify the domain first with ONE unscoped
    read of the term over the corpus, denominator printed; a member the domain does not hold voids the subtraction; a
    wrong-domain census returning EMPTY gets acted on, so the tell is a denominator whose scope (in PATH and in TIME) is
    narrower than the sentence beside it. An inherited claim has no denominator to narrow: the tell is grammatical --
    NEVER / ALWAYS / EVERY / NOTHING / ANY in a sentence whose evidence names one object or none; ask which instrument
    produced it and what that instrument can see. Non-application: a sentence whose subject IS the swept or exercised
    object.
    (ii) SAME GRAIN. (iii) INTENT COHERENCE (one axis, one intent). (iv) STATE COHERENCE (name which values one remedy
    does NOT move). Outcome arrays, typed-result sets and predicates ARE schemas. A value-enum proposal arrives with
    its four-postulate record + word-boundary token census, or it is not a proposal. `rcg/rulings/RULINGS.jsonl`
    R-0006/R-0009.
22a. **INSTRUMENT TRAPS you cannot re-derive at the call site.** CODE: diff deployed bytes against the BUILD INPUT
    (source-map/manifest), never by filename; a cherry-picked/ephemeral pin is resolved by CONTENT (`git show
    <pin>:<file>` + negative control), never `merge-base --is-ancestor`; running-bytes-older-than-built passes every
    rung. DELIVERY: SENT != EMITTED != READ -- only an agent-side ACK is a sound oracle; an orphaned watcher reads
    REACHABLE because the agent is deaf. RETRIEVAL: a failed retrieval returns a VALUE; paginated `list-*` +
    `--query length()` returns the PAGE count and `--no-paginate` is the hazard; `aws s3 ls` renders LOCAL time,
    `s3api` UTC; never type a literal `Z` into a `--date=format`. IAM traps: `/cloud-ops`. ROSTER:
    `get_agent_status(<serial>)` is THREE LIMBS -- liveness / PID / `Working on` are per-LANE; `Pending task orders`
    and `Latest logs`/`Blockers` are BASE-scoped and exact-string-match a free-text `<status>`, so they are never a
    lane's orders and never a count of what is open; to ask what a LANE owes, parse `<issued_to>` from the order
    files. Annex section 22a.
28. **THE SUBSTRATE TEST -- before you BUILD ON a resource, card it: 7 questions, 3 grains** -- PROCESS (1 methodology,
    2 cadence/trigger DESIRED-vs-APPLIED), ARTIFACT (3 persistence/authority, 4 exact location), TRUST (5 coverage +
    denominator, 6 key/identity space, 7 failure mode distinguishable from a genuine negative). Every row carries its
    OWNER. Binds only when the resource becomes LOAD-BEARING; never card what you merely consult. Contract:
    `org/standards/SUBSTRATE_CARD.schema.json`. Annex section 28.
30. **EVERY NEW PIPELINE IS BUILT TO LGIC -- its homes, tenancy and names come from the canon and its builders.** Tier
    homes and tenancy: `infra/logic/02_DOCTRINE.md` R1-R21. Every S3 address is `lib/opal_naming.py address()` output
    and every resource name is `name()` output; a builder REFUSAL is a missing registry row to add
    (`infra/logic/registry/`), never a hand-typed workaround; a deliberate departure is an R20 register entry Andrew
    acknowledges. The L4 PRD cites builder output for every new address and name, and the CTO refuses a PRD that types
    one; the commit-time naming gate REFUSES names today (LGIC_ENFORCE). Non-application: existing pipelines --
    each reaches conformance through its own migration project (R19), never as a rider.
- **NEVER** trust a producer's self-report or rc=0 -- verify against the SERVED artifact / live state.

## 5. HARD STOPS (NEVER)

- **NEVER** move served output without never-widen sign-off (CTO+COO); verified DELTA=0 needs no hold. A sign-off
  names the act's BLAST RADIUS (what the act may touch and the rollback per key), never the producer's decision. Where
  a half names an expected outcome, that outcome is read from the producer's own rule at signing, never predicted from
  the input's shape, and the half covers BOTH branches or it is not signed. First count the writers of the named
  property: N writers = N rules read, and N is printed. A `--month`-style override that lets a scheduled producer run
  off its own clock creates a new reachable state on the manual path: the sign-off covers it or the override does not
  land. Non-application: an act whose write set is a literal key list the actor controls.
- **NEVER** leave a confirmed deploy half-landed -- finish in-session or roll back + escalate loud; ledger entry in
  `org/critical_paths/change_management/` opened at start, closed at completion. An IMAGE act names in that entry
  EVERY task family that pulls the tag it moves (one `describe-task-definition` sweep); pin per family by digest where
  a family must not move. An entry a device left OPEN proves only that THIS device saw no completion: before acting on
  any open/`--red` entry, measure the ARTIFACT (rev-parse + describe + is-ancestor with a positive control); world-done
  -> close SUPERSEDED, never re-execute. During a WORKER deploy the entry sits on the worker's branch until the drain,
  so a shared-tree read of `.open_deploys/` is not evidence: read EVERY live worktree (`git worktree list --porcelain`,
  then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), union them, print the per-tree
  denominator, and use `ls-tree`/`ls -a` since `ls -1` hides `.unindexed_red_state.json`. Annex section NEVER-2.
- **NEVER rebase on a shared branch** (CLOUD, box/*, DEV/PROD/main); rejected push = pull-merge, re-push. Gate:
  `.tools/hooks/never-rules-gate.sh`; audited override `# never-override: <reason>`. Scratch branches free.
- **NEVER call a pipeline stale/broken until you resolve the TRADING CALENDAR -- count trading days.** Everything is
  `T-1` unless declared; Friday IS Monday's answer. One frontier: `lib/trading_calendar.py`; a `comp-freshness` entry
  lacking `freshness_basis: trading-day-frontier` false-alarms every Monday.
- **NEVER stand up a shadow/build-alongside pipeline, duplicate output path, or standing parity comparator** (Andrew
  complete veto) -- build correctly, port directly, same-window rollback; consolidation fine. Record:
  `ANDREW_DIRECT_20260804_1827Z_*` (tier1 CTO).
- **NEVER build an alert/alarm/SNS/SES-send/notification/freshness-checker/monitor unless Andrew explicitly asks.
  Standing moratorium** -- canonical routes first. Findings land as gates or owned blocking items.
  `docs/architecture/MDPF_DEBTCLEAN_PRD.md` sections 11-12.
- **Ad-hoc gold runs are PERMITTED FOR QA; production pipelines MUST be scheduled** -- success-of-upstream as the only
  trigger is a defect; ad-hoc artifacts are never production evidence.
- **NEVER write device-specific logic into ajb_workspace/portal -- DERIVE, don't hardcode** (workspace root -> `git
  rev-parse --show-toplevel`; drive prefix -> `test -d /cygdrive/c`). Legit only when device-ness is the code's
  PURPOSE. Surface, don't chase. `LD-0405`.
- **NEVER** bare `terraform apply` (use `safe-apply`), bare `git commit` (use `safe-commit.sh`), or `aws lambda
  update-function-code` (Terraform only). Only the terraform limb is mechanically gated. Annex section NEVER-9.
- **NEVER** reference another firm's data from a pipeline tree -- BUCKET or KEY-PREFIX. The mechanism is
  substrate-shaped and both shapes are live: shared bucket -> key-prefix + IAM condition; per-firm buckets ->
  bucket-scoped Deny. Gate: `.tools/ds-precommit-check.py` `_CROSS_FIRM_FOREIGN_{BUCKETS,KEY_PREFIXES}` -- the guard is
  only as wide as its enumeration, so a new firm name is a GATE EDIT. IAM limb: DESIRED, apply unverified.

## 6. LANE + COMMIT MECHANICS

14. **Every `.py` edit passes `.tools/commit-gate.sh`** (py_compile + ds-precommit + ruff py39). Universal.
14a. **Commit via `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -F <msgfile> -- <paths>`; do NOT
    pre-`git add`; `-F` not `-m`; the message file is written by a NON-SHELL writer** (Write tool / python). `--force`
    bypasses only contamination checks, never a lane refusal; that escape is `GIT_COMMIT_AUTHOR_OVERRIDE=<LANE>`,
    AUDITED (`org/git-author-override-audit.<device>.log`, one file per box, is the instrument). The override's value is not validated and its exit
    covers the entire staged set, so ONE LANE PER COMMIT is a discipline, not a mechanism.
    `docs/architecture/ADHC_OWNPTH.md`.
14b. **While other seats are LIVE, commit anything bigger than a one-file edit in YOUR OWN linked worktree and merge it
    back in a gap** (`git worktree add ../<slot> -b <branch>`; merge back with `.tools/safe-merge.sh`, whose
    `--continue` limb keeps a conflicted drain inside the guards). It INVERTS for an APPEND-ONLY SHARED FILE (a surprise
    channel, a log): do NOT isolate there; take the shared index's seconds-long race, because two branches appending to
    one channel land at the same offset and guarantee a conflict. EDIT IN THE WORKTREE WHERE YOU WILL COMMIT.
    Non-application: a trivial one-file commit; a seat working alone; a drain (graded against the shared index).
16. **Local bash = Git Bash 3.6.7 default utilities only** (no pgrep/pkill/flock/pidof/setsid/wget without guarded
    fallback). `.tools/jq.exe` is vendored -- resolve it first, fail closed loud. Never `2>/dev/null` a read whose
    EMPTINESS carries a verdict. `docs/architecture/ADHC_BASHFIX.md`.

## Agent Autonomy

**Do NOT ask permission** to read/write/build/test/commit/push CLOUD-DEV/run scripts/call Opal-owned APIs.
**Egress is open on every channel, except Bloomberg.** Human confirmation ONLY for: recursive deletion, destructive git,
dropping tables/S3 deletes, stopping EC2, anything unrecoverable. Deleting a ref already contained in its trunk loses no
commit and is not destructive git (`ANDREW_DIRECT_20261009_035xZ_GOVERN_ADJUDICATES_YES_TO_BOTH.md`, tier0_exec).
- **PUSHES NEED NO WORD FROM ANDREW -- agents push at will** (workspace `box/*` and `CLOUD`; portal, `opal_ai` and `mcportal`
  `DEV` and `PROD`). ONE exception: a portal `PROD` push that changes a CLIENT-FACING page (one a partner-firm or client login
  can open) waits on his word; an Opal-internal page (staff-only, e.g. Portfolio Management, Security Analysis) does not. Unsure =
  client-facing; the push receipt names the pages changed and their class. Who may push where stays with
  `.tools/hooks/never-rules-gate.sh`. Order: `ANDREW_DIRECT_20261009_044xZ_*` (tier1 CTO).
- **Bloomberg pulls go only through their queue; other vendor APIs need no per-use word.** Per-user entitlement
  scoping waits for a second MCP user. Order: `ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_*` (tier0_exec).

**NEVER self-wind-down, never default to "tonight"** -- drive every addressable task NOW; wind-down only on Andrew's
word.

29. **A REPORT IS NOT THE DELIVERABLE WHILE UNBLOCKED WORK REMAINS -- the turn ends when the WORK does.** Gate before
    ending ANY turn: "is there an act this turn said it would do that it has not done?" -- yes + unblocked -> do it,
    report after. Ending on a report is correct only when the next act is blocked/gated/out-of-lane -- say which.
    `LD-0461`.

## Detailed Documentation

Deploy protocols `docs/deployment/` -- graph `docs/architecture/NFRA_GLOBGRPH_PRD.md` -- critical surfaces
`org/critical_paths/README.md` -- start guide `org/XXX.md` -- **Bloomberg, ANY scenario: READ
`integrations/bloomberg/READ_HERE.md` FIRST** (two-phase budgeted sign-in; a refusal names the SURFACE; derived layer
is current-day-only; never mint `data/bloomberg/`).

## Git

- **Working branch = the box's `box/<box>`; `CLOUD`'s ONE writer: integrator `0.0.0_AB_MSTR`**, via each
  box's scheduled `.tools/box-sync.sh`. Portal/opal_ai/mcportal: `DEV` trunk, `PROD` by `/prod-deploy`.
  `/integrate`. Shims reach shells via `~/bin` FORWARDERS (profiles never
  load): on WARN run `bash .tools/provision-path-shims.sh`. AWS via the `.tools/aws` shim (+`aws.cmd`, both or
  neither); never bare `MSYS_NO_PATHCONV=1 aws`.
- `MSYS_NO_PATHCONV=1` only for TF imports/ARN args and `git show <ref>:<path>` with a slashed ref; NEVER for `git
  push`/`safe-apply`. Never `2>/dev/null` a `git show` -- the mangle returns clean-empty; run a positive control beside
  any ABSENT verdict.
- Python/PS shelling to bash -> `.tools/git_bash_resolver.py`; Python spawning ANY MSYS binary ->
  `.tools/msys_argv_guard.py msys_safe_run()` -- never bare unix names in argv. Corruption oracle: echo the argument back.
- **Put the control on the RETRIEVAL:** print the denominator beside the number; paginated `list-*` auto-paginate then
  count client-side; name the QUESTION'S plane before the sweep's; authorship is not evidence.
- **A commit message is an EXECUTION VECTOR** -- `-F <file>` authored by a non-shell writer; `-m` deprecated for any
  body with special characters. `LD-0276`.
- **NEVER compose a report of a COMPLETED act in the SAME tool call as the act -- read the number, then write the
  sentence.** Does not bind the `safe-commit -F` message file. Verify a substantive send by `wc -c` on the delivered
  file.
- 31. **MESSAGE DISCIPLINE (Andrew-direct 2026-09-24): one ask per message, under 150 words, cite the file instead
  of restating it; the CTO is copied on DECISIONS only -- FYIs and corroborations go to the record, not to an inbox.
  A seat's record batches are hourly or per closed decision, never per message.**
- **An acked message never rides a later heartbeat/piggyback drain** (Andrew-direct 2026-09-24); unacked mail still
  replays. Mechanism: `org/mcp/server.py`, `0.0.0_AB_MSTR`'s lane -- DESIRED until landed there.
- **"Queued if not live" is a WISH, not a delivery. A BASE serial with no base session is a silent hole** -- an inbox
  is a per-recipient slice. Address a LIVE recipient, or PARK the item on its own carrier with an OWNER and the
  CONDITION that un-parks it.
- **A commit report states its PUSH STATE as a MEASURED value:** "on origin @hash (ls-remote read)" / "LOCAL @hash
  (ls-remote read)" / "push state UNREAD" -- never a default; re-measure at send time.

## Portal

- `portal/` -- `bun install && bun run dev --port 5174`; dev builds use port 5174 ONLY (Andrew-direct 2026-09-24);
  resolve bun via profile, don't bake a path.
- **Portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row; PROD only by
  a chosen-set promote** (NFRA_DEVPLN; `portal/CONTRIBUTING-BOXES.md`). Test-only needs no approver; a live FAST lease is
  its seat's approval (`open-calls.py approval-lease`); Opal-internal waits for the building box's CTO, client-facing for
  Andrew. Mechanism: `.tools/portal-hooks/pre-push` (fail-closed on DEV/PROD) and `never-rules-gate.sh`; VALGATE runs on
  every push. Order: `ANDREW_DIRECT_20261014_114xZ_*` (tier1 CTO).

## Changing this file

**A rule = imperative (<=2 lines) + mechanism + pointer.** RULES ONLY: no incident reports, no measurements, no dated
quotations, no "found by" -- the incident that taught a rule is not the rule; it goes to `docs/doctrine/CLAUDE_ANNEX.md`
(long-form) or `docs/references/` (what happened). A new verification rule STATES ITS COST AND NON-APPLICATION in one
line each or it does not land. **A law edit has THREE surfaces: commit + same-turn MCP broadcast to live seats + push
state stated in the broadcast.** Where the author is mechanically barred from broadcasting (the CVO, whose one send is
the slug), the broadcast surface is satisfied by RELAY: the author asks a seat permitted to broadcast, naming itself and
the commit; the relaying seat owes the broadcast same-turn and says it is a relay. **Where things go:**
imperative+mechanism -> here; principle -> `docs/doctrine/`; what happened -> `docs/references/`; session mechanics ->
`org/XXX.md`; decision -> `org/tier0/ledger/`. Never cut a MECHANISM to save space.
