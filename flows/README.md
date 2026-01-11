## Available Flows
- [T2I V4](./T2I%20V4/) — ComfyUI: ≥ 0.6.0 (verified on 0.8.2)

---

## Known Limitations & Performance Notes

### Initial Load & Caching
- Large workflows may require a significant initial startup time, especially after:
  - a fresh ComfyUI start
  - version updates
  - driver or backend changes
- First-time execution at high resolutions can take **20+ minutes**, as kernels, models, samplers, and tensor shapes are cached.
- Subsequent runs are **significantly faster** once the cache is populated.

---

### VRAM Usage & OOM Behavior
- High-resolution runs (e.g. 1920×1080) with multiple samplers and post-processing stages may cause **short, recoverable out-of-memory (OOM) events**.
- These OOMs are expected under peak load and usually **do not crash ComfyUI**.
- Reducing batch size or disabling optional post-processing stages can lower peak VRAM usage if needed.

---

### Resolution & Aspect Ratio
- Different resolutions and aspect ratios trigger **separate shape-specific caches**.
- Running the largest or most demanding resolution first is recommended to maximize cache reuse.
- Smaller resolutions benefit from previously cached components but may still require brief warmup.

---

### Browser Performance
- Very large workflows can temporarily **block the browser UI** after loading.
- Allow up to **1 minute** for the interface to fully settle before interacting.
- This is a frontend limitation and does not indicate a crash or freeze.

---

### Stability Expectations
These workflows prioritize:
- reproducibility
- seed stability
- modularity  

…over minimal node count or instant feedback.

They are intended for **advanced users** and production-style iteration, not quick one-click generation.

---

### Tested Environment
*(Optional – adjust to your setup)*

- **GPU:** AMD Radeon RX 7900 XT  
- **Total VRAM:** 20,464 MB  
- **Total System RAM:** 65,486 MB  
- **PyTorch:** 2.10.0a0+rocm7.10.0a20251120  
- **AMD Architecture:** gfx1100  
- **ROCm Version:** 7.10  
- **VRAM State:** HIGH_VRAM
