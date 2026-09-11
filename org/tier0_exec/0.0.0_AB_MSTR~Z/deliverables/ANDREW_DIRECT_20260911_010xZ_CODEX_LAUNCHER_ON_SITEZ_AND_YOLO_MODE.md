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

## 4b. THE THIRD WORD, ~01:1xZ -- `ajb2` was not defined in a fresh window, and the fix is the PROFILE

Andrew ran `ajb2 3.0.0_SA_CVO~X` in a fresh PowerShell 5.1 window at `C:\Users\Opal Bloomberg` and got
`CommandNotFoundException`, then, verbatim at this terminal:

> **"ask mstr base if need be, this needs to be consistent across devices."**

**Cause, measured:** `ajb2` is a FUNCTION defined only by dot-sourcing `.tools\ajb2.ps1`. This device's
PowerShell 5.1 profile (`...\OneDrive - Opal Capital\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`,
device-local, 8.3 short paths by design) dot-sources `.tools\ajb.ps1` at its line 24-25 and had NO line
for `ajb2.ps1`. The repo launcher was never the problem.

**Act:** inserted, directly under the `ajb` line and in the SAME SHAPE, a `$ajb2 = '<short-path>\.tools\ajb2.ps1'`
+ `if (Test-Path $ajb2) { . $ajb2 } else { Write-Warning ... }` block with a comment naming this word.
Dot-sourcing `ajb2.ps1` at load defines the function and `$Global:Ajb2RepoRoot` and launches nothing
(every executable line sits inside `function ajb2 {` at :61 onward; scanned before wiring).

**Verified** by starting a fresh `powershell.exe` (profile loads) with the registry-composed PATH a new
window receives: `ajb2` = Function, `codex` resolves to `%APPDATA%\npm\codex.ps1`, root derives to the
workspace, a non-existent name does not resolve, exit 0.

**Consistency across devices:** asked `0.0.0_AB_MSTR` on the bus (MessageId ffdd224b-83e4-4ad2-bf99-a65d7db08430)
for the laptop profile's exact `ajb2` wiring and its codex PATH mechanism (bun shim vs persistent PATH);
site Z aligns to the laptop's text if it differs. The two profiles are device-local by design (different
user homes, one with a space), so "consistent" means same function name, same dot-source shape, same
guard -- with each device's own path. The profile is outside the repo, which is where a device path belongs.

**Not done:** no seat launched. A window opened BEFORE 01:0xZ lacks `%APPDATA%\npm` on its PATH and will
fail at the app-server start even after dot-sourcing; a NEW window has both.

**ALIGNED to the laptop's answer (bus c7def525-48ea-458b-8c9a-bc2db726ee9c, 01:18Z), ~01:2xZ:**
the laptop's block derives the path -- `$ajb2 = Join-Path (Split-Path -Parent $ajb) 'ajb2.ps1'` -- so a
moved clone means editing ONE line, not two. Site Z now carries that derivation line and the laptop's
four comment lines character-for-character; only the `$ajb` literal differs per device. Two deliberate
divergences, both decided rather than inherited: (1) the `else { Write-Warning ... }` guard is KEPT on
site Z and the laptop offered to add it there, so both devices carry it -- a silent skip is what made
tonight's fault read as a launcher fault; (2) site Z's block stays in `Microsoft.PowerShell_profile.ps1`
(CurrentUserCurrentHost), not the laptop's `profile.ps1` (AllHosts), because on this device the whole
toolkit -- the `$ajb` line the derivation depends on, the `kill` router, the bare-name wrappers -- lives
in CurrentHost and `profile.ps1` holds only the ps-lock guard; moving `ajb2` alone would split one
device's wiring and undefine `$ajb` for the derivation. Consistency at the level Andrew means -- same
function name, same derivation, same guard -- holds; the file follows each device's toolkit placement.
Re-verified in a fresh profile-loading shell after the alignment: `ajb2` Function, `$ajb2` derived and
present, `codex` resolves, negative control absent, exit 0. PATH mechanism confirmed the SAME SHAPE on
both devices: the package manager's global bin on the persistent USER PATH, no profile involvement.

