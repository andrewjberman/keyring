/** Controlled asynchronous component lifecycle; manual hooks and static markup, not a browser. */
import { afterAll, expect, test } from 'bun:test'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'
const root = process.env.IRPT_PORTAL_REVIEW_ROOT!
if (!root) throw new Error('Exact portal snapshot required')
const load = (path: string) => import(pathToFileURL(resolve(root, path)).href)
const React = await load('node_modules/react/index.js')
const { renderToStaticMarkup } = await load('node_modules/react-dom/server.js')
const { OwnedRequestHistory } = await load('src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx')
const { ProspectJobStatus } = await load('src/pages/InvestorReporting/tabs/analysis/ProspectJobStatus.tsx')
const fixture = JSON.parse(readFileSync(resolve(root, 'src/pages/InvestorReporting/__tests__/mvp-selection/tests/producer-owned-history.json'), 'utf8'))
const idA = fixture.read.identity.request_id, idB = 'REQ-' + 'b'.repeat(24)
const request = (id: string) => ({ ...structuredClone(fixture.read), identity: { ...fixture.read.identity, request_id: id } })
const report = (id: string, label = 'Retained section') => ({ requestId: id, attemptRef: 'offline',
  sections: [{ sectionRef: label, ordinal: 2, kind: 'modeled', title: label, values: [] },
    { sectionRef: 'earlier', ordinal: 1, kind: 'metric', title: 'Earlier section', values: [] }],
  extractionValidation: { validated: false, unconfirmedValueCount: 2, reasonCode: 'UNCERTIFIED' } })
const page = (ids = [idA, idB], cursor: string | null = null) => ({ items: ids.map(request), next_cursor: cursor })
const tick = () => new Promise<void>((done) => setImmediate(done))
function deferred() {
  let resolve!: (v: any) => void, reject!: (e: Error) => void
  const promise = new Promise((yes, no) => { resolve = yes; reject = no })
  return { promise, resolve, reject }
}
function nodes(tree: any): any[] {
  if (Array.isArray(tree)) return tree.flatMap(nodes)
  return tree && typeof tree === 'object' && tree.props ? [tree, ...nodes(tree.props.children)] : []
}
function text(tree: any): string {
  if (typeof tree === 'string' || typeof tree === 'number') return String(tree)
  if (Array.isArray(tree)) return tree.map(text).join('')
  return tree?.props ? text(tree.props.children) : ''
}
function harness(initialApi: any) {
  let api = initialApi, cursor = 0, dirty = true, tree: any, disposed = false, updatesAfterDispose = 0
  const slots: any[] = [], effects: any[] = []
  const internals = React.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE
  function render() {
    for (let cycle = 0; cycle < 20; cycle++) {
      if (!dirty && tree) break
      dirty = false; cursor = 0
      const pending: (() => void)[] = [], previous = internals.H
      internals.H = {
        useState(initial: any) {
          const i = cursor++
          if (!(i in slots)) slots[i] = initial
          return [slots[i], (value: any) => {
            if (disposed) updatesAfterDispose++
            const next = typeof value === 'function' ? value(slots[i]) : value
            if (!Object.is(next, slots[i])) { slots[i] = next; dirty = true }
          }]
        },
        useEffect(effect: () => any, deps: any[]) {
          const i = cursor++, old = effects[i]
          if (!old || deps.some((v, j) => !Object.is(v, old.deps[j]))) pending.push(() => {
            old?.cleanup?.(); effects[i] = { deps, cleanup: effect() }
          })
        },
      }
      try { tree = OwnedRequestHistory({ api }) } finally { internals.H = previous }
      pending.forEach((fn) => fn())
    }
    return tree
  }
  return {
    render,
    async settle() { for (let i = 0; i < 4; i++) { render(); await tick() }; render() },
    html() { return renderToStaticMarkup(render()) },
    button(label: string) { return nodes(render()).find((n) => n.type === 'button' && text(n).startsWith(label)) },
    click(label: string) { const b = this.button(label); if (!b || b.props.disabled) throw new Error('Unavailable button: ' + label); b.props.onClick(); render() },
    status() { return nodes(render()).find((n) => n.type === ProspectJobStatus) },
    change(next: any) { api = next; dirty = true; render() },
    unmount() { effects.forEach((e) => e?.cleanup?.()); disposed = true },
    get lateUpdates() { return updatesAfterDispose },
  }
}
const results: any[] = [], observations: any[] = []
function control(name: string, run: () => Promise<void>) {
  test(name, async () => {
    const fetch = globalThis.fetch
    globalThis.fetch = (() => { throw new Error('NETWORK_FORBIDDEN') }) as any
    try { await run(); results.push({ name, outcome: 'PASS' }) }
    catch (e) { results.push({ name, outcome: 'FAIL', error: String(e) }); throw e }
    finally { globalThis.fetch = fetch }
  })
}
function api(changes: any = {}) {
  return { listOwnedAnalysisRequests: async () => page(), getOwnedAnalysisRequest: async (id: string) => request(id),
    getOwnedAnalysisReport: async (id: string) => report(id), ...changes }
}

