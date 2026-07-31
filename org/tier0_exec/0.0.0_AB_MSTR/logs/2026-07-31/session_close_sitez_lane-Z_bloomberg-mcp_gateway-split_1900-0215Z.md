# Site Z (~Z lane) session close — Bloomberg MCP, gateway split, RV-0058, startup law changes

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE, IMPLEMENT

**Agent:** `0.0.0_AB_MSTR~Z` (site Z / Opal Bloomberg box) · **Window:** 2026-07-30T19:00Z → 2026-07-31T02:15Z
**Commits:** 11 (mine) · **Spawned:** `0.7.0_AE_CloudOps~Z` · **Peer log:** its own `/log`, same window
*(No flat `org/tier0_exec/0.0.0_AB_MSTR~Z/` folder exists — base folder, lane in title, per the flat-vs-nested
finding this session landed in `XXX.md`.)*

---

## Current State

**Startup (all verified, not assumed).** Registered `0.0.0_AB_MSTR~Z` PID 20980. Inbox Monitor
`bzomdmqe7` and agentbus consumer `b4sqr53fv` both armed and confirmed `running` via `TaskOutput` —
the only probe that observes a *consumer*. Agentbus took over a stale lock (dead pid 1784) and
immediately received real mail, which is consumer-side transport proof independent of any ack. Repo
opened **9 commits behind**; pulled ff-only. `A.3` PATH: 93/95 resolve bare **and** the mandatory
exercise passed (a forwarder actually ran) — the check my predecessor built after the 07-29
"93 of 93 resolved, zero ran" incident.

**Bloomberg.** Terminal located at `C:\blp\Wintrv\wintrv.exe` (**not** `C:\blp\DSKTOP`), launched, and
the local DAPI exercised end-to-end: reference data, historical series, bulk fields. `.tools/bloomberg-mcp/`
was **untracked** — now committed (`f7bb8abd0`), first time in git.

**MEASURED, and it overturns the committed docs:** the DAPI serves with the **Terminal GUI exited and the
user logged out** — `wintrv` gone, Bloomberg processes 25 → 1, `bbcomm` (PID 21728) holding
`127.0.0.1:8194`, live data still ticking (USDCAD 1.4009 → 1.4011 across the logout). **The dependency is
`bbcomm`, not the GUI and not an interactive login.** `blp_client.py` and the README both asserted
"running and logged in"; corrected. **NOT established, deliberately untested** (Andrew: signing in is
cheap): cold boot with no login. `//blp/emsx` returns `False` — order/trade is not reachable from this
seat, so read-only has an entitlement floor under the design one.

**Gateway.** Server renamed `m365-gateway` → `opal-gateway`, deployed by CloudOps~Z and verified on the
live plane. This device's client key `m365` → `opal` (backed up, non-`mcpServers` content verified
unchanged; effective next session). `teams-assist` converted to **bare tool names** — the estate's only
live breakage surface, 2 lines, 1 file.

**Audit-archive.** `A.2` emits 11 findings every site-Z startup, all device-keying artifacts. **Fails
closed** — snapshot withheld, baseline not advanced — so site Z structurally cannot clobber the laptop's
4.8 MB tamper baseline. **⛔ Do not "repair" by re-baselining here; that is the one action that destroys
it.** Both agents on record not touching it.

---

## What landed

| Commit | What |
|---|---|
| `e7d4c119c` | **RV-0058** — CHANGES-REQUESTED, watermark HOLDS at 0056, no tag |
| `56d22bb03` | RV-0058 Amendment 1 — I asserted a dead seat that was alive |
| `e5ee29ee0` `fc540a479` `703b6fb3b` | Andrew-direct startup law: `/mstr-review` off at load, `/git-pull once` on |
| `f7bb8abd0` | Bloomberg MCP bulk/BDS serializer fix + first commit of the MCP |
| `91db036ae` `aa9845787` `b02e7be04` | `NFRA_BBGMCP` spec + two correction passes |
| `747dc955e` | `XXX.md` — tilde-lane paths: agent folders FLAT, inboxes NESTED |
| `18af8cb92` | `teams-assist` → bare tool names |

