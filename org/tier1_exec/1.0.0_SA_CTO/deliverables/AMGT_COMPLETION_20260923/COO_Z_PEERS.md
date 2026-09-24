# MANDATE -- `2.0.0_SA_COO~Z` -- AMGT **Peers** tab (B04 / P1)

**Authority:** Andrew-direct 2026-09-24 ~02:2xZ at the `1.0.0_SA_CTO~Z` terminal, VERBATIM: *"granted, spawn
2.0.0_SA_COO~Z. Then yes, go."* -- answering `CLOSER_PROPOSE_PEERS_20260924.md`.
**Contract:** `CONTRACT.md` (this folder), Peers row added. **Trace:**
`org/tier1_exec/4.0.0_SA_CRO/deliverables/PEERS_END_TO_END_GAP_BRIEF_20260923.md` + `.evidence.json`.
⚠ **You were NOT spawned: you are already LIVE** (measured 02:2xZ, PID 22020). No identity was created.

## FIRST ACTION -- the live thread, before anything else counts

**LIVE FIRST:** one journey, one trace artifact. Sign in -> `/security-analysis/BA_US_Equity` on the **served
stack** (bundle `d2n2nzpeqf34ge`, PROD authorizer, deployed function `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`)
-> click **Peers** -> observe identity line "BA US", the **derived** badge, **12 comparables**, counts line
**"5 present / 12 absent of 17"**. Crosses hops 1, 2, 3, 5, 7.
⛔ **A `/market` redirect is a FAILURE, not a pass.** ⛔ **No offline closure below counts toward an acceptance
ID until this passes.** **The permitted identity (`user.role==='admin'` AND `claims.userType==='Dev'`) is
Andrew's input** -- if it is not in hand, say so as a blocker and keep the rest moving.

## THE FOUR STEPS, in order

1. **THE LIVE THREAD** (above). Record request, the route's identity block, the `peer_read` record, rendered counts.
2. **ONE KEY SPACE** (hop 4, `lib/research/identity/**` -- already yours). `crosswalk.py` takes the **widened
   identity set (`universe/v1`)** as a **second registration source** beside the 89-name coverage list; re-mint
   `crosswalk/v1/<as_of>.json` with `--write-pool`.
   ⛔ **RULED BY THE CTO, DO NOT RE-OPEN: the ranker KEEPS its fall-through; the crosswalk widens to meet it.**
   Converge the route UP to the producer, never trim the producer down -- the fall-through is why 191 keys and
   **111 real derived sets** exist, and removing it destroys landed work to make two resolvers agree.
   ⛔ **REFUSED: the route must NOT accept a landed peers object's own identity block as a third surface.** That
   makes any pool key resolvable and is the guess the crosswalk's ratified text forbids. **A resolver that
   trusts the artifact it is resolving has no authority left.**
   **Proof:** `crosswalk.resolve()` over the **191** newest pool keys prints **191 MEASURED**, or a printed
   refusal list with reasons; then deployed `/peers` for `AAPL_US_Equity` returns `basis: derived` with members
   and `peer_read.status SERVED`. **Unstrands 111 sets.**
3. **CARRY THE PRESENT COLUMNS** (hop 7). **(a) frontend:** `cscTable.ts` `MEMBER_FIELD_FOR_CODE` gains
   `ey_ntm -> factors.ey_ntm`, rendered as `1 / ey_ntm` under the R-1 `display_label` (**NTM grain** -- rk-14:
   a fiscal-year label never sits over an NTM figure), with a nested-field reader in `valueOf`.
   **(b) producer (`lib/research/peers/**`, NEWLY YOURS):** copy each row's `price`, `ev`, `ey` onto the member
   row as top-level fields the map can name; re-run the batch.
   **Proof:** a served Boeing object whose members carry all five present codes, and the rendered table
   reporting **"5 present / 12 absent of 17 declared; 5 column(s) carry a per-member value"** with summary rows
   at **n=12** -- offline harness first, then the live screen.
4. **OWNER + TRIGGER FOR THE BATCH** (hop 6). You are the owner. Stated trigger: *"after each `crosswalk/v1` or
   `universe/v1` re-mint, run `python -m lib.research.peers.engine --write-pool --as-of <stamp>` over the
   current crosswalk."* Run it **once now, after step 2's re-mint**, so `6861_JP_Equity`, `CAT_US_Equity` and
   `CSL_AU_Equity` gain an object (derived, or an explicit absent).
   **Proof:** a new partition whose key set **equals** the crosswalk's MEASURED set, printed with **both**
   denominators.

## YOUR WRITE SURFACE (the CONTRACT rows you own)

`portal/src/pages/SecurityAnalysis/**` · `portal/src/api/endpoints/amgt-lead-panel.ts` · `portal/src/App.tsx`
(AMGT route rows only) · `lib/research/api/scoped_amgt.py` + the `opal-amgt-scoped-api` package ·
`lib/research/identity/**` · **`lib/research/peers/**` (NEW)**.
⭐ **The peers grant needs no `.owned-paths.yaml` edit and that is EXERCISED:** `resolve_lane` -> `BASE_EXEC`,
`check_agent(2.0.0_SA_COO~Z)` -> **True**, negative control on `org/tier0/ledger/` -> **False**. **If any
commit is refused at a path this table gives you, that refusal is a BLOCKER message, not a workaround.**

## ⛔ HALF-CHECKED IS THE TRAP HERE

**Hop 8: `PostureTab.tsx:339-347` calls `usePeerSet` for the subject AND for the comparable.** Every change in
steps 2 and 3 lands on Posture unchanged. **A fix verified on the Peers tab alone is HALF-CHECKED.** Run every
case through the **Posture comparable read** too.

## OPERATING RULES

**FILES OVER MAIL:** overwrite `STATUS.md` in place (current state, ~5 KB, not a journal) at
`org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_EXPERIENCE/`. **No ACK messages.** A message carries exactly one
of: interface published, blocker, review handoff -- each citing `path@commit`, owner, requested action, IDs.
**NO SIDE-QUESTS:** park off-thread questions as one STATUS line with owner + un-park condition.
**Commit** via `.tools/safe-commit.sh` with pathspecs, in your own worktree (14b).
⚠ **The working branch is now `CLOUD`** (ONE TRUNK, shared tree at `f534c14693`); a command naming `SITEZ`
names a branch being archived. Pull-merge before any push, **never rebase**.

**ALREADY PARKED -- do not work these:** the scanner-universe refresh (`asOf` **2026-08-06**, seven weeks old,
upstream writer unnamed) · FX for the 0.2x-5x band (22 subjects graded across currencies) · the 12 absent CSC
columns (need Bloomberg fields the scanner does not carry). **The last two are Andrew's data-source calls.**
⛔ **No vendor or Bloomberg call sits on this thread, and none is authorized here.**
