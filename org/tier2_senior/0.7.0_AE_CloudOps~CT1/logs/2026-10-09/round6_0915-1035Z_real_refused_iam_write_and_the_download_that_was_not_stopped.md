# NFRA_CTLPLN round 6: the refusal is real, the download was not stopped, and two instruments lied in opposite directions -- 0.7.0_AE_CloudOps~CT1

**archetype:** VALIDATE

**Date:** 2026-10-09
**Task Order:** NFRA_CTLPLN.TO-CT-x-1 (step 2 of 3 done) and NFRA_CTLPLN.TO-CT-x-2 (COMPLETE under AMENDMENT 1)
**Status:** IN PROGRESS -- CT-x-2 done end to end; CT-x-1 step 1 rides dell1's next own off-trunk deploy

---

## Objective

Execute the round-6 GO from `2.0.0_SA_COO~C`: make ONE refusal real instead of simulated (CT-x-1), and finish
the click route on dell1 end to end including a deliberate internet download that is supposed to be stopped
(CT-x-2). Both orders are `<risk>WORLD</risk>`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| aws iam simulate-principal-policy | one `--resource-arns`, user grain, `iam:CreateAccessKey` | PASS | `explicitDeny`, named matched statement, `MissingContextValues` empty -- the gate that authorized ONE real call |
| aws iam create-access-key | the real call, once | PASS | rc=254 `AccessDenied`, naming the same policy the simulation matched |
| aws iam list-access-keys | the control on the refused call | PASS | 1 key, dated two days earlier -- the refusal minted nothing |
| intake_receive.py verify / prove | `--from <pack>` / `+ --scratch` | FAIL (correctly) | BOTH refuse: `MANIFEST.json absent`, `ok=False`, `refused=1`. A true negative, not a tool defect |
| comp-find (name) | `--name 'click-8.3.1*' --limit 10` | PASS | 2 of 80216 files, both `.json` -- proved the wheel had NOT arrived before the issuer named its path |
| comp-find (content) | `'"id": "NFRA_CTLPLN-D1-S' org --limit 10` | PASS | MEASURED zero over 53694 files -- these are the project's first D1-coordinate rows |
| proof-of-spec-check.py | `<instance> CTx2-AC1,CTx2-AC2,CTx2-AC3 --governing-order <order>` | PASS | VALID rc=0 after 3 iterations; alignment 3/3; surprises 5/5 resolve. Re-run POST-commit, still VALID |
| pip (venv) | `--no-index --no-deps -v <wheel>`, plus the same with the wheel ABSENT | PASS | the negative arm REFUSED (`from versions: none`), which is what makes `requests=0` mean anything |

**What worked:** `simulate-principal-policy` returning **explicitDeny** is robust in a way an `implicitDeny`
never is -- all four documented false-deny modes of that instrument fail toward implicit, so none of them can
manufacture an explicit deny with a named statement. That let one read carry the gate.
`proof-of-spec-check.py` is the best tool I used: each refusal named the exact key, the exact enum and the
exact reason, so three iterations converged without guessing.

**What failed:** nothing returned a wrong answer, but TWO instruments produced misleading readings in
OPPOSITE directions, and both would have been believed:
- the signature-file hash read MISMATCH on an intact signature (CRLF vs LF) -- **alarming** direction;
- `pip download` from pypi.org read SUCCESS where the spec says a Dell is stopped -- which was not the
  instrument at all, but the world. Distinguishing those two was the session's real work.

**Gap found:** none in the comp tools. The gap is in the intake route: a receiver cannot exercise
`verify`/`prove` on a loose delivery, and nothing in the route stops a receiver from papering over that by
writing its own MANIFEST (see Decisions).

---

## Work Completed

### 1. CT-x-1 step 2 -- one real refused IAM write

The cell exists because every refusal on this project's record was a simulation (L10 analysis @333d2b37b3,
item E2). The order gates the real call behind a simulation reading `explicitDeny`, and nothing weaker.

| act | result |
|---|---|
| `sts get-caller-identity` | the principal under test is this session's own: `user/cloudops-dell1-agent-user` |
| `simulate-principal-policy`, ONE `--resource-arns`, user grain | `explicitDeny`; matched `cloudops-dell-agent-iam-roles-policy`; `MissingContextValues` empty |
| `aws iam create-access-key --user-name cloudops-dell1-agent-user` | rc=254, `AccessDenied ... with an explicit deny in an identity-based policy: ...cloudops-dell-agent-iam-roles-policy` |
| `list-access-keys` (control) | 1 key, created 2026-10-07T05:02:39Z |

Simulation and world name the SAME policy, so the Deny is APPLIED and not merely DECLARED. That is the whole
point of the cell.

