/**
 * app.js — Modular Frontend Script for Kurikulum KPT-OBE SISTEKIN 2026
 * Program Studi Sistem dan Teknologi Informasi (S1) FSTI UWG Malang
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Management (Dark / Light Mode)
    initTheme();

    // 2. Mermaid Diagram Initialization
    initMermaid();

    // 3. Live Table Search Filter (for Document Pages)
    initTableSearch();

    // 4. Live Portal Cards Filter (for index.html)
    initPortalSearch();
});

/**
 * Initialize theme from localStorage and bind toggle button
 */
function initTheme() {
    const themeToggle = document.getElementById('themeToggle');
    let currentTheme = localStorage.getItem('sistekin_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', currentTheme);
            localStorage.setItem('sistekin_theme', currentTheme);
        });
    }
}

/**
 * Initialize Mermaid diagram rendering with responsive styling
 */
function initMermaid() {
    if (typeof mermaid !== 'undefined') {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        mermaid.initialize({
            startOnLoad: true,
            theme: currentTheme === 'dark' ? 'dark' : 'default',
            flowchart: { curve: 'basis', useMaxWidth: true },
            securityLevel: 'loose'
        });
    }
}

/**
 * Live Table Search Filter for Document Pages
 */
function initTableSearch() {
    const searchInput = document.getElementById('globalTableSearch');
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        const tableRows = document.querySelectorAll('main.content table tbody tr');

        if (tableRows.length === 0) {
            // Fallback for tables without tbody
            const allRows = document.querySelectorAll('main.content table tr');
            allRows.forEach((row, idx) => {
                if (idx === 0 && row.querySelector('th')) return; // skip header
                const text = row.innerText.toLowerCase();
                row.style.display = (query === '' || text.includes(query)) ? '' : 'none';
            });
            return;
        }

        tableRows.forEach(row => {
            const text = row.innerText.toLowerCase();
            row.style.display = (query === '' || text.includes(query)) ? '' : 'none';
        });
    });
}

/**
 * Live Portal Cards Filter for index.html
 */
function initPortalSearch() {
    const portalSearchInput = document.getElementById('portalSearchInput');
    if (!portalSearchInput) return;

    portalSearchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        const cards = document.querySelectorAll('.portal-card, .card');

        cards.forEach(card => {
            const text = card.innerText.toLowerCase();
            card.style.display = (query === '' || text.includes(query)) ? '' : 'none';
        });
    });
}
