# MSTR session — cross-device MCP closed, device-portability class named and gated (0000–1415Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE, SCRIBE

## Window

2026-07-29 00:00Z → 14:15Z. Continues `logs/2026-07-28/session_close_missions_register_build.md`.
49 commits authored base-side this session (27 since 00:00Z). Second device (`0.0.0_AB_MSTR~Z`)
live throughout; 19 trunk envelopes from Z, 11 from base.

## What was done

### 1. Cross-device MCP — Andrew's goal, CLOSED both directions

Andrew: *"it is not complete until you and ~Z can send and receive messages to one another via mcp."*

**The entire blocker was one line: `.gitignore`'s `org/mcp/inbox/`, zero tracked files.** `server.py`
writes to `INBOX_DIR = Path(__file__).parent/"inbox"`; both sites share the same repo and that
subtree never travelled. **Not the broker, not the schema, not SQS.** A trunk, an envelope spec and
a 268-line Port-2 SQS proposal were all built to solve cross-device messaging while the existing MCP
transport sat one gitignore line from working — nobody had asked *why* it didn't cross before
deciding to replace it.

- `afa3ada086` (CTO) — level-by-level negation. **Zero code change to `server.py`.**
- `a2a3a00c59` (CTO) — `org/mcp/inbox/0.0.0_AB_MSTR/**` lane to both MSTR serials. `~Z` could write
  the reply but not commit it; the trunk works only because it *had* a lane and the inbox never did.
- `b395a2f839` — first delivery receipt committed.
- Z's `1e409244d7` — their MCP send; base's `check_inbox()` surfaced it.
- **Status: EXERCISED both directions.** Z confirmed `opal-agent-comms` bound post-restart;
  `register_agent`/`get_agent_status`/`check_inbox`/`heartbeat` all real tool calls.

**Self-cleaning by design:** only *undelivered* mail is tracked; `read/` stays ignored, so a message
drops out of git when read. Measured before landing: 0 unread vs 2,389 archived.

**Deletion-as-receipt ratified** (CTO, in the lane note): the receiver's deletion commit is
agent-side proof of consumption per Rule 22b. The fabric's first mechanical READ oracle — and it
fell out of a conflict `~Z` surfaced rather than worked around.

### 2. D-1 ratified, D-3 caught before it fired

`LD-0306` ratified (`eff96f5079`) on Andrew's word after he priced the latency I had not:
**git 4–15 min vs SQS 4.8 s measured.** My standing "don't ratify" recommendation was *true as a
statement and wrong as advice* — it silently priced real-time at zero.

**Then `~Z` sent a STOP**: PRD WS-3 still mandated the alarm the 07-28 moratorium bans, with **AC-5
requiring it be EXERCISED** — i.e. fire a live page at Andrew. PRD last touched 2026-07-17T15:34;
moratorium landed 2026-07-28T14:18. **My recording of the ratification is what made it live.**
CTO amended at `4e21f6a563` in ~8 minutes. AC-5′ is stronger than what it replaced: mutant-exercised,
so a sender that reports delivered despite a breach must FAIL.

### 3. Device portability — the class, and the gate

`.tools/verify-device.sh` (`153dd05c01`, 208 lines): **8 areas EXERCISED**, negative-controlled both
ways. Base reports PASS=11 FAIL=0 **UNVERIFIABLE=1**.

Fixes landed: launcher space-in-root + `OPAL_WS_ROOT` (`d11015b5bf`) · `.tools/aws` MZ-magic dispatch
(`6c836e0fdd`) · `~/bin` forwarder flavor bug (`8b61042af6`) · both-flavor reboot fallback ·
`fix-git-fstab` `noumount` removal + third verdict cell · `XXX.md` A.3 exercise line ·
`merge=union` (CTO `f989e47ee7`) · `.gitignore` `.tools/` blanket inverted (CTO).

### 4. Population + register

Killed/respawned `DS~A` + `AE~A` (wedged, work preserved out-of-repo first), respawned `AE~A` +
`DS` base on CTO's time-critical request. Mission register moved to **view-time compile**
(`LD-0341` A21) — the post-commit hook writes nothing tracked, which was blocking DT's pushes.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | routing for EC2 network posture | **FAIL (honest)** | "NO CURATED RULE" — catalog gap; rail-checked raw `aws` was correct |
| `comp-missions` | `emit` / `compile` ×4 | PASS | 1735 lines; view-time model |
| `comp-surface-check` | via `safe-commit` ×20 | PASS | no critical surface touched |
| `comp-pulse` | risk-reflex, every commit | PASS | denominators printed |
| `owned-paths-validate` | `--check-agent` ×6 | PASS | `~Z` auto-permit confirmed with controls |
| `verify-device.sh` | new; baseline + 2 negative controls | PASS | reproduces the site-Z failure `command -v` was blind to |

