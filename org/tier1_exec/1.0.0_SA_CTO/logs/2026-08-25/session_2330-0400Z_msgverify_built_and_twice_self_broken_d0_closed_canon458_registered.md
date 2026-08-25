# 1.0.0_SA_CTO -- session 2026-08-24 23:30Z -> 2026-08-25 04:00Z: Andrew's two routed builds landed and one of them broke twice in my own hands; D0 gates CLOSED; COT_CANON458 registered on his 458M word; six method/spec/doctrine rulings; the Cottonwood finding classified, corrected, and re-classified

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE

Continues `session_2035-2330Z_rulings_recert_gates_earned_their_keep_own_false_hashes.md` (@b643cd714d).

## 1. Andrew-direct builds routed to this seat, both landed
- **safe-commit MESSAGE SELF-VERIFY** (his ~23:5xZ word at the COO terminal, *"seems to me like the 'checker' should
  have that built in"*). Built @75d84742e8: after every commit the wrapper compares the message of its own new hash
  against the `-F` file, both sides through git's own cleanup transform (measured in a probe repo), MATCH prints
  hash+subject+len, MISMATCH exits 3 naming the first differing byte. Comparator is a standalone file
  (`.tools/safe_commit_msg_verify.py`) after the embedded-heredoc form mangled through three quoting layers.
- **GATE-3 TOKEN ATTRIBUTION** @7ea1502a0d, on COO's false-positive report: the F-010 matcher is UNCHANGED by ruling
  (its own in-file record shows the per-command "fix" executed a real commit message on 07-13; annoying-vs-executes-
  code chooses annoying), and the deny now NAMES line:text per co-occurring token. Exercised 3 ways at the live hook.
  The 67-arm battery HUNG on this loaded box -- OWED a quiet-window run, stated not skipped.
- **SEATING LINT** authorized by his word at ~F's terminal, built by ~F, accepted here with both card conditions.

## 2. ⛔ THE msg-verify BROKE TWICE, IN MY OWN HANDS, AND BOTH ARE FILED FABRIC-WIDE (68578)
1. **RACE:** it read `git rev-parse HEAD` AFTER committing, so a peer's commit landing in that window made it report
   the PEER'S hash and subject for MY commit -- **the shared-worktree HEAD class the feature exists to kill,
   reintroduced inside the fix.** Measured on its author: my commit `ccd60bd341`, its announcement `633cfc7c8b`.
   Caught only because the printed subject did not match the message I had just written.
2. **THE REPAIR SHIPPED BROKEN** @2d90173069: my edit wrote a literal **0x01 control byte** where the sed
   backreference belonged, so the capture substituted empty and the loud branch fired on every commit. **Same
   control-byte-in-a-tool class I fixed in comp-find six hours earlier -- third instance tonight, all three mine.**
   It failed in the SAFE direction by design, which is the only reason a broken verifier never became a lying one.
- **WORKING FORM @e5d7f493d8**, hash taken from `git commit`'s own output, no HEAD fallback, exercised end-to-end on
  its own commit. **CONSEQUENCE BROADCAST: any `[msg-verify] committed <hash>` line before @e5d7f493d8 is unreliable
  FOR THE HASH** (the MATCH/MISMATCH verdict is unaffected); re-derive from a path-scoped `git log -1 -- <file>`.
- **METHOD NOTE, the transferable half:** the broken form survived THREE of my own edits because I kept exercising a
  RETYPED COPY of the regex rather than the line in the file. **A control retyped is a control not tested.**

## 3. D0 GATES: CLOSED @04b20e008d -- the first project to close under the pipeline
Closure form per my own 66676 ruling (ratification-commissioned, no retroactive TO): delivered instance + CVO's
independent re-run + the ruling. **Verified at this seat rather than accepted** -- read the instance at @0f34fb69c8
and re-ran the checker myself (VALID rc=0 with its own honest announce-frame); CVO's three green batteries cited AS
CVO'S. **Four residuals carried forward explicitly** (gate 2 unarmed; the seating lint INERT on the live corpus with
COO's `<assignee>` remedy routed; the twr hazard's disarm and remediation at two owners; ~F's "the author's tests keep
passing because the author's blind spots are in both"). ~F released to the cap repair -- the first infrastructure
project to enter the pipeline at stage 1.

## 4. COT_CANON458 REGISTERED + PRD @ccd60bd341, on his 458M word
His reason is the load-bearing half and no lane could have measured it: *the number is canonical BECAUSE IT IS WHAT
THE CLIENT THEMSELVES SEE* -- now the governing precedent for client-facing figures (applied the same hour to the
Gain/Loss basis ruling). **Two requirements, only one ever scoped:** exclude held-away AND be on current data -- ship
the first alone and we emit 449.7M correctly implemented and still wrong. **Scope boundary ruled: the stopped
`fact_holdings` producer stays ADVI_COTETL's** -- a Rule 24(iv) failure ACROSS a registration boundary is the boundary
telling you where the work goes. **Order inversion declared in the PRD, not papered** (COO decomposed before the PRD
so measurement was not blocked by a pending registration call).

## 5. The Cottonwood finding: classified, corrected by DS~F, re-classified
I measured "cot silver HAS 08-20/08-21" and DS~F measured "stops at 08-19" -- **both true, different prefixes, neither
named.** *A prefix is part of a measurement, not part of its context.* Corrected shape, source-confirmed: the value
source was MIGRATED from `opal-data-cot/silver/holdings/` to `blackdiamond/cottonwood/silver/fact_holdings/`; **the
deprecated path is still fed to 08-21 and the migrated-TO path stopped at 08-19.** Silent because
`latest_holdings_date(on_or_before=)` falls back and does not error. Scope pinned by DS~F's adjacent-table control:
**one table's producer, not the tree, not the firm.** COO added prior art from the project's own file (a cot AUA
freeze root-caused to a holdings mechanism, $22.14M, ten weeks ago) as a POINTER, explicitly not a diagnosis.

## 6. Rulings issued this window
Transactions spec amendment (twelve stay enumerated, two DECLARED STATES: PII-EXCLUDED-PERMANENT vs NO-SOURCE-TODAY)
@462b301a3e - s.11 #11 SUPERSEDED-IN-PART on AE~G's self-scan (the gate count is TWO; a promote check reads #11 AND
s.14) @26bfd45353 - s.14(a) operationalised on AE~G's three-status split (REFUSED-NO-BMV to zero; the other two
reported and explained -- a bar that cannot be satisfied is broken, not high) @5fe8888189 - the Transactions
serving collision (sovereign shape wins; serving DEFERS; fan-out is the round-2 spec) - the per-family SERVING-STATE
axis (`deferred` now, `fan_out` round 2; AE~G's two-fields-at-one-grain Rule-24 refutation of my one-axis suggestion
RATIFIED) - the Gain/Loss METHOD ruling (serve the custodian's reported figure; the derived value is a printed
control; the basis identity DECLARED UNDETERMINED, not curve-fitted) - **doctrine section 8** on COO's proposed class
@52b2b946a5 (*your QUESTION framed the population*) - the push-chase TERMINATED with its instrument's blindness named.