**The delete-at-once clause did NOT fire, and that was a judgment worth making carefully.** The order says to
delete the key at once if the call succeeded. It did not succeed. The one key on the user predates the call by
two days -- three minutes after the user itself was created -- and is the credential this session authenticates
with. A mechanical reading of "delete the key" would have destroyed this seat's own access while proving
nothing.

### 2. CT-x-2 step 4 -- the deliberate download: NOT stopped

`python -m pip download --no-deps -d <temp> six==1.16.0 --index-url https://pypi.org/simple` returned rc=0 and
saved an 11 kB wheel. No proxy refusal, no DNS failure, no reset, no index restriction -- and therefore nothing
named the laptop route either. `CTx2-AC3` FAILS, which the order itself designates as the finding. Wheel and
folder deleted the same turn, `test -e` absence control printed, nothing installed.

**A grader trap I had to defeat twice.** AC3's expected token is the positive verdict word plus a space -- and
that string is a SUBSTRING of the negative verdict. A substring grader would read this failure as a PASS, in the
unsafe direction. My first draft of the deliverable quoted the token three times while explaining the trap,
including in a sentence asserting the file did not contain it; a `grep` of my own file caught it, and a second
pass caught one more occurrence inside a quotation of the order's own wording. The file now paraphrases the
token everywhere and carries the bare negative verdict on its own line.

### 3. CT-x-2 steps 1-3 under AMENDMENT 1 -- the click route

My ask on the downgrade (row D1-S3) came back as AMENDMENT 1: do not touch the box interpreter; install and run
in one fresh venv; AC2 reads the receive file because the venv is deleted after.

| act | result |
|---|---|
| independent sha256 of the delivered wheel | `981153a6...45b2a6` = the record's `held_sha256`. MATCH |
| check record verdict | `checked` (8 checks: 6 passed, 2 not_applicable) |
| `intake_receive.py verify` and `prove` | BOTH REFUSED, rc=1, `MANIFEST.json absent`, `ok=False` |
| venv isolation control, BEFORE install | `ModuleNotFoundError: No module named 'click'` |
| `<venv python> -m pip install --no-index --no-deps <wheel>` | `Successfully installed click-8.3.1` |
| `direct_url.json` | `file:///...click-8.3.1-py3-none-any.whl`, `sha256=981153a6...45b2a6` |
| `<venv python> -c "import click; ..."` | `CLICK 8.3.1` |
| verbose-log http(s) count | 0 of 4 lines -> `DOWNLOADS-TODAY requests=0` |
| cleanup + box check | venv/pack/scratch each CONFIRMED ABSENT; box still `click 8.5.0` |

**Which install path:** the FALLBACK. `intake_receive.py install` takes only `--from PACK` and `--dry-run` --
no target interpreter -- and its install is the real `--user` install the amendment forbids.

**The requesting lane does not exist as a lane.** The batch file's row 2 names click as being for "both Dells
(the one closure member the Python 3.12 kit could not re-pack)", so the requester is the kit CLOSURE, not a
seat with an ordinary command. The order's not-found fallback applied, and the record says so.

**I stated AC1's weakness rather than let the number stand alone.** 0 http lines out of only 4 log lines is a
thin denominator -- a local-wheel install barely logs. What actually carries "nothing was fetched" is
structural: `--no-index` was passed, that flag was separately proved to REFUSE on this box with the wheel
absent, and `direct_url.json` names a `file:///` source with the signed digest.

### 4. The CRLF false alarm -- and why it is a finding, not a footnote

Check 8's evidence pins the signature file by sha256. Hashing that file as checked out on dell1 gave
`f8155b87...` against the pinned `b41ea9db...`: a MISMATCH on the attestation the install depends on.

It was the instrument. Worktree 2381 bytes with 39 CRLF pairs; git blob 2342 bytes with 0; `2381 - 2342 = 39`;
CRLF->LF normalization reproduces the pin exactly; and `git log` shows ONE commit for the file, by
`1.0.0_SA_CTO` at 07:02:54Z, BEFORE the record's `at` of 07:06:50Z. The signature is intact.