control('one bounded history page and fresh request then sections on every selection', async () => {
  const calls: any[] = []
  const ui = harness(api({ listOwnedAnalysisRequests: async (q: any) => { calls.push(['list', q]); return page() },
    getOwnedAnalysisRequest: async (id: string) => { calls.push(['request', id]); return request(id) },
    getOwnedAnalysisReport: async (id: string) => { calls.push(['sections', id]); return report(id) } }))
  await ui.settle()
  expect(calls).toEqual([['list', { limit: 25 }]])
  ui.click('Open ' + idA); await ui.settle()
  expect(calls.slice(1)).toEqual([['request', idA], ['sections', idA]])
  expect(ui.status().props.requestId).toBe(idA)
  const key = ui.status().key
  ui.click('Open ' + idA); await ui.settle()
  expect(calls.slice(3)).toEqual([['request', idA], ['sections', idA]])
  expect(ui.status().key).not.toBe(key)
  const html = ui.html(); observations.push({ name: 'actual_section_markup', html })
  expect(html).toContain('UNCERTIFIED')
  expect(html).toContain('UNSUPPORTED')
  expect(html).toContain('MODELED')
  expect(html).toContain('modeled analysis, not actual performance')
  expect(html.indexOf('Earlier section')).toBeLessThan(html.indexOf('Retained section'))
  ui.unmount()
})

control('late request from earlier selection cannot start its sections read', async () => {
  const pending = deferred(), reads: string[] = []
  const ui = harness(api({ getOwnedAnalysisRequest: (id: string) => id === idA ? pending.promise : Promise.resolve(request(id)),
    getOwnedAnalysisReport: async (id: string) => { reads.push(id); return report(id, 'current-B') } }))
  await ui.settle(); ui.click('Open ' + idA); await ui.settle()
  ui.click('Open ' + idB); await ui.settle()
  pending.resolve(request(idA)); await ui.settle()
  expect(reads).toEqual([idB])
  expect(ui.status().props.requestId).toBe(idB)
  expect(ui.html()).toContain('current-B')
  ui.unmount()
})

control('late sections from earlier selection cannot replace current sections', async () => {
  const pending = deferred()
  const ui = harness(api({ getOwnedAnalysisReport: (id: string) => id === idA ? pending.promise : Promise.resolve(report(id, 'current-B')) }))
  await ui.settle(); ui.click('Open ' + idA); await ui.settle()
  ui.click('Open ' + idB); await ui.settle()
  pending.resolve(report(idA, 'stale-A')); await ui.settle()
  expect(ui.html()).toContain('current-B'); expect(ui.html()).not.toContain('stale-A')
  ui.unmount()
})

control('same-ID reopen clears old sections and request denial prevents further report read', async () => {
  let allowed = true, reads = 0
  const ui = harness(api({ getOwnedAnalysisRequest: async (id: string) => { if (!allowed) throw new Error('revoked'); return request(id) },
    getOwnedAnalysisReport: async (id: string) => { reads++; return report(id, 'formerly-visible') } }))
  await ui.settle(); ui.click('Open ' + idA); await ui.settle()
  expect(ui.html()).toContain('formerly-visible')
  allowed = false; ui.click('Open ' + idA)
  expect(ui.html()).not.toContain('formerly-visible')
  await ui.settle()
  expect(ui.html()).toContain('This request is unavailable or access has changed.')
  expect(ui.status()).toBe(undefined); expect(reads).toBe(1)
  ui.unmount()
})

