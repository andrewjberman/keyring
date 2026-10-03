# NFRA_OPLGTW -- aged OPEN remediation rows, triaged (3.0.0_SA_CVO~O, 2026-10-03 ~22:3xZ)

Asked by the round-15 analysis @b56208fd64, section 4 item 5: "The issuer and the CVO list each one with its
owner and the condition that moves it. Rows that no condition moves are closed with a reason."

Population: the 25 OPEN rows of `remediations/REMEDIATION_v1.md` (round v1), the set the gate disclosed
at @d809704b87. Each row was re-measured at HEAD, or on the live release `af2d762970`, by this seat.

Result: 15 REMEDIATED, flipped IN PLACE in REMEDIATION_v1.md; 9 OPEN, each with an owner and a condition;
1 PROPOSED CLOSE, held OPEN until the issuer concurs. Z-S46 (v3) is also flipped REMEDIATED (@bee7c817d7: the
surprise-gate refusal branch now post-checks each gate file and prints REMAIN STAGED; verified at HEAD).

The rows change only their own clocks, per the surprise-row-gate rule:
- `remediation.state` OPEN -> REMEDIATED;
- `closed` false -> true;
- for the 6 ARMED rows (W3-S9, S61, S45, S48, W2-S10, S49), `disarm` ARMED -> DISARMED with `at`.

Each row's evidence lives HERE, not in the row.

## REMEDIATED (15)

- `NFRA_OPLGTW-W3-S2`: tests/conftest.py:18-24 sends AUDIT_PATH to a temp file (citing this row), so the suite no longer appends to the tracked audit.jsonl.
- `NFRA_OPLGTW-W3-S6`: tests/test_ratelimit.py:25-29 patches time.monotonic through monkeypatch, which restores it after each test.
- `NFRA_OPLGTW-W6-S9`: test_schwab_engine.py test_ogq1_ac02 no longer carries the 0.25 s timing assertion; it asserts the child pid, spin and sample counts and a lower lag bound, which load only loosens.
- `NFRA_OPLGTW-W3-S5`: af2d762970:app/oauth_as.py register_client writes access_state.EXPIRES_AT = now + CLIENT_IDLE_LIFETIME_SECONDS; the table TTL is on expires_at (access_state.py:47-52).
- `NFRA_OPLGTW-W3-S11`: af2d762970:app/server.py:803-812 runs _ms_guard BEFORE reading site_id (comment cites W3-S11).
- `NFRA_OPLGTW-W3-S18`: af2d762970:app/ratelimit.py:44-45 AUTH_PATHS carries /schwab/download/login and /schwab/download/callback.
- `NFRA_OPLGTW-W5-S6`: OG-o-4 (complete, drained @7a114b5d6a) closed it in code: AC2 'a 500-row page of narrow rows returns 500' PASS on the issuer re-grade.
- `NFRA_OPLGTW-W4-S10`: infra/aws/lambda/ci/build-and-upload.sh:505-519 prints an explicit SKIP for a manifest with no declared_blobs; the set -e abort path is gone.
- `NFRA_OPLGTW-S19`: .tools/halt-gate-check.sh:49-55 derives the shared root from git rev-parse --git-common-dir, so a linked worktree scans the shared inbox.
- `NFRA_OPLGTW-W3-S9`: af2d762970: resolve_tier(principal, cfg) at all five sites (guard.py:76, integrations/base.py:144, token_broker.py:156, tools.py:132; tier.py:84 defines it); tier and allowlists key on the principal (rosters by tid/oid).
- `NFRA_OPLGTW-S61`: With W3-S9: the fifth consumer, token_broker.py:156, resolves on the principal at af2d762970.
- `NFRA_OPLGTW-S45`: OG-n-1 complete; aws ec2 describe-addresses shows EIP 3.214.118.242 (eipalloc-093d97376b28d2388) on i-07dccb1615503ac99, read 22:2xZ.
- `NFRA_OPLGTW-S48`: tests/acceptance/onhost_bench.py _cap_respected reads peak_child_rss_bytes on every terminal path and grades None as not respected (OG-r-3 change 1, repair R2-b, citing S48).
- `NFRA_OPLGTW-W2-S10`: OG-r-3 change 3 grades AC4 on the ruled windows (proof VALID; the order superseded); OG-r-4 re-measured capacity on live 4231bd2ddc, SUFFICIENT (drained @7258b0d6c5).
- `NFRA_OPLGTW-S49`: With W2-S10: the attributable 5xx are carried by the ruled windows in OG-r-3 change 3.

## OPEN -- owner and the condition that moves it (9)

- `NFRA_OPLGTW-W6-S2`, owner `2.0.0_SA_COO~O`: OG-gr-3 adopts R9's measured grain, and OG-rl-5 releases it (round 16).
- `NFRA_OPLGTW-S57`, owner `1.0.0_SA_CTO~O`: The CTO rules R-OG-22 against OG-r-4 AC1 (export peak RSS flat over 25k/125k/250k rows). export.py:204 still writes the complete CSV before it serves.
- `NFRA_OPLGTW-S4`, owner `1.0.0_SA_CTO~O`: Placed with the 49F ADVI chain's owner (as Z-W13-S2), who measures the dispatch count after OG-c-1's closure.
- `NFRA_OPLGTW-S5`, owner `1.0.0_SA_CTO~O`: With S4: the 49F chain owner gates dispatch on the closure's objects.
- `NFRA_OPLGTW-W4-S12`, owner `1.0.0_SA_CTO~O`: With S4: advi-49f-gold-dispatch's owner classifies on the CHAIN terminal line.
- `NFRA_OPLGTW-W1-S9`, owner `1.0.0_SA_CTO~O`: Before LGIC_ENFORCE flips: registry rows for the three names, or an R20 register entry Andrew acknowledges (Rule 30).
- `NFRA_OPLGTW-W2-S6`, owner `1.0.0_SA_CTO~O`: The owner's word to delete the synthetic probe items (still present at Z-W20-S1, 2026-10-02), and a TTL for future probes.
- `NFRA_OPLGTW-S36`, owner `1.0.0_SA_CTO~O`: With W2-S6 (DISARMED; cleanup only).
- `NFRA_OPLGTW-W2-S8`, owner `2.0.0_SA_COO~O`: .gitattributes gains eol rules for .service, .txt, .yaml, .json, .md, .html and .jsonl (none at HEAD), or the next gateway release deploys from an LF checkout.

## PROPOSED CLOSE (1), held OPEN until `2.0.0_SA_COO~O` concurs

- `NFRA_OPLGTW-S43`: The seal inputs are durable (S42). The other cited out-of-repo paths cannot be recovered, and no act restores them, so this seat proposes closing with that reason. Any claim resting only on them stays ungraded. It is held OPEN until the issuer concurs.

-- 3.0.0_SA_CVO~O
