# TO NFRA_CTLPLN.TO-CT-u-2 -- workstream REMOTE CT-u-2: the laptop-side read of "does each box answer SSH by key, and refuse the rest"

<to_id>NFRA_CTLPLN.TO-CT-u-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~61</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>REMOTE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-u-2` (`decompositions/NFRA_CTLPLN_DECOMP.remote1.md`) | **outcome_ref:** FWD-27 |
**depends_on:** `CT-u-1` (same worker's queue; staged until the issuer hands it over)

---

## WORKER FACE

### THE CELL

FWD-27's DONE WHEN: from the laptop, `ssh -o BatchMode=yes <user>@<tailnet-ip> hostname` answers with the box's own name for sitez,
dell1, dell2 and the laptop itself. Its ACCEPT also says port 22 is admitted only from the tailnet and a password login is refused.
MEASURED TODAY: nothing reads this. You build the read, so that after Andrew's elevated run on a box, one command shows whether that
box is done, and a `CLOSED`/`OPEN`/`REFUSED` answer is never confused with "the probe could not run".

### BUILD

`.tools/ssh-tailnet-verify.py` (Python 3.9 compatible, standard library only, ruff clean, ASCII only):
`python .tools/ssh-tailnet-verify.py [--box <name> ...] [--user <login>] [--timeout 5] [--selftest]`.

1. Boxes and addresses come from `lib/devices.py` (`devices()`; each row has `name`, `tailnet_address`). No box name or address is typed
   in the tool. `--user` defaults to the environment variable `OPAL_SSH_USER`; with neither set the tool refuses
   (`REFUSED: no login name`, exit 2). Do not guess a login.
2. Per box, in this order, one line `BOX <name> <addr> <check>=<verdict> ...`:
   - `port22`: a TCP connect to `<addr>:22` within the timeout. `OPEN`, `CLOSED` (refused or timed out), or `PROBE-ERROR` (the probe itself
     failed to run; never reported as CLOSED).
   - `key`: only if port22 is OPEN: `ssh -o BatchMode=yes -o ConnectTimeout=<t> -o StrictHostKeyChecking=accept-new -o PasswordAuthentication=no <user>@<addr> hostname`.
     Run through `subprocess` with an argv list (never a shell string). `ANSWERED:<the hostname printed>` when rc=0, `DENIED` when it prints
     `Permission denied`, `PROBE-ERROR` otherwise. A key answer counts only when the hostname printed equals the box's `name` or
     `tailnet_name` or one of its `aliases` in the register, compared case-insensitively; anything else is `MISMATCH:<printed>`.
   - `password_arm`: only if port22 is OPEN: `ssh -o BatchMode=yes -o PreferredAuthentications=password -o PubkeyAuthentication=no ...`
     must NOT log in. `REFUSED` when it prints `Permission denied` or `no more authentication methods`; `LOGGED-IN` is a FAILURE;
     `PROBE-ERROR` otherwise. (BatchMode means no password is ever typed or sent.)
   - `nontailnet_arm`: report only `NOT-DRIVEN` for every box. The tool cannot source a connection from a non-tailnet address; the
     firewall rule's remote scope is read separately, from the box's own enable receipt. Say so in the line; do not fake a pass.
3. LAST line: `SSH-VERIFY boxes=<n> done=<k> not_done=<list or ->`, where a box is `done` only when port22=OPEN, key=ANSWERED and
   password_arm=REFUSED. Exit 0 when every requested box is done, else 1 (2 on refusal).
4. `--selftest`: runs against a local fake SSH listener and fake `ssh` stubs, no network beyond loopback. Cases: (1) a box answering key
   with its own name is done; (2) a closed port is CLOSED, not PROBE-ERROR; (3) a probe that cannot start is PROBE-ERROR, not CLOSED;
   (4) a hostname that differs from the register reads MISMATCH and is not done; (5) a password login that succeeds reads LOGGED-IN
   and is not done; (6) no `--user` and no `OPAL_SSH_USER` refuses. LAST line: `SSH-VERIFY-SELFTEST cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

You run `ssh` only against the loopback fake in `--selftest` and, for AC2, against the real register once (a read; the boxes mostly answer
CLOSED today). You never type or send a password, and you never write a key or an `authorized_keys` file anywhere. You change no remote
machine, start no service on the real machine and send nothing on the agent bus. No box name, tailnet address, user name or path under
a user's home is typed into the tool. Nothing here is an alert or a monitor; it is a one-shot read. The law files `CLAUDE.md` and
`org/XXX.md` are LOCKED. No non-ASCII.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W61-S<k>`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTu2-AC1" cell_refs="CT-u-2"><invocation>python .tools/ssh-tailnet-verify.py --selftest</invocation><expect>SSH-VERIFY-SELFTEST cases=</expect></criterion>
`CTu2-AC1` -- every case passing; the line reads `ok=True`.

<criterion id="CTu2-AC2" cell_refs="CT-u-2"><invocation>python .tools/ssh-tailnet-verify.py --user probe-only --timeout 3</invocation><expect>SSH-VERIFY boxes=4</expect></criterion>
`CTu2-AC2` -- the tool run once against the real register, reading all four boxes (`done` may be any number today; the exit code is not graded). It
makes a TCP connect and, where a port answers, a BatchMode ssh with a login name that exists nowhere (`probe-only`), so no real account is tried.
</proof_of_spec>

<expected_criteria>CTu2-AC1,CTu2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~61/NFRA_CTLPLN.TO-CT-u-2.ssh-tailnet-verify-tool.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTu2-AC1,CTu2-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.remote1.md</decomp_doc>
<owned_cells>CT-u-2</owned_cells>
</decomp_ref>

<paths>
.tools/ssh-tailnet-verify.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-shot read, nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a closed port reported as a probe failure or the reverse (cases 2, 3); a different machine answering at the address read as the box (case 4, hostname compared with the register); a password login that works read as fine (case 5); the non-tailnet arm claimed as passed when it was not driven (printed NOT-DRIVEN); BLIND: a tailnet address re-assigned to another machine with a matching name.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.23 FWD-27; CTO msg 108406; plan `LD0644_ROLLOUT_PLAN_CLUSTER_REMOTE_ACCESS_TAILNET_20261011.md` section 3 (verification from the laptop).
