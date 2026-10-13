# TO COMM_ASSIST.TO-CA-i-2 -- round 17 CA-i-2: the assistant verifies muse's signature at the RECEIVER and refuses every other answer (FWD-7; W8-S6)

<to_id>COMM_ASSIST.TO-CA-i-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~10</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-2` (`decompositions/COMM_ASSIST_DECOMP.round17.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Andrew's assistant (LDO-001, `data/transcripts/scripts/teams_chat/tenant.py`) texts him a draft and acts on his answer: `1` sends it, `0` drops
it, notes redraft it. He will also answer from muse, an agent on his tailnet, by a SIGNED answer file. The rule: **an answer from muse acts only
when its signature verifies against muse's public key pinned in the assistant's own configuration; any other muse answer is refused and
recorded, and nothing is sent.** The check happens HERE, in the receiver, because the machine that forwards the answer has AWS rights of its own
and can put an event on the queue directly: a check anywhere upstream of the receiver can be skipped. The existing text path (`sms.reply`) is the
fallback and must not change in behaviour.

### THE CONTRACT (fixed by the issuer; the forwarder cell and the check pin their halves of it)

- Event kind: `muse.reply` (a new kind; add it to `ROUTES`). Payload: `{"answer": {"payload": "<text>", "signature": "<armored SSHSIG>"}}`.
- `answer.payload` is the exact text that was signed: a JSON object `{"tag", "action", "notes", "version", "signed_at"}`; `action` is `send`,
  `drop` or `edit`. Signature namespace: `muse-answer@opal`. Key type `ssh-ed25519`.
- The pinned key: environment variable `MUSE_ANSWER_PUBKEY`, read AT CALL TIME (not at import), holding one `ssh-ed25519 AAAA... [comment]` line.
  Unset or blank: fail CLOSED (refuse every muse answer, reason `no-key-configured`). Type no key into any file.

### BUILD, IN THIS ORDER

1. A new module `data/transcripts/scripts/teams_chat/muse_verify.py`, **standard library only**. The handler has no extra layer (only the Python runtime
   and boto3), so no `ssh-keygen`, no `cryptography`, no `nacl`. It exposes `verify(pubkey_line, namespace, message_bytes, armored_signature) -> (ok, reason)`
   with reason `ok`, `bad-signature` or `no-key-configured`; it never raises on bad input (a malformed signature is `bad-signature`).
   - SSHSIG (OpenSSH `PROTOCOL.sshsig`): strip the `-----BEGIN/END SSH SIGNATURE-----` lines and base64-decode. Blob = the 6 bytes `SSHSIG`, uint32 version
     (must be 1), then SSH strings (uint32 big-endian length + bytes): public key, namespace, reserved, hash algorithm (`sha256` or `sha512`), signature.
     The public-key string is itself `string "ssh-ed25519"` + `string <32-byte key>`; the signature string is `string "ssh-ed25519"` + `string <64-byte sig>`.
   - The signed data is: `SSHSIG` + string namespace + string reserved + string hash algorithm + string H(message), H the named hash. Check the blob's
     namespace equals `muse-answer@opal` and its embedded public key equals the pinned key's 32 bytes (compare the bytes, not the comment).
   - Ed25519 verification per RFC 8032 section 5.1.7 with Python integers and `hashlib.sha512`: reject `s >= L`, reject a point that does not decode,
     check `[s]B = R + [k]A`. About sixty lines. The check's real `ssh-keygen -Y sign` signatures are your control: a verifier that agrees with them is
     right, one that does not is wrong, whatever it reasons.
