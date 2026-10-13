# TO COMM_ASSIST.TO-CA-h-3 -- round 16 CA-h-3: the signed-answer path for muse, as a design (FWD-7; FWD-8 and FWD-5 ride it)

<to_id>COMM_ASSIST.TO-CA-h-3</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~8</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-h-3` (`decompositions/COMM_ASSIST_DECOMP.round16.md`) | **outcome_ref:** FWD-7 |
**depends_on:** CA-h-1 (this order is STAGED: it becomes `pending` when CA-h-1 is terminal and its folder layout is fixed; the issuer flips it and hands it to you on your same slot)

---

## WORKER FACE

### THE CELL

Andrew will answer a waiting draft (send it, drop it, or redraft it with notes) from muse, a tailnet VM, by writing an ANSWER FILE
into the dell2 reader folder you laid out in CA-h-1 (read `data/transcripts/scripts/muse_reader/refresh.py` and the `README.txt` it
writes). A job on dell2 forwards the file into the assistant (LDO-001). One rule governs the design: **an answer acts only when it
is shown to come from muse; any other answer is refused and recorded.** The reason: muse reaches dell2 as the SAME account dell2's
own agents run as, so an unsigned file cannot be told from a forged one. Nothing goes out in Andrew's name without his answer,
from either place.

You write ONE document, `MUSE_ANSWER_PATH_DESIGN.md`, in your deliverables folder: at most 140 lines, six sections, EXACTLY these
headings (the check reads them):

```
## 1. How muse's answer is shown to come from muse
## 2. How the forwarder verifies it
## 3. What is recorded on a refusal
## 4. The stale-version refusal
## 5. The write entry and the grant it needs
## 6. The forged-answer test that must refuse
```

### WHAT EACH SECTION MUST SETTLE

1. Two candidates, and a choice with the reason: (a) a signature made with muse's own key (its public key is already in the boxes'
   `administrators_authorized_keys`; read how `org/devices/` and `.tools/` name and use it; say which signature scheme the box can
   verify with what it has installed, e.g. `ssh-keygen -Y verify`, measured with one command if you can), or (b) a path only
   muse's SSH principal can write (say what on dell2 would enforce that, as an ACL or a separate account, and whether the dell2
   agents' account can write it). Name the weaker case plainly.
2. The forwarder (a dell2 job): what it reads, the order of checks (signature or path first, then the draft's tag and version),
   what it does on success (it posts ONE event into the assistant), and that it is idempotent (the same file twice acts once).
3. The refusal record: where it is written, the fields (time, file name, reason, the tag), and that a refusal never reaches the
   assistant.
4. The stale-version refusal: read `on_sms_reply`, `unseen` and the `pending` shape in
   `data/transcripts/scripts/teams_chat/tenant.py`. State what an answer must carry (the tag and the draft `version` it was
   shown) so the assistant refuses an answer to a draft that changed, the way the text path does ("changed just before your
   reply, so nothing was done").
5. The ENTRY the forwarder writes to. The assistant's event routes are in `ROUTES` in `tenant.py` (`sms.reply` carries Andrew's
   text answers; `owner.text` also exists). Name the one entry and the exact payload fields a muse answer would use, and the
   statement of WRITE permission dell2's identity would need (the action and the resource, scoped to that entry only). This is a
   statement the design names. Grant (d) is superseded: the Dell users join `AdministratorAccessOpalCapital` with three denies kept
   (audit writes, production S3 object deletes, table/database deletes; ruling @53acd6fe5f). Read `infra/aws/terraform/nfra-ctlpln-identity/`
   and say whether the group already permits the write; if it does, still name the entry and the scoped statement and say it is not
   a new request; if not, it is requested by name under C-ROLE-REQUEST and not inherited.
6. The test the build cell must pass: one answer signed or written by muse is acted on, and one answer written by the dell2
   agents' account without muse's proof is refused and recorded. State the two inputs and the two expected outcomes, and the
   control (that the refused arm refuses for the stated reason, not for an unrelated one).

### RULES FOR THIS CELL

- Edit nothing but the files in `<paths>`. This is a design: no script, no key, no AWS call, no SSH to any box, no change to
  `tenant.py`. Reading repo files and running ONE local command to measure what a box can verify is allowed.
- Quote file and line for every claim about existing code. Where you could not measure something, say "not measured".
- No non-ASCII. Bake no absolute path.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAh3-AC1" cell_refs="CA-h-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h3_design.py"</invocation><expect>H3-DESIGN sections=6 of 6</expect></criterion>
`CAh3-AC1` -- the issuer's check (read it; do not edit it): the document exists with the six headings above, at most 140 lines, names an assistant entry (`sms.reply` or `owner.text`) and the draft version. It prints sections=0 at the base.

<criterion id="CAh3-AC2" cell_refs="CA-h-3" judgment="true"/>
`CAh3-AC2` -- JUDGMENT, never self-graded: the design makes a forged answer from the dell2 agents' account refuse, names the weaker case plainly, settles the stale-version rule from the real code, and names the write entry and its grant as a separate request.
</proof_of_spec>

<expected_criteria>CAh3-AC1,CAh3-AC2</expected_criteria>

Run `CAh3-AC1` from the worktree root under `timeout 120`. Record `CAh3-AC2` with NO verdict (status `UNVERIFIABLE-BY-INSTRUMENT`,
the reason naming `3.0.0_SA_CVO`). Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~8/COMM_ASSIST.TO-CA-h-3.muse-signed-answer-design.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAh3-AC1,CAh3-AC2`, and flip `<status>` to `complete` only when
the mechanical criterion passes and the instance is VALID. Your surprise rows are `COMM_ASSIST-W8-S<k>`; append only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round16.md</decomp_doc>
<owned_cells>CA-h-3</owned_cells>
</decomp_ref>

<paths>
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-h-3.muse-signed-answer-design.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~8/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a design; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; the design NAMES the write statement to be requested later under C-ROLE-REQUEST.
comp-adversary: RUN -- a design that trusts a file because of where it sits (refused by section 1's weaker-case clause); a design whose refused arm refuses for an unrelated reason (section 6's control); a design that assumes the admin group covers the write without reading it (refused by section 5). BLIND: what dell2 can verify with its installed tools is measured only if the worker runs the one allowed command.
lane: the <paths> block IS the grant (worker RULING 1); STAGED until CA-h-1 is terminal.
</preflight>

Base: CAh3-AC1 base: FAIL as expected (sections=0, document absent).
Source: CTO round-15 analysis item 3 @15fdb72f21; PRD v0.6 FWD-7 and the CVO's refusal review `org/tier1_exec/3.0.0_SA_CVO/deliverables/COMM_ASSIST_PRD_V05_RATIFIED_TEXT_REVIEW_20261013.md` @1147cd5608; ruling @2f0ed70e40 section 4.