control('separate section refusal exposes no old or synthesized report', async () => {
  const ui = harness(api({ getOwnedAnalysisReport: async () => { throw new Error('expired') } }))
  await ui.settle(); ui.click('Open ' + idA); await ui.settle()
  expect(ui.html()).toContain('Report sections are not available.')
  expect(ui.html()).not.toContain('data-slot="owned-report-sections"')
  expect(ui.status().props.requestId).toBe(idA)
  ui.unmount()
})

control('empty visible page can continue and refresh clears selection and cursor', async () => {
  const calls: any[] = []
  const ui = harness(api({ listOwnedAnalysisRequests: async (q: any) => { calls.push(q); return q.cursor ? page([idA]) : page([], 'opaque-cursor') } }))
  await ui.settle()
  expect(ui.html()).toContain('No visible requests on this page. More pages are available.')
  ui.click('Next page'); await ui.settle()
  expect(calls).toEqual([{ limit: 25 }, { limit: 25, cursor: 'opaque-cursor' }])
  ui.click('Open ' + idA); await ui.settle(); expect(ui.status()).not.toBe(undefined)
  ui.click('Refresh request list'); await ui.settle()
  expect(calls[2]).toEqual({ limit: 25 }); expect(ui.status()).toBe(undefined)
  expect(ui.html()).not.toContain('data-slot="owned-report-sections"')
  ui.unmount()
})

control('replaced API ignores late history and does not carry old selected data', async () => {
  const pending = deferred()
  const ui = harness(api({ listOwnedAnalysisRequests: () => pending.promise }))
  await ui.settle()
  ui.change(api({ listOwnedAnalysisRequests: async () => page([idB]) })); await ui.settle()
  pending.resolve(page([idA])); await ui.settle()
  expect(ui.button('Open ' + idA)).toBe(undefined)
  expect(ui.button('Open ' + idB)).not.toBe(undefined)
  ui.unmount()
})

control('history failure is actionable and does not pretend to be an empty page', async () => {
  const ui = harness(api({ listOwnedAnalysisRequests: async () => { throw new Error('denied') } }))
  await ui.settle()
  expect(ui.html()).toContain('Request history could not be confirmed.')
  expect(ui.html()).not.toContain('No requests on this page.')
  expect(ui.button('Refresh request list').props.disabled).toBe(false)
  ui.unmount()
})

control('unmount guards late history request and report completions', async () => {
  for (const kind of ['history', 'request', 'report']) {
    const pending = deferred()
    const options: any = kind === 'history' ? { listOwnedAnalysisRequests: () => pending.promise }
      : kind === 'request' ? { getOwnedAnalysisRequest: () => pending.promise }
      : { getOwnedAnalysisReport: () => pending.promise }
    const ui = harness(api(options)); await ui.settle()
    if (kind !== 'history') { ui.click('Open ' + idA); await ui.settle() }
    ui.unmount()
    pending.resolve(kind === 'history' ? page() : kind === 'request' ? request(idA) : report(idA))
    await tick(); await tick()
    expect(ui.lateUpdates).toBe(0)
  }
})

afterAll(() => {
  const source = JSON.parse(readFileSync(resolve(root, 'review-source-hashes.json'), 'utf8'))
  writeFileSync(process.env.IRPT_PORTAL_REVIEW_OUTPUT!, JSON.stringify({ pin: source.pin,
    source_sha256: source.hashes, controls: results, observations,
    limitations: ['Manual hook dispatcher/async doubles/static markup, no browser or actual React scheduling',
      'Current status child mounting/issued ID/key inspected; its actual polling lifecycle not run here',
      'AnalysisTab firm/scope/revision remount key inspected separately, not end-to-end mounted',
      'Offline typed API doubles; no HTTP, persistence, live access change or integrated acceptance'] }, null, 2) + '\n')
})
