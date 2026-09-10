// ============================================================
//  report.js  —  ตรรกะหน้ารายงาน (ทำให้เสร็จแล้ว ★)
// ============================================================
const $ = (s) => document.querySelector(s);
async function api(url) { return (await fetch(url)).json(); }
function fillTable(tableSel, statusSel, r) {
  const t = $(tableSel), st = $(statusSel);
  const thead = t.querySelector("thead"), tbody = t.querySelector("tbody");
  thead.innerHTML = ""; tbody.innerHTML = "";
  if (!r.ok) { st.className = "status " + (r.todo ? "todo" : "err"); st.textContent = (r.todo ? "🚧 " : "⚠️ ") + r.error; return; }
  const rows = r.data || [];
  if (!rows.length) { st.className = "status"; st.textContent = "ไม่มีข้อมูล"; return; }
  st.textContent = "";
  const cols = Object.keys(rows[0]);
  thead.innerHTML = "<tr>" + cols.map(c => "<th>" + c + "</th>").join("") + "</tr>";
  tbody.innerHTML = rows.map(row => "<tr>" + cols.map(c => "<td>" + (row[c] ?? "—") + "</td>").join("") + "</tr>").join("");
}
async function loadSummary() {
  const r = await api("/api/reports/summary");
  if (!r.ok) return;
  const d = r.data || {};
  if (d.members !== undefined) $("#m_members").textContent = d.members;
  if (d.titles !== undefined) $("#m_titles").textContent = d.titles;
  if (d.loans_active !== undefined) $("#m_active").textContent = d.loans_active;
  if (d.overdue !== undefined) $("#m_overdue").textContent = d.overdue;
}
async function loadAll() {
  loadSummary();
  fillTable("#popularTable", "#popularStatus", await api("/api/reports/popular-books"));
  fillTable("#overdueTable", "#overdueStatus", await api("/api/reports/overdue"));
  fillTable("#activeTable", "#activeStatus", await api("/api/reports/active-members"));
}
loadAll();