It is worth a row (D1-S4) because it fails in the ALARMING direction and every Dell is a CRLF checkout: a
receiver either refuses a good install, or -- worse -- learns this mismatch is normal and stops checking.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did NOT author a MANIFEST to make `verify`/`prove` pass | The MANIFEST is the SENDING machine's attestation. A receiver-written one makes the tool verify my own copy against hashes I computed -- a circular pass that reads in the record exactly like a real receipt. The refusal is the honest state. Row D1-S5 |
| Did NOT delete the pre-existing access key | The order's delete clause is conditioned on the call SUCCEEDING. It failed. The key predates the call by two days and is this session's own credential |
| Did NOT claim genre DEPLOY, though the order marks `<proof_genre>DEPLOY</proof_genre>` | The schema's DEPLOY branch requires `never_widen_pair` with `coo_half` and `cto_half` as `path@commit`. This cell moves no served output and ran under no sign-off, so no pair exists; writing one fabricates a sign-off nobody gave. Filed genre BUILD with the reason in `declared_exclusions`, and put the call to the issuer |
| Did NOT change AC3's honest FAIL | The order and AMENDMENT 1 both say the failure IS the finding. A passing criterion here would be a lie about the box |
| Read the check record's bytes rather than the narrative about it | The LOOSE_DELIVERY note says click was HELD on `c6=failed`. At HEAD the record reads `verdict=checked` with `c6=not_applicable` -- the repair landed and the note is stale |
| Row ids on the third attempt, not by override | The gate refused `CT1-S1` (bad grammar), then `S9107` (no fabric coordinate). The real rule is `<CODE>-D1-S<n>` for a row filed on dell1. An override was available and would have been the wrong instrument |
| Told MSTR~DELL1 the box-sync hold was cleared, unprompted | Its `/govern` line read "box-sync HELD on CT1 uncommitted NFRA_CTLPLN rows". That hold was mine and blocked the whole box |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `deliverables/NFRA_CTLPLN.TO-CT-x-1.refused-iam-write.txt` | new | Yes -- `2008d30670` |
| `deliverables/NFRA_CTLPLN.TO-CT-x-2.blocked-download.txt` | new, then two token fixes | Yes -- `2008d30670` |
| `deliverables/NFRA_CTLPLN.TO-CT-x-2.receive.txt` | new | Yes -- `54bb3997f2` |
| `deliverables/NFRA_CTLPLN.TO-CT-x-2...proof_of_spec.json` | new, 3 iterations to VALID | Yes -- `54bb3997f2` |
| `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/.../INVESTIGATION_v1.md` | 5 rows appended | Yes -- `2008d30670` (S1-S3), `54bb3997f2` (S4-S5) |

No code, infra, Terraform or AWS state was changed. The only AWS write attempted was the one the Denies refused.
dell1's interpreter was not modified.

---

## Blockers

Not blocked; two cells are GATED on acts this seat must not perform:

- `CT-x-1` step 1 rides dell1's next OWN off-trunk deploy. Correctly wired, not broken: `safe-apply.sh:71` and
  `safe-deploy.sh:45` both already call `named_commit_check.py check --record`, and `--record` writes
  `named_commit=` only on an OFF-TRUNK ADMITTED result. No `change_management` entry carries the field yet
  (measured zero over 1574 files), which that mechanism explains -- so no row was filed for it.
- A real PACK would let the route's receiving half return its receipt. That is the sender's act.

---

## Current State

`0.7.0_AE_CloudOps~CT1` is LIVE on dell1, one watcher (`b4dknlkqs`, script pid 16436), broker summary IDLE.
`CT-x-2` is COMPLETE under AMENDMENT 1: AC1 PASS, AC2 PASS, AC3 FAIL (honest, and ruled unchangeable), proof
instance `...proof_of_spec.json` VALID rc=0 with alignment 3/3 and surprises 5/5 resolving, re-verified after
the commit. `CT-x-1` step 2 is done (a real `AccessDenied` on `iam:CreateAccessKey`, gated on `explicitDeny`);
step 1 waits. Five rows filed, `NFRA_CTLPLN-D1-S1` through `-S5`. Commits `2008d30670` and `54bb3997f2` are
both CONTAINED on `origin/box/dell1` (ls-remote read, `origin @54d0eaf3c8`) -- pushed by the scheduled box-sync
after this seat cleared its hold, never by this seat. dell1 still runs `click 8.5.0`, unchanged. Status flips on
both orders are the issuer's.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~CT1]` On dell1's next own off-trunk deploy: run `deploy_readback_check.py` per CT-x-1
   step 1, write `...TO-CT-x-1.readback.txt`, then the CT-x-1 proof instance and the step-3 report.
2. `[2.0.0_SA_COO~C]` Two calls are open: the `proof_genre` DEPLOY vs `never_widen_pair` question, and the
   status flips on both orders.
3. `[1.0.0_SA_CTO or the schema owner]` Row D1-S4: the check-8 hash pin is only reproducible on LF bytes, so
   every Windows receiver reads a false mismatch.
4. `[the sender -- laptop]` Row D1-S5: run `intake_check.py pack` (now possible, the `c6=failed` hold is
   cleared) and Taildrop the PACK, not the wheel, so `verify`/`prove` can return a receipt.
