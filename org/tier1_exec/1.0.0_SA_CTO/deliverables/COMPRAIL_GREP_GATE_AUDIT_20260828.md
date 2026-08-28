# The raw-grep gate, measured -- and the proposal to close it (2026-08-28, 1.0.0_SA_CTO~D)

**Andrew-direct (this terminal, 2026-08-28 ~17:5xZ, VERBATIM):** *"your task is going to be checking the
gating functions on raw grep and we need to figure out how to narrow it even harder or just block it
entirely and replace with a comp-grep function (which may already exist) that is properly scoped, i am
very tired of grep."*

Everything below was EXERCISED against the live hook (`.tools/hooks/comp-tool-hud.sh` @ working tree,
`org/mcp/comprail-gate1.enforce` PRESENT since 57c86bd4bf 2026-06-26) by feeding it the exact PreToolUse
JSON the harness sends, and READ from `org/mcp/comp-which-rail.log` (41,661 rows). No number here is
inferred from a comment.

## 1. What the gate is, mechanically

ONE hook gates Bash search: `comp-tool-hud.sh` (PreToolUse, matcher `Bash|Grep|Glob`).
`never-rules-gate.sh` has NO grep limb (its 26 `grep` lines are its own internal greps). The hook:

1. stands down under a live `/freeform` marker;
2. if the command's LEADING verb is operational (`cd echo export ls python git bash ...`), EXITS unless a
   later `&&`/`;`/`|` segment starts with a **grep-family** word (`grep rg egrep fgrep findstr ack ag find`);
3. classifies by regex into ~15 advisory classes (aws_iam_inspect, infra_grep, s3_artifact, portal, ...);
   an unclassified search falls to `comp_which`;
4. DENIES (`permissionDecision: deny`) only for: the four raw-aws-INSPECTION classes, `infra_grep`
   (needs the literal `infra/aws/` or `.tf` in the command), and Gate-1 = class `comp_which` AND
   `grep -r|rg|find` AND an ESTATE path (`data/*/scripts | portal/src | infra/aws | .tf`) AND **no `|`
   anywhere in the command**;
5. everything else is an `additionalContext` NUDGE (throttled) or SILENCE. **A silent allow writes no
   log line anywhere**, and `agent_telemetry/*.jsonl` does not carry the command -- so the escape rate
   has NO denominator. That is finding #0.

## 2. Exercised: what passes today (SILENT = no deny, no nudge)

| Command shape | Result | Why |
|---|---|---|
| `grep -rn foo .` (the whole repo) | **SILENT** | `.` is not an "estate path" |
| `grep -rn foo org/` / `docs/` / `daily_reports/` | **SILENT** | non-estate path |
| `grep -rln foo .` | **SILENT** | same |
| `grep -rn TENANT infra/` | **SILENT** | infra_grep needs `infra/aws/` or `.tf`; `infra/` alone escapes |
| `find org -name *.md` | **SILENT** | non-estate path |
| `grep -rn foo org/ \| head` | **SILENT** | any `\|` anywhere disarms Gate-1 |
| `cd /x && grep -rn foo org/` | **SILENT** | lead-verb exemption + non-estate path |
| `ls org/ && grep -rn foo docs/` | **SILENT** | same |
| `cd /x && aws iam get-role ...` | **SILENT** | lead verb `cd`; the re-check looks ONLY for grep-family, never for aws |
| `echo ===; aws lambda get-policy ...` | **SILENT** | same hole -- **this is the CLAUDE.md 2026-08-28 "raw-aws INSPECTION DID NOT FIRE for 2 seats on 2 command shapes"** |
| `export X=y; aws iam list-attached-role-policies ...` | **SILENT** | same |
| `grep -rn foo data/black_diamond/scripts/gold/` | NUDGE | the s3_artifact class shadows Gate-1 (documented at :222-227 as a "deferred call") |
| `grep -rn foo portal/src` | DENY | estate path, no pipe |
| `grep -rn foo infra/aws/` / `grep -n foo .../alb.tf` | DENY | infra_grep |
| `find . -name *.tf` | DENY | `.tf` matched |
| `aws iam get-role ...` (bare lead) | DENY | aws_iam_inspect |
| `ps -ef \| grep x` | SILENT (correct) | pipe-receiver grep is post-processing, not search |
| `... # rail-checked: <why>` | ALLOW + audited | the sanctioned override |

Read the table as a whole: **the wall stands only where the command already says `infra/aws`, `.tf`,
`portal/src` or a bare `aws <inspect>` -- the broadest possible search (`grep -rn foo .`) and every
compound command walk straight through.** The gate is precise about the narrow thing and blind to the
wide one, which is the inverse of a rail.

