import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const ctx = await b.newContext({ viewport: { width: 412, height: 915 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, locale: 'fr-FR' });
const p = await ctx.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
await p.goto('http://localhost:8765/index.html', { waitUntil: 'networkidle' });
await p.waitForTimeout(600);
const shots = [];
// --- Séance (aujourd'hui samedi = repos -> ouvrir J1)
await p.click('[data-open="J1"]'); await p.waitForTimeout(200);
await p.screenshot({ path: '/home/claude/app-seance.png' });
// saisir une série : poids via +, reps via +, cocher
const first = p.locator('.exo').first();
await first.locator('.set').first().locator('input[data-f="w"]').fill('16');
await first.locator('.set').first().locator('button[data-d="r"][data-v="1"]').click({ clickCount: 10 });
await first.locator('.set').first().locator('[data-done]').click();
await p.waitForTimeout(300);
const timerVisible = await p.locator('#timer').isVisible();
const t1 = await p.locator('#timer-t').textContent();
await p.screenshot({ path: '/home/claude/app-seance-2.png' });
// persistance : recharger et vérifier que la série est toujours là
await p.reload({ waitUntil: 'networkidle' }); await p.waitForTimeout(400);
const w = await p.locator('.exo').first().locator('.set').first().locator('input[data-f="w"]').inputValue();
const r = await p.locator('.exo').first().locator('.set').first().locator('input[data-f="r"]').inputValue();
const done = await p.locator('.exo').first().locator('.set').first().locator('[data-done]').getAttribute('class');
// terminer la séance
await p.click('#finish'); await p.waitForTimeout(300);
const hist = await p.locator('.card:has(h3:text("Historique")) .rowline').count();
// --- Repas
await p.click('[data-tab="repas"]'); await p.waitForTimeout(200);
await p.locator('.meal .cb').first().click(); await p.waitForTimeout(150);
await p.screenshot({ path: '/home/claude/app-repas.png' });
const mealTitle = await p.locator('.top h1').textContent();
// --- Courses
await p.click('[data-tab="courses"]'); await p.waitForTimeout(200);
await p.locator('.item .cb').nth(0).click(); await p.locator('.item .cb').nth(1).click(); await p.waitForTimeout(150);
const sub = await p.locator('.top .sub').textContent();
await p.screenshot({ path: '/home/claude/app-courses.png' });
// --- Suivi
await p.click('[data-tab="suivi"]'); await p.waitForTimeout(200);
await p.fill('#poids', '69,8'); await p.click('#save-poids'); await p.waitForTimeout(200);
const verdict = await p.locator('.verdict .eyebrow').textContent();
const prog = await p.locator('.card:has(h3:text("Progression")) .bar').count();
await p.screenshot({ path: '/home/claude/app-suivi.png' });
// persistance globale
await p.reload({ waitUntil: 'networkidle' }); await p.waitForTimeout(300);
const tab = await p.locator('#tabs button.on').textContent();
const poidsKept = await p.evaluate(() => JSON.parse(localStorage.getItem('carnet.v1')).poids);
const scrollX = await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
console.log(JSON.stringify({ timerVisible, t1, apresReload: { w, r, done }, historique: hist, mealTitle, courses: sub, verdict, barresProgression: prog, ongletRetenu: tab, poidsKept, scrollX, erreurs: errs }, null, 1));
await b.close();
