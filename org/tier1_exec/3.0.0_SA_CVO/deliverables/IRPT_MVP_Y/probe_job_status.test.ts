/** Offline effect/timer scheduling. Does not prove browser/React scheduling or runtime status. */
import { afterAll, expect, test } from 'bun:test'
import { createHash } from 'node:crypto'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'

const root = process.env.IRPT_PORTAL_REVIEW_ROOT
if (!root) throw new Error('An exact archived portal source root is required')
const load = (path: string) => import(pathToFileURL(resolve(root, path)).href)
const React = await load('node_modules/react/index.js')
const { renderToStaticMarkup } = await load('node_modules/react-dom/server.js')
const { ProspectJobStatus } = await load('src/pages/InvestorReporting/tabs/analysis/ProspectJobStatus.tsx')
const tick = () => new Promise<void>((done) => setImmediate(done))
const loading = { state: 'LOADING', producerState: 'RUNNING', publicReasonCode: null }
const ready = { state: 'READY', producerState: 'READY', publicReasonCode: null }
function deferred() {
  let resolve!: (value: any) => void
  let reject!: (error: Error) => void
  const promise = new Promise((yes, no) => { resolve = yes; reject = no })
  return { promise, resolve, reject }
}
function nodes(tree: any): any[] {
  if (Array.isArray(tree)) return tree.flatMap(nodes)
  return tree && typeof tree === 'object' && tree.props ? [tree, ...nodes(tree.props.children)] : []
}
function harness(api: any, requestId = 'issued-request') {
  let props = { api, requestId }, cursor = 0
  const slots: any[] = [], effects: any[] = []
  let pending: (() => void)[] = []
  const internals = React.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE
  function render() {
    cursor = 0
    const old = internals.H
    internals.H = {
      useState(initial: any) {
        const i = cursor++
        if (!(i in slots)) slots[i] = initial
        return [slots[i], (value: any) => { slots[i] = typeof value === 'function' ? value(slots[i]) : value }]
      },
      useEffect(effect: () => any, deps: any[]) {
        const i = cursor++, previous = effects[i]
        if (!previous || deps.some((value, j) => !Object.is(value, previous.deps[j]))) {
          pending.push(() => {
            previous?.cleanup?.()
            effects[i] = { deps, cleanup: effect() }
          })
        }
      },
    }
    let tree
    try { tree = ProspectJobStatus(props) } finally { internals.H = old }
    const committed = pending; pending = []
    committed.forEach((run) => run())
    return tree
  }
  return {
    render,
    html: () => renderToStaticMarkup(render()),
    async mount() { render(); await tick() },
    button() { return nodes(render()).find((node) => node.type === 'button') },
    async refresh() {
      const button = this.button()
      expect(button.props.disabled).toBe(false)
      button.props.onClick(); render(); await tick()
    },
    async change(nextApi: any, nextId: string) { props = { api: nextApi, requestId: nextId }; render(); await tick() },
    unmount() { effects.forEach((effect) => effect?.cleanup?.()) },
  }
}
const results: any[] = []
function control(name: string, run: (timers: any) => Promise<void>) {
  test(name, async () => {
    const previousSet = globalThis.setTimeout, previousClear = globalThis.clearTimeout
    const previousFetch = globalThis.fetch
    const queued = new Map<number, { callback: () => void; delay: number }>()
    const delays: number[] = []; let nextId = 0
    globalThis.setTimeout = ((callback: () => void, delay: number) => {
      const id = ++nextId; queued.set(id, { callback, delay }); delays.push(delay); return id
    }) as any
    globalThis.clearTimeout = ((id: number) => { queued.delete(id) }) as any
    globalThis.fetch = (() => { throw new Error('Network forbidden') }) as any
    const timers = {
      queued, delays,
      async fire() {
        const first = queued.entries().next().value
        if (!first) throw new Error('No pending timer')
        const [id, timer] = first; queued.delete(id); timer.callback(); await tick()
      },
    }
    try { await run(timers); results.push({ name, outcome: 'PASS', scheduled_delays: delays }) }
    catch (error) { results.push({ name, outcome: 'FAIL', error: String(error), scheduled_delays: delays }); throw error }
    finally {
      globalThis.setTimeout = previousSet; globalThis.clearTimeout = previousClear
      globalThis.fetch = previousFetch
    }
  })
}

control('LOADING makes at most twelve serial ID-only reads at five-second intervals', async (timers) => {
  const calls: any[][] = []
  const ui = harness({ getJobStatus: async (...args: any[]) => { calls.push(args); return loading },
    submitAnalysisRequest: () => { throw new Error('Unexpected submission') } })
  await ui.mount()
  for (let i = 1; i < 12; i++) {
    expect(timers.queued.size).toBe(1)
    await timers.fire()
  }
  expect(calls).toHaveLength(12)
  expect(calls.every((args) => args.length === 1 && args[0] === 'issued-request')).toBe(true)
  expect(timers.queued.size).toBe(0)
  expect(timers.delays).toEqual(Array(11).fill(5000))
  ui.unmount()
})