Full per-file detail: see commit messages.

**`/mstr-review` → RV-0058.** 700 commits, 18 serials, ~52.4h. Proxy acceptance disqualified twice
(LD-0339 is S3; 8 Tier-0 law-doc edits). **The READER GUARD's first live exercise, and it prevented a
write:** `get_live_agents` from site Z returns 1, all six Tier-1 read absent, and the unguarded path
prescribes `spawn-agent.ps1` — which would have duplicated `1.0.0` and `3.0.0`, both live on the laptop,
during a window where Andrew had barred spawning. Rendered `UNMEASURABLE`. F-004 (new): the guard's own
denominator was *inferred* from a transport artifact; closed with a derived `devices` accessor,
mutant-tested (adding a device to `queue_for` alone moves the count 2→3).

---

## Errors I made, and who caught them

A pre-GO record that carries only wins is not evidence.

1. **Asserted a dead seat that was alive** (`0.7.0_AE_CloudOps`). I took a relayed prose roster as fact
   and wrote it into a governance record — in the very review establishing that single-device liveness is
   `UNMEASURABLE`. I applied that discipline to the *instrument* and not to the *relay*. **Git was already
   holding three refuting commits from that serial and I did not look.** Caught by CTO. Guard extended to
   bind relayed liveness claims.
2. **Asserted a correlation as a root cause.** Wrote *"ROOT CAUSE, and it is ours"* into a commit for the
   deploy charmap crash, on a plausible non-ASCII correlation, never grounding the mechanism (Rule 22).
   Real cause: **pip's progress bar on the remote box** — `U+2501` ×40 at offset 429 — isolated by
   CloudOps~Z reproducing the stored SSM invocation and bypassing the failing CLI with boto3. My fix
   removed a real rule violation but **was never the mechanism.** I also introduced an `ERROR: WARN:`
   double prefix at `:106` by substituting a glyph without reading what `print_error` already emits.
3. **Overstated a blast radius to Andrew.** Reported Alyssa's daily tax workflow at risk from the rename
   off a count of 5 m365-tool refs in `tax-pt1`. Measured: **zero** `mcp__`-prefixed refs — bare names,
   untouched by a key change. Caught by CloudOps~Z verifying directly rather than trusting my reasoning.
4. **My key-vs-name proof had an unclosed alternative** — that `m365-gateway` truncates at the hyphen.
   CloudOps~Z killed it via hyphen survival (`opal-agent-comms` → `mcp__opal-agent-comms__*`).
5. **Routing error, mine:** I told CloudOps to ship the server rename as harmless. It **held**, correctly —
   Andrew's approval rested on a premise that had moved.

Also caught by my own controls: a `grep -c` false-PASS over an error message (`bcdedit`), a false `rc=0`
that read a pipeline tail rather than the gate, and three false negatives from ASCII-grepping a UTF-16 file.

---

## Findings that outlive this session

- **The client-visible MCP prefix is the registration KEY, not `FastMCP()`.** A prefix in a repo file
  encodes one device's local config into shared source. Bare names are correct in *both* key states, so
  they remove the ordering constraint rather than manage it. *Bare is a **uniqueness** judgement, not a
  style preference.*
- **A scanner pointed only at your own files cannot see the failure that arrives in someone else's output**
  (CloudOps~Z). The lint gate ships labelled authored-only *because* of this.
- **A successful deploy that fails its record-keeping leg is indistinguishable from a failed deploy at `rc`
  and from a clean one at the manifest — only the live plane separates them** (CloudOps~Z). A *missing*
  record invites a look; a **confident wrong one ends the inquiry.**
- **Tilde-lane paths use opposite forms in the two families** — agent folders FLAT (148 tracked files vs 1),
  inboxes NESTED. The inbox rule was phrased as a general principle; now scoped.
- **Merge commits inherit repo-default identity.** 6/6 merges today authored `0.0.0_AB_MSTR` (base, no `~Z`),
  14/14 content commits have committer = base. Since NEVER#7 mandates merge-pull on rejected pushes, every
  site-Z agent silently defeats the device-attribution the `~Z` suffix exists for. **Unfixed** — right
  altitude is `ajb.ps1` setting `GIT_AUTHOR_*`/`GIT_COMMITTER_*` from the serial. Andrew's word pending.
