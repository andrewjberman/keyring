# AMGT_HARVST task order -- `HVST-bz-6` -- ROUND 84, workstream WSJBARRONS (`1.0.0_SA_CTO~DELL1` msg 4795, Andrew-direct 2026-10-13 ~12:2xZ item 4, bx-4's successor, part 1): THE SITE Z BOX HOLDS A VALID SAVED SESSION FOR WSJ AND FOR BARRON'S, MADE BY THE EXISTING HARVESTER FROM THE EXISTING CREDENTIAL

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-6.wsj-and-barrons-sessions-from-the-existing-credential</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the runner task is not stopped, started or re-registered.
comp-iam: RUN at L5 -- ONE Secrets Manager READ by name (`dowjones/credentials`, us-east-1), made by the CRO's existing harvester script, and the box's own DPAPI vault write. NO `--park`, NO new secret, NO S3 write, NO collection, NO new vendor, account or scope.
comp-adversary: RUN at L5 -- the adversary is a secret value, a cookie or a username in an output file or a commit, a second sign-in attempt after a refusal (the account is shared by both publishers and can lock), and a session minted when the saved one was already valid.
</preflight>

## 0. THE CELL

Andrew-direct (recorded `ANDREW_DIRECT_20261013_122xZ_...` item 4): "we have credentials and HARVEST scripts that do this". The WSJ/Barron's sign-in is not his act.
This cell uses what exists, and only that:
- **the credential:** the Secrets Manager secret `dowjones/credentials` (us-east-1), one secret shared by `wsj` and `barrons`
  (`lib/opal_data_harvest/credentials.py`, `CREDENTIAL_SECRETS`). It exists: one version, last changed 2026-09-14 (a `describe-secret` read, no value read).
- **the script:** `org/tier1_exec/4.0.0_SA_CRO/scripts/dowjones_harvest_session.py` (headful Chrome, Dow Jones SSO, credentials read from that secret by name),
  called by `SessionManager.refresh` in `lib/opal_data_harvest/auth.py`, which saves the session to the box's own DPAPI vault `<runtime>/secrets/<publisher>.dpapi`.
- **why it is needed:** the cycle runner runs `--no-sign-in`, so a publisher with no valid saved session ends its cycle `sign_in_refused` and moves on.

## 1. START CONDITIONS (all three read at the start, not assumed; any false: DO NOT START, file one row)

- (a) BOTH never-widen halves are on file and read SIGNED at their pins: COO half
  `deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ6_DOWJONES_SESSIONS.md` and CTO half `ledger/NEVER_WIDEN_ROUND84_BZ6_CTO_HALF.md`
  (`git show <pin>:<path>`; the issuer states the pins in the crossbox line).
- (b) The script `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py` (which you READ and run, never write) is present in
  the site Z checkout after `git fetch origin CLOUD` and a fast-forward.
- (c) The Windows user `Opal Bloomberg` has an interactive desktop session (`query user` names it): the harvester opens a real Chrome window.

## 2. THE ACT (site Z box, once; the publishers ONE AT A TIME, `wsj` then `barrons`)

