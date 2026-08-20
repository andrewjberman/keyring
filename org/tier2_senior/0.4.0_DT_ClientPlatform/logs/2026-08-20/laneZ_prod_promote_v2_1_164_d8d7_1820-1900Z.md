# /prod-deploy -- portal v2.1.164 (D8 live-edit + D7 submit form) promoted ON SITE Z per Andrew-direct @a8660806b3
**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE
**serial:** 0.4.0_DT_ClientPlatform~Z (new ~Z seat, spawned this window; lane log in the BASE folder per convention)
**window:** 2026-08-20 1822Z -> ~1900Z
**Authorization:** Andrew-direct at the CTO~Z terminal, VERBATIM "promote can be handled here, bring 0.4.0_DT_ClientPlatform~Z to handle it." -- record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_ANDREW_DIRECT_20260820_D8_PROMOTE_ONSITE_DT_SEAT.md` @a8660806b3; MSTR~Z spawn frame msg 2583.

## Result: PROMOTE COMPLETE + ACCEPTED-PENDING-GATE -- PROD = 8a96c916, tag portal-v2.1.164, acceptance (a)-(d) exercised on PROD and filed at the CTO~Z gate

- **Payload (10 commits, full origin/PROD..DEV delta, enumerated in the freeze declaration msg 2599/2600):** headline D8 live-edit modals `ccda8711` + D7 client submit form `483b896c`; riders = ui-smoke instrument chain (f524ef6e/06a327ac/125d889d/99f3282d), tickerRegistry description strip 8cbb2f86, PORTAL_LINT.FIX1 ce98e334, OPAL_ANALYST.EXP1 /market fallback 715c431f (Andrew-expedited), merge 46f127eb. Items beyond the two named surfaces stated to COO~Z/CTO~Z BEFORE GO so nothing is discovered later; CTO~Z ACK 2609.
- **Mechanics (skill exactly, site-Z adapted):** paths derived from the real workspace root (never the laptop's hardcoded form); LD-0367 pushes integrator-only -- MSTR~Z executed DEV push (origin/DEV -> 483b896c, VALGATE clean), PROD push (e27dd5fa..8a96c916, re-derived parity pre-push), each <2 min turnaround. Freeze window declared BEFORE GO (COO~Z queued -- seat dark; CTO~Z live-ACKed "no other portal writer live, measured fact not a waiver").
- **Gates, in order:** tsc -b --noEmit 0 errors; dirty `bun.lock` = one-line xlsx integrity-hash noise, cleared; local PROD re-asserted from origin (no dry-run pollution); DEV CI on 483b896c = 1/1 workflows success (32403634957, by-headSha enumeration); merge --no-ff in ephemeral worktree `.runtmp/portal-promote-20260820T183300Z` (bun install FOREGROUND 420 pkgs; author+committer my serial -- portal repo had NO committer identity on this box, scoped via env, no config change); parity `git diff origin/DEV HEAD` EMPTY; deploy.yml 32404149499 success (1/1 on 8a96c916); tag portal-v2.1.164 peeled == PROD head; served-build markers (submit-request, portal-content) present at the edge with positive control (ticket-center).
- **Acceptance (all frames READ, colour law on every one; PNGs+netlogs scratchpad `d8d7accept/`):** (a) D8 both families both directions -- internal pencil on philosophy pillar dialog + benchmark modal, partner NO affordance on both; full D8-5 write cycle on PROD: PUT 200 -> override + "masking the repo copy" notice + Reset link -> DELETE 200 -> baseline restored, server count 1 -> 0, RESIDUE NONE. (b) D7F-3 pattern on PROD: partner /submit-request renders, partner /ticket-center REDIRECTED (/market) with internal positive control landing on the board; ONE client submission 201 -> `TCK-20260820-104774ce`, ack rendered FROM cutoff_et (D7F-11 branch); row contract verified (source dashboard_form:49financial, created_by svc-ticket-form, requester = session identity, events[0].actor svc-ticket-form); board CLEANED (claim 200 + complete 200, open=0). (c) colour law holds on all 9 read frames. (d) protocol + ledger.
- **Identities:** two fresh RS256 mints (dt-promote-internal@opalinvest.dev / dt-promote-partner@49financial.test) from `opal/auth/jwt-private-key`, claims per auth-handler jwt.ts -- the exercised DE~Z D8-5/6 method; key + tokens scratchpad-only, key file shredded post-battery, 60-min exp. Pre-run controls: no-token 401 / internal 200 / partner 200 / count=0.
- **Ledger (NEVER-law gate):** `org/critical_paths/change_management/20260820T1829Z_d8d7-prod-promote-v2-1-164_deploy_completion.md` -- **ALL SIX LEGS CLOSED, entry CLOSED ~1858Z** (L5 proof: MSTR~Z 185631Z -- 618265f446 merge-base ancestor of origin/SITEZ, rode integration @1fc3643501; tip bb87fcbe94). Well inside the 4h window.
- **Step 6 note:** the portal gitlink on SITEZ was ALREADY at 483b896c via MSTR~Z's D7 close @42f789623c -- my lane commit 618265f446 carries the ledger + PROD pairing record; its subject says "bump" but the gitlink delta was empty (recorded honestly here).
- **Main tree:** DEV @483b896c throughout; worktree pruned (physical `.runtmp` residue = known Windows long-path class, gitignored, inert); cwd = workspace root.

## Rollback (if ever needed)
`git -C portal push origin e27dd5fa25dfae275f7108585c09605c866458ad:PROD --force-with-lease` via integrator + re-run deploy.yml -- rollback sha encoded in the merge message per the skill.

## Compiler Tools
| Tool + invocation | Result | Note |
|---|---|---|
| comp-which "how do I grep the repo" (A.3 exercise) | forwarder RAN; PATH 98/99 comp-tools bare | startup |
| comp-find "D8-5" org/ | 33 hits / 14223 files (5 CONFIG, 28 DOC) | located the exercised D8-5/6 method + DE~Z record @981bf28609 |
| rail-checked raw: aws secretsmanager get-secret-value opal/auth/jwt-private-key | key fetched to scratchpad, content withheld | applied-plane identity mint; no comp-tool models caller secret reach (DE~Z precedent) |
| rail-checked raw: curl serving/battery controls on www.opalinvest.dev | 401/200/200 pre-controls; PUT/DELETE/POST as recorded | live-primitive verification of my OWN deploy (Rule 20) |
| proof instruments: ui-smoke.mjs x9 runs (--token/--click/--fill/--netlog) | 9/9 rc=0, every PNG read | the D8-5/D7F-3 exercised patterns vs PROD |
| deploy_ledger.py open/close-leg x6 | L1-L4,L6 closed; L5 open on integrator | the NEVER-law completion gate |
No comp-transform/comp-routes: no component or route CHANGED at this seat -- the promote ships DEV bytes already exercised at their build seats; comp-pipescript io not applicable (no gold script; DT portal-promote lane).

## Surprises (surprise channel -- surfaced, not chased)
1. COO~Z seat DARK at freeze declaration + release (both QUEUED) -- flagged in both messages; CTO~Z measured no other live portal writer; validation awaits its wake.
2. audit-archive-invoker startup findings (site-Z cross-device baseline class, 18 rows) -- already in FINDINGS.md, not chased.
3. The spawn frame's "origin/DEV tip carries both" was true only locally -- origin/DEV was 2 behind the shared tree until the integrator push (stated in the freeze declaration; CTO~Z called the honesty correct at the gate).

## Close-out (all in-window)
- CTO~Z gate verdict 185613Z (msg 2649): **ACCEPTED (a)-(d)**, independent ref checks concur (origin/PROD == peeled tag; both surfaces present in the PROD tree; main tree on DEV). The Andrew-direct charge @a8660806b3 is DISCHARGED per the gate; wind-down/hold = MSTR~Z's call with Andrew.
- MSTR~Z L5 confirmation 185631Z: 618265f446 on origin/SITEZ; ledger CLOSED all 6 legs.

## Next
1. `[2.0.0_SA_COO~Z at wake]` validate acceptance rows (msg 2647) + freeze-release record (nothing held on it -- acceptance done at CTO~Z).
2. `[0.0.0_AB_MSTR~Z]` this log rides the next integration sweep (their word); seat disposition with Andrew.