**What worked:** `comp-which` refusing to guess (score 0.38, "NO CURATED RULE") was more useful than
a confident wrong route. **What failed:** my first `owned-paths` harness returned DENY for all six
cases including a known-true positive control — a broken instrument I nearly used to refute a correct
correction. **Gap found:** no comp-tool covers EC2 network posture (VPC/SG/ALB); that question needed
raw `aws` and a `# rail-checked:` marker.

## Findings

1. **A write-time stand-in for a run-time fact** — 5 instances, 5 files, 4 authors. Both sites wrote
   it *into the detector built to find it*.
2. **A broad pathspec is the blast radius.** `safe-commit` stages with `git add -f`, overriding
   `.gitignore`: a directory pathspec swept **2,401** files; a *blocked* commit **leaves them staged**.
   Three distinct corruptions from one verb.
3. **A keyword detector cannot distinguish a specification from its prohibition.** Both sites
   false-positived on the same correct amendment, minutes apart.
4. **124 of 346 ledger files have unparseable YAML frontmatter** — invisible because
   `mstr-ledger-check` validates with awk, not a parser. 36% of the Tier-0 record. **Unrouted.**
5. **A ratification is not only a permission — it is an ACTIVATION of everything the gate was
   holding, including whatever went stale behind it.**
6. **`noumount` is valid to READ on a live mount and invalid to WRITE in fstab.** One bad option
   voids the whole line. **The flags you can read are not the flags you may write.**

## My errors this session (each caught, each by a control or a peer)

- Claimed `LD-0341` A20 had landed; it never reached a commit. **A pathspec is a request, not a receipt.**
- Claimed "there is no history to consult" for the override audit log — **false**; CVO found a
  17,172-line archive. I measured a *file's* age and inferred the *history's* age.
- Cited `owned-paths-validate.py:80-84` (home-folder fallback) as the whole rule; `~Z` correctly cited
  `:158-160`. My verification harness then returned an undiscriminating all-DENY.
- Wrote the XXX.md exercise probe against `comp-which --help` — rc tracks match/no-match, so a healthy
  tool reported dead. **A false FAIL in the line meant to replace a false PASS, same day.**
- Left `fix-git-fstab.ps1` telling the operator to expect flags it no longer writes — would have made
  a correct post-reboot result read as failure.
- Broke `~/bin/comp-which` on base running a positive control on the live forwarder instead of a copy.

## Blockers

None blocking me. Two items **AT ANDREW** (evidence-cited, not assumed):

- **fstab**: file on disk still carries `noumount`; rewriting needs elevation. `/c` will not survive
  a reboot. **LD-0340 OPEN.** Forwarders now fall back, so the absence is survivable, not fatal.
- **Wiring `verify-device.sh`** into a hook or startup rather than leaving it a command someone runs.

**AT CTO:** Port-2 SQS build (arch gate A.5) · the 124 unparseable ledger files · `terraform.exe`
still ignored, so site Z has no Terraform and does not know.

## Current state (zero-context)

`HEAD` on `CLOUD`, sync 0/0. Cross-device MCP live in both directions over git transport; the trunk
remains the **history tier** (a queue has nothing to re-read). `verify-device.sh` is the device gate:
`bash .tools/verify-device.sh`. Nine agents live; MDPF fires at 15:00/15:45/16:15/17:15Z are
**CTO/COO's, untouched by me**; deploy freeze holds to post-17:15Z. `portal` shows modified — DE
advanced DEV to `72f132c5`; the pointer bump is DT's promote authority, deliberately not swept.

## Next steps

1. **[Andrew]** Run `fix-git-fstab.ps1` elevated, reboot, check FLAGS not presence.
2. **[0.0.0_AB_MSTR~Z]** Run `verify-device.sh`, ACK `amb-b-0011` (deadline 18:00Z), continue the
   census (`org/tier0/audit/portability/` is the register of record).
3. **[1.0.0_SA_CTO]** Port-2 SQS build; the ledger-frontmatter sweep; the `terraform.exe` decision.
4. **[0.0.0_AB_MSTR]** Hold the `/loop`; do not touch MDPF.
