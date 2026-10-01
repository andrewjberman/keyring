# NFRA_OPLGTW task order -- `OG-lt-1` -- workstream TRNSPT-DEPS (O3): measure the stored sign-in's unattended lifetime, READ only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-lt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~17</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one on-demand measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads with existing access: read-only SSM on the gateway host.
comp-adversary: DECLARED-NOT-APPLICABLE -- a measurement; any token_broker change returns to the CTO (C7 O3).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM) and the gateway host's own Graph token refresh.
</preflight>

## 1. THE CELL -- `OG-lt-1` (decomposition addendum R3-T)

**The question** (PRD `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.2 C7 "Stored sign-in lifetime (order
O3)"; read it whole): how long does the gateway's server-held delegated token (the fixed identity behind the machine
routes, e.g. `MS_INGEST_IDENTITY`) refresh unattended before `NeedsLogin`? See
`infra/aws/ec2/opal-gateway/app/token_broker.py:171-183`. NFRA_TRNSPT's hourly schedule depends on the answer.

**Measure, on the live host `i-07dccb1615503ac99`, read-only SSM:**
1. **Store.** Read the token store's METADATA for that identity: when it last signed in interactively, and when it
   last refreshed silently. Use whatever store `token_broker.py` reads. Name the store, the key and the fields you
   used. Never print a token, a refresh token or a cache blob, and never let one leave the host. Hash or omit them.
2. **One silent refresh, on demand.** Run ONE refresh through the server-held path, by the host's own existing
   mechanism, and record its outcome: `OK` or `NeedsLogin`, with UTC time.
3. **Compute and classify.**
   - `observed_unattended_hours` = the refresh time minus the last interactive sign-in, when step 2 is `OK`. It is a
     LOWER BOUND on the lifetime, so its claim class is `measured`.
   - When step 2 reads `NeedsLogin`, record the span to the last OK refresh instead, with its claim class.
   - `verdict` = `GE_1_DAY` if the span is 24 hours or more, else `LT_1_DAY`.
4. **Record.** Write `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~17/TOKEN_LIFETIME.json` with
   exactly these keys:
   - `identity_class` (role words only, never an address);
   - `instrument` (the exact SSM command shape, secrets elided);
   - `measured_at_utc`, `last_interactive_auth_utc`, `last_silent_refresh_utc`;
   - `silent_refresh_now`;
   - `observed_unattended_hours` and `observed_unattended_hours_claim`;
   - `verdict`.

   Add a short `TOKEN_LIFETIME.md` explaining the instrument and what it cannot see. For example, the identity
   platform's own refresh-token policy is not readable from the host, so the span is a lower bound, never the
   ceiling.

## 2. BOUNDS

1. Read only. No code change, no `.env` change, no restart, no deploy. A `LT_1_DAY` verdict STOPS at the record: it
   returns to `1.0.0_SA_CTO~O` through the issuer, before any `token_broker` change.
2. Work in the worktree named in your identity line. Never push, merge, rebase, stash, `checkout --` or `clean`.
3. Use the `.tools/aws` shim for SSM. No vendor call. Commit with `.tools/safe-commit.sh` under your serial.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~17/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W17-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-lt-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/lt1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)fields present 9 of 9; malformed timestamps 0 of 3; claim class ok=True; verdict \w+ at [0-9.]+ h consistent=True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="J1" cell_refs="OG-lt-1" judgment="true"/>
</proof_of_spec>

- `AC1`: the record exists, every field is present, the timestamps are UTC, the claim class is declared, and the
  verdict agrees with the span.
- `J1`: graded at L9 by `3.0.0_SA_CVO~O`: the instrument reads the store the broker reads, the refresh was a real
  silent refresh on the server-held path, and the record's limits are stated. RECORD; NO VERDICT.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~17/NFRA_OPLGTW.TO-OG-lt-1.stored-signin-lifetime.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Record J1 as `UNVERIFIABLE-BY-INSTRUMENT` naming
`3.0.0_SA_CVO~O`. Report once: the verdict, the span, the instrument, and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~17, alone (its own component). It can run before OG-t-2 lands because it changes nothing, but it is cut
  with the rest of the workstream in the one issuance.
- The answer is passed to NFRA_TRNSPT's issuer through `1.0.0_SA_CTO~O` (cross-fabric).

<status>staged</status>
<round>8</round>
<slot>~17</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
