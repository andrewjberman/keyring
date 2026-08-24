# ANDREW-DIRECT 2026-08-24 -- Tier-2 seats are instantiated Opus 5 / xhigh, BY DEFAULT

**Seat addressed:** `0.0.0_AB_MSTR` (base MSTR, laptop)
**Terminal:** base MSTR, ~19:5xZ
**Recorded by:** `0.0.0_AB_MSTR`
**Archetype of this record:** SCRIBE (+ IMPLEMENT -- the mechanism landed with it)

---

## VERBATIM

> "For future reference, tier2 agents should always be instantiated with opus 5 model on extra
> high effort."

---

## WHY THIS RECORD EXISTS AT ALL -- THE INSTRUCTION WAS LIVING NOWHERE

Measured before writing this, `comp-find -i 'extra high effort|xhigh'` over `org/` and `docs/`:
**19 hits across 16,046 files, and NOT ONE of them is this instruction.** All 19 are
code-review artifacts describing the `xhigh` *review* level -- a different subject that happens
to share the token.

So for the several hours between his sentence and this file, a standing "always" existed
**only in one session's context.** Six Tier-2 lanes were seated correctly during that window
because the operator remembered. That is not compliance; that is luck with good posture.
**A context-clear, a session end, or a successor MSTR loses it silently -- and every subsequent
spawn still looks completely normal**, because a model/effort choice leaves no scar when it is
wrong. There is no failing check, no error, no artifact that reads differently.

**"Always" is a property of the spawn path, not of an operator's memory.** That is the whole
finding, and it is why this landed as code in the same turn as the record.

## THE MECHANISM

`.tools/spawn-agent.ps1:44-61` -- a DERIVED DEFAULT on MSTR's own provisioning primitive.

```
$tierDefaulted = @()
if ($Serial -match '^0\.([0-9]+)\.0_' -and [int]$Matches[1] -gt 0) {
    if (-not $Model)  { $Model  = 'claude-opus-5'; ... }
    if (-not $Effort) { $Effort = 'xhigh';         ... }
}
```

**Tier predicate:** `0.Y.0` where `Y > 0`, per `org/ORG_CHART.md:13` (read from source, not
recalled). A `~lane` suffix is an instance marker, never a tier -- `0.4.0_DS_X~G` is Tier 2.

**EXERCISED, not reasoned about** -- all four tiers, with the negatives as controls:

| serial | tier | predicate |
|---|---|---|
| `0.4.0_DS_ClientPlatform~G` | 2 | True |
| `0.7.0_AE_CloudOps~G` | 2 | True |
| `0.1.0_DS_MarketIntelligence` | 2 | True |
| `0.0.0_AB_MSTR` | 0 | False |
| `1.0.0_SA_CTO` / `2.0.0_SA_COO` / `4.0.0_SA_CRO~C` | 1 | False |
| `0.6.2_AE_PartnerETL` | 3 | False |

Tier 3 is correctly excluded: he said *tier2*, and widening his word to "senior-ish seats"
would be the interpretation class this estate has paid for repeatedly.

## TWO PROPERTIES THAT ARE DELIBERATE

**1. IT IS A DEFAULT, NOT AN OVERRIDE, AND NOT A GATE.** An explicit `-Model`/`-Effort` always
wins; the block only fills an *unset* flag. Nothing is held, nobody approves anything, no spawn
is refused. Under the no-inferred-gates rule, mechanizing an explicit instruction is executing
it -- manufacturing an approval step around it would not be.

**2. IT ANNOUNCES ITSELF.** `Write-Host` names the serial, what was defaulted, and how to
override. **A silent default and a typed flag are byte-identical in the audit log**, so without
the line nobody can tell whether the tier rule fired or an operator happened to pass the flags
-- and a default nobody can see is one nobody can find when it is wrong.

That second property is borrowed, same night, from `0.0.0_AB_MSTR~Z`'s `comp-closure` finding:
*normalize per member AND state in the output which comparison was used*, because half one alone
swaps a visible wrong answer for an invisible one. **Same shape, one layer over.** Their anchor
is our own hand-typed `Z` on a local-rendering git format string, where a FALSE marker was worse
than a missing one because it made readers stop asking.

## SCOPE AND WHAT IS NOT CLAIMED

- Binds the **spawn path**, both fabrics -- `spawn-agent.ps1` is shared, so `0.0.0_AB_MSTR~Z`
  inherits it on the next integration. Told them directly rather than letting it arrive silently.
- Does **not** touch `ajb.ps1`'s `$modelBySerial` (which carries only `0.0.3_BG_BBGTerminal`).
  A second home for the same decision is the two-homes-diverged hazard; one home, one rule.
- Does **not** retro-fit anything. Seats already live keep the model they were started with.
- **Ledgered at LD-0447.** This bullet first read *"no ledger entry minted"* on my judgment that
  the decision content was Andrew's and the axes fit poorly. `mstr-ledger-check` refused the
  commit and was right: a strategic MSTR commit touching a non-record path is ledgered before it
  propagates. **The axis mismatch was real and was still not a reason to skip the record** -- two
  different claims, and I collapsed them. See LD-0447 for the correction in full.

## POSTSCRIPT -- I CORRUPTED THIS FILE WRITING THE PARAGRAPH ABOVE

The bullet above landed as *"the axes fit poorly.  refused the commit"* -- a sentence with no
subject. I edited it with `python -c "..."` and the replacement text contained
`` `mstr-ledger-check` `` in backticks. **A DOUBLE-QUOTED SHELL STRING EVALUATES BACKTICKS BEFORE
PYTHON EVER SEES THEM**, so the shell ran the tool name as a command, it was not on PATH, and the
empty stdout was spliced into the file. `bash: mstr-ledger-check: command not found` went to
stderr among the commit output.

**THE CONTROL IS IN THE SAME COMMAND.** `LD-0447.md` was written by a QUOTED heredoc (`<<'EOF'`)
in that same invocation and contains the identical backticked token **intact** -- 1 occurrence
there, 0 here. Same string, same second, two quoting contexts, opposite outcomes. That is what
makes this a mechanism finding rather than a typo.

**THE ESTATE ALREADY HAS THIS RULE AND I STILL DID IT.** CLAUDE.md F-010 states it for
`git commit -m`; the `/agentbus` skill generalizes it to the bus body with its own measured
instance. **It was never a git rule or a bus rule -- it is a SHELL-ARGUMENT rule, and
`python -c "..."` is simply a third surface.** My commit message in the very same command was
safe, because it went through `-F` with a quoted heredoc. I used the safe pattern for the
message, the unsafe one for the file, and the difference was not deliberate.

**WHY IT IS WORSE THAN A LOUD FAILURE:** the artifact stayed well-formed. A missing subject reads
as a typo, not as evidence a command executed inside a governance record -- and had the token
been a real command rather than an unrouted one, its *output* would have been spliced in instead
of nothing. **The visible damage is the least of the failure mode.**

Not proposing a gate for this: F-010's own note is that text-matching is correct only where `-F`
moves content out of the shell-parsed argument, and a general "no backticks in double quotes"
matcher would fire on every legitimate mention. The durable form is the habit -- **quoted heredoc
to a file, then read the file** -- which is what repaired this.