## MCP traffic
~30 multi-recipient acts this window; every inbound READ-acked. Three corrections sent against myself (the two
msg-verify defects; the unnamed prefix). Zero traffic to any CRO serial, all session.

## Compiler Tools
| tool | invocation | result |
|---|---|---|
| safe-commit -F (msg-verify live) | ~12 commits | every landing verified by the tool's own report AND a path-scoped log |
| proof-of-spec-check | on ~F's D0 instance at its ref | VALID rc=0, announce-frame printed -- my own re-run, not ~F's claim |
| never-rules-gate (direct, file-fed JSON) | 3 cases | DENY+attribution / -F form silent PASS / plain PASS |
| aws s3 ls (rail-checked) | cot silver + bronze + 49F control | the classification read -- and the prefix lesson |
| git cat-file / branch -r --contains / reflog | push-chase + push-state claims | the local instrument's limit NAMED rather than worked around |

What failed: my own msg-verify, twice (s.2). One `sed -i` refused (`invalid reference \1`) -- the shell telling me the
truth Python had hidden. The 67-arm gate battery hung and is owed.

## Blockers
**None at this seat.** At Andrew: 14 open-calls cards + the push question (two instances now, both COO-authored,
arriving by fetch -- not a web merge, proven with a control) + the COT_CANON458 directive home. At COO: the
`<assignee>` back-fill; TO cuts on the two new decomps. At MSTR: the integration window.

## Next Steps
- **[Andrew]** the cards; the push question; the directive home.
- **[2.0.0_SA_COO]** COT_CANON458 + cap-repair TOs; the `<assignee>` element.
- **[3.0.0_SA_CVO]** certs as decomps land; the channel; the session scorecard at close.
- **[1.0.0_SA_CTO]** validate proofs; the PIPMAP proposals; the owed gate-battery run in a quiet window.
