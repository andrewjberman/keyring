# The comp-rail as a DIRECTED gate -- mandatory where it matters, silent where it does not, and every denial hands over the command that answers

Fork of 4.0.0_SA_CRO, 2026-10-08 ~23:2xZ. READ-ONLY. For Andrew-direct ~23:0xZ, call 3: "if its not mandatory, then agents
dont do it ... it probably does have to be a gate but it needs to be articulated better/more directed."
Record: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_230xZ_RETIRE_41_TOOLS_YES_ROUTER_FIXES_YES_RAIL_STAYS_A_GATE_BUT_DIRECTED.md`.
Numbers come from `org/mcp/comp-which-rail.log` (laptop), last 30 days (since 2026-09-08), 60,836 rows; [READ] = counted,
[INFER] = reasoning. Rail: `.tools/hooks/comp-tool-hud.sh` (463 lines).

---

## 0. The finding that shapes the design

**Today most denials land on behaviour we WANT, or on shapes that are harmless.** 30 days, laptop, 4,565 DENY rows [READ]:

| What was denied | Rows | Share | What it really was |
|---|---|---|---|
| CENSUS-FILTERED where the command is **comp-find or comp-read** piped to head/tail | 773 of 1,097 | 17% | an agent USING the rail's own tool, then trimming its output |
| infra_grep (a grep naming infra/ or a .tf) | 507 | 11% | **0 of 507 recursive**: every one a single-file or named-path read |
| repo_search inside a linked worktree (`wk-*`) | 1,014 of 1,795 | 22% | a worker searching its own isolated copy |
| any denial whose command is compound (`&&` / `;` in its first 80 chars) | 3,582 | 78% | **every other segment of that call was aborted too** |

Plus 1,183 `# rail-checked` overrides in the same window [READ], with reasons such as "single-file context", "local dir
listing", "backend worktree" and "one page dir". And two live cases from this session: `comp-find --help | grep` was
denied as a census pipe (the HELP text), and a `.py` and a `.tf` grep aborted a compound call holding a revert. **The gate
is mandatory in the wrong places. That trains the override, and the override is what makes it optional in practice.**

## 1. What the gate exists to prevent (the four failure modes)

| # | Failure mode | Why it costs | Trigger shape (Bash) |
|---|---|---|---|
| F1 | **Blind recursive search of the repo** | 63,682 tracked files plus gitignored. Slow, unranked, no denominator; gitignored state is silently included or excluded | `grep -r/-R/rg/find/findstr /s` whose target is a directory (or none) inside a git checkout |
| F2 | **An absence concluded from a search that cannot see** | "0 hits" from a scoped or ignored corpus read as "does not exist" (CLAUDE.md rule 21 traps) | the same, AND the answer is used as a negative. Only a printed denominator prevents it, which is exactly what comp-find adds |
| F3 | **Raw AWS ENUMERATION the served graph already answers** | slow paginated `list-*`; the page count read as the total (rule 22a) | `aws <svc> list-*` / `describe-*` without an id, where the graph holds that node type |
| F4 | **A census denominator erased** | `comp-find ... \| head` can cut the line that says how much was searched | a census tool piped into head/tail/grep **when its denominator prints last** |

Everything else (reading a known file, listing a known folder, a live `get`/`simulate` for APPLIED evidence, searching
outside the repo) is not a failure mode, and the gate should not touch it.

## 2. The directed rule table

Every DENY prints three things: (1) **WHY**, in one line naming the failure mode; (2) **RUN NEXT**, the exact replacement,
pre-filled with the agent's own pattern and path; (3) **REMAINDER**, the rest of the call with the offending segment
removed (section 4).