**A live defect the laptop caught in the text this seat quoted (bus cdc3ec30-a6d7-4610-8a44-4cc03af83ba7,
01:22Z):** inside a PowerShell double-quoted string the backtick is the escape character, and `` `a `` is
the BEL escape, so the site-Z profile's ORIGINAL `ajb` else-branch -- `` "... -- `ajb` unavailable." `` --
had been emitting a malformed warning (a bell character in place of the name) since it was written, and
this seat had copied that form onto the `ajb2` line. Both lines on site Z now read plain ASCII with no
escapes, matching the laptop's text exactly. **Both arms EXERCISED after the edit, the laptop's shape:**
ARM 1, fresh profile-loading `powershell.exe` with the registry PATH -> silent, `ajb` Function, `ajb2`
Function, exit 0. ARM 2, the exact else-branch text against a non-existent file -> the warning FIRES,
well-formed, no BEL character, no stray backtick. The laptop landed its own `ajb2` guard the same way and
asked for the word to guard its still-silent `ajb` line; given, same reason. After that the two devices
carry the same guard and the same warning text on both launchers, with only the two path literals
differing.

**The general form, the laptop's and the keeper:** "make the two devices match" is not a goal in itself;
what must match is the BEHAVIOUR, and the file it lives in is a device fact.

## 4c. THE FIRST REAL LAUNCH FAILED AT :340, ~07:5xZ -- and the cause was the npm shim shape, not the launcher

Andrew ran `ajb2 3.0.0_SA_CVO~Z` in a fresh window. `-ShowLaunchInfo` resolved every path; the launch died
at `start-codex-seat.ps1:340`: `Start-Process : This command cannot be run due to the error: %1 is not a
valid Win32 application.`

**Cause:** the npm global install ships THREE shims side by side in `%APPDATA%\npm`: an extensionless POSIX
script `codex` (421 B), `codex.cmd` (341 B) and `codex.ps1` (869 B). `Get-Command codex` in PowerShell
picks `codex.ps1` (which is why every verification above passed), but the launcher's `Start-Process
-FilePath 'codex'` WITH `-RedirectStandardOutput/-RedirectStandardError` runs with UseShellExecute=false,
i.e. raw CreateProcess, which takes the exact-name file first and tries to execute the shell script as a
PE image. The laptop never hits this because its codex comes from **bun**, whose global install writes a
real `codex.exe` shim. Two verifications of mine had passed on the wrong instrument: `Get-Command` and
`& codex` resolve differently from `Start-Process`.

**Act, on his word "What is this bullshit" (the launcher must work) and "consistent across devices":**
`bun install -g @openai/codex@0.154.0` -- the laptop's mechanism at the version Andrew himself installed
here via npm (his npm install left in place) -- which created `%USERPROFILE%\.bun\bin\codex.exe` (15,872 B)
+ `codex.bunx`; then `.bun\bin` inserted on the USER PATH immediately AHEAD of `%APPDATA%\npm` so the bare
name resolves to the exe first. **Verified with the launcher's exact call shape** on the registry-composed
PATH: `Start-Process -FilePath 'codex' -ArgumentList '--version' -RedirectStandardOutput ...` -> exit 0,
stdout `codex-cli 0.154.0`; `codex app-server --help` -> exit 0; a non-existent name still fails. Andrew
relaunched in a new window: **`3.0.0_SA_CVO~Z` came up as a Codex seat** (app-server on ws://127.0.0.1:50167,
heartbeat registered LIVE PID 34844, bridge bound 08:03:01Z, detector 10668).

**Egress note:** one package install from the public npm registry via bun, pinned to the version already
on this device, under his explicit word that the launcher must work here and match the laptop. Reversible:
`bun remove -g @openai/codex` plus one PATH entry.

**The two devices now match on the codex mechanism too:** bun global exe shim on the persistent USER PATH
on both. The npm shims remain on site Z behind it; they resolve for bash users and harm nothing.

**CORRECTION 08:2xZ -- THERE IS NO VERSION SKEW, and every "0.153.4 vs 0.154.0" line above is stale.**
`0.0.0_AB_MSTR` re-measured the laptop (bus 91e9ee2a-133e-41f0-aa97-96ae802e4fd4): `Get-Command codex
-All` returns one shim, `.bun\bin\codex.exe`, codex-cli **0.154.0**; no npm codex on the laptop. Its
0.153.4 was true at ~00:3xZ and the laptop was upgraded at 02:22 local; the number was then re-asserted
hours later without a re-read, and this seat carried it forward twice more. Both devices: 0.154.0, bun
exe shim, identical mechanism. The "starts but never routes turns" watch-item is DROPPED as a skew
symptom; only the `default_permissions` key question (s.4) survives, and the first live seat answers it by
running. The laptop also tested ITS launcher with the launcher's actual `Start-Process -Redirect...` call
shape and it passes there: one shim, nothing for CreateProcess to pick wrongly. The night's recurring
shape, in the laptop's words: a check that is not the consumer's own call is a different question
answered truthfully.

## 5. RELAYED, NOT ADJUDICATED

Same-turn broadcast to the live site-Z seats (`1.0.0_SA_CTO~Z` as the launcher chain's steward on this
fabric) and a bus frame to `0.0.0_AB_MSTR`, whose fabric owns the launcher. Push state stated in the
broadcast, measured by `git ls-remote`.