- **"Nobody is using this mcp" is empirically false.** Andrew 54,976 calls, Alyssa 895 across 29 tools,
  last today. ycharts credential **LIVE** — `ycharts_freshness` → `ok:true HTTP 200`, exercised on Andrew's
  explicit per-use word; the probe fetches real data and grades 403-expired vs seat-evicted separately.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which` (A.3 exercise) | PASS | forwarder *ran*, not merely resolved — the post-07-29 check |
| `comp-tool-hud` (advisory) | WARN | nudged a lambda search; raw calls carried `# rail-checked:` markers |
| `commit-gate.sh` | PASS | rc captured from the **gate**, not a pipeline tail (first attempt was a false PASS) |
| `comp-surface-check` (via safe-commit) | PASS | 1 file vs 6 surfaces, no critical surface touched |
| `comp-pulse` risk-reflex | CLEAN | measured, denominator printed (1 file vs 900 danger nodes) |
| owned-paths hook | **REFUSED ×2** | `docs/architecture/**` (ANY_CTO) and `infra/aws/ec2/**` (AE) — **both correct; no override taken** |
| F-010 commit gate | **REFUSED ×1** | `-m` carrying a backtick — switched to `-F`, correct |

**What worked:** the gates refused me three times and were right every time; declining the available
overrides kept two lanes' territory intact. **What failed:** `comp-iam`/`comp-estate` not used — no IAM or
estate-traversal work in my lane this window (CloudOps~Z carried the IAM side). **Gap found:** no comp-tool
models the MCP audit lake or MCP tool-name usage; both required rail-checked raw calls.

---

## Blockers

**None of mine.** Three items at Andrew, evidence-cited:

1. **[andrew]** SSM Agent MSI + hybrid activation — gate 4 closed and live-verified
   (activation `3d32065e-401f-453d-a2b9-34e4208c1864`), gate 2 is one elevated command. Activation *code*
   deliberately not printed to any transcript; `terraform output -raw activation_code`.
2. **[andrew]** Whether to spend a gateway restart proving `0198a978c` (pip fix) tonight. Recorded
   **GROUNDED-NOT-EXERCISED**. The one-character `tools.py` comment drift can ride the same deploy.
3. **[andrew]** Alyssa's client key `m365` → `opal`; and elevated `bcdedit /enum {current}` — `[d]` of the
   SentinelOne validation is **UNVERIFIED**, not clean (`Access is denied`; `BootupState = Normal boot`
   proves no safeboot flag at the 15:18:35 boot, not that the BCD is clean now).

---

## Next Steps

- **[0.7.0_AE_CloudOps~Z]** `/log` for the same window (tasked); then gate 2 on Andrew's MSI, and the
  caller-side SSM policy (second apply — `mi-*` does not exist until the box registers).
- **[0.7.0_AE_CloudOps~Z]** Follow-up **Deny** on `ssm:GetParameter`/`GetParameters` `Resource:"*"` — the
  managed policy grants account-wide Parameter Store read, unneeded for port-forwarding. Sequenced
  **after** proven registration, deliberately.
- **[1.0.0_SA_CTO]** RV-0057 F-001 device-keyed audit archive (STAGED). The reader guard it gates is
  **LIVE** (`b0b51cd47`) and exercised; the TO reads **unruled**, not blocked and not open.
- **[3.0.0_SA_CVO / andrew]** RV-0058 needs an acceptor with laptop-side audit access; proxy disqualified.
- **[0.0.0_AB_MSTR~Z]** Route three doctrine lines authored by CloudOps~Z: *the override exists for a gate
  that has SPOKEN, not one that is BROKEN*; *the hardening selected the failure*; *a scanner pointed only at
  your own files…*. Its authorship, not mine.
- **[andrew]** `NFRA_VELOCITY` GO issuance — this log and CloudOps~Z's are the gate.
