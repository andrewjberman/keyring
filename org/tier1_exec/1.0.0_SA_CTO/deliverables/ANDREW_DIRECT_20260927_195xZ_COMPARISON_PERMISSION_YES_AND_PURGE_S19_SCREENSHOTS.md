# ANDREW-DIRECT 2026-09-27 ~19:5xZ at the 1.0.0_SA_CTO terminal -- Comparison permission YES; purge the S19 client screenshots

**Verbatim:** "call 1 yes, call 2 definitely delete client screnshots"

## Call 1 -- YES

**The call:** may advisor firms' Comparison and Multi-Comp reports compare client portfolios against Opal's model
portfolios (P:1728413 / 1728415 / 1728315 / 1728420)?

**REC answered:** yes, for firms that already see those models in Opal's Model Portfolios view (FWD-11).

**Effect:**
- the firm reporting-permission half of `templates.json` comparison_catalog (2.0.0_SA_COO~Y 102027, item 2) is
  GRANTED on this word, scoped to the firms that see those models in Model Portfolios;
- 2.0.0_SA_COO~M validates;
- the identity half (4 read-only securities_info GETs) runs in 2.0.0_SA_COO~P's next window, as ruled at CTO 19:01Z.

## Call 2 -- PURGE from git history

**The call:** purge the S19 client screenshots from git history. The REC was "keep history"; Andrew overrode it.

**What is purged:** 34 PNGs in three folders under `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/`:

| folder | files |
|---|---|
| `prod-uiwalk-20260926.shots` | 20 |
| `prod-walk-20260926.shots` | 8 |
| `w9-round7.shots` | 6 |

**The commits that added them:**
- `9b5eed8f9d` and `4f632208c5` (both on origin/CLOUD, github.com/Opal-Capital/ajb_workspace);
- `a32823e232` (local only).

**Not in scope:** the 17 fixture-run PNGs (fixture data, S19's control).

**Consequences, stated so the execution is not a surprise:**
- The rewrite gives every commit after `9b5eed8f9d` (2026-09-26 ~03:55Z) a new hash, on both fabrics. That is 424+ on
  origin/CLOUD, plus every unpushed local commit.
- Records that cite a commit `@hash` from that span will point at the OLD hash. Blob hashes, which sign-offs verify
  with, do not change.
- The filter-repo commit-map (old -> new) is committed beside this record, so any cited hash stays resolvable.
- Every clone and worktree (laptop and site Z) must re-sync to the rewritten origin. A clone that pull-merges the old
  history back re-introduces the files, so the executor fences it.
- GitHub may keep unreferenced objects reachable by SHA until its own garbage collection. A support purge request is
  an external contact and is Andrew's to send.

**Executor:** `0.0.0_AB_MSTR` (the integrator; trunk pushes are that lane's). Execution goes through the
never-rules-gate's audited override, citing these words. The never-rebase-shared-branch law is lifted for this one act
only, by this word.
