# NFRA_MCPORTAL task order -- `MP-pc-4` -- WORKSTREAM PC ROUND 1: READ where Claude Code exposes the signed-in account and the 5-hour and weekly limits (FWD-22, U1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pc-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pc-4</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~23</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time read; nothing scheduled, and no alert or monitor is built (standing moratorium).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the check's credential-shape limb is the adversary arm on the one file this cell writes.
EGRESS CLASS, declared: none. Local files and local commands on this box only; no network call.
</preflight>

## 1. THE CELL -- `MP-pc-4` (workstream PC round 1, decomposition section PC.1)

Your worktree is `C:/tmp/mp-pc-23` (branch `wk-NFRA_MCPORTAL-pc-23`). Work and commit only there.

Andrew asked (2026-10-13, verbatim): "i want the mcp.opalinvest.dev/control-plane function to include the logged in
account + usage remaining on 5hr and weekly basis by box". PRD v0.8 FWD-22 needs, per box and per Claude Code login:
- the account's email, plan and organization, from the box's OWN login record, never a token;
- how much of the 5-hour limit and of the weekly limit remains, each with its reset time.

Every figure carries a claim: measured, or absent with its reason, never a guess. Before anything is built, this cell
answers ONE question: **WHERE are those figures exposed, and can a box read them without exposing a credential?** You
build nothing.

Investigate, on this box (site Z), at least these candidate sources. Add any others you find.
1. **Claude Code's local account record.** The user's Claude config (for example `~/.claude.json`, and the `~/.claude/`
   directory). Look for an account object (email, organization, plan or billing type). Print KEY NAMES, and print only
   these non-secret fields' values: email, organization name, plan or billing type. Never open a credentials file's
   values (for example `~/.claude/.credentials.json`): list its key names only.
2. **Claude Code's own commands.** `claude --help` and the help of any subcommand that looks relevant (status, usage,
   account, config). Run non-interactive forms only, under `timeout 20`. Note which interactive slash commands (for
   example `/status`, `/usage`) the help or docs name, and what they show. You cannot type a slash command, so record
   that limit as a claim, not as a guess about the output.
3. **The status line.** Claude Code passes a JSON object to a configured status-line command. Find whether that object
   carries account or rate-limit fields: read the installed Claude Code package's own files under its install directory
   (find it from `command -v claude` or `where claude`). Record the field names and the file and line where you saw them.
4. **The API's rate-limit headers.** Whether the 5-hour and weekly limits appear as response headers on the Anthropic
   API (for example names beginning `anthropic-ratelimit-unified-`). Read only what the installed package's own code
   or docs say. Make no network call.
5. **Anything already in this repository** that reads or records Claude Code usage or account, through
   `comp-find -i 'ratelimit|rate_limit|usage|oauthAccount' --files --limit 30`. Read each hit; do not stop at the first.

For each source record: what it exposes (`account`, `limit_5h`, `limit_weekly`, as many as apply), how a box would read
it, whether you MEASURED it on this box, its claim (`measured` = you saw the field with a real value on this box;
`inferred` = the package or docs say it exists but you did not see a value; `absent` = it does not expose it), and the
reason. The other three boxes (laptop, dell1, dell2) are not reachable from this cell: say so for each figure.

Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~23/U1_CLAUDE_ACCOUNT_AND_LIMITS_SOURCES.md`
with:
- a short prose finding: the best source for each of the three figures, and what a build cell would read;
- ONE ```json block, exactly this shape:
  `{"sources": [{"source": "<name>", "exposes": ["account" | "limit_5h" | "limit_weekly", ...], "how_read": "<text>", "box_measured": "sitez" | "none", "claim": "measured" | "inferred" | "absent", "reason": "<text>" | null}, ...]}`.
  Each of the three figures appears in at least one source's `exposes`. If no source exposes one of them, list it on a
  source row with claim "absent" and say why.

**NEVER write a credential value anywhere:** no token, key, cookie or session value in the file, in a commit, in a row
or in your report. If you see one, write "[redacted]". The check refuses the file on a credential-shaped string.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Read local files and run local `--help` and status commands only. No
   network call, no login, no logout, no config change, and no change to any `~/.claude*` file.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~23/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: your user's Claude Code config and install directory (key names and the three non-secret values only),
this repository, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W23-S<k>` (the next free k for W23). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pc-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/pc4.AC1.sh; echo "exit=$?"</invocation><expect>json_blocks=1; bad_rows=0; covered=account,limit_5h,limit_weekly; credential-shaped hits=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pc-4" judgment="true"/>
</proof_of_spec>

AC2 is a JUDGMENT criterion, graded by `3.0.0_SA_CVO~Z` at L9: does the finding name, for each of the three figures, a
source a build cell can read on every box without a credential, or say plainly that none exists? Record it in your
instance under `UNVERIFIABLE-BY-INSTRUMENT`, with `status_reason` naming the CVO. Give it no PASS or FAIL.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~23/NFRA_MCPORTAL.TO-MP-pc-4.claude-limits-sources-read.proof_of_spec.json`.
Report once, with:
- the check output;
- the commit hash;
- your one-paragraph finding;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC issuance (decomposition v9) from PRD v0.8 FWD-22 ("The first cell is a READ of where
Claude Code or the account exposes the limits, before anything is built") and the C17 round-2 analysis @d0dd3f0964 (U1).
Check dry-run at base 9be88c9134: AC1 FAIL (file absent). The checker was fed before the cut: a planted well-formed file
reads PASS, and the same file with one planted token-shaped field reads FAIL (credential-shaped hits=1). LOCAL, with no
build. The judgment criterion is here because the outcome is a reading: does the finding name a readable source?

<status>complete</status>
<round>1</round>
<workstream>PC</workstream>
<slot>~23</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
