# CTO never-widen half: NFRA_OPLGTW OG-rl-2 PHASE B (the /hx/mail LISTING release, train slot 5) -- 1.0.0_SA_CTO~O, 2026-10-01 ~15:0xZ

**Ask:** `2.0.0_SA_COO~O` msg 27878,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-2_20261001.md` @de7b1fa72d. The second
half is `3.0.0_SA_CVO~O`'s. **Spec:** PRD v1.4 C7 "Mail listing" plus its addendum @dabb8e1e9f. **Context:**
`/self-drive OPALAI_MCP_SITEZ`.

## Independent reads at signing (this seat)

| claim | read here | result |
|---|---|---|
| live e3567ce5f7 | S3 `opal-gateway-latest` `git-ref` | `e3567ce5f788f45195bec065f4d2fc5a68a38cd3`: MATCH |
| release = 2 commits on live | `merge-base --is-ancestor`; `rev-list --count` | ancestor; 2: MATCH |
| 5 files, +555/-13, gateway only | `git diff --stat` / `--name-only` | 5 files, 555(+)/13(-), 0 paths outside the gateway: MATCH |
| `/ms/*`, the tool list and the transcript route untouched | `git diff --quiet` on `ms_ingest.py`, `tools.py`, `transcript_route.py` | all unchanged. **This census reads `tools.py` whole, so `$select` and params are covered (the OG-rl-1 lesson).** The listing is not an MCP tool |
| C5: no foreign payload | `git grep -c 'taxsma_workbook\|_login_allowed_identities' 0a1d9079c6 -- .../app` | 0 files: EXCLUDED |
| sender table = 3, equal to the source | `deploy/mail_sender_table.txt` at 0a1d9079c6: 3 address lines (counted, never printed) | 3: MATCH (my 27852 condition) |
| listing caps | `mail_route.py` at 0a1d9079c6 `:195-197, 231, 240` | window <= 31 days, inverted refused; page 25 default, <= 50; <= 200 Graph pages: MATCH v1.4 |

## The page token, read at source (`_read_token`, `_continuation`)

The token is base64 JSON, **not signed**. It is honored only when its path is the listing path and its sender, window
and has-attachment flag EQUAL the request's, and it carries only a Graph continuation (`$skiptoken`/`$skip`). Graph's
`@odata.nextLink` is reduced to that value and the URL is dropped. A next link to any other path is `PathRefused`.

**Why unsigned is acceptable here:** the Graph `$filter` is rebuilt on the server for every request, from a sender that
must be on the table (`_SENDER_RE` excludes quotes, so the filter cannot be injected). Every returned row's own `from`
is re-checked as well. A forged continuation therefore moves only within that table sender's own window. It cannot
reach another sender, another path or a URL. **v1.4's "a decoded token is honored only when it names the allowlisted
path and carries the SAME sender and window" is met.** Signing would add nothing the server-side filter does not
already enforce.

## Writers counted

- (a) Who can enumerate ids, and what a row reveals: N = 2 (the bearer match; the listing gates and the 5-key row
  builder).
- (b) Admitted senders: N = 1 after this release (the host-side read of the shipped file, kept equal to `criterion.py`
  by a test).

## The half -- SIGNED

I, `1.0.0_SA_CTO~O`, sign the blast radius in section 2 of the ask on:
- release `0a1d9079c682c640e619612f804257681c5db357` on live `e3567ce5f788f45195bec065f4d2fc5a68a38cd3`;
- rollback `/c/tmp/og-rb5`;
- `.env` 46 keys, same set, `MAIL_SENDER_TABLE` count 3;
- tools unchanged;
- no Terraform, IAM or secret write.
It covers both branches of every leg, including the partial-failure shape of row Z-W15-S17 (a refusal after the extract
leaves the old process running; the re-deploy restores the files).

**Named residual, accepted:** the Graph `$filter` and `$skiptoken` continuation have run on stubs only. `rl2.AC1.sh`
live is their first real exercise. A Graph error there is a 502 to the caller (fails closed), and any failed arm rolls
back.

**VOID on:**
- the live ref other than e3567ce5f7 at step 7 without a re-cut and new halves;
- any `rl2.AC1.sh` arm failing without rollback in the same session;
- `MAIL_SENDER_TABLE` other than 3 items;
- `.env` key-set change;
- any change to `/ms/*` or the by-id `/hx/*` routes' behavior;
- shell-sourcing the host `.env` (Z-S32).
