# NFRA_OPLGTW task order -- `OG-en-8` -- the muse-only narrowed OAuth client: M365 mail and Teams tools (read and send) plus whoami, nothing else (round 38 E8; CTO msgs 34775 and 34800; Andrew-direct 2026-10-16 ~06:5xZ and ~07:0xZ)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-8</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-8</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~121</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order with its own never-widen ask (a NARROWING of an identity).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the narrowing lives in the gateway's entitlement code, keyed by OAuth client.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew's word, relayed verbatim by the CTO: "ok i want the COO~O to have this work folded in to OPLGTW" (record `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261016_065xZ_MUSE_GATEWAY_SCOPE_FOLDS_INTO_OPLGTW_COO_O.md` @66f25c55e2) and "im fine with muse having full access for now, ultimately it should just have m365 teams/emai, but we can get there" (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_070xZ_MUSE_FULL_GATEWAY_ACCESS_FOR_NOW_M365_TEAMS_EMAIL_TARGET.md` @adb8e79330), the CTO's ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_MUSE_ON_OPALGATEWAY_20261016_Z.md` @d5be3853aa ruling 1) and the CRO's scope (`@6e57b47a6a` section 5, route C), cut by the CTO's round-37 analysis (E8).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-8` (decomposition addendum R3-T.93, round 38 item E8, workstream ENRICH-R38, FWD-22)

WHAT IT IS. A client-keyed NARROWING of an otherwise unscoped identity. The muse application's OAuth client may reach ONLY the Microsoft 365 mail and Teams tools of the Opal gateway (both read and send) plus `whoami`, and no other source. Until the release that carries this code lands, muse keeps full gateway access (Andrew: "for now"); Andrew's own client keeps exactly what it has today; every other principal is unchanged. This cell BUILDS the narrowing and its offline tests; the never-widen ask (a narrowing: a half each from the CTO, COO and CVO) and the release are later applier orders.

READ FIRST, and answer in your report: (1) where the client-to-tool narrowing can live -- `app/data_entitlement.py` (`decide()`, `TOOL_CLASSES`, the tier lists), the access layer (`app/access_state.py` or the module that resolves a principal's tier and profile from the token), and how the token's OAuth client id reaches `decide()` (find the claim the gateway already reads, `azp` or `appid`; read it, do not guess; the client ids are configuration and no id appears in code or in your report: read them from the settings/env mechanism the gateway already uses, add one new optional setting `MUSE_CLIENT_ID` in the same form if none exists); (2) whether it is a tier list or a per-client allowlist (build the per-client allowlist: a principal whose token client equals the configured muse client id is admitted only to the allowlist); (3) the allowlist names the M365 mail and Teams tools by their REGISTERED names: read `app/tools.py` and the registry; list them in your report, read AND send (mail: list, read, search, filtered list, attachments, reply, send, create draft; Teams: teams, channels, chats, channel and chat messages, send channel and chat message, polling of addressed messages) plus `whoami`; do NOT type a list from memory and do NOT include any Schwab, Black Diamond, portal, harvest, ETF, MDPF, news, ycharts, graph or catalog tool; (4) the admission class of every tool it leaves reachable is the one the PRD rules (client data is data-grant class and master_admin only, PRD v3.1 Ruling 2 and v3.14), which is unchanged here.

BUILD. In the gateway app only: when the token's client equals the muse client id (and the setting is configured), `decide()` (or the layer that calls it) denies every tool outside the allowlist with the gateway's existing denial shape (`entitlement_denied`) BEFORE any data read, and `visible_tools`/tool listing for that client shows only the allowlist. When the setting is unset or empty the behaviour for every client is exactly today's (the narrowing is inert until configured: this is what lets the code ship before the configuration act). Do not change any tool's own admission class and do not touch the five `client_*` or Schwab sets.

TESTS (new file `tests/test_og_en8.py`; read `tests/test_og_bd3.py` and `tests/test_og_ad1.py` for the fixture style):
- `test_ogen8_ac01`: with the muse client configured, a principal whose token client is the muse client is refused a Schwab tool, a portal tool and a harvest tool (each `entitlement_denied`, zero reads) and is admitted to one mail tool, one Teams tool and `whoami`.
- `test_ogen8_ac02`: negative control on the same tools: a principal whose token client is ANOTHER client (Andrew's) passes the Schwab, portal and harvest tools exactly as before, and the muse allowlist is exactly the registered M365 mail and Teams tool names plus `whoami` (the test derives the expected names from `app/tools.py`).
- `test_ogen8_ac03`: with the setting UNSET, every tool's verdict for every principal equals the pre-change verdict (compare over all registered tools for the muse and the other client).
If a test elsewhere pins a set this changes, update it to the new truth with the smallest edit and name it; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no grant, no registry change. No client id, tenant id, e-mail address or person's name in any file or in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/access_state.py
infra/aws/ec2/opal-gateway/app/tier.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_og_en8.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_og_bd3.py
infra/aws/ec2/opal-gateway/tests/test_og_ad1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `tests/test_og_en8.py` and the gateway app files only as far as the narrowing needs (smallest change; `app/tools.py` you only READ unless a registration helper must change), and existing entitlement tests only to follow the new truth; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~121/`. Rows: id `NFRA_OPLGTW-Z-W121-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en8.py test_ogen8_ac01 test_ogen8_ac02 test_ogen8_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~121 '^infra/aws/ec2/opal-gateway/(app/(data_entitlement|access_state|tier|server|config|tools)\.py|tests/(test_og_(en8|bd3|ad1)|test_data_entitlement_family|test_data_entitlement_guard|test_entitlement_admin)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~121: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass: muse refused outside the allowlist, Andrew's client unchanged, the setting unset changes nothing. `AC2`: the commits of this serial touch only the entitlement code and tests named.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-8.muse-narrowed-client.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the answers to READ FIRST (1) to (4) with the allowlist tool names, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO round-37 analysis, E8), workstream ENRICH-R38 (decomposition addendum R3-T.93). Source draft `DRAFT_NOT_ISSUED_TO-OG-mu-1_muse_narrowed_client.md` (held until `OG-ap-23` released; it has, so it is cut now as the CTO ruled). WORLD-class later: the release carries a never-widen ask for a NARROWING of an identity (halves: CTO, COO, CVO) and a configuration act that sets `MUSE_CLIENT_ID` on the host; the served read is one real Schwab call and one portal call by muse's client REFUSED, Andrew's client passing (negative control). This cell is code and offline tests only.
- Risk WORLD by the L6 floor (a gateway infrastructure path); the entitlement code is admission-sensitive, so the issuer reads the diff before the drain and the CVO reads the narrowing at the ask.
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>complete</status>
<round>38</round>
<workstream>ENRICH-R38</workstream>
<slot>~121</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
