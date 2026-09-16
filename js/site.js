(() => {
  const root = document.documentElement;
  let preference;
  try { preference = localStorage.getItem('aditya-theme'); } catch (_) {}
  root.dataset.theme = preference || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.theme-toggle');
    const refresh = () => {
      const dark = root.dataset.theme === 'dark';
      button.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} mode`);
      button.setAttribute('aria-pressed', String(dark));
    };
    refresh();
    button.addEventListener('click', () => {
      root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('aditya-theme', root.dataset.theme); } catch (_) {}
      refresh();
    });
  });
})();
