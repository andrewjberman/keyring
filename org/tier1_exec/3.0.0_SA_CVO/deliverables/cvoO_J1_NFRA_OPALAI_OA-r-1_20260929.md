# J1 (rule J) on NFRA_OPALAI OA-r-1 -- PASS, with one residual named

Grader: `3.0.0_SA_CVO~O`, 2026-09-29 ~01:0xZ. The read was taken ahead of L9 on `2.0.0_SA_COO~AI`'s ask (msg 26335),
because J1 gates OA-e-3 under Andrew's G-SCOPE word (record @f8d1103a38).

**Criterion, read from the order** (`task-orders/NFRA_OPALAI.TO-OA-r-1.asker-binding-release.md:89-92`): "judges
whether each answer's scope is the asker's own, not merely whether the tool returned without error."

## What was read

- `deliverables/0.9.0_WK_NFRA_OPALAI~10/OA-r-1_NEGATIVE_ARMS.txt` @c14f28b5ca: 41 lines, `34 passed, 2 deselected`. The
  four named arms are PASSED (lines 6-9). The 2 deselected tests are admin-path `test_portal_grant` cases, under the
  issuer's ruling on row Z-W10-S4. Neither bears on answer scope.
- `tests/test_asker_binding.py` and `app/asker_scope.py` at the live release `d287ffb346`. The test file is
  byte-identical to the transcript commit, so the transcript grades the deployed bytes.

## Per arm: is the scope the asker's own, or only an error-free return?

| arm | what the test asserts beyond "no error" | scope verdict |
|---|---|---|
| old message, wider person | refusal code, AND the fetch list is EMPTY, AND there is no `data` key, AND the audit reads `denied`, AND there is no member read | nothing served: PASS |
| reply to another chat | a served query in chat C, then a send to chat D: refused, no Graph POST (`posts.ran == []`), audited `denied` | the answer cannot leave the asker's chat: PASS |
| group chat, unprofiled member | refusal code, AND the fetch list is EMPTY, AND there is no `data`, AND the verdict is `GROUP-MEMBER-DENIED` | nothing served to a group wider than its grants: PASS |
| same chat, recent message (positive) | `data` is served and the fetch is the one key. The store holds a grant for the ASKER ONLY, so a lookup keyed on the caller would return `asker_no_profile`. The serve therefore proves the grant read is the asker's | PASS |

The discriminating cases beside the arms show the asker's grant NARROWS what the caller could read. They check scope,
not error:
- `test_group_channels_are_the_intersection`: the row is on `cha`, the intersection is `{chb}`, so the query is refused
  with no fetch.
- `test_portal_grant::test_asker_portal_scope_refuses_other_channel`.
- `test_catalog_verdict_needs_the_callers_gate_too`: both gates are required, and neither widens the other.
- `test_group_all_members_pass_and_caller_is_excluded`: the caller has no profile, and the query still serves on the
  asker's and the member's grants.

## Residual: what "the asker's own" means at this grain

At the release, an asker's scope over a portal key is:
- the catalog gate at class `opal-internal` (`resolve_asker_class` returns `("opal-internal", "")` for EVERY Opal-tenant
  asker, `asker_scope.py:223`), AND
- the caller's gate, AND
- the asker's `portal_channels`, ONLY IF the grant carries them (`:384-397`).

The grant's masters, accounts, datasets and columns do not reach a portal key. This is a documented choice (row
NFRA_OPALAI-Z-W2-S1, `:369-370`), not a defect of this release. So for an asker whose grant has NO `portal_channels`,
every answer is scoped to the whole opal-internal catalog that the caller may also read. That is the asker's own scope
exactly as the contract defines it, but it is no narrower.

If G-SCOPE means per-person narrowing, each asker's grant needs `portal_channels` before OA-e-3 switches the Analyst
on. This observation places no condition on the PASS.

**J1: PASS.**

-- 3.0.0_SA_CVO~O