control('an unresolved read blocks overlap and the status button until it settles', async (timers) => {
  const pending = deferred(); let reads = 0
  const ui = harness({ getJobStatus: () => { reads++; return pending.promise } })
  await ui.mount()
  expect(ui.button().props.disabled).toBe(true)
  expect(timers.queued.size).toBe(0)
  expect(reads).toBe(1)
  pending.resolve(loading); await tick()
  expect(ui.button().props.disabled).toBe(false)
  expect(timers.queued.size).toBe(1)
  ui.unmount()
})

control('READY and refusal states stop polling after LOADING', async (timers) => {
  for (const terminal of [ready, { state: 'UNAVAILABLE', producerState: 'FAILED', publicReasonCode: 'TEST_REFUSED' }]) {
    let reads = 0
    const ui = harness({ getJobStatus: async () => ++reads === 1 ? loading : terminal })
    await ui.mount(); await timers.fire()
    expect(reads).toBe(2)
    expect(timers.queued.size).toBe(0)
    if (terminal.publicReasonCode) expect(ui.html()).toContain('TEST_REFUSED')
    ui.unmount()
  }
})

control('transport error clears old status, stops polls and explicit check restarts', async (timers) => {
  let reads = 0
  const ui = harness({ getJobStatus: async () => {
    reads++; if (reads === 2) throw new Error('Unavailable'); return reads === 1 ? loading : ready
  } })
  await ui.mount(); expect(ui.html()).toContain('Job status:')
  await timers.fire()
  expect(ui.html()).not.toContain('Job status:')
  expect(ui.html()).toContain('could not be confirmed')
  expect(timers.queued.size).toBe(0)
  await ui.refresh()
  expect(reads).toBe(3)
  expect(ui.html()).toContain('Job status: Ready')
  expect(timers.queued.size).toBe(0)
  ui.unmount()
})

control('unmount clears a pending timer without another read', async (timers) => {
  let reads = 0
  const ui = harness({ getJobStatus: async () => { reads++; return loading } })
  await ui.mount(); expect(timers.queued.size).toBe(1)
  ui.unmount()
  expect(timers.queued.size).toBe(0)
  expect(reads).toBe(1)
})

control('unmount ignores late successful and failed in-flight responses', async (timers) => {
  for (const reject of [false, true]) {
    const pending = deferred()
    const ui = harness({ getJobStatus: () => pending.promise })
    await ui.mount(); ui.unmount()
    if (reject) pending.reject(new Error('late refusal')); else pending.resolve(loading)
    await tick()
    expect(timers.queued.size).toBe(0)
    expect(ui.html()).not.toContain('Job status:')
    expect(ui.html()).not.toContain('could not be confirmed')
  }
})

control('request/API change ignores the old late response and retains new issued ID', async (timers) => {
  const old = deferred(), calls: string[] = []
  const firstApi = { getJobStatus: async (id: string) => { calls.push(id); return old.promise } }
  const nextApi = { getJobStatus: async (id: string) => { calls.push(id); return ready } }
  const ui = harness(firstApi, 'old-issued')
  await ui.mount(); await ui.change(nextApi, 'new-issued')
  expect(ui.html()).toContain('Job status: Ready')
  old.resolve(loading); await tick()
  expect(calls).toEqual(['old-issued', 'new-issued'])
  expect(ui.html()).toContain('new-issued')
  expect(ui.html()).toContain('Job status: Ready')
  expect(timers.queued.size).toBe(0)
  ui.unmount()
})

control('explicit check cancels waiting timer and resets a bounded twelve-read cycle', async (timers) => {
  let reads = 0
  const ui = harness({ getJobStatus: async () => { reads++; return loading } })
  await ui.mount(); const firstId = [...timers.queued.keys()][0]
  await ui.refresh()
  expect(reads).toBe(2)
  expect(timers.queued.has(firstId)).toBe(false)
  expect(timers.queued.size).toBe(1)
  for (let i = 1; i < 12; i++) await timers.fire()
  expect(reads).toBe(13)
  expect(timers.queued.size).toBe(0)
  ui.unmount()
})

control('missing reader and empty issued ID make no status request or timer', async (timers) => {
  const absent = harness({})
  await absent.mount()
  expect(absent.html()).toContain('Status is unavailable')
  expect(absent.button()).toBeUndefined()
  absent.unmount()
  let reads = 0
  const empty = harness({ getJobStatus: async () => { reads++; return ready } }, '')
  await empty.mount()
  expect(reads).toBe(0)
  expect(empty.html()).toContain('could not be confirmed')
  expect(timers.queued.size).toBe(0)
  empty.unmount()
})

afterAll(() => {
  const output = process.env.IRPT_PORTAL_REVIEW_OUTPUT
  if (!output) throw new Error('IRPT_PORTAL_REVIEW_OUTPUT is required')
  const paths = ['src/pages/InvestorReporting/tabs/analysis/ProspectJobStatus.tsx',
    'src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx']
  writeFileSync(output, JSON.stringify({
    pin: '940333dfcd12dd4329a35c4b3834ebb9dafa791c',
    method: 'Actual component/effect functions with manual React hook storage, deferred promises and controlled timer callbacks; static markup. No browser scheduler/runtime/status persistence proof.',
    source_sha256: Object.fromEntries(paths.map((path) => [path, createHash('sha256').update(readFileSync(resolve(root, path))).digest('hex')])),
    controls: results,
  }, null, 2) + '\n')
})
