# AMGT_RESAPP -- ROUND 88, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~02:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3396, `surprise-channel/adjudications/ADJUDICATION_v108.md` and
`surprise-channel/remediations/REMEDIATION_v33.md` @b374969da5 (MAY-CLOSE). Issuer packet:
`deliverables/2.0.0_SA_COO~R1/round88/DRAIN_END_PACKET.md` @100d91e165; issuer reads `round88_prep/ISSUER_READS.md`.

## 1. Graded

- **Round-87 item 1, the FAILED withhold: EXERCISED.** mm-1 ran the deployed reader on a planted copy: NU withheld, 0
  sentences, `withheld_failed` 1. The round-86 reader serves the planted sentence (negative arm). 4 of 4 unplanted names
  equal live. On the live function (KlosR/ap8O3..) the CVO's re-run reads AC2 YES: 5 of 5 names NO_SENTENCES.
- **Round-87 item 2, NU's empty-state card: MET on portal DEV** (e225e9e1; the CVO graded AC3 MET on its own ui-walk, row
  D1-C-S40). It is not on PROD. The Security Analysis page is Opal-internal, so the PROD promote needs no word from
  Andrew; it is round-89 item 7.
- **Round-87 items 3 and 4: MET.** mm-3 @85777c27a8 is graded MET (ADJUDICATION_v106). The set-but-missing library root now
  raises with the path named. The selector stays IGNORED under this seat's mm-4 half ADDENDUM 1 @c2b5454449.
- **Round-87 item 5, the carried rows: DISPOSITIONED.** The issuance read 17 of the 29 carried rows as `2.0.0_SA_COO~R1`'s:
  CLOSED 3, CUT 3, CARRIED 11. The packet's issuer-read check reads 7 of 7.
  - Three of those reads found producer defects: items 2-4 below.
  - Two rows closed on their reads (D1-W332-S2, Z-W212-S2). D1-S6 became D1-S19, which is now closed.
  - Z-W266-S3 stays a read (item 9).
- **mm-4, the redeploy: HOLDS.** Live CodeSha256 KlosR/ap8O3.. on the CVO's own re-run; AC2 YES, AC3 3 of 3 byte-equal to
  base. The source map records the deploy (D1-S19 closed, 4607adbfcd), and the NEVER-2 ledger is CLOSED 12 of 12.
- **Condition 4 of this seat's mm-4 half: MET on its mechanism, NOT EXERCISED against a populated list.**
  - The live read is byte-equal on 6 of 6 firms, but every list it compared was the 2-byte empty list. A filter that drops
    everything also returns `[]`, so on empty lists the equality cannot tell the two apart. Under CLAUDE.md rule 22,
    absent is not exercised-against.
  - The structural read (`scoped_amgt.py` names `selected_tenant` 0 times) shows the reader cannot branch on the selector.
    It does not cover any layer in front of the reader.
  - Nothing is reopened. Round 89 drives the populated case (item 1).

**FWD state.** This round adds exercised evidence to FWD-10 (the withhold) and DEV-only evidence to FWD-28 (empty states).
No FWD is graded REALIZED on this round alone. FWD-16 stays held by Andrew.

## 2. Graduated rows ruled

- **AMGT_RESAPP-S4 (mine): CUT as a round-89 cell (item 5).**
  - `.tools/git-hooks/mass-deletion-check.sh:111` takes `ROOT` from `--show-toplevel`, and `_audit()` (:160-165) appends to
    `$ROOT/$AUDIT_LOG`. A verdict written from a linked worktree therefore dies when that worktree is removed.
  - Build ladder rung 2: the estate already has the fix. `.tools/safe-commit.sh:177` resolves its audit root through
    `--git-common-dir`. The gate adopts that resolution for the audit path only; the gating logic is untouched.
  - The cell lands through the round-89 issuance, never as a rider on a product cell.
- **AMGT_RESAPP-S5 (`2.0.0_SA_COO~R1`'s):** carried into round 89 as item 6, with the remedy and close condition as
  REMEDIATION_v33 states them.

## 3. ENRICHMENT LIST (round 89, ONE issuance by `2.0.0_SA_COO~R1`)

1. **Condition 4 driven against a populated watchlist.** No served write.
   - Run the deployed reader at the live pin on a COPY of the watchlist store, with two firms' lists planted non-empty.
   - Per firm, an off-list `selected_tenant` reads byte-equal to the absent-selector read, and neither read carries the
     other firm's planted entry.
   - Plus one read of the request path in front of `scoped_amgt.py` (authorizer and router) for `selected_tenant`, with its
     denominator printed.
   - It is an issuer act or a LOCAL cell, mm-1 style.
2. **D1-S14:** each peer's price currency comes from the price source, not the scanner. 10 of 12 ASML peers carry none today.
3. **D1-S16:** peer members resolve through the identity pool. 12 of 12 read UNRESOLVED today, with SEDOL and numeric
   tickers.
4. **D1-S15:** the subject's market cap moves to the header's vintage, or it is dropped with its reason. Today it is dated
   2026-09-19, three weeks older than the header, and on a different vintage from its members.
5. **S4:** the mass-deletion gate's audit row lands in the shared tree. Risk LOCAL, one file, at most two criteria.
   - A gated deletion committed in a linked worktree leaves its row in the shared `org/mass-deletion-audit.log` after the
     worktree is removed.
   - Negative arm: the gate's verdict on the same deletion is unchanged.
6. **S5:** every `write_pool` caller refuses to write ABSENT over a served count. `crosswalk.py:1528` names 3 writers.
   - Close when an `add_security` run with an unreadable library root exits nonzero with no put, beside a control run that
     writes.
7. **mm-2 to PROD:** promote e225e9e1 by `/prod-deploy`. The page is Opal-internal, so no word from Andrew is needed. The
   receipt names the page and its class.
8. **AMGT_CORPUS `CRPS-at-10` leg p, STAGED.** This is the one redeploy that carries the dossier at method /11, or at /12
   if `CRPS-at-4` finds the master template.
   - It is cut in this issuance as a staged wave, under its own never-widen pair.
   - It starts when AMGT_CORPUS reports legs w and v done and `CRPS-at-4`'s master read is in. That is a dependency between
     two projects, not a wait on time.
   - It is not cut a second time in round 90.
   - Its AC carries a live hash re-read and the AC2 and AC3 re-runs from mm-4 as the no-regression arm.
9. **Issuer read: Z-W266-S3.** The driver chart serves 1 of 94 covered names. The read says whether the drafted names'
   drivers have any numeric source; a defect it finds becomes a round-90 cell.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- FWD-16: lifting his 2026-09-15 news hold.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1