| Rule | Trigger | Verdict | RUN NEXT (pre-filled) |
|---|---|---|---|
| R1 | recursive grep/rg/findstr on a directory in the SHARED checkout | DENY (F1/F2) | `comp-find '<pattern>' <dirs>` (`--files` when the agent used `-l`; `-i` kept) |
| R2 | `find <dir> -name/-iname <glob>` in the shared checkout | DENY (F1) | `comp-find --name '<glob>' <dir>` |
| R3 | recursive search inside a LINKED WORKTREE (`git worktree list` path) | DENY (F1) | `cd <worktree> && comp-find '<pattern>' <dirs>` as its own call |
| R4 | recursive grep over `infra/aws/terraform` asking which resource or module names something | DENY (F1) | `comp-find '<pattern>' infra/aws/terraform` (+ `comp-estate --resource '<pattern>'` as the graph-aware second line) |
| R5 | `aws iam list-roles/list-policies/list-users`, `aws lambda list-functions`, `aws s3api list-buckets` (an enumeration the graph holds) | DENY (F3) | `comp-kuzu "MATCH (n:CloudNode) WHERE n.node_type = '<TYPE>' RETURN n.name"` (or `comp-find --corpus aws '<pattern>' <TYPE>`) |
| R6 | comp-find / comp-read / another census piped to head/tail/grep, denominator printed last | DENY (F4), **interim only** | the same command with `--limit N` / `--page` / `--band` (head -N -> `--limit N`) |
| R6' | the same, once the tool prints its denominator FIRST | ALLOW | -- (the denominator cannot be cut by head; see build step 3) |

**Pass list (ALLOW, logged with a shape, never denied):**
- single-file grep or sed anywhere, **infra and .tf included** (507 false denials go away);
- `ls`, `git -C`, `cat` or `head` of a named file, and a named-folder listing;
- a pipe receiver (`cmd | grep`);
- any path OUTSIDE a git checkout: scratchpad, AppData, `/tmp` that is not a worktree, `~`;
- live AWS `get-*`, `simulate-principal-policy` and `describe-*` with an id. These are APPLIED-plane evidence (rule 22a)
  and the served graph cannot stand in for them;
- `comp-* --help`;
- native Grep, Glob and Read (unchanged).
**Escape:** `# rail-checked: <why>` stays, audited. Its target rate drops sharply once the pass list stops the false
denials.

## 3. Worked examples (real denials, 30-day log)