2. In `tenant.py` add `on_muse_reply(ctx)` and `ROUTES["muse.reply"] = on_muse_reply`:
   - No `answer`, or no `payload`, or no `signature`: refuse, reason `no-signature`. Pinned key unset: `no-key-configured`. Verification fails: `bad-signature`.
   - A refusal changes no draft and sends nothing (no chat post, no text to Andrew, no event). It appends `{"at": <iso now>, "reason": <reason>, "tag": <the
     tag in the payload if it parses, else null>}` to `ctx.state["muse_refusals"]`, keeping the last 50, and returns `"muse-refused"`.
   - On a verified answer, parse the signed payload and run it through the SAME code `on_sms_reply` runs for the same tag, action, notes and version, so
     send, drop, edit, the stale-version check and every message to Andrew behave exactly as the text path does; return that function's result string.
     (Set the verified fields as the context's payload for that call, or factor a small helper both call; do not copy the logic.)
3. **W8-S6.** In `on_sms_reply`, the stale check (`unseen(ctx, p)`) also covers `action == "edit"`. A text-path edit carries no `version` in its payload, so its
   behaviour must not change; an answer that does carry a `version` and is stale gets `"unseen"` and the "changed just before your reply" text, and the
   draft is not redrafted.
4. Add tests to `data/transcripts/scripts/tests/test_teams_chat_tenant.py` (and a small `test_muse_verify.py` beside it if you prefer): at least one valid
   answer per action, a forged-key answer, an unsigned answer, a tampered payload, a stale edit, and the unset-key case. Generate signatures with
   `ssh-keygen -Y sign` inside the test and skip with a clear reason when `ssh-keygen` is absent. Existing tests must still pass.
5. No non-ASCII. No AWS call, no network, no change to Terraform or to any file outside `<paths>`.

### RULES FOR THIS CELL

- Edit nothing but the files in `<paths>`. This is a code change with tests: it is NOT deployed here (a later cell deploys it under change management).
- A forged `sms.reply` that imitates the text path is a pre-existing weakness of the text path and is outside this cell: if you confirm it from the code,
  file ONE row naming it and keep working.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi2-AC1" cell_refs="CA-i-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_receiver.py"</invocation><expect>I2-RECEIVER ok=True arms=7 of 7</expect></criterion>
`CAi2-AC1` -- the issuer's check (read it; do not edit it): real `ssh-keygen -Y sign` keys, seven arms. A muse-signed send is acted on; a forger's signature, an unsigned answer, a direct send with no `answer`, a tampered payload and a wrong namespace are each refused with the stated reason and change nothing; a stale signed edit gets `unseen`. It prints ok=False at the base.

<criterion id="CAi2-AC2" cell_refs="CA-i-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAi2-AC2` -- the bound, a control that PASSES at the base (19 passed) and must still pass with your new tests added: the assistant's flow tests, the text path included.
</proof_of_spec>

<expected_criteria>CAi2-AC1,CAi2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~10/COMM_ASSIST.TO-CA-i-2.receiver-verifies-muse-signature.proof_of_spec.json`,
validate it by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree:
`python .tools/proof-of-spec-check.py <instance> CAi2-AC1,CAi2-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID. Your
final report names: the Ed25519 verification you wrote and how you know it is right (the seven arms, plus your own tests), the exact refusal reasons, and
whether the edit-branch change altered any text-path test. Your surprise rows are `COMM_ASSIST-W10-S<k>`; append only to the investigation file and keep its
existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-2</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/teams_chat/muse_verify.py
data/transcripts/scripts/tests/test_teams_chat_tenant.py
data/transcripts/scripts/tests/test_muse_verify.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-2.receiver-verifies-muse-signature.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~10/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made; the deploy that pins MUSE_ANSWER_PUBKEY is cell CA-i-4.
comp-adversary: RUN -- a check upstream of the receiver (refused: the whole cell is the receiver); a verifier that accepts any well-formed signature (refused: AC1 forger, tamper and namespace arms); a refused arm that refuses for an unrelated reason (refused: AC1 asserts the stated reason string); a muse answer applied to a draft that moved on (refused: AC1 stale-edit arm); a change to the text path (refused: AC2). BLIND: the handler's real packaging (the zip is built elsewhere; stdlib only is assumed from chat_assist.tf:70, which names no layer) is not read by this cell.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAi2-AC1 base: FAIL as expected (route missing, 0 of 7); CAi2-AC2 base: PASS as expected (control, 19 passed). AC1 green arm: PASS as expected against a scratch reference receiver using ssh-keygen -Y verify (7 of 7).
Source: CTO round-16 analysis `ledger/ROUND_ANALYSIS.round16.md` @6e9e2fc1ff section 3 item 2 and the ruling in its section 2; CVO grade `COMM_ASSIST-C-S1` (commit 6d9d2b697d); rows COMM_ASSIST-W8-S6, W8-S8; PRD v0.7 FWD-7.
