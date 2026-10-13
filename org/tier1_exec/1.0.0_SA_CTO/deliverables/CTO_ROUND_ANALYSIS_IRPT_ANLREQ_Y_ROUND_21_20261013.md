# CTO ROUND-21 ANALYSIS -- IRPT_ANLREQ (workstreams Y and YR) -- answering the round-20 L10 slug (2026-10-13 ~14:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 6987, `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_20_L9_GRADE_20261013.md`
@af5f05fd94, on the issuer's compile `ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md`. **Prior:** the round-20 analysis. **No PRD addendum.**

## 1. What round 20 did

- **Release 20 is live in all eight packagers at the signed digests** (CVO's read, 14:21Z). There are 0 TypeError, Traceback or
  ImportError lines. No function ever ran one of the three wrong irpt-holdings versions.
- **The A4 caller-class count is 0 lines.** That zero is vacuous: there is no traffic on seven functions, and none of directory-search's
  57 to 69 invocations was a cross-firm selection.
- **AR-y-211 (reader r19.2) is built, not released.**
- **AR-y-216** moved the three suites to the rule (narrative 69/0, directory-search 216/4/0, export-render 313/0). The remaining 4
  `test_read_once` failures fail on the original bytes too.

## 2. Rulings

1. **AR211-y-AC3J FAIL is upheld, and this seat's blocklist ruling is WITHDRAWN.** A 17-word attribute blocklist turns back `Acct Cost
   Basis`, `Acct Gain`, `Acct Weight` and other neighbours (the CVO ran them). A list of attribute words cannot be complete. **Rule: the
   ALLOWLIST.** A header with an account root enters the backstop only when every other word is an identifier-tail word, with
   `alias` added to the tail words and `primary` to the modifiers, so `Acct Alias` and `Primary Acct` still read as account columns.
   This is the remedy the CVO named. It was built, not released, so the fail cost nothing live.
2. **Row `W65-S4` (the status rule reaches narrative's no-selection path): covered, no action.** This seat's release-20 CTO half
   already states that narrative's no-selection path is fail-closed for a row without `status`, and that none of the 23 internal rows
   lacks one. The change refuses; it does not widen. That nobody is affected was measured before the release. The CVO dispositions the row.
3. **Row `D2-S71` (`build-and-upload.sh` exits 1 after a good upload): this project fixes it.** Its releases are the script's
   heaviest use, and a failed verify step that the applier must work around by hand is a defect in every release. One cell owns
   `infra/aws/lambda/ci/build-and-upload.sh` only. If the owned-paths gate refuses the path, that refusal names the owner, and it
   goes in as a surprise row, not as a message.
4. **The status rule is exercised by an act, not awaited.** "Callers with no row are counted when one selects another firm" is a
   wait. NO FWD IS A WAIT: drive it.
5. **Housekeeping deletions** (worker worktrees and scratch folders, compile section 5 item 5) are a recursive deletion and Andrew's
   act. This seat lists them on dell2's open calls as one act. Nothing waits on it.

## 3. ENRICHMENT LIST for round 21 (ONE issuance)

1. **Reader r19.3, the allowlist** (build only):
   - Every case of AR-y-211, plus the CVO's six neighbours, returns `[]` on one-account sheets.
   - `Acct Alias` and `Primary Acct` still read as account columns.
   - The two-account controls are still turned back.
   - The CVO's neighbour list is written into the criterion before the build.
2. **The ci script fix** (one file): an upload that lands verifies, exits 0 and updates the source map. A head-object that fails
   exits non-zero with the CLI's error printed. Two arms: a real upload to a scratch key, and a forced verify failure.
3. **The driven status-rule exercise, as a never-widen pair.** It mints identity rows for one sitting, with the R2-cw-1 shape as the
   precedent:
   - Two synthetic internal identities: one whose row is `disabled`, and one with no row (token only).
   - Each selects a firm other than its own on `irpt-directory-search`.
   - PASS: both are refused, each with one caller-class line naming its class (`row_non_active`, `row_absent`).
   - Positive control: an `active` synthetic row selecting the same firm is admitted.
   - The rows are deleted after `exp` and read ABSENT.
   - The pair is cut and signed before any mint.
4. **The r19.3 release pair (two-leg)** follows item 1. Its stored-input recount runs on a Dell CloudOps lane once the Dell
   identities' grants land (`2.0.0_SA_COO~C`, round 12, first cell). Until then it is a surprise row, never a laptop order
   (Andrew-direct, msg 6938).

## 4. Acts only Andrew can do

- The portal PROD promote that carries the sheets notice and the ticket wording (`dell1-e7f2`; card 9, his localhost smoke in progress).
- The housekeeping deletions (a new act row on dell2's list).

-- 1.0.0_SA_CTO~DELL2
