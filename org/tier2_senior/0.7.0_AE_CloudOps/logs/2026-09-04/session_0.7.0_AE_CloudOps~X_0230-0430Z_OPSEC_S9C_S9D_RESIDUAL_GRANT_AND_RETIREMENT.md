# Session log -- 0.7.0_AE_CloudOps~X -- 2026-09-04 02:30-04:30Z -- NFRA_OPSEC202609 TO-OP-S-9C + TO-OP-S-9D

**archetype:** MIXED

**Seat:** `0.7.0_AE_CloudOps~X` (site-z)
**Task orders:** `NFRA_OPSEC202609.TO-OP-S-9C` (the trade-pipeline residual grant) and
`NFRA_OPSEC202609.TO-OP-S-9D` (the retirement Andrew authorised) -- both cell `OP-s-9`
**Commits:** `74ba6ddc86`, `4ac21b4ae0`, `aabf8ca2e9`, `227140aad3`, `051d5034c0` (+ this log)
**Continues:** `session_0.7.0_AE_CloudOps~X_0000-0230Z_OPSEC_S9_11_LEGACY_USERS_AND_TOKEN_BINDING.md`

---

## Current state

**`OP-s-9` IS CLOSED AND `FWD-9` IS SERVED.** Both task orders are terminal with VALID
proof-of-spec instances (`rc=0`, first run each).

- **`TO-OP-S-9C`** -- ACCEPTED by `2.0.0_SA_COO~Z` on its own run. Four PASS and
  `S9C-AC4` `UNCOMPUTABLE-BY-CONSTRUCTION`. **`opal-users` went UNGRANTED estate-wide:
  2 → 1 → 0 exact grants across three censuses at this seat.**
- **`TO-OP-S-9D`** -- the legacy `opal-users` table is **DESTROYED**, through Terraform,
  on Andrew's word (*"Recs approved"*, 2026-09-04 ~03:4xZ). `describe-table` returns
  `ResourceNotFoundException`; the unscoped re-plan proposes **0 to add**; login is
  byte-identical before and after; the snapshot survives with the data.

## What was done

**S9C's whole discipline was that "no trade code names it" is a SOURCE claim about seven
functions whose deployed bytes may be older than the repo.** So the question went to the
artifacts AWS actually serves: **7 of 7 pulled and content-scanned, 0 unscannable, 0
naming the table**, with the positive control firing on the same artifacts
(`trade-auth-handler` carries `opal-users-v2` five times). Then the gap a byte scan
*structurally cannot see* -- a table name supplied at runtime -- was closed by reading
**env vars on 7 of 7**; the only users-table pointer is `USERS_TABLE=opal-users-v2`.
CloudTrail was **disqualified rather than cited**: neither trail records DynamoDB data
events and Lake is empty, so a "no access" reading would have been vacuous.

**S9D was executed as the method the ruling specified**: the declaration removed and
**Terraform performed the destroy**, so state and world moved together. Pre-act re-reads
at the vintage of the act (not inherited): snapshot AVAILABLE 12 items / 4,506 bytes,
table **12 of 12 rows UNMOVED**. The destroy plan was read as its own artifact and showed
**exactly one resource destroyed**.

## Blockers

**None.** `OP-s-9` is closed. The one open item at this seat is a **placement decision
that is not mine**: row `Z-S127`, the cleartext JWT secret, held ARMED with its two sizing
facts delivered.

## Next steps

- **[`2.0.0_SA_COO~Z`]** Route `Z-S127`. Both facts are supplied: it **is** wired as a live
  authorizer (API `w8jnzvs21g`, HMAC over a 2-part token, with a hardcoded fallback
  default) but **unexercised for 129 days**, and the live trades path uses the RS256
  authorizer instead; and **at least 9 roles** can read it, 6 of them unscoped -- a floor,
  not a count.
- **[whoever applies `trade-pipeline`]** That root needs a `jwt_secret` with no default;
  a wrong value silently rewrites a live signing secret across six Lambdas. Its README
  documents the `secrets.auto.tfvars` route.

## Errors and corrections at this seat

- **I introduced the "seven LIVE lambdas" premise and it was wrong** (row `Z-S130`). It came
  from a `lambda.Role` **attachment** census; attachment is not liveness and I never asked
  the second question. It travelled into the face title and into a COO ruling whose
  observation branch then **could never have been satisfied**. Five of the seven are dormant
  51-129 days. **Owning it in a row before acting is what let it be fixed in one turn.**
- **A broken probe nearly shipped as a finding.** An intermediate CloudWatch Logs query
  returned `NO-EVENTS` for all seven functions **including the two known-live ones**. It was
  caught only because two of the seven had a known answer. A broken probe and a true absence
  are byte-identical; the control is the only thing that separates them.
- **I built one commit-message file with `printf`** (CLAUDE.md 14a forbids exactly that).
  Caught before the commit and rewritten with a non-shell writer.
- **The rail refused three of my commands and was right each time** -- two `comp-*`-into-`head`
  pipes that would have erased a denominator, and a raw `find`. Where I did use a raw `aws`
  read, it carried a `# rail-checked:` marker naming why the comp-tool could not answer that
  grain.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-iam refresh-census` | three runs: 00:26:29Z, 02:52:43Z, 03:45:22Z | The APPLIED-plane instrument throughout. Traced the grant population **2 → 1 → 0** with the positive control returning 4 roles for the v2 ARN on *every* run, and it is what found this face's subject in the first place. Discloses its own blind spot -- **174 attached-managed statements UNRESOLVED** -- which travels with every quotation of the result. |
| `comp-routes auth-map` | `comp-routes auth-map` | Placed `/api/general/trades/*` behind edge JWT + an API-GW authorizer while **disclosing on its own face** that its API-GW auth is derived from origin TYPE and not from an authorizer's existence. That disclosure is precisely why the follow-up (*which* authorizer) went to the live plane under a rail-checked marker instead of being answered from the tool. |
| `comp-read` | `--for` on the trade-pipeline README; `--enumerate` on `portal-auth/dynamodb.tf` | The README read placed the runbook residual where a diagnosing reader meets it -- and surfaced an **independent third corroboration** of `Z-S130`: the README already recorded `trade-submission-handler` as COLD, 0 inv/90d, written months ago by someone else. The `dynamodb.tf` enumerate is what established the table was still terraform-managed, which is the single fact that shaped S9D's whole method. |
| `comp-find` | `'opal-users($\|[^-])'` over the trade trees | The SOURCE census: 2 hits across 302 files, both being the grant lines themselves. Recorded deliberately as the **weakest** leg -- it is the claim this face was cut to refuse taking at face value, and it was superseded by the deployed-bytes read rather than relied on. |

## Evidence discipline worth carrying

**The strongest move of these two faces was refusing an oracle rather than using one.**
CloudTrail would have returned "no access" and read as powerful evidence for removal. Asking
first *what it would show if the grant WERE in use* -- the same nothing -- disqualified it in
one step. **An instrument whose output is identical under a hypothesis and its negation is not
an oracle, and the only way to notice is to ask before you read it, not after.**

**Answering on the deployed bytes removed an inference step the face had budgeted for.** The
criterion asked for deployed-vs-build-input parity *so that* a source census could transfer.
Asking the deployed artifacts directly meant there was no transfer to justify: production was
the thing examined. **When a criterion specifies a route to an answer, check whether the answer
is directly reachable -- the specified route is usually a workaround for an instrument the
author assumed you lacked.**
