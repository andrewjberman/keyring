# ANDREW-DIRECT 2026-09-11 ~01:0xZ -- the Codex launcher on site Z, and "yolo mode"

**archetype:** SCRIBE (record) + VALIDATE · **recorded by** `0.0.0_AB_MSTR~Z` · **terminals:** the laptop terminal (first word, relayed by `0.0.0_AB_MSTR` on the bus) and the `0.0.0_AB_MSTR~Z` terminal (second word, direct)

---

## 1. THE WORDS, VERBATIM AND COMPLETE

**At the laptop terminal ~00:3xZ**, relayed by `0.0.0_AB_MSTR` on the agentbus (MessageId
856d1a74-800a-47fa-8320-14e58c41cf67, 00:55:10Z), verbatim as relayed:

> **"need you to send the ajb2 launcher script details to MSTR~Z, we need that codex launcher on the
> sitez device"**

**At the `0.0.0_AB_MSTR~Z` terminal ~01:0xZ**, typed mid-turn, verbatim:

> **"yes we also need that yolo mode, which I believe the launcher accounts for natively but that
> would need to be clarified all the same"**

NOTHING IS PARAPHRASED AND NOTHING IS OMITTED. No other words on this subject at this terminal.

---

## 2. WHAT THEY SETTLE

| question | settled? | by which words |
|---|---|---|
| the Codex launcher must work on site Z | **YES** | "we need that codex launcher on the sitez device" |
| Codex seats here run in "yolo mode" (no approvals, no sandbox) | **YES** | "we also need that yolo mode" |
| whether the launcher already provides it | **A QUESTION, answered below from the script** | "would need to be clarified" |
| which serial to seat on site Z, and when | **NOT SETTLED** -- not asked, not inferred | -- |

---

## 3. THE LAUNCHER ON SITE Z -- MEASURED, AND THE ONE ACT

- Launcher chain at HEAD byte-identical to the laptop's (10 of 10 tracked; blob hashes matched:
  `.tools/ajb2.ps1` 0ff53ab1, `org/mcp/start-codex-seat.ps1` 37f06053). `ajb2 <serial> -ShowLaunchInfo`
  resolves every path correctly on this device.
- The `codex` binary was ALREADY INSTALLED HERE by Andrew tonight: `npm ls -g` = `@openai/codex@0.154.0`
  at `%APPDATA%\npm`; `~/.codex/auth.json` written 20:26 EDT; `config.toml` trusts the profile root,
  `[windows] sandbox = "unelevated"`.
- **Defect found:** `%APPDATA%\npm` was on neither the user nor the machine PATH, and the launcher
  starts the binary by bare name (`Start-Process -FilePath 'codex'` :340; `& codex` :461, :465).
- **Act:** appended `C:\Users\Opal Bloomberg\AppData\Roaming\npm` to the persistent USER PATH.
  Verified on the registry-composed PATH a fresh shell receives: `codex --version` = codex-cli 0.154.0;
  negative control does not resolve. Open terminals must be reopened.
- **Reported, not touched:** version skew, site Z 0.154.0 (npm) vs laptop 0.153.4 (bun).

---

## 4. "YOLO MODE" -- THE LAUNCHER ACCOUNTS FOR IT NATIVELY, AND HERE IS THE LINE

`org/mcp/start-codex-seat.ps1` @37f06053, lines 333-336, verbatim:

```powershell
$codexPermissionArgs = @(
    '-c', 'default_permissions=":danger-full-access"',
    '-c', 'approval_policy="never"'
)
```

Those two overrides are passed to **both** processes the launcher starts: the app-server
(`$appServerArgs = ($codexPermissionArgs + @('app-server', '--listen', $endpoint))`, :338-340) and the
foreground TUI (`& codex @codexPermissionArgs resume --remote ...` :461 and `& codex @codexPermissionArgs
--remote ...` :465).

`codex --help` on the installed 0.154.0 names the flag form of the same thing:
`--dangerously-bypass-approvals-and-sandbox` -- "Skip all confirmation prompts and execute commands
without sandboxing" -- and `-a never` -- "Never ask for user approval". The launcher sets the two
config keys behind that flag (`approval_policy="never"` = no approval prompts;
`default_permissions=":danger-full-access"` = the full-access permissions preset, i.e. no sandbox)
per invocation, so **no flag needs adding and nothing in the chain needs editing for yolo mode.**

**QUALIFIER, stated so it can be falsified:** a per-invocation `-c` override takes precedence over
`~/.codex/config.toml` for the keys it sets, and this device's `config.toml` carries
`[windows] sandbox = "unelevated"` (written during Andrew's own setup tonight). Two things are
**PROVEN ONLY BY A LAUNCH**, not by reading: (a) that `:danger-full-access` fully supersedes that
Windows-specific sandbox setting on 0.154.0; (b) that 0.154.0 honours the key name
`default_permissions` at all -- the installed package's README does not document it (grep over the
package dir: zero hits for `default_permissions` / `danger-full-access` / `approval_policy`), and the
binary's `--help` documents the same intent under `-s danger-full-access` and
`--dangerously-bypass-approvals-and-sandbox`. The launcher was exercised on the laptop at 0.153.4, so
the key is presumably live there; a one-patch skew is where a silently-ignored key would hide.
Discriminator at the first real seat: the seat runs a shell command with no approval prompt and no
sandbox denial in `.runtime/codex-seats/<serial>/app-server.stderr.log`. If it prompts or is denied,
the one-line remedy belongs to the launcher's steward (`1.0.0_SA_CTO`, laptop): add
`--dangerously-bypass-approvals-and-sandbox` (or `-s danger-full-access`) to `$codexPermissionArgs`.
This seat did not run that test: it would seat a Codex serial (Andrew's or the COO's call) and spend a
vendor call (per-use word rule).

---

## 5. RELAYED, NOT ADJUDICATED

Same-turn broadcast to the live site-Z seats (`1.0.0_SA_CTO~Z` as the launcher chain's steward on this
fabric) and a bus frame to `0.0.0_AB_MSTR`, whose fabric owns the launcher. Push state stated in the
broadcast, measured by `git ls-remote`.
