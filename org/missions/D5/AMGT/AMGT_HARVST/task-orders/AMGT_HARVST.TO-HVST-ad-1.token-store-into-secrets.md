# AMGT_HARVST task order -- `HVST-ad-1` -- ROUND 31 chain 1: THE TOKEN STORE -- THE wsj AND barrons SESSION BUNDLES INTO AWS SECRETS, ft's BUNDLE EXPIRY MEASURED, AND THE sa ACCOUNT CHECK READS ITS `{user_id}` (FWD-1, FWD-9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ad-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~87</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; no collection run in this cell.
comp-iam: RUN at L5 -- NO publisher request of any kind (the playbook hard stop covers bbg/wsj/barrons; this cell sends none to anyone). Phase A0: no network. Phase A: AWS Secrets Manager CreateSecret/PutSecretValue for exactly the two secrets the halves name; secret VALUES are never printed, logged, written to a file or committed. NO S3 write, NO delete.
comp-adversary: RUN at L5 -- the adversary is a secret written with the wrong content or overwriting another publisher's secret, or a value leaked into a log. AC1 reads the two secrets back by NAME and compares a SHA-256 of the stored value to the local bundle's, prints hashes only, and plants a sentinel value in the writer's test to prove it never reaches any output.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO REQUEST TO ANY PUBLISHER** in this cell, in any phase.
2. **No secret VALUE** is printed, logged, written or committed. Hashes and names only.
3. The runtime root `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest` is READ-ONLY. The local
   saved-session files STAY; the collector keeps reading them until a cloud read of the Secret is proven (a later round).
4. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~87/scripts/`; outputs named `ad1_*`.
5. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~87/AMGT_HARVST.TO-HVST-ad-1.token-store-into-secrets.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-ad-1.token-store-into-secrets`.

<paths>
lib/opal_data_harvest/credentials.py
lib/opal_data_harvest/test_ad1_token_store.py
org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~87/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE WORK (`ROUND_ANALYSIS.round30.md` section 4 item 1, ruling 5)

**PHASE A0 (LOCAL, no network), merged by the issuer before the pair:**
1. **The bundle writer.** In `credentials.py`, a function that reads a publisher's saved-session file (the collector's own
   DPAPI reader) and writes it to a named Secret (create if absent, else put a new version). It returns a SHA-256 of the value
   written, never the value. Only wsj and barrons are in scope; any other publisher name refuses.
2. **The sa account id.** `sa_rest_fetch.check()` hard-codes `/api/v3/account/1btfwdu/info` (row `Z-W85-S2`), but
   `contracts.json` sa `auth_check` names `{user_id}`.
   - It now takes the user id from the stored sa session, whichever field carries it (measure it; print the field NAME, never
     its value).
   - If none carries it, it raises; it never falls back to the literal.
3. **ft's bundle expiry, read-only:** print, per cookie in the stored ft bundle, the cookie NAME and its expiry (UTC), plus
   the earliest expiry of the login cookies. Values are never printed.

**PHASE B (WORLD, under a pair):** run the writer ONCE for wsj and ONCE for barrons, into the two Secret names the halves name.
Then run AC1.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ad-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~87/scripts/ad1_ac1_store_readback.py</invocation><expect>PUBLISHER NETWORK CALLS: 0</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-ad-1"><invocation>python -m pytest lib/opal_data_harvest/test_ad1_token_store.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-ad-1"><invocation>python -m pytest lib/opal_data_harvest/ -rA --tb=line</invocation><expect>passed</expect></criterion>
</proof_of_spec>

**What each criterion must prove or print:**
- **AC1** (after phase B; at phase A0 it prints `NOT YET WRITTEN` per secret). It prints:
  - per secret: its NAME, existence, and whether the SHA-256 of its stored value equals the SHA-256 of the local bundle;
  - ft's bundle expiry per cookie name, and the earliest login-cookie expiry;
  - the sa session field name that carries `user_id`;
  - the line `PUBLISHER NETWORK CALLS: 0`.
- **AC2**, the plants; a mutant restoring each base behaviour fails:
  - (a) the writer refuses any publisher other than wsj and barrons;
  - (b) a planted sentinel value never appears in any output or return;
  - (c) `check()` builds its URL from the session's user id and never from the literal `1btfwdu`;
  - (d) a session with no user id makes `check()` raise.
- **AC3:** the base is commit `6adebef352`, pinned. Print the base and after pass counts. No test that passed at the base
  fails.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round30.md` @`6adebef352` section 4 item 1, ruling 5. The cloud ruling section 0 cell 1.
- **The Secret names are named in the halves at phase B,** following the existing pattern (`bloomberg/session`,
  `seeking-alpha/session`, `astn/ft/session`). Rule 30's `name()` builder applies to new pipelines, and HARVST is an existing
  one; the halves say so.
- **`sa_rest_fetch.py` sits under `org/tier1_exec/4.0.0_SA_CRO/scripts/`**, the collector's `consumer` for sa
  (`contracts.json`). If owned-paths refuses the worker's commit there, it is a row, and the issuer routes the one-line fix to
  `4.0.0_SA_CRO~Z`.
- **Premise counts, re-measured at the cut** (ruling 4): two bundles to store (`wsj.dpapi`, `barrons.dpapi`, both present,
  mtime 09-30 per `ab-1`'s census); one hard-coded account literal.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>31</round>
<slot>~87</slot>
<fabric>site-z</fabric>
