const citations = {
 tmi: `@article{zhao2026pelvic,
  title = {Pelvic Fracture Reduction Planning via Joint Shape-Intensity Reference},
  author = {Zhao, Xirui and Xiao, Deqiang and Zhang, Teng and Shao, Long and Ai, Danni and Fan, Jingfan and Fu, Tianyu and Lin, Yucong and Song, Hong and Wang, Junqiang and Yang, Jian},
  journal = {IEEE Transactions on Medical Imaging},
  year = {2026}, volume = {45}, number = {4}, pages = {1352--1368},
  doi = {10.1109/TMI.2025.3621670}
}`,
 cmig: `@article{zhao2026defect,
  title = {Defect-adaptive landmark detection in pelvis CT images via personalized structure-aware learning},
  author = {Zhao, Xirui and Xiao, Deqiang and Zhang, Teng and Fan, Jingfan and Ai, Danni and Fu, Tianyu and Lin, Yucong and Shao, Long and Song, Hong and Wang, Junqiang and Yang, Jian},
  journal = {Computerized Medical Imaging and Graphics},
  year = {2026}, volume = {127}, pages = {102693},
  doi = {10.1016/j.compmedimag.2025.102693}
}`
};
const dialog = document.getElementById('citation-dialog');
const citationText = document.getElementById('citation-text');
const status = document.getElementById('copy-status');
document.querySelectorAll('[data-citation]').forEach(button => button.addEventListener('click', () => {
 citationText.textContent = citations[button.dataset.citation]; status.textContent = ''; dialog.showModal();
}));
document.getElementById('close-citation').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if(event.target === dialog) { const r=dialog.getBoundingClientRect(); if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom) dialog.close(); } });
document.getElementById('copy-citation').addEventListener('click', async () => {
 try { await navigator.clipboard.writeText(citationText.textContent); status.textContent = 'Copied to clipboard.'; }
 catch { const range=document.createRange(); range.selectNodeContents(citationText); const selection=window.getSelection(); selection.removeAllRanges(); selection.addRange(range); status.textContent='Text selected. Press Ctrl+C (or ⌘C) to copy.'; }
});