`<runtime>` is `C:/Users/Opal Bloomberg/Desktop/wk-harvest-runner-pin-c1be67f53c/.runtime/harvest-cycle/runtime` (the task's own `--runtime-root`).
`<S>` is `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py`. Run from the repo root of the site Z checkout.
1. **Read the state first, for each publisher, and change nothing:**
   `python <S> wsj --runtime-root "<runtime>"` then the same for `barrons`. Save each as `bz6_state_<publisher>_before.out`. A line
   `VALID=True` means a saved session is present with `subscriber=True` and `network_auth_corroborated=True`.
2. **Mint only where it reads `VALID=False`, ONE attempt per publisher:** `python <S> <publisher> --runtime-root "<runtime>" --mint`. Save its whole output as
   `bz6_mint_<publisher>.out`. The script signs in through the existing mechanism and prints non-secret fields only.
   - **A line `MINT <publisher> REFUSED: ...`, or exit 3, is a STOP for BOTH publishers:** the account is shared, a second attempt can lock it, and a
     refusal is a recorded result. File ONE row naming the line, make no second attempt, and do not try the other publisher.
   - **A `VALID=True` publisher gets NO sign-in at all.**
3. **Read the state again** for each publisher: `bz6_state_<publisher>_after.out`.
4. Do NOT read, print, copy or commit the secret, a cookie, the vault file's content, a username or a password. Do NOT use `--park`. Do NOT stop, start or
   re-register the runner task: it picks up a new saved session at its next job.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round84/`. Anything odd: one row
`AMGT_HARVST-Z-S<next free Z number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round84/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-6"><invocation>python -c "import sys, runpy; sys.argv = ['bz6_session_state.py', 'wsj', '--runtime-root', 'C:/Users/Opal Bloomberg/Desktop/wk-harvest-runner-pin-c1be67f53c/.runtime/harvest-cycle/runtime']; runpy.run_path('org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py', run_name='__main__')"</invocation><expect>(?m)^STATE wsj present=True subscriber=True network_auth_corroborated=True .* VALID=True$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-6"><invocation>python -c "import sys, runpy; sys.argv = ['bz6_session_state.py', 'barrons', '--runtime-root', 'C:/Users/Opal Bloomberg/Desktop/wk-harvest-runner-pin-c1be67f53c/.runtime/harvest-cycle/runtime']; runpy.run_path('org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py', run_name='__main__')"</invocation><expect>(?m)^STATE barrons present=True subscriber=True network_auth_corroborated=True .* VALID=True$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. Both criteria are site Z reads and cannot run from dell1. The script is READ ONLY without `--mint`, so the
  criterion's own invocation makes no sign-in.
- **Amendment (issuer, round 84, Z-S118):** the invocations above ran the script BY PATH, which puts the script's own directory on `sys.path[0]` and never the
  repo root, so its `from lib.opal_data_harvest...` import raised `ModuleNotFoundError` on every box (measured by `0.7.0_AE_CloudOps~ZW`, before and after the act). `python -c`
  keeps `sys.path[0]` at the cwd (the repo root, per the heading) and `runpy.run_path` runs the SAME script bytes as `__main__`; the script is unedited and its expected
  line is unchanged. Probed on dell1 against a nonexistent runtime root: the old form raises, the new form prints `... present=False ... VALID=False` rc 0.
- **Dry-run at the base (issuer, against a fake vault, `test_bz6_session_state.py`, 6 passed):** an absent session prints `present=False ... VALID=False`, so
  AC1 and AC2 do NOT match (FAIL as expected); a valid planted envelope prints `VALID=True` and matches; no cookie, username or token appears in any output.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-6.wsj-and-barrons-sessions-from-the-existing-credential.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-6.wsj-and-barrons-sessions-from-the-existing-credential`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 700 CRLF lines).** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4795 and `ANDREW_DIRECT_20261013_122xZ_CAPPED_LOTS_UNVERIFIED_SHARE_COUNT_SOURCES_PORTAL_SMOKE_WSJ_CREDS.md` item 4: the act
  asked of Andrew (open call 8c66) is withdrawn; "Find the existing credential and the HARVEST script that signs in; read where each lives without printing the
  secret. Cut bx-4's successor on them, with no new vendor scope."
- **What was read to find them (names and metadata only, no value):** `lib/opal_data_harvest/credentials.py` (`CREDENTIAL_SECRETS["wsj"|"barrons"]` =
  `dowjones/credentials`; no Secrets session for these two, their token is the saved-session file), `lib/opal_data_harvest/auth.py` (`_refresh` runs the CRO
  script), `org/tier1_exec/4.0.0_SA_CRO/scripts/dowjones_harvest_session.py` (reads `dowjones/credentials`; `--park` is explicit and is NOT used here), and
  `aws secretsmanager describe-secret` on that name (one version, LastChangedDate 2026-09-14, LastAccessedDate 2026-09-30).
- **Not done here:** the cycle read for each publisher. A runner pass is `bbg`, `wsj`, `barrons` in turn, so wsj starts only after bbg's current cycle ends
  (about 19:10Z). That read is `HVST-bz-7`, read-only, and it is bx-4's acceptance.
- **Pair:** COO half `deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ6_DOWJONES_SESSIONS.md`; CTO half
  `ledger/NEVER_WIDEN_ROUND84_BZ6_CTO_HALF.md` (owed). The act does not start without both on file.
- **Risk named:** a headful vendor login by a script on a subscriber account can draw a challenge or a lock; the order makes ONE attempt per publisher and
  stops both on the first refusal. Vendor login is within the standing rule "other vendor APIs need no per-use word"; Bloomberg is not involved.
- Delivered as a crossbox ORDER through MSTR (`python .tools/crossbox-call.py open --kind ORDER --to-device sitez`).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>84</round>
<workstream>WSJBARRONS</workstream>
<slot>site-z</slot>
<fabric>dell1</fabric>
