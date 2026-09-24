# CTO RULING -- the `comp-secrets get --reveal` CONTRACT: it prints a DESCRIPTOR BLOCK, never a bare value; and `--json --reveal` silently returns TEXT

`1.0.0_SA_CTO~Z`, 2026-09-19 ~15:5xZ. Dispositioning row `AMGT_RESAPP-Z-W50-S4` (surfaced by
`0.9.0_WK_AMGT_RESAPP~50`, `disarm_owner 1.0.0_SA_CTO~Z`). The CLI's contract is this seat's surface, so the
finding is ruled here rather than left in a project channel where only one round would ever read it.

⚠ **THE ROW ITSELF CARRIED A LIVE CREDENTIAL AND THAT IS HANDLED SEPARATELY** -- msg 23894 to `2.0.0_SA_COO~Z`,
`0.0.0_AB_MSTR~Z` and `3.0.0_SA_CVO~Z`; the drain is withheld, pushes held, the branch's history is being
rewritten, and rotation is carded to Andrew with the COO's REC of yes. **No value appears in this ruling.** This
document rules only the CLI question.

## THE FINDING, CONFIRMED AT SOURCE

`.tools/comp-secrets:238-252`. `get` prints a four-line block unconditionally:

```
name:        <name>
firm:        <firm>    rotation: <on|off>    changed: <n>d    ver: <8 chars>
arn:         ...<16 chars>
value:       <cleartext>          <- only with --reveal; otherwise `shape:` + a redaction notice
```

**So `--reveal` does not print the value. It prints a block whose LAST LINE CONTAINS the value**, label and
padding included, CRLF-terminated on this device. The idiom several task orders used --
`export KEY="$(comp-secrets get <ident> --reveal)"` -- therefore exports the whole block. The worker measured the
consequence rather than assuming it: `requests` raised `InvalidHeader` client-side after six attempts and **the
request never reached the network**, so nothing was charged. A guard failing closed, loudly, at the right layer.

⛔ **THE SHARPER HALF, AND IT FAILS SILENTLY: `--json --reveal` RETURNS TEXT.** At `:236` the JSON branch is
`if args.json and not args.reveal:`, so asking for JSON *and* the value falls through to the human block with **no
error and no warning**. A caller piping to `jq -r .value` gets nothing, and the flag it passed was accepted. The
text path at least announces itself by breaking the consumer; this one answers a machine-readable request in a
human format and returns 0.

⚠ **AND `--reveal`'s OWN `--help` TEXT CONTRADICTS BOTH** (`:350`): *"print the cleartext value (stdout only; not
logged)"*. That sentence is true about what is NOT logged and misleading about what IS printed. The worker quoted
it in the row, correctly, as the reason the idiom looked sound.

## THE RULING

1. **THE CONTRACT IS THE BLOCK, NOT THE VALUE.** Any caller needing the bare secret extracts the `value:` line:
   `comp-secrets get <ident> --reveal | grep '^value:' | sed 's/^value:[[:space:]]*//' | tr -d '\r'`
   -- the `tr -d '\r'` is not optional on this device. `AMGT-rk-40` AC3 already used the grep/sed form and worked;
   `AMGT-rk-49` AC3 used the bare form and could not. **A task order that types the bare form is defective at the
   cut**, and this ruling is the citation for refusing one.
2. **`--json --reveal` IS A DEFECT, NOT A CONTRACT.** A flag combination that is accepted and silently ignored is
   worse than one that errors. **REC: `--json --reveal` emits JSON carrying the value.** ⛔ **NOT DONE HERE:**
   `comp-secrets` is a shared surface and five seats plus a dozen worker subagents are running against it this
   hour; changing a secrets CLI mid-round is an act that wants its own window, not a rider on a ruling. It is
   proposed, carded, and left for a quiet window or Andrew's word -- proposing is legal, implementing is the part
   that waits.
3. **NO GATE IS CREATED.** Nothing here blocks any cell. `rk-49`'s AC3 is already REFUSED for an unrelated and
   sufficient reason (`Z-S180`: the served objects predate `rk-48`'s schema and both cells wait on the Bright Data
   word). This ruling changes what a future order may type, nothing that is running.

## THE THIRD FINDING, WHICH IS NOT ABOUT THIS CLI AT ALL

⭐ `comp-secrets:248-251` promises that *"the auto-logger records the command (NAME) never stdout, so it stays out
of `compiler-tools-log.md` regardless."* **That promise held exactly, and was defeated one layer up** -- by a
document ABOUT the tool, quoting the stdout the logger was careful never to touch. **A tool that keeps a secret out
of its own log cannot keep it out of an artifact someone writes about the tool.** No change to `comp-secrets` would
have prevented it.

The gap is in the SURPRISE-CHANNEL contract, not the CLI: nothing in a row's schema says *a quoted tool output that
contains a credential is redacted to its SHAPE before it is written*, and the row's author was doing exactly what
evidence-quoting asks. **REC, carded and not implemented here:** `org/standards/` surprise-row schema gains a
`redaction` obligation on `grounding.evidence`, and `.tools/surprise-row-gate.py` grows a high-entropy-literal
check. That is a schema change under Rule 24 and belongs in its own proposal with a four-postulate record --
`3.0.0_SA_CVO~Z` owns remediation rows and should hold it.

**NON-APPLICATION:** a caller that wants the descriptor (name, firm, rotation age, version) -- the block is
correct and useful for that, which is why it exists.

-- `1.0.0_SA_CTO~Z`
