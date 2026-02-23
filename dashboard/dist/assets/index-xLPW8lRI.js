(function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))o(e);new MutationObserver(e=>{for(const i of e)if(i.type==="childList")for(const a of i.addedNodes)a.tagName==="LINK"&&a.rel==="modulepreload"&&o(a)}).observe(document,{childList:!0,subtree:!0});function t(e){const i={};return e.integrity&&(i.integrity=e.integrity),e.referrerPolicy&&(i.referrerPolicy=e.referrerPolicy),e.crossOrigin==="use-credentials"?i.credentials="include":e.crossOrigin==="anonymous"?i.credentials="omit":i.credentials="same-origin",i}function o(e){if(e.ep)return;e.ep=!0;const i=t(e);fetch(e.href,i)}})();const c=typeof location<"u"&&(location.hostname==="localhost"||location.hostname==="127.0.0.1")?"http://localhost:5000/api":"/api";async function r(n){try{return await(await fetch(`${c}${n}`)).json()}catch(s){return console.error(`Error fetching ${n}:`,s),null}}function m(n){const s=document.getElementById("fleet-container");!s||!n||(s.innerHTML=n.map(t=>`
    <div class="vehicle-item" onclick="triggerOrchestration('${t.id}')" data-vin="${t.id}">
      <div class="vehicle-info">
        <span class="vin">${t.id}</span>
        <span class="model">${t.model}</span>
      </div>
      <div class="health-bar">
        <div class="health-fill" style="width: ${t.health_score}%; background: ${t.health_score>80?"#00ff88":t.health_score>60?"#ffcc00":"#ff4d4d"}"></div>
      </div>
    </div>
  `).join(""))}let l="";function g(n){const s=document.getElementById("log-container");if(!s||!n)return;if(n.length===0){(!s.innerHTML||s.innerHTML.includes("No active"))&&(s.innerHTML='<div class="empty-state">No active orchestration tasks</div>');return}s.innerHTML=n.sort((e,i)=>i.timestamp-e.timestamp).map(e=>`
    <div class="log-entry">
      <span class="timestamp">${new Date(e.timestamp*1e3).toLocaleTimeString([],{hour:"2-digit",minute:"2-digit",second:"2-digit"})}</span>
      <span class="agent-name">[${e.agent}]</span> ${e.message}
    </div>
  `).join("");const t=n.filter(e=>e.agent==="customer_engagement_agent").sort((e,i)=>e.timestamp-i.timestamp),o=document.getElementById("sapi-container");if(o){const e=t[t.length-1];if(e&&e.message!==l){const i=document.createElement("div");i.className="chat-bubble bot",i.innerText=e.message,o.appendChild(i),l=e.message,o.scrollTop=o.scrollHeight}}}function u(n){const s=document.getElementById("audit-container");if(!(!s||!n)){if(n.length===0){s.innerHTML='<div class="empty-state">System secure. No alerts.</div>';return}s.innerHTML=n.sort((t,o)=>o.timestamp-t.timestamp).map(t=>`
    <div class="log-entry">
      <span class="timestamp">${new Date(t.timestamp*1e3).toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"})}</span>
      <span class="agent-name">${t.agent}</span> 
      <span class="status-${t.status.toLowerCase().includes("flagged")?"flagged":"approved"}">${t.status}</span>: ${t.action}
    </div>
  `).join("")}}async function d(){try{const n=await r("/vehicles"),s=await r("/dashboard/logs"),t=await r("/dashboard/audits");n&&m(n.slice(0,50)),s&&g(s),t&&u(t)}catch(n){console.warn("Poll Loop Failed:",n)}setTimeout(d,2e3)}async function f(n){console.log(`Triggering AI for: ${n}`),document.querySelectorAll(".vehicle-item").forEach(i=>i.classList.remove("active"));const t=document.querySelector(`[data-vin="${n}"]`);t&&t.classList.add("active");const o=document.getElementById("log-container");o&&(o.innerHTML='<div class="loading">Initializing agent orchestration...</div>');const e=document.getElementById("sapi-container");e&&(e.innerHTML=""),l="";try{await fetch(`${c}/dashboard/logs`,{method:"DELETE"});const a=await(await fetch(`${c}/trigger/${n}`,{method:"POST"})).json();console.log("Orchestration Response:",a)}catch(i){console.error("Trigger Failed:",i)}}window.triggerOrchestration=f;d();console.log("MECH-CHAT Premium Dashboard Initialized");