1. **infra single-file read.**
   - Before: `grep -n role infra/aws/terraform/x.tf` -> DENY infra_grep ("comp-tool on the HUD: grepping infra/.tf ...
     GATED per Rule 21").
   - After: ALLOW, logged `shape=single-file`. Nothing to route: the agent named the file.
2. **comp-find trimmed with tail.**
   - Before: `comp-find --name 'BUCKETLESS*' --limit 6 2>&1 | tail` -> DENY CENSUS-FILTERED.
   - After (interim R6): `WHY: tail can cut comp-find's denominator line. RUN NEXT: comp-find --name 'BUCKETLESS*' --limit 6`.
   - After build step 3 (R6'): ALLOW.
3. **Recursive Terraform search.**
   - Before: `grep -rn -l -E "inf-ec2-launch-monitor|inf-ec2-retry-launch|inf-otp-alert" infra/aws/terraform/ ...` ->
     generic DENY.
   - After (R4):
     `WHY: recursive search of infra/aws/terraform (F1). RUN NEXT: comp-find --files 'inf-ec2-launch-monitor|inf-ec2-retry-launch|inf-otp-alert' infra/aws/terraform/`.
3b. **comp-find's own help.**
   - Before (this session): `comp-find --help | grep -E -- '--(files|...)'` -> DENY CENSUS-FILTERED, and the whole call was
     aborted.
   - After: ALLOW (`comp-* --help` is on the pass list).
4. **Compound call aborted by one segment.**
   - Before: `cd <ws>; git checkout -- <file>; grep -n ... infra/aws/globgrph/*.py` -> DENY. The revert did not run, and
     nothing said so.
   - After:
     `WHY: segment 3 is a multi-file grep (F1). NOTHING IN THIS CALL RAN. REMAINDER: cd <ws>; git checkout -- <file>. RUN NEXT: comp-find '<pattern>' infra/aws/globgrph`.
5. **IAM enumeration.**
   - Before: `aws iam list-users --query "Users[].UserName"` -> DENY aws_iam_inspect.
   - After (R5):
     `WHY: an IAM enumeration the served graph holds (F3). RUN NEXT: comp-find --corpus aws '' IAM_USER (or comp-kuzu "MATCH (n:CloudNode) WHERE n.node_type = 'IAM_USER' RETURN n.name")`.
     A live `aws iam get-user --user-name X` is ALLOWED: that is APPLIED evidence.

## 4. The compound-call fix

A PreToolUse deny is all-or-nothing for the call, and the hook cannot run part of it. So the deny text itself carries the
recovery:
- **`NOTHING IN THIS CALL RAN`** as its first words. The agent never assumes the other segments ran; today the revert case
  shows it did assume that.
- **`REMAINDER:`** the call re-joined without the offending segment, ready to run as is.
- **`RUN NEXT:`** the replacement for that segment.
The hook already splits segments (`_search_seg`, comp-tool-hud.sh:151-199), so the remainder is that list minus one. Rule
16's warning (a denial aborts the whole call) moves from a law line agents must remember into the denial they read.

## 5. Measuring it, so we know it works

Today a DENY row carries no serial, and a route row carries a `route_id` but no serial (comp-which:1780) [READ]. Add:
1. `serial=` (from `$OPAL_AGENT_SERIAL` or the session serial file) and `deny_id=` on every DENY and ALLOW-SEARCH row.
2. The deny prints `deny_id`. comp-find and comp-read log `src=deny:<deny_id>` when their argv equals the RUN NEXT line
   (the hook writes the expected argv to a small state file keyed by `deny_id`; the tool compares on start).
3. Weekly figures, from the log alone:
   - **follow rate**: RUN NEXT executed within 10 minutes;
   - **override rate per rule**;
   - **false-deny rate**: overrides whose reason names a pass-list shape;
   - **denials per 100 searches**.
   Targets go to Andrew with the first week's numbers, not before.

## 6. Where the articulation lives

| Place | What it says | Owner / gate |
|---|---|---|
| The denial text (comp-tool-hud.sh) | WHY + RUN NEXT + REMAINDER, per rule. This is the main carrier: agents read it at the exact moment it matters | the rail's owner (NFRA_COMPRAIL; `.tools/hooks/` lane) |
| CLAUDE.md rule 21 | the four failure modes, the pass list in one line, and "a denial hands you the command: run it" | law-locked: Andrew's order, `ANDREW_LAW_EDIT_ORDER` |
| Seat prompts (Codex especially) | "a known path needs no router; search with comp-find; read the denial's RUN NEXT" | each seat's owner |

**Draft rule 21 (for Andrew; replaces the "comp-which is the reflex" lines):**
> **21. Search the repo with comp-find, never blind recursive grep; read AWS through the served graph before you list
> it.** The rail DENIES four things: a recursive repo search, a `find -name` over the repo, an AWS enumeration the graph
> holds, and a census output cut before its denominator. Every denial prints the command that answers: run it next. A
> denial runs NOTHING in its call; its REMAINDER line is the rest of your call. Free: one named file, a named folder, a
> pipe receiver, any path outside a checkout, a live AWS get/simulate, native Grep/Glob/Read. comp-which is for when you
> do not know the tool. Mechanism: `.tools/hooks/comp-tool-hud.sh`.

## 7. Build steps, in order

1. **Pass list and R1-R5 replacement text** in comp-tool-hud.sh. Pattern and path extraction already exist (`_search_seg`).
   Add the REMAINDER/RUN NEXT block. Re-run `.tools/comprail-gate1-fptest.sh`, plus new cases for the 5 examples above.
2. **serial and deny_id on rows**; the `src=deny:<id>` match in comp-find and comp-read.
3. **Denominator-first output in comp-find and comp-read** (the summary line at the top as well as the bottom). Then R6
   becomes R6' and 773 denials a month disappear.
4. **Rule 21 law edit** on Andrew's order, with the commit + broadcast + push-state triple.
5. **Seat prompt lines.**
6. **Two weeks later:** the section 5 figures to Andrew, measured against COMPRAIL AC5.

## Not read

- Site Z, dell1 and dell2 rail logs. The figures are the laptop's only; site Z's archive shows the same classes
  (router review).
- The full bodies of comp-tool-hud.sh lines 220-463 (the aws tiers) beyond their messages and class names.
- How a PreToolUse hook could rewrite a command instead of denying it (not checked; this design assumes deny-with-text).
- Whether `IAM_USER` is a node type in the served graph (the census lists IAM_ROLE and IAM_POLICY). Example 5's RUN NEXT
  must be checked against `comp-kuzu --schema` when built.