Rail-log census since 2026-08-01 (DENY / RUN-OVERRIDE): infra_grep 145/33, aws_freshness 41/38,
aws_iam_inspect 24/26, aws_deploy_verify 9/1, aws_route 7/3, comp_which **4**/0. Gate-1 -- the "broad
repo grep" limb -- has fired FOUR times in four weeks. The denominator of broad greps it did not see is
unrecorded (finding #0), but the probe table says why: almost none of them match its path list.

## 3. The replacement already exists, and it is comp-find, not comp-grep

- `.tools/comp-find` (22 KB): graded content + `--name` filename search, `.gitignore`-bounded corpus with a
  PRINTED denominator, bands (HEAD/DEF/SURFACED/CONFIG/TEST/DOC/COLD), paging, `--corpus`, `--hidden`,
  and the SYSTEMS-CONTEXT block per hit. `comp-which` routes to it; its own help says it "replaces comp-grep".
- `.tools/comp-grep` (9.7 KB): the 2026-06-18 original; still resolves (`~/bin/comp-grep`), still used
  (824 runs since 08-01 vs 2,696 comp-find) but nothing routes to it since the 2026-08-07 repoint.
- Both are Python over `git ls-files` + in-process `re` (rg is absent on this box; a python->bash grep
  subprocess can silently return empty on Windows). Both log every run to the rail log.

So the "properly scoped comp-grep" Andrew asked for is **comp-find**; the only work is making the gate
send people there, and retiring the comp-grep name to a forwarder so two names stop competing.

## 4. Proposal -- BLOCK, not narrow (recommended)

"Narrowing harder" means growing the estate-path list, and every path it does not name is a new hole
(the `infra/` vs `infra/aws/` escape is that failure mode already). The clean rule is the one the PRD
§3 table wrote in June and the hook never implemented:

**T1 (recommended now) -- every standalone repo search in Bash is DENIED, routed to comp-find.**
- Evaluate EVERY segment of the command (split on `&&`, `;`, `||`, newline), not just the leading verb.
  A segment whose leading token is `grep|rg|egrep|fgrep|findstr|ack|ag|find` with a path argument (a
  directory, `.`, a glob, or `-r/-R`) = a repo search -> DENY, regardless of path, regardless of what
  came before it, regardless of a `|` elsewhere in the command.
- Pipe-RECEIVER grep (`cmd | grep`) stays free (post-processing, PRD §3).
- The same per-segment evaluation fixes the aws-inspection hole for free: `cd X && aws iam get-role`
  is denied because the `aws iam get-role` SEGMENT is.
- `# rail-checked: <why>` and `/freeform` keep working unchanged (shared deny path).
- Deny reason names the exact replacement: `comp-find '<pattern>' <path>` / `comp-find --name '<glob>'`
  / `comp-which "<question>"`. Never a dead end.
- **Log every ALLOW of a search-shaped segment** (`ALLOW-SEARCH  tool=Bash  shape=<pipe-receiver|single-file|...>`)
  so the escape rate has a denominator from day one.

**T2 (Andrew's call) -- single-file greps too.** `grep -n foo path/file.py` is today exempt (:98). comp-find
handles one file (`comp-find foo path/file.py`) and prints the denominator; the cost is that `grep -q` /
`grep -c` predicates INSIDE scripted Bash (an `if grep -q ...; then`) would need `# rail-checked`. I would
ship T1 first and read the ALLOW-SEARCH log for a week before deciding T2.

**Native `Grep`/`Glob` tools -- also Andrew's call.** The 06-22 refinement ("native escape is fine") made them
nudge-only. If "tired of grep" includes the native tool, that flips to deny with the same reason; I have not
assumed it.

**Retire the name:** `.tools/comp-grep` becomes a 3-line forwarder to `comp-find` (same args, one WARN line),
so the 824 habitual runs land on the graded tool without breaking anyone.

## 5. Cost and non-application (the clause CLAUDE.md requires of a new verification rule)

- Cost per Bash call: unchanged in kind (the hook already regex-classifies every Bash command); the
  per-segment split adds a `tr`/`sed` pass measured in milliseconds.
- Does NOT apply to: pipe-receiver grep; `/freeform` sessions; `# rail-checked` overrides; the native
  Read tool; any non-search Bash. T2/native are explicitly NOT in T1.
- Fix the hook's own record while in there: its comment cites the FP test at `.tools/hooks/comprail-gate1-fptest.sh`;
  the file is at `.tools/comprail-gate1-fptest.sh`. The FP test is extended with the 14 shapes in §2 (both
  arms each) BEFORE the gate change lands, so the gate is measured by a test that was red first.
- Three surfaces for the law edit (CLAUDE.md Rule 21 text, the hook, the FP test) + the same-turn broadcast
  the law requires. Andrew has this seat off the fabric channel this session -- the broadcast is the one
  step I would need his word on, or MSTR relays it at the integration window.

## 6. Decision needed

(a) T1 as written -- go/no-go. (b) T2 single-file greps -- now / after a week of ALLOW-SEARCH data / never.
(c) Native Grep/Glob -- keep nudge-only (06-22 ruling) or flip to deny.
